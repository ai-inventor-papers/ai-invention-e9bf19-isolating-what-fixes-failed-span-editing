#!/usr/bin/env python3
"""Does hygiene or checking fix span-editing? (gen_plan_experiment_3_idx3)

Implements and scores three matched conditions on identical rows from
en->ru_RU / en->uk_UA, using google/gemma-3-12b-it as the fixed repair model:

  B  -- faithful reproduction of Padmanabhan (2025)'s masked-fill
        severity-skip baseline (QE-span masking, single uncorrected LLM call,
        no post-processing).
  D  -- B plus a trivial HYGIENE retry filter (leftover placeholder / leaked
        instruction text triggers a single deterministic-free retry). No
        content checker involved.
  C1 -- the 4-category deterministic content-invariant checker flags every
        invariant span in the FULL sentence (not just QE spans) and repairs
        them all in one uncorrected pass (no re-verification against the
        checker after the repair call).

All three are scored identically: reference-free DeltaCOMET
(Unbabel/wmt22-cometkiwi-da) on the natural subsample, fix-rate / true
regression-rate (checker-verdict, against the wmt24pp clean reference) on the
injected-error subsample, edit volume, and LLM call/token/cost ledger.

See checker.py (4-category checker) and llm_client.py (OpenRouter client with
a live cost ledger) for the two main supporting modules.
"""

from __future__ import annotations

import asyncio
import gc
import json
import random
import re
import resource
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import psutil
from loguru import logger

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checker import CATEGORIES, Checker  # noqa: E402
from llm_client import BudgetExceededError, CostLedger, OpenRouterClient  # noqa: E402

# ============================================================================
# Config
# ============================================================================

WORKDIR = Path(__file__).resolve().parent
DATA_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/"
    "gen_art_dataset_1/data_out/full_data_out.json"
)

SEED = 42
LANG_PAIRS = ["en-ru_RU", "en-uk_UA"]  # -> checker lang keys "ru_RU"/"uk_UA"
LANG_KEY_OF_PAIR = {"en-ru_RU": "ru_RU", "en-uk_UA": "uk_UA"}
LANG_NAME_OF_PAIR = {"en-ru_RU": "Russian", "en-uk_UA": "Ukrainian"}

N_NATURAL_PER_PAIR = 160  # within the plan's ~150-200/pair range
N_INJECTED_PER_CELL = 30  # within the plan's <=40/cell cap

MODEL = "google/gemma-3-12b-it"
MAX_USD_BUDGET = 10.0
COST_HALT_THRESHOLD = 8.0  # fallback_plan: complete one language pair fully before starting the second if approaching $8

MAX_CONCURRENCY = 8
BOOTSTRAP_ITERS = 1000

HYGIENE_REGEX = re.compile(
    r"__BLANK__|__[A-Z]+__|\bCorrected words\b|\bHere is the corrected\b|\bHere's the corrected\b",
    re.IGNORECASE,
)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(WORKDIR / "logs" / "run.log", rotation="30 MB", level="DEBUG")


# ============================================================================
# Hardware / resource limits (aii-use-hardware)
# ============================================================================

def _container_ram_gb() -> float | None:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    return None


def setup_resource_limits() -> None:
    total_ram_gb = _container_ram_gb() or psutil.virtual_memory().total / 1e9
    ram_budget_gb = min(total_ram_gb * 0.75, 20.0)  # data (29MB) is tiny; generous headroom for COMET/Stanza/torch
    resource.setrlimit(
        resource.RLIMIT_AS, (int(ram_budget_gb * 3 * 1024**3), int(ram_budget_gb * 3 * 1024**3))
    )
    resource.setrlimit(resource.RLIMIT_CPU, (3 * 3600, 3 * 3600))
    logger.info(f"RAM budget set to {ram_budget_gb:.1f} GB (container total {total_ram_gb:.1f} GB)")


# ============================================================================
# Phase 0 -- Load + select scope
# ============================================================================

def load_data() -> dict:
    logger.info(f"Loading dataset from {DATA_PATH}")
    data = json.loads(DATA_PATH.read_text())
    return data


def index_examples(data: dict) -> dict[str, list[dict]]:
    by_dataset = {}
    for ds in data["datasets"]:
        by_dataset[ds["dataset"]] = ds["examples"]
    return by_dataset


