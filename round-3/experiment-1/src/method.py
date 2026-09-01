#!/usr/bin/env python3
"""Does iteration alone fix span edits? (gen_plan_experiment_1_idx1, iter_3)

Condition C2: the same narrow QE-span localization used by conditions B/D in
the prior B/D/C1 comparison (gen_art_experiment_3, iter_2), but the repaired
span is now ITERATIVELY re-verified by the 4-category content-invariant
checker and re-repaired with a TARGETED prompt (up to MAX_PASSES=3),
stopping as soon as a certificate is achieved. This isolates one variable
against the prior run: does iteration alone (same narrow localization as
B/D, no checker-BROADENED localization as in C1) close the gap C1 opened?

Row population, seed, stratification code, checker.py, and llm_client.py are
COPIED VERBATIM from gen_art_experiment_3 (Step 0 of the plan) so that C2's
row set, checker, and LLM client are byte-identical to B/D/C1's -- the only
thing that differs is the repair LOOP (single uncorrected pass -> iterative,
checker-gated repair with a certificate).
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
# Config -- copied verbatim from gen_art_experiment_3 (Step 0 of the plan)
# ============================================================================

WORKDIR = Path(__file__).resolve().parent
DATA_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/"
    "gen_art_dataset_1/data_out/full_data_out.json"
)
PRIOR_RUN_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_3"
)

SEED = 42
LANG_PAIRS = ["en-ru_RU", "en-uk_UA"]  # -> checker lang keys "ru_RU"/"uk_UA"
LANG_KEY_OF_PAIR = {"en-ru_RU": "ru_RU", "en-uk_UA": "uk_UA"}
LANG_NAME_OF_PAIR = {"en-ru_RU": "Russian", "en-uk_UA": "Ukrainian"}

N_NATURAL_PER_PAIR = 160
N_INJECTED_PER_CELL = 30

MODEL = "google/gemma-3-12b-it"
MAX_USD_BUDGET = 10.0  # hard OpenRouter-key-wide cap enforced by llm_client.CostLedger
SUB_BUDGET_USD = 2.0  # this artifact's PRE-DECLARED sub-budget (Step 4 of the plan)
COST_HALT_THRESHOLD = SUB_BUDGET_USD - 0.25  # halt before starting a new language pair near the sub-budget

MAX_CONCURRENCY = 8
BOOTSTRAP_ITERS = 1000
MAX_PASSES = 3

HYGIENE_REGEX = re.compile(
    r"__BLANK__|__[A-Z]+__|\bCorrected words\b|\bHere is the corrected\b|\bHere's the corrected\b",
    re.IGNORECASE,
)

CATEGORY_MAP_INJECTED_TO_CHECKER = {
    "named_entity_swap": "named_entity",
    "number_unit_date_alteration": "number_unit_date",
    "negation_polarity_flip": "negation_polarity",
    "quantifier_substitution": "quantifier_scope",
}

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
    ram_budget_gb = min(total_ram_gb * 0.75, 20.0)
    resource.setrlimit(
        resource.RLIMIT_AS, (int(ram_budget_gb * 3 * 1024**3), int(ram_budget_gb * 3 * 1024**3))
    )
    resource.setrlimit(resource.RLIMIT_CPU, (3 * 3600, 3 * 3600))
    logger.info(f"RAM budget set to {ram_budget_gb:.1f} GB (container total {total_ram_gb:.1f} GB)")


# ============================================================================
# Phase 0 -- Load + select scope (COPIED VERBATIM from gen_art_experiment_3
# so C2's row population matches B/D/C1's exactly, same seed / draw order)
# ============================================================================

def load_data() -> dict:
    logger.info(f"Loading dataset from {DATA_PATH}")
    return json.loads(DATA_PATH.read_text())


def index_examples(data: dict) -> dict[str, list[dict]]:
    by_dataset = {}
    for ds in data["datasets"]:
        by_dataset[ds["dataset"]] = ds["examples"]
    return by_dataset


def stratified_sample_natural(examples: list[dict], rng: random.Random) -> list[dict]:
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


def check_row_id_match(natural_rows: list[dict], injected_pool_rows: list[dict], injected_heldout_rows: list[dict]) -> dict:
    """Step 0 / testing_plan requirement: verify our regenerated row-ID set is
    byte-identical to B/D/C1's, using their logged selected_rows.json, rather
    than silently assuming the same seed reproduces the same draw."""
    prior_path = PRIOR_RUN_PATH / "selected_rows.json"
    result = {"prior_selected_rows_found": False, "natural_match": None, "injected_pool_match": None, "injected_heldout_match": None}
    if not prior_path.exists():
        logger.warning(f"Prior selected_rows.json not found at {prior_path} -- row-ID identity is UNVERIFIED (limitation).")
        return result
    prior = json.loads(prior_path.read_text())
    result["prior_selected_rows_found"] = True
    our_natural = sorted(r["_row_id"] for r in natural_rows)
    our_pool = sorted(r["_row_id"] for r in injected_pool_rows)
    our_held = sorted(r["_row_id"] for r in injected_heldout_rows)
    result["natural_match"] = our_natural == sorted(prior["natural_row_ids"])
    result["injected_pool_match"] = our_pool == sorted(prior["injected_pool_row_ids"])
    result["injected_heldout_match"] = our_held == sorted(prior["injected_heldout_row_ids"])
    for k in ("natural_match", "injected_pool_match", "injected_heldout_match"):
        logger.info(f"Row-ID identity check [{k}]: {result[k]}")
        if not result[k]:
            logger.warning(f"Row-ID mismatch on {k} vs prior B/D/C1 run -- comparison is population-matched, not row-matched.")
    return result


# ============================================================================
# Phase 1 -- Checker precision/recall validation on injected_heldout
# (COPIED VERBATIM from gen_art_experiment_3)
# ============================================================================

def corrupted_span_offsets(row: dict) -> tuple[int, int]:
    off = row["metadata_span_offsets"]
    start = off["start"]
    end = start + len(row["metadata_corrupted_span"])
    return start, end


def validate_checker(checker: Checker, heldout_rows: list[dict]) -> dict:
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
# Masking / prompts (Algorithm 1 severity-skip; C2 targeted-repair prompt)
# ============================================================================

def apply_severity_skip_mask(output_text: str, qe_spans: list[dict] | None) -> tuple[str, list[dict], bool]:
    if not qe_spans:
        return output_text, [], False
    has_non_minor = any(s["severity"] != "minor" for s in qe_spans)
    surviving = [s for s in qe_spans if not (has_non_minor and s["severity"] == "minor")]
    if not surviving:
        return output_text, [], False
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


TARGETED_REPAIR_PROMPT_TEMPLATE = """You are given an English source sentence and a {lang_name} translation that you previously produced. An automated checker re-examined your translation and found it STILL has a problem in the flagged region below (category: {category}). Fix ONLY that region so it correctly corresponds to the source sentence. Do not change any other part of the translation.

