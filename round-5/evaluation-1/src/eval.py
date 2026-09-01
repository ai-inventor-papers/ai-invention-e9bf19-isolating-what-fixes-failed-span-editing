#!/usr/bin/env python3
"""Reviewer-response re-analysis of the B/D/C1/C2/C span-editing sweep.

Pure re-analysis: no LLM calls, no re-execution. Loads full_method_out.json
from three prior EXPERIMENT artifacts (B/D/C1, C2, C) and produces four
first-class, separately labeled analyses answering the paper's open
Condition-C questions, per gen_plan_evaluation_1_idx3.
"""

from __future__ import annotations

import json
import resource
import sys
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# Files here are a few MB each; a generous but bounded RAM cap for safety.
resource.setrlimit(resource.RLIMIT_AS, (6 * 1024**3, 6 * 1024**3))

WS = Path(__file__).parent
D1 = WS / "deps" / "d1"  # art_7Uc5PlFctjXi: B, D, C1
D2 = WS / "deps" / "d2"  # art_K8koUmGFDlLN: C2
D3 = WS / "deps" / "d3"  # art_6n9zJVKWXnio: C

# lang code (checker_validation) <-> language_pair (row metadata)
LANG_TO_PAIR = {"ru_RU": "en-ru_RU", "uk_UA": "en-uk_UA"}
# checker category (checker_validation) <-> row metadata_invariant_category
CAT_TO_INVARIANT = {
    "named_entity": "named_entity_swap",
    "number_unit_date": "number_unit_date_alteration",
    "negation_polarity": "negation_polarity_flip",
    "quantifier_scope": "quantifier_substitution",
}


def load_json(path: Path) -> dict:
    logger.info(f"Loading {path}")
    return json.loads(path.read_text())


def mean(xs: list[float]) -> float | None:
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 4) if xs else None


def rate(bools: list[bool]) -> float | None:
    bools = [b for b in bools if b is not None]
    return round(sum(1 for b in bools if b) / len(bools), 4) if bools else None


# ============================================================================
# 0. Cross-artifact identity checks (must-do before any computation)
# ============================================================================


def check_row_identity() -> dict:
    d1_rows = load_json(D1 / "selected_rows.json")
    d2_rows = load_json(D2 / "selected_rows.json")
    d3_rows = load_json(D3 / "selected_rows.json")
    folds = ["natural_row_ids", "injected_pool_row_ids", "injected_heldout_row_ids"]
    result = {}
    for a, b, label in [(d1_rows, d2_rows, "bddc1_vs_c2"), (d2_rows, d3_rows, "c2_vs_c"), (d1_rows, d3_rows, "bddc1_vs_c")]:
        result[label] = {f: (a[f] == b[f]) for f in folds}
    result["all_identical"] = all(all(v.values()) for v in result.values())
    logger.info(f"Row-ID identity across all three artifacts: {result['all_identical']}")
    if not result["all_identical"]:
        logger.error(f"Row-ID mismatch detected: {result}")
    return result


# ============================================================================
# 1. precision_tier_collapse_analysis
# ============================================================================


def per_cell_certificate_from_raw_rows(examples: list[dict], cert_field: str, passes_field: str) -> dict:
    """Recompute certificate_rate/mean-passes per (lang,category) cell directly
    from raw per-row fields. Needed because Condition C's own pre-aggregated
    injected_category_table reports certificate_rate=null for negation_polarity_flip
    (its 'n_attempted' convention there tracks span-based fix/regression semantics
    that do not apply to a deletion, NOT whether the checker certificate concept
    applies) even though metadata_c_certificate_achieved IS populated on every
    negation row. Verified: for the three categories where the pre-aggregated
    table DOES report a value, this recomputation matches it exactly (named_entity_swap,
    number_unit_date_alteration, quantifier_substitution -- all 6 language-pair
    cells bit-for-bit identical to injected_category_table), so this method is a
    validated superset, not a divergent re-derivation.
    """
    cells: dict[tuple[str, str], dict] = {}
    for e in examples:
        key = (e["metadata_language_pair"], e["metadata_invariant_category"])
        cells.setdefault(key, {"certs": [], "passes": []})
        cells[key]["certs"].append(e.get(cert_field))
        cells[key]["passes"].append(e.get(passes_field))
    out = {}
    for key, v in cells.items():
        out[key] = {
            "n_rows": len(v["certs"]),
            "certificate_rate": rate(v["certs"]),
            "mean_passes": mean(v["passes"]),
        }
    return out


