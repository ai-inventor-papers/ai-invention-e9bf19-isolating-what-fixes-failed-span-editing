# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 07:27:41 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Isolating What Fixes Failed Span Editing
hypothesis: >-
  Padmanabhan (2025)'s WMT25 Task 3 secondary system (SURREYPAI-S2) -- QE-flagged spans masked with a __BLANK__ token, a single
  TowerPlus-9B fill-in pass, no re-check -- scored ΔCOMET = -0.0108, the single worst result of all eight ranked Task 3 entries
  in the WMT25 findings paper, against +0.0201 for the same team's primary retranslation-selection system (SURREYPAI-S1, six
  candidate LLMs). The paper's own appendix attributes much of that gap to mundane failures (a literal unfilled '__BLANK__'
  leaking into the output as '__HEARTBREAK__', 'Corrected words: [...]' format leakage, a single weak 9B model versus a six-model
  selection pool, and a severity heuristic that leaves minor-severity spans unedited whenever a non-minor span co-occurs),
  and a stronger-model QE-informed system in the same ranking (BASELINE-S2, 27B parameters) lands near break-even rather than
  negative on the three language pairs where it reports a directly comparable figure -- weak, task-internal evidence against
  the absence-of-verification story being the sole cause, drawn from only three numeric data points (two from the same paper's
  own two systems, one language pair with all three systems directly comparable) and treated as a motivating diagnosis, not
  a proof, given how thin that evidentiary base is. We hypothesize that once model capability is controlled -- by matching
  the repair model to TowerPlus-9B (or, if that model is unavailable through every third-party route, a substitute whose fidelity
  to the original system is itself verified rather than assumed) and by first removing a trivial post-hoc hygiene filter's
  worth of gain (condition D: reject/retry outputs containing leftover mask tokens or leaked instruction text, no invariant
  checker) -- a genuine, separable residual gap remains between (i) broadening localization from one QE-flagged span to every
  content-invariant violation in the sentence and (ii) adding an iterate-to-verified-pass loop around each repair (a deterministic
  verify-and-retry procedure structurally similar in spirit to, but not a full instance of, counterexample-guided synthesis),
  and that specifically the iteration/verification component (isolated in condition C2: QE-span-only localization, but iteratively
  re-verified until it passes or the pass budget is exhausted) is what converts scoped editing from net-negative to net-non-negative
  on real WMT25 errors -- more than broadened localization alone (condition C1: check all invariants, but repair each in a
  single uncorrected pass) does. This claim remains UNTESTED as of this iteration: no condition (B, D, C1, C2, or C) has been
  run, the deterministic content-invariant checker that all downstream measurement depends on is unvalidated against WMT25
  Task 3's actual error types (and its entity detector for Chinese and Japanese is known, in advance, to have a severe recall
  gap since it falls back to embedded-Latin-script matching for languages with no capitalization signal), and the repair model
  that fixity of comparison depends on has been forced to substitute to a model lacking the original's machine-translation
  fine-tuning, whose behavioral fidelity to Padmanabhan's system is not yet checked. The next iteration's job is therefore
  sequential and gated, not a simultaneous five-condition sweep: first validate the checker's precision/recall on the held-out
  validation split and validate that condition B, run with the substitute repair model, reproduces the original system's qualitative
  failure signature (leftover placeholders, similar direction and rough magnitude of ΔCOMET) as a sanity check on the fixed-model
  design itself; only once both hold does a B/D/C1/C2/C comparison (even a partial one -- B, D, and C1 on one or two language
  pairs -- is preferable to none) speak to the localization-versus-verification question this hypothesis asks.
motivation: >-
  This reframes the previous iteration after fetching and reading, in full, both Padmanabhan (2025) (including Appendix B)
  and the WMT25 shared-task findings paper's Task 3 section (Table 15, Section 6.4) directly — not from summaries. Two verified
  facts sharpen the causal story. First, Padmanabhan's own paper documents concrete implementation failures behind the −0.0108
  result: a garbled literal placeholder token ('__HEARTBREAK__') surviving into the output where '__BLANK__' should have been
  filled, 'Corrected words: [...]' prompt-format leakage, a single 9B model (TowerPlus-9B) used only for this system while
  the sibling submission drew on six candidate models, and a severity heuristic (Algorithm 1) that leaves minor-severity spans
  unedited whenever any non-minor span is present. Second, and more decisively, the WMT25 findings paper's own system ranking
  (Table 15, eight entries: two organizer baselines plus six submissions from three teams) shows this exact masked-fill system,
  SURREYPAI-S2, finishes DEAD LAST by average ΔCOMET across all eight — while a different QE-informed correction system in
  the same ranking, BASELINE-S2 (XCOMET-XL error detection feeding a 27-billion-parameter Gemma3 for automatic post-editing),
  lands in 3rd place with near-zero, mixed ΔCOMET (e.g. 0.000 on En-Cs, +0.007 on En-Is, +0.002 on En-Ru) rather than SURREYPAI-S2's
  consistent negative range (−0.007 to −0.014 across the same language pairs). That is direct, task-internal evidence that
  QE-informed correction is not doomed by design — a stronger model correcting flagged errors lands far closer to break-even
  than a weak model doing naive masked-fill does — which is exactly the confound (model capability and implementation maturity,
  not scoped correction itself) this hypothesis's design must control for before crediting any verification mechanism. Crediting
  a certified loop for fixing a bug a one-line regex would also fix, or for simply matching a bigger model, is not an interesting
  finding, so this hypothesis rules both out first (condition D for hygiene; a fixed, matched repair model across all repair-performing
  conditions) and only then asks the load-bearing question: once those are controlled, does iterative verification specifically
  — as opposed to just seeing more of the sentence — do the work? That question matters because it tells practitioners which
  piece of a scoped-editing pipeline to build: a broader deterministic scanner (cheap, one-shot, no LLM calls per iteration)
  or a genuine verify-and-repair loop (more LLM calls, but catches self-introduced errors). In regulated, terminology-heavy
  domains (legal, medical, financial) where a single corrupted number or flipped negation is a severe failure independent
  of an aggregate COMET delta, this distinction determines whether an auditable per-invariant certificate is worth its extra
  inference cost, or whether a cheaper wider net already captures most of the benefit.
assumptions:
- >-
  Content invariants — named entities, numbers/units/dates, negation polarity, and quantifier scope — can be extracted from
  a source sentence and checked deterministically (NER, regex, cue lists, alignment) against a candidate translation with
  high enough precision/recall against a human-annotated sample that the checker's verdicts, not raw flags, can serve as scoring
  ground truth.
- >-
  Padmanabhan (2025)'s masked-fill design (mask a QE-flagged substring with __BLANK__, TowerPlus-9B single completion pass,
  conditional severity-based masking heuristic that skips minor-severity spans) can be faithfully reproduced as baseline B
  at the scale available here, including its exact severity-skip behavior, so the comparison targets the actual documented
  system rather than a strawman.
- >-
  A trivial post-hoc hygiene filter (reject/retry any output containing a leftover mask token, garbled placeholder text, or
  leaked 'Corrected words:'-style prompt artifacts) is cheap enough to run as condition D within budget and is a fair lower
  bound for how much of B's gap to full retranslation basic output sanitization alone closes, before crediting any invariant-checker
  mechanism.
- >-
  A failed invariant check localizes to a target-language span precise enough to scope a repair (verifiable against human-annotated
  error regions), and TowerPlus-9B — the same weak repair model as B, held fixed across B, D, C1, C2, and C — can be instructed
  to revise only that span across iterations without the loop degenerating into full-sentence regeneration by the final pass.
- >-
  A meaningful fraction of WMT25 Task 3's real errors (six language pairs, five domains) fall into these four checkable categories
  rather than being purely stylistic, and a modest, separately-reported set of injected invariant-violating errors gives adequate
  statistical power where natural incidence of any one category is low.
investigation_approach: >-
  Build and validate a deterministic content-invariant checker (NER for entities; regex plus cross-lingual matching for numbers/units/dates;
  per-language cue lists for negation polarity; a closed-class word list for quantifier scope) against a held-out human-annotated
  sample, reporting precision/recall before using it downstream. Use WMT25 Task 3's English-to-{Chinese, Czech, Japanese,
  Icelandic, Russian, Ukrainian} test data (6,000 translations, five domains, provided QE error-span annotations) plus a modest
  injected-error set for power. Fix the repair model to TowerPlus-9B in every condition that performs a repair, matching B's
  model exactly so no result can be attributed to model capability. Run five conditions at a matched maximum edit-pass budget:
  (B) faithful reproduction of Padmanabhan's secondary system — QE-flagged span masked, severity-skip heuristic applied, one
  TowerPlus-9B fill-in pass, no re-check; (D) B plus a trivial post-hoc hygiene filter that detects and retries (same single-pass
  budget) any output containing a leftover mask token, garbled placeholder, or leaked instruction/format text — no invariant
  checker at all, establishing the ceiling basic hygiene alone can reach; (C1) the deterministic checker flags every failing
  invariant in the sentence (not just the QE span), each is repaired in one uncorrected pass, no re-verification — isolates
  broadened localization; (C2) localization restricted to the original QE-flagged span only, but that span is iteratively
  repaired and re-verified by the checker until it passes or the pass budget is exhausted — isolates the verification/iteration
  loop; (C) both changes combined — checker flags all invariants, each is iteratively repaired and re-verified to a certificate
  or budget exhaustion. Also run a same-severity-restricted variant of C1/C2/C that respects B's minor-severity-skip heuristic,
  to check whether any gain is partly just a broader repair mandate rather than the mechanism itself. For all five (plus the
  severity-matched variants), measure: (i) fix rate on the four checkable categories, scored on all flagged repairs and on
  the human-confirmed subset; (ii) true (human-confirmed) regression rate — invariants correct pre-repair that become violated
  post-repair; (iii) net translation-quality change via COMET, reported the same way as Padmanabhan's ΔCOMET for direct comparability
  to −0.0108 and +0.0201; (iv) edit volume / gain-to-edit-ratio, to rule out C converging to full retranslation; (v) LLM calls/tokens
  per sentence, since C2 and C multiply calls relative to B/D/C1. Report all headline metrics separately for natural-error
  and injection-augmented subsets, and separately per language pair.
success_criteria: >-
  The central, mechanism-attributing claim is confirmed if: (a) D closes only part of B's gap to full retranslation (i.e.,
  hygiene alone is not sufficient — ruling out the 'C just caught a regex-fixable bug' explanation), and (b) among C1, C2,
  and C, condition C2 (iteration/verification with QE-span-only localization) achieves a materially larger reduction in true
  regression rate and a materially larger ΔCOMET improvement over D than C1 (broadened localization, single-pass) does, establishing
  verification as the load-bearing mechanism rather than merely seeing more of the sentence; and (c) full condition C achieves
  a non-negative mean ΔCOMET together with a true regression rate substantially and statistically significantly lower than
  B's, at a fix rate comparable to or higher than B's, on the natural-error subset specifically (not only injected errors),
  without C's edit volume collapsing to full-retranslation levels. Disconfirmed (for the mechanism claim) if C1 and C2 improve
  on D by statistically indistinguishable amounts — meaning the two factors cannot be separated by this design after all,
  or contribute equally, and the CEGIS framing's specific claim about verification being the differentiator does not hold.
  Disconfirmed (for the net-positive claim) if C's ΔCOMET remains negative or statistically indistinguishable from B's replicated
  result even after controlling for model and hygiene — meaning the field's negative result on scoped editing generalizes
  past the confounds this hypothesis controls for, which is itself a real, informative finding. A result where C is net-positive
  only on injected errors but not on WMT25's real errors is a partial disconfirmation, indicating the checker's advantage
  is confined to synthetically-clean error types.
related_works:
- >-
  Padmanabhan 2025, 'Can QE-informed (Re)Translation lead to Error Correction?' (WMT25 Task 3 submission SURREYPAI, fetched
  and read in full including Appendix B): reports ΔCOMET = −0.0108 for its secondary, single-TowerPlus-9B masked-fill scoped-editing
  system (submission SURREYPAI-S2) versus +0.0201 for its own primary system, which selects among six candidate LLM retranslations
  by QE score (SURREYPAI-S1); its Appendix B and Section 4.2 directly document a literal unfilled '__BLANK__' leaking into
  output as '__HEARTBREAK__', 'Corrected words: [...]' format leakage, and a conditional heuristic (Algorithm 1) that leaves
  minor-severity spans unedited whenever a non-minor span co-occurs — concrete confounds this hypothesis's condition D and
  matched-repair-model design are built specifically to control for before crediting any verification mechanism.
