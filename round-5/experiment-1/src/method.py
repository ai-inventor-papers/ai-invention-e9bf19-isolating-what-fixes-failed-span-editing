#!/usr/bin/env python3
"""Rescue Condition C's missing quality score (gen_plan_experiment_1_idx1).

Condition C (art_6n9zJVKWXnio, 320 wmt25_task3_natural rows across
en-ru_RU / en-uk_UA) was scored twice before with real Unbabel/wmt22-cometkiwi-da
unavailable due to persistent HF-Hub 429 throttling that Condition B
(art_G9ppuk8aHUhW) also hit. This artifact is a SCORING-ONLY rerun: it
generates no new repair text at all, it only tries -- with genuinely new
mitigations vs. the two prior failed attempts -- to obtain the real COMET
checkpoint and score Condition C's already-generated pre/post-repair text.

Two genuinely new mitigations vs. the prior attempts:
  (a) an alternate mirror endpoint (hf-mirror.com) tried alongside the
      primary huggingface.co endpoint,
  (b) attempts spread across separate wall-clock windows (not just
      exponential backoff inside one process lifetime), so a per-minute or
      per-hour 429 window is actually crossed.

If real COMET is genuinely unobtainable within the time-boxed mitigation
window, this falls back to the EXACT SAME LLM-judge proxy configuration
Condition B's own fidelity check used (openai/gpt-4o-mini, JUDGE_PROMPT
verbatim from that artifact's method.py, temperature=0.0, 0-1 adequacy
scale), re-scoring a fresh sample of Condition B's own rows with that
identical proxy IN THIS SAME RUN so the output reports a same-proxy
B-vs-C comparison instead of an isolated, incomparable number.
"""

from __future__ import annotations

import asyncio
import gc
import glob
import json
import os
import random
import re
import resource
import sys
import time
from pathlib import Path
from typing import Any

import aiohttp
from huggingface_hub.errors import HfHubHTTPError
from loguru import logger

# --------------------------------------------------------------------------
# Setup: logging, resource limits, paths
# --------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
Path(ROOT / "logs").mkdir(exist_ok=True)
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(ROOT / "logs" / "run.log"), rotation="30 MB", level="DEBUG")

# Container RAM budget: the two source method_out.json files are a few MB
# each; parsed objects run a small multiple of that. COMET model + XLM-R
# encoder activations for batch_size<=32 on 320+ rows are modest. Cap well
# under the 56GB container limit observed by aii-use-hardware.
RAM_BUDGET_BYTES = 12 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))
resource.setrlimit(resource.RLIMIT_CPU, (3 * 3600, 3 * 3600))

RUN_ROOT = Path("/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5")
HF_TOKEN = os.environ.get("HF_TOKEN")

COMET_MODEL = "Unbabel/wmt22-cometkiwi-da"
ENDPOINTS = ["https://huggingface.co", "https://hf-mirror.com"]
# Genuinely new vs. the two prior in-process-backoff attempts: real
# wall-clock-separated windows, so a per-minute/per-hour 429 bucket is
# actually crossed rather than retried inside one short-lived process.
WINDOW_OFFSETS_MIN = [0, 25, 75, 165]
PHASE1_HARD_CAP_S = 3.0 * 3600  # leave >=2.5h of the 6h budget for fallback + writeup

JUDGE_MODEL = "openai/gpt-4o-mini"
# Verbatim from Condition B's method.py (art_G9ppuk8aHUhW,
# iter_2/gen_art/gen_art_experiment_2/method.py:490-498) -- copied
# character-for-character so the proxy fallback is provably identical, not
# a paraphrase.
JUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a
continuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).
Respond with ONLY the number, nothing else.

SOURCE (English): {source}

TRANSLATION: {mt}

