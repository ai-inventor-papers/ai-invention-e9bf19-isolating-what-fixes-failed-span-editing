#!/usr/bin/env python3
"""Evaluation for 'Does Hygiene or Verification Fix Editing?'

Reads (never re-executes) whatever B/D/C1 span-editing results, checker-validation
results, and condition-B fidelity-gate results this iteration's sibling gen_art
experiments produced, and computes the paired-CI comparisons, regression/fix-rate
tables, edit-volume-to-gain ratios, a checker-precision-gated sensitivity re-analysis,
and a six-language-pair ΔCOMET reconciliation table against Padmanabhan (2025) /
WMT25 findings-paper Table 15. Every metric that has no real input degrades to an
explicit NOT_AVAILABLE rather than a fabricated number.
"""

from __future__ import annotations

import gc
import json
import math
import resource
import sys
from pathlib import Path
from typing import Any

import numpy as np
import psutil
from loguru import logger
from scipy import stats

WORKSPACE = Path(__file__).resolve().parent
DEP_DATA = WORKSPACE / "dep_data"
LOG_DIR = WORKSPACE / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOG_DIR / "run.log", rotation="30 MB", level="DEBUG")

RNG_SEED = 42
N_BOOT = 10_000
CI_ALPHA = 0.05
SENSITIVITY_THRESHOLD = 0.6
UNDERPOWERED_N = 20
FLAGGED_WEAK_CELLS = [("zh_CN", "named_entity"), ("ja_JP", "named_entity")]

# ---------------------------------------------------------------------------
# Verbatim quoted figures — WMT25 findings paper (aclanthology.org/2025.wmt-1.24),
# Table 15 "Task 3 - Performance of systems across languages with ∆COMET and
# Gain to Edit Ratio (GER) metrics", fetched and regex-extracted verbatim from the
# PDF at https://aclanthology.org/2025.wmt-1.24.pdf on 2026-09-01 (page containing
# "SURREYPAI-S2" / "BASELINE-S2"). Column order in the source is
# En-Cs, En-Is, En-Ja, En-Ru, En-Uk, En-Zh, Average, each as (∆COMET, GER).
# These are the paper's own numbers, quoted, not measurements made here.
# ---------------------------------------------------------------------------
PADMANABHAN_TABLE15_SOURCE = (
    "Findings of the WMT25 Shared Task on Automated Translation Evaluation "
    "Systems, Table 15 (https://aclanthology.org/2025.wmt-1.24.pdf, page ~60, "
    "'Task 3 - Performance of systems across languages'), verbatim OCR-extracted "
    "2026-09-01 via regex grep on the fetched PDF text."
)
PADMANABHAN_TABLE15 = {
    "SURREYPAI-S2": {
        "en-cs_CZ": {"delta_comet": -0.007, "ger": -0.005},
        "en-is_IS": {"delta_comet": -0.010, "ger": -0.006},
        "en-ja_JP": {"delta_comet": -0.013, "ger": -0.008},
        "en-ru_RU": {"delta_comet": -0.008, "ger": -0.005},
        "en-uk_UA": {"delta_comet": -0.014, "ger": -0.009},
        "en-zh_CN": {"delta_comet": -0.013, "ger": -0.010},
        "average": {"delta_comet": -0.011, "ger": -0.007},
    },
    "BASELINE-S2": {
        "en-cs_CZ": {"delta_comet": 0.000, "ger": 0.000},
        "en-is_IS": {"delta_comet": 0.007, "ger": 0.026},
        "en-ja_JP": {"delta_comet": -0.008, "ger": -0.036},
        "en-ru_RU": {"delta_comet": 0.002, "ger": 0.009},
        "en-uk_UA": {"delta_comet": 0.004, "ger": 0.017},
        "en-zh_CN": {"delta_comet": -0.005, "ger": -0.023},
        "average": {"delta_comet": 0.000, "ger": -0.001},
    },
}
# Padmanabhan (2025)'s own self-reported Table 3 average, quoted in the artifact
# plan and cross-checked (rounding-consistent) against Table 15 above by the
# iter_1 research dossier (research_out.json, gen_art_research_1).
PADMANABHAN_SELF_REPORTED_AVG_DELTA_COMET = -0.0108

INVARIANT_CATEGORIES = [
    "named_entity",
    "number_unit_date",
    "negation_polarity",
    "quantifier",
]


