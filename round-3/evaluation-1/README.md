# Reconciled Five-Condition Repair Scorecard

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** evaluation  
**ID:** `art__bfSxpVnFUc8`

## Layman Summary

Builds one unified scoreboard comparing five different ways of fixing AI-translation errors, checking whether adding a verification step to re-check translations really pays off.

## Full Summary

Reconciled five-condition (B/D/C1/C2/C) translation repair evaluation, built entirely from existing/sibling artifact JSON outputs (zero OpenRouter calls, no GPU, no re-execution of any method). Loads art_7Uc5PlFctjXi's full_method_out.json for conditions B/D/C1 (per-row fix_success/true_regression on the 240-row injected pool, plus pooled/per-language ΔCOMET on the 320-row natural pool), art_QLpPxaqf1VzK's full_method_out.json for the 24-cell global checker validation, and art_7Uc5PlFctjXi's checker_validation.json for the 8-cell within-experiment validation. Discovers the two iteration-3 sibling artifacts for conditions C2 and C at run time by matching gen_plan titles (no formal dependency edge exists on them), since they were built by extending B/D/C1's method.py. Condition C2's sibling artifact (iter_3 gen_art_experiment_1, 'Testing Whether Iteration Alone Fixes Span Edits') completed during this run and was successfully loaded, including handling a genuinely different output schema (natural_pooled/injected_category_table with per-row metadata_c2_fixed/metadata_c2_true_regression fields, rather than B/D/C1's metrics.pooled.<cond> convention) via schema-agnostic accessor functions. Condition C's sibling artifact (iter_3 gen_art_experiment_2, 'Condition C: broad checker plus iterative repair') was still running after being polled repeatedly for over an hour with zero file-system activity (stalled after checker validation, mid-way through the en-ru_RU pass); per the plan's explicit fallback, its metrics were set to the literal string 'NOT_AVAILABLE' with a not_available_reason rather than fabricated, and this degradation propagates into every downstream table cell and the final verdict. Produces four metric groups: (1) an 8-cell validation-reconciliation table naming the within-experiment (175-row) table, not the global (24-cell) table, as the one that actually gated C1's repair scope, with an explicit reconciliation_note on why the two n's and two precision definitions differ and confirming directional (not numerical) agreement; (2) category-broken-out (named_entity/number_unit_date/negation_polarity/quantifier_scope) fix_rate and true_regression_rate per condition, pooled with and without negation rows, each with a 2000-resample bootstrap 95% CI stratified by language_pair, reproducing B/D/C1's original headline numbers exactly (B/D 0.7375 fix_rate / 0.050 true_regression_rate, C1 0.4542/0.125) as a correctness check before extending to C2; (3) a pre-registered numeric tolerance test (same-sign AND magnitude ratio in [0.5x, 2.0x]) for Condition B's fidelity replication of Padmanabhan (2025), applied to the measured -0.0164 vs -0.0108 (ratio 1.52x, PASS, labeled a borderline pass), plus a secondary CI-containment check; (4) a mechanism test comparing C2 against C1 on 240 matched injected-pool rows via paired bootstrap on true_regression_rate and fix_rate (C2-C1 true_regression_rate = -0.071, 95% CI [-0.117,-0.025], i.e. C2 has materially LOWER true regression than C1) plus a ΔCOMET comparison via a documented normal-approximation substitute (since only pooled ΔCOMET, not per-row, exists upstream) that favors C1 (C2-C1 ΔCOMET = -0.013, CI excludes 0 against C2), yielding an explicit MIXED mechanism_verdict since the two outcome axes point in different directions; the net_positive_verdict for full condition C could not be computed (UNDETERMINED) because condition C's sibling artifact never produced output, so the overall top-level verdict is 'UNDETERMINED — condition C2/C data unavailable' rather than a forced CONFIRMED/DISCONFIRMED. Assembles a unified 5-row (B/D/C1/C2/C) JSON table with pooled/per-language ΔCOMET, fix/true-regression rates (including/excluding negation), per-category breakdowns, edit-volume/LLM-call stats, and an availability_flag per condition, explicitly marked as intended to replace the paper's current three-condition Section 6.3 table. Deliverables: eval.py (schema-agnostic across the two upstream output conventions, deterministic seed=42), full/mini/preview eval_out.json validated against the exp_eval_sol_out schema, and a pinned pyproject.toml (numpy==2.5.2, loguru==0.7.3). Downstream GEN_PAPER_TEXT should report the MIXED mechanism finding (C2 lowers true regression but at some COMET cost relative to C1) as the primary result, present the overall verdict as genuinely undetermined pending condition C's completion rather than papering over the gap, and reuse the validation-reconciliation table's stated fact (within-experiment table gates C1's scope, not the global table) verbatim rather than re-deriving it.

## Dependencies

- `art_mhfmDpGp4z1J` — dataset
- `art_7Uc5PlFctjXi` — B/D/C1 results
- `art_QLpPxaqf1VzK` — checker validation

## Output Files

- `eval.py`
- `full_eval_out.json`
- `mini_eval_out.json`
- `preview_eval_out.json`

## Demo Files

- **eval.py** — Evaluation script with metrics computation

---
*Generated by AI Inventor Pipeline*
