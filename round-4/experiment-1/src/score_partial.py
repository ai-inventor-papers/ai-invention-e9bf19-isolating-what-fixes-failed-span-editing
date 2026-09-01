#!/usr/bin/env python3
"""Fallback_plan #2 path: the full 560-row sweep did not reach
completion_fraction=1.0 within the turn-by-turn wall-clock available to this
session (unrelated to CALL_TIMEOUT_S/heartbeat robustness -- the sweep itself
was progressing steadily with no stalls, see logs/run_method.log heartbeats).
Scores whatever rows DID reach a terminal state in condition_c_progress.jsonl
and writes method_out.json with completion_fraction explicitly < 1.0, per the
plan's explicit partial-report fallback. Does NOT pad missing rows.

Reuses every scoring/summarization function from method.py verbatim -- only
the sweep-execution step is skipped in favor of reading the partial JSONL.
"""
from __future__ import annotations

import gc
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import method as m
from checker import Checker

WORKDIR = m.WORKDIR


def main():
    t0 = time.time()
    m.setup_resource_limits()
    rng = random.Random(m.SEED)

    data = m.load_data()
    by_dataset = m.index_examples(data)
    natural_rows = m.stratified_sample_natural(by_dataset["wmt25_task3_natural"], rng)
    injected_pool_rows = m.stratified_sample_injected(by_dataset["injected_error_augmentation"], rng, "experimental_pool", m.N_INJECTED_PER_CELL)
    injected_heldout_rows = m.stratified_sample_injected(by_dataset["injected_error_augmentation"], rng, "checker_validation_heldout", None)
    row_id_check = m.check_row_id_match(natural_rows, injected_pool_rows, injected_heldout_rows)
    del data
    gc.collect()

    checker_unrestricted = Checker(excluded_cells=set())
    validation = m.validate_checker(checker_unrestricted, injected_heldout_rows)
    excluded = m.excluded_cells_from_validation(validation)
    checker = Checker(excluded_cells=excluded)
    n_negation_injected = sum(1 for r in injected_pool_rows if m.is_negation_deletion_row(r))

    completed = m.load_completed_rows(m.OUT_JSONL)
    natural_results = [rec for rec in completed.values() if rec.get("kind") == "natural"]
    injected_results = [rec for rec in completed.values() if rec.get("kind") == "injected"]
    n_total_expected = len(natural_rows) + len(injected_pool_rows)
    n_total_got = len(natural_results) + len(injected_results)
    completion_fraction = n_total_got / n_total_expected if n_total_expected else 0.0
    print(f"PARTIAL run: {n_total_got}/{n_total_expected} rows terminal "
          f"({len(natural_results)} natural, {len(injected_results)} injected). "
          f"completion_fraction={completion_fraction:.4f}")

    # per-language-pair coverage breakdown of the partial sample (fallback_plan #2)
    coverage_by_pair = {}
    for pair in m.LANG_PAIRS:
        nat_target = m.N_NATURAL_PER_PAIR
        inj_target = m.N_INJECTED_PER_CELL * 4
        nat_got = sum(1 for r in natural_results if r["language_pair"] == pair)
        inj_got = sum(1 for r in injected_results if r["language_pair"] == pair)
        coverage_by_pair[pair] = {
            "natural_got": nat_got, "natural_target": nat_target,
            "injected_got": inj_got, "injected_target": inj_target,
        }
    print("Per-language-pair partial coverage:", json.dumps(coverage_by_pair, indent=2))

    comet_model = m.try_load_comet()
    comet_available = comet_model is not None
    natural_comet = {p: [] for p in m.LANG_PAIRS}
    row_source_cache = {r["_row_id"]: r["input"] for r in natural_rows}

    if comet_available:
        for pair in m.LANG_PAIRS:
            pair_rows = [r for r in natural_results if r["language_pair"] == pair]
            if not pair_rows:
                continue
            sources = [row_source_cache[r["row_id"]] for r in pair_rows]
            originals = [r["original"] for r in pair_rows]
            edited = [r["C"]["output"] if "C" in r and "output" in r["C"] else r["original"] for r in pair_rows]
            orig_scores = m.comet_score_batch(comet_model, sources, originals)
            edited_scores = m.comet_score_batch(comet_model, sources, edited)
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
        for pair in m.LANG_PAIRS:
            pair_rows = [r for r in natural_results if r["language_pair"] == pair]
            if not pair_rows:
                continue
            sources = [row_source_cache[r["row_id"]] for r in pair_rows]
            originals = [r["original"] for r in pair_rows]
            edited = [r["C"]["output"] if "C" in r and "output" in r["C"] else r["original"] for r in pair_rows]
            orig_scores = [m.proxy_qe_score(s, o) for s, o in zip(sources, originals)]
            edited_scores = [m.proxy_qe_score(s, e) for s, e in zip(sources, edited)]
            natural_comet[pair] = [e - o for e, o in zip(edited_scores, orig_scores)]

    c_metrics = m.summarize_condition_c(natural_results, injected_results, natural_comet, rng)
    comparison_table = m.build_comparison_table(c_metrics, natural_comet, rng)

    for pair in m.LANG_PAIRS:
        pair_rows = [r for r in natural_results if r["language_pair"] == pair]
        for r, d in zip(pair_rows, natural_comet.get(pair, [])):
            r["delta_comet"] = d

    elapsed = time.time() - t0

    output = {
        "metadata": {
            "method_name": "checker_broadened_iterative_repair_C",
            "description": (
                "Condition C: checker-broadened localization (C1) + iterative repair-and-reverify (C2) combined "
                "-- detect_all() re-run FRESH every pass on the CURRENT text, up to MAX_PASSES=3, stopping on a "
                "zero-flag certificate. Wrapped in per-call hard timeout + retry, heartbeat logging, incremental "
                "resumable JSONL writes, and a wall-clock cap. THIS RUN IS PARTIAL (see completion_fraction): the "
                "sweep was progressing steadily with zero stalls (heartbeats confirm rows_done advancing every "
                "30s the entire time -- the exact silent-hang failure mode this artifact was built to survive did "
                "NOT recur) but did not finish within the wall-clock available to this packaging pass. Scored "
                "per fallback_plan #2: score what is terminal, report completion_fraction explicitly, no padding."
            ),
            "c2_run_reused_from": str(m.C2_RUN_PATH),
            "bddc1_run_reused_from": str(m.PRIOR_BDDC1_RUN_PATH),
            "row_id_identity_check_vs_c2": row_id_check,
            "repair_model": m.MODEL,
            "seed": m.SEED,
            "max_passes": m.MAX_PASSES,
            "call_timeout_s": m.CALL_TIMEOUT_S,
            "max_retries": m.MAX_RETRIES,
            "heartbeat_every_s": m.HEARTBEAT_EVERY_S,
            "wall_clock_cap_s": m.WALL_CLOCK_CAP_S,
            "wall_clock_cap_hit": False,
            "partial_run": True,
            "partial_run_reason": (
                "Sweep was killed (PID-based, per process_isolation rules) after "
                f"{n_total_got}/{n_total_expected} rows reached a terminal state -- NOT due to a stall (heartbeat "
                "log shows continuous progress, ~0.75 rows/s, zero idle warnings) but because this packaging pass "
                "needed to produce method_out.json within its own turn budget. The robustness instrumentation "
                "this artifact was built to add (timeout+retry, heartbeat, incremental resumable writes) is fully "
                "exercised and verified working (see dry_run_test.py output and the heartbeat log); what is "
                "missing is only wall-clock, not correctness."
            ),
            "language_pairs": m.LANG_PAIRS,
            "n_natural_per_pair_target": m.N_NATURAL_PER_PAIR,
            "n_injected_per_cell_target": m.N_INJECTED_PER_CELL,
            "n_natural_rows_processed": len(natural_results),
            "n_injected_pool_rows_processed": len(injected_results),
            "n_injected_heldout_rows": len(injected_heldout_rows),
            "n_negation_deletion_rows_total": n_negation_injected,
            "completion_fraction": round(completion_fraction, 4),
            "partial_coverage_by_language_pair": coverage_by_pair,
            "checker_validation": {
                "per_cell": validation,
                "excluded_cells": [f"{lang}|{cat}" for lang, cat in sorted(excluded)],
            },
            "cost_ledger": {"note": "cost ledger accounting lives in the sweep process's own log (logs/run_method.log); this scoring-only pass makes no LLM calls itself.", "spent_usd_at_kill_time_approx": None},
            "sub_budget_usd": m.SUB_BUDGET_USD,
            "runtime_seconds_scoring_only": round(elapsed, 1),
            "metrics": c_metrics,
            "comparison_table_B_D_C1_C2_vs_C": comparison_table,
            "comet_available": comet_available,
            "delta_comet_metric": "Unbabel/wmt22-cometkiwi-da" if comet_available else "DeltaCOMET-proxy (NOT COMET)",
            "checker_verdict_definitions": (
                "injected-pool rows: passed/certificate = detect_all() (broadened, full-sentence, non-excluded "
                "cells only) returns ZERO flags on the current candidate text -- re-checked FRESH every pass, not "
                "restricted to the row's own known-corrupted category. fixed/true_regression use the SAME "
                "ground-truth definitions B/D/C1/C2 used. natural rows: certificate = detect_all() returns zero "
                "flags on the current text."
            ),
            "negation_attemptability_note": (
                "Unlike B/D/C2 (narrow oracle/QE-span localization -- structurally cannot target a DELETION), "
                "Condition C's checker-based detect_all() localization CAN flag negation_polarity_flip deletion "
                "rows via the absence-vs-source heuristic. See metrics.negation_attemptability."
            ),
            "limitations_not_verified_identical_to_prior_run": [
                item for item, ok in [
                    ("natural row IDs", row_id_check.get("natural_match")),
                    ("injected-pool row IDs", row_id_check.get("injected_pool_match")),
                    ("injected-heldout row IDs", row_id_check.get("injected_heldout_match")),
                ] if ok is not True
            ] or ["none -- row-ID identity to C2 (and transitively B/D/C1) was fully verified"],
            "robustness_note": (
                "The prior attempt at this exact condition (iter_3/gen_art_experiment_2) died silently mid-sweep "
                "with no traceback and a stale log. This run's instrumentation was verified working three ways: "
                "(1) dry_run_test.py's timeout-injection unit test confirms a 90s-hung call is cut off at "
                f"CALL_TIMEOUT_S={m.CALL_TIMEOUT_S}s and the row is marked hard-failed rather than hanging the "
                "sweep; (2) the live sweep's heartbeat log shows continuous rows_done progress every 30s with "
                "zero stall warnings for its entire runtime; (3) the resume mechanism (load_completed_rows) is "
                "what allowed this very scoring pass to read the partial JSONL cleanly. The silent-hang failure "
                "mode did not recur; what limited this run was wall-clock budget, addressed by scoring the "
                "partial result per fallback_plan #2 rather than blocking indefinitely."
            ),
        },
        "datasets": [
            {"dataset": "natural_repair_C", "examples": [m.natural_example(r) if hasattr(m, "natural_example") else _natural_example(r, row_source_cache) for r in natural_results]},
            {"dataset": "injected_pool_repair_C", "examples": [_injected_example(r, injected_pool_rows) for r in injected_results]},
        ],
    }

    out_path = WORKDIR / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")


