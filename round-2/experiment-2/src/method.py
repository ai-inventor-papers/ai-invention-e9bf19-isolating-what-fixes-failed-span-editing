#!/usr/bin/env python3
"""Condition B fidelity check: faithful masked-fill baseline (Padmanabhan 2025 SURREYPAI-S2).

Reproduces the masked-fill baseline (Algorithm 1) on the WMT25 Task 3
en-zh_CN / en-cs_CZ experimental_pool rows using google/gemma-3-12b-it as the
forced substitute repair model (Unbabel Tower-Plus-9B is confirmed absent from
OpenRouter -- see the dossier dependency), then gates the reproduction against
Padmanabhan's documented failure signature: negative ΔCOMET of comparable
direction/magnitude plus non-trivial leakage of masking artifacts into the
repaired text.

Baseline vs. proposed method: this artifact is itself a sanity-check gate, so
"baseline" is the untouched original hypothesis (delta measured relative to
it) and "method" is condition B's masked-fill edit. Both are scored with the
identical COMET call in the same pass to eliminate scorer-side confounds.
"""

from __future__ import annotations

import argparse
import asyncio
import gc
import json
import os
import random
import re
import resource
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any

import aiohttp
from huggingface_hub.errors import HfHubHTTPError
from loguru import logger
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

# --------------------------------------------------------------------------
# Setup: logging, resource limits, paths
# --------------------------------------------------------------------------
ROOT = Path(__file__).parent
Path("logs").mkdir(exist_ok=True)
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Container RAM budget: full_data_out.json is ~29MB on disk; parsed Python
# objects run 3-6x that. Cap well under the 28GB container limit.
RAM_BUDGET_BYTES = 8 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))

DATASET_DEP = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
)
FULL_DATA_PATH = DATASET_DEP / "data_out" / "full_data_out.json"
MINI_DATA_PATH = DATASET_DEP / "data_out" / "mini_data_out.json"

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/responses"
OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"
AII_COST_LEDGER = os.environ.get("AII_COST_LEDGER")

HF_TOKEN = os.environ.get("HF_TOKEN")

RNG = random.Random(20260901)

# --------------------------------------------------------------------------
# Experiment configuration (from artifact_plan + resource-dossier dependency)
# --------------------------------------------------------------------------
LANG_PAIRS = ["en-zh_CN", "en-cs_CZ"]
REPAIR_MODEL = "google/gemma-3-12b-it"
# Ranked substitutes from the dossier (Block B), tried in order if the primary
# repair model is unavailable/rate-limited on OpenRouter at execution time.
REPAIR_MODEL_FALLBACKS = [
    "qwen/qwen-2.5-7b-instruct",
    "mistralai/mistral-nemo",
    "meta-llama/llama-3.1-8b-instruct",
    "mistralai/ministral-8b-2512",
]

COMET_MODEL_PRIMARY = "Unbabel/wmt22-cometkiwi-da"  # organizer-footnoted scorer, gated CC-BY-NC-SA-4.0
COMET_MODEL_SECONDARY = "Unbabel/wmt22-comet-da"  # same license family, distinct repo
# HF Hub download budget: this run observed a persistent, account-wide 429 on
# EVERY huggingface.co/api/models/* call (including fully public repos like
# bert-base-uncased) -- see method_out.json metadata.hf_probe_log. That is
# infra-level throttling from concurrent sibling AI-Inventor runs sharing this
# host's HF token/IP, not a per-repo gate issue. Retry with backoff for a
# bounded wall-clock budget before falling back.
HF_DOWNLOAD_MAX_WAIT_S = 600.0
HF_DOWNLOAD_BACKOFF_START_S = 20.0
HF_DOWNLOAD_BACKOFF_CAP_S = 90.0

SOFT_COST_CAP_USD = 6.0
HARD_COST_CAP_USD = 6.5

# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled
# with WMT25 organizer Table 15 (dossier Block A). Only Czech and Ukrainian
# are individually quoted in the dossier; Chinese has no pinned per-pair
# figure, so it falls back to the documented pooled range as the plan directs.
PUBLISHED_DELTA_COMET = {
    "en-cs_CZ": -0.00724,
    "en-zh_CN": None,  # no per-pair figure in the dossier -> use pooled/range fallback below
}
PUBLISHED_POOLED_DELTA_COMET = -0.0108
PUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A
MAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)