def stratified_sample_natural(examples: list[dict], rng: random.Random) -> list[dict]:
    """Sample ~N_NATURAL_PER_PAIR rows/pair from the experimental_pool fold,
    balanced across domain."""
    selected = []
    for pair in LANG_PAIRS:
        pool = [
            (i, e) for i, e in enumerate(examples)
            if e["metadata_language_pair"] == pair and e["metadata_fold"] == "experimental_pool"
        ]
        by_domain = defaultdict(list)
        for i, e in pool:
            by_domain[e["metadata_domain"]].append((i, e))
        n_domains = len(by_domain)
        per_domain = max(1, N_NATURAL_PER_PAIR // max(1, n_domains))
        picked = []
        for dom, rows in by_domain.items():
            rng.shuffle(rows)
            picked.extend(rows[:per_domain])
        rng.shuffle(picked)
        picked = picked[:N_NATURAL_PER_PAIR]
        for i, e in picked:
            row = dict(e)
            row["_row_id"] = f"wmt25_task3_natural:{i}"
            selected.append(row)
        logger.info(f"Natural subsample [{pair}]: {len(picked)} rows across {n_domains} domains")
    return selected


def stratified_sample_injected(examples: list[dict], rng: random.Random, fold: str, n_per_cell: int | None) -> list[dict]:
    selected = []
    for pair in LANG_PAIRS:
        for cat in [
            "named_entity_swap", "number_unit_date_alteration",
            "negation_polarity_flip", "quantifier_substitution",
        ]:
            cell = [
                (i, e) for i, e in enumerate(examples)
                if e["metadata_language_pair"] == pair
                and e["metadata_fold"] == fold
                and e["metadata_invariant_category"] == cat
            ]
            rng.shuffle(cell)
            if n_per_cell is not None:
                cell = cell[:n_per_cell]
            for i, e in cell:
                row = dict(e)
                row["_row_id"] = f"injected_error_augmentation:{i}"
                selected.append(row)
            logger.info(f"Injected [{fold}] subsample [{pair},{cat}]: {len(cell)} rows")
    return selected


# ============================================================================
# Phase 1 -- Checker precision/recall validation on injected_heldout
# ============================================================================

def corrupted_span_offsets(row: dict) -> tuple[int, int]:
    """metadata_span_offsets in the dataset is indexed into
    metadata_clean_target_text (start = end of the unchanged prefix, end =
    start + len(original_span)) -- NOT into the corrupted `output` text. The
    prefix up to `start` is byte-identical between clean and corrupted text
    (single-span substitution), so `start` is valid in BOTH coordinate
    systems, but the correct end offset INTO `output` is
    start + len(corrupted_span), not the dataset's `end` (which is
    start + len(original_span)). Verified directly against the data:
    row['output'][start : start+len(corrupted_span)] == corrupted_span for
    every category, including the empty-string (deletion) case.
    """
    off = row["metadata_span_offsets"]
    start = off["start"]
    end = start + len(row["metadata_corrupted_span"])
    return start, end


CATEGORY_MAP_INJECTED_TO_CHECKER = {
    "named_entity_swap": "named_entity",
    "number_unit_date_alteration": "number_unit_date",
    "negation_polarity_flip": "negation_polarity",
    "quantifier_substitution": "quantifier_scope",
}


def validate_checker(checker: Checker, heldout_rows: list[dict]) -> dict:
    """Precision/recall per (lang, category) cell, defined as:
      recall_cell    = P(checker flags overlap the row's known corrupted span | row in cell)
      precision_cell = (# flagged spans across cell rows overlapping the known corrupted span)
                        / (# total flagged spans across cell rows)
    This is a CONSERVATIVE precision estimate: the heldout fold only labels the
    ONE span that was deliberately corrupted per row, so every other genuine
    entity/number/negation/quantifier the detector correctly flags in the same
    sentence is counted against precision. Documented explicitly rather than
    silently treated as a true false-positive rate.
    """
    cells = defaultdict(lambda: {"tp_recall": 0, "n_rows": 0, "tp_precision": 0, "n_flags": 0})
    for row in heldout_rows:
        pair = row["metadata_language_pair"]
        lang = LANG_KEY_OF_PAIR[pair]
        cat_injected = row["metadata_invariant_category"]
        cat = CATEGORY_MAP_INJECTED_TO_CHECKER[cat_injected]
        key = (lang, cat)
        cells[key]["n_rows"] += 1
        source = row["input"]
        hyp = row["output"]
        gt_start, gt_end = corrupted_span_offsets(row)
        try:
            spans = checker.detect_category(cat, source, hyp, lang)
        except Exception as e:
            logger.error(f"Checker failed on row {row['_row_id']} cat={cat} lang={lang}: {e}")
            spans = []
        overlapped = any(s.start < gt_end and gt_start < s.end for s in spans)
        if overlapped:
            cells[key]["tp_recall"] += 1
        cells[key]["n_flags"] += len(spans)
        cells[key]["tp_precision"] += sum(1 for s in spans if s.start < gt_end and gt_start < s.end)

    results = {}
    for (lang, cat), c in cells.items():
        recall = c["tp_recall"] / c["n_rows"] if c["n_rows"] else 0.0
        precision = c["tp_precision"] / c["n_flags"] if c["n_flags"] else 0.0
        results[f"{lang}|{cat}"] = {
            "lang": lang, "category": cat, "n_rows": c["n_rows"],
            "recall": round(recall, 4), "precision": round(precision, 4),
            "n_flags_total": c["n_flags"],
        }
    return results


def excluded_cells_from_validation(validation: dict) -> set[tuple[str, str]]:
    excluded = set()
    for v in validation.values():
        if v["recall"] < 0.5 or v["precision"] < 0.5:
            excluded.add((v["lang"], v["category"]))
    return excluded


# ============================================================================
# Masking (Algorithm 1 severity-skip heuristic)
# ============================================================================

def apply_severity_skip_mask(output_text: str, qe_spans: list[dict] | None) -> tuple[str, list[dict], bool]:
    """Returns (masked_text, surviving_spans, did_mask).

    Verbatim per the plan's pseudocode: if any span with severity != 'minor'
    exists in the sentence, skip (do not mask) all minor-severity spans;
    otherwise mask minor spans too.
    """
    if not qe_spans:
        return output_text, [], False
    has_non_minor = any(s["severity"] != "minor" for s in qe_spans)
    surviving = [s for s in qe_spans if not (has_non_minor and s["severity"] == "minor")]
    if not surviving:
        return output_text, [], False
    # Guard against overlaps/out-of-range spans -- keep first-seen, non-overlapping, in-range spans only.
    surviving_sorted = sorted(surviving, key=lambda s: s["start_i"])
    kept = []
    last_end = -1
    for s in surviving_sorted:
        st, en = s["start_i"], s["end_i"]
        if st < last_end or st < 0 or en > len(output_text) or en <= st:
            continue
        kept.append(s)
        last_end = en
    if not kept:
        return output_text, [], False
    masked = output_text
    for s in sorted(kept, key=lambda s: s["start_i"], reverse=True):
        masked = masked[: s["start_i"]] + "__BLANK__" + masked[s["end_i"] :]
    return masked, kept, True


MASK_PROMPT_TEMPLATE = """You are given an English source sentence and its translation into {lang_name}. Some words or phrases in the translation have been removed and replaced with the placeholder token __BLANK__ (one placeholder per removed span). Fill in each __BLANK__ with the correct {lang_name} text so the completed translation is fluent and faithful to the source sentence. Output ONLY the completed translation text with every __BLANK__ replaced by real text, and nothing else -- no explanation, no notes, no metadata, no list of corrected words.

Source (English):
{source}

Masked translation ({lang_name}):
{masked}

Completed translation ({lang_name}):"""


def build_mask_prompt(source: str, masked_text: str, lang_name: str) -> str:
    return MASK_PROMPT_TEMPLATE.format(source=source, masked=masked_text, lang_name=lang_name)


C1_PROMPT_TEMPLATE = """You are given an English source sentence and its {lang_name} translation. An automated checker has flagged the following spans in the translation as content-invariant elements (named entities, numbers/units/dates, negation markers, or quantifiers) that must be verified against the source. For EACH flagged span: compare it to the source sentence: if it does not correctly correspond to the source content (e.g. a swapped name, an altered number, a flipped negation, a changed quantifier), correct it so it does. If it already correctly corresponds to the source, leave it unchanged. Do not change any other part of the translation.

Source (English):
{source}

Translation ({lang_name}):
{hyp}

Flagged spans:
{flags_list}

Output ONLY the corrected translation text, and nothing else -- no explanation, no notes."""


def build_c1_prompt(source: str, hyp: str, flags: list, lang_name: str) -> str:
    lines = []
    for f in flags:
        lines.append(f'- [{f.category}] "{f.text}" (position {f.start}-{f.end})')
    return C1_PROMPT_TEMPLATE.format(source=source, hyp=hyp, flags_list="\n".join(lines), lang_name=lang_name)


def has_leakage(text: str) -> bool:
    return bool(HYGIENE_REGEX.search(text))


def word_edit_distance(a: str, b: str) -> int:
    aw, bw = a.split(), b.split()
    n, m = len(aw), len(bw)
    if n == 0:
        return m
    if m == 0:
        return n
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            cost = 0 if aw[i - 1] == bw[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    return prev[m]


def edit_volume(original: str, edited: str) -> float:
    n = max(1, len(original.split()))
    return word_edit_distance(original, edited) / n


# ============================================================================
# Condition pipelines
# ============================================================================

async def run_condition_B(row: dict, client: OpenRouterClient, source: str, output_text: str,
                            qe_spans: list[dict] | None, lang_name: str, row_id: str) -> dict:
    masked_text, surviving, did_mask = apply_severity_skip_mask(output_text, qe_spans)
    if not did_mask:
        return {"output": output_text, "n_llm_calls": 0, "spans_masked": 0, "no_op": True,
                "leakage": False, "error": None}
    prompt = build_mask_prompt(source, masked_text, lang_name)
    result = await client.call(MODEL, prompt, temperature=0.0, max_tokens=1024,
                                 meta={"row_id": row_id, "condition": "B"})
    repaired = result["text"].strip() if result["success"] and result["text"].strip() else output_text
    return {
        "output": repaired, "n_llm_calls": 1, "spans_masked": len(surviving), "no_op": False,
        "leakage": has_leakage(repaired), "error": result["error"],
        "input_tokens": result["input_tokens"], "output_tokens": result["output_tokens"],
    }


async def run_condition_D(row: dict, client: OpenRouterClient, source: str, output_text: str,
                            qe_spans: list[dict] | None, lang_name: str, row_id: str) -> dict:
    masked_text, surviving, did_mask = apply_severity_skip_mask(output_text, qe_spans)
    if not did_mask:
        return {"output": output_text, "n_llm_calls": 0, "spans_masked": 0, "no_op": True,
                "hygiene_triggered": False, "leakage": False, "error": None}
    prompt = build_mask_prompt(source, masked_text, lang_name)
    result = await client.call(MODEL, prompt, temperature=0.0, max_tokens=1024,
                                 meta={"row_id": row_id, "condition": "D", "attempt": 1})
    out1 = result["text"].strip() if result["success"] and result["text"].strip() else output_text
    n_calls = 1
    in_tok, out_tok = result["input_tokens"], result["output_tokens"]
    hygiene_triggered = has_leakage(out1)
    final_output = out1
    if hygiene_triggered:
        # Retry at temperature=0.3: a temperature=0 retry of the identical
        # prompt to the same model is deterministic-identical and would just
        # reproduce the same leakage, so a non-zero retry temperature is the
        # only choice that can plausibly change the outcome (documented here
        # per the plan's explicit "document choice" instruction).
        retry_result = await client.call(MODEL, prompt, temperature=0.3, max_tokens=1024,
                                           meta={"row_id": row_id, "condition": "D", "attempt": 2})
        n_calls += 1
        in_tok += retry_result["input_tokens"]
        out_tok += retry_result["output_tokens"]
        final_output = retry_result["text"].strip() if retry_result["success"] and retry_result["text"].strip() else out1
    return {
        "output": final_output, "n_llm_calls": n_calls, "spans_masked": len(surviving), "no_op": False,
        "hygiene_triggered": hygiene_triggered, "leakage": has_leakage(final_output), "error": result["error"],
        "input_tokens": in_tok, "output_tokens": out_tok,
    }


async def run_condition_C1(row: dict, client: OpenRouterClient, checker: Checker, source: str,
                             output_text: str, lang: str, lang_name: str, row_id: str) -> dict:
    flags = checker.detect_all(source, output_text, lang, respect_exclusions=True)
    if not flags:
        return {"output": output_text, "n_llm_calls": 0, "n_flags": 0, "flag_categories": [],
                "no_op": True, "leakage": False, "error": None}
    prompt = build_c1_prompt(source, output_text, flags, lang_name)
    result = await client.call(MODEL, prompt, temperature=0.0, max_tokens=1536,
                                 meta={"row_id": row_id, "condition": "C1"})
    repaired = result["text"].strip() if result["success"] and result["text"].strip() else output_text
    return {
        "output": repaired, "n_llm_calls": 1, "n_flags": len(flags),
        "flag_categories": sorted({f.category for f in flags}), "no_op": False,
        "leakage": has_leakage(repaired), "error": result["error"],
        "input_tokens": result["input_tokens"], "output_tokens": result["output_tokens"],
    }


# ============================================================================
# Injected-pool: oracle-localized B/D (no native QE signal), checker-localized C1
# ============================================================================

def oracle_qe_span(row: dict) -> list[dict]:
    start, end = corrupted_span_offsets(row)
    return [{"start_i": start, "end_i": end, "severity": "major"}]


def invariant_multiset(source_text: str, text: str, lang: str, checker: Checker) -> Counter:
    spans = checker.detect_all(source_text, text, lang, respect_exclusions=True)
    return Counter((s.category, s.text.strip().lower()) for s in spans)


def compute_fix_and_regression(row: dict, repaired_output: str, lang: str, checker: Checker) -> dict:
    source = row["input"]
    corrupted_span = row["metadata_corrupted_span"]
    clean_target = row["metadata_clean_target_text"]
    fixed = corrupted_span not in repaired_output
    gold_ms = invariant_multiset(source, clean_target, lang, checker)
    repaired_ms = invariant_multiset(source, repaired_output, lang, checker)
    lost = sum((gold_ms - repaired_ms).values())
    corrupted_ms = invariant_multiset(source, row["output"], lang, checker)
    lost_baseline = sum((gold_ms - corrupted_ms).values())
    return {
        "fixed": fixed,
        "invariants_lost_vs_gold": int(lost),
        "invariants_lost_vs_gold_baseline": int(lost_baseline),
        "true_regression": lost > lost_baseline,
    }


async def process_injected_row(row: dict, client: OpenRouterClient, checker: Checker) -> dict:
    pair = row["metadata_language_pair"]
    lang = LANG_KEY_OF_PAIR[pair]
    lang_name = LANG_NAME_OF_PAIR[pair]
    source = row["input"]
    corrupted_hyp = row["output"]
    row_id = row["_row_id"]

    oracle_spans = oracle_qe_span(row)
    out = {"row_id": row_id, "language_pair": pair, "category": row["metadata_invariant_category"]}
    try:
        b = await run_condition_B(row, client, source, corrupted_hyp, oracle_spans, lang_name, row_id)
        out["B"] = {**b, **compute_fix_and_regression(row, b["output"], lang, checker)}
    except BudgetExceededError:
        raise
    except Exception as e:
        logger.error(f"Condition B failed on injected row {row_id}: {e}")
        out["B"] = {"error": str(e)}

    try:
        d = await run_condition_D(row, client, source, corrupted_hyp, oracle_spans, lang_name, row_id)
        out["D"] = {**d, **compute_fix_and_regression(row, d["output"], lang, checker)}
    except BudgetExceededError:
        raise
    except Exception as e:
        logger.error(f"Condition D failed on injected row {row_id}: {e}")
        out["D"] = {"error": str(e)}

    try:
        c1 = await run_condition_C1(row, client, checker, source, corrupted_hyp, lang, lang_name, row_id)
        out["C1"] = {**c1, **compute_fix_and_regression(row, c1["output"], lang, checker)}
    except BudgetExceededError:
        raise
    except Exception as e:
        logger.error(f"Condition C1 failed on injected row {row_id}: {e}")
        out["C1"] = {"error": str(e)}

    return out


async def process_natural_row(row: dict, client: OpenRouterClient, checker: Checker) -> dict:
    pair = row["metadata_language_pair"]
    lang = LANG_KEY_OF_PAIR[pair]
    lang_name = LANG_NAME_OF_PAIR[pair]
    source = row["input"]
    hyp = row["output"]
    qe_spans = row.get("metadata_qe_flagged_spans")
    row_id = row["_row_id"]

    out = {"row_id": row_id, "language_pair": pair, "domain": row["metadata_domain"], "original": hyp}
    for cond, coro in [
        ("B", run_condition_B(row, client, source, hyp, qe_spans, lang_name, row_id)),
        ("D", run_condition_D(row, client, source, hyp, qe_spans, lang_name, row_id)),
        ("C1", run_condition_C1(row, client, checker, source, hyp, lang, lang_name, row_id)),
    ]:
        try:
            res = await coro
            res["edit_volume"] = round(edit_volume(hyp, res["output"]), 4)
            out[cond] = res
        except BudgetExceededError:
            raise
        except Exception as e:
            logger.error(f"Condition {cond} failed on natural row {row_id}: {e}")
            out[cond] = {"error": str(e)}
    return out


async def run_pipeline(natural_rows: list[dict], injected_rows: list[dict], checker: Checker,
                         ledger: CostLedger) -> tuple[list[dict], list[dict]]:
    natural_results, injected_results = [], []
    async with OpenRouterClient(ledger, max_concurrency=MAX_CONCURRENCY) as client:
        # Process per-language-pair so a budget/time halt still leaves complete
        # coverage for at least one pair (fallback_plan).
        for pair in LANG_PAIRS:
            if ledger.would_exceed(0.0) and ledger.spent_usd >= COST_HALT_THRESHOLD:
                logger.warning(f"Halting before language pair {pair}: cost ledger ${ledger.spent_usd:.4f}")
                break
            nat_pair = [r for r in natural_rows if r["metadata_language_pair"] == pair]
            inj_pair = [r for r in injected_rows if r["metadata_language_pair"] == pair]
            logger.info(f"Processing {pair}: {len(nat_pair)} natural, {len(inj_pair)} injected rows")

            sem_batches_nat = await asyncio.gather(
                *[process_natural_row(r, client, checker) for r in nat_pair], return_exceptions=True
            )
            for r in sem_batches_nat:
                if isinstance(r, BudgetExceededError):
                    logger.warning("Budget exceeded during natural-row processing; stopping.")
                    break
                if isinstance(r, Exception):
                    logger.error(f"Unhandled error in natural row: {r}")
                    continue
                natural_results.append(r)

            sem_batches_inj = await asyncio.gather(
                *[process_injected_row(r, client, checker) for r in inj_pair], return_exceptions=True
            )
            for r in sem_batches_inj:
                if isinstance(r, BudgetExceededError):
                    logger.warning("Budget exceeded during injected-row processing; stopping.")
                    break
                if isinstance(r, Exception):
                    logger.error(f"Unhandled error in injected row: {r}")
                    continue
                injected_results.append(r)

            logger.info(f"Cost ledger after {pair}: {ledger.summary()}")
    return natural_results, injected_results


# ============================================================================
# Phase 5 -- COMET scoring
# ============================================================================

def try_load_comet():
    try:
        import comet

        logger.info("Downloading/loading Unbabel/wmt22-cometkiwi-da checkpoint...")
        model_path = comet.download_model("Unbabel/wmt22-cometkiwi-da")
        model = comet.load_from_checkpoint(model_path)
        logger.info("COMET checkpoint loaded successfully.")
        return model
    except Exception as e:
        logger.warning(f"COMET (Unbabel/wmt22-cometkiwi-da) unavailable: {e}. Falling back to a non-gated proxy.")
        return None


def comet_score_batch(model, sources: list[str], hyps: list[str]) -> list[float]:
    import torch

    gpus = 1 if torch.cuda.is_available() else 0
    data = [{"src": s, "mt": h} for s, h in zip(sources, hyps)]
    out = model.predict(data, batch_size=16, gpus=gpus, progress_bar=False)
    return list(out.scores)


def char_trigram_jaccard(a: str, b: str) -> float:
    def trigrams(s: str) -> set[str]:
        s = s.strip()
        return {s[i : i + 3] for i in range(max(0, len(s) - 2))} or {s}

    ta, tb = trigrams(a), trigrams(b)
    if not ta and not tb:
        return 1.0
    return len(ta & tb) / len(ta | tb)


def proxy_qe_score(source: str, hyp: str) -> float:
    """DeltaCOMET-proxy fallback: NOT COMET. Character-trigram Jaccard overlap
    between hyp and source is meaningless across scripts (en vs ru/uk), so
    instead this scores internal well-formedness only: fraction of the
    hypothesis retained relative to itself is not applicable pre/post-edit
    scoring needs a stable reference -- so the proxy compares hyp length
    plausibility (chars-per-source-char ratio, clipped) as an extremely weak
    fluency/completeness signal. Always reported under the
    'DeltaCOMET-proxy' label, never as 'DeltaCOMET'.
    """
    ratio = len(hyp.strip()) / max(1, len(source.strip()))
    # Plausible translation length ratios en->ru/uk are roughly 0.8-1.3x source chars.
    return max(0.0, 1.0 - abs(ratio - 1.0))


def bootstrap_ci(values: list[float], iters: int, rng: random.Random) -> tuple[float, float, float]:
    if not values:
        return (0.0, 0.0, 0.0)
    n = len(values)
    mean = sum(values) / n
    boots = []
    for _ in range(iters):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        boots.append(sum(sample) / n)
    boots.sort()
    lo = boots[int(0.025 * iters)]
    hi = boots[min(iters - 1, int(0.975 * iters))]
    return (mean, lo, hi)


# ============================================================================
# Main
# ============================================================================

def summarize_conditions(natural_results: list[dict], injected_results: list[dict], validation: dict,
                           excluded: set, comet_available: bool,
                           natural_comet: dict, ledger: CostLedger, checker_leakage_B: float) -> dict:
    conditions = ["B", "D", "C1"]
    per_pair_metrics = defaultdict(lambda: defaultdict(dict))
    pooled_metrics = defaultdict(dict)

    rng = random.Random(SEED)

    # --- natural: DeltaCOMET (or proxy) + edit volume ---
    for cond in conditions:
        for pair in LANG_PAIRS:
            deltas = natural_comet.get(pair, {}).get(cond, [])
            mean, lo, hi = bootstrap_ci(deltas, BOOTSTRAP_ITERS, rng)
            per_pair_metrics[pair][cond]["delta_comet_mean"] = mean
            per_pair_metrics[pair][cond]["delta_comet_ci95"] = [lo, hi]
            per_pair_metrics[pair][cond]["n_scored"] = len(deltas)
            evs = [r[cond]["edit_volume"] for r in natural_results
                   if r["language_pair"] == pair and "edit_volume" in r.get(cond, {})]
            per_pair_metrics[pair][cond]["edit_volume_mean"] = round(sum(evs) / len(evs), 4) if evs else None
            calls = [r[cond].get("n_llm_calls", 0) for r in natural_results if r["language_pair"] == pair]
            per_pair_metrics[pair][cond]["n_llm_calls_mean"] = round(sum(calls) / len(calls), 4) if calls else None

        all_deltas = [v for pair in LANG_PAIRS for v in natural_comet.get(pair, {}).get(cond, [])]
        mean, lo, hi = bootstrap_ci(all_deltas, BOOTSTRAP_ITERS, rng)
        pooled_metrics[cond]["delta_comet_mean"] = mean
        pooled_metrics[cond]["delta_comet_ci95"] = [lo, hi]
        pooled_metrics[cond]["n_scored"] = len(all_deltas)

    # --- injected: fix_rate / true_regression_rate ---
    for cond in conditions:
        for pair in LANG_PAIRS:
            rows = [r for r in injected_results if r["language_pair"] == pair and cond in r and "fixed" in r[cond]]
            fixed = [r[cond]["fixed"] for r in rows]
            regressed = [r[cond]["true_regression"] for r in rows]
            per_pair_metrics[pair][cond]["fix_rate"] = round(sum(fixed) / len(fixed), 4) if fixed else None
            per_pair_metrics[pair][cond]["true_regression_rate"] = round(sum(regressed) / len(regressed), 4) if regressed else None
            per_pair_metrics[pair][cond]["n_injected_scored"] = len(rows)
        rows_all = [r for r in injected_results if cond in r and "fixed" in r[cond]]
        fixed_all = [r[cond]["fixed"] for r in rows_all]
        regressed_all = [r[cond]["true_regression"] for r in rows_all]
        pooled_metrics[cond]["fix_rate"] = round(sum(fixed_all) / len(fixed_all), 4) if fixed_all else None
        pooled_metrics[cond]["true_regression_rate"] = round(sum(regressed_all) / len(regressed_all), 4) if regressed_all else None
        pooled_metrics[cond]["n_injected_scored"] = len(rows_all)

    return {
        "per_language_pair": {p: dict(v) for p, v in per_pair_metrics.items()},
        "pooled": dict(pooled_metrics),
    }


@logger.catch(reraise=True)
def main():
    t0 = time.time()
    setup_resource_limits()
    rng = random.Random(SEED)

    data = load_data()
    by_dataset = index_examples(data)
    natural_all = by_dataset["wmt25_task3_natural"]
    injected_all = by_dataset["injected_error_augmentation"]

    natural_rows = stratified_sample_natural(natural_all, rng)
    injected_pool_rows = stratified_sample_injected(injected_all, rng, "experimental_pool", N_INJECTED_PER_CELL)
    injected_heldout_rows = stratified_sample_injected(injected_all, rng, "checker_validation_heldout", None)

    (WORKDIR / "selected_rows.json").write_text(json.dumps({
        "seed": SEED,
        "natural_row_ids": [r["_row_id"] for r in natural_rows],
        "injected_pool_row_ids": [r["_row_id"] for r in injected_pool_rows],
        "injected_heldout_row_ids": [r["_row_id"] for r in injected_heldout_rows],
    }, indent=2))
    logger.info(
        f"Selected {len(natural_rows)} natural, {len(injected_pool_rows)} injected-pool, "
        f"{len(injected_heldout_rows)} injected-heldout rows"
    )

    del natural_all, injected_all
    gc.collect()

    # --- Phase 1: build + validate checker ---
    checker_unrestricted = Checker(excluded_cells=set())
    logger.info("Running checker unit smoke test on 2 hand-picked heldout rows/category/lang...")
    smoke_ok = 0
    smoke_rows = defaultdict(list)
    for r in injected_heldout_rows:
        smoke_rows[(r["metadata_language_pair"], r["metadata_invariant_category"])].append(r)
    for key, rows in smoke_rows.items():
        for r in rows[:2]:
            lang = LANG_KEY_OF_PAIR[r["metadata_language_pair"]]
            cat = CATEGORY_MAP_INJECTED_TO_CHECKER[r["metadata_invariant_category"]]
            gt_start, gt_end = corrupted_span_offsets(r)
            try:
                flagged = checker_unrestricted.is_flagged(cat, r["input"], r["output"], lang, gt_start, gt_end)
                smoke_ok += 1 if flagged else 0
            except Exception as e:
                logger.error(f"Smoke test error {key}: {e}")
    logger.info(f"Checker smoke test: flagged the known corrupted span in {smoke_ok} spot-checks")

    logger.info("Running full checker validation on injected_heldout fold...")
    validation = validate_checker(checker_unrestricted, injected_heldout_rows)
    excluded = excluded_cells_from_validation(validation)
    logger.info(f"Checker validation: {json.dumps(validation, indent=2)}")
    logger.info(f"Excluded cells (recall<0.5 or precision<0.5): {sorted(excluded)}")

    checker = Checker(excluded_cells=excluded)

    # --- Phase 2-4: run B / D / C1 on natural + injected-pool rows ---
    ledger = CostLedger(cap_usd=MAX_USD_BUDGET)
    natural_results, injected_results = asyncio.run(
        run_pipeline(natural_rows, injected_pool_rows, checker, ledger)
    )
    logger.info(f"Pipeline complete. Cost ledger: {ledger.summary()}")

    # --- B fidelity sanity check: leakage rate ---
    # NOTE: run_condition_B always sets an "error" key (None on success), so
    # membership-testing "error" in r["B"] is always True -- the value must be
    # checked instead, or every row is (silently) filtered out.
    b_masked = [
        r for r in natural_results
        if "B" in r and r["B"].get("error") is None and not r["B"].get("no_op", True)
    ]
    b_leaks_masked = [r["B"]["leakage"] for r in b_masked]
    leakage_rate = sum(b_leaks_masked) / len(b_leaks_masked) if b_leaks_masked else 0.0
    logger.info(
        f"Condition B leakage rate (of masked rows): {leakage_rate:.4f} "
        f"({sum(b_leaks_masked)}/{len(b_leaks_masked)}). Padmanabhan's original 9B model showed "
        f"substantial literal-placeholder/metadata leakage; a near-zero rate here indicates google/"
        f"gemma-3-12b-it is materially more instruction-following, which is a FIDELITY CAVEAT on any "
        f"comparison of B's DeltaCOMET against the paper's reported -0.0108 (documented, not silently proceeded past)."
    )

    # --- Phase 5: COMET scoring on natural rows ---
    comet_model = try_load_comet()
    comet_available = comet_model is not None
    natural_comet = {p: {"B": [], "D": [], "C1": []} for p in LANG_PAIRS}
    row_source_cache = {r["_row_id"]: r["input"] for r in natural_rows}

    if comet_available:
        for pair in LANG_PAIRS:
            pair_rows = [r for r in natural_results if r["language_pair"] == pair]
            sources = [row_source_cache[r["row_id"]] for r in pair_rows]
            originals = [r["original"] for r in pair_rows]
            orig_scores = comet_score_batch(comet_model, sources, originals)
            for cond in ["B", "D", "C1"]:
                edited = [r[cond]["output"] if cond in r and "output" in r[cond] else r["original"] for r in pair_rows]
                edited_scores = comet_score_batch(comet_model, sources, edited)
                deltas = [e - o for e, o in zip(edited_scores, orig_scores)]
                natural_comet[pair][cond] = deltas
            del sources, originals, orig_scores
            gc.collect()
        del comet_model
        gc.collect()
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    else:
        for pair in LANG_PAIRS:
            pair_rows = [r for r in natural_results if r["language_pair"] == pair]
            sources = [row_source_cache[r["row_id"]] for r in pair_rows]
            originals = [r["original"] for r in pair_rows]
            orig_scores = [proxy_qe_score(s, o) for s, o in zip(sources, originals)]
            for cond in ["B", "D", "C1"]:
                edited = [r[cond]["output"] if cond in r and "output" in r[cond] else r["original"] for r in pair_rows]
                edited_scores = [proxy_qe_score(s, e) for s, e in zip(sources, edited)]
                deltas = [e - o for e, o in zip(edited_scores, orig_scores)]
                natural_comet[pair][cond] = deltas

    metrics = summarize_conditions(natural_results, injected_results, validation, excluded,
                                     comet_available, natural_comet, ledger, leakage_rate)

    # --- STOP/reproduce verdict ---
    padmanabhan_delta = -0.0108
    b_pooled = metrics["pooled"].get("B", {}).get("delta_comet_mean")
    if b_pooled is not None:
        same_direction = b_pooled < 0
        magnitude_ratio = abs(b_pooled) / abs(padmanabhan_delta) if padmanabhan_delta else None
    else:
        same_direction, magnitude_ratio = None, None
    reproduce_verdict = {
        "padmanabhan_reported_delta_comet": padmanabhan_delta,
        "condition_B_pooled_delta_comet_mean": b_pooled,
        "same_direction": same_direction,
        "magnitude_ratio_vs_paper": magnitude_ratio,
        "caveats": [
            "Substitute repair model (google/gemma-3-12b-it) differs from the paper's Tower-Plus-9B "
            "(TowerPlus-9B and the plan's fallback google/gemma-2-9b-it are both confirmed absent from "
            "OpenRouter -- see the resource dossier, art_5ySTX4YfxqG_).",
            f"Condition B leakage rate on masked rows was {leakage_rate:.4f}; the paper attributes its "
            "entire -0.0108 result to prompt-following failure and literal-placeholder leakage, so a "
            "low leakage rate here is expected to move DeltaCOMET toward a smaller (less negative) magnitude, "
            "not to falsify replication.",
            "This is fidelity EVIDENCE, not proof: language-pair coverage (ru_RU/uk_UA only, vs the "
            "paper's 6-pair average), and masking prompt text was reconstructed from the dossier's "
            "described Algorithm 1 (QE-span-driven severity-skip masking), not quoted verbatim from the "
            "paper (the dossier's structured output did not carry the literal prompt string).",
        ],
        "comet_available": comet_available,
        "delta_comet_metric": "Unbabel/wmt22-cometkiwi-da" if comet_available else "DeltaCOMET-proxy (NOT COMET; see proxy_qe_score docstring)",
    }

    checker_validation_out = {
        "per_cell": validation,
        "excluded_cells": [f"{lang}|{cat}" for lang, cat in sorted(excluded)],
        "precision_definition_caveat": (
            "Precision is computed against the SINGLE known-corrupted span per heldout row; every other "
            "genuine invariant span the detector also (correctly) flags in that sentence counts against "
            "precision, so these numbers are a conservative lower bound on true localization precision, "
            "not an unbiased estimate."
        ),
    }

    elapsed = time.time() - t0
    logger.info(f"Total runtime: {elapsed:.1f}s. Assembling method_out.json...")

    # ------------------------------------------------------------------
    # Assemble exp_gen_sol_out.json-schema-compliant output
    # ------------------------------------------------------------------
    def natural_example(row: dict) -> dict:
        ex = {
            "input": f"[{row['language_pair']}] {row_source_cache.get(row['row_id'], '')}",
            "output": row["original"],
            "metadata_row_id": row["row_id"],
            "metadata_language_pair": row["language_pair"],
            "metadata_domain": row["domain"],
        }
        for cond in ["B", "D", "C1"]:
            c = row.get(cond, {})
            ex[f"predict_{cond.lower()}"] = c["output"] if c.get("error") is None and "output" in c else row["original"]
            ex[f"metadata_{cond.lower()}_n_llm_calls"] = c.get("n_llm_calls")
            ex[f"metadata_{cond.lower()}_edit_volume"] = c.get("edit_volume")
            ex[f"metadata_{cond.lower()}_leakage"] = c.get("leakage")
            ex[f"metadata_{cond.lower()}_no_op"] = c.get("no_op")
            if cond == "D":
                ex["metadata_d_hygiene_triggered"] = c.get("hygiene_triggered")
            if cond == "C1":
                ex["metadata_c1_n_flags"] = c.get("n_flags")
                ex["metadata_c1_flag_categories"] = c.get("flag_categories")
            if c.get("error") is not None:
                ex[f"metadata_{cond.lower()}_error"] = c["error"]
        return ex

    def injected_example(row: dict) -> dict:
        rid = row["row_id"]
        src_row = next((r for r in injected_pool_rows if r["_row_id"] == rid), None)
        source_text = src_row["input"] if src_row else ""
        corrupted_hyp = src_row["output"] if src_row else ""
        ex = {
            "input": f"[{row['language_pair']}/{row['category']}] {source_text}",
            "output": corrupted_hyp,
            "metadata_row_id": rid,
            "metadata_language_pair": row["language_pair"],
            "metadata_invariant_category": row["category"],
        }
        for cond in ["B", "D", "C1"]:
            c = row.get(cond, {})
            ex[f"predict_{cond.lower()}"] = c["output"] if c.get("error") is None and "output" in c else corrupted_hyp
            ex[f"metadata_{cond.lower()}_fixed"] = c.get("fixed")
            ex[f"metadata_{cond.lower()}_true_regression"] = c.get("true_regression")
            ex[f"metadata_{cond.lower()}_n_llm_calls"] = c.get("n_llm_calls")
            if c.get("error") is not None:
                ex[f"metadata_{cond.lower()}_error"] = c["error"]
        return ex

    output = {
        "metadata": {
            "method_name": "hygiene_vs_checking_span_editing",
            "description": (
                "Three matched span-editing conditions (B: faithful masked-fill severity-skip baseline; "
                "D: B + trivial hygiene retry filter; C1: 4-category checker-broadened single uncorrected "
                "repair pass) on identical en-ru_RU/en-uk_UA rows, scored for DeltaCOMET (natural subsample), "
                "fix_rate/true_regression_rate (injected-pool subsample, checker-verdict against wmt24pp clean "
                "reference), edit_volume, and LLM cost."
            ),
            "repair_model": MODEL,
            "seed": SEED,
            "language_pairs": LANG_PAIRS,
            "n_natural_per_pair_target": N_NATURAL_PER_PAIR,
            "n_injected_per_cell_target": N_INJECTED_PER_CELL,
            "n_natural_rows_processed": len(natural_results),
            "n_injected_pool_rows_processed": len(injected_results),
            "n_injected_heldout_rows": len(injected_heldout_rows),
            "checker_validation": checker_validation_out,
            "condition_B_leakage_rate_sanity_check": leakage_rate,
            "reproduce_verdict": reproduce_verdict,
            "metrics": metrics,
            "cost_ledger": ledger.summary(),
            "runtime_seconds": round(elapsed, 1),
            "injected_pool_localization_protocol_caveat": (
                "Injected rows carry no native QE signal, so conditions B and D use an ORACLE QE span "
                "(the row's known corrupted-span offsets, severity='major') as their masking input on the "
                "injected-pool subset -- this isolates repair-GENERATION fidelity (B vs D) from localization "
                "quality. Condition C1 instead uses its own checker-based localization (no oracle) on the "
                "injected-pool subset, so C1's injected-pool fix_rate additionally reflects real checker "
                "localization performance, not just repair generation. This asymmetry is deliberate and "
                "documented, not an oversight -- see the plan's Phase 4/testing_plan and this field. "
                "A further consequence: negation_polarity_flip corruptions are DELETIONS (the target-language "
                "marker is removed, corrupted_span=''), so the oracle span is zero-width and the severity-skip "
                "masker's __BLANK__ substitution has nothing to select -- B/D therefore no-op (never attempt a "
                "repair) on every negation_polarity_flip row in the injected-pool subset by construction, which "
                "is why their negation-category fix_rate is 0 and is NOT evidence B/D 'failed' to fix negation."
            ),
            "fix_rate_and_regression_definitions": (
                "fix_rate (per injected row) = 1 if the exact corrupted_span string is no longer present "
                "(substring search) in the repaired output, else 0. true_regression_rate = 1 if the number "
                "of gold-reference invariant spans (checker-detected on metadata_clean_target_text) missing "
                "from the repaired output's checker-detected invariant set EXCEEDS the number already missing "
                "in the pre-repair corrupted hypothesis (i.e. the repair step introduced NEW collateral loss "
                "of genuinely-correct invariants beyond what the injected corruption itself already removed)."
            ),
        },
        "datasets": [
            {"dataset": "natural_repair_B_D_C1", "examples": [natural_example(r) for r in natural_results]},
            {"dataset": "injected_pool_repair_B_D_C1", "examples": [injected_example(r) for r in injected_results]},
        ],
    }

    out_path = WORKDIR / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")

    (WORKDIR / "checker_validation.json").write_text(json.dumps(checker_validation_out, indent=2))
    logger.info("Wrote checker_validation.json")


if __name__ == "__main__":
    main()