- >-
  WMT25 Findings paper, 'Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems' (fetched and read
  in full, including Table 15 and Section 6.4's Task 3 discussion): confirms 'Task 3 results show that minimal editing is
  challenging even when informed by quality indicators' (verbatim, Section 7) and, more specifically, that of eight ranked
  Task 3 entries (2 organizer baselines + 6 submissions from 3 teams), SURREYPAI-S2 (Padmanabhan's masked-fill system) ranks
  LAST by average ΔCOMET, while BASELINE-S2 — an organizer baseline that also performs QE-informed correction (XCOMET-XL error
  detection feeding a 27B-parameter Gemma3 for automatic post-editing) — ranks 3rd with near-zero, mixed ΔCOMET (e.g. 0.000
  En-Cs, +0.007 En-Is, +0.002 En-Ru) rather than SURREYPAI-S2's consistently negative range on the same pairs. This task-internal
  contrast is the direct evidence this hypothesis's motivation and D/matched-model design are built on: a stronger model doing
  QE-informed correction lands near break-even, so scoped/QE-guided correction's failure here is not uniform across the task,
  and the weakest system's identity (small model, masked-fill, documented output-hygiene bugs) is itself informative.
- >-
  Deoghare et al. 2023 (EMNLP Findings, 'Quality Estimation-Assisted Automatic Post-Editing', read in full): a jointly-trained
  encoder-decoder APE model where word-level QE is an auxiliary training signal or additional decoder input, but the decoder
  always regenerates the full target sentence from scratch in every variant — it reduces but does not eliminate over-correction
  (18.30 vs 19.39 TER) without ever freezing non-flagged spans or iterating to a verified certificate, a materially different
  mechanism from this hypothesis's localized, non-regenerative, iterate-to-certificate repair.
- >-
  Deoghare et al. 2025 ('Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE', read in full): uses Grid
  Beam Search to force QE-tagged 'OK' spans as lexical constraints while the decoder retains full freedom to reorder and rephrase
  around them — soft-constrained full regeneration, not frozen-span editing with an explicit stopping certificate; oracle-vs-predicted-tag
  gaps of 0.3–1.3 TER show the method's ceiling is bounded by QE tag accuracy in a way this hypothesis's checker precision/recall
  validation step makes explicit rather than implicit.
- >-
  LaSEr-Edit (localized span-level editing over full regeneration in controlled-text-generation) and roundtrip-verification-and-repair
  approaches to faithful autoformalization (iterate-to-certificate stopping verified by logical equivalence): the two closest
  analogues to this hypothesis's mechanism outside MT, neither tested in machine translation and neither evaluated against
  a real, documented failure of naive scoped editing with the localization-versus-verification factors experimentally separated
  the way this hypothesis's B/D/C1/C2/C design does.
inspiration: >-
  Cross-field transfer from formal methods and program synthesis, specifically Counterexample-Guided Inductive Synthesis (CEGIS):
  a synthesizer proposes a candidate, a verifier either certifies it or returns a concrete counterexample that scopes the
  next refinement, and the loop terminates on an explicit certificate rather than a fixed pass count. Reading Padmanabhan
  (2025) in full (not just its headline numbers) showed MT researchers have already tried a surface version of scoped editing
  and it lost to full retranslation — but the paper's own appendix attributes much of that loss to mundane bugs (a leaked
  placeholder token, a weak model, a heuristic that skips spans) rather than to the absence of a CEGIS-style loop per se.
  The refined transplant this hypothesis tests is therefore not 'verification fixes scoped editing' as a bundled claim, but
  a factorial decomposition modeled on how a rigorous systems paper would isolate a confound: first subtract what trivial
  hygiene explains (condition D, no CEGIS machinery at all), then separately vary CEGIS's two distinguishable ingredients
  — broader counterexample discovery (C1: see more failing invariants) versus the refine-and-reverify loop itself (C2: keep
  refining the same one until it verifies) — to determine which piece, if either, is actually load-bearing once the mundane
  confounds are removed.
terms:
- term: Content invariant
  definition: >-
    A piece of source-sentence meaning — a named entity, a number/unit/date, a negation polarity marker, or a quantifier —
    that must be preserved in any faithful translation and can be checked deterministically (via NER, regex, cue lists, or
    alignment) rather than judged by a learned QE model.
- term: Condition D (hygiene-filtered baseline)
  definition: >-
    Baseline B (Padmanabhan's masked-fill system) plus a trivial post-hoc filter that rejects and retries any output containing
    a leftover mask token, a garbled placeholder, or leaked prompt/instruction text — with no content-invariant checker involved
    — used to measure how much of B's gap to full retranslation basic output hygiene alone closes.
- term: Localization breadth vs. verification loop (C1 vs. C2)
  definition: >-
    The two mechanisms this hypothesis separates: C1 broadens what is checked (every failing invariant, not just the one QE-flagged
    span) but repairs each in a single uncorrected pass; C2 keeps localization narrow (the original QE-flagged span only)
    but iteratively repairs and re-verifies that span until it passes or a pass budget is exhausted.
- term: Certificate (translation)
  definition: >-
    A translation for which every extracted content invariant has been checked by the deterministic checker and passes; an
    explicit, checkable, auditable stopping condition produced by conditions C2 and C but absent from B, D, and C1.
- term: True (human-confirmed) regression rate
  definition: >-
    The fraction of content invariants correctly rendered before a repair step that become violated after it, scored only
    against human-confirmed violations so the metric is not inflated by checker or QE-explanation false positives — the quantitative
    form of the self-introduced-error failure Padmanabhan (2025)'s Appendix B documents qualitatively (e.g. the literal '__HEARTBREAK__'
    placeholder artifact).
summary: >-
  After reading Padmanabhan (2025)'s WMT25 Task 3 system in full, its documented −0.0108 ΔCOMET failure for scoped span editing
  turns out to be partly explained by mundane bugs (a leaked placeholder token, format leakage, a weak single model, a span-skipping
  heuristic); this hypothesis first subtracts what a trivial hygiene fix and a matched repair model explain, then factorially
  separates broadened invariant localization from an iterate-to-certificate verification loop (borrowed from counterexample-guided
  synthesis) to determine which mechanism, if either, actually converts scoped MT editing from a documented loss into a net-positive
  result.
_relation_rationale: >-
  Same B/D/C1/C2/C frame; narrowed evidentiary claims and added explicit validation gates reviewer flagged as missing.
_confidence_delta: decreased
_key_changes:
- >-
  Downgraded the 3-point shared-task contrast (Padmanabhan's two systems + one organizer baseline, only 1 of 6 language pairs
  fully comparable) from decisive evidence to a weak, motivating diagnosis, per reviewer's MAJOR evidentiary critique.
- >-
  Made explicit that zero of the five conditions have been run this iteration and that every quoted ΔCOMET number is from
  prior publications, not new measurement -- the hypothesis no longer implies a completed comparison.
- >-
  Added an explicit prerequisite the previous version lacked: before trusting any B/D/C1/C2/C result, condition B run with
  the forced substitute repair model (google/gemma-3-12b-it in place of unavailable TowerPlus-9B) must be validated to reproduce
  Padmanabhan's original failure signature (placeholder leakage, comparable ΔCOMET direction/magnitude), addressing the reviewer's
  MAJOR methodology critique that a non-MT-fine-tuned substitute could give condition B a different capability floor entirely.
- >-
  Added an explicit prerequisite that the deterministic invariant checker's precision/recall must be validated on the held-out
  split before its verdicts are used for fix-rate/regression-rate scoring, and flagged in advance that Chinese/Japanese entity
  detection (Latin-script-substring fallback only) is a known, not merely possible, recall gap -- addressing the reviewer's
  MAJOR rigor critique.
- >-
  Softened the CEGIS framing to 'structurally similar in spirit to, but not a full instance of, counterexample-guided synthesis'
  per the reviewer's MINOR novelty critique, since the method has no candidate generalization or unrealizability reasoning.
- >-
  Reframed the next-iteration task as a gated, sequential validate-then-compare pipeline (checker validation -> condition-B
  fidelity check -> even a partial B/D/C1 comparison) rather than an unordered five-condition sweep, so partial progress toward
  the mechanism claim is possible without all five conditions running at once.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_5ySTX4YfxqG_
type: research
title: Resource Dossier for Scoped-Editing Replication
summary: >-
  This research artifact delivers a fully resolved, implementation-ready resource dossier for replicating Padmanabhan (2025)'s
  SURREYPAI-S2 masked-fill baseline (WMT25 Task 3, ΔCOMET=-0.0108) and building the four-category content-invariant checker
  (entity / number-unit-date / negation-polarity / quantifier-scope) across Chinese, Czech, Japanese, Icelandic, Russian,
  and Ukrainian. It provides: (1) the verbatim Algorithm 1 pseudocode and full masking prompt template quoted directly from
  the paper's arXiv HTML mirror, plus the three documented leakage bugs (literal __BLANK__/placeholder survival, metadata
  leakage, prompt-following failure) that any faithful replication must expect to reproduce; (2) the reconciled, authoritative
  WMT25 Table 15 (8 systems x 6 language pairs x ΔCOMET/GER), confirming Padmanabhan's self-reported and the organizers' re-scored
  numbers are consistent (rounding only, not a real discrepancy), and pinning the exact scorer footnoted by the organizers
  (Unbabel/wmt22-cometkiwi-da) as the sole ΔCOMET metric across every system; (3) a DEFINITIVE, triple-confirmed resolution
  that TowerPlus-9B is absent from OpenRouter (raw model-list JSON regex search across 705K characters, HF Inference-Providers
  panel showing no active provider, and targeted hosting search all agree), together with a corrected finding that the plan's
  assumed fallback google/gemma-2-9b-it is ALSO no longer listed, and a freshly re-ranked substitute table (google/gemma-3-12b-it
  recommended, with exact live OpenRouter pricing/context for 5 candidates) with an explicit, undownplayed limitation about
  the generation mismatch and missing MT fine-tuning; (4) the exact COMET package/checkpoint/install command, its CC-BY-NC-SA-4.0
  license terms (gated HF download), and a measured GPU throughput benchmark (~155 segments/sec on 1x V100, ~648 on 8x V100)
  with an honestly-reported absence of any CPU benchmark rather than an invented number; and (5) a fully resourced language
  x category decision table for the four-category checker, with real package/model names, license terms, and reported precision/recall
  for every cell that has one, explicitly marked 'unvalidated - needs pilot' elsewhere. The dossier also issues seven corrections
  to the plan's own preliminary research (Stanza's NER coverage is far broader than assumed, Duckling's real gap is Czech+Icelandic
  not Ukrainian, MultiLegalNeg covers none of the six target languages, Japanese quantifier-negation scope is not a clean
  'obligatory wide scope' rule per the linguistics literature, etc.), each backed by a freshly fetched primary source rather
  than trusting the earlier pass. Every claim is cited to a specific fetched page, PDF, or API response fetched in this research
  pass; no numbers were invented where a source did not provide one.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_mhfmDpGp4z1J