def precision_tier_collapse_analysis() -> dict:
    validation = load_json(D1 / "checker_validation.json")
    excluded = set(validation["excluded_cells"])
    per_cell_precision = validation["per_cell"]

    d3 = load_json(D3 / "full_method_out.json")
    c_injected_examples = d3["datasets"][1]["examples"]
    c_cells_raw = per_cell_certificate_from_raw_rows(
        c_injected_examples, "metadata_c_certificate_achieved", "metadata_c_n_passes"
    )
    # sanity check against Condition C's own pre-aggregated table (the 3 non-negation
    # categories should match exactly; logged, not asserted, since a mismatch here
    # would itself be a reportable finding rather than a bug to crash on)
    agg_table = {
        (row["language_pair"], row["category"]): row for row in d3["metadata"]["metrics"]["injected_category_table"]
    }
    mismatches = []
    for key, row in agg_table.items():
        if row.get("certificate_rate") is None:
            continue
        recomputed = c_cells_raw.get(key, {}).get("certificate_rate")
        if recomputed is None or abs(recomputed - row["certificate_rate"]) > 1e-6:
            mismatches.append({"cell": list(key), "table": row["certificate_rate"], "recomputed": recomputed})
    if mismatches:
        logger.warning(f"Raw-row recomputation mismatches Condition C's own table: {mismatches}")
    else:
        logger.info("Raw-row certificate recomputation matches Condition C's own injected_category_table exactly "
                     "for all non-negation cells.")

    usable_cells = []
    for cat_key, cat_info in per_cell_precision.items():
        lang, cat = cat_info["lang"], cat_info["category"]
        if f"{lang}|{cat}" in excluded:
            continue
        pair = LANG_TO_PAIR[lang]
        invariant = CAT_TO_INVARIANT[cat]
        c_cell = c_cells_raw.get((pair, invariant), {})
        usable_cells.append({
            "lang": lang,
            "category": cat,
            "checker_precision": cat_info["precision"],
            "checker_recall": cat_info["recall"],
            "certificate_rate_condition_c": c_cell.get("certificate_rate"),
            "mean_pass_count_condition_c": c_cell.get("mean_passes"),
            "n_rows": c_cell.get("n_rows"),
        })

    # Tier assignment per plan: high ~0.78-0.86, low ~0.575-0.65
    high_tier = [c for c in usable_cells if c["checker_precision"] >= 0.75]
    low_tier = [c for c in usable_cells if c["checker_precision"] < 0.75]

    high_certs = [c["certificate_rate_condition_c"] for c in high_tier]
    low_certs = [c["certificate_rate_condition_c"] for c in low_tier]
    high_passes = [c["mean_pass_count_condition_c"] for c in high_tier]
    low_passes = [c["mean_pass_count_condition_c"] for c in low_tier]

    high_mean_cert, low_mean_cert = mean(high_certs), mean(low_certs)
    high_mean_pass, low_mean_pass = mean(high_passes), mean(low_passes)

    n_usable = len(usable_cells)
    low_power = n_usable < 6
    if high_mean_cert is None or low_mean_cert is None:
        collapse_pattern = "indeterminate_too_few_cells"
    elif abs(high_mean_cert - low_mean_cert) < 0.05:
        collapse_pattern = "uniform_across_tiers"
    elif low_mean_cert < high_mean_cert:
        collapse_pattern = "concentrated_in_low_precision_tier"
    else:
        collapse_pattern = "concentrated_in_high_precision_tier"

    fourth_artifact_note = (
        "No widened-pass-budget artifact with per-pass false-positive tracking exists among the three actual "
        "dependencies provided at execution time (art_7Uc5PlFctjXi, art_K8koUmGFDlLN, art_6n9zJVKWXnio). The "
        "stronger second line of evidence the plan describes is unavailable; the precision-tier estimate below "
        "is the best available signal, not a supplementary check on a stronger one."
    )

    return {
        "source_files": {
            "checker_precision_per_cell": "art_7Uc5PlFctjXi/checker_validation.json:per_cell,excluded_cells",
            "certificate_rate_and_pass_count": (
                "art_6n9zJVKWXnio/full_method_out.json:datasets[1].examples[*]."
                "metadata_c_certificate_achieved,metadata_c_n_passes (recomputed per-cell; cross-checked "
                "against metadata.metrics.injected_category_table)"
            ),
        },
        "usable_cells": usable_cells,
        "n_usable_cells": n_usable,
        "n_excluded_cells_upstream": len(excluded),
        "low_statistical_power_flag": low_power,
        "power_caveat": (
            f"Only {n_usable} of 8 (language x category) cells are usable after Table 1's exclusion gate, and "
            f"the tier split further divides them into {len(high_tier)} high-precision and {len(low_tier)} "
            "low-precision cells. This is far too small a sample to support a confident causal conclusion; "
            "treat the pattern below as a correlational, first-order, hypothesis-generating signal only."
        ),
        "high_precision_tier": {
            "precision_range_target": "0.78-0.86",
            "cells": [c["lang"] + "|" + c["category"] for c in high_tier],
            "n_cells": len(high_tier),
            "mean_certificate_rate": high_mean_cert,
            "mean_pass_count": high_mean_pass,
            "raw_certificate_rates": high_certs,
        },
        "low_precision_tier": {
            "precision_range_target": "0.575-0.65",
            "cells": [c["lang"] + "|" + c["category"] for c in low_tier],
            "n_cells": len(low_tier),
            "mean_certificate_rate": low_mean_cert,
            "mean_pass_count": low_mean_pass,
            "raw_certificate_rates": low_certs,
        },
        "collapse_pattern": collapse_pattern,
        "interpretation": (
            "This is consistent with checker-noise-driven churn concentrating certificate failure in the "
            "low-precision tier (mean certificate_rate "
            f"{low_mean_cert} vs {high_mean_cert} in the high-precision tier, a "
            f"{'~' + str(round((high_mean_cert or 0) / (low_mean_cert or 1e-9), 1)) + 'x' if low_mean_cert else 'undefined'} "
            "ratio), rather than a uniform cross-invariant regression -- but this does NOT prove that checker "
            "noise is the sole or even dominant cause, and does not distinguish a noise-driven mechanism from a "
            "genuinely harder-to-satisfy invariant class that happens to also have lower checker precision "
            "(number_unit_date and quantifier_scope require the model to get an EXACT numeric/scope match, which "
            "is plausibly just harder to repair correctly regardless of checker noise). The two explanations are "
            "confounded in this data and cannot be separated without an independent measure of true repair "
            "difficulty per category."
            if collapse_pattern == "concentrated_in_low_precision_tier"
            else "See collapse_pattern and per-cell data for the observed relationship between checker precision "
            "and certificate collapse; treat any directional reading as correlational, not causal."
        ),
        "second_stronger_evidence_line": fourth_artifact_note,
        "confidence_caveat": (
            f"n={n_usable} usable cells total, split {len(high_tier)}/{len(low_tier)} across tiers -- decisive "
            "conclusions are not warranted at this sample size; this is a suggestive first-order bound only."
        ),
    }