Score:"""
JUDGE_TEMPERATURE = 0.0
JUDGE_MAX_TOKENS = 10
COST_CAP_USD = 9.0  # hard stop below the $10 artifact ceiling, matching the plan's fallback
# openai/gpt-4o-mini list pricing (per OpenRouter, USD per token)
JUDGE_PRICE_IN_PER_TOK = 0.15 / 1_000_000
JUDGE_PRICE_OUT_PER_TOK = 0.60 / 1_000_000

random.seed(42)


# ============================================================================
# Phase 0: locate the two upstream artifacts on disk (no new generation)
# ============================================================================
def _load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_condition_c() -> Path:
    """Locate art_6n9zJVKWXnio (Condition C: 320 natural rows, iterate-and-
    reverify repair). Verified by content signature (unique metadata keys +
    exact row count), not by filename -- the artifact id is not embedded in
    any filename on disk, so path-matching alone cannot confirm identity.
    """
    candidates = sorted(glob.glob(str(RUN_ROOT / "**" / "full_method_out.json"), recursive=True))
    matches = []
    for c in candidates:
        try:
            d = _load_json(Path(c))
        except (json.JSONDecodeError, OSError) as e:
            logger.debug(f"Skipping unreadable candidate {c}: {e}")
            continue
        datasets = d.get("datasets", [])
        if not datasets:
            continue
        ds0 = datasets[0]
        examples = ds0.get("examples", [])
        has_c2_signature = any("metadata_c2_certificate_achieved" in ex for ex in examples[:3])
        n_natural = sum(
            1 for ex in examples if str(ex.get("metadata_row_id", "")).startswith("wmt25_task3_natural:")
        )
        if has_c2_signature and n_natural == 320:
            matches.append(c)
    assert matches, (
        "BLOCKING: could not locate Condition C (art_6n9zJVKWXnio, 320 natural rows, "
        "metadata_c2_certificate_achieved signature) under any full_method_out.json "
        f"beneath {RUN_ROOT}. Candidates scanned: {len(candidates)}."
    )
    if len(matches) > 1:
        logger.warning(f"Multiple Condition C matches found, using the first: {matches}")
    logger.info(f"Located Condition C at: {matches[0]}")
    return Path(matches[0])


def find_condition_b() -> Path:
    """Locate art_G9ppuk8aHUhW (Condition B: masked-fill fidelity check,
    the artifact whose LLM-judge proxy config the fallback path must reuse
    verbatim). Verified by its unique metadata.condition signature.
    """
    candidates = sorted(glob.glob(str(RUN_ROOT / "**" / "full_method_out.json"), recursive=True))
    matches = []
    for c in candidates:
        try:
            d = _load_json(Path(c))
        except (json.JSONDecodeError, OSError) as e:
            logger.debug(f"Skipping unreadable candidate {c}: {e}")
            continue
        if d.get("metadata", {}).get("condition") == "B_substitute_model_fidelity_check":
            matches.append(c)
    assert matches, (
        "BLOCKING: could not locate Condition B (art_G9ppuk8aHUhW, "
        "metadata.condition=='B_substitute_model_fidelity_check') under any "
        f"full_method_out.json beneath {RUN_ROOT}. Candidates scanned: {len(candidates)}."
    )
    if len(matches) > 1:
        logger.warning(f"Multiple Condition B matches found, using the first: {matches}")
    logger.info(f"Located Condition B at: {matches[0]}")
    return Path(matches[0])


def load_condition_c_rows(path: Path) -> list[dict]:
    d = _load_json(path)
    ds0 = d["datasets"][0]
    rows = ds0["examples"]
    natural_rows = [r for r in rows if str(r.get("metadata_row_id", "")).startswith("wmt25_task3_natural:")]
    assert len(natural_rows) == 320, f"expected 320 natural rows in Condition C, got {len(natural_rows)}"
    out = []
    for r in natural_rows:
        out.append(
            {
                "row_id": r["metadata_row_id"],
                "language_pair": r["metadata_language_pair"],
                "source_text": r["input"],
                "pre_repair_text": r["output"],
                "post_repair_text": r["predict_c2"],
                "certificate_achieved": r.get("metadata_c2_certificate_achieved"),
                "n_passes": r.get("metadata_c2_n_passes"),
                "no_op": r.get("metadata_c2_no_op"),
            }
        )
    return out


def extract_b_fidelity_config(path: Path) -> dict:
    """Extract Condition B's LLM-judge proxy config verbatim from its own
    metadata + this script's copy of its method.py's JUDGE_PROMPT (see the
    module docstring's provenance note above -- the prompt string here is a
    character-for-character copy of iter_2/gen_art/gen_art_experiment_2/
    method.py:490-498, confirmed by direct diff during development).
    """
    d = _load_json(path)
    meta = d.get("metadata", {})
    comet_sub = meta.get("comet_substitution", {})
    assert "llm_judge_quality_proxy_v1" in comet_sub.get("substitute_scorer", ""), (
        "Condition B's metadata.comet_substitution.substitute_scorer does not name "
        "llm_judge_quality_proxy_v1 -- config extraction assumption violated."
    )
    return {
        "model_id": JUDGE_MODEL,
        "prompt_template": JUDGE_PROMPT,
        "temperature": JUDGE_TEMPERATURE,
        "max_tokens": JUDGE_MAX_TOKENS,
        "scoring_convention": "regex-parsed first [0,1] float, clipped to [0,1]; "
        "delta = judge(post_repair_text) - judge(pre_repair_text)",
        "source_artifact": "art_G9ppuk8aHUhW",
        "source_condition_metadata": comet_sub,
        "reconstructed_from_partial_evidence": False,  # prompt matched byte-for-byte against source method.py
    }


def load_condition_b_rows_for_rescoring(path: Path, n_sample: int, seed: int = 42) -> list[dict]:
    """Load a seeded sample of Condition B's own rows (pre/post repair text)
    to re-score with the identical proxy in this run, so the fallback output
    is a same-proxy, same-run B-vs-C comparison rather than an isolated
    number. B has a single 1560-row natural population (en-zh_CN/en-cs_CZ,
    all wmt25_task3_natural rows, unlike C's 320) -- there is no 320-row
    'natural' subset inside B to assert against; that subset only exists in
    C. We sample n_sample rows (default: 320, matching C's count) stratified
    evenly across B's two language pairs for a comparably-sized rescore.
    """
    d = _load_json(path)
    ds0 = d["datasets"][0]
    rows = ds0["examples"]
    by_pair: dict[str, list[dict]] = {}
    for r in rows:
        by_pair.setdefault(r["metadata_lang_pair"], []).append(r)
    rng = random.Random(seed)
    per_pair_n = n_sample // max(len(by_pair), 1)
    sampled = []
    for pair, pair_rows in sorted(by_pair.items()):
        take = min(per_pair_n, len(pair_rows))
        sampled.extend(rng.sample(pair_rows, take))
    out = []
    for r in sampled:
        out.append(
            {
                "row_id": r["metadata_row_id"],
                "language_pair": r["metadata_lang_pair"],
                "source_text": r["metadata_source_en"],
                "pre_repair_text": r["output"],
                "post_repair_text": r["predict_condition_b_repaired"],
            }
        )
    return out


# ============================================================================
# Phase 1: mitigated real-COMET download attempt
# ============================================================================
def try_comet_download(endpoint: str, local_dir: Path, timeout_s: int = 300) -> tuple[str | None, dict]:
    from huggingface_hub import snapshot_download

    t0 = time.time()
    entry = {"ts": t0, "endpoint": endpoint, "status": None, "elapsed_s": None, "error": None}
    try:
        os.environ["HF_HUB_ENDPOINT"] = endpoint
        path = snapshot_download(
            repo_id=COMET_MODEL,
            local_dir=str(local_dir),
            etag_timeout=30,
            token=HF_TOKEN,
        )
        entry["status"] = "SUCCESS"
        entry["elapsed_s"] = time.time() - t0
        return path, entry
    except HfHubHTTPError as e:
        code = getattr(e.response, "status_code", None)
        entry["status"] = code if code is not None else "HTTP_ERROR"
        entry["error"] = str(e)[:400]
        entry["elapsed_s"] = time.time() - t0
        return None, entry
    except Exception as e:  # DNS failure, org block, timeout, etc. -- all informative, all logged
        entry["status"] = "EXC"
        entry["error"] = f"{type(e).__name__}: {str(e)[:400]}"
        entry["elapsed_s"] = time.time() - t0
        return None, entry
    finally:
        os.environ.pop("HF_HUB_ENDPOINT", None)


def run_phase1_mitigation(run_start: float) -> tuple[str | None, list[dict]]:
    attempts_log: list[dict] = []
    local_dir = ROOT / "hf_cache" / "wmt22-cometkiwi-da"
    checkpoint_dir = None
    for offset_min in WINDOW_OFFSETS_MIN:
        target_t = run_start + offset_min * 60
        wait_s = target_t - time.time()
        if wait_s > 0:
            logger.info(f"Waiting {wait_s:.0f}s to reach mitigation window offset={offset_min}min")
            time.sleep(wait_s)
        for endpoint in ENDPOINTS:
            logger.info(f"[window +{offset_min}min] attempting COMET download from {endpoint}")
            path, entry = try_comet_download(endpoint, local_dir)
            attempts_log.append(entry)
            logger.info(f"  -> status={entry['status']} elapsed={entry['elapsed_s']:.1f}s")
            if path:
                checkpoint_dir = path
                break
        if checkpoint_dir:
            break
        if time.time() - run_start > PHASE1_HARD_CAP_S:
            logger.warning("Phase 1 hard cap (3.0h) reached without success; moving to fallback")
            break
    return checkpoint_dir, attempts_log


# ============================================================================
# Phase 2a: REAL-COMET scoring path
# ============================================================================
def find_checkpoint_ckpt(checkpoint_dir: str) -> str:
    matches = glob.glob(os.path.join(checkpoint_dir, "checkpoints", "*.ckpt"))
    assert matches, f"No .ckpt found under {checkpoint_dir}/checkpoints/"
    return matches[0]


def comet_score_batch(model: Any, pairs: list[tuple[str, str]], gpus: int, batch_size: int = 32) -> list[float]:
    data = [{"src": src, "mt": mt} for src, mt in pairs]
    out = model.predict(data, batch_size=batch_size, gpus=gpus, progress_bar=False)
    return [float(s) for s in out.scores]


def paired_bootstrap_ci(deltas: list[float], n_boot: int = 10000, seed: int = 42, alpha: float = 0.05) -> dict:
    rng = random.Random(seed)
    n = len(deltas)
    if n == 0:
        return {"mean": None, "ci_low": None, "ci_high": None, "n_boot": n_boot, "n": 0}
    boot_means = []
    for _ in range(n_boot):
        sample = [deltas[rng.randrange(n)] for _ in range(n)]
        boot_means.append(sum(sample) / n)
    boot_means.sort()
    lo_idx = int((alpha / 2) * n_boot)
    hi_idx = int((1 - alpha / 2) * n_boot) - 1
    return {
        "mean": sum(deltas) / n,
        "ci_low": boot_means[max(0, lo_idx)],
        "ci_high": boot_means[min(n_boot - 1, hi_idx)],
        "n_boot": n_boot,
        "n": n,
    }


def bootstrap_paired_difference(
    deltas_a: list[float], deltas_b: list[float], n_boot: int = 10000, seed: int = 42, alpha: float = 0.05
) -> dict:
    """Bootstraps the difference of two INDEPENDENT sample means (a - b).
    a and b are not row-paired (different populations / different rows), so
    this resamples each side independently with replacement -- an
    unpaired-mean-difference bootstrap, not a paired-difference bootstrap in
    the per-row sense (there is no shared row id to pair on between B and C).
    """
    rng = random.Random(seed)
    na, nb = len(deltas_a), len(deltas_b)
    if na == 0 or nb == 0:
        return {"mean_diff": None, "ci_low": None, "ci_high": None, "n_boot": n_boot, "n_a": na, "n_b": nb}
    diffs = []
    for _ in range(n_boot):
        sa = sum(deltas_a[rng.randrange(na)] for _ in range(na)) / na
        sb = sum(deltas_b[rng.randrange(nb)] for _ in range(nb)) / nb
        diffs.append(sa - sb)
    diffs.sort()
    lo_idx = int((alpha / 2) * n_boot)
    hi_idx = int((1 - alpha / 2) * n_boot) - 1
    return {
        "mean_diff": (sum(deltas_a) / na) - (sum(deltas_b) / nb),
        "ci_low": diffs[max(0, lo_idx)],
        "ci_high": diffs[min(n_boot - 1, hi_idx)],
        "n_boot": n_boot,
        "n_a": na,
        "n_b": nb,
    }


def groupby_mean(rows: list[dict], values: list[float], key: str) -> dict:
    buckets: dict[str, list[float]] = {}
    for r, v in zip(rows, values):
        buckets.setdefault(r[key], []).append(v)
    return {k: (sum(v) / len(v), len(v)) for k, v in buckets.items()}


def run_real_comet_path(checkpoint_dir: str, natural_c_rows: list[dict], attempts_log: list[dict]) -> dict:
    import torch
    from comet import load_from_checkpoint

    ckpt_path = find_checkpoint_ckpt(checkpoint_dir)
    logger.info(f"Loading COMET from checkpoint: {ckpt_path}")
    model = load_from_checkpoint(ckpt_path)
    gpus = 1 if torch.cuda.is_available() else 0
    logger.info(f"Scoring {len(natural_c_rows)} rows x2 (pre/post) with real COMET (gpus={gpus})")

    pre_pairs = [(r["source_text"], r["pre_repair_text"]) for r in natural_c_rows]
    post_pairs = [(r["source_text"], r["post_repair_text"]) for r in natural_c_rows]
    pre_scores = comet_score_batch(model, pre_pairs, gpus=gpus)
    post_scores = comet_score_batch(model, post_pairs, gpus=gpus)
    del model
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    for r, pre, post in zip(natural_c_rows, pre_scores, post_scores):
        r["comet_before"] = pre
        r["comet_after"] = post
        r["delta_comet"] = post - pre

    deltas = [r["delta_comet"] for r in natural_c_rows]
    by_lang = groupby_mean(natural_c_rows, deltas, "language_pair")
    ci = paired_bootstrap_ci(deltas)

    n_leaked_or_noop = sum(1 for r in natural_c_rows if r.get("no_op"))
    logger.info(
        f"Real-COMET pooled mean delta_comet={ci['mean']:.5f} "
        f"[{ci['ci_low']:.5f},{ci['ci_high']:.5f}] over n={len(deltas)}"
    )

    return {
        "quality_metric_path_taken": "real_wmt22_cometkiwi_da",
        "attempts_log": attempts_log,
        "condition_c_delta_comet_natural_pooled_mean": ci["mean"],
        "condition_c_delta_comet_natural_bootstrap_ci": ci,
        "condition_c_delta_comet_by_language_pair": {
            k: {"mean_delta_comet": v[0], "n": v[1]} for k, v in by_lang.items()
        },
        "condition_c_n_natural_rows_scored": len(natural_c_rows),
        "condition_c_n_rows_no_op_c2_repair": n_leaked_or_noop,
        "condition_c_delta_comet_per_row": [
            {
                "row_id": r["row_id"],
                "language_pair": r["language_pair"],
                "comet_before": r["comet_before"],
                "comet_after": r["comet_after"],
                "delta_comet": r["delta_comet"],
                "certificate_achieved": r["certificate_achieved"],
                "n_passes": r["n_passes"],
            }
            for r in natural_c_rows
        ],
        "directly_comparable_to_C1_C2_real_comet_numbers": True,
        "comet_model_used": COMET_MODEL,
    }, natural_c_rows


# ============================================================================
# Phase 2b: FALLBACK -- LLM-judge proxy identical to Condition B, in-run
# rescoring of both B's own rows and C's rows
# ============================================================================
async def call_openrouter_judge(
    session: aiohttp.ClientSession, sem: asyncio.Semaphore, source: str, mt: str, cfg: dict
) -> tuple[float | None, dict]:
    prompt = cfg["prompt_template"].format(source=source, mt=mt)
    payload = {
        "model": cfg["model_id"],
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": cfg["max_tokens"],
        "temperature": cfg["temperature"],
    }
    headers = {"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}", "Content-Type": "application/json"}
    async with sem:
        for attempt in range(4):
            try:
                async with session.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=60),
                ) as resp:
                    body = await resp.json()
                    if resp.status != 200:
                        logger.warning(f"OpenRouter non-200 (attempt {attempt}): {resp.status} {str(body)[:200]}")
                        await asyncio.sleep(2**attempt)
                        continue
                    usage = body.get("usage", {})
                    text = body["choices"][0]["message"]["content"]
                    m = re.search(r"[01](?:\.\d+)?|0?\.\d+", text)
                    score = max(0.0, min(1.0, float(m.group(0)))) if m else None
                    return score, {
                        "prompt_tokens": usage.get("prompt_tokens", 0),
                        "completion_tokens": usage.get("completion_tokens", 0),
                    }
            except (aiohttp.ClientError, asyncio.TimeoutError, KeyError, ValueError) as e:
                logger.warning(f"OpenRouter call failed (attempt {attempt}): {type(e).__name__}: {str(e)[:150]}")
                await asyncio.sleep(2**attempt)
        return None, {"prompt_tokens": 0, "completion_tokens": 0}


async def run_proxy_scoring(rows: list[dict], cfg: dict, cost_state: dict, concurrency: int = 8) -> list[dict]:
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency * 2)
    async with aiohttp.ClientSession(connector=connector) as session:
        for r in rows:
            if cost_state["cumulative_usd"] > COST_CAP_USD:
                logger.warning(f"Cost cap ${COST_CAP_USD} reached; stopping proxy scoring with partial results")
                break
            pre_score, pre_usage = await call_openrouter_judge(session, sem, r["source_text"], r["pre_repair_text"], cfg)
            post_score, post_usage = await call_openrouter_judge(
                session, sem, r["source_text"], r["post_repair_text"], cfg
            )
            cost = (
                (pre_usage["prompt_tokens"] + post_usage["prompt_tokens"]) * JUDGE_PRICE_IN_PER_TOK
                + (pre_usage["completion_tokens"] + post_usage["completion_tokens"]) * JUDGE_PRICE_OUT_PER_TOK
            )
            cost_state["cumulative_usd"] += cost
            r["proxy_before"] = pre_score
            r["proxy_after"] = post_score
            r["proxy_delta"] = (post_score - pre_score) if (pre_score is not None and post_score is not None) else None
    return rows


def run_fallback_path(
    natural_c_rows: list[dict], b_rows_for_rescore: list[dict], b_fidelity_config: dict, attempts_log: list[dict]
) -> dict:
    assert os.environ.get("OPENROUTER_API_KEY"), "OPENROUTER_API_KEY must be set for the LLM-judge fallback"
    cost_state = {"cumulative_usd": 0.0}

    logger.info(f"Fallback path: re-scoring {len(b_rows_for_rescore)} Condition-B rows with the identical proxy")
    b_rows_scored = asyncio.run(run_proxy_scoring(b_rows_for_rescore, b_fidelity_config, cost_state))
    logger.info(f"Cumulative cost after B rescoring: ${cost_state['cumulative_usd']:.4f}")

    logger.info(f"Fallback path: scoring {len(natural_c_rows)} Condition-C rows with the identical proxy")
    c_rows_scored = asyncio.run(run_proxy_scoring(natural_c_rows, b_fidelity_config, cost_state))
    logger.info(f"Cumulative cost after C scoring: ${cost_state['cumulative_usd']:.4f}")

    delta_proxy_b = [r["proxy_delta"] for r in b_rows_scored if r.get("proxy_delta") is not None]
    delta_proxy_c = [r["proxy_delta"] for r in c_rows_scored if r.get("proxy_delta") is not None]

    paired_bc = bootstrap_paired_difference(delta_proxy_c, delta_proxy_b)
    n_b_target = len(b_rows_for_rescore)
    n_c_target = len(natural_c_rows)
    partial_b = len(delta_proxy_b) < n_b_target
    partial_c = len(delta_proxy_c) < n_c_target

    return {
        "quality_metric_path_taken": "llm_judge_proxy_fallback_identical_to_condition_B",
        "attempts_log": attempts_log,
        "proxy_config_used": {k: v for k, v in b_fidelity_config.items() if k != "source_condition_metadata"},
        "condition_b_proxy_delta_pooled_mean_natural_rerun": (
            sum(delta_proxy_b) / len(delta_proxy_b) if delta_proxy_b else None
        ),
        "condition_b_n_rows_target": n_b_target,
        "condition_b_n_rows_scored": len(delta_proxy_b),
        "condition_b_partial": partial_b,
        "condition_c_proxy_delta_pooled_mean_natural": (
            sum(delta_proxy_c) / len(delta_proxy_c) if delta_proxy_c else None
        ),
        "condition_c_n_rows_target": n_c_target,
        "condition_c_n_rows_scored": len(delta_proxy_c),
        "condition_c_partial": partial_c,
        "condition_c_minus_condition_b_proxy_delta_unpaired_bootstrap": paired_bc,
        "cumulative_openrouter_cost_usd": cost_state["cumulative_usd"],
        "directly_comparable_to_C1_C2_real_comet_numbers": False,
        "directly_comparable_to": "Condition B, same-proxy, same-run rescoring only",
        "explicit_caveat": (
            "Real wmt22-cometkiwi-da was unreachable after mitigated attempts across "
            f"{len(WINDOW_OFFSETS_MIN)} time-separated windows and {len(ENDPOINTS)} endpoints "
            "(see attempts_log). This number is an LLM-judge proxy, identical in model/prompt/"
            "convention to Condition B's fidelity check, and must NOT be treated as numerically "
            "comparable to C1 or C2's real-COMET delta-COMET figures."
        ),
    }, b_rows_scored, c_rows_scored


# ============================================================================
# Main
# ============================================================================
@logger.catch(reraise=True)
def main() -> None:
    run_start = time.time()
    logger.info("=== Rescue Condition C's Missing Quality Score: starting ===")

    condition_c_path = find_condition_c()
    condition_b_path = find_condition_b()
    natural_c_rows = load_condition_c_rows(condition_c_path)
    logger.info(f"Loaded {len(natural_c_rows)} Condition-C natural rows from {condition_c_path}")
    b_fidelity_config = extract_b_fidelity_config(condition_b_path)
    logger.info(f"Extracted Condition-B proxy config (model={b_fidelity_config['model_id']})")
    b_rows_for_rescore = load_condition_b_rows_for_rescoring(condition_b_path, n_sample=len(natural_c_rows))
    logger.info(f"Sampled {len(b_rows_for_rescore)} Condition-B rows for identical-proxy rescoring (fallback-only)")

    checkpoint_dir, attempts_log = run_phase1_mitigation(run_start)
    real_comet_available = checkpoint_dir is not None

    if real_comet_available:
        logger.info(f"Real COMET obtained at {checkpoint_dir}; taking the real-COMET path")
        result, scored_rows = run_real_comet_path(checkpoint_dir, natural_c_rows, attempts_log)
        examples = [
            {
                "input": r["source_text"],
                "output": r["pre_repair_text"],
                "predict_c2_post_repair": r["post_repair_text"],
                "metadata_row_id": r["row_id"],
                "metadata_language_pair": r["language_pair"],
                "metadata_comet_before": r["comet_before"],
                "metadata_comet_after": r["comet_after"],
                "metadata_delta_comet": r["delta_comet"],
                "metadata_c2_certificate_achieved": r["certificate_achieved"],
                "metadata_c2_n_passes": r["n_passes"],
            }
            for r in scored_rows
        ]
        datasets = [{"dataset": "condition_c_natural_real_comet_rescore", "examples": examples}]
    else:
        logger.warning("Real COMET unobtainable within budget; taking the LLM-judge proxy fallback path")
        result, b_scored, c_scored = run_fallback_path(
            natural_c_rows, b_rows_for_rescore, b_fidelity_config, attempts_log
        )
        examples_c = [
            {
                "input": r["source_text"],
                "output": r["pre_repair_text"],
                "predict_c2_post_repair": r["post_repair_text"],
                "metadata_row_id": r["row_id"],
                "metadata_language_pair": r["language_pair"],
                "metadata_proxy_before": r.get("proxy_before"),
                "metadata_proxy_after": r.get("proxy_after"),
                "metadata_proxy_delta": r.get("proxy_delta"),
            }
            for r in c_scored
        ]
        examples_b = [
            {
                "input": r["source_text"],
                "output": r["pre_repair_text"],
                "predict_condition_b_repaired": r["post_repair_text"],
                "metadata_row_id": r["row_id"],
                "metadata_language_pair": r["language_pair"],
                "metadata_proxy_before": r.get("proxy_before"),
                "metadata_proxy_after": r.get("proxy_after"),
                "metadata_proxy_delta": r.get("proxy_delta"),
            }
            for r in b_scored
        ]
        datasets = [
            {"dataset": "condition_c_natural_proxy_fallback_rescore", "examples": examples_c},
            {"dataset": "condition_b_natural_proxy_fallback_rescore", "examples": examples_b},
        ]

    result["schema_version"] = "exp_gen_sol_out"
    result["method_name"] = "rescue_condition_c_missing_quality_score"
    result["condition_c_source_artifact"] = "art_6n9zJVKWXnio"
    result["condition_b_source_artifact"] = "art_G9ppuk8aHUhW"
    result["total_wallclock_s"] = time.time() - run_start

    output = {"metadata": result, "datasets": datasets}
    out_path = ROOT / "method_out.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")
    logger.info(f"quality_metric_path_taken = {result['quality_metric_path_taken']}")
    logger.info("=== Done ===")


if __name__ == "__main__":
    main()