type: dataset
title: WMT25 Translation Error-Correction Dataset
summary: >-
  Produces data.py (a uv inline script, deterministic seed) and full_data_out.json validated against the exp_sel_data_out
  schema, containing 8,519 one-row-per-example rows across two dataset groups. (1) wmt25_task3_natural: all 6,000 rows of
  the official WMT25 Task 3 combined test set, fetched directly from the wmt-conference/wmt25-mteval GitHub release (data/testset/wmt25_task3_combined_test_set.tsv,
  released 2025-07-24) -- 1,000 segments each for en->{zh_CN, cs_CZ, ja_JP, is_IS, ru_RU, uk_UA}, spanning the news/social/speech/literary/dialogue
  domains. Each row carries the English source, the specific MT system's hypothesis output, the CometKiwi-derived QE error
  spans (character offsets + severity in {minor,major,critical} -- the actual pre-scoring localization signal), domain, doc/segment/system
  ids, and the QE overall score. No public post-hoc human MQM severity/type gold layer matching the findings-paper Table 15
  was found (the release's post_edit column is empty for all 6000 rows); this gap is documented in the output's top-level
  metadata rather than silently assumed away, and qe_flagged_spans is used as the operational localization signal per the
  plan's fallback. (2) injected_error_augmentation: 2,519 programmatically corrupted rows built from a wholly disjoint corpus
  -- held-out human post-edited target text from google/wmt24pp (WMT24++, arXiv:2502.12404) -- covering the same 6 language
  pairs and all 4 planned invariant categories (named_entity_swap, number_unit_date_alteration, negation_polarity_flip, quantifier_substitution),
  balanced up to 130 rows per (language_pair, category) cell. Each injected row carries the pre-corruption clean target text,
  the corrupted text, the exact original_span/corrupted_span strings, and character span_offsets, so a downstream checker's
  precision/recall against a known ground truth is directly computable. Category construction: numbers/dates use script-independent
  regex with boundary guards against handle-like tokens (e.g. @user12); negation and quantifier corruptions use per-language
  cue/pair lists matched on word boundaries for space-delimited languages (cs_CZ/is_IS/ru_RU/uk_UA) and only fire when exactly
  one negation marker is present in the sentence (Slavic/Czech negative-concord languages allow multiple co-occurring negation
  markers, so removing just one does not reliably flip polarity unless it is the only one); named-entity swap uses a capitalization
  heuristic for cs_CZ/is_IS (explicit accented-letter classes, not a naive Unicode range) and ru_RU/uk_UA (Cyrillic capitals),
  filtered by per-language function-word stoplists, a sentence-boundary-capitalization exclusion, and a corpus-frequency cap
  (real proper nouns are rare across ~960 rows; capitalized function words recur often) -- for zh_CN/ja_JP, which carry no
  capitalization signal, entities are detected only via embedded Latin-script substrings, a documented lower-recall NER-tooling
  gap versus a full multilingual NER pass. Both dataset groups are stratified by language_pair (and language_pair x category
  for the injected set) into metadata_fold in {experimental_pool (~82%), checker_validation_heldout (~18%)}, kept strictly
  disjoint so the eventual checker validation is never contaminated by rows used for the B/D/C1/C2/C system comparison. Output
  is 28MB (under the 100MB limit, not split), schema-validated against exp_sel_data_out, with full/mini/preview variants and
  a pinned pyproject.toml (loguru==0.7.3) for reproducibility.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_QLpPxaqf1VzK
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Testing a Translation Error Checker
summary: >-
  This experiment validates a four-category content-invariant checker (named_entity_swap, number_unit_date_alteration, negation_polarity_flip,
  quantifier_substitution) against the checker_validation_heldout fold of the WMT25 translation error-correction dataset (art_mhfmDpGp4z1J),
  across all six target languages (zh_CN, cs_CZ, ja_JP, is_IS, ru_RU, uk_UA), following the resource dossier's recommendations
  (art_5ySTX4YfxqG_). checker_module.py implements the checker: stanza NER for named-entity detection where a trained model
  exists (zh, ja, ru, uk, confirmed live), a documented regex/capitalization-heuristic fallback for cs/is (stanza ships no
  NER model for either, exactly as the dossier flags -- logged explicitly per fallback_plan rather than silently substituted);
  a uniform regex parser for number/unit/date/currency across all six languages (Duckling was not attempted, per fallback_plan,
  given its own excluded-language gap and JVM/Docker footprint); a cross-lingual polarity-mismatch check for negation (English
  source cue presence vs. target cue presence) since the injected corruption DELETES the segment's one negation cue, leaving
  nothing at the ground-truth offset for target-only span detection -- the sentence-level fallback the plan's own fallback_plan
  anticipates; and closed-class quantifier word-list matching for the in-place antonym-swap corruption. A language-naive BASELINE
  checker (Latin-only capitalization regex applied uniformly regardless of script, bare-digit number regex, and NO negation/quantifier
  resource at all) is run side by side on the identical rows for a controlled comparison. method.py scores both systems over
  448 injected checker_validation_heldout rows (ground-truth spans -> direct recall) and 1,080 natural checker_validation_heldout
  rows x 4 categories (CometKiwi qe_flagged_spans -> secondary, noisier false-positive proxy for precision, exactly as the
  plan specifies never to use alone for the headline table), computes 2000-resample bootstrap 95% CIs for precision and recall
  in every (language, category) cell, and marks a cell excluded_from_headline when either falls below the 0.5 usability threshold.
  Result: recall is strong for our method in 20/24 cells (>=0.7), but the natural-row precision proxy is noisy (common numbers/quantifiers/entities
  in ordinary text count as 'false positives' against sparse QE spans), so only 6/24 cells clear both thresholds; negation_polarity_flip
  is the strongest headline result, clearing the bar in 5/6 languages with 0.35-0.92 recall and 0.75-0.89 precision where
  the baseline scores exactly 0.0 recall (no negation resource at all). An unexpected, honestly-reported finding: for named_entity_swap
  on zh_CN/ja_JP the baseline's Latin-capitalization regex actually beats our stanza-NER checker on recall, because the dataset's
  own construction restricts entity corruptions on those two scripts to embedded Latin-script substrings (a dataset-methodology
  artifact, not evidence NER underperforms regex in general) -- flagged explicitly in methodology_notes rather than hidden.
  Zero OpenRouter/LLM calls were used ($0 of the $10 budget); all detectors are deterministic rule-based/NER functions. Output
  validated against the exp_gen_sol_out schema, with full/mini/preview variants and a pinned pyproject.toml (uv pip freeze)
  for reproducibility. Downstream GEN_PAPER_TEXT should treat the negation-polarity result as the primary positive finding,
  the zh/ja entity-detection mismatch as a documented scope-boundary finding, and the natural-row-proxy precision numbers
  as a noisy secondary signal never to be quoted as if they were exact.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_G9ppuk8aHUhW
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Sanity-Check for the Masked-Fill Baseline
summary: >-
  This artifact executes method.py, a faithful reproduction of Padmanabhan (2025)'s SURREYPAI-S2 masked-fill baseline (Condition
  B) on 1,560 experimental_pool rows spanning en-zh_CN (779) and en-cs_CZ (781) from the WMT25 Task 3 dataset dependency.
  For each row, a severity-conditioned masking rule (qe_overall_score >= 0.90: no mask; 0.50-0.90: mask non-minor spans; <0.50:
  mask all flagged spans) determines which QE-flagged error spans get replaced with a placeholder token, then a single OpenRouter
  call to google/gemma-3-12b-it (the dossier-confirmed substitute for the unavailable TowerPlus-9B/gemma-2-9b-it) fills the
  masked spans with no retry or re-check, exactly matching Condition B's faithful-baseline design. All 1,560 rows completed
  in 221.1s for a total OpenRouter cost of $0.076 (well under the $10 budget). A regex-based leakage detector flags surviving
  placeholder tokens, garbled tokens, and generic instruction-following artifacts (e.g. 'Corrected words:', 'Here is the revised...')
  in the repaired text, mirroring Padmanabhan's Appendix B failure modes; pooled leakage rate came out to 0.092 (9.2% of masked
  rows show leakage). For quality scoring, the plan called for Unbabel/wmt22-cometkiwi-da (organizer-footnoted scorer) with
  wmt22-comet-da as secondary fallback; both are gated HF Hub checkpoints. At execution time HuggingFace Hub returned a persistent,
  account-wide HTTP 429 on every download attempt for both checkpoints (confirmed via exponential-backoff retries against
  a 600s wall-clock budget for the primary and a 180s budget for the secondary -- 12 total attempts, all 429), so per the
  artifact's fallback plan the script cascaded to a documented non-COMET substitute: an LLM-judge 0-1 adequacy proxy (openai/gpt-4o-mini
  via OpenRouter, scored before/after the edit). This substitution is explicitly recorded in method_out.json's metadata.comet_substitution
  field with the reason, substitute name, and an explicit warning that the proxy's scale/calibration is NOT comparable to
  Padmanabhan's ΔCOMET. Under this substitute scorer, pooled mean delta (proxy quality after minus before) was -0.056, i.e.
  Condition B's masked-fill edit degrades quality on average, consistent in DIRECTION with the paper's ΔCOMET=-0.0108 finding
  but not directly comparable in magnitude since the metric itself differs. The gate_verdict is reported as PASS_UNRELIABLE_SUBSTITUTED_SCORER
  -- a three-way verdict (not a clean PASS/FAIL) that flags the reproduction as directionally consistent with the documented
  failure signature (negative quality delta + non-trivial leakage) but explicitly caveats that the magnitude comparison against
  the paper's -0.0108/-0.007..-0.014 published deltas cannot be trusted because the scorer itself was substituted. method_out.json
  also contains, per language pair, mean delta, leakage rate, n_spans_flagged/masked, and 5-10 verbatim example leaked outputs
  for qualitative inspection, plus the full published_comparison block and gate_component_results breakdown (direction/magnitude/leakage).
  This artifact's core deliverable for downstream use is the explicit, non-hidden caveat: any downstream artifact (Condition
  D/C1/C2/C) that relies on this fidelity check passing should treat the COMET-based magnitude claim as UNVERIFIED and should
  either retry the real COMET checkpoint when HF Hub throttling clears, or explicitly carry the same LLM-judge proxy forward
  for a fair (still-substituted-but-consistent) comparison rather than mixing a real-COMET result for one condition against
  this proxy-scored one.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_7Uc5PlFctjXi
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Checker-Based Repair Beats Hygiene Retry Fixes
summary: |-
  Implements and scores three matched span-editing conditions on identical en-ru_RU/en-uk_UA rows from the WMT25 Task 3 dataset (art_mhfmDpGp4z1J), using google/gemma-3-12b-it (OpenRouter) as the fixed repair model, per gen_plan_experiment_3_idx3: B (faithful reproduction of Padmanabhan (2025)'s masked-fill severity-skip baseline: QE-flagged spans masked with __BLANK__, single uncorrected LLM call), D (B plus a trivial hygiene retry -- a second call, temperature=0.3, fires only if leftover placeholder/leaked-instruction text is detected), and C1 (a from-scratch 4-category deterministic content-invariant checker -- named entity via Stanza NER, number/unit/date via script-independent regex, negation polarity via per-language sentence-scoped cue lists with a negative-concord guard and a source-alignment deletion signal, quantifier scope via closed-class word lists -- flags every invariant in the FULL sentence and repairs them all in one uncorrected pass). The checker was validated on the dataset's injected_error_augmentation heldout fold (175 rows) via a conservative single-positive-per-row precision/recall metric; 3 of 8 (language, category) cells (ru_RU/uk_UA named_entity, uk_UA quantifier_scope) failed the recall/precision>=0.5 threshold and were excluded from C1's repair scope, documented in checker_validation.json.

  All three conditions ran on an identical stratified subsample: 320 natural rows (160/pair) scored for reference-free DeltaCOMET (Unbabel/wmt22-cometkiwi-da, real gated checkpoint successfully loaded, not a proxy) with 1000-iteration bootstrap 95% CIs, and 240 injected-pool rows (30/cell) scored for fix_rate (corrupted-span-string-absence) and a true_regression_rate (checker-detected invariants present in the wmt24pp clean reference that are newly missing post-repair, beyond what the corruption itself already removed). Total cost: $0.066 of the $10 OpenRouter budget (1,447 calls). Runtime: ~13 minutes on 1x RTX 2000 Ada GPU.

  Headline finding: condition B closely replicates Padmanabhan's direction and rough magnitude (pooled DeltaCOMET -0.0164, 95% CI [-0.0237, -0.0101], vs the paper's -0.0108 -- 1.5x magnitude, same sign, CI excludes 0), with a documented fidelity caveat that gemma-3-12b-it showed only 6.25% leakage on masked rows (19/304) versus the paper's model-native leakage failure mode. Condition D (hygiene retry) barely moves DeltaCOMET (-0.0157) and leaves fix_rate/true_regression_rate on the injected set IDENTICAL to B (0.7375 / 0.050) -- the hygiene retry essentially never fires usefully, so D does NOT close B's gap; this is evidence against 'it's just a leakage/regex bug'. Condition C1 (checker-broadened localization) cuts the COMET degradation roughly 5x versus B/D (pooled DeltaCOMET -0.0035, 95% CI [-0.0071, -0.0008] -- still excludes 0 but far smaller), at the cost of a substantially lower fix_rate (0.454 vs 0.738) and a higher true_regression_rate (0.125 vs 0.050) on the injected-pool subset. This pattern -- checking helps overall translation quality more than hygiene does, but at a real fix-rate and regression-rate cost -- is exactly the result the next iteration's verification-loop conditions (C2/C) are meant to investigate.

  Two protocol choices are documented explicitly in method_out.json metadata rather than left implicit: (1) injected rows carry no native QE signal, so B/D use an ORACLE QE span (the row's true corrupted-span offsets, computed correctly as start=dataset-offset-start, end=start+len(corrupted_span) since the dataset's own span_offsets are indexed into the pre-corruption clean text, not the corrupted output -- a real bug caught and fixed during testing) with severity='major', isolating repair-generation fidelity from localization quality, while C1 uses its own real checker-based localization on the same injected-pool rows; (2) negation_polarity_flip corruptions are deletions (corrupted_span=''), so the oracle span is zero-width and B/D structurally never attempt a repair on any negation row in the injected-pool subset (fix_rate=0 there is a known artifact of the masking design applied to deletions, not evidence of failure).

  Deliverables: method.py (main script), checker.py (4-category checker module), llm_client.py (async OpenRouter client with a live cost ledger), method_out.json/full_method_out.json (identical, schema-validated against exp_gen_sol_out) + mini/preview variants, checker_validation.json, selected_rows.json (exact row ids for reproducibility), pyproject.toml (pinned deps).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_qUG1DIUZKEBQ
type: evaluation
in_dependencies:
- id: art_mhfmDpGp4z1J
  label: dataset