# Masking placeholder. The dossier's Block A confirms the *rule* (Algorithm 1)
# verbatim but research_out.json's machine-readable answer field does not
# carry the literal prompt string retrievable at execution time -- only its
# shape (single blank token per sentence, per-sentence call). This
# reconstruction follows that documented shape and Appendix B's own leakage
# vocabulary ("__BLANK__" / "Corrected words:") so a faithful bug reproduction
# is possible; the substitution is logged explicitly in method_out.json.
MASK_TOKEN = "__BLANK__"
MASKING_PROMPT_TEMPLATE = """You are repairing a machine-translated sentence. Some words or phrases in the
translation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.

Using the original English source sentence for reference, replace every occurrence of {mask_token} in the
translation with the correct words so the translation is fluent and faithful to the source. Preserve every part
of the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not
explain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.

English source:
{source}

Translation with blanks:
{masked_sentence}

Repaired translation:"""

LEAK_PATTERNS = [
    re.compile(r"__BLANK__"),
    re.compile(r"__\w+__"),
    re.compile(r"(?i)corrected words?\s*:"),
    re.compile(r"(?i)here is the (corrected|fixed|revised)"),
    re.compile(r"(?i)^(sure|okay|here's|here is)\b"),
    re.compile(r"\[MASK\]|\[BLANK\]|<blank>|<mask>", re.IGNORECASE),
]


# --------------------------------------------------------------------------
# Data loading
# --------------------------------------------------------------------------
def load_natural_rows(data_path: Path, lang_pairs: list[str]) -> list[dict[str, Any]]:
    """Load wmt25_task3_natural rows for the given language pairs, experimental_pool fold only."""
    logger.info(f"Loading dataset from {data_path}")
    data = json.loads(data_path.read_text())
    natural = next(ds for ds in data["datasets"] if ds["dataset"] == "wmt25_task3_natural")
    rows = [
        e
        for e in natural["examples"]
        if e["metadata_language_pair"] in lang_pairs and e["metadata_fold"] == "experimental_pool"
    ]
    del data
    gc.collect()
    n_dropped_none_qe = sum(1 for r in rows if r["metadata_overall_qe_score"] is None)
    rows = [r for r in rows if r["metadata_overall_qe_score"] is not None]
    logger.info(
        f"Loaded {len(rows)} experimental_pool rows across {lang_pairs} "
        f"(dropped {n_dropped_none_qe} rows with null QE score -- the severity rule needs it)"
    )
    return rows


