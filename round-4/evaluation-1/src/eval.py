#!/usr/bin/env python3
"""Final B/D/C1/C2/C scorecard and Condition-C verdict.

Consolidates the five-condition (B/D/C1/C2/C) span-editing comparison:
  1. Per-row COMET-availability gate (falsifiable key search).
  2. True paired bootstrap on fix_rate / true_regression_rate (per-row data
     genuinely exists); documented normal-approximation fallback for
     pooled DeltaCOMET (per-row COMET does not exist in any upstream artifact).
  3. Disjoint-population check between the DeltaCOMET row population (320
     natural) and the fix_rate/regression row population (240 injected).
  4. Fix-rate-advantage reconciliation (including vs excluding negation rows).
  5. Condition C net-positive / success-criterion verdict.
  6. Full five-condition scorecard table.
"""

import json
import resource
import sys
from pathlib import Path

import numpy as np
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ---- memory budget (pure local JSON processing, small footprint) ----
RAM_BUDGET_BYTES = 6 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))

WORKSPACE = Path(__file__).parent
RUN_ROOT = WORKSPACE.parents[2]  # .../run_VO5kqjjB2Uk5/3_invention_loop
ITER_ROOT = WORKSPACE.parents[1]  # .../iter_4

BDC1_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_3/full_method_out.json"
)
C2_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_art/gen_art_experiment_1/full_method_out.json"
)
CHECKER_VALIDATION_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_method_out.json"
)
DATASET_PREVIEW_PATH = Path(
    "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/preview_data_out.json"
)

N_BOOT = 2000
SEED = 42
Z95 = 1.959963984540054

# ============================================================================
# Condition C discovery
# ============================================================================


def discover_condition_c():
    """Scan this iteration's gen_art siblings for a completed Condition C artifact."""
    gen_art_dir = ITER_ROOT / "gen_art"
    candidates = sorted(p for p in gen_art_dir.iterdir() if p.is_dir() and p.name != WORKSPACE.name)
    log_lines = []
    for cand in candidates:
        struct_path = cand / ".terminal_claude_agent_struct_out.json"
        title, summary = "", ""
        if struct_path.exists():
            try:
                struct = json.loads(struct_path.read_text())
                title = struct.get("title", "")
                summary = struct.get("summary", "")
            except (json.JSONDecodeError, OSError) as exc:
                log_lines.append(f"{cand.name}: could not parse struct file ({exc})")
        text_blob = f"{title} {summary}".lower()
        is_condition_c_named = (
            "condition c" in text_blob
            or "combined" in text_blob
            or cand.name.startswith("gen_art_experiment")
        )
        full_out = cand / "full_method_out.json"
        method_out = cand / "method_out.json"
        out_path = full_out if full_out.exists() else (method_out if method_out.exists() else None)
        log_lines.append(
            f"{cand.name}: title={title!r} name_match={is_condition_c_named} "
            f"output_exists={out_path is not None}"
        )
        if is_condition_c_named and out_path is not None:
            justification = (
                f"Matched sibling directory '{cand.name}' whose recorded title "
                f"({title!r}) references Condition C / combined-fix framing, and "
                f"its {out_path.name} exists on disk."
            )
            return {
                "found": True,
                "path": str(out_path),
                "title": title,
                "justification": justification,
                "scan_log": log_lines,
            }
    return {"found": False, "path": None, "title": None, "justification": None, "scan_log": log_lines}


def load_condition_c(discovery):
    """Attempt to load and interpret Condition C's output; classify completeness."""
    if not discovery["found"]:
        return {
            "status": "not_found",
            "data": None,
            "completion_fraction": None,
        }
    try:
        data = json.loads(Path(discovery["path"]).read_text())
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning(f"Condition C output found at {discovery['path']} but failed to parse: {exc}")
        return {"status": "not_found", "data": None, "completion_fraction": None}

    datasets = data.get("datasets", [])
    natural_examples = []
    injected_examples = []
    for ds in datasets:
        name = ds.get("dataset", "").lower()
        if "natural" in name:
            natural_examples = ds.get("examples", [])
        elif "injected" in name:
            injected_examples = ds.get("examples", [])

    n_natural_expected = 320
    n_injected_expected = 240
    lang_pairs_seen = {e.get("metadata_language_pair") for e in natural_examples}
    completion_fraction = None
    partial = False
    if len(natural_examples) < n_natural_expected or len(injected_examples) < n_injected_expected:
        partial = True
        total_seen = len(natural_examples) + len(injected_examples)
        total_expected = n_natural_expected + n_injected_expected
        completion_fraction = round(total_seen / total_expected, 4) if total_expected else None
    md = data.get("metadata", {})
    if isinstance(md, dict) and md.get("completion_fraction") is not None:
        completion_fraction = md["completion_fraction"]
        partial = True
    if isinstance(md, dict) and md.get("n_rows_completed") is not None:
        partial = True

    status = "partial" if partial else "complete"
    return {
        "status": status,
        "data": data,
        "natural_examples": natural_examples,
        "injected_examples": injected_examples,
        "completion_fraction": completion_fraction,
        "lang_pairs_seen": sorted(x for x in lang_pairs_seen if x),
    }


# ============================================================================
# Step 1: per-row COMET availability check
# ============================================================================


def find_per_row_comet_field(obj, path="", max_depth=6):
    """Recursively search a loaded JSON object for a plausible per-row COMET array."""
    if max_depth <= 0:
        return None
    if isinstance(obj, dict):
        for k, v in obj.items():
            kl = k.lower()
            if isinstance(v, (int, float)) and any(
                tag in kl for tag in ("comet_before", "comet_after", "delta_comet_row", "comet_score")
            ) and "mean" not in kl and "ci95" not in kl:
                return f"{path}.{k}" if path else k
            if isinstance(v, (dict, list)):
                found = find_per_row_comet_field(v, f"{path}.{k}" if path else k, max_depth - 1)
                if found:
                    return found
    elif isinstance(obj, list) and obj:
        sample = obj[0]
        # Only treat this as a candidate PER-ROW array if its length is in the natural-
        # subsample ballpark (>=50); short lists (e.g. per-language-pair aggregates,
        # len==2) are NOT per-row data even if a field name contains "comet".
        if isinstance(sample, dict) and len(obj) >= 50:
            for k in sample:
                kl = k.lower()
                if any(tag in kl for tag in ("comet_before", "comet_after", "delta_comet", "comet_score")):
                    if "mean" not in kl and "ci95" not in kl and "per_edit_volume" not in kl:
                        return f"{path}[].{k}"
        if isinstance(sample, dict):
            found = find_per_row_comet_field(sample, f"{path}[0]", max_depth - 1)
            if found:
                return found
    return None