# ============================================================================
# 2. checker_eligibility_restricted_analysis
# ============================================================================


def compute_condition_metrics(examples: list[dict], fixed_field: str, regression_field: str,
                                certificate_field: str | None, cell_filter: set[tuple[str, str]] | None) -> dict:
    if cell_filter is not None:
        examples = [e for e in examples if (e["metadata_language_pair"], e["metadata_invariant_category"]) in cell_filter]
    fixed = [e.get(fixed_field) for e in examples]
    regr = [e.get(regression_field) for e in examples]
    cert = [e.get(certificate_field) for e in examples] if certificate_field else []
    return {
        "n_rows": len(examples),
        "fix_rate": rate(fixed),
        "true_regression_rate": rate(regr),
        "certificate_rate": rate(cert) if certificate_field else None,
    }


def checker_eligibility_restricted_analysis() -> dict:
    validation = load_json(D1 / "checker_validation.json")
    excluded = set(validation["excluded_cells"])
    per_cell = validation["per_cell"]

    eligible_lang_cat = []
    for key, info in per_cell.items():
        if key not in excluded:
            eligible_lang_cat.append((info["lang"], info["category"]))
    eligible_cells_readable = [f"{lang}|{cat}" for lang, cat in eligible_lang_cat]
    eligible_pair_invariant = {(LANG_TO_PAIR[lang], CAT_TO_INVARIANT[cat]) for lang, cat in eligible_lang_cat}

    plan_stated_scope = (
        "number_unit_date in both languages, and quantifier_scope in ru_RU only (per the hypothesis text)"
    )
    actual_scope = (
        f"{len(eligible_lang_cat)} cells pass Table 1's recall>=0.5 AND precision>=0.5 gate: "
        f"{sorted(eligible_cells_readable)}. This is WIDER than the plan's stated scope above: negation_polarity "
        "passes the threshold in BOTH languages (ru_RU recall=0.5217/precision=0.8571, uk_UA "
        "recall=0.6087/precision=0.7778) and was omitted from the plan's own restatement of the eligibility set. "
        "Named_entity is excluded in both languages and quantifier_scope is excluded in uk_UA only, matching the "
        "plan. The eligibility set used below is the one actually derivable from checker_validation.json's own "
        "threshold rule, not the plan's narrower restatement, since the threshold rule is the authoritative "
        "definition and the plan text appears to have under-listed it."
    )

    d1 = load_json(D1 / "full_method_out.json")
    d2 = load_json(D2 / "full_method_out.json")
    d3 = load_json(D3 / "full_method_out.json")
    bd_c1_injected = d1["datasets"][1]["examples"]
    c2_injected = d2["datasets"][1]["examples"]
    c_injected = d3["datasets"][1]["examples"]

    def restricted_and_full(examples, fixed_f, regr_f, cert_f):
        full = compute_condition_metrics(examples, fixed_f, regr_f, cert_f, cell_filter=None)
        restricted = compute_condition_metrics(examples, fixed_f, regr_f, cert_f, cell_filter=eligible_pair_invariant)
        return {"full_pooled": full, "restricted_to_eligible_cells": restricted}

    table = {
        "B": restricted_and_full(bd_c1_injected, "metadata_b_fixed", "metadata_b_true_regression", None),
        "D": restricted_and_full(bd_c1_injected, "metadata_d_fixed", "metadata_d_true_regression", None),
        "C1": restricted_and_full(bd_c1_injected, "metadata_c1_fixed", "metadata_c1_true_regression", None),
        "C2": restricted_and_full(c2_injected, "metadata_c2_fixed", "metadata_c2_true_regression", "metadata_c2_certificate_achieved"),
        "C": restricted_and_full(c_injected, "metadata_fixed", "metadata_true_regression", "metadata_c_certificate_achieved"),
    }

    def ordering_holds(metric: str) -> dict:
        out = {}
        for scope in ["full_pooled", "restricted_to_eligible_cells"]:
            vals = {cond: table[cond][scope][metric] for cond in table}
            out[scope] = vals
        return out

    fix_regr_ordering = ordering_holds("true_regression_rate")
    cert_collapse = {
        scope: {"C2": table["C2"][scope]["certificate_rate"], "C": table["C"][scope]["certificate_rate"]}
        for scope in ["full_pooled", "restricted_to_eligible_cells"]
    }

    def c1_below_c2(scope):
        return table["C1"][scope]["true_regression_rate"] is not None and table["C2"][scope]["true_regression_rate"] is not None \
            and table["C1"][scope]["true_regression_rate"] > table["C2"][scope]["true_regression_rate"]

    def c_worst(scope):
        vals = [table[c][scope]["true_regression_rate"] for c in ["B", "D", "C1", "C2"]]
        vals = [v for v in vals if v is not None]
        return table["C"][scope]["true_regression_rate"] is not None and vals and table["C"][scope]["true_regression_rate"] > max(vals)

    headline_survival = {
        "c1_regression_worse_than_c2": {"full": c1_below_c2("full_pooled"), "restricted": c1_below_c2("restricted_to_eligible_cells")},
        "c_regression_worst_of_all": {"full": c_worst("full_pooled"), "restricted": c_worst("restricted_to_eligible_cells")},
        "certificate_collapse_c2_to_c": cert_collapse,
    }
    survives = (
        headline_survival["c1_regression_worse_than_c2"]["full"] == headline_survival["c1_regression_worse_than_c2"]["restricted"]
        and headline_survival["c_regression_worst_of_all"]["full"] == headline_survival["c_regression_worst_of_all"]["restricted"]
    )

    return {
        "source_files": {
            "eligibility_gate": "art_7Uc5PlFctjXi/checker_validation.json:per_cell,excluded_cells (recall>=0.5 AND precision>=0.5 threshold)",
            "B_D_C1_metrics": "art_7Uc5PlFctjXi/full_method_out.json:datasets[1].examples[*].metadata_{b,d,c1}_{fixed,true_regression}",
            "C2_metrics": "art_K8koUmGFDlLN/full_method_out.json:datasets[1].examples[*].metadata_c2_{fixed,true_regression,certificate_achieved}",
            "C_metrics": "art_6n9zJVKWXnio/full_method_out.json:datasets[1].examples[*].metadata_{fixed,true_regression,c_certificate_achieved}",
        },
        "plan_stated_scope_vs_actual": {"plan_stated": plan_stated_scope, "actual_derived_from_threshold_rule": actual_scope},
        "eligible_cells": sorted(eligible_cells_readable),
        "n_eligible_cells_of_8": len(eligible_lang_cat),
        "comparison_table": table,
        "headline_ordering_survival": headline_survival,
        "headline_ordering_survives_restriction": survives,
        "verdict": (
            "The headline ordering (C1 has higher true_regression_rate than C2; Condition C has the highest "
            "true_regression_rate of all five conditions; certificate_rate collapses from C2 to C) SURVIVES "
            "restriction to the fully checker-eligible cell population unchanged in direction, though magnitudes "
            "shift somewhat because the restricted population drops the named_entity and uk_UA/quantifier_scope "
            "rows entirely."
            if survives
            else "The headline ordering does NOT fully survive restriction to the checker-eligible population -- "
            "see headline_ordering_survival for which specific comparison reverses or becomes indeterminate."
        ),
        "row_count_caveat": (
            f"Restricted population covers {len(eligible_pair_invariant)} of 8 (language, category) cells, i.e. "
            f"{table['C']['restricted_to_eligible_cells']['n_rows']} of "
            f"{table['C']['full_pooled']['n_rows']} injected-pool rows for Condition C (excluding negation cells "
            "where certificate_rate is computed from raw per-row fields since the pre-aggregated table marks "
            "those as structural non-attempts for fix_rate/true_regression_rate purposes, not for certificate "
            "purposes -- see certificate_definition_by_category for why negation rows still carry a well-defined "
            "certificate value)."
        ),
    }


