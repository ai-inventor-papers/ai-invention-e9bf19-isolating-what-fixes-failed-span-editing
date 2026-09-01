# Why Condition C's Combined Repair Fix Collapsed

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** evaluation  
**ID:** `art_ImnQ5UsI-lMB`

## Layman Summary

Re-analyzes three prior translation-repair experiments to separate genuine quality regressions from cases where the automated error-checker itself was simply unreliable.

## Full Summary

Pure re-analysis (no new LLM calls, no new COMET scoring) of three prior span-editing repair experiments on WMT25 en-ru_RU/en-uk_UA translations (B/D/C1 from art_7Uc5PlFctjXi, C2 from art_K8koUmGFDlLN, and Condition C from art_6n9zJVKWXnio), produced as eval.py + eval_out.json validated against the exp_eval_sol_out schema. First verified exact row-ID identity across all three artifacts' selected_rows.json for all three folds (natural, injected-pool, injected-heldout), including the B/D/C1-vs-C pair that had never been directly cross-checked before -- confirmed byte-identical. Produces four separately labeled, source-traced analyses. (1) precision_tier_collapse_analysis: splits the 5 checker-eligible (language,category) cells (of 8) into a high-precision tier (negation_polarity, checker precision 0.78-0.86) and a low-precision tier (number_unit_date, quantifier_scope, precision 0.575-0.65), recomputing Condition C's per-cell certificate_rate directly from raw per-row fields (validated as an exact superset of Condition C's own pre-aggregated table for the 3 categories it does report, and additionally recovers negation_polarity's certificate rate, which that table reports as null). Finds collapse_pattern='concentrated_in_low_precision_tier': mean certificate_rate 0.35 in the high-precision tier vs 0.089 in the low-precision tier (n=2 vs n=3 cells, explicitly flagged as low statistical power), consistent with checker-noise-driven churn rather than uniform cross-invariant regression, reported with fully hedged, non-causal language. No fourth widened-pass-budget artifact was found among the actual dependencies, so this is documented as the best available evidence rather than silently omitted. (2) checker_eligibility_restricted_analysis: derives the exact eligibility scope from checker_validation.json's own recall>=0.5 AND precision>=0.5 threshold rule (5 of 8 cells: number_unit_date both languages, negation_polarity both languages, quantifier_scope in ru_RU only) -- noting this is wider than the plan text's own restatement, which omitted negation_polarity -- then computes fix_rate/true_regression_rate/certificate_rate for B, D, C1, C2, and C restricted to only these cells, side by side with the full pooled figures. The headline ordering (C1 worse regression than C2; Condition C worst of all on true_regression_rate; certificate_rate collapse from C2 to C) survives this restriction unchanged in direction. (3) certificate_definition_by_category: reads art_6n9zJVKWXnio's method.py/checker.py directly (excluded_cells_from_validation + Checker.detect_all(respect_exclusions=True)) and confirms via a worked example row that a row's certificate status is scored only over non-excluded invariant categories, independent of whether the row's own corrupted category is itself excluded (e.g. a named_entity_swap row in an excluded cell is never checked on its own corruption category) -- option (b) in the plan's decision tree. Also surfaces an incidental finding: Condition C's own re-fit checker validation shows named_entity recall/precision of exactly 0.0/0.0 (vs the original run's 1.0/0.32), meaning named_entity is never flagged at all in Condition C's environment, though this does not change the excluded_cells set or any headline result. (4) normal_approx_bias_direction: proves algebraically that treating two positively-correlated ΔCOMET measurements as independent (Var(X-Y)=Var(X)+Var(Y) instead of minus 2*Cov(X,Y)) yields a conservative (wider), not narrower, interval whenever Cov(X,Y)>0, with a numeric worked example using the actual reported B/C1/C2 ΔCOMET 95% CI half-widths at several assumed correlation values. Confirms no per-row ΔCOMET array is persisted in any of the three artifacts (checked directly), so the actual covariance sign cannot be estimated empirically -- the claim is explicitly downgraded from an unconditional assertion to a conditional one ('IF the shared row population/repair model/checker induce positive correlation, THEN the substitute is conservative') with plausible covariance sources named and the exact additional data (per-row paired bootstrap replicates) that would resolve it. eval_out.json's metadata field contains the full detail for all four analyses; metrics_agg carries a flat numeric summary; the datasets/examples array poses each analysis as a directly-quotable question/answer pair with the full analysis object attached via metadata_analysis for schema compliance. Total cost: $0 (no LLM calls). Deliverables: eval.py, eval_out.json (+ full/mini/preview variants, all schema-validated), pyproject.toml with pinned dependencies, deps/ containing the copied dependency files used for computation.

## Dependencies

- `art_6n9zJVKWXnio` — condition-c-results
- `art_7Uc5PlFctjXi` — checker-validation
- `art_K8koUmGFDlLN` — condition-c2-results

## Output Files

- `eval.py`
- `full_eval_out.json`
- `mini_eval_out.json`
- `preview_eval_out.json`

## Demo Files

- **eval.py** — Evaluation script with metrics computation

---
*Generated by AI Inventor Pipeline*