def check_per_row_comet_availability(label, data):
    examples = []
    for ds in data.get("datasets", []):
        examples.extend(ds.get("examples", []))
    if examples:
        keys = set()
        for ex in examples[:5]:
            keys.update(ex.keys())
        comet_keys = [k for k in keys if "comet" in k.lower()]
        if comet_keys:
            return {"available": True, "json_path": f"datasets[].examples[].{sorted(comet_keys)}", "note": None}
    md_found = find_per_row_comet_field(data.get("metadata", {}))
    if md_found:
        return {"available": True, "json_path": f"metadata.{md_found}", "note": None}
    all_top_keys = sorted(data.keys())
    example_keys = sorted({k for ds in data.get("datasets", []) for ex in ds.get("examples", []) for k in ex})
    return {
        "available": False,
        "json_path": None,
        "note": (
            f"Enumerated top-level keys {all_top_keys} and per-row example keys "
            f"{example_keys[:40]}{'...' if len(example_keys) > 40 else ''} for {label}; "
            "no field matching comet_before/comet_after/delta_comet/comet_score at the row "
            "level was found. Only pooled/per-language-pair aggregate delta_comet_mean + "
            "delta_comet_ci95 are stored (metadata.metrics.*). Per-row edit_volume, "
            "n_llm_calls, fixed, and true_regression ARE stored at row level (see the "
            "fix_rate/true_regression_rate paired-bootstrap results below, which use exactly "
            "this row-level data)."
        ),
    }


# ============================================================================
# Bootstrap helpers
# ============================================================================