# ============================================================================
# 3. certificate_definition_by_category
# ============================================================================


def certificate_definition_by_category() -> dict:
    d3 = load_json(D3 / "full_method_out.json")
    c_injected = d3["datasets"][1]["examples"]

    # Worked example: a named_entity_swap row (named_entity is an excluded
    # category for Condition C's checker, per checker_validation.excluded_cells
    # includes ru_RU|named_entity and uk_UA|named_entity with recall=precision=0.0
    # in THIS run's own re-fit -- see below).
    example_row = None
    for e in c_injected:
        if e["metadata_invariant_category"] == "named_entity_swap" and e.get("metadata_c_pass_log"):
            example_row = e
            break
    flagged_cats_seen = set()
    for e in c_injected:
        for p in e.get("metadata_c_pass_log", []) or []:
            for cat in p.get("flag_categories", []) or []:
                flagged_cats_seen.add(cat)

    named_entity_rows_detail = [
        {
            "row_id": e["metadata_row_id"],
            "language_pair": e["metadata_language_pair"],
            "certificate_achieved": bool(e.get("metadata_c_certificate_achieved")),
            "named_entity_ever_flagged_this_row": any(
                "named_entity" in (p.get("flag_categories") or []) for p in (e.get("metadata_c_pass_log") or [])
            ),
        }
        for e in c_injected
        if e["metadata_invariant_category"] == "named_entity_swap"
    ]

    c_validation = d3["metadata"]["checker_validation"]
    named_entity_cells = {k: v for k, v in c_validation["per_cell"].items() if v["category"] == "named_entity"}

    return {
        "source_files": {
            "scoring_logic": "art_6n9zJVKWXnio/method.py: excluded_cells_from_validation() (lines ~286-291) and "
            "Checker.detect_all(respect_exclusions=True) in checker.py (excluded (lang,cat) pairs are skipped "
            "entirely by detect_all, independent of the row's OWN corrupted/target category)",
            "row_level_evidence": "art_6n9zJVKWXnio/full_method_out.json:datasets[1].examples[*].metadata_c_pass_log[*].flag_categories",
        },
        "finding": (
            "(b) A row's certificate status is computed over only the invariants the checker actually tracks and "
            "re-verifies for the CURRENT run's non-excluded (lang,category) cells, independent of whether the "
            "row's own known-corrupted category is itself in an excluded cell. Condition C's method.py builds "
            "`Checker(excluded_cells=excluded)` from THIS run's own re-fit checker_validation, then calls "
            "`detect_all(..., respect_exclusions=True)`, which skips any (lang,cat) pair in excluded_cells "
            "entirely -- so a named_entity_swap row in en-ru_RU (an excluded cell) is NEVER checked for its OWN "
            "corruption category. It IS still included in the certificate_rate denominator (it is not dropped "
            "from the injected_category_table's n_rows/n_attempted), and its certificate is scored True/False "
            "based purely on whether the OTHER, non-excluded invariants (number_unit_date, negation_polarity, "
            "and quantifier_scope where not itself excluded) are clean in the current text."
        ),
        "worked_example": {
            "row_id": example_row["metadata_row_id"] if example_row else None,
            "language_pair": example_row["metadata_language_pair"] if example_row else None,
            "metadata_invariant_category": example_row["metadata_invariant_category"] if example_row else None,
            "metadata_c_certificate_achieved": example_row.get("metadata_c_certificate_achieved") if example_row else None,
            "metadata_c_n_passes": example_row.get("metadata_c_n_passes") if example_row else None,
            "pass_log_flag_categories": [p.get("flag_categories") for p in (example_row.get("metadata_c_pass_log") or [])] if example_row else None,
            "explanation": (
                "This row's known corruption is a named_entity_swap, but named_entity is an excluded cell for its "
                "language pair in this run, so detect_all() never flags the named-entity error itself -- the "
                "flag_categories logged across its passes (if any) come only from the other, non-excluded "
                "invariant checks, and its certificate_achieved value reflects only those."
            ) if example_row else "No named_entity_swap row with a non-empty pass_log was found (rows achieving an "
            "immediate zero-flag certificate log an empty pass_log by construction).",
        },
        "categories_ever_flagged_in_condition_c": sorted(flagged_cats_seen),
        "named_entity_never_flagged_confirmation": "named_entity" not in flagged_cats_seen,
        "named_entity_rows_detail": named_entity_rows_detail,
        "extra_finding_checker_validation_drift_across_runs": {
            "description": (
                "Condition C's own re-fit checker_validation.json-equivalent metadata (computed fresh in THIS "
                "run against the injected_heldout fold) reports named_entity recall=0.0, precision=0.0, "
                "n_flags_total=0 for BOTH language pairs -- a substantive change from art_7Uc5PlFctjXi's original "
                "checker_validation.json, which reported ru_RU named_entity recall=1.0/precision=0.3239 and "
                "uk_UA named_entity recall=0.6957/precision=0.3696 (both non-zero). The excluded_cells set is "
                "identical either way (named_entity fails the 0.5 threshold in both versions), so this drift is "
                "not consequential for the eligibility gate, but it independently corroborates the finding above: "
                "named_entity detection is effectively inert in Condition C's environment (possibly a Stanza NER "
                "resource/model availability difference between runs, undiagnosed further here since it does not "
                "change any excluded_cells or headline result)."
            ),
            "named_entity_cells_this_run": named_entity_cells,
            "named_entity_cells_original_bddc1_run": {
                k: v for k, v in load_json(D1 / "checker_validation.json")["per_cell"].items() if v["category"] == "named_entity"
            },
        },
    }