title: Does Hygiene or Verification Fix Editing?
summary: >-
  Implements the full evaluation pipeline specified in the artifact plan for the hypothesis 'Does Hygiene or Verification
  Fix Editing?': paired bootstrap 95%-CI ΔCOMET (B-D, C1-D, C1-B, both paired-difference and marginal-mean forms), Wilson
  and Clopper-Pearson binomial CIs for true (ground-truth-confirmed) regression rate and fix rate (both all-flagged and ground-truth-confirmed
  variants) per condition, an edit-volume-to-gain ratio (mean edited-character-fraction / mean ΔCOMET gain) for D and C1,
  a pre-registered checker-precision/recall-gated sensitivity re-analysis (0.6 threshold, zh_CN/ja_JP named-entity flagged
  in advance), and a six-language-pair ΔCOMET/GER reconciliation table. At evaluation time, this iteration's three sibling
  B/D/C1 experiment sessions (gen_art_experiment_1/2/3) were still actively running (growing terminal-session logs, no result
  files written yet) and produced no checker_validation*.json, condition_b_fidelity*.json, or b_d_c1_results*.json outputs,
  so eval.py's discovery step correctly found nothing usable and every affected metric degrades explicitly to NOT_AVAILABLE
  with a stated reason and the exact search paths tried, per the plan's graceful-degradation requirement -- no placeholder
  numbers were fabricated anywhere. The condition-B fidelity-gate verdict is surfaced as a first-class metadata field (condition_b_fidelity_gate_verdict
  = NOT_AVAILABLE) with a top-level caveat explaining that every B/D/C1 comparison is conditional on it. The six-language-pair
  reconciliation table's quoted column is populated with real, verbatim SURREYPAI-S2 and BASELINE-S2 per-language-pair ΔCOMET/GER
  figures freshly extracted from WMT25 findings-paper Table 15 (fetched and regex-grepped from the primary PDF, not copied
  from a prior summary that omitted the full breakdown); its measured column is NOT_AVAILABLE pending the sibling experiments.
  A real, non-fabricated descriptive statistic is also reported from the dataset dependency alone: per-(language_pair, invariant_category)
  row counts in the checker_validation_heldout fold, including the pre-registered zh_CN/ja_JP named-entity-swap cell counts,
  clearly labeled as composition data rather than a precision/recall measurement. All statistics primitives (bootstrap paired
  CI, Wilson CI, Clopper-Pearson CI, sensitivity re-analysis, edit-volume-to-gain ratio) were validated two ways: an in-script
  self-test on synthetic fixtures (logged, never written into eval_out.json's reported metrics) and a separate integration
  check against a hand-built fixture file mimicking the real b_d_c1_results schema, confirming every 'if real data existed'
  code path produces correct, sensible numbers. eval_out.json validates against the exp_eval_sol_out schema. The evaluation
  script re-scans for sibling outputs on every run (glob-based discovery pruning .venv/.git/node_modules so it stays fast
  even while sibling experiments are mid-install) and should simply be re-run once the B/D/C1 experiments finish, at which
  point every NOT_AVAILABLE field will populate with real paired statistics automatically -- no code changes needed.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 4 artifacts were created THIS iteration.

id: art_QLpPxaqf1VzK
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Testing a Translation Error Checker
summary: >-
  This experiment validates a four-category content-invariant checker (named_entity_swap, number_unit_date_alteration, negation_polarity_flip,
  quantifier_substitution) against the checker_validation_heldout fold of the WMT25 translation error-correction dataset (art_mhfmDpGp4z1J),
  across all six target languages (zh_CN, cs_CZ, ja_JP, is_IS, ru_RU, uk_UA), following the resource dossier's recommendations
  (art_5ySTX4YfxqG_). checker_module.py implements the checker: stanza NER for named-entity detection where a trained model
  exists (zh, ja, ru, uk, confirmed live), a documented regex/capitalization-heuristic fallback for cs/is (stanza ships no
  NER model for either, exactly as the dossier flags -- logged explicitly per fallback_plan rather than silently substituted);
  a uniform regex parser for number/unit/date/currency across all six languages (Duckling was not attempted, per fallback_plan,
  given its own excluded-language gap and JVM/Docker footprint); a cross-lingual polarity-mismatch check for negation (English
  source cue presence vs. target cue presence) since the injected corruption DELETES the segment's one negation cue, leaving
  nothing at the ground-truth offset for target-only span detection -- the sentence-level fallback the plan's own fallback_plan
  anticipates; and closed-class quantifier word-list matching for the in-place antonym-swap corruption. A language-naive BASELINE
  checker (Latin-only capitalization regex applied uniformly regardless of script, bare-digit number regex, and NO negation/quantifier
  resource at all) is run side by side on the identical rows for a controlled comparison. method.py scores both systems over
  448 injected checker_validation_heldout rows (ground-truth spans -> direct recall) and 1,080 natural checker_validation_heldout
  rows x 4 categories (CometKiwi qe_flagged_spans -> secondary, noisier false-positive proxy for precision, exactly as the
  plan specifies never to use alone for the headline table), computes 2000-resample bootstrap 95% CIs for precision and recall
  in every (language, category) cell, and marks a cell excluded_from_headline when either falls below the 0.5 usability threshold.
  Result: recall is strong for our method in 20/24 cells (>=0.7), but the natural-row precision proxy is noisy (common numbers/quantifiers/entities
  in ordinary text count as 'false positives' against sparse QE spans), so only 6/24 cells clear both thresholds; negation_polarity_flip
  is the strongest headline result, clearing the bar in 5/6 languages with 0.35-0.92 recall and 0.75-0.89 precision where
  the baseline scores exactly 0.0 recall (no negation resource at all). An unexpected, honestly-reported finding: for named_entity_swap
  on zh_CN/ja_JP the baseline's Latin-capitalization regex actually beats our stanza-NER checker on recall, because the dataset's
  own construction restricts entity corruptions on those two scripts to embedded Latin-script substrings (a dataset-methodology
  artifact, not evidence NER underperforms regex in general) -- flagged explicitly in methodology_notes rather than hidden.
  Zero OpenRouter/LLM calls were used ($0 of the $10 budget); all detectors are deterministic rule-based/NER functions. Output
  validated against the exp_gen_sol_out schema, with full/mini/preview variants and a pinned pyproject.toml (uv pip freeze)
  for reproducibility. Downstream GEN_PAPER_TEXT should treat the negation-polarity result as the primary positive finding,
  the zh/ja entity-detection mismatch as a documented scope-boundary finding, and the natural-row-proxy precision numbers
  as a noisy secondary signal never to be quoted as if they were exact.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_G9ppuk8aHUhW
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Sanity-Check for the Masked-Fill Baseline
summary: >-
  This artifact executes method.py, a faithful reproduction of Padmanabhan (2025)'s SURREYPAI-S2 masked-fill baseline (Condition
  B) on 1,560 experimental_pool rows spanning en-zh_CN (779) and en-cs_CZ (781) from the WMT25 Task 3 dataset dependency.
  For each row, a severity-conditioned masking rule (qe_overall_score >= 0.90: no mask; 0.50-0.90: mask non-minor spans; <0.50:
  mask all flagged spans) determines which QE-flagged error spans get replaced with a placeholder token, then a single OpenRouter
  call to google/gemma-3-12b-it (the dossier-confirmed substitute for the unavailable TowerPlus-9B/gemma-2-9b-it) fills the
  masked spans with no retry or re-check, exactly matching Condition B's faithful-baseline design. All 1,560 rows completed
  in 221.1s for a total OpenRouter cost of $0.076 (well under the $10 budget). A regex-based leakage detector flags surviving
  placeholder tokens, garbled tokens, and generic instruction-following artifacts (e.g. 'Corrected words:', 'Here is the revised...')
  in the repaired text, mirroring Padmanabhan's Appendix B failure modes; pooled leakage rate came out to 0.092 (9.2% of masked
  rows show leakage). For quality scoring, the plan called for Unbabel/wmt22-cometkiwi-da (organizer-footnoted scorer) with
  wmt22-comet-da as secondary fallback; both are gated HF Hub checkpoints. At execution time HuggingFace Hub returned a persistent,
  account-wide HTTP 429 on every download attempt for both checkpoints (confirmed via exponential-backoff retries against
  a 600s wall-clock budget for the primary and a 180s budget for the secondary -- 12 total attempts, all 429), so per the
  artifact's fallback plan the script cascaded to a documented non-COMET substitute: an LLM-judge 0-1 adequacy proxy (openai/gpt-4o-mini
  via OpenRouter, scored before/after the edit). This substitution is explicitly recorded in method_out.json's metadata.comet_substitution
  field with the reason, substitute name, and an explicit warning that the proxy's scale/calibration is NOT comparable to
  Padmanabhan's ΔCOMET. Under this substitute scorer, pooled mean delta (proxy quality after minus before) was -0.056, i.e.
  Condition B's masked-fill edit degrades quality on average, consistent in DIRECTION with the paper's ΔCOMET=-0.0108 finding
  but not directly comparable in magnitude since the metric itself differs. The gate_verdict is reported as PASS_UNRELIABLE_SUBSTITUTED_SCORER
  -- a three-way verdict (not a clean PASS/FAIL) that flags the reproduction as directionally consistent with the documented
  failure signature (negative quality delta + non-trivial leakage) but explicitly caveats that the magnitude comparison against
  the paper's -0.0108/-0.007..-0.014 published deltas cannot be trusted because the scorer itself was substituted. method_out.json
  also contains, per language pair, mean delta, leakage rate, n_spans_flagged/masked, and 5-10 verbatim example leaked outputs
  for qualitative inspection, plus the full published_comparison block and gate_component_results breakdown (direction/magnitude/leakage).
  This artifact's core deliverable for downstream use is the explicit, non-hidden caveat: any downstream artifact (Condition
  D/C1/C2/C) that relies on this fidelity check passing should treat the COMET-based magnitude claim as UNVERIFIED and should
  either retry the real COMET checkpoint when HF Hub throttling clears, or explicitly carry the same LLM-judge proxy forward
  for a fair (still-substituted-but-consistent) comparison rather than mixing a real-COMET result for one condition against
  this proxy-scored one.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_7Uc5PlFctjXi
type: experiment
in_dependencies:
- id: art_5ySTX4YfxqG_
  label: resource dossier
- id: art_mhfmDpGp4z1J
  label: dataset
title: Checker-Based Repair Beats Hygiene Retry Fixes
summary: |-
  Implements and scores three matched span-editing conditions on identical en-ru_RU/en-uk_UA rows from the WMT25 Task 3 dataset (art_mhfmDpGp4z1J), using google/gemma-3-12b-it (OpenRouter) as the fixed repair model, per gen_plan_experiment_3_idx3: B (faithful reproduction of Padmanabhan (2025)'s masked-fill severity-skip baseline: QE-flagged spans masked with __BLANK__, single uncorrected LLM call), D (B plus a trivial hygiene retry -- a second call, temperature=0.3, fires only if leftover placeholder/leaked-instruction text is detected), and C1 (a from-scratch 4-category deterministic content-invariant checker -- named entity via Stanza NER, number/unit/date via script-independent regex, negation polarity via per-language sentence-scoped cue lists with a negative-concord guard and a source-alignment deletion signal, quantifier scope via closed-class word lists -- flags every invariant in the FULL sentence and repairs them all in one uncorrected pass). The checker was validated on the dataset's injected_error_augmentation heldout fold (175 rows) via a conservative single-positive-per-row precision/recall metric; 3 of 8 (language, category) cells (ru_RU/uk_UA named_entity, uk_UA quantifier_scope) failed the recall/precision>=0.5 threshold and were excluded from C1's repair scope, documented in checker_validation.json.

  All three conditions ran on an identical stratified subsample: 320 natural rows (160/pair) scored for reference-free DeltaCOMET (Unbabel/wmt22-cometkiwi-da, real gated checkpoint successfully loaded, not a proxy) with 1000-iteration bootstrap 95% CIs, and 240 injected-pool rows (30/cell) scored for fix_rate (corrupted-span-string-absence) and a true_regression_rate (checker-detected invariants present in the wmt24pp clean reference that are newly missing post-repair, beyond what the corruption itself already removed). Total cost: $0.066 of the $10 OpenRouter budget (1,447 calls). Runtime: ~13 minutes on 1x RTX 2000 Ada GPU.

  Headline finding: condition B closely replicates Padmanabhan's direction and rough magnitude (pooled DeltaCOMET -0.0164, 95% CI [-0.0237, -0.0101], vs the paper's -0.0108 -- 1.5x magnitude, same sign, CI excludes 0), with a documented fidelity caveat that gemma-3-12b-it showed only 6.25% leakage on masked rows (19/304) versus the paper's model-native leakage failure mode. Condition D (hygiene retry) barely moves DeltaCOMET (-0.0157) and leaves fix_rate/true_regression_rate on the injected set IDENTICAL to B (0.7375 / 0.050) -- the hygiene retry essentially never fires usefully, so D does NOT close B's gap; this is evidence against 'it's just a leakage/regex bug'. Condition C1 (checker-broadened localization) cuts the COMET degradation roughly 5x versus B/D (pooled DeltaCOMET -0.0035, 95% CI [-0.0071, -0.0008] -- still excludes 0 but far smaller), at the cost of a substantially lower fix_rate (0.454 vs 0.738) and a higher true_regression_rate (0.125 vs 0.050) on the injected-pool subset. This pattern -- checking helps overall translation quality more than hygiene does, but at a real fix-rate and regression-rate cost -- is exactly the result the next iteration's verification-loop conditions (C2/C) are meant to investigate.

  Two protocol choices are documented explicitly in method_out.json metadata rather than left implicit: (1) injected rows carry no native QE signal, so B/D use an ORACLE QE span (the row's true corrupted-span offsets, computed correctly as start=dataset-offset-start, end=start+len(corrupted_span) since the dataset's own span_offsets are indexed into the pre-corruption clean text, not the corrupted output -- a real bug caught and fixed during testing) with severity='major', isolating repair-generation fidelity from localization quality, while C1 uses its own real checker-based localization on the same injected-pool rows; (2) negation_polarity_flip corruptions are deletions (corrupted_span=''), so the oracle span is zero-width and B/D structurally never attempt a repair on any negation row in the injected-pool subset (fix_rate=0 there is a known artifact of the masking design applied to deletions, not evidence of failure).

  Deliverables: method.py (main script), checker.py (4-category checker module), llm_client.py (async OpenRouter client with a live cost ledger), method_out.json/full_method_out.json (identical, schema-validated against exp_gen_sol_out) + mini/preview variants, checker_validation.json, selected_rows.json (exact row ids for reproducibility), pyproject.toml (pinned deps).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_3
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_qUG1DIUZKEBQ
type: evaluation
in_dependencies:
- id: art_mhfmDpGp4z1J
  label: dataset