# --------------------------------------------------------------------------
# Algorithm 1: severity-conditioned masking rule (verbatim from dossier Block A)
# --------------------------------------------------------------------------
def merge_overlapping_spans(spans: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Merge overlapping/adjacent char spans so masking never corrupts offsets.

    Keeps the most severe severity label for a merged region (critical > major > minor).
    """
    if not spans:
        return []
    sev_rank = {"critical": 3, "major": 2, "minor": 1}
    ordered = sorted(spans, key=lambda s: (s["start_i"], s["end_i"]))
    merged = [dict(ordered[0])]
    for s in ordered[1:]:
        last = merged[-1]
        if s["start_i"] <= last["end_i"]:
            last["end_i"] = max(last["end_i"], s["end_i"])
            if sev_rank.get(s["severity"], 0) > sev_rank.get(last["severity"], 0):
                last["severity"] = s["severity"]
        else:
            merged.append(dict(s))
    return merged


def compute_spans_to_mask(qe_score: float, spans: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Algorithm 1, verbatim per the dossier: severity-conditioned masking rule."""
    spans = spans or []
    if qe_score >= 0.90:
        return []
    if qe_score >= 0.50:
        non_minor = [s for s in spans if s["severity"] != "minor"]
        return non_minor if non_minor else spans
    return spans


def apply_masking(text: str, spans_to_mask: list[dict[str, Any]]) -> str:
    """Replace each (merged) span's char range in text with MASK_TOKEN, right-to-left."""
    merged = merge_overlapping_spans(spans_to_mask)
    merged.sort(key=lambda s: s["start_i"], reverse=True)
    out = text
    for s in merged:
        start, end = s["start_i"], s["end_i"]
        start = max(0, min(start, len(out)))
        end = max(start, min(end, len(out)))
        out = out[:start] + MASK_TOKEN + out[end:]
    return out


# --------------------------------------------------------------------------
# OpenRouter async calling (Responses API, matches aii-openrouter-llms shape)
# --------------------------------------------------------------------------
class CostTracker:
    def __init__(self, hard_cap: float):
        self.total_usd = 0.0
        self.n_calls = 0
        self.n_failed = 0
        self.hard_cap = hard_cap
        self._lock = asyncio.Lock()

    async def add(self, cost_usd: float | None, tool: str, **meta) -> None:
        async with self._lock:
            if cost_usd is not None:
                self.total_usd += cost_usd
            self.n_calls += 1
            if AII_COST_LEDGER and cost_usd is not None:
                rec = {"ts": time.time(), "tool": tool, "cost_usd": float(cost_usd), **meta}
                try:
                    with open(AII_COST_LEDGER, "a", encoding="utf-8") as f:
                        f.write(json.dumps(rec) + "\n")
                except OSError:
                    pass

    def over_cap(self) -> bool:
        return self.total_usd >= self.hard_cap


_pricing_cache: dict[str, tuple[float, float]] = {}


def load_openrouter_pricing() -> None:
    if _pricing_cache:
        return
    import requests

    try:
        resp = requests.get(OPENROUTER_MODELS_URL, timeout=30)
        for entry in resp.json().get("data", []):
            name = entry.get("id")
            if not name:
                continue
            price = entry.get("pricing") or {}
            try:
                _pricing_cache[name] = (float(price.get("prompt", 0) or 0), float(price.get("completion", 0) or 0))
            except (TypeError, ValueError):
                continue
        logger.info(f"Loaded OpenRouter pricing catalog ({len(_pricing_cache)} models)")
    except Exception as e:
        logger.warning(f"Could not load OpenRouter pricing catalog: {e}")


def estimate_call_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    priced = _pricing_cache.get(model)
    if priced is None:
        return None
    return round(input_tokens * priced[0] + output_tokens * priced[1], 8)


@retry(
    retry=retry_if_exception_type((aiohttp.ClientError, asyncio.TimeoutError)),
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=2, min=2, max=30),
)
async def call_openrouter(
    session: aiohttp.ClientSession, model: str, prompt: str, max_tokens: int, temperature: float = 0.0
) -> dict[str, Any]:
    payload = {"model": model, "input": prompt, "max_output_tokens": max_tokens, "temperature": temperature}
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    async with session.post(OPENROUTER_URL, json=payload, headers=headers, timeout=aiohttp.ClientTimeout(total=120)) as resp:
        body = await resp.json()
        if resp.status != 200:
            return {"success": False, "error": f"status {resp.status}: {str(body)[:300]}"}

        output_text, reasoning_text = "", ""
        if body.get("output_text"):
            output_text = body["output_text"]
        for item in body.get("output", []) or []:
            if item.get("type") == "reasoning" and isinstance(item.get("summary"), list) and item["summary"]:
                reasoning_text = item["summary"][0].get("text", "")
            elif item.get("type") == "message" and "content" in item:
                content = item["content"]
                if isinstance(content, list) and content:
                    fc = content[0]
                    if isinstance(fc, dict) and "text" in fc:
                        output_text = fc["text"]
                elif isinstance(content, str):
                    output_text = content
        if not output_text and reasoning_text:
            output_text = reasoning_text

        usage = body.get("usage", {}) or {}
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        reported_cost = usage.get("cost")
        cost = float(reported_cost) if isinstance(reported_cost, (int, float)) else estimate_call_cost(
            model, input_tokens, output_tokens
        )
        return {
            "success": True,
            "response": output_text,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost,
        }


async def repair_row(
    session: aiohttp.ClientSession,
    sem: asyncio.Semaphore,
    row: dict[str, Any],
    model_chain: list[str],
    cost_tracker: CostTracker,
) -> dict[str, Any]:
    source = row["input"]
    hyp = row["output"]
    qe_score = row["metadata_overall_qe_score"]
    spans = row["metadata_qe_flagged_spans"] or []
    spans_to_mask = compute_spans_to_mask(qe_score, spans)

    result: dict[str, Any] = {
        "row_id": f"{row['metadata_doc_id']}::{row['metadata_segment_id']}::{row['metadata_system_id']}",
        "lang_pair": row["metadata_language_pair"],
        "qe_score": qe_score,
        "n_spans_flagged": len(spans),
        "n_spans_masked": len(spans_to_mask),
        "source": hyp,  # pre-edit hypothesis (condition B's "before")
        "source_en": source,
        "masked_text": None,
        "repaired_text": hyp,
        "model_used": None,
        "n_llm_calls": 0,
        "call_error": None,
    }

    if not spans_to_mask:
        return result  # condition B never touches the sentence when qe_score >= 0.90

    if cost_tracker.over_cap():
        result["call_error"] = "hard_cost_cap_reached_skipped"
        return result

    masked_text = apply_masking(hyp, spans_to_mask)
    result["masked_text"] = masked_text
    max_tokens = min(1200, max(150, int(len(source.split()) * 3) + 100))
    prompt = MASKING_PROMPT_TEMPLATE.format(mask_token=MASK_TOKEN, source=source, masked_sentence=masked_text)

    last_error = None
    async with sem:
        for model in model_chain:
            try:
                r = await call_openrouter(session, model, prompt, max_tokens=max_tokens, temperature=0.0)
            except Exception as e:
                last_error = str(e)
                continue
            if r.get("success"):
                await cost_tracker.add(
                    r.get("cost_usd"),
                    tool="gen_art_experiment_2_condition_b",
                    model=model,
                    row_id=result["row_id"],
                )
                result["repaired_text"] = r["response"].strip() or hyp
                result["model_used"] = model
                result["n_llm_calls"] = 1
                return result
            last_error = r.get("error")
            logger.warning(f"{model} failed on row {result['row_id']}: {last_error} -- trying next fallback")

    result["call_error"] = last_error
    logger.error(f"All repair models failed for row {result['row_id']}: {last_error}")
    return result