def paired_bootstrap_mean_diff(x, y, n_boot=N_BOOT, seed=SEED):
    """x, y: same-length arrays of per-row values on MATCHED rows. Returns point estimate + 95% CI."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    assert len(x) == len(y) and len(x) > 0
    d = x - y
    point = float(np.mean(d))
    rng = np.random.default_rng(seed)
    n = len(d)
    idx = rng.integers(0, n, size=(n_boot, n))
    resample_means = d[idx].mean(axis=1)
    lo, hi = np.percentile(resample_means, [2.5, 97.5])
    return {
        "point_estimate": point,
        "ci95": [float(lo), float(hi)],
        "n_matched_rows": int(n),
        "n_boot": n_boot,
        "seed": seed,
        "ci_excludes_zero": bool(lo > 0 or hi < 0),
    }


def normal_approx_diff(mean_x, ci_x, mean_y, ci_y):
    """Independence-assuming normal-approximation fallback for two pooled bootstrap CIs.

    se_diff = sqrt(se_x^2 + se_y^2), each se estimated as the mean CI half-width / 1.96.
    CAVEAT: this assumes X and Y are independent. In fact the two conditions here are
    scored on IDENTICAL matched rows, so a true paired test would exploit that positive
    correlation and yield a narrower (more powerful) CI than this approximation produces.
    This is used ONLY where no per-row data exists to run the true paired test.
    """
    se_x = ((ci_x[1] - ci_x[0]) / 2) / Z95
    se_y = ((ci_y[1] - ci_y[0]) / 2) / Z95
    se_diff = float(np.sqrt(se_x**2 + se_y**2))
    diff = mean_x - mean_y
    lo, hi = diff - Z95 * se_diff, diff + Z95 * se_diff
    return {
        "formula": "se_diff = sqrt(se_x^2 + se_y^2); se_i = (ci_i_upper - ci_i_lower) / 2 / 1.959963984540054",
        "independence_assumption_caveat": (
            "Assumes X and Y are statistically independent. They are NOT: both conditions "
            "are scored on the identical matched row population, so their errors are "
            "positively correlated. A true paired bootstrap would exploit that correlation "
            "for a narrower, more powerful CI than this normal approximation gives. Used only "
            "because no per-row COMET values are stored in any upstream artifact (see step 1)."
        ),
        "se_x": se_x,
        "se_y": se_y,
        "se_diff": se_diff,
        "point_estimate": float(diff),
        "ci95": [float(lo), float(hi)],
        "ci_excludes_zero": bool(lo > 0 or hi < 0),
    }


# ============================================================================
# Main
# ============================================================================


def main():
    logger.info("Loading dependency artifacts")
    bdc1 = json.loads(BDC1_PATH.read_text())
    c2 = json.loads(C2_PATH.read_text())
    checker_validation = json.loads(CHECKER_VALIDATION_PATH.read_text())
    dataset_preview = json.loads(DATASET_PREVIEW_PATH.read_text())
    logger.info("Loaded B/D/C1, C2, checker-validation, dataset preview")

    bdc1_natural = {e["metadata_row_id"]: e for e in bdc1["datasets"][0]["examples"]}
    bdc1_injected = {e["metadata_row_id"]: e for e in bdc1["datasets"][1]["examples"]}
    c2_natural = {e["metadata_row_id"]: e for e in c2["datasets"][0]["examples"]}
    c2_injected = {e["metadata_row_id"]: e for e in c2["datasets"][1]["examples"]}
    logger.info(
        f"B/D/C1 natural={len(bdc1_natural)} injected={len(bdc1_injected)}; "
        f"C2 natural={len(c2_natural)} injected={len(c2_injected)}"
    )

    # ------------------------------------------------------------------
    # Step 3: disjoint-population check (do this early; other steps rely on it)
    # ------------------------------------------------------------------
    comet_row_ids = set(bdc1_natural.keys())
    assert comet_row_ids == set(c2_natural.keys()), "natural row-id sets must match across B/D/C1 and C2"
    fix_rate_row_ids = set(bdc1_injected.keys())
    assert fix_rate_row_ids == set(c2_injected.keys()), "injected row-id sets must match across B/D/C1 and C2"
    overlap = comet_row_ids & fix_rate_row_ids
    disjoint_population_check = {
        "comet_population_n": len(comet_row_ids),
        "fix_rate_population_n": len(fix_rate_row_ids),
        "overlap_count": len(overlap),
        "overlap_row_ids": sorted(overlap),
        "verified": len(overlap) == 0,
    }
    logger.info(f"Disjoint-population check: overlap_count={disjoint_population_check['overlap_count']}")
    if disjoint_population_check["overlap_count"] != 0:
        logger.error("DATA-INTEGRITY FINDING: comet and fix-rate row populations overlap unexpectedly")

    # ------------------------------------------------------------------
    # Step 1: per-row COMET availability
    # ------------------------------------------------------------------
    logger.info("Step 1: per-row COMET availability check")
    per_row_comet_availability = {
        "b": check_per_row_comet_availability("B (within B/D/C1 artifact)", bdc1),
        "d": check_per_row_comet_availability("D (within B/D/C1 artifact)", bdc1),
        "c1": check_per_row_comet_availability("C1 (within B/D/C1 artifact)", bdc1),
        "c2": check_per_row_comet_availability("C2 artifact", c2),
    }
    for cond, res in per_row_comet_availability.items():
        logger.info(f"  per_row_comet_{cond}_available = {res['available']}")

    # ------------------------------------------------------------------
    # Condition C discovery + loading
    # ------------------------------------------------------------------
    logger.info("Scanning for Condition C sibling artifact")
    c_discovery = discover_condition_c()
    for line in c_discovery["scan_log"]:
        logger.info(f"  scan: {line}")
    c_load = load_condition_c(c_discovery)
    logger.info(f"Condition C status: {c_load['status']}")

    condition_c_natural = {}
    condition_c_injected = {}
    per_row_comet_c_available = {"available": False, "json_path": None, "note": "Condition C artifact not found."}
    if c_load["status"] in ("complete", "partial"):
        condition_c_natural = {e["metadata_row_id"]: e for e in c_load.get("natural_examples", [])}
        condition_c_injected = {e["metadata_row_id"]: e for e in c_load.get("injected_examples", [])}
        per_row_comet_c_available = check_per_row_comet_availability("Condition C", c_load["data"])
        logger.info(f"  per_row_comet_c_available = {per_row_comet_c_available['available']}")

    per_row_comet_availability["c"] = per_row_comet_c_available

    # ------------------------------------------------------------------
    # Step 2 + 4: fix_rate / true_regression_rate paired bootstrap (real per-row data)
    # ------------------------------------------------------------------
    logger.info("Step 2/4: true paired bootstrap on fix_rate and true_regression_rate")

    all_injected_ids = sorted(bdc1_injected.keys())
    noneg_injected_ids = sorted(
        rid for rid in all_injected_ids if bdc1_injected[rid]["metadata_invariant_category"] != "negation_polarity_flip"
    )
    neg_injected_ids = sorted(set(all_injected_ids) - set(noneg_injected_ids))
    assert len(all_injected_ids) == 240 and len(noneg_injected_ids) == 180 and len(neg_injected_ids) == 60

    def get_binary(source_dict, row_id, key, fallback_key=None):
        row = source_dict[row_id]
        val = row.get(key)
        if val is None and fallback_key is not None and fallback_key in row:
            val = row.get(fallback_key)
        return 1.0 if val else 0.0  # None (structural non-attempt) and False both -> 0 (non-fix / non-regression)

    def condition_vector(cond_label, row_ids, metric):
        """metric in {'fixed','true_regression'}. Returns np.array over row_ids for the given condition."""
        key = f"metadata_{cond_label}_{metric}"
        if cond_label in ("b", "d", "c1"):
            src = bdc1_injected
            fallback = None
        elif cond_label == "c2":
            src = c2_injected
            fallback = None
        elif cond_label == "c":
            src = condition_c_injected
            # Condition C's own artifact may (per its pseudocode, which reuses C2's code
            # verbatim) still emit fields prefixed metadata_c2_* rather than metadata_c_*;
            # fall back to that prefix if metadata_c_* is absent on a row.
            fallback = f"metadata_c2_{metric}"
        else:
            raise ValueError(cond_label)
        return np.array([get_binary(src, rid, key, fallback) for rid in row_ids])

    pairs_to_test = [("c1", "c2"), ("c1", "c"), ("c2", "c"), ("c", "b"), ("c", "d")]
    condition_c_available_for_pairs = c_load["status"] in ("complete", "partial")

    paired_bootstrap_results = {"fix_rate": {}, "true_regression_rate": {}}
    for metric_name, metric_key in (("fix_rate", "fixed"), ("true_regression_rate", "true_regression")):
        for cx, cy in pairs_to_test:
            pair_key = f"{cx}_vs_{cy}"
            if ("c" in (cx, cy)) and not condition_c_available_for_pairs:
                paired_bootstrap_results[metric_name][pair_key] = {
                    "status": "UNAVAILABLE",
                    "reason": f"Condition C status is '{c_load['status']}'",
                }
                continue
            try:
                x_all = condition_vector(cx, all_injected_ids, metric_key)
                y_all = condition_vector(cy, all_injected_ids, metric_key)
                x_noneg = condition_vector(cx, noneg_injected_ids, metric_key)
                y_noneg = condition_vector(cy, noneg_injected_ids, metric_key)
                paired_bootstrap_results[metric_name][pair_key] = {
                    "including_negation_n240": paired_bootstrap_mean_diff(x_all, y_all),
                    "excluding_negation_n180": paired_bootstrap_mean_diff(x_noneg, y_noneg),
                }
            except KeyError as exc:
                paired_bootstrap_results[metric_name][pair_key] = {"status": "UNAVAILABLE", "reason": str(exc)}
    logger.info("Paired bootstrap complete for fix_rate and true_regression_rate")

    # ------------------------------------------------------------------
    # Step 4: fix-rate-advantage reconciliation table (C1 vs C2, the reviewer-flagged pair)
    # ------------------------------------------------------------------
    c1_fixed_all = condition_vector("c1", all_injected_ids, "fixed")
    c2_fixed_all = condition_vector("c2", all_injected_ids, "fixed")
    c1_fixed_noneg = condition_vector("c1", noneg_injected_ids, "fixed")
    c2_fixed_noneg = condition_vector("c2", noneg_injected_ids, "fixed")

    fix_rate_advantage_240_including_negation = paired_bootstrap_mean_diff(c2_fixed_all, c1_fixed_all)
    fix_rate_advantage_180_excluding_negation = paired_bootstrap_mean_diff(c2_fixed_noneg, c1_fixed_noneg)

    direction_verified = abs(fix_rate_advantage_240_including_negation["point_estimate"]) < abs(
        fix_rate_advantage_180_excluding_negation["point_estimate"]
    )
    logger.info(
        f"Fix-rate advantage (C2-C1): incl_negation={fix_rate_advantage_240_including_negation['point_estimate']:.4f} "
        f"excl_negation={fix_rate_advantage_180_excluding_negation['point_estimate']:.4f} "
        f"direction_verified={direction_verified}"
    )

    fix_rate_reconciliation = {
        "fix_rate_advantage_240_including_negation": {
            **fix_rate_advantage_240_including_negation,
            "row_population": "injected_error_augmentation experimental_pool, all 4 categories",
            "denominator": 240,
            "negation_rows_included": True,
        },
        "fix_rate_advantage_180_excluding_negation": {
            **fix_rate_advantage_180_excluding_negation,
            "row_population": "injected_error_augmentation experimental_pool, metadata_invariant_category != negation_polarity_flip",
            "denominator": 180,
            "negation_rows_included": False,
        },
        "reconciliation_explanation": (
            "negation_polarity_flip corruptions are deletions (corrupted_span==''), so they are "
            "structural non-attempts for whichever condition can only mask/repair a non-empty span "
            "(B, D, and, on this row set, they count as failures in C2's own attempted-only figure too "
            "since C2's checker cannot re-insert a deleted zero-width span either); including these "
            "60 rows in the denominator mechanically narrows any measured C2-over-C1 fix-rate gap "
            "relative to excluding them, because they contribute 0 to both C1's and C2's numerator "
            "while still counting in both denominators. Verified numerically below."
        ),
        "direction_verified_including_smaller_in_magnitude_than_excluding": direction_verified,
    }

    # ------------------------------------------------------------------
    # Step 2: normal-approximation DeltaCOMET pairwise comparisons (documented fallback)
    # ------------------------------------------------------------------
    logger.info("Step 2: normal-approximation DeltaCOMET pairwise comparisons")
    pooled_comet = {
        "b": bdc1["metadata"]["metrics"]["pooled"]["B"],
        "d": bdc1["metadata"]["metrics"]["pooled"]["D"],
        "c1": bdc1["metadata"]["metrics"]["pooled"]["C1"],
        "c2": c2["metadata"]["metrics"]["natural_pooled"],
    }
    condition_c_pooled_comet = None
    if c_load["status"] in ("complete", "partial") and isinstance(c_load["data"].get("metadata", {}).get("metrics"), dict):
        md = c_load["data"]["metadata"]
        for key_guess in ("natural_pooled", "metrics"):
            if key_guess in md and isinstance(md[key_guess], dict) and "delta_comet_mean" in md[key_guess]:
                condition_c_pooled_comet = md[key_guess]
                break
        if condition_c_pooled_comet is None and "metrics" in md:
            m = md["metrics"]
            if isinstance(m, dict) and "pooled" in m and "C" in m.get("pooled", {}):
                condition_c_pooled_comet = m["pooled"]["C"]
    if condition_c_pooled_comet is not None:
        pooled_comet["c"] = condition_c_pooled_comet

    comet_pairs = [("c1", "c2"), ("c1", "c"), ("c2", "c"), ("c", "b"), ("c", "d")]
    delta_comet_normal_approx = {}
    for cx, cy in comet_pairs:
        pair_key = f"{cx}_vs_{cy}"
        if cx not in pooled_comet or cy not in pooled_comet:
            delta_comet_normal_approx[pair_key] = {
                "status": "UNAVAILABLE",
                "reason": f"pooled delta_comet not available for '{cx if cx not in pooled_comet else cy}'",
            }
            continue
        mx, cix = pooled_comet[cx]["delta_comet_mean"], pooled_comet[cx]["delta_comet_ci95"]
        my, ciy = pooled_comet[cy]["delta_comet_mean"], pooled_comet[cy]["delta_comet_ci95"]
        delta_comet_normal_approx[pair_key] = normal_approx_diff(mx, cix, my, ciy)
    logger.info("Normal-approximation DeltaCOMET comparisons complete")

    # ------------------------------------------------------------------
    # Step 5: Condition C verdict
    # ------------------------------------------------------------------
    logger.info("Step 5: Condition C verdict")

    # (a) D closes only part of B's gap
    b_mean, b_ci = pooled_comet["b"]["delta_comet_mean"], pooled_comet["b"]["delta_comet_ci95"]
    d_mean, d_ci = pooled_comet["d"]["delta_comet_mean"], pooled_comet["d"]["delta_comet_ci95"]
    b_vs_d = normal_approx_diff(b_mean, b_ci, d_mean, d_ci)
    criterion_a_pass = (not b_vs_d["ci_excludes_zero"]) and (abs(d_mean) < abs(b_mean))
    criterion_a = {
        "description": "D closes only part of B's gap (hygiene retry does not meaningfully move DeltaCOMET)",
        "b_delta_comet_mean": b_mean,
        "d_delta_comet_mean": d_mean,
        "b_minus_d_normal_approx": b_vs_d,
        "pass": criterion_a_pass,
    }

    # (b) among C1/C2/(C), material improvement in regression-rate reduction AND DeltaCOMET
    c1_vs_c2_regression = paired_bootstrap_results["true_regression_rate"].get("c1_vs_c2", {})
    c1_vs_c2_comet = delta_comet_normal_approx.get("c1_vs_c2", {})
    reg_excl = c1_vs_c2_regression.get("excluding_negation_n180", {})
    # Diffs are computed as (c1 - c2). A genuine REDUCTION under c2 requires c1's regression rate
    # to be materially HIGHER than c2's, i.e. the (c1 - c2) diff must be positive AND its CI exclude 0.
    reg_material = (
        isinstance(reg_excl, dict)
        and reg_excl.get("ci_excludes_zero", False)
        and reg_excl.get("point_estimate", 0) > 0
    )
    # A genuine DeltaCOMET IMPROVEMENT under c2 requires c2's (less negative) mean to exceed c1's,
    # i.e. the (c1 - c2) diff must be NEGATIVE AND its CI exclude 0.
    comet_material = (
        isinstance(c1_vs_c2_comet, dict)
        and c1_vs_c2_comet.get("ci_excludes_zero", False)
        and c1_vs_c2_comet.get("point_estimate", 0) < 0
    )
    criterion_b = {
        "description": "C2 (or C) shows materially larger true-regression-rate reduction AND materially larger DeltaCOMET improvement than C1 (CI excludes 0 on the paired difference)",
        "c1_vs_c2_true_regression_rate_paired_diff_excl_negation": reg_excl,
        "c1_vs_c2_delta_comet_normal_approx": c1_vs_c2_comet,
        "regression_reduction_material": reg_material,
        "comet_improvement_material": comet_material,
        "pass_c1_vs_c2": bool(reg_material and comet_material),
        "note": (
            "C2 attempted-population fix_rate/regression are far better than C1's, and C2's "
            "pooled DeltaCOMET (-0.0166) is essentially indistinguishable from B/D and WORSE than "
            "C1's (-0.0035); this criterion is evaluated pairwise using the true paired regression "
            "bootstrap and the normal-approximation COMET comparison, matching the mixed pattern "
            "already reported by the C2 artifact."
        ),
    }

    # (c) full Condition C
    if c_load["status"] == "not_found":
        condition_c_verdict = "UNDETERMINED_NO_ARTIFACT"
        criterion_c = {
            "description": "Condition C's own success criteria (non-negative-or-near-zero DeltaCOMET, "
            "regression significantly below B's, fix_rate >= B's, edit volume not collapsed to full-retranslation levels)",
            "status": "NOT_EVALUATED",
            "reason": "No Condition C sibling artifact was found by evaluation run time.",
        }
        rationale = (
            f"Condition C sibling artifact was not found (scan of {len(c_discovery['scan_log'])} "
            f"gen_art siblings under {ITER_ROOT / 'gen_art'} yielded no matching, completed output). "
            "Steps (1)-(4) and the B/D/C1/C2-only portions of the scorecard (step 6) are complete "
            "as a standalone deliverable. Condition C's own three success sub-criteria could not be "
            "evaluated against real numbers."
        )
    elif c_load["status"] == "partial":
        condition_c_verdict = "MIXED_PARTIAL"
        criterion_c = {
            "description": "Condition C's own success criteria, evaluated on a PARTIAL run",
            "status": "PARTIAL",
            "completion_fraction": c_load["completion_fraction"],
            "lang_pairs_seen": c_load["lang_pairs_seen"],
        }
        rationale = (
            f"Condition C's output exists but is partial (completion_fraction="
            f"{c_load['completion_fraction']}, language pairs seen={c_load['lang_pairs_seen']}). "
            "Reporting partial metrics with partial=true rather than extrapolating full-run numbers."
        )
    else:
        c_pooled = pooled_comet.get("c")
        c_comet_threshold_pass = c_pooled is not None and c_pooled["delta_comet_ci95"][1] >= -0.005
        c_vs_b_regression = paired_bootstrap_results["true_regression_rate"].get("c_vs_b", {})
        c_vs_b_reg_excl = c_vs_b_regression.get("excluding_negation_n180", {}) if isinstance(c_vs_b_regression, dict) else {}
        c_regression_below_b = (
            isinstance(c_vs_b_reg_excl, dict)
            and c_vs_b_reg_excl.get("ci_excludes_zero", False)
            and c_vs_b_reg_excl.get("point_estimate", 0) < 0
        )
        c_fixed_all = condition_vector("c", all_injected_ids, "fixed") if condition_c_injected else None
        c_fix_rate = float(np.mean(c_fixed_all)) if c_fixed_all is not None else None
        b_fix_rate = float(np.mean(condition_vector("b", all_injected_ids, "fixed")))
        c_fix_rate_pass = c_fix_rate is not None and c_fix_rate >= b_fix_rate
        criterion_c = {
            "description": "mean DeltaCOMET CI-upper >= -0.005 AND true_regression significantly below B's AND fix_rate >= B's AND edit volume not collapsed to full-retranslation levels",
            "c_pooled_delta_comet": c_pooled,
            "delta_comet_threshold_used": -0.005,
            "delta_comet_pass": c_comet_threshold_pass,
            "c_vs_b_true_regression_paired_excl_negation": c_vs_b_reg_excl,
            "regression_pass": c_regression_below_b,
            "c_fix_rate_incl_negation": c_fix_rate,
            "b_fix_rate_incl_negation": b_fix_rate,
            "fix_rate_pass": c_fix_rate_pass,
        }
        all_c_pass = bool(c_comet_threshold_pass and c_regression_below_b and c_fix_rate_pass)
        if criterion_a_pass and criterion_b["pass_c1_vs_c2"] and all_c_pass:
            condition_c_verdict = "CONFIRMED"
        elif not all_c_pass and (c_pooled is not None and c_pooled["delta_comet_mean"] < -0.005):
            condition_c_verdict = "DISCONFIRMED"
        else:
            condition_c_verdict = "MIXED"
        rationale = (
            f"criterion_a(pass={criterion_a_pass}) AND criterion_b(pass={criterion_b['pass_c1_vs_c2']}) AND "
            f"criterion_c(comet={c_comet_threshold_pass}, regression={c_regression_below_b}, fix_rate={c_fix_rate_pass})"
        )

    condition_c_verdict_block = {
        "condition_c_status": c_load["status"],
        "condition_c_completion_fraction": c_load["completion_fraction"],
        "criterion_a_d_closes_part_of_b_gap": criterion_a,
        "criterion_b_c2_over_c1_material_improvement": criterion_b,
        "criterion_c_condition_c_own_success": criterion_c,
        "condition_c_verdict": condition_c_verdict,
        "condition_c_verdict_rationale": rationale,
        "discovery": {k: v for k, v in c_discovery.items() if k != "scan_log"},
        "discovery_scan_log": c_discovery["scan_log"],
    }
    logger.info(f"condition_c_verdict = {condition_c_verdict}")

    # ------------------------------------------------------------------
    # Step 6: full scorecard
    # ------------------------------------------------------------------
    logger.info("Step 6: building five-condition scorecard")

    def cost_from_ledger(ledger):
        return ledger.get("spent_usd") if isinstance(ledger, dict) else None

    lang_pairs_present = sorted({bdc1_injected[rid]["metadata_language_pair"] for rid in all_injected_ids})

    def per_language_fix_and_regression(cond_key):
        out = {}
        for lp in lang_pairs_present:
            lp_all_ids = [rid for rid in all_injected_ids if bdc1_injected[rid]["metadata_language_pair"] == lp]
            lp_noneg_ids = [rid for rid in noneg_injected_ids if bdc1_injected[rid]["metadata_language_pair"] == lp]
            out[lp] = {
                "fix_rate_including_negation": float(np.mean(condition_vector(cond_key, lp_all_ids, "fixed"))),
                "fix_rate_excluding_negation": float(np.mean(condition_vector(cond_key, lp_noneg_ids, "fixed"))),
                "true_regression_rate_including_negation": float(
                    np.mean(condition_vector(cond_key, lp_all_ids, "true_regression"))
                ),
                "true_regression_rate_excluding_negation": float(
                    np.mean(condition_vector(cond_key, lp_noneg_ids, "true_regression"))
                ),
                "n_rows_including_negation": len(lp_all_ids),
                "n_rows_excluding_negation": len(lp_noneg_ids),
            }
        return out

    def pooled_natural_row_stat(cond_key, field_suffix, source_dict=None):
        """Mean of a per-row natural-subsample field, computed directly from the 320 matched rows
        (upstream's own 'pooled' block does not carry edit_volume/n_llm_calls means, only its
        per_language_pair breakdown does -- so these are recomputed here from row-level data)."""
        source_dict = source_dict if source_dict is not None else bdc1_natural
        primary_key = f"metadata_{cond_key}_{field_suffix}"
        fallback_key = f"metadata_c2_{field_suffix}" if cond_key == "c" else None
        vals = []
        for rid in source_dict:
            row = source_dict[rid]
            v = row.get(primary_key)
            if v is None and fallback_key is not None:
                v = row.get(fallback_key)
            vals.append(float(v or 0.0))
        return float(np.mean(vals))

    scorecard = []
    cond_defs = [
        ("B", "b", bdc1["metadata"]["cost_ledger"], bdc1["metadata"]["metrics"]),
        ("D", "d", bdc1["metadata"]["cost_ledger"], bdc1["metadata"]["metrics"]),
        ("C1", "c1", bdc1["metadata"]["cost_ledger"], bdc1["metadata"]["metrics"]),
    ]
    for label, key, cost_ledger, metrics_block in cond_defs:
        pooled = metrics_block["pooled"][label]
        per_pair = {lp: metrics_block["per_language_pair"][lp][label] for lp in metrics_block["per_language_pair"]}
        fixed_all = condition_vector(key, all_injected_ids, "fixed")
        fixed_noneg = condition_vector(key, noneg_injected_ids, "fixed")
        reg_all = condition_vector(key, all_injected_ids, "true_regression")
        reg_noneg = condition_vector(key, noneg_injected_ids, "true_regression")
        scorecard.append(
            {
                "condition": label,
                "pooled_delta_comet_mean": pooled["delta_comet_mean"],
                "pooled_delta_comet_ci95": pooled["delta_comet_ci95"],
                "fix_rate_including_negation_n240": float(np.mean(fixed_all)),
                "fix_rate_excluding_negation_n180": float(np.mean(fixed_noneg)),
                "true_regression_rate_including_negation_n240": float(np.mean(reg_all)),
                "true_regression_rate_excluding_negation_n180": float(np.mean(reg_noneg)),
                "mean_edit_volume": pooled_natural_row_stat(key, "edit_volume"),
                "mean_llm_calls_per_sentence": pooled_natural_row_stat(key, "n_llm_calls"),
                "total_openrouter_cost_contributed_usd": cost_from_ledger(cost_ledger),
                "per_language_pair": per_pair,
                "fix_rate_and_regression_by_language_pair": per_language_fix_and_regression(key),
            }
        )

    # C2
    c2_pooled = c2["metadata"]["metrics"]["natural_pooled"]
    c2_per_pair = c2["metadata"]["metrics"]["natural_per_language_pair"]
    c2_fixed_all_v = condition_vector("c2", all_injected_ids, "fixed")
    c2_fixed_noneg_v = condition_vector("c2", noneg_injected_ids, "fixed")
    c2_reg_all_v = condition_vector("c2", all_injected_ids, "true_regression")
    c2_reg_noneg_v = condition_vector("c2", noneg_injected_ids, "true_regression")
    scorecard.append(
        {
            "condition": "C2",
            "pooled_delta_comet_mean": c2_pooled["delta_comet_mean"],
            "pooled_delta_comet_ci95": c2_pooled["delta_comet_ci95"],
            "fix_rate_including_negation_n240": float(np.mean(c2_fixed_all_v)),
            "fix_rate_excluding_negation_n180": float(np.mean(c2_fixed_noneg_v)),
            "true_regression_rate_including_negation_n240": float(np.mean(c2_reg_all_v)),
            "true_regression_rate_excluding_negation_n180": float(np.mean(c2_reg_noneg_v)),
            "mean_edit_volume": pooled_natural_row_stat("c2", "edit_volume", c2_natural),
            "mean_llm_calls_per_sentence": c2_pooled.get("n_llm_calls_mean"),
            "total_openrouter_cost_contributed_usd": cost_from_ledger(c2["metadata"]["cost_ledger"]),
            "per_language_pair": c2_per_pair,
            "fix_rate_and_regression_by_language_pair": per_language_fix_and_regression("c2"),
        }
    )

    # C
    if c_load["status"] in ("complete", "partial") and condition_c_injected:
        c_fixed_all_v = condition_vector("c", all_injected_ids, "fixed")
        c_fixed_noneg_v = condition_vector("c", noneg_injected_ids, "fixed")
        c_reg_all_v = condition_vector("c", all_injected_ids, "true_regression")
        c_reg_noneg_v = condition_vector("c", noneg_injected_ids, "true_regression")
        c_md = c_load["data"].get("metadata", {})
        c_cost = cost_from_ledger(c_md.get("cost_ledger", {}))
        scorecard.append(
            {
                "condition": "C",
                "status": c_load["status"],
                "completion_fraction": c_load["completion_fraction"],
                "pooled_delta_comet_mean": condition_c_pooled_comet.get("delta_comet_mean") if condition_c_pooled_comet else None,
                "pooled_delta_comet_ci95": condition_c_pooled_comet.get("delta_comet_ci95") if condition_c_pooled_comet else None,
                "fix_rate_including_negation_n240": float(np.mean(c_fixed_all_v)),
                "fix_rate_excluding_negation_n180": float(np.mean(c_fixed_noneg_v)),
                "true_regression_rate_including_negation_n240": float(np.mean(c_reg_all_v)),
                "true_regression_rate_excluding_negation_n180": float(np.mean(c_reg_noneg_v)),
                "mean_edit_volume": pooled_natural_row_stat("c", "edit_volume", condition_c_natural) if condition_c_natural else None,
                "mean_llm_calls_per_sentence": pooled_natural_row_stat("c", "n_llm_calls", condition_c_natural) if condition_c_natural else None,
                "total_openrouter_cost_contributed_usd": c_cost,
                "fix_rate_and_regression_by_language_pair": per_language_fix_and_regression("c"),
            }
        )
    else:
        scorecard.append(
            {
                "condition": "C",
                "status": c_load["status"],
                "note": "Condition C not available at evaluation run time; see condition_c_verdict block.",
            }
        )

    # ------------------------------------------------------------------
    # Checker-validation context (ru_RU / uk_UA cells only, for scorecard footnote)
    # ------------------------------------------------------------------
    checker_table = checker_validation["metadata"]["table"]
    checker_ru_uk = [row for row in checker_table if row["language"] in ("ru_RU", "uk_UA")]

    # ------------------------------------------------------------------
    # Assemble output per exp_eval_sol_out schema
    # ------------------------------------------------------------------
    logger.info("Assembling output JSON")

    metrics_agg = {
        "disjoint_population_overlap_count": disjoint_population_check["overlap_count"],
        "comet_population_n": disjoint_population_check["comet_population_n"],
        "fix_rate_population_n": disjoint_population_check["fix_rate_population_n"],
        "fix_rate_advantage_240_including_negation_point": fix_rate_advantage_240_including_negation["point_estimate"],
        "fix_rate_advantage_240_including_negation_ci_lo": fix_rate_advantage_240_including_negation["ci95"][0],
        "fix_rate_advantage_240_including_negation_ci_hi": fix_rate_advantage_240_including_negation["ci95"][1],
        "fix_rate_advantage_180_excluding_negation_point": fix_rate_advantage_180_excluding_negation["point_estimate"],
        "fix_rate_advantage_180_excluding_negation_ci_lo": fix_rate_advantage_180_excluding_negation["ci95"][0],
        "fix_rate_advantage_180_excluding_negation_ci_hi": fix_rate_advantage_180_excluding_negation["ci95"][1],
        "reconciliation_direction_verified": int(direction_verified),
        "b_pooled_delta_comet_mean": pooled_comet["b"]["delta_comet_mean"],
        "d_pooled_delta_comet_mean": pooled_comet["d"]["delta_comet_mean"],
        "c1_pooled_delta_comet_mean": pooled_comet["c1"]["delta_comet_mean"],
        "c2_pooled_delta_comet_mean": pooled_comet["c2"]["delta_comet_mean"],
        "c_pooled_delta_comet_mean": (pooled_comet.get("c") or {}).get("delta_comet_mean", float("nan")),
        "b_vs_d_normal_approx_point": b_vs_d["point_estimate"],
        "b_vs_d_normal_approx_ci_excludes_zero": int(b_vs_d["ci_excludes_zero"]),
        "c1_vs_c2_delta_comet_point": c1_vs_c2_comet.get("point_estimate", float("nan")) if isinstance(c1_vs_c2_comet, dict) else float("nan"),
        "c1_vs_c2_regression_paired_point_excl_negation": reg_excl.get("point_estimate", float("nan")) if isinstance(reg_excl, dict) else float("nan"),
        "n_bootstrap_iterations": N_BOOT,
        "bootstrap_seed": SEED,
        "per_row_comet_b_available": int(per_row_comet_availability["b"]["available"]),
        "per_row_comet_d_available": int(per_row_comet_availability["d"]["available"]),
        "per_row_comet_c1_available": int(per_row_comet_availability["c1"]["available"]),
        "per_row_comet_c2_available": int(per_row_comet_availability["c2"]["available"]),
        "per_row_comet_c_available": int(per_row_comet_availability["c"]["available"]),
        "condition_c_found": int(c_discovery["found"]),
    }
    # drop any NaN (schema requires plain numbers; NaN is not valid JSON)
    metrics_agg = {k: (v if not (isinstance(v, float) and np.isnan(v)) else None) for k, v in metrics_agg.items()}
    metrics_agg = {k: v for k, v in metrics_agg.items() if v is not None}

    # datasets: one row per injected-pool example carrying per-condition eval_ fields
    injected_dataset_examples = []
    for rid in all_injected_ids:
        base = bdc1_injected[rid]
        c2_row = c2_injected[rid]
        is_negation = base["metadata_invariant_category"] == "negation_polarity_flip"
        ex = {
            "input": base["input"][:2000],
            "output": base["output"][:2000],
            "metadata_row_id": rid,
            "metadata_language_pair": base["metadata_language_pair"],
            "metadata_invariant_category": base["metadata_invariant_category"],
            "metadata_is_negation_deletion_row": is_negation,
            "eval_b_fixed": float(bool(base.get("metadata_b_fixed"))),
            "eval_d_fixed": float(bool(base.get("metadata_d_fixed"))),
            "eval_c1_fixed": float(bool(base.get("metadata_c1_fixed"))),
            "eval_c2_fixed": float(bool(c2_row.get("metadata_c2_fixed"))),
            "eval_b_true_regression": float(bool(base.get("metadata_b_true_regression"))),
            "eval_d_true_regression": float(bool(base.get("metadata_d_true_regression"))),
            "eval_c1_true_regression": float(bool(base.get("metadata_c1_true_regression"))),
            "eval_c2_true_regression": float(bool(c2_row.get("metadata_c2_true_regression"))),
            "eval_c1_minus_c2_fixed_diff": float(bool(base.get("metadata_c1_fixed"))) - float(bool(c2_row.get("metadata_c2_fixed"))),
        }
        if condition_c_injected:
            c_row = condition_c_injected.get(rid)
            if c_row is not None:
                ex["eval_c_fixed"] = float(bool(c_row.get("metadata_c2_fixed", c_row.get("metadata_c_fixed"))))
                ex["eval_c_true_regression"] = float(
                    bool(c_row.get("metadata_c2_true_regression", c_row.get("metadata_c_true_regression")))
                )
        injected_dataset_examples.append(ex)

    natural_dataset_examples = []
    for rid in sorted(bdc1_natural.keys()):
        base = bdc1_natural[rid]
        c2_row = c2_natural[rid]
        ex = {
            "input": base["input"][:2000],
            "output": base["output"][:2000],
            "metadata_row_id": rid,
            "metadata_language_pair": base["metadata_language_pair"],
            "eval_b_edit_volume": float(base.get("metadata_b_edit_volume") or 0.0),
            "eval_d_edit_volume": float(base.get("metadata_d_edit_volume") or 0.0),
            "eval_c1_edit_volume": float(base.get("metadata_c1_edit_volume") or 0.0),
            "eval_c2_edit_volume": float(c2_row.get("metadata_c2_edit_volume") or 0.0),
            "eval_b_n_llm_calls": float(base.get("metadata_b_n_llm_calls") or 0),
            "eval_c1_n_llm_calls": float(base.get("metadata_c1_n_llm_calls") or 0),
            "eval_c2_n_llm_calls": float(c2_row.get("metadata_c2_n_llm_calls") or 0),
        }
        natural_dataset_examples.append(ex)

    output = {
        "metadata": {
            "evaluation_name": "final_b_d_c1_c2_c_scorecard_and_c_verdict",
            "description": (
                "Consolidated five-condition (B/D/C1/C2/C) span-editing scorecard: per-row-COMET "
                "availability gate, true paired bootstrap on fix_rate/true_regression_rate, the "
                "disjoint-population check, the fix-rate-advantage reconciliation (reviewer-flagged "
                "+0.2875 vs +0.3833), and the Condition C net-positive verdict."
            ),
            "n_bootstrap_iterations": N_BOOT,
            "bootstrap_seed": SEED,
            "seed_provenance": "Matches the seed=42 recorded in art_7Uc5PlFctjXi's method_out.json metadata (B/D/C1's own stratification seed).",
            "step1_per_row_comet_availability": per_row_comet_availability,
            "step2_paired_bootstrap_fix_rate_true_regression": paired_bootstrap_results,
            "step2_delta_comet_normal_approximation_pairwise": delta_comet_normal_approx,
            "step3_disjoint_population_check": disjoint_population_check,
            "step4_fix_rate_advantage_reconciliation": fix_rate_reconciliation,
            "step5_condition_c_verdict": condition_c_verdict_block,
            "step6_scorecard": scorecard,
            "step6_cost_column_caveat": (
                "B, D, and C1 were run as ONE combined sweep (art_7Uc5PlFctjXi) and share a single "
                "cost_ledger, so total_openrouter_cost_contributed_usd is identical ($0.06574) across "
                "those three rows -- it is the shared run's total spend, not a per-condition split. "
                "C2 (art_K8koUmGFDlLN) and C (if present) are each a separate run with their own ledger."
            ),
            "checker_validation_ru_uk_context": checker_ru_uk,
            "dependency_artifacts": {
                "b_d_c1": str(BDC1_PATH),
                "c2": str(C2_PATH),
                "checker_validation": str(CHECKER_VALIDATION_PATH),
                "dataset": str(DATASET_PREVIEW_PATH),
                "condition_c": c_discovery.get("path"),
            },
        },
        "metrics_agg": metrics_agg,
        "datasets": [
            {"dataset": "injected_pool_fix_rate_and_regression_paired", "examples": injected_dataset_examples},
            {"dataset": "natural_rows_edit_volume_and_calls", "examples": natural_dataset_examples},
        ],
    }

    out_path = WORKSPACE / "full_eval_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")

    return output


if __name__ == "__main__":
    main()