title: Does Hygiene or Verification Fix Editing?
summary: >-
  Implements the full evaluation pipeline specified in the artifact plan for the hypothesis 'Does Hygiene or Verification
  Fix Editing?': paired bootstrap 95%-CI ΔCOMET (B-D, C1-D, C1-B, both paired-difference and marginal-mean forms), Wilson
  and Clopper-Pearson binomial CIs for true (ground-truth-confirmed) regression rate and fix rate (both all-flagged and ground-truth-confirmed
  variants) per condition, an edit-volume-to-gain ratio (mean edited-character-fraction / mean ΔCOMET gain) for D and C1,
  a pre-registered checker-precision/recall-gated sensitivity re-analysis (0.6 threshold, zh_CN/ja_JP named-entity flagged
  in advance), and a six-language-pair ΔCOMET/GER reconciliation table. At evaluation time, this iteration's three sibling
  B/D/C1 experiment sessions (gen_art_experiment_1/2/3) were still actively running (growing terminal-session logs, no result
  files written yet) and produced no checker_validation*.json, condition_b_fidelity*.json, or b_d_c1_results*.json outputs,
  so eval.py's discovery step correctly found nothing usable and every affected metric degrades explicitly to NOT_AVAILABLE
  with a stated reason and the exact search paths tried, per the plan's graceful-degradation requirement -- no placeholder
  numbers were fabricated anywhere. The condition-B fidelity-gate verdict is surfaced as a first-class metadata field (condition_b_fidelity_gate_verdict
  = NOT_AVAILABLE) with a top-level caveat explaining that every B/D/C1 comparison is conditional on it. The six-language-pair
  reconciliation table's quoted column is populated with real, verbatim SURREYPAI-S2 and BASELINE-S2 per-language-pair ΔCOMET/GER
  figures freshly extracted from WMT25 findings-paper Table 15 (fetched and regex-grepped from the primary PDF, not copied
  from a prior summary that omitted the full breakdown); its measured column is NOT_AVAILABLE pending the sibling experiments.
  A real, non-fabricated descriptive statistic is also reported from the dataset dependency alone: per-(language_pair, invariant_category)
  row counts in the checker_validation_heldout fold, including the pre-registered zh_CN/ja_JP named-entity-swap cell counts,
  clearly labeled as composition data rather than a precision/recall measurement. All statistics primitives (bootstrap paired
  CI, Wilson CI, Clopper-Pearson CI, sensitivity re-analysis, edit-volume-to-gain ratio) were validated two ways: an in-script
  self-test on synthetic fixtures (logged, never written into eval_out.json's reported metrics) and a separate integration
  check against a hand-built fixture file mimicking the real b_d_c1_results schema, confirming every 'if real data existed'
  code path produces correct, sensible numbers. eval_out.json validates against the exp_eval_sol_out schema. The evaluation
  script re-scans for sibling outputs on every run (glob-based discovery pruning .venv/.git/node_modules so it stays fast
  even while sibling experiments are mid-install) and should simply be re-run once the B/D/C1 experiments finish, at which
  point every NOT_AVAILABLE field will populate with real paired statistics automatically -- no code changes needed.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Machine translation systems increasingly ship with an automatic quality-estimation (QE) step that flags likely errors in a translation without needing a human reference [1]. The natural next question is whether those flags can drive automatic repair: instead of retranslating a whole sentence to fix one wrong number or dropped negation, an editing system could touch only the flagged span and leave the rest of the sentence -- which the base translator already got right -- untouched. This is *scoped editing*: localize a problem with QE, then repair only that region. Scoped editing matters because a system that regenerates an entire sentence can silently break a correct number, name, or negation while fixing something else, and the total-sentence quality metrics used to score MT systems do not distinguish "improved and stayed faithful" from "improved by chance while corrupting a different part of the sentence" [2]. In a regulated, terminology-heavy domain -- legal, medical, financial translation -- a single flipped number or negation is a severe, auditable failure independent of whether the sentence's aggregate quality score went up.

The 2025 WMT shared task on automated translation evaluation (Task 3, minimal editing) gave scoped editing its first head-to-head test against full retranslation, scored the same way across eight ranked systems [3]. A scoped-editing system that masks each QE-flagged span with a placeholder token and fills it with one pass of a small (9-billion-parameter) language model finished dead last, at $-0.0108$ mean $\Delta$COMET, while the same team's sibling system -- which retranslates the whole sentence with six candidate large language models and keeps the QE-best one -- scored $+0.0201$ [4]. Read alone, this looks like a clean argument against scoped editing. It does not survive reading the losing system's own account of itself: the paper documents a literal, unfilled placeholder token surviving into the output as garbled text, bracketed prompt-format instructions leaking into the translated string, a single 9-billion-parameter repair model chosen for this system alone against a six-model pool for its sibling, and a severity heuristic that silently skips minor-severity spans whenever a more severe span is present in the same sentence [4]. None of these are failures of scoped editing as a strategy. And the same ranking contains a second, independently built scoped-editing system -- an organizer baseline pairing fine-grained error detection with a 27-billion-parameter correction model -- that lands third with near-zero, mixed $\Delta$COMET, not the first system's consistent negative range [3]. Two systems attempting the same strategy on the same data landed in opposite territory, and the field's headline negative result on scoped editing is confounded with model capability and implementation hygiene in a way no prior study isolates: existing QE-assisted post-editing work always regenerates the full sentence rather than freezing untouched spans [5,6], and no post-editing study matches a fixed repair model across a design that separately varies how much of the sentence gets checked and whether a repair is iteratively re-verified [7,8].

Naming the confound is a diagnosis, not a fix. The previous iteration of this project treated a comparison of three published numbers -- two systems from one paper, one language pair fully comparable across all three -- as evidence that model capability and hygiene, not scoped editing itself, explain the field's negative result, and left the actual question -- what specifically closes the gap -- as future work. A reviewer of that draft correctly identified this as thin: three numbers with no confidence intervals, drawn overwhelmingly from a single paper's self-report, is not enough to hang a paper's argument on, and a paper whose headline method has zero of its own conditions executed is a protocol description, not a result. This iteration answers both objections directly. We built the full six-language-pair reconciliation the prior draft lacked, quantified how thin the original three-point comparison actually was, and -- for the first time in this project -- ran a controlled comparison ourselves: a faithful reproduction of the losing system (Condition B), a hygiene-only variant that fixes nothing but output artifacts (Condition D), and a broadened-localization variant that checks every content invariant in the sentence rather than only the one QE flagged it (Condition C1), on identical rows, with one fixed repair model, and with the real reference-free COMET checkpoint the shared task itself uses.

The result is not the mechanism story the design was originally built to test -- iterative verification versus broadened localization -- because the iterative-verification conditions (C2, C) have not yet run. But what did run answers a narrower, still load-bearing question, and the answer is not what a reader of the prior diagnosis would expect. Hygiene does not close the gap: Condition D's mean $\Delta$COMET ($-0.0157$, pooled over two language pairs) is statistically indistinguishable from Condition B's faithful reproduction ($-0.0164$), and every downstream repair-quality metric is identical between them, ruling out "it was just a leftover-placeholder bug" as the explanation. Broadened localization, on its own, with no re-verification at all, is not the null result the design anticipated for it: Condition C1's mean $\Delta$COMET is $-0.0035$, a roughly fivefold reduction in the translation-quality cost of scoped editing relative to B and D, and on one of the two language pairs the 95% CI crosses zero -- a qualitatively different outcome from B and D's consistently negative intervals. That gain is not free: C1's fix rate on the injected-error set it was scored against drops from 0.74 to 0.45, and its true (ground-truth-confirmed) regression rate rises from 0.05 to 0.13, a pattern the paper reports honestly as a genuine quality-versus-correctness trade-off rather than an unqualified win.

[FIGURE:fig1]

**Summary of contributions.**

- A resolved, six-language-pair reconciliation of the WMT25 Task 3 evidence this project's argument rests on, replacing the prior draft's three-point comparison with the full published record for both relevant systems and an explicit accounting of how little of that record has confidence intervals or independent replication (Section 5).
- The first executed conditions of the project's own five-condition protocol: a faithful reproduction of the losing shared-task system (Condition B) scored with the real reference-free COMET checkpoint, a hygiene-only control (Condition D), and a broadened-localization, single-pass repair condition (Condition C1), run on 320 natural WMT25 sentences and 240 injected-error sentences across two language pairs with one repair model held fixed across all three (Section 6).
- Direct evidence that a trivial output-hygiene fix explains none of the losing system's gap, while broadening what a deterministic checker is allowed to flag -- with no iterative re-verification at all -- explains most of it in $\Delta$COMET terms, at a measured cost in fix rate and true regression rate that the iteration-based conditions this protocol was designed to test may or may not resolve (Section 6, Section 7).
- A validated four-category content-invariant checker, with per-language, per-category precision and recall reported against a held-out ground-truth split rather than assumed: negation-polarity detection is the strongest category, clearing a usability threshold in five of six languages, while named-entity detection for Chinese and Japanese is confirmed, not merely anticipated, to fail that threshold -- and this specific coverage gap is traced to which categories Condition C1 could and could not repair (Section 6.1).
- An honest accounting of what remains open: the iterative-verification conditions (C2, C) that would isolate whether re-checking a repair is what matters, versus broadened one-pass checking alone, have not been run, and Section 7 states exactly what would confirm or overturn the current reading once they are.

# Related Work

**Quality-estimation-informed post-editing.** Automatic post-editing systems that use word-level QE as a training signal jointly train an encoder-decoder that regenerates the full target sentence in every variant; adding the QE signal reduces over-correction (18.30 vs. 19.39 TER) but never freezes a QE-clean span, so the model can still rewrite text no error was ever flagged in [5]. A later system replaces the auxiliary-signal approach with Grid Beam Search, forcing QE-tagged "OK" spans as lexical constraints while the decoder keeps freedom to reorder and rephrase around them; this is closer to scoped editing in spirit but is a soft constraint on regeneration rather than a frozen, iteratively verified span, and the paper's own oracle-versus-predicted-tag gap of 0.3-1.3 TER shows the method's ceiling is set by QE tag accuracy without ever isolating that dependency as a separate factor [6]. Prompting large language models directly with structured error annotations improves post-editing outcomes over unstructured feedback, but every condition in that study still regenerates the sentence and none tests a repair-then-verify loop against a single-pass repair with the same signal [7]. A related line automatically predicts MQM-style error spans and post-edits with them inside an LLM-as-judge evaluation pipeline, again as a one-shot correction step rather than an iterated one [10]. A third WMT25 Task 3 submission takes yet another route to the same problem: it generates a natural-language explanation of each QE-flagged error with the xTower explanation model, then hands that explanation, rather than the raw error span, to a large language model (Gemini 1.5 Pro) as the correction prompt [28]. That system reports only absolute COMET, BLEU, and TER on its own held-out test predictions, not the shared task's $\Delta$COMET ranking metric, so it cannot be placed in Table 1's reconciliation, but it is a third independent design choice in the same task -- explanation-mediated correction rather than masked-fill or fine-grained-detector correction -- and, like every system reviewed here, it regenerates the flagged segment in a single pass with no re-verification step. Our Condition C1 result -- broadened localization alone, held fixed against the same repair model as the faithful baseline, cutting $\Delta$COMET degradation roughly fivefold -- is, to our knowledge, the first controlled evidence in this literature that separates "check more of the sentence" from "use a better model or a fancier decoding constraint" as an explanation for a scoped-editing system's quality gain.

**Localized and energy-guided editing.** Locate-and-edit approaches to controlled text generation obtain a full generation from a base model, then use an energy function to find and replace only the spans that violate a stated constraint, explicitly to avoid the semantic drift full regeneration under a constraint tends to introduce [11]. This is the closest existing mechanism to the localization half of our design, but it has not been applied to machine translation and has not been evaluated against a documented real-world failure of naive scoped editing with localization breadth held apart from other design choices as a single controlled factor.

**Iterative self-refinement.** Self-Refine shows that a single language model can generate an output, critique its own output, and revise it over several rounds without external supervision, improving results on tasks from code optimization to dialogue response generation [8]. The mechanism our protocol's still-unrun conditions (C2, C) are built to test -- iterate a repair against a check until it passes -- is structurally related, but Self-Refine's critique step is the same model judging its own work, which is known to be an unreliable verifier of the model's own errors; our design instead iterates against a deterministic, non-learned checker precisely to avoid that confound. This iteration's contribution to that comparison is narrower than the full mechanism question: it establishes that the checker itself, used only to broaden what gets flagged rather than to re-verify anything, already moves the outcome substantially, which sets the baseline any iterative-verification result must beat to be credited as doing additional work.

**Counterexample-guided synthesis.** Counterexample-Guided Inductive Synthesis (CEGIS) is a synthesis loop in which a candidate is checked against a specification by a verifier that either certifies it or returns a concrete counterexample scoping the next candidate, terminating on an explicit certificate rather than a fixed budget [9]. We do not claim to import CEGIS as a synthesis algorithm, and we are explicit that the parallel is looser than it may first appear: our checker's "counterexample" is a flagged span, not a candidate-generalizing constraint, and nothing in our design performs unrealizability reasoning or generalizes across counterexamples the way a synthesis loop does. What we borrow is narrower and more defensible -- the separation of concerns between what a verifier is allowed to see (localization breadth) and whether the loop is allowed to run more than once (iteration) -- as the factorial structure of a verify-and-retry protocol whose relationship to CEGIS is one of inspiration, not instantiation; the closer methodological kin for the mechanism this paper actually tests are the iterative-refinement and locate-and-edit lines above.

**Evaluation infrastructure.** All $\Delta$COMET figures in this paper and in the shared task we build on are computed with the same reference-free quality-estimation checkpoint, `wmt22-cometkiwi-da` [2], distinct in both purpose and license from the neural framework it descends from [1] and from the fine-grained error-detection model, xCOMET, that a subsequent quality-estimation shared task and one Task 3 baseline use as an input signal rather than a scoring metric [12,13]. Our natural-error data is WMT25 Task 3's released test set [3]; our injected-error data is built from WMT24++, a disjoint, human-post-edited multilingual corpus spanning 55 languages and dialects [14].

# Preliminaries

We define four terms used throughout the protocol.

A **content invariant** is a piece of source-sentence meaning -- a named entity, a number, unit, or date, a negation polarity marker, or a quantifier -- that must survive translation, and that can be checked deterministically (via named-entity recognition, regular expressions, cue-word lists, or alignment) rather than judged by a learned model. We check four invariant categories: entity identity, number/unit/date value, negation polarity, and quantifier scope.

A translation's **certificate** is the state in which every content invariant extracted from its source sentence has been checked and passes. A certificate is an explicit, auditable stopping condition, produced only by the still-unrun iterative-verification conditions (C2, C); the conditions executed this iteration (B, D, C1) never produce one, since none of them re-checks a repair after making it.

**Localization breadth** is how much of the sentence a system is allowed to flag as needing repair. *Narrow* localization repairs only the span the original quality-estimation model flagged (Conditions B and D); *broad* localization repairs every invariant our checker finds violated, whether or not quality estimation flagged it (Condition C1, and the planned C1's iterative counterpart C).

**Iteration** is whether a flagged span, once repaired, is re-checked and re-repaired if it still fails, up to a fixed pass budget, or whether the system accepts a single repair pass unconditionally. Every condition executed this iteration uses a single, uncorrected pass; iteration remains untested.

# Method

## Design Rationale

Our method isolates localization from verification by construction. The shared-task contrast in Section 1 leaves two explanations for the losing system's failure open at once: it could be that scoped editing without any re-verification is fundamentally worse than full retranslation, or it could be that a small, buggy, single-pass repair model was simply going to fail regardless of what strategy wrapped it. A protocol that changes both the localization scope and the presence of iteration at the same time as it changes the repair model -- as the shared task's two natural systems effectively do -- cannot separate these. Our protocol removes the confound in two steps: it fixes the repair model identically across every condition that performs a repair, and it varies localization breadth and iteration as two independently switchable factors rather than one bundled "use the improved system" toggle.

## Five Conditions, Three Executed

All five conditions share one deterministic content-invariant checker (Section 6.1) and, in every condition that performs a language-model repair, one fixed repair model, `google/gemma-3-12b-it` (Section 4.4). This iteration executes Conditions B, D, and C1; Conditions C2 and C -- the two conditions that isolate iterative verification -- are specified but not yet run, and every claim below is scoped accordingly.

**Condition B (faithful baseline, executed).** A reproduction of the original masked-fill system: the quality-estimation model's flagged span is masked with a placeholder token according to the paper's severity-conditioned masking rule (mask nothing above a 0.90 QE score; mask only major-severity spans, or all spans if only minor-severity ones exist, between 0.50 and 0.90; mask everything below 0.50), filled with one repair-model pass, and accepted without any check [4]. Its purpose in this iteration is twofold: it reproduces the original failure mode as a fidelity check on the substitute repair model (Section 6.2), and it anchors the two comparison conditions below.

**Condition D (hygiene filter, no checker, executed).** Condition B, plus a trivial post-hoc filter that detects and retries -- within the same single-pass budget -- any output containing a leftover mask token, garbled placeholder text, or leaked instruction-format text. No content-invariant checker is involved. This condition measures how much of Condition B's gap to full retranslation basic output hygiene alone closes, before any credit goes to a more sophisticated mechanism.

**Condition C1 (broad localization, single pass, executed).** The checker flags every invariant violation in the sentence, not only the original quality-estimation span; each flagged violation is repaired in one uncorrected pass, with no re-verification. This condition isolates the effect of broadening what gets checked while holding iteration fixed at "none." Per-category repair scope is gated by the checker's own validated precision and recall (Section 6.1): a (language, category) cell whose recall or precision falls below 0.5 on the held-out validation split is excluded from C1's repair scope for that cell, and the exclusions are recorded rather than silently absorbed into the headline numbers.

**Condition C2 (narrow localization, iterative verification, not yet run).** Localization stays restricted to the original quality-estimation-flagged span, but that span is repaired, re-checked by the checker, and re-repaired if it still fails, up to the shared pass budget, stopping on a certificate. This condition is designed to isolate the effect of iteration while holding localization fixed at "narrow" -- the comparison this paper's original design most wanted to run, and has not yet run.

**Condition C (broad localization, iterative verification, not yet run).** Both changes combined: every checker-flagged invariant is repaired and re-verified to a certificate or budget exhaustion.

A severity-matched variant of C1, C2, and C additionally respects Condition B's minor-severity-skip rule. Its purpose is to isolate two distinct explanations for any gain broadened localization shows: covering minor-severity spans that B's own heuristic deliberately skips (a difference in which spans get attempted at all, orthogonal to the checker mechanism) versus genuinely broader content-invariant coverage that B's design would still miss even without the severity-skip rule (a difference attributable to the checker itself). Comparing C1 against its severity-matched counterpart isolates the first effect; comparing the severity-matched counterpart against B isolates the second. This variant is specified in the protocol but was not run this iteration alongside C1.

## Metrics

For each executed condition, the protocol measures, matching the shared task's own reporting where possible for direct comparability to its $-0.0108$ and $+0.0201$ figures: (i) fix rate on the four checkable categories, scored against the human-confirmed injected-error subset; (ii) true regression rate, the fraction of invariants correct before repair that a repair step breaks, scored only against ground-truth-confirmed cases so the metric is not inflated by the checker's own false positives; (iii) mean $\Delta$COMET using the same checkpoint the shared task used [2]; (iv) edit volume, the mean fraction of the sentence's characters touched by a repair, to check that broadened localization does not degenerate into full-sentence regeneration; and (v) language-model calls per sentence, since C2 and C (once run) multiply calls relative to B, D, and C1.

## Repair-Model Resolution

The original system's repair model, a 9-billion-parameter machine-translation-tuned language model built on a Gemma-2 base, is required to be identical across every repair-performing condition so that no measured difference can be attributed to model capability rather than protocol design. Confirming this model's continued availability through the third-party hosting route the original plan assumed took three independent checks [ARTIFACT:art_5ySTX4YfxqG_]: a full regular-expression sweep of that route's live model catalog (over 700,000 characters of listing text) returned zero matches for the model or its publisher; the model's own hosting page listed no active serving provider; and a targeted search of major inference hosts found no listing anywhere. A second, independent check found that the specific same-base substitute the original plan had assumed was still available (`google/gemma-2-9b-it`) had also since been delisted from the same catalog. We resolve this with a documented substitution to `google/gemma-3-12b-it`, a same-lineage, similarly-sized instruction-tuned model with confirmed live pricing and context length, recording as an explicit limitation that the substitute lacks the original model's machine-translation-specific fine-tuning.

Because a substitute with no MT-specific fine-tuning is a genuine threat to the eventual comparison's validity -- it could give the entire fixed-model design a different capability floor than the original system, undermining every condition at once rather than just Condition B -- we did not treat this substitution as adequate on its own. We required Condition B, run with the substitute, to reproduce the original system's qualitative failure signature (negative $\Delta$COMET, same order of magnitude, non-trivial leakage) before trusting any comparison built on top of it. Section 6.2 reports that this fidelity check passed.

# Data

## Natural Errors: WMT25 Task 3

We use the complete WMT25 Task 3 combined test set: 6,000 translations, 1,000 for each of six English-source language pairs (Chinese, Czech, Icelandic, Japanese, Russian, Ukrainian), spanning five domains -- news (1,808 rows), social media (1,684), speech (1,416), literary text (1,064), and dialogue (28) [ARTIFACT:art_mhfmDpGp4z1J]. Every row carries the quality-estimation model's flagged error spans as released with the test set: character offsets and a severity label in \{minor, major, critical\}. 5,700 of the 6,000 rows carry at least one flagged span; across all flagged spans, 45,611 are labeled major, 14,741 critical, and 1,336 minor -- only 2.2% of all flagged spans, so Condition B's rule of skipping minor spans whenever a more severe span co-occurs affects a small but not negligible fraction of the data.

We searched for a post-hoc human-annotated error-type layer to use as scoring ground truth beyond the released quality-estimation flags and did not find one publicly available for this test set; the release's designated field for this is empty across all 6,000 rows. We considered whether MQM-annotated segments from prior WMT General MT shared tasks might substitute, but those campaigns annotate different, earlier-year test segments for the general translation task rather than Task 3's own 2025 test sentences, so there is no row-level overlap to exploit; we did not attempt to build a proxy from non-overlapping segments and instead record this as an open gap rather than papering over it with mismatched data. We use the released quality-estimation flags the same way the original system did -- as the operational localization signal -- but score true regression rate only where a ground-truth check is possible, which the natural-error subset alone cannot fully provide.

## Injected Errors: A Controlled Complement

Because natural incidence of any single invariant category can be low and because natural rows have no ground truth for the checker itself, we built a controlled complement from WMT24++, a corpus of human post-edited translations across 55 languages and dialects that is wholly disjoint from WMT25 Task 3 in both source year and content [14]. We took clean, human-authored target text for the same six language pairs and programmatically corrupted it into one of four invariant categories: named-entity swap, number/unit/date alteration, negation polarity flip, and quantifier substitution, producing 2,519 rows balanced up to 130 per language-pair-by-category cell (negation flips: 724 rows; entity swaps: 656; number/unit/date alterations: 651; quantifier substitutions: 488) [ARTIFACT:art_mhfmDpGp4z1J]. Each injected row carries the pre-corruption clean text, the corrupted text, and the exact character span of the change, so a checker's precision and recall against a known answer is computable directly rather than estimated.

Category construction used language-appropriate methods rather than one rule applied uniformly. Negation and quantifier corruptions use per-language cue-word lists and only fire when a sentence contains exactly one negation marker, since several target languages permit multiple co-occurring negation markers (negative concord), where removing one does not reliably flip the sentence's polarity. Entity detection for the four space-delimited, capitalization-marking languages (Czech, Icelandic, Russian, Ukrainian) uses a capitalization heuristic filtered by a per-language function-word stoplist, a sentence-boundary exclusion, and a corpus-frequency cap. Chinese and Japanese carry no capitalization signal at all, so entity corruption there is restricted to embedded Latin-script substrings -- a limitation of the dataset's own construction, not of the checker built to detect it, and one that turns out to matter directly for the checker validation results in Section 6.1.

Both dataset groups are split by language pair (and, for the injected set, by language pair and category) into an experimental pool (4,920 of 6,000 natural rows, 2,071 of 2,519 injected rows -- roughly 82% of each) and a checker-validation holdout (1,080 natural, 448 injected -- roughly 18% of each), kept strictly disjoint so that validating the checker's precision and recall never draws on the same rows used for the B/D/C1 comparison.

[FIGURE:fig2]

Figure 2 summarizes this composition: 6,000 natural WMT25 Task 3 rows across six language pairs and five domains, and 2,519 injected-error rows across the same six language pairs and four invariant categories, including the two smallest injected cells (Japanese number/unit/date alterations at 18 rows and Japanese named-entity swaps at 55 rows), both below the 130-row target for reasons the dataset's own metadata documents (no capitalization signal to drive the entity heuristic, and a genuinely lower numeral count in the source corpus for that pair) rather than a rebalanced total that conceals the gap.

## Scoring Infrastructure

$\Delta$COMET throughout this protocol is computed with `wmt22-cometkiwi-da`, the same checkpoint the shared task's organizers footnote as the exact scorer behind every entry in its results table [2,3] [ARTIFACT:art_5ySTX4YfxqG_]. Section 6.2's fidelity check and Section 6.3's B/D/C1 comparison both obtain the real checkpoint successfully -- an earlier attempt within this project hit a persistent, account-wide HTTP 429 from HuggingFace Hub on every download attempt for this checkpoint and its fallback, and cascaded to a non-comparable LLM-judge proxy as a documented substitute; the throttling had cleared by the time the B/D/C1 comparison ran, and every $\Delta$COMET figure reported from Section 6.2 onward in this paper uses the real checkpoint, not the proxy. We flag this explicitly because the two runs are not interchangeable: any number in this paper attributed to the proxy scorer is labeled as such and never mixed with a real-COMET figure in the same comparison.

# Results

This iteration executes three of the protocol's five conditions -- B, D, and C1, on 320 natural rows and 240 injected-pool rows spanning two language pairs, en-ru\_RU and en-uk\_UA -- and validates the checker they depend on. Conditions C2 and C, which would isolate iterative verification as a distinct mechanism from broadened localization, have not been run; every result below concerns the question "does broadening what gets checked help, holding the repair model and the number of repair passes fixed," not the fuller question of whether iteration adds anything beyond that.

## Checker Validation

The four-category content-invariant checker (named entity via Stanza NER with a capitalization-heuristic fallback for Czech and Icelandic, number/unit/date via a script-independent regex parser, negation polarity via cross-lingual cue-presence matching, and quantifier scope via closed-class word-list matching) was scored against 448 injected and 1,080 natural rows in the checker-validation holdout, across all six languages and four categories, against a language-naive baseline checker (Latin-only capitalization regex, bare-digit number regex, no negation or quantifier resource) run on the identical rows [ARTIFACT:art_QLpPxaqf1VzK].

Recall was strong for our checker in 20 of 24 (language, category) cells ($\geq 0.7$), but the natural-row precision proxy -- computed against sparse QE-flagged spans, where every other genuine invariant the checker correctly flags in the same sentence counts as a false positive -- is noisy enough that only 6 of 24 cells clear both the recall and precision usability threshold of 0.5. Negation-polarity detection is the strongest headline result: it clears the bar in five of six languages, with recall ranging 0.57-0.92 and precision 0.75-0.89, where the language-naive baseline scores exactly 0.0 recall (it has no negation resource at all). The sixth language, Chinese, fails on recall alone (0.35), just below threshold. Number/unit/date detection clears the bar for Chinese (recall 1.0, precision 0.59); no other category-language cell besides negation and this one clears both thresholds.

[FIGURE:fig3]

An unexpected but honestly-reported finding concerns named-entity detection for Chinese and Japanese specifically: the language-naive baseline's crude Latin-capitalization regex actually beats our Stanza-NER checker on recall for these two languages, because the injected dataset's own construction restricts entity corruptions on scripts with no capitalization signal to embedded Latin-script substrings (Section 5.2) -- a property of how the ground truth was built, not evidence that NER underperforms regex in general. This is a scope-boundary finding we carry forward directly: it is the reason Condition C1, below, excludes named-entity repair for Russian and Ukrainian and quantifier-scope repair for Ukrainian from its checker-validated repair scope, using a separate, stricter within-experiment validation on the two language pairs it actually ran on (Section 6.3).

## Condition-B Fidelity: The Substitute Model Reproduces the Original Failure

Before trusting any B/D/C1 comparison built on the substitute repair model, we required Condition B, run with `google/gemma-3-12b-it` in place of the unavailable original model, to reproduce Padmanabhan (2025)'s documented failure signature. Two independent checks both pass. First, an earlier fidelity run on a larger, six-hundred-fold sample of Chinese and Czech rows (1,560 rows, $221.1$s runtime, \$0.076) reproduced the qualitative signature -- non-trivial leakage (9.2% of masked rows showed leftover placeholder or leaked instruction text, versus the original paper's model-native leakage failure mode) and a negative quality delta under a substitute LLM-judge proxy scorer (mean $-0.056$) -- while explicitly flagging that the proxy scale is not comparable to $\Delta$COMET [ARTIFACT:art_G9ppuk8aHUhW]. Second, and decisively, the B/D/C1 comparison below obtained the real `wmt22-cometkiwi-da` checkpoint successfully: pooled over both language pairs, Condition B's mean $\Delta$COMET is $-0.0164$ (95% CI $[-0.0237, -0.0101]$), the same direction as Padmanabhan's reported $-0.0108$ and 1.5$\times$ its magnitude, with a CI that excludes zero [ARTIFACT:art_7Uc5PlFctjXi]. The substitute model's own leakage rate under this comparison's masking prompt was low, 6.25% (19 of 304 masked rows) -- lower than the original paper's own failure mode, which is expected, since the original result is attributed largely to prompt-following failure specific to the smaller, non-instruction-tuned original model, and a modern instruction-tuned substitute reproduces the direction and rough scale of the quality cost without reproducing every underlying bug. Both checks point the same way: the fixed-model design's capability floor is close enough to the original system's to support the comparison that follows, with the caveat -- carried forward explicitly, not dropped -- that the substitute still lacks machine-translation-specific fine-tuning.

## The B/D/C1 Comparison

[FIGURE:fig4]

Condition D (hygiene filter) does not close Condition B's gap. Pooled over en-ru\_RU and en-uk\_UA, D's mean $\Delta$COMET is $-0.0157$ (95% CI $[-0.0226, -0.0097]$), statistically indistinguishable from B's $-0.0164$, and every downstream metric on the injected-pool subsample is identical between the two conditions: fix rate 0.7375 and true regression rate 0.050 in both. The hygiene retry essentially never fires usefully in this run -- most rows scored by D never trigger the leakage detector that would prompt a retry -- so basic output hygiene is not the explanation for the losing system's gap, ruling out the cheapest possible account of the shared-task result.

Condition C1 (broadened localization, single uncorrected pass) tells a different story. Pooled $\Delta$COMET is $-0.0035$ (95% CI $[-0.0071, -0.0008]$), roughly a fivefold reduction in magnitude relative to B and D, and the CI still excludes zero but is far tighter around it. Broken out by language pair, the effect is stronger for en-uk\_UA than en-ru\_RU: C1's en-uk\_UA $\Delta$COMET is $-0.0008$ with a 95% CI of $[-0.0019, +0.0004]$ -- the only condition-and-pair combination in this comparison whose interval includes zero -- against B's $-0.0151$ and D's $-0.0134$ on the same pair. En-ru\_RU's C1 result is smaller in magnitude but still clearly negative ($-0.0063$, CI $[-0.0133, -0.0011]$).

That gain does not come free. On the injected-pool subsample, C1's fix rate drops to 0.4542 from B/D's 0.7375, and its true regression rate rises to 0.125 from 0.050. Part of this drop is a direct, traceable consequence of the checker-coverage gap documented in Section 6.1: three of the eight (language, category) cells evaluated within this run's own checker-validation split failed the recall/precision usability threshold (Russian and Ukrainian named-entity, and Ukrainian quantifier scope) and were excluded from C1's repair scope entirely, meaning C1 structurally cannot fix injected errors in those categories no matter how well it performs elsewhere. C1 also edits substantially less of each sentence than B or D despite this broader flagging in principle: mean edit volume is 0.021 for C1 (0.030 en-ru\_RU, 0.012 en-uk\_UA) versus 0.146 pooled for B and D (0.147 and 0.145 respectively), so the localization the checker performs is genuinely narrower per repair event, not a route to full-sentence regeneration under a different name. Language-model call counts stay close across all three conditions (0.80-1.01 calls per sentence), so C1's quality gain is not bought with substantially more inference.

[FIGURE:fig5]

## The Six-Language-Pair Reconciliation

The previous iteration of this project argued its central diagnosis from three published numbers -- SURREYPAI-S2's pooled $-0.0108$, its sibling SURREYPAI-S1's $+0.0201$, and the organizer baseline BASELINE-S2's per-pair figures on exactly the three language pairs where its own report gives a directly comparable value. A reviewer correctly flagged this as thin: two of the three points share an author, none carries a confidence interval, and only one language pair (English-Czech) had all three systems reported side by side. Table 1 replaces that partial comparison with the complete per-language-pair record for both scoped-editing systems, extracted verbatim from the WMT25 findings paper's Table 15 across all six language pairs [3] [ARTIFACT:art_qUG1DIUZKEBQ].

| Language pair | SURREYPAI-S2 $\Delta$COMET | SURREYPAI-S2 GER | BASELINE-S2 $\Delta$COMET | BASELINE-S2 GER |
|---|---|---|---|---|
| en-cs\_CZ | $-0.007$ | $-0.005$ | $0.000$ | $0.000$ |
| en-is\_IS | $-0.010$ | $-0.006$ | $+0.007$ | $+0.026$ |
| en-ja\_JP | $-0.013$ | $-0.008$ | $-0.008$ | $-0.036$ |
| en-ru\_RU | $-0.008$ | $-0.005$ | $+0.002$ | $+0.009$ |
| en-uk\_UA | $-0.014$ | $-0.009$ | $+0.004$ | $+0.017$ |
| en-zh\_CN | $-0.013$ | $-0.010$ | $-0.005$ | $-0.023$ |

*Table 1: Verbatim per-language-pair $\Delta$COMET and general-error-rate (GER) figures for the two Task 3 scoped-editing systems, from the WMT25 findings paper's Table 15 [3], reproduced in full rather than the three-pair subset the prior iteration relied on.*

The complete table both strengthens and complicates the prior diagnosis. It strengthens it in breadth: SURREYPAI-S2 is negative on all six pairs, while BASELINE-S2 is negative on only two (English-Japanese, English-Chinese) and non-negative on the other four -- a pattern visible across the full language coverage, not an artifact of which three pairs happened to be directly comparable. It complicates the diagnosis in magnitude: on English-Japanese and English-Chinese, BASELINE-S2's own $\Delta$COMET is negative too ($-0.008$ and $-0.005$), meaning the stronger-model system does not uniformly clear break-even -- capability and hygiene explain most, not all, of the gap between the two systems, and the two pairs where BASELINE-S2 also struggles are worth flagging for whatever follow-on work extends this comparison to those languages. Neither published figure carries a confidence interval or a stated sample-level variance, so Table 1 remains what it always was -- two systems' self-reported means -- and the honest reading is that it motivates the controlled comparison in Section 6.3 rather than substituting for it. What Section 6.3 adds that Table 1 alone cannot is a matched-repair-model result: our own Condition B, run under the same real COMET checkpoint on two of these six pairs, reproduces SURREYPAI-S2's negative direction and rough magnitude ($-0.0177$ en-ru\_RU, $-0.0151$ en-uk\_UA, against the paper's $-0.008$ and $-0.014$ on the same pairs), giving this project's own diagnosis a fourth, independently measured data point rather than resting entirely on the two systems' self-reports.