async def run_condition_b(
    rows: list[dict[str, Any]], model_chain: list[str], cost_tracker: CostTracker, concurrency: int
) -> list[dict[str, Any]]:
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency * 2)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [repair_row(session, sem, row, model_chain, cost_tracker) for row in rows]
        results = []
        for i, coro in enumerate(asyncio.as_completed(tasks)):
            res = await coro
            results.append(res)
            if (i + 1) % 100 == 0 or (i + 1) == len(tasks):
                logger.info(
                    f"Condition B progress: {i + 1}/{len(tasks)} rows, "
                    f"cumulative cost=${cost_tracker.total_usd:.4f}"
                )
    return results


# --------------------------------------------------------------------------
# Leakage detection (qualitative failure-signature check, Appendix B bugs)
# --------------------------------------------------------------------------
def detect_leakage(text: str) -> bool:
    return any(p.search(text) for p in LEAK_PATTERNS)


# --------------------------------------------------------------------------
# COMET scoring, with HF-throttling-aware retry then a documented fallback
# --------------------------------------------------------------------------
def _hf_download_with_backoff(checkpoint_name: str, max_wait_s: float) -> str | None:
    """Download a COMET checkpoint, retrying through account-wide HF 429s.

    Calls huggingface_hub.snapshot_download directly (what comet.download_model
    wraps internally) rather than going through comet's own download_model,
    which swallows the real HTTP error and re-raises a generic
    ``KeyError("... not supported by COMET")`` after a pointless legacy-model
    fallback attempt -- that masked the actual 429s during initial testing.

    Returns the local checkpoint path, or None if the wall-clock budget
    expired without success (caller decides the fallback).
    """
    import os as _os

    from huggingface_hub import snapshot_download

    start = time.time()
    backoff = HF_DOWNLOAD_BACKOFF_START_S
    attempt = 0
    while time.time() - start < max_wait_s:
        attempt += 1
        try:
            model_path = snapshot_download(repo_id=checkpoint_name, token=HF_TOKEN)
            path = _os.path.join(model_path, "checkpoints", "model.ckpt")
            logger.info(f"Downloaded COMET checkpoint {checkpoint_name} on attempt {attempt} -> {path}")
            return path
        except HfHubHTTPError as e:
            logger.warning(
                f"[{checkpoint_name}] HF download attempt {attempt} failed ({type(e).__name__}: "
                f"{str(e)[:150]}); retrying in {backoff:.0f}s "
                f"(elapsed {time.time() - start:.0f}s / budget {max_wait_s:.0f}s)"
            )
        except Exception as e:
            logger.warning(f"[{checkpoint_name}] download attempt {attempt} failed ({type(e).__name__}): {str(e)[:200]}")
        time.sleep(min(backoff, max(0.0, max_wait_s - (time.time() - start))))
        backoff = min(backoff * 1.6, HF_DOWNLOAD_BACKOFF_CAP_S)
    logger.error(f"[{checkpoint_name}] download did not succeed within {max_wait_s:.0f}s budget")
    return None


def load_comet_scorer() -> tuple[Any, str, bool]:
    """Load the COMET/QE scorer, cascading through fallbacks. Returns (scorer_obj, name, is_real_comet)."""
    from comet import load_from_checkpoint

    for checkpoint_name, budget in [(COMET_MODEL_PRIMARY, HF_DOWNLOAD_MAX_WAIT_S), (COMET_MODEL_SECONDARY, 180.0)]:
        path = _hf_download_with_backoff(checkpoint_name, budget)
        if path:
            model = load_from_checkpoint(path)
            return model, checkpoint_name, True

    logger.warning(
        "Both COMET checkpoints unobtainable within budget (persistent HF Hub throttling). "
        "Falling back to a non-COMET, LLM-judge-based quality-delta proxy scored via OpenRouter "
        "(no HF dependency). This is a DOCUMENTED SUBSTITUTION -- not COMET -- and is flagged "
        "in method_out.json's metadata.comet_substitution field."
    )
    return None, "llm_judge_quality_proxy_v1", False