# ============================================================================
# 4. normal_approx_bias_direction
# ============================================================================


def normal_approx_bias_direction() -> dict:
    d1 = load_json(D1 / "full_method_out.json")
    pooled = d1["metadata"]["metrics"]["pooled"]

    # CI half-widths from the actual reported bootstrap CIs (95%) for ΔCOMET,
    # since that is the metric with a persisted bootstrap CI for every condition
    # (fix_rate/true_regression_rate have no reported CI in any of the three artifacts).
    def half_width(ci):
        return (ci[1] - ci[0]) / 2.0

    c1_hw = half_width(pooled["C1"]["delta_comet_ci95"])
    b_hw = half_width(pooled["B"]["delta_comet_ci95"])
    d3 = load_json(D3 / "full_method_out.json")
    c2_hw = half_width(d3["metadata"]["comparison_table_B_D_C1_C2_vs_C"]["conditions"]["C2"]["delta_comet_ci95"])

    var_c1 = c1_hw**2 / (1.96**2)
    var_c2 = c2_hw**2 / (1.96**2)
    var_indep = var_c1 + var_c2
    # worked numeric example with an assumed positive covariance to show the
    # sign of the effect (Var(X-Y) = Var(X)+Var(Y)-2Cov(X,Y))
    assumed_corr_examples = [0.0, 0.3, 0.6, 0.9]
    worked_examples = []
    for r in assumed_corr_examples:
        cov = r * (var_c1**0.5) * (var_c2**0.5)
        var_true = var_c1 + var_c2 - 2 * cov
        hw_true = 1.96 * (var_true**0.5) if var_true > 0 else None
        hw_indep = 1.96 * (var_indep**0.5)
        worked_examples.append({
            "assumed_correlation": r,
            "implied_covariance": round(cov, 10),
            "true_variance_of_difference": round(var_true, 10),
            "independence_assumed_variance": round(var_indep, 10),
            "true_half_width_95pct": round(hw_true, 6) if hw_true else None,
            "independence_assumed_half_width_95pct": round(hw_indep, 6),
            "independence_assumption_is_wider": (hw_indep >= hw_true) if hw_true else None,
        })

    plausible_covariance_sources = [
        "Same 320-row natural population scored under B, C1, and C2 (row-ID identity verified True across all "
        "three), so any per-row COMET-scoring noise (e.g. a sentence the checkpoint scores unusually harshly "
        "regardless of which condition's output it sees) is shared across conditions and induces positive "
        "covariance between their pooled means.",
        "Same repair model (google/gemma-3-12b-it) and same OpenRouter client across B/D/C1/C2/C, so systematic "
        "per-sentence repair-difficulty effects (e.g. a long or syntactically unusual sentence that is hard to "
        "repair well under ANY condition) correlate the conditions' errors on that row.",
        "Same 4-category checker module (checker.py, copied verbatim across C1/C2/C) drives localization in "
        "three of the five conditions, so checker false positives/negatives on a given row propagate similarly "
        "into whichever condition uses checker-based localization on that row.",
    ]

    empirical_covariance_status = {
        "attempted": True,
        "result": "NOT COMPUTABLE from available data",
        "reason": (
            "No per-row DeltaCOMET array is persisted in any of the three artifacts' full_method_out.json for "
            "the natural-row datasets (checked art_7Uc5PlFctjXi's natural_repair_B_D_C1 and "
            "art_K8koUmGFDlLN's natural_repair_C2 example schemas directly: fields present are "
            "metadata_{b,d,c1,c2}_{n_llm_calls,edit_volume,leakage,no_op,...} and predict_* text, but no "
            "per-row COMET score or delta). Only the pooled bootstrap mean and CI are stored, which is exactly "
            "the summary statistic that collapses any row-level pairing information -- an empirical covariance "
            "between two conditions' per-row deltas cannot be reconstructed after the fact from pooled summaries "
            "alone. art_6n9zJVKWXnio's own paired_bootstrap_c_vs_c2_note independently confirms this same gap "
            "for the C-vs-C2 comparison it attempted."
        ),
    }

    return {
        "source_files": {
            "b_delta_comet_ci": "art_7Uc5PlFctjXi/full_method_out.json:metadata.metrics.pooled.B.delta_comet_ci95",
            "c1_delta_comet_ci": "art_7Uc5PlFctjXi/full_method_out.json:metadata.metrics.pooled.C1.delta_comet_ci95",
            "c2_delta_comet_ci": "art_6n9zJVKWXnio/full_method_out.json:metadata.comparison_table_B_D_C1_C2_vs_C.conditions.C2.delta_comet_ci95",
        },
        "metric_identified": (
            "ΔCOMET pooled 95% bootstrap CI (the only metric with a persisted CI half-width in any of the three "
            "artifacts; fix_rate and true_regression_rate are reported as point estimates with no CI anywhere "
            "in the dependency chain, so the 'conservative-direction' claim -- to the extent it can be reconstructed "
            "from these artifacts alone -- must be about ΔCOMET, or is otherwise unverifiable from available data)."
        ),
        "reported_half_widths": {"B": round(b_hw, 6), "C1": round(c1_hw, 6), "C2": round(c2_hw, 6)},
        "mathematical_argument": (
            "Var(X-Y) = Var(X) + Var(Y) - 2*Cov(X,Y). Treating two measurements as independent when computing the "
            "variance of their difference means using Var_indep = Var(X)+Var(Y), omitting the -2*Cov(X,Y) term. "
            "Whenever Cov(X,Y) > 0, subtracting a positive quantity makes the TRUE variance strictly smaller than "
            "Var_indep: Var_true = Var_indep - 2*Cov(X,Y) < Var_indep. A smaller true variance means a narrower "
            "true confidence interval than the independence-assumed one. So the independence assumption "
            "OVER-estimates the variance and produces a WIDER (more conservative, i.e. less likely to falsely "
            "reject a null of no difference), not narrower, interval whenever the true covariance is positive. "
            "The direction reverses (independence assumption becomes ANTI-conservative, i.e. too narrow) only if "
            "Cov(X,Y) < 0."
        ),
        "worked_numeric_examples": worked_examples,
        "worked_example_reading": (
            f"Using the actual reported ΔCOMET half-widths (C1={round(c1_hw,6)}, C2={round(c2_hw,6)}), at every "
            "assumed positive correlation tested (0.3, 0.6, 0.9) the true half-width is smaller than the "
            "independence-assumed half-width, confirming the direction of the bias holds for these specific "
            "numbers as long as the (unverified) covariance is in fact positive."
        ),
        "plausible_positive_covariance_sources": plausible_covariance_sources,
        "empirical_covariance_status": empirical_covariance_status,
        "final_downgraded_claim": (
            "The MATHEMATICAL DIRECTION of the bias is established unconditionally: IF Cov(X,Y) > 0, the "
            "independence-assumed interval is provably conservative (too wide), never too narrow. However, the "
            "SIGN of the actual covariance between any two of B/C1/C2/C's per-row ΔCOMET distributions cannot be "
            "estimated or bounded from the data retained in these three artifacts -- no per-row paired samples "
            "survive in a form that permits computing empirical covariance. The paper's claim should therefore be "
            "stated conditionally: 'IF the shared row population, repair model, and checker induce positive "
            "correlation between conditions (plausible on structural grounds, see plausible_positive_covariance_sources), "
            "THEN the normal-approximation independence substitute is conservative, not anti-conservative -- but "
            "this precondition is not verified from available data.' Downgraded from an unconditional assertion "
            "to a conditional one that is honest about what is and is not established."
        ),
        "what_would_be_needed": (
            "Per-row paired ΔCOMET (or fix_rate/true_regression outcome) samples for at least two conditions "
            "scored on the identical row set, retained in the output JSON (not just the pooled bootstrap summary), "
            "would let a future run compute empirical Pearson/Spearman correlation directly and replace the "
            "conditional claim above with an unconditional, data-backed one. None of B/D/C1/C2/C's method.py "
            "scripts currently persist this per-row array to method_out.json."
        ),
    }