# Discussion

**What this iteration establishes, and what it does not.** Three findings are now measured, not quoted: hygiene alone does not explain the losing shared-task system's gap; broadened localization, on its own and with no re-verification, closes most of that gap in $\Delta$COMET terms while costing measurable ground on fix rate and true regression rate; and the substitute repair model this protocol depends on reproduces the original system's qualitative failure closely enough to support the comparison built on it. What remains unmeasured is the question the protocol's design was originally built around: whether iterating a repair against a deterministic check (Conditions C2 and C) does anything beyond what broadened one-pass checking already does. C1's own trade-off -- better aggregate quality, worse targeted fix rate and higher true regression rate -- is exactly the pattern that would make an iteration loop valuable if it exists: a system that catches C1's own regressions by re-checking after each repair could plausibly keep C1's quality gain while recovering some of its fix-rate loss. That is a specific, falsifiable prediction for Condition C2 to test, not a claim we are making about it in advance.

**Why the fivefold reduction is smaller than it looks.** $\Delta$COMET is a whole-sentence, reference-free quality metric; a checker that flags more of the sentence but repairs each flagged span with a single pass from the same weak repair model is, in effect, betting that more targeted, smaller edits (mean edit volume 0.021 versus B/D's 0.146) degrade the sentence less on average than fewer, larger masked-and-refilled edits do, even when some of those smaller edits are wrong. The result is consistent with that bet paying off in aggregate quality while not paying off in whether the specific error the checker was built to catch actually gets fixed. Both readings are true at once, and reporting only the $\Delta$COMET number, as the shared task's own scoring convention does, would hide the second.

**Why the checker's entity-detection gap for Chinese and Japanese is not incidental.** Section 6.1's finding that a crude Latin-script regex outperforms Stanza NER on these two languages is a property of how the injected-error ground truth was constructed (entity corruptions restricted to embedded Latin-script substrings for scripts with no capitalization signal), not a general claim about NER quality. But its consequence in Section 6.3 is real regardless of cause: C1 structurally cannot repair named-entity errors in Russian or Ukrainian, or quantifier-scope errors in Ukrainian, in this run, because those three cells failed the checker's own validated usability threshold. Any future run that adds Chinese or Japanese to the B/D/C1 comparison inherits this gap directly, and a genuine fix requires a CJK-capable entity extractor evaluated on real (not Latin-substring-restricted) entity corruptions, not a change to the checker's logic.

**Limitations.** The most consequential limitation is coverage: the B/D/C1 comparison ran on two of six language pairs (en-ru\_RU, en-uk\_UA), both Slavic-family languages with capitalization-based entity detection available, so the fivefold $\Delta$COMET reduction reported here has not been tested on Chinese or Japanese, where the checker's own validated coverage is weakest, or on Czech or Icelandic. A second is that Conditions C2 and C, which would isolate iteration as a distinct mechanism, remain unrun; every claim in this paper about "what fixes scoped editing" concerns localization breadth specifically, not verification. A third is the repair-model substitution: `google/gemma-3-12b-it` passes both fidelity checks in Section 6.2, but it still lacks the original TowerPlus-9B's machine-translation-specific fine-tuning, and this difference could itself interact with localization breadth in ways this iteration cannot separate from the localization effect. A fourth is that the checker-validation results in Section 6.1 use natural-row QE flags as a noisy precision proxy (only 6 of 24 cells clear both thresholds), so categories outside negation-polarity and Chinese number/unit/date should be read as unvalidated for headline claims even where they were used within C1's repair scope after passing the stricter, within-experiment validation reported in Section 6.3.

**What the next iteration must do.** Two things, directly enabled by this iteration's infrastructure and requiring no further design decisions: run Conditions C2 and C on the same two language pairs and repair model as the B/D/C1 comparison, to test whether iterative re-verification recovers C1's fix-rate and regression-rate cost while preserving its $\Delta$COMET gain -- the specific, falsifiable prediction stated above; and extend the comparison to the remaining four language pairs, prioritizing Chinese and Japanese specifically because they are where the checker's own validated coverage is weakest and where a CJK-capable entity extractor, not just more compute, is the prerequisite for a fair test.

# Conclusion

A shared task's worst-ranked result on scoped machine-translation editing sits, on the complete six-language-pair record, next to a same-task, same-strategy system that clears break-even on four of six pairs and falls short on two -- evidence that the failure is substantially, though not entirely, confounded with model capability and implementation maturity. This iteration moved that diagnosis from three quoted numbers to a measured comparison: with one repair model held fixed across conditions, a trivial output-hygiene fix explains none of the losing system's gap, while broadening what a validated deterministic checker is allowed to flag -- with no re-verification at all -- explains roughly four-fifths of it in $\Delta$COMET terms, at a real and measured cost in fix rate and true regression rate. Whether an iterative verify-and-repair loop recovers that cost without losing the quality gain is the specific, now well-defined question the next iteration's already-built infrastructure exists to answer.

# References

[1] R. Rei, C. Stewart, A. C. Farinha, A. Lavie. COMET: A Neural Framework for MT Evaluation. EMNLP 2020.

[2] R. Rei, M. V. Treviso, N. M. Guerreiro, C. Zerva, A. C. Farinha, C. Maroti, J. G. C. de Souza, T. Glushkova, D. M. Alves, A. Lavie, L. Coheur, A. F. T. Martins. CometKiwi: IST-Unbabel 2022 Submission for the Quality Estimation Shared Task. WMT 2022.

[3] A. Lavie, G. Hanneman, S. Agrawal, D. Kanojia, C.-K. Lo, V. Zouhar, F. Blain, C. Zerva, E. Avramidis, S. Deoghare, A. Sindhujan, J. Wang, D. I. Adelani, B. Thompson, T. Kocmi, M. Freitag, D. Deutsch. Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems: Linguistic Diversity is Challenging and References Still Help. WMT 2025.

[4] S. Padmanabhan. Can QE-informed (Re)Translation lead to Error Correction? WMT 2025.

[5] S. Deoghare, D. Kanojia, F. Blain, T. Ranasinghe, P. Bhattacharyya. Quality Estimation-Assisted Automatic Post-Editing. Findings of ACL: EMNLP 2023.

[6] S. Deoghare, D. Kanojia, P. Bhattacharyya. Giving the Old a Fresh Spin: Quality Estimation-Assisted Constrained Decoding for Automatic Post-Editing. arXiv:2501.17265, 2025.

[7] D. Ki, M. Carpuat. Guiding Large Language Models to Post-Edit Machine Translation with Error Annotations. NAACL-HLT 2024.

[8] A. Madaan, N. Tandon, P. Gupta, et al. Self-Refine: Iterative Refinement with Self-Feedback. NeurIPS 2023.

[9] S. Jha, S. A. Seshia. A Theory of Formal Synthesis via Inductive Learning. Acta Informatica, 54, 693-726, 2015.

[10] Q. Lu, L. Ding, K. Zhang, J. Zhang, D. Tao. MQM-APE: Toward High-Quality Error Annotation Predictors with Automatic Post-Editing in LLM Translation Evaluators. COLING 2024.

[11] H. Son, S. Eom, M. Song, J. Lee. LaSEr-Edit: Localized Span-level Error Editing with Energy-based Localization. 2024.

[12] N. M. Guerreiro, R. Rei, D. van Stigt, L. Coheur, P. Colombo, A. Martins. xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection. TACL, 12, 979-995, 2023.

[13] C. Zerva, F. Blain, J. G. C. de Souza, D. Kanojia, S. Deoghare, N. M. Guerreiro, G. Attanasio, R. Rei, C. Orasan, M. Negri, M. Turchi, R. Chatterjee, P. Bhattacharyya, M. Freitag, A. Martins. Findings of the Quality Estimation Shared Task at WMT 2024: Are LLMs Closing the Gap in QE? WMT 2024.

[14] D. Deutsch, E. Briakou, I. Caswell, et al. WMT24++: Expanding the Language Coverage of WMT24 to 55 Languages & Dialects. ACL 2025.

[15] Unbabel/COMET model license table (per-checkpoint license terms).

[16] unbabel-comet PyPI package (Apache-2.0 scoring package).

[17] T. Gowda et al. PyMarian: Fast Neural Machine Translation and Evaluation in Python. arXiv:2408.11853, 2024.

[18] spaCy zh_core_web_lg model card (Chinese NER, F1 0.7134).

[19] spaCy ja_core_news_lg model card (Japanese NER, F1 0.7119).

[20] spaCy ru_core_news_lg model card (Russian NER, F1 0.9530).

[21] spaCy uk_core_news_trf model card (Ukrainian NER, F1 0.8968).

[22] J. Straková, M. Straka. NameTag 3: A Tool and a Service for Multilingual/Multitagset NER. ACL 2025. (Czech F1 86.39/89.29; Ukrainian cross-check F1 92.18)

[23] python-duckling language coverage (date/number/unit parsing for Japanese, Russian, Ukrainian, Chinese).

[24] Han, Storoshenko, Sakurai. On the variability of negative scope in Japanese. Journal of Linguistics.

[25] B. Partee, V. Borschev. Russian Genitive of Negation research program.

[26] Á. Angantýsson. Sentential Negation and Verb Placement in Embedded Clauses in Icelandic. 2008.

[27] IceBERT-finetuned-ner model card (vesteinn/IceBERT-finetuned-ner), Icelandic NER fine-tuned on the mim_gold_ner corpus, F1 0.8721.

[28] P. K. Sharma. Leveraging QE-based Explanations for Quality-Informed Corrections. WMT 2025.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) The B/D vs. C1 fix-rate and true-regression-rate comparison (Section 6.3, headline: fix rate 0.7375 for B/D vs. 0.4542 for C1) is not a fair like-for-like comparison because of an undisclosed structural asymmetry: per the underlying artifact (art_7Uc5PlFctjXi), negation-polarity-flip corruptions in the injected set are span deletions (corrupted_span=''), so B/D's oracle-QE-span masking design gives them a zero-width span and they 'structurally never attempt a repair on any negation row' -- meaning B/D's fix rate on that entire category is mechanically 0 regardless of repair quality, while C1 uses its own real checker-based localization and can attempt negation repairs. Negation is 1 of 4 categories (30 of 240 injected-pool rows, 12.5%), so this asymmetry is baked into the pooled fix-rate and regression-rate numbers the paper reports as if they reflected repair-quality differences alone. The paper's Results and Discussion sections never mention this; a reader has no way to know that part of C1's apparent disadvantage (or part of B/D's apparent advantage, depending on direction) is a design artifact of how the two conditions are localized rather than a difference in repair capability.
  Action: Report fix rate and true-regression-rate broken out by category (or at minimum, pooled excluding negation vs. pooled including it) for all three conditions, and state explicitly in Section 6.3 that B/D structurally cannot attempt negation repairs under the oracle-span design used for the injected set. If excluding negation changes the magnitude of the fix-rate/regression-rate gap between B/D and C1, report the corrected comparison as the headline number instead of the confounded pooled one.
- [MAJOR] (rigor) The paper describes two different checker-validation procedures with materially different results and never reconciles them. Section 6.1 reports a 'global' validation on the full checker-validation-heldout fold (448 injected + 1,080 natural rows across all 6 languages, all 24 language-category cells) where only 6 of 24 cells clear both a 0.5 recall and 0.5 precision threshold. Section 6.3 then reports a 'separate, stricter within-experiment validation on the two language pairs it actually ran on,' where only 3 of 8 cells for en-ru_RU/en-uk_UA are excluded -- implying 5 of 8 pass, a much higher pass rate for the same two languages than the global validation's 6/24 (of which only 2 concern these two languages, per the text: negation for 5/6 languages and Chinese number/date). This is either two genuinely different validation methodologies (the supporting artifact art_7Uc5PlFctjXi describes a 'conservative single-positive-per-row precision/recall metric' on 175 rows, distinct from Section 6.1's natural-row noisy-precision-proxy approach on 448+1080 rows) that happen to disagree, or an inconsistency in how 'validated' is being used across the paper. Since C1's actual repair scope in the reported results is gated by the Section 6.3 (within-experiment) validation, not the Section 6.1 (global) one, the reader cannot tell which validation result should inform their confidence in C1's headline numbers, and the paper's own Limitations section ('only 6 of 24 cells clear both thresholds... categories outside negation-polarity and Chinese number/unit/date should be read as unvalidated') appears to contradict the fact that C1 used a 5/8 pass rate to determine its actual repair scope.
  Action: Name both validation procedures explicitly where each is introduced (e.g., 'global checker validation' vs. 'within-run checker validation'), state precisely why they differ (different holdout size, different precision definition, different threshold), and clarify in the Limitations section which one actually governs the reported C1 results, so that the 6/24 caveat and the 5/8 gating decision are not left implicitly in tension.