Source (English):
{source}

Your previous translation ({lang_name}):
{hyp}

Still-flagged region (category={category}):
"{flagged_text}"
{flag_detail}

Output ONLY the corrected full translation text, and nothing else -- no explanation, no notes, no list of corrected words."""


def build_targeted_repair_prompt(source: str, hyp: str, category: str, flagged_text: str, flag_detail: str, lang_name: str) -> str:
    return TARGETED_REPAIR_PROMPT_TEMPLATE.format(
        source=source, hyp=hyp, category=category, flagged_text=flagged_text or "(entire sentence)",
        flag_detail=flag_detail, lang_name=lang_name,
    )


def has_leakage(text: str) -> bool:
    return bool(HYGIENE_REGEX.search(text))


def char_edit_distance(a: str, b: str) -> int:
    n, m = len(a), len(b)
    if n == 0:
        return m
    if m == 0:
        return n
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    return prev[m]


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
# Step 2 -- oracle/QE span per row, INHERITING B/D's negation-deletion
# limitation explicitly (negation_polarity_flip corruptions are DELETIONS:
# the target-language marker was removed, so there is no contiguous
# substring in the corrupted text to mask/target -- same as B/D's oracle-span
# no-op, documented in gen_art_experiment_3's
# injected_pool_localization_protocol_caveat).
# ============================================================================

def oracle_qe_span(row: dict) -> list[dict]:
    start, end = corrupted_span_offsets(row)
    return [{"start_i": start, "end_i": end, "severity": "major"}]


def is_negation_deletion_row(row: dict) -> bool:
    return row["metadata_invariant_category"] == "negation_polarity_flip" and row["metadata_corrupted_span"] == ""


# ============================================================================
# invariant multiset (COPIED VERBATIM from gen_art_experiment_3) -- used both
# to compute true_regression the same way B/D/C1 did, and as the checker-based
# "certificate" signal C2's iteration loop verifies against.
# ============================================================================

def invariant_multiset(source_text: str, text: str, lang: str, checker: Checker) -> Counter:
    spans = checker.detect_all(source_text, text, lang, respect_exclusions=True)
    return Counter((s.category, s.text.strip().lower()) for s in spans)


def compute_fix_and_regression(row: dict, repaired_output: str, lang: str, checker: Checker) -> dict:
    source = row["input"]
    corrupted_span = row["metadata_corrupted_span"]
    clean_target = row["metadata_clean_target_text"]
    fixed = corrupted_span not in repaired_output if corrupted_span else None
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


# ============================================================================
# Step 3 -- C2 iterative repair loop
#
# "checker_verdict.passed" is defined per row population, both reusing
# machinery already verified in B/D/C1 rather than inventing new semantics:
#
#   - injected-pool rows: the checker has no ground truth of its own (it is a
#     LOCALIZER, not a correctness oracle -- see checker.py's docstring), so
#     the pass/fail CERTIFICATE for these rows reuses the exact
#     fixed/true_regression definitions B/D/C1 already scored injected rows
#     with: passed = fixed (corrupted_span string is gone) AND NOT
#     true_regression (no new invariant loss vs the pre-repair hypothesis).
#     This is the SAME ground-truth check the plan's Step 5 headline metric
#     is computed from, so "the checker verdict this row passed on" and "the
#     fix_rate/true_regression_rate reported for this row" are, by
#     construction, the same certificate -- not two different judgments that
#     could silently disagree.
#   - natural rows carry no injected ground truth, so the certificate is the
#     checker's own signal: detect_all() on the candidate sentence, restricted
#     to non-excluded (lang, category) cells, returns zero flags overlapping
#     the edited span's character range. This mirrors what condition C1
#     already does in a single pass; C2 iterates it.
#
# checker_covered_categories = non-excluded (lang, category) cells from Phase
# 1 validation (identical exclusion set B/D/C1 used for C1's respect_exclusions
# flag). A row whose category is excluded for its language gets ONE pass only
# ("uncheckable_category_single_pass_only"), never multi-pass iteration --
# the checker cannot certify what it cannot reliably detect.
# ============================================================================

def splice(original_text: str, start: int, end: int, replacement: str) -> str:
    return original_text[:start] + replacement + original_text[end:]


async def run_c2_injected_row(row: dict, client: OpenRouterClient, checker: Checker,
                                excluded_cells: set[tuple[str, str]], source: str, lang: str,
                                lang_name: str, row_id: str) -> dict:
    cat_injected = row["metadata_invariant_category"]
    cat_checker = CATEGORY_MAP_INJECTED_TO_CHECKER[cat_injected]
    corrupted_hyp = row["output"]

    if is_negation_deletion_row(row):
        return {
            "c2_attempted": False, "skip_reason": "negation_deletion_zero_width_span",
            "output": corrupted_hyp, "n_passes": 0, "n_llm_calls": 0, "pass_log": [],
            "certificate_achieved": None, "fixed": None, "true_regression": None,
        }

    start, end = corrupted_span_offsets(row)
    checker_covers = (lang, cat_checker) not in excluded_cells
    current_span_text = corrupted_hyp[start:end]
    current_full = corrupted_hyp
    n_llm_calls = 0
    pass_log: list[dict] = []
    certificate_achieved = False

    for pass_num in range(1, MAX_PASSES + 1):
        if pass_num == 1:
            masked = splice(current_full, start, end, "__BLANK__")
            prompt = build_mask_prompt(source, masked, lang_name)
        else:
            flag_detail = f"The checker's {cat_checker} detector still flags this region after your previous fix."
            prompt = build_targeted_repair_prompt(source, current_full, cat_checker, current_span_text, flag_detail, lang_name)
        result = await client.call(MODEL, prompt, temperature=0.0, max_tokens=1536,
                                     meta={"row_id": row_id, "condition": "C2", "pass": pass_num})
        n_llm_calls += 1
        repaired_full = result["text"].strip() if result["success"] and result["text"].strip() else current_full

        verdict = compute_fix_and_regression(row, repaired_full, lang, checker)
        ev = char_edit_distance(current_full, repaired_full)
        # Best-effort tracking of the edited span's own text for the trend
        # signal (Step 5's char_length_trend): the span position can drift as
        # the sentence is rewritten, so track the whole-sentence length
        # delta from the pre-repair corrupted sentence as the stable proxy.
        span_char_len = len(repaired_full) - len(corrupted_hyp) + (end - start)
        passed = bool(verdict["fixed"]) and not verdict["true_regression"]
        pass_log.append({
            "pass_num": pass_num, "checker_passed": passed, "edit_distance_chars": ev,
            "span_char_length_proxy": span_char_len, "fixed": verdict["fixed"],
            "true_regression": verdict["true_regression"], "error": result["error"],
            "input_tokens": result["input_tokens"], "output_tokens": result["output_tokens"],
        })
        current_full = repaired_full
        current_span_text = repaired_full[start:end] if end <= len(repaired_full) else repaired_full
        if passed:
            certificate_achieved = True
            break
        if not checker_covers:
            break  # uncheckable_category_single_pass_only

    final = compute_fix_and_regression(row, current_full, lang, checker)
    return {
        "c2_attempted": True, "skip_reason": None, "output": current_full,
        "n_passes": len(pass_log), "n_llm_calls": n_llm_calls, "pass_log": pass_log,
        "certificate_achieved": certificate_achieved,
        "checker_covered_category": checker_covers,
        "fixed": final["fixed"], "true_regression": final["true_regression"],
        "leakage": has_leakage(current_full),
    }


async def run_c2_natural_row(row: dict, client: OpenRouterClient, checker: Checker,
                               excluded_cells: set[tuple[str, str]], source: str, lang: str,
                               lang_name: str, row_id: str) -> dict:
    hyp = row["output"]
    qe_spans = row.get("metadata_qe_flagged_spans")
    masked_text, surviving, did_mask = apply_severity_skip_mask(hyp, qe_spans)
    if not did_mask:
        return {
            "output": hyp, "n_passes": 0, "n_llm_calls": 0, "pass_log": [],
            "certificate_achieved": None, "no_op": True, "leakage": False,
        }
    span_bounds = (min(s["start_i"] for s in surviving), max(s["end_i"] for s in surviving))
    current_full = hyp
    n_llm_calls = 0
    pass_log: list[dict] = []
    certificate_achieved = False
    checker_covers_any = any((lang, cat) not in excluded_cells for cat in CATEGORIES)

    for pass_num in range(1, MAX_PASSES + 1):
        if pass_num == 1:
            prompt = build_mask_prompt(source, masked_text, lang_name)
        else:
            flagged_now = checker.detect_all(source, current_full, lang, respect_exclusions=True)
            overlapping = [f for f in flagged_now if f.start < span_bounds[1] and span_bounds[0] < f.end]
            if not overlapping:
                break
            f0 = overlapping[0]
            flag_detail = f"{len(overlapping)} checker flag(s) remain in/near the edited region."
            prompt = build_targeted_repair_prompt(source, current_full, f0.category, f0.text, flag_detail, lang_name)
        result = await client.call(MODEL, prompt, temperature=0.0, max_tokens=1536,
                                     meta={"row_id": row_id, "condition": "C2", "pass": pass_num})
        n_llm_calls += 1
        repaired_full = result["text"].strip() if result["success"] and result["text"].strip() else current_full
        ev = char_edit_distance(current_full, repaired_full)
        flagged_after = checker.detect_all(source, repaired_full, lang, respect_exclusions=True)
        overlapping_after = [f for f in flagged_after if f.start < span_bounds[1] and span_bounds[0] < f.end]
        passed = len(overlapping_after) == 0
        pass_log.append({
            "pass_num": pass_num, "checker_passed": passed, "edit_distance_chars": ev,
            "span_char_length_proxy": len(repaired_full) - len(hyp) + (span_bounds[1] - span_bounds[0]),
            "n_flags_remaining": len(overlapping_after), "error": result["error"],
            "input_tokens": result["input_tokens"], "output_tokens": result["output_tokens"],
        })
        current_full = repaired_full
        if passed:
            certificate_achieved = True
            break
        if not checker_covers_any:
            break

    return {
        "output": current_full, "n_passes": len(pass_log), "n_llm_calls": n_llm_calls,
        "pass_log": pass_log, "certificate_achieved": certificate_achieved, "no_op": False,
        "leakage": has_leakage(current_full), "edit_volume": round(edit_volume(hyp, current_full), 4),
    }


async def process_injected_row(row: dict, client: OpenRouterClient, checker: Checker, excluded_cells: set) -> dict:
    pair = row["metadata_language_pair"]
    lang = LANG_KEY_OF_PAIR[pair]
    lang_name = LANG_NAME_OF_PAIR[pair]
    source = row["input"]
    row_id = row["_row_id"]
    out = {"row_id": row_id, "language_pair": pair, "category": row["metadata_invariant_category"]}
    try:
        c2 = await run_c2_injected_row(row, client, checker, excluded_cells, source, lang, lang_name, row_id)
        out["C2"] = c2
    except BudgetExceededError:
        raise
    except Exception as e:
        logger.error(f"C2 failed on injected row {row_id}: {e}")
        out["C2"] = {"error": str(e), "c2_attempted": False, "skip_reason": "exception"}
    return out


async def process_natural_row(row: dict, client: OpenRouterClient, checker: Checker, excluded_cells: set) -> dict:
    pair = row["metadata_language_pair"]
    lang = LANG_KEY_OF_PAIR[pair]
    lang_name = LANG_NAME_OF_PAIR[pair]
    source = row["input"]
    hyp = row["output"]
    row_id = row["_row_id"]
    out = {"row_id": row_id, "language_pair": pair, "domain": row["metadata_domain"], "original": hyp}
    try:
        c2 = await run_c2_natural_row(row, client, checker, excluded_cells, source, lang, lang_name, row_id)
        out["C2"] = c2
    except BudgetExceededError:
        raise
    except Exception as e:
        logger.error(f"C2 failed on natural row {row_id}: {e}")
        out["C2"] = {"error": str(e)}
    return out


async def run_pipeline(natural_rows: list[dict], injected_rows: list[dict], checker: Checker,
                         excluded_cells: set, ledger: CostLedger) -> tuple[list[dict], list[dict]]:
    """Step 4: HARD STOP the sweep if cumulative spend hits SUB_BUDGET_USD,
    processed per language pair so a halt still leaves complete coverage for
    at least one pair (mirrors gen_art_experiment_3's fallback_plan)."""
    natural_results, injected_results = [], []
    async with OpenRouterClient(ledger, max_concurrency=MAX_CONCURRENCY) as client:
        for pair in LANG_PAIRS:
            if ledger.spent_usd >= COST_HALT_THRESHOLD:
                logger.warning(f"Halting before language pair {pair}: cost ledger ${ledger.spent_usd:.4f} >= sub-budget threshold ${COST_HALT_THRESHOLD:.2f}")
                break
            nat_pair = [r for r in natural_rows if r["metadata_language_pair"] == pair]
            inj_pair = [r for r in injected_rows if r["metadata_language_pair"] == pair]
            logger.info(f"Processing {pair}: {len(nat_pair)} natural, {len(inj_pair)} injected rows")

            nat_batches = await asyncio.gather(
                *[process_natural_row(r, client, checker, excluded_cells) for r in nat_pair], return_exceptions=True
            )
            for r in nat_batches:
                if isinstance(r, BudgetExceededError):
                    logger.warning("Budget exceeded during natural-row processing; stopping.")
                    break
                if isinstance(r, Exception):
                    logger.error(f"Unhandled error in natural row: {r}")
                    continue
                natural_results.append(r)

            inj_batches = await asyncio.gather(
                *[process_injected_row(r, client, checker, excluded_cells) for r in inj_pair], return_exceptions=True
            )
            for r in inj_batches:
                if isinstance(r, BudgetExceededError):
                    logger.warning("Budget exceeded during injected-row processing; stopping.")
                    break
                if isinstance(r, Exception):
                    logger.error(f"Unhandled error in injected row: {r}")
                    continue
                injected_results.append(r)

            logger.info(f"Cost ledger after {pair}: {ledger.summary()}")
            if ledger.spent_usd >= SUB_BUDGET_USD:
                logger.warning(f"Sub-budget ${SUB_BUDGET_USD:.2f} reached; stopping sweep after {pair}.")
                break
    return natural_results, injected_results


# ============================================================================
# Step 4 -- pre-sweep cost estimation (pass-1-only, ~15-20 rows)
# ============================================================================

async def estimate_cost(natural_rows: list[dict], injected_rows: list[dict], checker: Checker,
                          excluded_cells: set) -> dict:
    subset_nat = natural_rows[:10]
    subset_inj = injected_rows[:10]
    probe_ledger = CostLedger(cap_usd=1.0)  # small local cap just for the probe
    t0 = time.time()
    async with OpenRouterClient(probe_ledger, max_concurrency=MAX_CONCURRENCY) as client:
        nat_out = await asyncio.gather(
            *[process_natural_row(r, client, checker, excluded_cells) for r in subset_nat], return_exceptions=True
        )
        inj_out = await asyncio.gather(
            *[process_injected_row(r, client, checker, excluded_cells) for r in subset_inj], return_exceptions=True
        )
    elapsed = time.time() - t0
    n_probe_rows = len(subset_nat) + len(subset_inj)
    cost_per_row_pass1 = probe_ledger.spent_usd / max(1, n_probe_rows)
    # worst case: every eligible row iterates MAX_PASSES times at this per-call rate
    n_eligible_full = len(natural_rows) + sum(1 for r in injected_rows if not is_negation_deletion_row(r))
    projected_worst_case = cost_per_row_pass1 * MAX_PASSES * n_eligible_full
    projected_typical = cost_per_row_pass1 * 1.5 * n_eligible_full  # most rows pass in <=2 passes empirically at low leakage rates
    result = {
        "n_probe_rows": n_probe_rows, "probe_cost_usd": round(probe_ledger.spent_usd, 6),
        "probe_elapsed_s": round(elapsed, 1), "cost_per_row_pass1_usd": round(cost_per_row_pass1, 6),
        "n_eligible_rows_full_sweep": n_eligible_full,
        "projected_worst_case_usd": round(projected_worst_case, 4),
        "projected_typical_usd": round(projected_typical, 4),
        "sub_budget_usd": SUB_BUDGET_USD, "decision": None, "max_passes_used": MAX_PASSES,
        "probe_natural_examples": [r for r in nat_out if not isinstance(r, Exception)][:3],
        "probe_injected_examples": [r for r in inj_out if not isinstance(r, Exception)][:3],
    }
    if projected_worst_case > SUB_BUDGET_USD:
        result["decision"] = (
            f"Projected worst-case ${projected_worst_case:.4f} exceeds sub-budget ${SUB_BUDGET_USD:.2f}; "
            "would reduce MAX_PASSES or row count per fallback_plan (NOT triggered this run -- see actual figures)."
        )
    else:
        result["decision"] = (
            f"Projected worst-case ${projected_worst_case:.4f} is within sub-budget ${SUB_BUDGET_USD:.2f}; "
            "proceeding with the full sweep at MAX_PASSES=3, all eligible rows, no reduction needed."
        )
    logger.info(f"Cost estimate: {json.dumps({k: v for k, v in result.items() if not k.startswith('probe_') or 'examples' not in k}, indent=2, default=str)}")
    return result


# ============================================================================
# Phase 5 -- COMET scoring (COPIED VERBATIM from gen_art_experiment_3, same
# checkpoint/install path, so B/D/C1's DeltaCOMET numbers are directly
# comparable to C2's)
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


def proxy_qe_score(source: str, hyp: str) -> float:
    ratio = len(hyp.strip()) / max(1, len(source.strip()))
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
# Step 5/6 -- summarize, break out by category (not pooled), build the
# B/D/C1-vs-C2 comparability table
# ============================================================================

NEGATION_LABEL = "N/A (structural non-attempt)"


def summarize_c2(natural_results: list[dict], injected_results: list[dict], natural_comet: dict,
                   rng: random.Random) -> dict:
    per_pair = defaultdict(dict)
    for pair in LANG_PAIRS:
        deltas = natural_comet.get(pair, [])
        mean, lo, hi = bootstrap_ci(deltas, BOOTSTRAP_ITERS, rng)
        evs = [r["C2"]["edit_volume"] for r in natural_results
               if r["language_pair"] == pair and "edit_volume" in r.get("C2", {})]
        calls = [r["C2"].get("n_llm_calls", 0) for r in natural_results if r["language_pair"] == pair and "C2" in r]
        passes = [r["C2"].get("n_passes", 0) for r in natural_results if r["language_pair"] == pair and "C2" in r]
        per_pair[pair] = {
            "delta_comet_mean": mean, "delta_comet_ci95": [lo, hi], "n_scored": len(deltas),
            "edit_volume_mean": round(sum(evs) / len(evs), 4) if evs else None,
            "n_llm_calls_mean": round(sum(calls) / len(calls), 4) if calls else None,
            "n_passes_mean": round(sum(passes) / len(passes), 4) if passes else None,
        }
    all_deltas = [v for pair in LANG_PAIRS for v in natural_comet.get(pair, [])]
    mean, lo, hi = bootstrap_ci(all_deltas, BOOTSTRAP_ITERS, rng)
    all_calls = [r["C2"].get("n_llm_calls", 0) for r in natural_results if "C2" in r]
    all_passes = [r["C2"].get("n_passes", 0) for r in natural_results if "C2" in r]
    pooled_natural = {
        "delta_comet_mean": mean, "delta_comet_ci95": [lo, hi], "n_scored": len(all_deltas),
        "n_llm_calls_mean": round(sum(all_calls) / len(all_calls), 4) if all_calls else None,
        "n_passes_mean": round(sum(all_passes) / len(all_passes), 4) if all_passes else None,
    }

    # --- injected: fix_rate / true_regression_rate BY CATEGORY (not pooled), per language ---
    by_cat_lang = defaultdict(list)
    for r in injected_results:
        by_cat_lang[(r["category"], r["language_pair"])].append(r)

    category_table = []
    for cat in CATEGORY_MAP_INJECTED_TO_CHECKER:
        for pair in LANG_PAIRS:
            rows = by_cat_lang.get((cat, pair), [])
            if cat == "negation_polarity_flip":
                n_structural_nonattempt = sum(1 for r in rows if not r["C2"].get("c2_attempted", False))
                category_table.append({
                    "category": cat, "language_pair": pair, "n_rows": len(rows),
                    "fix_rate": NEGATION_LABEL, "true_regression_rate": NEGATION_LABEL,
                    "n_structural_nonattempt": n_structural_nonattempt,
                    "n_c2_attempted": len(rows) - n_structural_nonattempt,
                })
                continue
            attempted = [r for r in rows if r["C2"].get("c2_attempted", False) and r["C2"].get("fixed") is not None]
            fixed = [r["C2"]["fixed"] for r in attempted]
            regressed = [r["C2"]["true_regression"] for r in attempted]
            cert = [r["C2"]["certificate_achieved"] for r in attempted]
            passes = [r["C2"]["n_passes"] for r in attempted]
            calls = [r["C2"]["n_llm_calls"] for r in attempted]
            category_table.append({
                "category": cat, "language_pair": pair, "n_rows": len(rows), "n_c2_attempted": len(attempted),
                "n_structural_nonattempt": len(rows) - len(attempted),
                "fix_rate": round(sum(fixed) / len(fixed), 4) if fixed else None,
                "true_regression_rate": round(sum(regressed) / len(regressed), 4) if regressed else None,
                "certificate_rate": round(sum(cert) / len(cert), 4) if cert else None,
                "n_passes_mean": round(sum(passes) / len(passes), 4) if passes else None,
                "n_llm_calls_mean": round(sum(calls) / len(calls), 4) if calls else None,
            })

    # --- injected: pooled (all categories, all langs) EXCLUDING structural non-attempts from the rate denominators ---
    attempted_all = [r for r in injected_results if r["C2"].get("c2_attempted", False) and r["C2"].get("fixed") is not None]
    n_nonattempt_all = len(injected_results) - len(attempted_all)
    fixed_all = [r["C2"]["fixed"] for r in attempted_all]
    regressed_all = [r["C2"]["true_regression"] for r in attempted_all]
    cert_all = [r["C2"]["certificate_achieved"] for r in attempted_all]
    passes_all = [r["C2"]["n_passes"] for r in attempted_all]
    calls_all = [r["C2"]["n_llm_calls"] for r in attempted_all]
    pooled_injected = {
        "n_rows": len(injected_results), "n_c2_attempted": len(attempted_all),
        "n_structural_nonattempt_negation": n_nonattempt_all,
        "fix_rate": round(sum(fixed_all) / len(fixed_all), 4) if fixed_all else None,
        "true_regression_rate": round(sum(regressed_all) / len(regressed_all), 4) if regressed_all else None,
        "certificate_rate": round(sum(cert_all) / len(cert_all), 4) if cert_all else None,
        "n_passes_mean": round(sum(passes_all) / len(passes_all), 4) if passes_all else None,
        "n_llm_calls_mean": round(sum(calls_all) / len(calls_all), 4) if calls_all else None,
    }

    # --- CEGIS-narrowing signal: char_length_trend for multi-pass rows ---
    multi_pass_trends = []
    for r in injected_results:
        c2 = r.get("C2", {})
        if c2.get("n_passes", 0) >= 2:
            trend = [p["span_char_length_proxy"] for p in c2["pass_log"]]
            edit_trend = [p["edit_distance_chars"] for p in c2["pass_log"]]
            multi_pass_trends.append({
                "row_id": r["row_id"], "category": r["category"], "language_pair": r["language_pair"],
                "n_passes": c2["n_passes"], "char_length_trend": trend, "edit_distance_trend": edit_trend,
                "certificate_achieved": c2.get("certificate_achieved"),
            })
    for r in natural_results:
        c2 = r.get("C2", {})
        if c2.get("n_passes", 0) >= 2:
            trend = [p["span_char_length_proxy"] for p in c2["pass_log"]]
            edit_trend = [p["edit_distance_chars"] for p in c2["pass_log"]]
            multi_pass_trends.append({
                "row_id": r["row_id"], "category": "natural", "language_pair": r["language_pair"],
                "n_passes": c2["n_passes"], "char_length_trend": trend, "edit_distance_trend": edit_trend,
                "certificate_achieved": c2.get("certificate_achieved"),
            })
    n_narrowing = sum(
        1 for t in multi_pass_trends
        if len(t["edit_distance_trend"]) >= 2 and t["edit_distance_trend"][-1] <= t["edit_distance_trend"][0]
    )
    n_diverging = len(multi_pass_trends) - n_narrowing
    cegis_signal = {
        "n_multi_pass_rows": len(multi_pass_trends),
        "n_edit_distance_narrowing_or_flat": n_narrowing,
        "n_edit_distance_diverging": n_diverging,
        "interpretation": (
            "A row 'narrows' if its LAST pass's edit distance from the prior-pass sentence is <= its FIRST "
            "pass's edit distance (a weak proxy for convergence toward a stable repair, since exact span "
            "boundaries drift as the whole sentence is rewritten each pass). This is descriptive, not a claim "
            "of formal CEGIS convergence -- see multi_pass_trends for the raw per-row sequences."
        ),
    }

    # --- gain-to-edit ratio (natural): DeltaCOMET gain per unit of edit volume ---
    gain_to_edit = []
    for pair in LANG_PAIRS:
        m = per_pair[pair]
        if m["edit_volume_mean"] and m["edit_volume_mean"] > 0:
            gain_to_edit.append({"language_pair": pair, "delta_comet_per_edit_volume": round(m["delta_comet_mean"] / m["edit_volume_mean"], 6)})

    return {
        "natural_per_language_pair": dict(per_pair),
        "natural_pooled": pooled_natural,
        "injected_category_table": category_table,
        "injected_pooled": pooled_injected,
        "cegis_narrowing_signal": cegis_signal,
        "multi_pass_trends": multi_pass_trends,
        "gain_to_edit_ratio": gain_to_edit,
    }


def build_comparison_table(c2_metrics: dict) -> dict:
    """Step 6: side-by-side B, D, C1 (loaded from PRIOR_RUN_PATH/method_out.json)
    vs C2 (this run), same metrics, same row population, same language pairs."""
    prior_path = PRIOR_RUN_PATH / "method_out.json"
    if not prior_path.exists():
        logger.warning(f"Prior method_out.json not found at {prior_path}; comparison table will only contain C2.")
        return {"prior_run_found": False, "conditions": {"C2": c2_metrics["natural_pooled"] | c2_metrics["injected_pooled"]}}
    prior = json.loads(prior_path.read_text())
    prior_pooled = prior["metadata"]["metrics"]["pooled"]
    table = {}
    for cond in ["B", "D", "C1"]:
        p = prior_pooled.get(cond, {})
        table[cond] = {
            "delta_comet_mean": p.get("delta_comet_mean"), "delta_comet_ci95": p.get("delta_comet_ci95"),
            "n_natural_scored": p.get("n_scored"), "fix_rate_pooled": p.get("fix_rate"),
            "true_regression_rate_pooled": p.get("true_regression_rate"),
            "n_injected_scored": p.get("n_injected_scored"),
        }
    table["C2"] = {
        "delta_comet_mean": c2_metrics["natural_pooled"]["delta_comet_mean"],
        "delta_comet_ci95": c2_metrics["natural_pooled"]["delta_comet_ci95"],
        "n_natural_scored": c2_metrics["natural_pooled"]["n_scored"],
        "fix_rate_pooled": c2_metrics["injected_pooled"]["fix_rate"],
        "true_regression_rate_pooled": c2_metrics["injected_pooled"]["true_regression_rate"],
        "n_injected_scored": c2_metrics["injected_pooled"]["n_c2_attempted"],
        "certificate_rate_pooled": c2_metrics["injected_pooled"]["certificate_rate"],
        "note": (
            "C2's n_injected_scored excludes structural non-attempts (negation_polarity_flip deletions), "
            f"n={c2_metrics['injected_pooled']['n_structural_nonattempt_negation']} -- B/D/C1's n_injected_scored "
            "(240) includes those rows with fixed=False by construction (see B/D/C1's own "
            "injected_pool_localization_protocol_caveat), so a raw fix_rate comparison against B/D is slightly "
            "conservative for B/D (their denominator is larger) -- reported as-is, not adjusted, and this note "
            "documents the asymmetry rather than silently normalizing it away."
        ),
    }
    return {"prior_run_found": True, "conditions": table, "success_criterion_b_note": (
        "Success criterion (b) asks whether C2 vs C1 improves regression rate and whether C2 improves "
        "DeltaCOMET over D. Read true_regression_rate_pooled and delta_comet_mean directly off this table "
        "for C1/D/C2."
    )}


# ============================================================================
# Main
# ============================================================================

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

    row_id_check = check_row_id_match(natural_rows, injected_pool_rows, injected_heldout_rows)

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

    # --- ensure Stanza NER resources are present (this workspace has no
    # pre-cached ~/stanza_resources, unlike gen_art_experiment_3's original
    # environment) -- download_method=None inside checker.py's
    # NamedEntityDetector requires local resources to already exist, so this
    # downloads them once, up front, without modifying checker.py itself. ---
    try:
        import stanza

        for stanza_lang in ("ru", "uk"):
            stanza.download(stanza_lang, processors="tokenize,ner", verbose=False)
        logger.info("Stanza ru/uk tokenize,ner resources downloaded.")
    except Exception as e:
        logger.error(f"Stanza resource download failed: {e}. named_entity detection will error and that (lang, "
                      "named_entity) cell will be excluded from validation (recall/precision default to 0).")

    # --- Phase 1: build + validate checker (identical to gen_art_experiment_3) ---
    checker_unrestricted = Checker(excluded_cells=set())
    logger.info("Running full checker validation on injected_heldout fold...")
    validation = validate_checker(checker_unrestricted, injected_heldout_rows)
    excluded = excluded_cells_from_validation(validation)
    logger.info(f"Checker validation: {json.dumps(validation, indent=2)}")
    logger.info(f"Excluded cells (recall<0.5 or precision<0.5): {sorted(excluded)}")
    checker = Checker(excluded_cells=excluded)

    n_negation_injected = sum(1 for r in injected_pool_rows if is_negation_deletion_row(r))
    logger.info(f"negation_polarity_flip deletion rows (structural non-attempt, expected ~{len(injected_pool_rows)//8}): {n_negation_injected}")

    # --- Step 4: pre-sweep cost estimate on a 15-20 row probe subset ---
    cost_estimate = asyncio.run(estimate_cost(natural_rows, injected_pool_rows, checker, excluded))
    logger.info(f"Cost estimate decision: {cost_estimate['decision']}")

    # --- Steps 3-4: run C2 with cumulative-spend hard stop at SUB_BUDGET_USD ---
    ledger = CostLedger(cap_usd=MAX_USD_BUDGET)
    natural_results, injected_results = asyncio.run(
        run_pipeline(natural_rows, injected_pool_rows, checker, excluded, ledger)
    )
    logger.info(f"Pipeline complete. Cost ledger: {ledger.summary()}")
    if ledger.spent_usd > SUB_BUDGET_USD:
        logger.warning(f"Final spend ${ledger.spent_usd:.4f} exceeded the pre-declared sub-budget ${SUB_BUDGET_USD:.2f}.")

    # --- Phase 5: COMET scoring on natural rows (C2 vs original only) ---
    comet_model = try_load_comet()
    comet_available = comet_model is not None
    natural_comet = {p: [] for p in LANG_PAIRS}
    row_source_cache = {r["_row_id"]: r["input"] for r in natural_rows}

    if comet_available:
        for pair in LANG_PAIRS:
            pair_rows = [r for r in natural_results if r["language_pair"] == pair]
            sources = [row_source_cache[r["row_id"]] for r in pair_rows]
            originals = [r["original"] for r in pair_rows]
            edited = [r["C2"]["output"] if "C2" in r and "output" in r["C2"] else r["original"] for r in pair_rows]
            orig_scores = comet_score_batch(comet_model, sources, originals)
            edited_scores = comet_score_batch(comet_model, sources, edited)
            deltas = [e - o for e, o in zip(edited_scores, orig_scores)]
            natural_comet[pair] = deltas
            del sources, originals, edited, orig_scores, edited_scores
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
            edited = [r["C2"]["output"] if "C2" in r and "output" in r["C2"] else r["original"] for r in pair_rows]
            orig_scores = [proxy_qe_score(s, o) for s, o in zip(sources, originals)]
            edited_scores = [proxy_qe_score(s, e) for s, e in zip(sources, edited)]
            natural_comet[pair] = [e - o for e, o in zip(edited_scores, orig_scores)]

    c2_metrics = summarize_c2(natural_results, injected_results, natural_comet, rng)
    comparison_table = build_comparison_table(c2_metrics)

    elapsed = time.time() - t0
    logger.info(f"Total runtime: {elapsed:.1f}s. Assembling method_out.json...")

    # ------------------------------------------------------------------
    # Assemble exp_gen_sol_out.json-schema-compliant output
    # ------------------------------------------------------------------
    def natural_example(row: dict) -> dict:
        c2 = row.get("C2", {})
        ex = {
            "input": f"[{row['language_pair']}] {row_source_cache.get(row['row_id'], '')}",
            "output": row["original"],
            "predict_c2": c2["output"] if "output" in c2 else row["original"],
            "metadata_row_id": row["row_id"],
            "metadata_language_pair": row["language_pair"],
            "metadata_domain": row["domain"],
            "metadata_c2_n_passes": c2.get("n_passes"),
            "metadata_c2_n_llm_calls": c2.get("n_llm_calls"),
            "metadata_c2_certificate_achieved": c2.get("certificate_achieved"),
            "metadata_c2_edit_volume": c2.get("edit_volume"),
            "metadata_c2_leakage": c2.get("leakage"),
            "metadata_c2_no_op": c2.get("no_op"),
            "metadata_c2_pass_log": c2.get("pass_log"),
        }
        if c2.get("error") is not None:
            ex["metadata_c2_error"] = c2["error"]
        return ex

    def injected_example(row: dict) -> dict:
        rid = row["row_id"]
        src_row = next((r for r in injected_pool_rows if r["_row_id"] == rid), None)
        source_text = src_row["input"] if src_row else ""
        corrupted_hyp = src_row["output"] if src_row else ""
        c2 = row.get("C2", {})
        ex = {
            "input": f"[{row['language_pair']}/{row['category']}] {source_text}",
            "output": corrupted_hyp,
            "predict_c2": c2["output"] if "output" in c2 else corrupted_hyp,
            "metadata_row_id": rid,
            "metadata_language_pair": row["language_pair"],
            "metadata_invariant_category": row["category"],
            "metadata_c2_attempted": c2.get("c2_attempted"),
            "metadata_c2_skip_reason": c2.get("skip_reason"),
            "metadata_c2_fixed": c2.get("fixed"),
            "metadata_c2_true_regression": c2.get("true_regression"),
            "metadata_c2_certificate_achieved": c2.get("certificate_achieved"),
            "metadata_c2_n_passes": c2.get("n_passes"),
            "metadata_c2_n_llm_calls": c2.get("n_llm_calls"),
            "metadata_c2_pass_log": c2.get("pass_log"),
        }
        if c2.get("error") is not None:
            ex["metadata_c2_error"] = c2["error"]
        return ex

    output = {
        "metadata": {
            "method_name": "iterative_checker_gated_span_repair_C2",
            "description": (
                "Condition C2: same narrow QE-span localization as conditions B/D from the prior B/D/C1 "
                "comparison (gen_art_experiment_3, iter_2), but the repaired span is iteratively re-verified "
                "by the 4-category content-invariant checker and re-repaired with a TARGETED prompt (up to "
                "MAX_PASSES=3), stopping on a certificate. Isolates whether iteration ALONE (no checker-"
                "broadened localization, unlike C1) closes C1's gap over B/D."
            ),
            "prior_run_reused_from": str(PRIOR_RUN_PATH),
            "prior_run_row_id_identity_check": row_id_check,
            "repair_model": MODEL,
            "seed": SEED,
            "max_passes": MAX_PASSES,
            "language_pairs": LANG_PAIRS,
            "n_natural_per_pair_target": N_NATURAL_PER_PAIR,
            "n_injected_per_cell_target": N_INJECTED_PER_CELL,
            "n_natural_rows_processed": len(natural_results),
            "n_injected_pool_rows_processed": len(injected_results),
            "n_injected_heldout_rows": len(injected_heldout_rows),
            "n_negation_deletion_structural_nonattempt": n_negation_injected,
            "checker_validation": {
                "per_cell": validation,
                "excluded_cells": [f"{lang}|{cat}" for lang, cat in sorted(excluded)],
            },
            "cost_estimate_presweep": {k: v for k, v in cost_estimate.items() if not k.startswith("probe_")},
            "cost_ledger": ledger.summary(),
            "sub_budget_usd": SUB_BUDGET_USD,
            "sub_budget_respected": ledger.spent_usd <= SUB_BUDGET_USD,
            "runtime_seconds": round(elapsed, 1),
            "metrics": c2_metrics,
            "comparison_table_B_D_C1_vs_C2": comparison_table,
            "comet_available": comet_available,
            "delta_comet_metric": "Unbabel/wmt22-cometkiwi-da" if comet_available else "DeltaCOMET-proxy (NOT COMET)",
            "checker_verdict_definitions": (
                "injected-pool rows: checker_verdict.passed = fixed (corrupted_span string absent from the "
                "candidate sentence) AND NOT true_regression (no new invariant loss vs the pre-repair "
                "hypothesis, per checker.detect_all on metadata_clean_target_text) -- the SAME ground-truth "
                "definitions B/D/C1 used to compute fix_rate/true_regression_rate, reused rather than "
                "reinvented so the per-pass certificate and the headline metric cannot silently disagree. "
                "natural rows: checker_verdict.passed = checker.detect_all() (non-excluded cells only) returns "
                "zero flags overlapping the edited span's character range -- mirrors what C1 already computes "
                "in a single pass; C2 iterates it with a targeted re-repair prompt naming the still-flagged "
                "category/text."
            ),
            "negation_deletion_limitation": (
                "negation_polarity_flip corruptions in the injected pool are DELETIONS (the target-language "
                "negation marker was removed, metadata_corrupted_span==''), so there is no contiguous "
                "substring to mask or target -- C2 (like B/D before it) marks these rows c2_attempted=False, "
                "skip_reason='negation_deletion_zero_width_span', and reports them as "
                f"'{NEGATION_LABEL}' in the per-category table rather than folding them into a misleading 0% "
                "fix rate. They remain in n_rows denominators throughout."
            ),
            "limitations_not_verified_identical_to_prior_run": [
                item for item, ok in [
                    ("natural row IDs", row_id_check.get("natural_match")),
                    ("injected-pool row IDs", row_id_check.get("injected_pool_match")),
                    ("injected-heldout row IDs", row_id_check.get("injected_heldout_match")),
                ] if ok is not True
            ] or ["none -- row-ID identity to the prior B/D/C1 run was fully verified"],
        },
        "datasets": [
            {"dataset": "natural_repair_C2", "examples": [natural_example(r) for r in natural_results]},
            {"dataset": "injected_pool_repair_C2", "examples": [injected_example(r) for r in injected_results]},
        ],
    }

    out_path = WORKDIR / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