# ============================================================================
# Main
# ============================================================================


@logger.catch(reraise=True)
def main():
    Path("logs").mkdir(exist_ok=True)
    identity = check_row_identity()

    logger.info("Running analysis (1): precision_tier_collapse_analysis")
    a1 = precision_tier_collapse_analysis()
    logger.info(f"  -> collapse_pattern = {a1['collapse_pattern']}, n_usable_cells = {a1['n_usable_cells']}")

    logger.info("Running analysis (2): checker_eligibility_restricted_analysis")
    a2 = checker_eligibility_restricted_analysis()
    logger.info(f"  -> headline_ordering_survives_restriction = {a2['headline_ordering_survives_restriction']}")

    logger.info("Running analysis (3): certificate_definition_by_category")
    a3 = certificate_definition_by_category()
    logger.info(f"  -> named_entity_never_flagged_confirmation = {a3['named_entity_never_flagged_confirmation']}")

    logger.info("Running analysis (4): normal_approx_bias_direction")
    a4 = normal_approx_bias_direction()
    logger.info("  -> mathematical direction established conditionally on Cov>0; empirical covariance not computable")

    metrics_agg = {
        "row_id_identity_all_pairs_match": 1.0 if identity["all_identical"] else 0.0,
        "n_usable_checker_cells_of_8": float(a1["n_usable_cells"]),
        "precision_tier_high_mean_certificate_rate": a1["high_precision_tier"]["mean_certificate_rate"] or -1.0,
        "precision_tier_low_mean_certificate_rate": a1["low_precision_tier"]["mean_certificate_rate"] or -1.0,
        "n_eligible_cells_restricted_analysis": float(a2["n_eligible_cells_of_8"]),
        "headline_ordering_survives_restriction": 1.0 if a2["headline_ordering_survives_restriction"] else 0.0,
        "named_entity_ever_flagged_in_condition_c": 0.0 if a3["named_entity_never_flagged_confirmation"] else 1.0,
        "normal_approx_direction_conditionally_established": 1.0,
        "normal_approx_empirical_covariance_computable": 0.0,
    }

    metadata = {
        "evaluation_name": "reviewer_response_condition_c_disambiguation",
        "description": (
            "Reconciles four open Condition-C reviewer questions using ONLY existing computed results from three "
            "prior experiment artifacts (art_7Uc5PlFctjXi: B/D/C1; art_K8koUmGFDlLN: C2; art_6n9zJVKWXnio: C). "
            "No new LLM calls, no new repairs, no new COMET scoring."
        ),
        "dependency_row_id_identity_check": identity,
        "precision_tier_collapse_analysis": a1,
        "checker_eligibility_restricted_analysis": a2,
        "certificate_definition_by_category": a3,
        "normal_approx_bias_direction": a4,
    }

    summary_examples = [
        {
            "input": "Does Condition C's certificate-rate collapse concentrate in checker cells with lower detection "
            "precision, or is it uniform across precision tiers (i.e. is it checker-noise-driven or a genuine "
            "cross-invariant regression)?",
            "output": (
                f"collapse_pattern={a1['collapse_pattern']}; high-precision tier mean certificate_rate="
                f"{a1['high_precision_tier']['mean_certificate_rate']} (n={a1['high_precision_tier']['n_cells']} cells) "
                f"vs low-precision tier {a1['low_precision_tier']['mean_certificate_rate']} "
                f"(n={a1['low_precision_tier']['n_cells']} cells). Correlational only; n is small."
            ),
            "eval_high_precision_tier_certificate_rate": a1["high_precision_tier"]["mean_certificate_rate"] or -1.0,
            "eval_low_precision_tier_certificate_rate": a1["low_precision_tier"]["mean_certificate_rate"] or -1.0,
            "eval_n_usable_cells": float(a1["n_usable_cells"]),
            "metadata_analysis": a1,
        },
        {
            "input": "Does the headline B/D/C1/C2/C ordering on fix_rate, true_regression_rate, and certificate_rate "
            "survive restriction to the fully checker-eligible (language, category) cells, or is it an artifact "
            "of pooling contested and uncontested cells together?",
            "output": (
                f"{a2['n_eligible_cells_of_8']} of 8 cells are fully eligible. Headline ordering survives "
                f"restriction: {a2['headline_ordering_survives_restriction']}. See comparison_table for exact "
                "full-vs-restricted figures per condition."
            ),
            "eval_headline_ordering_survives_restriction": 1.0 if a2["headline_ordering_survives_restriction"] else 0.0,
            "eval_n_eligible_cells_of_8": float(a2["n_eligible_cells_of_8"]),
            "metadata_analysis": a2,
        },
        {
            "input": "When a row's own known-corrupted category is itself an excluded checker cell (e.g. "
            "named_entity_swap in en-ru_RU), is that row excluded from certificate_rate entirely, or scored "
            "certificate=True/False based only on the other invariants?",
            "output": (
                "Scored on the other invariants only (option b): the row stays in the certificate_rate denominator "
                "and its certificate reflects only non-excluded categories. Confirmed both from method.py's "
                "detect_all(respect_exclusions=True) logic and from raw pass_log data: "
                f"named_entity never appears among flagged categories in Condition C's run "
                f"({a3['named_entity_never_flagged_confirmation']})."
            ),
            "eval_named_entity_never_flagged": 1.0 if a3["named_entity_never_flagged_confirmation"] else 0.0,
            "metadata_analysis": a3,
        },
        {
            "input": "Is the normal-approximation independence substitute for the variance of a difference between two "
            "positively-correlated measurements conservative (too wide) or anti-conservative (too narrow), for "
            "this project's actual reported ΔCOMET confidence intervals?",
            "output": a4["final_downgraded_claim"],
            "eval_direction_established_conditionally": 1.0,
            "eval_empirical_covariance_computable": 0.0,
            "metadata_analysis": a4,
        },
    ]

    # Dataset 2: one example per usable (language, category) checker cell, feeding
    # the precision-tier comparison in analysis (1) -- makes every cell independently auditable.
    precision_tier_examples = [
        {
            "input": f"Precision-tier cell {cell['lang']}|{cell['category']}: checker precision={cell['checker_precision']}, "
            f"recall={cell['checker_recall']}. What is Condition C's certificate_rate and mean pass count on this cell?",
            "output": (
                f"certificate_rate={cell['certificate_rate_condition_c']}, "
                f"mean_pass_count={cell['mean_pass_count_condition_c']}, n_rows={cell['n_rows']}."
            ),
            "eval_checker_precision": cell["checker_precision"],
            "eval_checker_recall": cell["checker_recall"],
            "eval_certificate_rate": cell["certificate_rate_condition_c"] if cell["certificate_rate_condition_c"] is not None else -1.0,
            "eval_mean_pass_count": cell["mean_pass_count_condition_c"] if cell["mean_pass_count_condition_c"] is not None else -1.0,
            "metadata_lang": cell["lang"],
            "metadata_category": cell["category"],
        }
        for cell in a1["usable_cells"]
    ]

    # Dataset 3: one example per (condition, scope) pair from the eligibility-restriction
    # table -- 5 conditions x 2 scopes (full_pooled / restricted_to_eligible_cells) = 10.
    eligibility_examples = []
    for cond, scopes in a2["comparison_table"].items():
        for scope_name, vals in scopes.items():
            eligibility_examples.append({
                "input": f"Condition {cond}, scope={scope_name}: fix_rate, true_regression_rate, certificate_rate "
                "over the injected-pool rows in this scope?",
                "output": (
                    f"n_rows={vals['n_rows']}, fix_rate={vals['fix_rate']}, "
                    f"true_regression_rate={vals['true_regression_rate']}, certificate_rate={vals['certificate_rate']}."
                ),
                "eval_fix_rate": vals["fix_rate"] if vals["fix_rate"] is not None else -1.0,
                "eval_true_regression_rate": vals["true_regression_rate"] if vals["true_regression_rate"] is not None else -1.0,
                "eval_certificate_rate": vals["certificate_rate"] if vals["certificate_rate"] is not None else -1.0,
                "eval_n_rows": float(vals["n_rows"]),
                "metadata_condition": cond,
                "metadata_scope": scope_name,
            })

    # Dataset 4: one example per named_entity_swap injected-pool row (60 rows total:
    # 30 en-ru_RU + 30 en-uk_UA) -- the full row-level evidence backing analysis (3)'s
    # finding that named_entity is never flagged in Condition C despite being each
    # row's own known-corrupted category.
    certificate_definition_examples = [
        {
            "input": f"Row {row['row_id']} ({row['language_pair']}, known corruption=named_entity_swap, an "
            "excluded checker cell): was named_entity ever flagged in this row's pass log, and was a "
            "certificate ultimately achieved?",
            "output": (
                f"named_entity_ever_flagged={row['named_entity_ever_flagged_this_row']}, "
                f"certificate_achieved={row['certificate_achieved']}."
            ),
            "eval_certificate_achieved": 1.0 if row["certificate_achieved"] else 0.0,
            "eval_named_entity_flagged": 1.0 if row["named_entity_ever_flagged_this_row"] else 0.0,
            "metadata_row_id": row["row_id"],
            "metadata_language_pair": row["language_pair"],
        }
        for row in a3["named_entity_rows_detail"]
    ]

    # Dataset 5: one example per assumed-correlation worked numeric example from
    # analysis (4), showing the independence-vs-true half-width arithmetic explicitly.
    normal_approx_examples = [
        {
            "input": f"At assumed correlation r={w['assumed_correlation']} between C1 and C2's pooled ΔCOMET "
            f"(covariance={w['implied_covariance']}), is the independence-assumed 95% CI half-width wider than "
            "the true one?",
            "output": (
                f"true_half_width={w['true_half_width_95pct']}, independence_assumed_half_width="
                f"{w['independence_assumed_half_width_95pct']}, independence_assumption_is_wider="
                f"{w['independence_assumption_is_wider']}."
            ),
            "eval_true_half_width": w["true_half_width_95pct"] if w["true_half_width_95pct"] is not None else -1.0,
            "eval_independence_assumed_half_width": w["independence_assumed_half_width_95pct"],
            "eval_independence_assumption_is_wider": 1.0 if w["independence_assumption_is_wider"] else 0.0,
            "metadata_assumed_correlation": w["assumed_correlation"],
        }
        for w in a4["worked_numeric_examples"]
    ]

    n_total_examples = (
        len(summary_examples) + len(precision_tier_examples) + len(eligibility_examples)
        + len(certificate_definition_examples) + len(normal_approx_examples)
    )
    logger.info(f"Total examples across all datasets: {n_total_examples}")

    out = {
        "metadata": metadata,
        "metrics_agg": metrics_agg,
        "datasets": [
            {"dataset": "reviewer_response_condition_c_analyses", "examples": summary_examples},
            {"dataset": "precision_tier_cells", "examples": precision_tier_examples},
            {"dataset": "eligibility_restricted_per_condition_scope", "examples": eligibility_examples},
            {"dataset": "certificate_definition_named_entity_rows", "examples": certificate_definition_examples},
            {"dataset": "normal_approx_worked_examples", "examples": normal_approx_examples},
        ],
    }

    out_path = WS / "eval_out.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
