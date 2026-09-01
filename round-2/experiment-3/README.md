# Checker-Based Repair Beats Hygiene Retry Fixes

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_7Uc5PlFctjXi`

## Layman Summary

Compares three ways to fix AI-translation errors: a masking baseline, a hygiene retry trick, and a smarter error-checker, measuring which improves quality without breaking correct text.

## Full Summary

Implements and scores three matched span-editing conditions on identical en-ru_RU/en-uk_UA rows from the WMT25 Task 3 dataset (art_mhfmDpGp4z1J), using google/gemma-3-12b-it (OpenRouter) as the fixed repair model, per gen_plan_experiment_3_idx3: B (faithful reproduction of Padmanabhan (2025)'s masked-fill severity-skip baseline: QE-flagged spans masked with __BLANK__, single uncorrected LLM call), D (B plus a trivial hygiene retry -- a second call, temperature=0.3, fires only if leftover placeholder/leaked-instruction text is detected), and C1 (a from-scratch 4-category deterministic content-invariant checker -- named entity via Stanza NER, number/unit/date via script-independent regex, negation polarity via per-language sentence-scoped cue lists with a negative-concord guard and a source-alignment deletion signal, quantifier scope via closed-class word lists -- flags every invariant in the FULL sentence and repairs them all in one uncorrected pass). The checker was validated on the dataset's injected_error_augmentation heldout fold (175 rows) via a conservative single-positive-per-row precision/recall metric; 3 of 8 (language, category) cells (ru_RU/uk_UA named_entity, uk_UA quantifier_scope) failed the recall/precision>=0.5 threshold and were excluded from C1's repair scope, documented in checker_validation.json.

All three conditions ran on an identical stratified subsample: 320 natural rows (160/pair) scored for reference-free DeltaCOMET (Unbabel/wmt22-cometkiwi-da, real gated checkpoint successfully loaded, not a proxy) with 1000-iteration bootstrap 95% CIs, and 240 injected-pool rows (30/cell) scored for fix_rate (corrupted-span-string-absence) and a true_regression_rate (checker-detected invariants present in the wmt24pp clean reference that are newly missing post-repair, beyond what the corruption itself already removed). Total cost: $0.066 of the $10 OpenRouter budget (1,447 calls). Runtime: ~13 minutes on 1x RTX 2000 Ada GPU.

Headline finding: condition B closely replicates Padmanabhan's direction and rough magnitude (pooled DeltaCOMET -0.0164, 95% CI [-0.0237, -0.0101], vs the paper's -0.0108 -- 1.5x magnitude, same sign, CI excludes 0), with a documented fidelity caveat that gemma-3-12b-it showed only 6.25% leakage on masked rows (19/304) versus the paper's model-native leakage failure mode. Condition D (hygiene retry) barely moves DeltaCOMET (-0.0157) and leaves fix_rate/true_regression_rate on the injected set IDENTICAL to B (0.7375 / 0.050) -- the hygiene retry essentially never fires usefully, so D does NOT close B's gap; this is evidence against 'it's just a leakage/regex bug'. Condition C1 (checker-broadened localization) cuts the COMET degradation roughly 5x versus B/D (pooled DeltaCOMET -0.0035, 95% CI [-0.0071, -0.0008] -- still excludes 0 but far smaller), at the cost of a substantially lower fix_rate (0.454 vs 0.738) and a higher true_regression_rate (0.125 vs 0.050) on the injected-pool subset. This pattern -- checking helps overall translation quality more than hygiene does, but at a real fix-rate and regression-rate cost -- is exactly the result the next iteration's verification-loop conditions (C2/C) are meant to investigate.

Two protocol choices are documented explicitly in method_out.json metadata rather than left implicit: (1) injected rows carry no native QE signal, so B/D use an ORACLE QE span (the row's true corrupted-span offsets, computed correctly as start=dataset-offset-start, end=start+len(corrupted_span) since the dataset's own span_offsets are indexed into the pre-corruption clean text, not the corrupted output -- a real bug caught and fixed during testing) with severity='major', isolating repair-generation fidelity from localization quality, while C1 uses its own real checker-based localization on the same injected-pool rows; (2) negation_polarity_flip corruptions are deletions (corrupted_span=''), so the oracle span is zero-width and B/D structurally never attempt a repair on any negation row in the injected-pool subset (fix_rate=0 there is a known artifact of the masking design applied to deletions, not evidence of failure).

Deliverables: method.py (main script), checker.py (4-category checker module), llm_client.py (async OpenRouter client with a live cost ledger), method_out.json/full_method_out.json (identical, schema-validated against exp_gen_sol_out) + mini/preview variants, checker_validation.json, selected_rows.json (exact row ids for reproducibility), pyproject.toml (pinned deps).

## Dependencies

- `art_5ySTX4YfxqG_` — resource dossier
- `art_mhfmDpGp4z1J` — dataset

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