def score_comet_batch(
    model: Any, pairs: list[tuple[str, str, str]], batch_size: int = 16, gpus: int = 1
) -> list[float]:
    """pairs: list of (source_en, mt_text, _unused_ref). Returns COMET scores, one per pair."""
    data = [{"src": src, "mt": mt} for src, mt, _ in pairs]
    output = model.predict(data, batch_size=batch_size, gpus=gpus, progress_bar=False)
    return list(output.scores)


# --------------------------------------------------------------------------
# LLM-judge fallback scorer (only used if COMET is genuinely unobtainable)
# --------------------------------------------------------------------------
JUDGE_MODEL = "openai/gpt-4o-mini"
JUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a
continuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).
Respond with ONLY the number, nothing else.

SOURCE (English): {source}

TRANSLATION: {mt}

Score:"""


async def judge_quality(session: aiohttp.ClientSession, sem: asyncio.Semaphore, source: str, mt: str) -> float | None:
    async with sem:
        try:
            r = await call_openrouter(session, JUDGE_MODEL, JUDGE_PROMPT.format(source=source, mt=mt), max_tokens=10, temperature=0.0)
        except Exception:
            return None
    if not r.get("success"):
        return None
    m = re.search(r"[01](?:\.\d+)?|0?\.\d+", r["response"])
    if not m:
        return None
    try:
        return max(0.0, min(1.0, float(m.group(0))))
    except ValueError:
        return None


async def run_llm_judge_scoring(
    pairs: list[tuple[str, str]], concurrency: int, cost_tracker: CostTracker
) -> list[float | None]:
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency * 2)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [judge_quality(session, sem, src, mt) for src, mt in pairs]
        return list(await asyncio.gather(*tasks))


# --------------------------------------------------------------------------
# Gate decision
# --------------------------------------------------------------------------
def get_published_delta(lang_pair: str) -> tuple[float, str]:
    pinned = PUBLISHED_DELTA_COMET.get(lang_pair)
    if pinned is not None:
        return pinned, "per_pair_pinned"
    return PUBLISHED_POOLED_DELTA_COMET, "pooled_fallback"


def compute_gate(
    per_pair_delta_comet: dict[str, float], per_pair_leakage_rate: dict[str, float], is_real_comet: bool
) -> dict[str, Any]:
    direction_by_pair = {p: per_pair_delta_comet[p] < 0 for p in per_pair_delta_comet}
    gate_passes_direction = all(direction_by_pair.values())

    magnitude_by_pair = {}
    for p, delta in per_pair_delta_comet.items():
        published, source = get_published_delta(p)
        magnitude_by_pair[p] = {
            "published_delta": published,
            "published_source": source,
            "observed_delta": delta,
            "abs_diff": abs(delta - published),
            "within_tolerance": abs(delta - published) < MAGNITUDE_TOLERANCE,
        }
    gate_passes_magnitude = all(v["within_tolerance"] for v in magnitude_by_pair.values())

    gate_passes_leakage = any(v > 0.0 for v in per_pair_leakage_rate.values())

    verdict = "PASS" if (gate_passes_direction and gate_passes_leakage) else "FAIL"
    if not is_real_comet:
        verdict = f"{verdict}_UNRELIABLE_SUBSTITUTED_SCORER"

    return {
        "verdict": verdict,
        "gate_component_results": {
            "direction": {"pass": gate_passes_direction, "by_pair": direction_by_pair},
            "magnitude": {"pass": gate_passes_magnitude, "by_pair": magnitude_by_pair, "note": "reported, not solely gating per plan"},
            "leakage": {"pass": gate_passes_leakage, "by_pair": per_pair_leakage_rate},
        },
    }


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
@logger.catch(reraise=True)
def main() -> None:
    parser = argparse.ArgumentParser(description="Condition B masked-fill baseline fidelity check")
    parser.add_argument("--max-rows-per-pair", type=int, default=None, help="Cap rows per language pair (testing)")
    parser.add_argument("--mini", action="store_true", help="Use mini_data_out.json instead of full")
    parser.add_argument("--concurrency", type=int, default=16, help="Async OpenRouter concurrency")
    parser.add_argument("--skip-comet", action="store_true", help="Skip COMET scoring (plumbing test only)")
    parser.add_argument("--hf-max-wait", type=float, default=None, help="Override HF_DOWNLOAD_MAX_WAIT_S (testing)")
    parser.add_argument("--out", type=str, default="method_out.json")
    args = parser.parse_args()

    global HF_DOWNLOAD_MAX_WAIT_S
    if args.hf_max_wait is not None:
        HF_DOWNLOAD_MAX_WAIT_S = args.hf_max_wait

    logger.info(f"=== Condition B fidelity check starting (mini={args.mini}, max_rows_per_pair={args.max_rows_per_pair}) ===")
    data_path = MINI_DATA_PATH if args.mini else FULL_DATA_PATH
    rows = load_natural_rows(data_path, LANG_PAIRS)

    by_pair: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        by_pair.setdefault(r["metadata_language_pair"], []).append(r)
    for p in LANG_PAIRS:
        if p not in by_pair:
            by_pair[p] = []
        RNG.shuffle(by_pair[p])
        if args.max_rows_per_pair is not None:
            by_pair[p] = by_pair[p][: args.max_rows_per_pair]
    rows = [r for p in LANG_PAIRS for r in by_pair[p]]
    logger.info(f"Row counts per pair after capping: { {p: len(by_pair[p]) for p in LANG_PAIRS} }")

    # --- Cost estimate BEFORE running anything ---
    load_openrouter_pricing()
    n_expected_calls = sum(
        1 for r in rows if compute_spans_to_mask(r["metadata_overall_qe_score"], r["metadata_qe_flagged_spans"] or [])
    )
    avg_chars = sum(len(r["output"]) + len(r["input"]) for r in rows) / max(1, len(rows))
    avg_tokens_per_call = avg_chars / 3.5 + 350  # rough chars->token + prompt scaffolding overhead
    priced = _pricing_cache.get(REPAIR_MODEL, (0.0, 0.0))
    est_cost = n_expected_calls * (avg_tokens_per_call * 0.6 * priced[0] + avg_tokens_per_call * 0.4 * priced[1])
    logger.info(
        f"Upfront estimate: {n_expected_calls} expected LLM calls, ~{avg_tokens_per_call:.0f} tok/call, "
        f"{REPAIR_MODEL} pricing -> ~${est_cost:.4f} (soft cap ${SOFT_COST_CAP_USD}, hard cap ${HARD_COST_CAP_USD})"
    )
    if est_cost > SOFT_COST_CAP_USD:
        keep_frac = SOFT_COST_CAP_USD / est_cost
        logger.warning(f"Estimate exceeds soft cap -- subsampling rows to {keep_frac:.2%} to stay under budget")
        for p in LANG_PAIRS:
            n_keep = max(1, int(len(by_pair[p]) * keep_frac))
            by_pair[p] = by_pair[p][:n_keep]
        rows = [r for p in LANG_PAIRS for r in by_pair[p]]

    # --- Condition B: run masked-fill baseline over OpenRouter ---
    cost_tracker = CostTracker(hard_cap=HARD_COST_CAP_USD)
    model_chain = [REPAIR_MODEL] + REPAIR_MODEL_FALLBACKS
    t0 = time.time()
    results = asyncio.run(run_condition_b(rows, model_chain, cost_tracker, args.concurrency))
    logger.info(
        f"Condition B complete: {len(results)} rows in {time.time() - t0:.1f}s, "
        f"total OpenRouter cost=${cost_tracker.total_usd:.4f} ({cost_tracker.n_calls} calls)"
    )
    models_actually_used = Counter(r["model_used"] for r in results if r["model_used"])
    logger.info(f"Repair models actually used: {dict(models_actually_used)}")
    n_call_errors = sum(1 for r in results if r["call_error"])
    if n_call_errors:
        logger.warning(f"{n_call_errors} rows had no successful repair call (kept as untouched hypothesis)")

    # --- Leakage detection ---
    for r in results:
        r["leaked"] = detect_leakage(r["repaired_text"]) if r["n_spans_masked"] > 0 else False

    # --- COMET scoring ---
    is_real_comet = False
    comet_model_name = None
    if args.skip_comet:
        logger.warning("--skip-comet set: writing null deltas for a plumbing-only smoke test")
        for r in results:
            r["comet_before"] = None
            r["comet_after"] = None
            r["delta_comet"] = None
    else:
        scorer, comet_model_name, is_real_comet = load_comet_scorer()
        if is_real_comet:
            import torch

            gpus = 1 if torch.cuda.is_available() else 0
            pairs_before = [(r["source_en"], r["source"], "") for r in results]
            pairs_after = [(r["source_en"], r["repaired_text"], "") for r in results]
            logger.info(f"Scoring {len(results)} pairs x2 (before/after) with {comet_model_name} (gpus={gpus})")
            scores_before = score_comet_batch(scorer, pairs_before, batch_size=32, gpus=gpus)
            scores_after = score_comet_batch(scorer, pairs_after, batch_size=32, gpus=gpus)
            for r, cb, ca in zip(results, scores_before, scores_after):
                r["comet_before"] = float(cb)
                r["comet_after"] = float(ca)
                r["delta_comet"] = float(ca) - float(cb)
            del scorer
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        else:
            logger.info(f"Scoring with fallback scorer: {comet_model_name}")
            judge_pairs_before = [(r["source_en"], r["source"]) for r in results]
            judge_pairs_after = [(r["source_en"], r["repaired_text"]) for r in results]
            scores_before = asyncio.run(run_llm_judge_scoring(judge_pairs_before, args.concurrency, cost_tracker))
            scores_after = asyncio.run(run_llm_judge_scoring(judge_pairs_after, args.concurrency, cost_tracker))
            for r, cb, ca in zip(results, scores_before, scores_after):
                r["comet_before"] = cb
                r["comet_after"] = ca
                r["delta_comet"] = (ca - cb) if (cb is not None and ca is not None) else None

    # --- Aggregate per-pair / pooled stats ---
    per_pair_results = {}
    for pair in LANG_PAIRS:
        pair_rows = [r for r in results if r["lang_pair"] == pair]
        masked_rows = [r for r in pair_rows if r["n_spans_masked"] > 0]
        deltas = [r["delta_comet"] for r in pair_rows if r["delta_comet"] is not None]
        leaked_rows = [r for r in masked_rows if r["leaked"]]
        per_pair_results[pair] = {
            "n_rows": len(pair_rows),
            "n_rows_with_spans_flagged": sum(1 for r in pair_rows if r["n_spans_flagged"] > 0),
            "n_rows_masked_by_condition_b": len(masked_rows),
            "n_llm_calls": sum(r["n_llm_calls"] for r in pair_rows),
            "mean_delta_comet": (sum(deltas) / len(deltas)) if deltas else None,
            "n_scored": len(deltas),
            "leakage_rate": (len(leaked_rows) / len(masked_rows)) if masked_rows else 0.0,
            "n_leaked": len(leaked_rows),
            "example_leaked_outputs": [
                {"row_id": r["row_id"], "masked_text": r["masked_text"], "repaired_text": r["repaired_text"]}
                for r in leaked_rows[:10]
            ],
            "example_largest_negative_delta": sorted(
                [r for r in pair_rows if r["delta_comet"] is not None], key=lambda r: r["delta_comet"]
            )[:5],
        }

    all_deltas = [r["delta_comet"] for r in results if r["delta_comet"] is not None]
    all_masked = [r for r in results if r["n_spans_masked"] > 0]
    all_leaked = [r for r in all_masked if r["leaked"]]
    pooled_mean_delta_comet = (sum(all_deltas) / len(all_deltas)) if all_deltas else None
    pooled_leakage_rate = (len(all_leaked) / len(all_masked)) if all_masked else 0.0

    gate = compute_gate(
        {p: per_pair_results[p]["mean_delta_comet"] for p in LANG_PAIRS if per_pair_results[p]["mean_delta_comet"] is not None},
        {p: per_pair_results[p]["leakage_rate"] for p in LANG_PAIRS},
        is_real_comet,
    )
    logger.info(f"GATE VERDICT: {gate['verdict']}")
    logger.info(f"Pooled mean ΔCOMET: {pooled_mean_delta_comet}, pooled leakage rate: {pooled_leakage_rate:.3f}")

    limitations_if_fail = []
    if not is_real_comet:
        limitations_if_fail.append(
            "COMET (Unbabel/wmt22-cometkiwi-da and wmt22-comet-da) could not be downloaded within the "
            f"{HF_DOWNLOAD_MAX_WAIT_S:.0f}s+180s retry budget due to a persistent, account-wide 429 from "
            "huggingface.co (observed on unrelated public repos too, e.g. bert-base-uncased) -- almost "
            "certainly concurrent sibling AI-Inventor runs on this host saturating the shared HF token/IP. "
            "The reported deltas use an LLM-judge (openai/gpt-4o-mini) 0-1 adequacy-score proxy instead of "
            "COMET; they are NOT comparable in scale or calibration to Padmanabhan's ΔCOMET figures, and the "
            "gate verdict is marked *_UNRELIABLE_SUBSTITUTED_SCORER accordingly. Downstream conditions "
            "(D/C1/C2/C) that depend on a faithful ΔCOMET reproduction should re-run this artifact once COMET "
            "can be downloaded, rather than trusting this pass's magnitude numbers."
        )
    if gate["verdict"].startswith("FAIL"):
        limitations_if_fail.append(
            "Direction and/or leakage gate components failed -- see gate_component_results for which. "
            "This means condition B on this reproduction did not exhibit Padmanabhan's documented failure "
            "signature and downstream conditions built on 'condition B degrades quality' should not assume "
            "that premise holds for this substitute repair model / data slice without further investigation."
        )
    if REPAIR_MODEL not in models_actually_used:
        limitations_if_fail.append(
            f"Primary repair model {REPAIR_MODEL} was never successfully used; results reflect fallback "
            f"model(s) {dict(models_actually_used)} instead, which changes the generation-mismatch confound "
            "discussed in the resource dossier (Block B)."
        )

    output = {
        "metadata": {
            "condition": "B_substitute_model_fidelity_check",
            "repair_model_requested": REPAIR_MODEL,
            "repair_model_fallback_chain": REPAIR_MODEL_FALLBACKS,
            "repair_models_actually_used": dict(models_actually_used),
            "comet_model_requested": COMET_MODEL_PRIMARY,
            "comet_model_used": comet_model_name,
            "comet_is_real_comet": is_real_comet,
            "comet_substitution": None
            if is_real_comet
            else {
                "reason": "persistent account-wide HF Hub 429 throttling, both COMET checkpoints unobtainable",
                "substitute_scorer": "llm_judge_quality_proxy_v1 (openai/gpt-4o-mini, 0-1 adequacy score via OpenRouter)",
                "warning": "NOT comparable in scale/calibration to Padmanabhan's ΔCOMET -- see limitations_if_fail",
            },
            "masking_prompt_provenance": (
                "Algorithm 1 severity rule is verbatim from the resource-dossier dependency (Block A, cited to "
                "arxiv.org/html/2511.13884). The literal masking PROMPT TEXT was not retrievable in "
                "machine-readable form from that dependency's research_out.json at execution time (only its "
                "documented shape: single blank token per sentence, one call per sentence). This script's "
                "MASKING_PROMPT_TEMPLATE is a faithful reconstruction of that documented shape, not a verbatim "
                "quote -- flagged per the artifact plan's fallback item (5)."
            ),
            "mask_token": MASK_TOKEN,
            "lang_pairs": LANG_PAIRS,
            "n_rows_per_pair": {p: per_pair_results[p]["n_rows"] for p in LANG_PAIRS},
            "n_llm_calls": cost_tracker.n_calls,
            "total_cost_usd": round(cost_tracker.total_usd, 6),
            "soft_cost_cap_usd": SOFT_COST_CAP_USD,
            "hard_cost_cap_usd": HARD_COST_CAP_USD,
            "pooled_mean_delta_comet": pooled_mean_delta_comet,
            "pooled_leakage_rate": pooled_leakage_rate,
            "per_pair_results": per_pair_results,
            "published_comparison": {
                "padmanabhan_pooled_delta_comet": PUBLISHED_POOLED_DELTA_COMET,
                "padmanabhan_per_pair_range": PUBLISHED_PER_PAIR_RANGE,
                "padmanabhan_per_pair_pinned": PUBLISHED_DELTA_COMET,
            },
            "gate_verdict": gate["verdict"],
            "gate_component_results": gate["gate_component_results"],
            "limitations_if_fail": limitations_if_fail,
            "leak_patterns_used": [p.pattern for p in LEAK_PATTERNS],
        },
        "datasets": [
            {
                "dataset": "condition_b_masked_fill_baseline",
                "examples": [
                    {
                        "input": r["masked_text"] if r["masked_text"] is not None else r["source"],
                        "output": r["source"],
                        "predict_condition_b_repaired": r["repaired_text"],
                        "metadata_row_id": r["row_id"],
                        "metadata_lang_pair": r["lang_pair"],
                        "metadata_qe_score": r["qe_score"],
                        "metadata_n_spans_flagged": r["n_spans_flagged"],
                        "metadata_n_spans_masked": r["n_spans_masked"],
                        "metadata_source_en": r["source_en"],
                        "metadata_model_used": r["model_used"],
                        "metadata_n_llm_calls": r["n_llm_calls"],
                        "metadata_call_error": r["call_error"],
                        "metadata_leaked": r["leaked"],
                        "metadata_comet_before": r["comet_before"],
                        "metadata_comet_after": r["comet_after"],
                        "metadata_delta_comet": r["delta_comet"],
                    }
                    for r in results
                ],
            }
        ],
    }

    out_path = ROOT / args.out
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