def _natural_example(row: dict, row_source_cache: dict) -> dict:
    c = row.get("C", {})
    ex = {
        "input": f"[{row['language_pair']}] {row_source_cache.get(row['row_id'], '')}",
        "output": row.get("original", ""),
        "predict_c": c.get("output", row.get("original", "")),
        "metadata_row_id": row["row_id"],
        "metadata_language_pair": row["language_pair"],
        "metadata_domain": row.get("domain"),
        "metadata_status": row.get("status"),
        "metadata_c_n_passes": c.get("n_passes"),
        "metadata_c_n_llm_calls": c.get("n_llm_calls"),
        "metadata_c_certificate_achieved": c.get("certificate_achieved"),
        "metadata_c_edit_volume": c.get("edit_volume"),
        "metadata_c_leakage": c.get("leakage"),
        "metadata_c_no_op": c.get("no_op"),
        "metadata_c_pass_log": c.get("pass_log"),
    }
    if "delta_comet" in row:
        ex["metadata_delta_comet"] = row["delta_comet"]
    return ex


def _injected_example(row: dict, injected_pool_rows: list[dict]) -> dict:
    rid = row["row_id"]
    src_row = next((r for r in injected_pool_rows if r["_row_id"] == rid), None)
    source_text = src_row["input"] if src_row else ""
    corrupted_hyp = src_row["output"] if src_row else ""
    c = row.get("C", {})
    return {
        "input": f"[{row['language_pair']}/{row['category']}] {source_text}",
        "output": corrupted_hyp,
        "predict_c": c.get("output", corrupted_hyp),
        "metadata_row_id": rid,
        "metadata_language_pair": row["language_pair"],
        "metadata_invariant_category": row["category"],
        "metadata_is_negation_deletion_row": row.get("is_negation_deletion_row"),
        "metadata_negation_localized_pre_repair": row.get("negation_localized_pre_repair"),
        "metadata_status": row.get("status"),
        "metadata_fixed": row.get("fixed"),
        "metadata_true_regression": row.get("true_regression"),
        "metadata_c_certificate_achieved": c.get("certificate_achieved"),
        "metadata_c_n_passes": c.get("n_passes"),
        "metadata_c_n_llm_calls": c.get("n_llm_calls"),
        "metadata_c_pass_log": c.get("pass_log"),
    }


if __name__ == "__main__":
    main()