- [MINOR] (scope) The executed B/D/C1 comparison runs on exactly the two language pairs (en-ru_RU, en-uk_UA) with capitalization-based entity detection -- the setting where the checker performs best, per the paper's own checker-validation results. The headline 'fivefold reduction' / 'four-fifths' figures are therefore measured in the most favorable available setting, not a representative one, and the paper's own analysis suggests the effect would likely be smaller for Chinese and Japanese (where named-entity coverage fails outright). This is disclosed in the Limitations section but not flagged where the headline numbers are first introduced.
  Action: When stating the fivefold/four-fifths figures in the abstract-equivalent contributions list and Results overview, add a parenthetical noting they are measured on the two language pairs with the strongest checker coverage, and that CJK generalization is untested -- consistent with how the paper already treats this caveat in Discussion, just surfaced earlier.
- [MINOR] (methodology) The Condition-B fidelity gate requires the substitute model to reproduce 'the same order of magnitude' of ΔCOMET as the original (-0.0108), but the actual reproduction is 1.5x the original magnitude (-0.0164 vs. -0.0108), and 'same order of magnitude' was never quantitatively pre-specified (e.g., as a ratio bound) before the check was run. A 1.5x deviation is plausible as noise but could also indicate the substitute model's capability floor is somewhat different from the original's -- exactly the threat the fidelity check exists to rule out -- and the paper's own PASS_UNRELIABLE_SUBSTITUTED_SCORER framing in the underlying artifact suggests the original team itself treated this as a three-way, not binary, verdict.
  Action: State the pre-registered (or post-hoc, if not pre-registered) numeric tolerance used for 'same order of magnitude' explicitly, and discuss whether a 1.5x deviation is within that tolerance or represents a borderline pass that should further temper confidence in the magnitude (not just direction) of the B/D/C1 comparison.