def set_resource_limits() -> None:
    """Cap RAM well under the 57GB cgroup limit; this job never needs more than
    a few hundred MB (a 29MB dataset file plus small JSON result files)."""
    # numpy/scipy's BLAS/LAPACK libraries reserve large virtual address ranges
    # at import time (arena/thread-pool mappings) far beyond actual RSS use, so
    # the budget must be generous even though real data here is ~30MB.
    budget_bytes = 16 * 1024**3  # 16GB — well under the 57GB cgroup limit
    avail = psutil.virtual_memory().available
    assert budget_bytes < avail, f"budget {budget_bytes} > available {avail}"
    resource.setrlimit(resource.RLIMIT_AS, (budget_bytes, budget_bytes))
    resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))
    logger.info(f"RAM budget set to {budget_bytes / 1e9:.1f}GB, CPU budget 3600s")


# ---------------------------------------------------------------------------
# Statistics primitives — generic, reusable for real or synthetic paired data.
# ---------------------------------------------------------------------------


def bootstrap_paired_ci(
    diffs: np.ndarray, n_boot: int = N_BOOT, alpha: float = CI_ALPHA, seed: int = RNG_SEED
) -> dict[str, float]:
    """Bootstrap 95% CI (seeded, percentile method) over paired differences."""
    diffs = np.asarray(diffs, dtype=np.float64)
    n = diffs.shape[0]
    if n == 0:
        return {"mean": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": 0}
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    boot_means = diffs[idx].mean(axis=1)
    lo, hi = np.percentile(boot_means, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return {
        "mean": float(diffs.mean()),
        "ci_lo": float(lo),
        "ci_hi": float(hi),
        "n": int(n),
        "n_boot": int(n_boot),
    }


def wilson_ci(successes: int, n: int, alpha: float = CI_ALPHA) -> dict[str, float]:
    """Wilson score interval for a binomial proportion — used when n is small,
    since it stays inside [0,1] and is less anti-conservative than the normal
    approximation at low counts."""
    if n == 0:
        return {"phat": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": 0}
    z = stats.norm.ppf(1 - alpha / 2)
    phat = successes / n
    denom = 1 + z**2 / n
    center = (phat + z**2 / (2 * n)) / denom
    half = (z * math.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2))) / denom
    return {
        "phat": float(phat),
        "ci_lo": float(max(0.0, center - half)),
        "ci_hi": float(min(1.0, center + half)),
        "n": int(n),
        "successes": int(successes),
        "underpowered": bool(n < UNDERPOWERED_N),
    }


def clopper_pearson_ci(successes: int, n: int, alpha: float = CI_ALPHA) -> dict[str, float]:
    """Exact binomial CI — reported alongside Wilson for the smallest cells,
    where the two can visibly diverge."""
    if n == 0:
        return {"phat": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": 0}
    lo = 0.0 if successes == 0 else stats.beta.ppf(alpha / 2, successes, n - successes + 1)
    hi = 1.0 if successes == n else stats.beta.ppf(1 - alpha / 2, successes + 1, n - successes)
    return {
        "phat": float(successes / n),
        "ci_lo": float(lo),
        "ci_hi": float(hi),
        "n": int(n),
        "successes": int(successes),
    }


def paired_delta_comet(
    rows: list[dict[str, Any]], cond_a: str, cond_b: str
) -> dict[str, float]:
    """Bootstrap paired CI for comet(cond_a) - comet(cond_b) over rows carrying
    both conditions' comet scores under keys f'comet_{cond}'."""
    diffs = np.array(
        [r[f"comet_{cond_a}"] - r[f"comet_{cond_b}"] for r in rows], dtype=np.float64
    )
    return bootstrap_paired_ci(diffs)


def marginal_mean_ci(rows: list[dict[str, Any]], cond: str) -> dict[str, float]:
    vals = np.array([r[f"comet_{cond}"] for r in rows], dtype=np.float64)
    return bootstrap_paired_ci(vals)  # same bootstrap machinery, single-sample mean


def true_regression_rate(rows: list[dict[str, Any]], cond: str) -> dict[str, float]:
    """Fraction of rows (restricted upstream to the injected-error ground-truth
    subset) where `cond`'s comet score dropped below the pre-repair baseline —
    i.e. a confirmed regression, not merely a checker-flagged one."""
    flags = [1 if r.get(f"true_regression_{cond}") else 0 for r in rows]
    n = len(flags)
    successes = sum(flags)
    return {"wilson": wilson_ci(successes, n), "clopper_pearson": clopper_pearson_ci(successes, n)}


def fix_rate(rows: list[dict[str, Any]], cond: str, ground_truth_only: bool) -> dict[str, float]:
    """Fraction of checker-flagged (or ground-truth-confirmed) spans that `cond`
    actually fixed."""
    key = f"gt_fixed_{cond}" if ground_truth_only else f"flagged_fixed_{cond}"
    flags = [1 if r.get(key) else 0 for r in rows if key in r]
    n = len(flags)
    successes = sum(flags)
    return {"wilson": wilson_ci(successes, n), "clopper_pearson": clopper_pearson_ci(successes, n)}


def edit_volume_to_gain_ratio(rows: list[dict[str, Any]], cond: str, baseline_cond: str) -> dict[str, float]:
    """Mean edited-character-fraction divided by mean ΔCOMET gain over baseline;
    reports the raw edit fraction alongside the ratio so a large ratio can be
    read as 'aggressive editing, little gain' rather than only inferred."""
    edit_fracs = [r[f"edit_char_fraction_{cond}"] for r in rows]
    gains = [r[f"comet_{cond}"] - r[f"comet_{baseline_cond}"] for r in rows]
    mean_edit_frac = float(np.mean(edit_fracs))
    mean_gain = float(np.mean(gains))
    ratio = mean_edit_frac / mean_gain if mean_gain != 0 else float("inf")
    return {
        "mean_edit_char_fraction": mean_edit_frac,
        "mean_comet_gain_over_baseline": mean_gain,
        "edit_volume_to_gain_ratio": ratio,
        "n": len(rows),
    }


def sensitivity_reanalysis(
    rows: list[dict[str, Any]],
    checker_precision_recall: dict[str, dict[str, float]],
    threshold: float,
) -> dict[str, Any]:
    """Recompute the core comparisons after excluding rows in (language,
    category) cells whose checker precision OR recall falls under `threshold`."""
    excluded_cells = [
        cell
        for cell, pr in checker_precision_recall.items()
        if pr.get("precision", 1.0) < threshold or pr.get("recall", 1.0) < threshold
    ]
    kept_rows = [
        r
        for r in rows
        if f"{r.get('language')}|{r.get('category')}" not in excluded_cells
    ]
    return {
        "threshold": threshold,
        "pre_registered_expected_weak_cells": [f"{l}|{c}" for l, c in FLAGGED_WEAK_CELLS],
        "excluded_cells": excluded_cells,
        "n_before": len(rows),
        "n_after": len(kept_rows),
        "delta_comet_d_minus_b_after_exclusion": (
            paired_delta_comet(kept_rows, "D", "B") if kept_rows else None
        ),
        "delta_comet_c1_minus_d_after_exclusion": (
            paired_delta_comet(kept_rows, "C1", "D") if kept_rows else None
        ),
    }


# ---------------------------------------------------------------------------
# Self-test — proves the statistics primitives are correct on synthetic
# fixtures BEFORE they are trusted on (or absence of) real data. Fixtures are
# clearly synthetic and never written into eval_out.json.
# ---------------------------------------------------------------------------


def run_self_test() -> dict[str, Any]:
    logger.info("Running self-test of statistics primitives on synthetic fixtures")
    rng = np.random.default_rng(0)
    n = 200
    comet_b = rng.normal(0.55, 0.05, n)
    comet_d = comet_b + rng.normal(0.01, 0.01, n)  # D slightly improves over B
    comet_c1 = comet_d + rng.normal(0.0, 0.01, n)  # C1 roughly ties D
    rows = [
        {
            "comet_B": float(comet_b[i]),
            "comet_D": float(comet_d[i]),
            "comet_C1": float(comet_c1[i]),
            "true_regression_D": bool(comet_d[i] < comet_b[i] - 0.02),
            "true_regression_C1": bool(comet_c1[i] < comet_d[i] - 0.02),
            "gt_fixed_D": bool(rng.random() < 0.6),
            "gt_fixed_C1": bool(rng.random() < 0.65),
            "flagged_fixed_D": bool(rng.random() < 0.8),
            "flagged_fixed_C1": bool(rng.random() < 0.82),
            "edit_char_fraction_D": float(rng.uniform(0.02, 0.08)),
            "edit_char_fraction_C1": float(rng.uniform(0.05, 0.20)),
            "language": ["cs_CZ", "is_IS", "ja_JP"][i % 3],
            "category": INVARIANT_CATEGORIES[i % 4],
        }
        for i in range(n)
    ]
    d_minus_b = paired_delta_comet(rows, "D", "B")
    c1_minus_d = paired_delta_comet(rows, "C1", "D")
    assert d_minus_b["mean"] > 0, "self-test: D should beat B by construction"
    assert d_minus_b["ci_lo"] < d_minus_b["mean"] < d_minus_b["ci_hi"]
    reg_d = true_regression_rate(rows, "D")
    assert 0.0 <= reg_d["wilson"]["phat"] <= 1.0
    fake_pr = {"cs_CZ|named_entity": {"precision": 0.3, "recall": 0.9}}
    sens = sensitivity_reanalysis(rows, fake_pr, SENSITIVITY_THRESHOLD)
    assert sens["n_after"] < sens["n_before"], "self-test: exclusion should drop rows"
    evgr = edit_volume_to_gain_ratio(rows, "C1", "D")
    assert evgr["mean_edit_char_fraction"] > 0
    wci = wilson_ci(3, 10)
    cci = clopper_pearson_ci(3, 10)
    assert wci["ci_lo"] < wci["phat"] < wci["ci_hi"]
    assert cci["ci_lo"] < cci["phat"] < cci["ci_hi"]
    logger.success("Self-test PASSED: bootstrap CI, Wilson/Clopper-Pearson CI, sensitivity re-analysis, edit-ratio all behave as expected on synthetic fixtures")
    return {
        "status": "PASSED",
        "n_synthetic_rows": n,
        "d_minus_b_delta_comet_synthetic": d_minus_b,
        "c1_minus_d_delta_comet_synthetic": c1_minus_d,
        "note": "Synthetic fixture used ONLY to validate the statistics code paths; not used anywhere in eval_out.json's reported metrics.",
    }


# ---------------------------------------------------------------------------
# Discovery of real sibling-artifact inputs (never fabricated if absent).
# ---------------------------------------------------------------------------


_PRUNE_DIRS = {".venv", "venv", ".git", "node_modules", "__pycache__", ".ability_client_venv"}
_MAX_FILES_SCANNED_PER_SIBLING = 20_000  # sibling experiments run concurrently and may
# still be mid-install (growing .venv trees); this caps worst-case scan cost per sibling.


def _iter_files_pruned(root: Path):
    """os.walk with topdown pruning of venvs/.git/node_modules — sibling
    experiment agents run concurrently and may be mid-`uv pip install`, so a
    naive rglob can spend minutes walking a growing site-packages tree."""
    import os as _os

    scanned = 0
    for dirpath, dirnames, filenames in _os.walk(root, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in _PRUNE_DIRS]
        for fn in filenames:
            scanned += 1
            if scanned > _MAX_FILES_SCANNED_PER_SIBLING:
                logger.warning(f"{root}: exceeded scan cap ({_MAX_FILES_SCANNED_PER_SIBLING} files), stopping early")
                return
            yield Path(dirpath) / fn


def discover_input_files() -> dict[str, list[Path]]:
    """Scan sibling iter_2 gen_art (and gen_plan, defensively) output
    directories for files matching the three expected input types. Returns
    empty lists, not errors, when nothing is found. Prunes venv/git/node_modules
    subtrees since sibling experiment agents may be running concurrently and
    mid-install."""
    import fnmatch

    iter_root = WORKSPACE.parent.parent  # .../iter_2
    search_roots = [iter_root / "gen_art", iter_root / "gen_plan", iter_root / "gen_exp", iter_root / "gen_data"]
    patterns = {
        "checker_validation": ["checker_validation*.json", "*checker_validation*.json"],
        "condition_b_fidelity": ["condition_b_fidelity*.json", "*condition_b_fidelity*.json", "*fidelity_gate*.json"],
        "b_d_c1_results": ["b_d_c1_results*.json", "*b_d_c1*.json", "method_out*.json", "*_out.json"],
    }
    found: dict[str, list[Path]] = {k: [] for k in patterns}
    for root in search_roots:
        if not root.exists():
            continue
        for sibling in sorted(root.iterdir()):
            if not sibling.is_dir() or sibling == WORKSPACE:
                continue
            for f in _iter_files_pruned(sibling):
                for key, globs in patterns.items():
                    if any(fnmatch.fnmatch(f.name, g) for g in globs) and f not in found[key]:
                        found[key].append(f)
    for key, files in found.items():
        logger.info(f"discovered {len(files)} candidate file(s) for '{key}': {[str(f) for f in files]}")
    return found


def try_load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError, UnicodeDecodeError) as e:
        logger.warning(f"malformed/unreadable JSON at {path}: {e}")
        return None


# ---------------------------------------------------------------------------
# Descriptive stats computable from the real dataset dependency alone (no
# checker predictions needed) — grounds the report in real numbers even when
# the experiment outputs are absent.
# ---------------------------------------------------------------------------


def summarize_checker_validation_heldout_composition() -> dict[str, Any]:
    """Real composition (language x category counts) of the checker-validation
    heldout fold, computed directly from the dataset dependency. This is NOT a
    precision/recall measurement (no checker predictions exist to score) — it
    only characterizes how much ground truth would be available to score
    against, once a checker's predictions exist."""
    full_path = DEP_DATA / "full_data_out.json"
    if not full_path.exists():
        logger.warning(f"dataset dependency not found at {full_path}")
        return {"status": "NOT_AVAILABLE", "reason": "dependency dataset file missing"}
    data = json.loads(full_path.read_text())
    injected = next(
        (ds for ds in data["datasets"] if ds["dataset"] == "injected_error_augmentation"), None
    )
    if injected is None:
        return {"status": "NOT_AVAILABLE", "reason": "injected_error_augmentation dataset group missing"}
    counts: dict[str, int] = {}
    lang_totals: dict[str, int] = {}
    for ex in injected["examples"]:
        if ex.get("metadata_fold") != "checker_validation_heldout":
            continue
        lang = ex.get("metadata_language_pair", "unknown")
        cat = ex.get("metadata_invariant_category", "unknown")
        cell = f"{lang}|{cat}"
        counts[cell] = counts.get(cell, 0) + 1
        lang_totals[lang] = lang_totals.get(lang, 0) + 1
    del data
    gc.collect()
    weak_cells_present = {
        f"en-{lang}|named_entity_swap": counts.get(f"en-{lang}|named_entity_swap", 0)
        for lang in ["zh_CN", "ja_JP"]
    }
    return {
        "status": "COMPUTED_FROM_DATASET_NOT_A_CHECKER_SCORE",
        "note": (
            "Row counts per (language_pair, invariant_category) cell in the "
            "checker_validation_heldout fold, from the real dataset dependency. "
            "Precision/recall against these cells is NOT_AVAILABLE because no "
            "checker prediction file was found among sibling artifacts (see "
            "checker_validation_precision_recall below)."
        ),
        "cell_counts": counts,
        "language_pair_totals": lang_totals,
        "zh_CN_ja_JP_named_entity_swap_cell_counts": weak_cells_present,
    }


# ---------------------------------------------------------------------------
# Main evaluation, degrading gracefully per input type.
# ---------------------------------------------------------------------------


def build_reconciliation_table(measured_by_langpair: dict[str, dict[str, float]] | None) -> dict[str, Any]:
    """Metric (f): six-language-pair ΔCOMET table, quoted-vs-measured."""
    rows = []
    for lp in ["en-cs_CZ", "en-is_IS", "en-ja_JP", "en-ru_RU", "en-uk_UA", "en-zh_CN"]:
        quoted_surreypai = PADMANABHAN_TABLE15["SURREYPAI-S2"].get(lp)
        quoted_baseline = PADMANABHAN_TABLE15["BASELINE-S2"].get(lp)
        measured = (measured_by_langpair or {}).get(lp)
        rows.append(
            {
                "language_pair": lp,
                "quoted_surreypai_s2_delta_comet": quoted_surreypai["delta_comet"] if quoted_surreypai else "NOT_REPORTED_IN_SOURCE",
                "quoted_surreypai_s2_ger": quoted_surreypai["ger"] if quoted_surreypai else "NOT_REPORTED_IN_SOURCE",
                "quoted_baseline_s2_delta_comet": quoted_baseline["delta_comet"] if quoted_baseline else "NOT_REPORTED_IN_SOURCE",
                "quoted_baseline_s2_ger": quoted_baseline["ger"] if quoted_baseline else "NOT_REPORTED_IN_SOURCE",
                "quote_location": PADMANABHAN_TABLE15_SOURCE,
                "measured_this_iteration": measured if measured is not None else "NOT_AVAILABLE",
            }
        )
    return {
        "rows": rows,
        "coverage_note": (
            "This iteration's B/D/C1 experiments (gen_art_experiment_1/2/3 in "
            "iter_2/gen_art) produced no result files at evaluation time — all "
            "'measured_this_iteration' cells are NOT_AVAILABLE. The quoted "
            "columns are the paper's own published per-language-pair figures, "
            "verified against the primary source, not measurements made here. "
            "The artifact plan itself documents that even a completed run "
            "would cover only ~2 of these 6 language pairs (a subset of "
            "experimental_pool), so the coverage gap is structural, not only "
            "a symptom of missing outputs."
        ),
    }


@logger.catch(reraise=True)
def main() -> None:
    set_resource_limits()
    self_test_result = run_self_test()

    logger.info("Discovering sibling experiment input files (B/D/C1, checker-validation, fidelity-gate)")
    found = discover_input_files()

    checker_validation_data = None
    for f in found["checker_validation"]:
        loaded = try_load_json(f)
        if loaded is not None:
            checker_validation_data = {"source_file": str(f), "content": loaded}
            break

    fidelity_gate_data = None
    for f in found["condition_b_fidelity"]:
        loaded = try_load_json(f)
        if loaded is not None:
            fidelity_gate_data = {"source_file": str(f), "content": loaded}
            break

    bdcresults_data = None
    for f in found["b_d_c1_results"]:
        loaded = try_load_json(f)
        if loaded is not None and isinstance(loaded, dict) and "datasets" in loaded:
            bdcresults_data = {"source_file": str(f), "content": loaded}
            break

    dataset_composition = summarize_checker_validation_heldout_composition()

    # --- (g) fidelity-gate verdict: first-class, prominent -----------------
    if fidelity_gate_data is not None:
        verdict = fidelity_gate_data["content"].get("verdict", "MALFORMED_NO_VERDICT_FIELD")
        fidelity_gate_verdict = verdict
        fidelity_gate_evidence = fidelity_gate_data["content"]
    else:
        fidelity_gate_verdict = "NOT_AVAILABLE"
        fidelity_gate_evidence = {
            "reason": (
                "No condition_b_fidelity*.json (or equivalent) file was found among "
                "sibling iter_2 gen_art experiment outputs at evaluation time — the "
                "three sibling experiment sessions (gen_art_experiment_1/2/3) had not "
                "written any result files (only in-progress terminal session logs "
                "existed)."
            ),
            "searched_files": [str(f) for f in found["condition_b_fidelity"]],
        }

    top_level_caveat = (
        "CONDITION-B FIDELITY GATE: " + fidelity_gate_verdict + ". "
        + (
            "Every B/D/C1 comparison below is conditional on this verdict; a "
            "FAIL or NOT_AVAILABLE verdict means the absolute ΔCOMET/regression/"
            "fix-rate numbers below (where present) cannot be attributed to "
            "Padmanabhan's original SURREYPAI-S2 design — only to the substitute "
            "google/gemma-3-12b-it pipeline as actually run, since TowerPlus-9B "
            "is confirmed unavailable on OpenRouter (see iter_1 gen_art_research_1)."
            if fidelity_gate_verdict != "PASS"
            else "Gate passed: the substitute-model pipeline is judged faithful "
            "enough to support attributing the comparison to the original design."
        )
    )

    # --- (a)-(e): paired B/D/C1 comparisons ---------------------------------
    if bdcresults_data is not None:
        content = bdcresults_data["content"]
        rows: list[dict[str, Any]] = []
        for ds in content.get("datasets", []):
            for ex in ds.get("examples", []):
                rows.append(ex)
        logger.info(f"loaded {len(rows)} per-sentence B/D/C1 rows from {bdcresults_data['source_file']}")
        required = {"comet_B", "comet_D", "comet_C1"}
        usable_rows = [r for r in rows if required.issubset(r.keys())]
        if not usable_rows:
            logger.warning("b_d_c1_results file found but no rows carry comet_B/comet_D/comet_C1 — treating as unusable")
        paired_comparisons: dict[str, Any] | str
        if usable_rows:
            paired_comparisons = {
                "n_paired_rows": len(usable_rows),
                "delta_comet_D_minus_B": paired_delta_comet(usable_rows, "D", "B"),
                "delta_comet_C1_minus_D": paired_delta_comet(usable_rows, "C1", "D"),
                "delta_comet_C1_minus_B": paired_delta_comet(usable_rows, "C1", "B"),
                "marginal_mean_comet_B": marginal_mean_ci(usable_rows, "B"),
                "marginal_mean_comet_D": marginal_mean_ci(usable_rows, "D"),
                "marginal_mean_comet_C1": marginal_mean_ci(usable_rows, "C1"),
                "true_regression_rate_D": true_regression_rate(usable_rows, "D"),
                "true_regression_rate_C1": true_regression_rate(usable_rows, "C1"),
                "fix_rate_D_all_flagged": fix_rate(usable_rows, "D", ground_truth_only=False),
                "fix_rate_D_ground_truth_only": fix_rate(usable_rows, "D", ground_truth_only=True),
                "fix_rate_C1_all_flagged": fix_rate(usable_rows, "C1", ground_truth_only=False),
                "fix_rate_C1_ground_truth_only": fix_rate(usable_rows, "C1", ground_truth_only=True),
                "edit_volume_to_gain_D": edit_volume_to_gain_ratio(usable_rows, "D", "B"),
                "edit_volume_to_gain_C1": edit_volume_to_gain_ratio(usable_rows, "C1", "D"),
            }
        else:
            paired_comparisons = "NOT_AVAILABLE"
    else:
        usable_rows = []
        paired_comparisons = "NOT_AVAILABLE"
        logger.warning("no usable b_d_c1_results file found among sibling artifacts")

    # --- (1) checker precision/recall table ---------------------------------
    if checker_validation_data is not None:
        checker_pr_table = checker_validation_data["content"]
    else:
        checker_pr_table = {
            "status": "NOT_AVAILABLE",
            "reason": (
                "No checker_validation*.json (or equivalent) file was found among "
                "sibling iter_2 gen_art experiment outputs."
            ),
            "searched_files": [str(f) for f in found["checker_validation"]],
        }

    # --- (e) sensitivity re-analysis -----------------------------------------
    if usable_rows and isinstance(checker_pr_table, dict) and "cells" in checker_pr_table:
        sensitivity = sensitivity_reanalysis(usable_rows, checker_pr_table["cells"], SENSITIVITY_THRESHOLD)
    else:
        sensitivity = {
            "status": "NOT_AVAILABLE",
            "reason": (
                "Requires both usable per-sentence B/D/C1 rows AND a checker "
                "precision/recall table with a 'cells' mapping — at least one is "
                "missing."
            ),
            "pre_registered_expected_weak_cells": [f"{l}|{c}" for l, c in FLAGGED_WEAK_CELLS],
            "pre_registered_threshold": SENSITIVITY_THRESHOLD,
        }

    # --- (f) six-language reconciliation table -------------------------------
    measured_by_langpair = None
    if usable_rows:
        by_lp: dict[str, list[dict[str, Any]]] = {}
        for r in usable_rows:
            lp = r.get("metadata_language_pair") or r.get("language_pair")
            if lp:
                by_lp.setdefault(lp, []).append(r)
        if by_lp:
            measured_by_langpair = {
                lp: {
                    "delta_comet_D_minus_B": paired_delta_comet(rs, "D", "B"),
                    "delta_comet_C1_minus_B": paired_delta_comet(rs, "C1", "B"),
                    "n": len(rs),
                }
                for lp, rs in by_lp.items()
            }
    reconciliation_table = build_reconciliation_table(measured_by_langpair)

    # ---------------------------------------------------------------------
    # Assemble metrics_agg (flat numeric-only, per exp_eval_sol_out schema)
    # ---------------------------------------------------------------------
    metrics_agg: dict[str, float] = {
        "n_input_types_expected": 3,
        "n_input_types_available": sum(
            x is not None for x in [checker_validation_data, fidelity_gate_data, bdcresults_data]
        ),
        "data_availability_fraction": sum(
            x is not None for x in [checker_validation_data, fidelity_gate_data, bdcresults_data]
        ) / 3.0,
        "n_paired_bdc1_rows_used": len(usable_rows),
        "padmanabhan_self_reported_avg_delta_comet_surreypai_s2": PADMANABHAN_SELF_REPORTED_AVG_DELTA_COMET,
        "padmanabhan_table15_avg_delta_comet_surreypai_s2": PADMANABHAN_TABLE15["SURREYPAI-S2"]["average"]["delta_comet"],
        "padmanabhan_table15_avg_delta_comet_baseline_s2": PADMANABHAN_TABLE15["BASELINE-S2"]["average"]["delta_comet"],
        "n_checker_validation_heldout_cells_with_dataset_ground_truth": len(
            dataset_composition.get("cell_counts", {})
        ),
        "self_test_passed": 1.0 if self_test_result["status"] == "PASSED" else 0.0,
    }
    if isinstance(paired_comparisons, dict):
        metrics_agg["delta_comet_D_minus_B_mean"] = paired_comparisons["delta_comet_D_minus_B"]["mean"]
        metrics_agg["delta_comet_C1_minus_D_mean"] = paired_comparisons["delta_comet_C1_minus_D"]["mean"]
        metrics_agg["delta_comet_C1_minus_B_mean"] = paired_comparisons["delta_comet_C1_minus_B"]["mean"]

    # ---------------------------------------------------------------------
    # Build the `datasets` array (schema requires >=1 dataset, >=1 example,
    # each example needs `input`/`output`; per-example eval_* fields must be
    # numeric).
    # ---------------------------------------------------------------------
    status_examples = []
    for key, present, source_files in [
        ("checker_validation_precision_recall", checker_validation_data is not None, found["checker_validation"]),
        ("condition_b_fidelity_gate", fidelity_gate_data is not None, found["condition_b_fidelity"]),
        ("b_d_c1_per_sentence_results", bdcresults_data is not None, found["b_d_c1_results"]),
    ]:
        status_examples.append(
            {
                "input": f"expected sibling-artifact input: {key}",
                "output": "AVAILABLE" if present else "NOT_AVAILABLE",
                "metadata_searched_files": [str(f) for f in source_files],
                "metadata_search_roots": [
                    str(WORKSPACE.parent.parent / d) for d in ["gen_art", "gen_plan", "gen_exp", "gen_data"]
                ],
                "predict_availability_status": "AVAILABLE" if present else "NOT_AVAILABLE",
                "eval_available": 1.0 if present else 0.0,
            }
        )

    reconciliation_examples = []
    for row in reconciliation_table["rows"]:
        quoted = row["quoted_surreypai_s2_delta_comet"]
        reconciliation_examples.append(
            {
                "input": f"WMT25 Table 15 SURREYPAI-S2/BASELINE-S2 vs this iteration's measurement, language pair {row['language_pair']}",
                "output": json.dumps(row, ensure_ascii=False),
                "metadata_language_pair": row["language_pair"],
                "metadata_quote_location": row["quote_location"],
                "predict_measured_this_iteration": str(row["measured_this_iteration"]),
                "eval_quoted_surreypai_s2_delta_comet": float(quoted) if isinstance(quoted, (int, float)) else float("nan"),
                "eval_measured_available": 1.0 if row["measured_this_iteration"] != "NOT_AVAILABLE" else 0.0,
            }
        )

    datasets_out = [
        {"dataset": "input_availability_status", "examples": status_examples},
        {"dataset": "six_language_pair_delta_comet_reconciliation", "examples": reconciliation_examples},
    ]
    if usable_rows:
        bdc_examples = []
        for r in usable_rows[:5000]:  # safety cap; per-sentence detail is already in the source file
            bdc_examples.append(
                {
                    "input": r.get("input", "")[:2000] if isinstance(r.get("input"), str) else str(r.get("input"))[:2000],
                    "output": r.get("output", "")[:2000] if isinstance(r.get("output"), str) else str(r.get("output"))[:2000],
                    "metadata_language_pair": r.get("metadata_language_pair") or r.get("language_pair"),
                    "eval_comet_B": float(r["comet_B"]),
                    "eval_comet_D": float(r["comet_D"]),
                    "eval_comet_C1": float(r["comet_C1"]),
                    "eval_delta_comet_D_minus_B": float(r["comet_D"] - r["comet_B"]),
                    "eval_delta_comet_C1_minus_D": float(r["comet_C1"] - r["comet_D"]),
                }
            )
        datasets_out.append({"dataset": "b_d_c1_per_sentence_deltas", "examples": bdc_examples})

    output = {
        "metadata": {
            "evaluation_name": "Does Hygiene or Verification Fix Editing? — B/D/C1 paired comparison",
            "description": (
                "Evaluates checker-validation precision/recall, the condition-B "
                "fidelity-gate verdict, and per-sentence B/D/C1 span-editing "
                "results from this iteration's sibling gen_art experiments. "
                "Degrades gracefully to NOT_AVAILABLE per component when the "
                "corresponding sibling experiment produced no output file."
            ),
            "condition_b_fidelity_gate_verdict": fidelity_gate_verdict,
            "top_level_caveat": top_level_caveat,
            "self_test": self_test_result,
            "detailed_results": {
                "1_checker_validation_precision_recall": checker_pr_table,
                "1b_checker_validation_heldout_dataset_composition": dataset_composition,
                "2_condition_b_fidelity_gate": {"verdict": fidelity_gate_verdict, "evidence": fidelity_gate_evidence},
                "a_paired_delta_comet_and_related_bdc1_metrics": paired_comparisons,
                "e_sensitivity_reanalysis_precision_recall_gated": sensitivity,
                "f_six_language_pair_reconciliation_table": reconciliation_table,
            },
        },
        "metrics_agg": metrics_agg,
        "datasets": datasets_out,
    }

    out_path = WORKSPACE / "eval_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.success(f"Wrote {out_path} ({out_path.stat().st_size / 1e3:.1f} KB)")

    del output
    gc.collect()


if __name__ == "__main__":
    main()