- [MINOR] (clarity) Figure 3 (checker validation) and Figure 4/5 (B/D/C1 comparison) are described only by caption in the prompt materials, but given the two-validation-procedure issue above, a reader relying on Figure 3 alone to judge checker reliability may draw a different conclusion than the actual gating logic used in Section 6.3.
  Action: Ensure Figure 3's caption or accompanying table distinguishes the global validation numbers from the within-experiment gating numbers used for C1, consistent with the reconciliation requested in the rigor critique above.
- [MINOR] (novelty) The CEGIS framing (Related Work) is now appropriately hedged ('we do not claim to import CEGIS as a synthesis algorithm... the parallel is looser than it may first appear'), which adequately resolves the prior review's concern about overstating the connection. No further action strictly required, but the paper could strengthen this section by more directly stating what would make the analogy tighter (e.g., if a future C2/C condition's checker output were used to constrain which repair candidates are even generated, rather than only accept/reject a single candidate) so the analogy has a concrete future test rather than remaining purely rhetorical.
  Action: Optional: add one sentence connecting the CEGIS discussion to a concrete prediction for Condition C2/C (e.g., whether repeated counterexamples localize to increasingly narrow spans, which would be the closest empirical analogue to CEGIS's counterexample-guided narrowing).
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-01 07:27:41 UTC

```
AI in translation emwrging opportunities
```

### [3] SYSTEM-USER prompt · 2026-09-01 07:28:45 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The file `.terminal_claude_agent_struct_out.json` does not contain valid JSON: Expecting ',' delimiter: line 3 column 2303 (char 2359). Rewrite the entire file with well-formed JSON.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
