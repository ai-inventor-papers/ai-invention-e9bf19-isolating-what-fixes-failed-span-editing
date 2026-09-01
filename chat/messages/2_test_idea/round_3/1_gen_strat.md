# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 3 · `gen_strat`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 07:29:06 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 07:29:12 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Isolating What Fixes Failed Span Editing
hypothesis: >-
  Padmanabhan (2025)'s WMT25 Task 3 secondary system (SURREYPAI-S2) -- QE-flagged spans masked with a __BLANK__ token, a single
  TowerPlus-9B fill-in pass, no re-check -- scored ΔCOMET = -0.0108, the worst of eight ranked Task 3 entries, against +0.0201
  for the same team's primary retranslation-selection system. This iteration ran the first controlled test of that gap with
  a fixed substitute repair model (google/gemma-3-12b-it, since TowerPlus-9B and its assumed fallback are confirmed delisted
  from every checked route) on two Slavic-family language pairs (en-ru_RU, en-uk_UA, 320 natural + 240 injected-pool rows),
  using the real wmt22-cometkiwi-da checkpoint throughout. Two of five conditions (B: faithful masked-fill baseline; D: B
  plus trivial output-hygiene retry) were compared against a third (C1: checker-broadened localization to every content-invariant
  violation in the sentence, single uncorrected repair pass, no re-verification). The results MEASURED, not merely hypothesized:
  (1) Condition D does not close B's gap -- pooled ΔCOMET -0.0157 (D) vs -0.0164 (B), 95% CIs overlapping almost completely,
  and every injected-pool repair-quality metric identical between them -- ruling out leftover-placeholder hygiene as the explanation.
  (2) Condition C1 -- broadened localization ALONE, with zero iteration -- cuts the ΔCOMET degradation roughly fivefold relative
  to B/D (pooled -0.0035, 95% CI [-0.0071,-0.0008]; en-uk_UA's own CI crosses zero), at a real cost in fix rate (0.7375 to
  0.4542 pooled) and true regression rate (0.050 to 0.125 pooled) on the injected-pool set. (3) That fix-rate/regression-rate
  comparison is NOT yet apples-to-apples, per reviewer critique: negation-polarity-flip corruptions in the injected set are
  span deletions, so B/D's oracle-QE-span masking design structurally cannot attempt ANY negation repair (12.5% of injected-pool
  rows), mechanically depressing B/D's fix rate and inflating C1's apparent disadvantage on that axis in a direction not yet
  disentangled from genuine repair-quality differences -- the category-broken-out comparison needed to isolate this confound
  has not been run. (4) The condition-B fidelity gate (substitute model must reproduce the original's failure signature) technically
  PASSED but only under an unquantified 'same order of magnitude' criterion; the measured deviation is 1.5x the original's
  -0.0108, which is plausibly noise but was never bounded by a pre-registered tolerance, so the magnitude (not direction)
  of every downstream B/D/C1 comparison carries an unresolved uncertainty the fidelity check was specifically built to rule
  out. (5) Two materially different checker-validation procedures exist in this iteration's own artifacts and are not yet
  reconciled: a global validation (448 injected + 1,080 natural rows, all 6 languages, all 24 language-category cells, natural-row
  QE-flag precision proxy) finds only 6/24 cells usable, while a separate within-experiment validation (175 rows, single-positive-per-row
  precision/recall, only the 2 languages C1 actually ran on) finds 5/8 cells usable for those same two languages -- and it
  is the within-experiment validation, not the global one, that actually gated C1's repair scope, a dependency the paper states
  but has not yet explained methodologically (different holdout size, different precision definition, different threshold).
  (6) The executed comparison ran exclusively on the two language pairs (Russian, Ukrainian) where the checker's own validation
  shows its strongest coverage (capitalization-based entity detection, no CJK gap), so the fivefold/four-fifths figures are
  a best-case measurement, not yet a representative one -- Chinese and Japanese, where named-entity recall is confirmed (not
  merely anticipated) to fail via the dataset's Latin-script-substring-restricted entity-corruption construction, remain untested
  for the B/D/C1 comparison itself. We hypothesize, with these six qualifications now attached rather than left implicit,
  that a genuine, separable residual gap remains between (i) broadening localization from one QE-flagged span to every content-invariant
  violation in the sentence (partially confirmed this iteration, condition C1, on 2/6 language pairs, with an unresolved negation-category
  confound in its cost accounting) and (ii) adding an iterate-to-verified-pass loop around each repair (condition C2, not
  yet run), and that specifically the iteration/verification component is what would recover C1's fix-rate and regression-rate
  cost while preserving its ΔCOMET gain -- a specific, falsifiable prediction for the next iteration to test, not yet supported
  or refuted by any run condition. The mechanism-attributing part of this hypothesis (iteration vs. broadened localization
  as the load-bearing factor) remains UNTESTED: conditions C2 and C have not been run. What is now measured, not hypothesized,
  is the narrower claim that broadened one-pass localization alone -- with the repair model, hygiene, and QE-span baseline
  all held fixed -- reduces (does not eliminate) scoped editing's aggregate quality cost relative to the field's documented
  worst case, on the two language pairs where the underlying checker is known to work well, at a real and only partially quantified
  cost in targeted-fix accuracy. The next iteration's job is sequential and gated, as before, but now with four additional
  prerequisites the reviewer identified as missing rather than assumed satisfied: (a) report and interpret the B/D-vs-C1 fix-rate/true-regression-rate
  comparison broken out by invariant category (or at minimum pooled excluding negation vs including it), since the pooled
  headline conflates a structural localization-design asymmetry with a genuine repair-quality difference; (b) name and reconcile
  the two checker-validation procedures explicitly -- global (24-cell, natural-QE-proxy) versus within-experiment (8-cell-per-run,
  single-positive-per-row) -- and state plainly which one governs any reported repair-scope decision, since they currently
  disagree in ways the paper does not explain; (c) state a pre-registered or explicitly post-hoc numeric tolerance for what
  counts as 'same order of magnitude' in the condition-B fidelity gate, and discuss whether the measured 1.5x deviation is
  inside or outside it; (d) before generalizing the fivefold-reduction finding beyond en-ru_RU/en-uk_UA, either run the B/D/C1
  comparison on at least one CJK pair (accepting the checker's known named-entity gap there as a documented limitation of
  that specific run, not of the finding) or explicitly scope every headline number to 'the two language pairs with strongest
  checker coverage' at first mention, not only in Limitations. Only after these four are addressed does running C2 and C --
  the comparison this hypothesis was originally designed to make -- become a comparison whose numbers can be trusted rather
  than one built on unreconciled or unstated internal inconsistencies.
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
  Same B/D/C1/C2/C frame; narrowed claims to what C1 actually showed and flagged 4 unresolved reviewer-identified gaps.
_confidence_delta: unchanged
_key_changes:
- >-
  Flagged the B/D-vs-C1 fix-rate/true-regression-rate comparison as confounded by a structural asymmetry (negation-flip corruptions
  are deletions, so B/D structurally cannot attempt negation repairs) per reviewer MAJOR methodology critique; the category-broken-out
  comparison needed to resolve it is now an explicit prerequisite, not yet run.
- >-
  Surfaced the unreconciled disagreement between the global checker validation (6/24 cells usable) and the within-experiment
  validation that actually gated C1's repair scope (5/8 cells for the 2 run languages) per reviewer MAJOR rigor critique;
  reconciling which governs which claim is now a named next-step prerequisite.
- >-
  Added an explicit caveat that the executed B/D/C1 comparison ran only on the two language pairs with the checker's strongest
  measured coverage (no CJK gap), so the fivefold/four-fifths figures are a best-case, not representative, measurement --
  surfaced at first mention rather than only in Limitations, per reviewer MINOR scope critique.
- >-
  Quantified the condition-B fidelity-gate concern: the substitute model's ΔCOMET is 1.5x the original's magnitude under an
  unquantified 'same order of magnitude' criterion, so the PASS verdict is now described as a borderline pass requiring a
  stated tolerance, not an unqualified pass, per reviewer MINOR methodology critique.
- >-
  Kept the core B/D/C1/C2/C factorial design and the mechanism question (iteration vs. broadened localization) untouched,
  since C1's own trade-off pattern (better ΔCOMET, worse fix-rate/regression-rate) is exactly the falsifiable prediction C2
  was designed to test, and nothing this iteration found contradicts that design.
- >-
  Reframed 'what the next iteration must do' as four concrete data-quality/reconciliation prerequisites (category breakout,
  validation reconciliation, tolerance statement, CJK scoping) that must be resolved before C2/C results would be trustworthy,
  rather than treating C1's results as already publication-ready.
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<iteration_status>
Current iteration: 3 of 5
Remaining (including this one): 3
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Run the checker, validate it, then run B/D/C1 for real
objective: >-
  Stop specifying the protocol and start running it: validate the deterministic content-invariant checker's precision/recall
  against the held-out slice, validate that condition B with the forced substitute repair model reproduces Padmanabhan's original
  failure signature, and then execute conditions B, D, and C1 (the minimum partial comparison the reviewer named) on at least
  two language pairs with real fix-rate, true-regression-rate, and ΔCOMET numbers -- so the next paper draft reports at least
  one measured comparison instead of quoting three numbers from two prior papers.
rationale: >-
  Every MAJOR reviewer critique points at the same root cause: nothing in the paper has been run. The fix is not more infrastructure
  -- iteration 1 already produced a validated 8,519-row dataset and a fully resolved replication/resource dossier -- it is
  spending this iteration's artifact budget on execution, in the exact gated order the paper itself already commits to (checker
  validation, then condition-B fidelity check, then a comparison). Gating matters because a downstream comparison built on
  an unvalidated checker or an unfaithful condition-B reproduction would be uninterpretable regardless of how many conditions
  get run, which is why this strategy treats validation as a hard prerequisite artifact rather than a parallel nice-to-have.
  Scoping to B/D/C1 rather than the full five-condition sweep (including C2, C, and the severity-matched variants) matches
  the reviewer's own stated minimum ('conditions B, D, C1 minimum, on one or two language pairs is preferable to none') and
  keeps the budget realistic: C2 and C multiply LLM calls per sentence through iteration, and spending the $10 OpenRouter
  budget establishing that B is faithfully reproduced and that D/C1 differ from it in a measurable, well-powered way is more
  valuable this iteration than a thin five-way sweep that runs out of budget before any condition is well-powered. This also
  directly answers the localization-vs-hygiene half of the mechanism question (does a one-line hygiene filter already close
  most of the gap, or does broadening what gets checked do more) even though the full localization-vs-iteration question (C1
  vs C2) is deferred one more iteration -- consistent with the paper's own 'sequential and gated, not simultaneous' framing
  in the hypothesis text. Two language pairs are chosen deliberately to include one CJK pair (documented severe entity-detection
  recall gap) and one non-CJK pair (materially better checker coverage), so the eventual write-up can honestly report whether
  the CJK gap changes the qualitative comparison rather than silently averaging over it -- directly addressing the reviewer's
  rigor and Chinese/Japanese critique.
artifact_directions:
- id: experiment_iter2_dir1
  type: experiment
  objective: >-
    Build the four-category deterministic content-invariant checker (entity identity, number/unit/date, negation polarity,
    quantifier scope) exactly as specified in the iter-1 resource dossier, run it against the checker_validation_heldout fold
    of both the natural and injected-error dataset rows, and report precision/recall per (language, category) cell -- including
    an explicit, unhedged report of the Chinese/Japanese entity-detection recall gap the dossier already flagged as a known
    limitation rather than a possible one.
  approach: >-
    Load data_out/full_data_out.json from the WMT25 dataset artifact, restrict to metadata_fold == checker_validation_heldout.
    Implement each category detector using the exact resources the dossier resolved (multilingual NER models for entities
    per language -- e.g. spaCy zh_core_web_lg/ja_core_news_lg/ru_core_news_lg/uk_core_news_trf, NameTag3 for Czech, IceBERT-finetuned-ner
    for Icelandic; a rule-based date/number/unit parser for the four natively-covered languages plus regex fallback for the
    other two; per-language negation cue lists with the single-negation-marker firing rule; closed-class quantifier word lists).
    Score against the injected rows' known ground-truth spans/categories (precision/recall directly computable) and, where
    natural rows carry QE-flagged spans, treat those as a secondary, noisier check. Report a full (language x category) precision/recall
    table plus 95% CIs (bootstrap over rows), explicitly calling out any cell below a usable threshold (e.g. Chinese/Japanese
    entity swap) as EXCLUDED from headline localization claims rather than silently included -- directly operationalizing
    the reviewer's rigor-critique action item. Persist the fitted checker as a reusable, deterministic scoring function/module
    so the next artifact can call it identically.
  depends_on:
  - id: art_5ySTX4YfxqG_
    label: resource dossier
    relation_type:
    relation_rationale:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
- id: experiment_iter2_dir2
  type: experiment
  objective: >-
    Run condition B (faithful masked-fill baseline, severity-skip heuristic, one repair pass, no re-check) with the forced
    substitute repair model on 2 language pairs (one CJK -- e.g. Chinese, one non-CJK -- e.g. Czech or Russian), and validate
    as an explicit sanity-check gate whether it reproduces Padmanabhan's original qualitative failure signature (leftover
    placeholder/mask-token leakage rate, direction and rough magnitude of mean ΔCOMET versus the -0.0108/-0.007-to--0.014
    published figures) before any comparison is trusted.
  approach: >-
    Use experimental_pool rows for the two chosen language pairs from the dataset artifact. Implement the exact masking prompt
    template and severity-conditioned masking rule from the resource dossier (mask nothing >=0.90 QE score; major-only or
    all-if-only-minor between 0.50-0.90; mask everything <0.50) via one OpenRouter call per flagged span to the confirmed
    substitute repair model (google/gemma-3-12b-it), one uncorrected fill pass, no re-check. Score with wmt22-cometkiwi-da
    (or the closest available open COMET scorer if the gated checkpoint is inaccessible within budget -- document any such
    substitution explicitly) to get per-sentence and mean ΔCOMET. Report, as the gate itself: (1) rate of leftover mask-token/placeholder/garbled-text
    leakage in outputs, compared qualitatively to the '__HEARTBREAK__'-style failure documented in Padmanabhan's Appendix
    B; (2) mean ΔCOMET direction and rough magnitude versus the published -0.0108/-0.007 figures. State plainly whether the
    substitute-model reproduction PASSES (same direction, comparable failure modes) or FAILS (meaningfully different behavior)
    the fidelity check -- if it fails, this is reported as a first-class limitation on everything condition D/C1 measure downstream,
    per the reviewer's methodology critique, not glossed over. Track and cap OpenRouter spend against the $10 budget (estimate
    cost per call up front from the two pairs' row counts before running the full sweep).
  depends_on:
  - id: art_5ySTX4YfxqG_
    label: resource dossier
    relation_type:
    relation_rationale:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
- id: experiment_iter2_dir3
  type: experiment
  objective: >-
    Run conditions D (condition B plus a trivial post-hoc hygiene filter, no invariant checker) and C1 (checker flags every
    invariant violation in the sentence, each repaired in one uncorrected pass, no re-verification) on the same 2 language
    pairs and same rows as the condition-B run, using the same fixed substitute repair model and the validated checker from
    the first artifact, so all three conditions (B, D, C1) are directly comparable on identical inputs.
  approach: >-
    Reuse condition B's outputs and reproduce/extend the pipeline: for D, add a deterministic post-generation filter (regex/string
    checks for leftover __BLANK__-style tokens, garbled placeholder patterns, and leaked instruction-format strings like 'Corrected
    words: [...]') that triggers exactly one retry pass within the same single-pass budget when triggered. For C1, run the
    validated checker (from artifact 1) over the full sentence rather than only the QE-flagged span, and repair every category
    violation the checker flags -- excluding any (language, category) cell the checker-validation artifact flagged as below-threshold
    (documenting the Chinese/Japanese entity exclusion explicitly here too, not just in the checker report) -- each in one
    uncorrected repair pass with the same fixed model and prompt style as B/D. Score all three conditions identically: fix
    rate (against checker-verdict and, where available, QE/human-confirmed subset), true regression rate on the injected-error
    subset (known ground truth), mean ΔCOMET per language pair and pooled, edit volume relative to gain, and LLM calls/tokens
    per sentence. Report results separately per language pair and separately for natural vs injected subsets, matching the
    paper's stated reporting protocol.
  depends_on:
  - id: art_5ySTX4YfxqG_
    label: resource dossier
    relation_type:
    relation_rationale:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
- id: evaluation_iter2_dir4
  type: evaluation
  objective: >-
    Turn the B/D/C1 outputs and the checker-validation results into the paper's first real comparative evidence: does D close
    most of B's gap (hygiene-alone explanation), does C1 do materially better than D (broadened-localization evidence), and
    does the condition-B fidelity gate pass -- reported with confidence intervals and explicit uncertainty quantification,
    plus a full six-language-pair ΔCOMET breakdown table replacing the three cherry-picked points Figure 3 currently relies
    on.
  approach: >-
    Load the checker-validation precision/recall table, the condition-B fidelity-gate verdict, and the B/D/C1 per-sentence
    results (produced in parallel this iteration; the executor reads them from the shared artifact pool at run time, not via
    a formal dependency edge, since no prior-iteration experiment exists to reference). Compute, with bootstrap or exact CIs
    where sample size allows: mean ΔCOMET per condition per language pair (paired differences B->D->C1 on identical rows,
    not independent means); true regression rate per condition on the injected-error ground-truth subset with CIs; fix rate
    per condition on both all-flagged and human/ground-truth-confirmed subsets; edit-volume-to-gain ratio for C1 versus B/D
    to rule out C1 degenerating toward full-sentence regeneration. Explicitly quantify the small-sample nature of this partial
    run (2 language pairs, one gated fidelity check) rather than overclaiming generality, directly answering the reviewer's
    evidentiary-uncertainty critique -- and separately report whether excluding the flagged low-recall (language, category)
    cells changes the C1-vs-D comparison materially. Produce a full six-language-pair ΔCOMET table for Padmanabhan's original
    B/D1 systems, quoting the resource dossier's Table 15 reconciliation directly (addressing the reviewer's clarity critique
    about the incomplete per-pair breakdown) placed alongside this iteration's own newly measured B/D/C1 numbers for direct
    visual contrast between quoted-prior-work and measured-this-iteration figures.
  depends_on:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
expected_outcome: >-
  A validated checker with a reported per-language, per-category precision/recall table (including an explicit CJK entity-detection
  exclusion where warranted); an explicit PASS/FAIL verdict on whether the substitute-model condition-B reproduction is faithful
  to Padmanabhan's original failure signature, reported as a first-class result rather than an assumption; and real, measured
  fix-rate/regression-rate/ΔCOMET/edit-volume results for conditions B, D, and C1 on two language pairs with confidence intervals
  -- giving the next paper draft its first genuine empirical answer to whether hygiene alone (D) or broadened localization
  (C1) closes B's gap, addressing all four MAJOR reviewer critiques (untested core question, thin evidentiary base, unvalidated
  repair-model substitution, unvalidated checker) with the minimum partial comparison the reviewer explicitly named as sufficient
  for resubmission.
summary: >-
  Executes the exact gated sequence the current paper already commits to but has not run: validate the checker, validate condition
  B's fidelity under the forced model substitution, then measure conditions B/D/C1 on two language pairs with real fix-rate/regression-rate/ΔCOMET
  numbers and honest uncertainty quantification -- converting the paper from a resource/diagnosis contribution into one with
  at least a partial, real comparative result.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
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
out_dependency_files:
  file_list:
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
out_dependency_files:
  file_list:
  - data.py
  - data_out/full_data_out.json
  - data_out/mini_data_out.json
  - data_out/preview_data_out.json
  data_file_paths:
  - data_out/full_data_out.json
  - data_out/mini_data_out.json
  - data_out/preview_data_out.json

--- Item 3 ---
id: art_QLpPxaqf1VzK
type: experiment
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 4 ---
id: art_G9ppuk8aHUhW
type: experiment
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 5 ---
id: art_7Uc5PlFctjXi
type: experiment
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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 6 ---
id: art_qUG1DIUZKEBQ
type: evaluation
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
out_dependency_files:
  file_list:
  - eval.py
  - full_eval_out.json
  - mini_eval_out.json
  - preview_eval_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

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
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

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

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 5 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool

**BROADER IS NOT THE SAME AS DEEPER.** Adding models, datasets, or settings to
an experiment that already ran makes the table bigger; it does not make the
contribution stronger, and it is the default a strategy generator drifts into
when it has nothing sharper to propose. Spend an artifact on scale only when
the SPREAD itself is the finding (a scaling trend, a regime boundary, a
generalisation claim the paper actually makes). Otherwise spend it on
something that could change the conclusion: the mechanism behind an observed
effect, the condition under which it disappears, the confound that would
explain it away, or the baseline whose absence a reviewer would name first.


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
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 07:29:12 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Bash · 2026-09-01 07:29:38 UTC

```
mkdir -p "$(dirname './.terminal_claude_agent_struct_out.json')" 2>/dev/null; pwd
```

### [5] TOOL RESULT — Bash · 2026-09-01 07:29:38 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [6] TOOL CALL — Write · 2026-09-01 07:30:48 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Run the iteration conditions, then reconcile the numbers",
      "objective": "Execute Conditions C2 (narrow localization, iterative verification) and C (broad localization, iterative verification) -- the two conditions this project's entire five-condition design was originally built to compare, and the only ones that can test whether iteration, as opposed to broadened one-pass checking, is the load-bearing mechanism -- on the same rows, repair model, and checker as the already-executed B/D/C1 comparison, and pair that with a single reconciliation evaluation that fixes every MAJOR/MINOR methodology gap the reviewer named in the existing B/D/C1 results before any C2/C number is trusted alongside them.",
      "rationale": "The paper's own Discussion and Conclusion already state the next iteration's job in specific, falsifiable terms: does re-checking a repair against the deterministic checker recover C1's fix-rate and true-regression-rate cost while preserving its ΔCOMET gain. That question is the paper's central untested claim and has now been deferred twice (iteration 1 specified it, iteration 2 executed everything except it) -- a third iteration spent only on re-analyzing B/D/C1 without ever running C2/C would leave the mechanism claim permanently unresolved with two iterations left after this one. At the same time, the reviewer's two MAJOR critiques are not resolved by running more conditions -- they are resolved by re-reading data that already exists: the negation-deletion asymmetry in B/D's fix-rate comparison and the unreconciled global-vs-within-experiment checker validation are both artifacts of how existing results were reported, not gaps that need new rows. Running C2/C without also fixing these would compound the problem, since C2/C reuse the exact same oracle-span-vs-checker-localization design that created the B/D-vs-C1 asymmetry in the first place -- so the reconciliation evaluation must run on all five conditions together, with category-level breakouts and an explicit negation-deletion flag baked in from the start rather than retrofitted later. Concretely: C2 keeps localization narrow (the QE-flagged span only, exactly as B/D use it, so it inherits the same negation-deletion asymmetry and must report around it identically) but adds a checker-gated repair-then-reverify loop up to a fixed pass budget, stopping on a certificate; C is the full combination, checker-broadened localization plus iteration. Both reuse the validated checker module and gemma-3-12b-it repair model from the existing C1 artifact so no new fidelity check is needed -- Condition B's fidelity gate already covers every condition that shares its repair model. Running both C2 and C (not just C2) matters because the paper's stated success criterion is a three-way comparison (C1 vs C2 vs C, not just C1 vs C2): if C1 and C2 improve on D by statistically indistinguishable amounts, the mechanism-attributing claim is disconfirmed regardless of what C achieves, and only having C lets that disconfirmation (or confirmation) actually be checked rather than inferred. Both conditions are cheap enough to fit comfortably inside the $10 budget: the prior B/D/C1 run on the same 560 rows cost $0.066 for roughly 1,447 calls at a single-pass budget; a bounded iteration budget of up to 3 passes multiplies call volume by at most 3x per condition, putting two new conditions at an estimated $0.30-0.50 total, leaving ample room to also log the CEGIS-relevant instrumentation (whether repeated counterexamples localize to narrower spans across iterations) the reviewer's optional novelty suggestion asked for at effectively zero marginal cost.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion) on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1 comparison, isolating the effect of iteration while holding localization fixed at narrow.",
          "approach": "Load the same 320 natural + 240 injected-pool row selection used by the B/D/C1 experiment (reuse selected_rows.json from that artifact so C2 runs on literally identical inputs) and import checker.py and llm_client.py from that artifact rather than reimplementing them. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.",
          "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "reuses checker+llm_client+rows"},
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).",
          "approach": "Reuse C2's pass-budget infrastructure and C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add C2's iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.",
          "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "reuses checker+llm_client+rows"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"},
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.",
          "approach": "Load B/D/C1 results from the existing experiment artifact and C2/C results from the two new experiment artifacts, plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table.",
          "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 results"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"},
            {"id": "art_qUG1DIUZKEBQ", "label": "reconciliation eval"},
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"}
          ]
        }
      ],
      "expected_outcome": "Real, measured ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count results for Conditions C2 and C on the same rows/model/checker as the existing B/D/C1 comparison, giving the paper its first genuine test of the mechanism-attributing claim (iteration vs. broadened localization) with a CONFIRMED/DISCONFIRMED/MIXED verdict against the hypothesis's own pre-specified success criteria; a single reconciled five-condition results table with category-level fix-rate/regression-rate breakouts that eliminates the negation-deletion confound the reviewer flagged as a MAJOR issue; an explicit, named reconciliation of the two previously-conflicting checker-validation procedures stating which one governs repair scope; and a quantified, pre-registered tolerance for the Condition-B fidelity gate that turns the previously unqualified PASS into a stated borderline-pass judgment -- collectively resolving both MAJOR and two of three MINOR reviewer critiques while advancing the paper from a three-condition partial result to the complete five-condition comparison the protocol was designed around.",
      "summary": "Runs the two conditions (C2, C) this project's entire design was built to compare -- iterative verification versus broadened localization -- on the same controlled setup as the existing B/D/C1 result, and pairs them with one evaluation artifact that fixes the reviewer's category-breakout, validation-reconciliation, and fidelity-tolerance critiques on all five conditions at once, turning the paper's central untested claim into a measured, verdict-bearing result."
    }
  ]
}
```

### [7] TOOL RESULT — Write · 2026-09-01 07:30:48 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Run the iteration conditions, then reconcile the numbers\",\n      \"objective\": \"Execute Conditions C2 (narrow localization, iterative verification) and C (broad localization, iterative verification) -- the two conditions this project's entire five-condition design was originally built to compare, and the only ones that can test whether iteration, as opposed to broadened one-pass checking, is the load-bearing mechanism -- on the same rows, repair model, and checker as the already-executed B/D/C1 comparison, and pair that with a single reconciliation evaluation that fixes every MAJOR/MINOR methodology gap the reviewer named in the existing B/D/C1 results before any C2/C number is trusted alongside them.\",\n      \"rationale\": \"The paper's own Discussion and Conclusion already state the next iteration's job in specific, falsifiable terms: does re-checking a repair against the deterministic checker recover C1's fix-rate and true-regression-rate cost while preserving its ΔCOMET gain. That question is the paper's central untested claim and has now been deferred twice (iteration 1 specified it, iteration 2 executed everything except it) -- a third iteration spent only on re-analyzing B/D/C1 without ever running C2/C would leave the mechanism claim permanently unresolved with two iterations left after this one. At the same time, the reviewer's two MAJOR critiques are not resolved by running more conditions -- they are resolved by re-reading data that already exists: the negation-deletion asymmetry in B/D's fix-rate comparison and the unreconciled global-vs-within-experiment checker validation are both artifacts of how existing results were reported, not gaps that need new rows. Running C2/C without also fixing these would compound the problem, since C2/C reuse the exact same oracle-span-vs-checker-localization design that created the B/D-vs-C1 asymmetry in the first place -- so the reconciliation evaluation must run on all five conditions together, with category-level breakouts and an explicit negation-deletion flag baked in from the start rather than retrofitted later. Concretely: C2 keeps localization narrow (the QE-flagged span only, exactly as B/D use it, so it inherits the same negation-deletion asymmetry and must report around it identically) but adds a checker-gated repair-then-reverify loop up to a fixed pass budget, stopping on a certificate; C is the full combination, checker-broadened localization plus iteration. Both reuse the validated checker module and gemma-3-12b-it repair model from the existing C1 artifact so no new fidelity check is needed -- Condition B's fidelity gate already covers every condition that shares its repair model. Running both C2 and C (not just C2) matters because the paper's stated success criterion is a three-way comparison (C1 vs C2 vs C, not just C1 vs C2): if C1 and C2 improve on D by statistically indistinguishable amounts, the mechanism-attributing claim is disconfirmed regardless of what C achieves, and only having C lets that disconfirmation (or confirmation) actually be checked rather than inferred. Both conditions are cheap enough to fit comfortably inside the $10 budget: the prior B/D/C1 run on the same 560 rows cost $0.066 for roughly 1,447 calls at a single-pass budget; a bounded iteration budget of up to 3 passes multiplies call volume by at most 3x per condition, putting two new conditions at an estimated $0.30-0.50 total, leaving ample room to also log the CEGIS-relevant instrumentation (whether repeated counterexamples localize to narrower spans across iterations) the reviewer's optional novelty suggestion asked for at effectively zero marginal cost.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion) on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1 comparison, isolating the effect of iteration while holding localization fixed at narrow.\",\n          \"approach\": \"Load the same 320 natural + 240 injected-pool row selection used by the B/D/C1 experiment (reuse selected_rows.json from that artifact so C2 runs on literally identical inputs) and import checker.py and llm_client.py from that artifact rather than reimplementing them. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.\",\n          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"reuses checker+llm_client+rows\"},\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).\",\n          \"approach\": \"Reuse C2's pass-budget infrastructure and C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add C2's iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.\",\n          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"reuses checker+llm_client+rows\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.\",\n          \"approach\": \"Load B/D/C1 results from the existing experiment artifact and C2/C results from the two new experiment artifacts, plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table.\",\n          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},\n            {\"id\": \"art_qUG1DIUZKEBQ\", \"label\": \"reconciliation eval\"},\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"Real, measured ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count results for Conditions C2 and C on the same rows/model/checker as the existing B/D/C1 comparison, giving the paper its first genuine test of the mechanism-attributing claim (iteration vs. broadened localization) with a CONFIRMED/DISCONFIRMED/MIXED verdict against the hypothesis's own pre-specified success criteria; a single reconciled five-condition results table with category-level fix-rate/regression-rate breakouts that eliminates the negation-deletion confound the reviewer flagged as a MAJOR issue; an explicit, named reconciliation of the two previously-conflicting checker-validation procedures stating which one governs repair scope; and a quantified, pre-registered tolerance for the Condition-B fidelity gate that turns the previously unqualified PASS into a stated borderline-pass judgment -- collectively resolving both MAJOR and two of three MINOR reviewer critiques while advancing the paper from a three-condition partial result to the complete five-condition comparison the protocol was designed around.\",\n      \"summary\": \"Runs the two conditions (C2, C) this project's entire design was built to compare -- iterative verification versus broadened localization -- on the same controlled setup as the existing B/D/C1 result, and pairs them with one evaluation artifact that fixes the reviewer's category-breakout, validation-reconciliation, and fidelity-tolerance critiques on all five conditions at once, turning the paper's central untested claim into a measured, verdict-bearing result.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [8] ASSISTANT · 2026-09-01 07:30:49 UTC

```
Strategy written to `./.terminal_claude_agent_struct_out.json`. It runs Conditions C2 and C (the mechanism-testing conditions the paper has deferred twice) on the same controlled setup as the existing B/D/C1 result, plus a reconciliation evaluation that fixes the reviewer's category-breakout, checker-validation, and fidelity-tolerance critiques across all five conditions at once.
```

### [9] SYSTEM-USER prompt · 2026-09-01 07:30:50 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'experiment_iter3_dir1' (experiment): dependency 'art_7Uc5PlFctjXi' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir1' (experiment): dependency 'art_QLpPxaqf1VzK' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir2' (experiment): dependency 'art_7Uc5PlFctjXi' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter3_dir2' (experiment): dependency 'art_QLpPxaqf1VzK' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'evaluation_iter3_dir3' (evaluation): dependency 'art_qUG1DIUZKEBQ' has type 'evaluation' which is not allowed (allowed: {'experiment', 'dataset'})

INSUFFICIENT VALID ARTIFACTS:
  Required: at least 1 valid artifacts
  Found: 0 valid out of 3 total
  Artifacts with invalid types, duplicate IDs, or invalid dependencies don't count as valid.

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []
2. Ensure at least 1 artifacts are fully valid (correct types, no ID conflicts, valid dependencies)

Output the corrected JSON with the fixed strategies.
</task>
```

### [10] TOOL CALL — Write · 2026-09-01 07:31:34 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Run the iteration conditions, then reconcile the numbers",
      "objective": "Execute Conditions C2 (narrow localization, iterative verification) and C (broad localization, iterative verification) -- the two conditions this project's entire five-condition design was originally built to compare, and the only ones that can test whether iteration, as opposed to broadened one-pass checking, is the load-bearing mechanism -- on the same rows, repair model, and checker as the already-executed B/D/C1 comparison, and pair that with a single reconciliation evaluation that fixes every MAJOR/MINOR methodology gap the reviewer named in the existing B/D/C1 results before any C2/C number is trusted alongside them.",
      "rationale": "The paper's own Discussion and Conclusion already state the next iteration's job in specific, falsifiable terms: does re-checking a repair against the deterministic checker recover C1's fix-rate and true-regression-rate cost while preserving its ΔCOMET gain. That question is the paper's central untested claim and has now been deferred twice (iteration 1 specified it, iteration 2 executed everything except it) -- a third iteration spent only on re-analyzing B/D/C1 without ever running C2/C would leave the mechanism claim permanently unresolved with two iterations left after this one. At the same time, the reviewer's two MAJOR critiques are not resolved by running more conditions -- they are resolved by re-reading data that already exists: the negation-deletion asymmetry in B/D's fix-rate comparison and the unreconciled global-vs-within-experiment checker validation are both artifacts of how existing results were reported, not gaps that need new rows. Running C2/C without also fixing these would compound the problem, since C2/C reuse the exact same oracle-span-vs-checker-localization design that created the B/D-vs-C1 asymmetry in the first place -- so the reconciliation evaluation must run on all five conditions together, with category-level breakouts and an explicit negation-deletion flag baked in from the start rather than retrofitted later. Concretely: C2 keeps localization narrow (the QE-flagged span only, exactly as B/D use it, so it inherits the same negation-deletion asymmetry and must report around it identically) but adds a checker-gated repair-then-reverify loop up to a fixed pass budget, stopping on a certificate; C is the full combination, checker-broadened localization plus iteration. Both reuse the validated checker module and gemma-3-12b-it repair model from the existing C1 artifact so no new fidelity check is needed -- Condition B's fidelity gate already covers every condition that shares its repair model. Running both C2 and C (not just C2) matters because the paper's stated success criterion is a three-way comparison (C1 vs C2 vs C, not just C1 vs C2): if C1 and C2 improve on D by statistically indistinguishable amounts, the mechanism-attributing claim is disconfirmed regardless of what C achieves, and only having C lets that disconfirmation (or confirmation) actually be checked rather than inferred. Both conditions are cheap enough to fit comfortably inside the $10 budget: the prior B/D/C1 run on the same 560 rows cost $0.066 for roughly 1,447 calls at a single-pass budget; a bounded iteration budget of up to 3 passes multiplies call volume by at most 3x per condition, putting two new conditions at an estimated $0.30-0.50 total, leaving ample room to also log the CEGIS-relevant instrumentation (whether repeated counterexamples localize to narrower spans across iterations) the reviewer's optional novelty suggestion asked for at effectively zero marginal cost.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion) on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1 comparison, isolating the effect of iteration while holding localization fixed at narrow.",
          "approach": "Re-implement the B/D/C1 pipeline's checker module and OpenRouter client (the executor should read the prior experiment's method.py/checker.py directly from the run tree at the workspace_path recorded for that artifact, since no formal dependency edge is possible between two experiment artifacts, and reproduce the identical row selection by regenerating the same stratified 320-natural/240-injected-pool sample from the dataset using the same seed/stratification rule documented there) so C2 runs on effectively identical inputs. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.",
          "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_5ySTX4YfxqG_", "label": "resource dossier"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).",
          "approach": "Re-implement the same checker module, OpenRouter client, and row selection as the C2 artifact (again reading the prior B/D/C1 experiment's method.py/checker.py from its workspace_path in the run tree as a reference implementation, since experiment artifacts cannot formally depend on each other) and reuse C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add an iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log as C2. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.",
          "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_5ySTX4YfxqG_", "label": "resource dossier"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.",
          "approach": "Load B/D/C1 results from the existing experiment artifact (art_7Uc5PlFctjXi) and C2/C results from the two new sibling experiment artifacts in this strategy (the executor discovers them from the shared artifact pool at run time, exactly as the prior evaluation artifact art_qUG1DIUZKEBQ already does for same-iteration siblings, since a formal dependency edge on same-iteration artifacts is not permitted), plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table. If either sibling C2 or C artifact has not yet produced output files at evaluation time, degrade that condition's fields to NOT_AVAILABLE with a stated reason, exactly as the prior evaluation artifact's graceful-degradation pattern already establishes, rather than fabricating placeholder numbers.",
          "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"}
          ]
        }
      ],
      "expected_outcome": "Real, measured ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count results for Conditions C2 and C on the same rows/model/checker as the existing B/D/C1 comparison, giving the paper its first genuine test of the mechanism-attributing claim (iteration vs. broadened localization) with a CONFIRMED/DISCONFIRMED/MIXED verdict against the hypothesis's own pre-specified success criteria; a single reconciled five-condition results table with category-level fix-rate/regression-rate breakouts that eliminates the negation-deletion confound the reviewer flagged as a MAJOR issue; an explicit, named reconciliation of the two previously-conflicting checker-validation procedures stating which one governs repair scope; and a quantified, pre-registered tolerance for the Condition-B fidelity gate that turns the previously unqualified PASS into a stated borderline-pass judgment -- collectively resolving both MAJOR and two of three MINOR reviewer critiques while advancing the paper from a three-condition partial result to the complete five-condition comparison the protocol was designed around.",
      "summary": "Runs the two conditions (C2, C) this project's entire design was built to compare -- iterative verification versus broadened localization -- on the same controlled setup as the existing B/D/C1 result, and pairs them with one evaluation artifact that fixes the reviewer's category-breakout, validation-reconciliation, and fidelity-tolerance critiques on all five conditions at once, turning the paper's central untested claim into a measured, verdict-bearing result."
    }
  ]
}
```

### [11] TOOL RESULT — Write · 2026-09-01 07:31:34 UTC

```
{"type": "update", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Run the iteration conditions, then reconcile the numbers\",\n      \"objective\": \"Execute Conditions C2 (narrow localization, iterative verification) and C (broad localization, iterative verification) -- the two conditions this project's entire five-condition design was originally built to compare, and the only ones that can test whether iteration, as opposed to broadened one-pass checking, is the load-bearing mechanism -- on the same rows, repair model, and checker as the already-executed B/D/C1 comparison, and pair that with a single reconciliation evaluation that fixes every MAJOR/MINOR methodology gap the reviewer named in the existing B/D/C1 results before any C2/C number is trusted alongside them.\",\n      \"rationale\": \"The paper's own Discussion and Conclusion already state the next iteration's job in specific, falsifiable terms: does re-checking a repair against the deterministic checker recover C1's fix-rate and true-regression-rate cost while preserving its ΔCOMET gain. That question is the paper's central untested claim and has now been deferred twice (iteration 1 specified it, iteration 2 executed everything except it) -- a third iteration spent only on re-analyzing B/D/C1 without ever running C2/C would leave the mechanism claim permanently unresolved with two iterations left after this one. At the same time, the reviewer's two MAJOR critiques are not resolved by running more conditions -- they are resolved by re-reading data that already exists: the negation-deletion asymmetry in B/D's fix-rate comparison and the unreconciled global-vs-within-experiment checker validation are both artifacts of how existing results were reported, not gaps that need new rows. Running C2/C without also fixing these would compound the problem, since C2/C reuse the exact same oracle-span-vs-checker-localization design that created the B/D-vs-C1 asymmetry in the first place -- so the reconciliation evaluation must run on all five conditions together, with category-level breakouts and an explicit negation-deletion flag baked in from the start rather than retrofitted later. Concretely: C2 keeps localization narrow (the QE-flagged span only, exactly as B/D use it, so it inherits the same negation-deletion asymmetry and must report around it identically) but adds a checker-gated repair-then-reverify loop up to a fixed pass budget, stopping on a certificate; C is the full combination, checker-broadened localization plus iteration. Both reuse the validated checker module and gemma-3-12b-it repair model from the existing C1 artifact so no new fidelity check is needed -- Condition B's fidelity gate already covers every condition that shares its repair model. Running both C2 and C (not just C2) matters because the paper's stated success criterion is a three-way comparison (C1 vs C2 vs C, not just C1 vs C2): if C1 and C2 improve on D by statistically indistinguishable amounts, the mechanism-attributing claim is disconfirmed regardless of what C achieves, and only having C lets that disconfirmation (or confirmation) actually be checked rather than inferred. Both conditions are cheap enough to fit comfortably inside the $10 budget: the prior B/D/C1 run on the same 560 rows cost $0.066 for roughly 1,447 calls at a single-pass budget; a bounded iteration budget of up to 3 passes multiplies call volume by at most 3x per condition, putting two new conditions at an estimated $0.30-0.50 total, leaving ample room to also log the CEGIS-relevant instrumentation (whether repeated counterexamples localize to narrower spans across iterations) the reviewer's optional novelty suggestion asked for at effectively zero marginal cost.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion) on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1 comparison, isolating the effect of iteration while holding localization fixed at narrow.\",\n          \"approach\": \"Re-implement the B/D/C1 pipeline's checker module and OpenRouter client (the executor should read the prior experiment's method.py/checker.py directly from the run tree at the workspace_path recorded for that artifact, since no formal dependency edge is possible between two experiment artifacts, and reproduce the identical row selection by regenerating the same stratified 320-natural/240-injected-pool sample from the dataset using the same seed/stratification rule documented there) so C2 runs on effectively identical inputs. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.\",\n          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).\",\n          \"approach\": \"Re-implement the same checker module, OpenRouter client, and row selection as the C2 artifact (again reading the prior B/D/C1 experiment's method.py/checker.py from its workspace_path in the run tree as a reference implementation, since experiment artifacts cannot formally depend on each other) and reuse C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add an iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log as C2. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.\",\n          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.\",\n          \"approach\": \"Load B/D/C1 results from the existing experiment artifact (art_7Uc5PlFctjXi) and C2/C results from the two new sibling experiment artifacts in this strategy (the executor discovers them from the shared artifact pool at run time, exactly as the prior evaluation artifact art_qUG1DIUZKEBQ already does for same-iteration siblings, since a formal dependency edge on same-iteration artifacts is not permitted), plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table. If either sibling C2 or C artifact has not yet produced output files at evaluation time, degrade that condition's fields to NOT_AVAILABLE with a stated reason, exactly as the prior evaluation artifact's graceful-degradation pattern already establishes, rather than fabricating placeholder numbers.\",\n          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"Real, measured ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count results for Conditions C2 and C on the same rows/model/checker as the existing B/D/C1 comparison, giving the paper its first genuine test of the mechanism-attributing claim (iteration vs. broadened localization) with a CONFIRMED/DISCONFIRMED/MIXED verdict against the hypothesis's own pre-specified success criteria; a single reconciled five-condition results table with category-level fix-rate/regression-rate breakouts that eliminates the negation-deletion confound the reviewer flagged as a MAJOR issue; an explicit, named reconciliation of the two previously-conflicting checker-validation procedures stating which one governs repair scope; and a quantified, pre-registered tolerance for the Condition-B fidelity gate that turns the previously unqualified PASS into a stated borderline-pass judgment -- collectively resolving both MAJOR and two of three MINOR reviewer critiques while advancing the paper from a three-condition partial result to the complete five-condition comparison the protocol was designed around.\",\n      \"summary\": \"Runs the two conditions (C2, C) this project's entire design was built to compare -- iterative verification versus broadened localization -- on the same controlled setup as the existing B/D/C1 result, and pairs them with one evaluation artifact that fixes the reviewer's category-breakout, validation-reconciliation, and fidelity-tolerance critiques on all five conditions at once, turning the paper's central untested claim into a measured, verdict-bearing result.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 8, "oldLines": 31, "newStart": 8, "newLines": 26, "lines": ["         {", "           \"type\": \"experiment\",", "           \"objective\": \"Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion) on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1 comparison, isolating the effect of iteration while holding localization fixed at narrow.\",", "-          \"approach\": \"Load the same 320 natural + 240 injected-pool row selection used by the B/D/C1 experiment (reuse selected_rows.json from that artifact so C2 runs on literally identical inputs) and import checker.py and llm_client.py from that artifact rather than reimplementing them. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.\",", "+          \"approach\": \"Re-implement the B/D/C1 pipeline's checker module and OpenRouter client (the executor should read the prior experiment's method.py/checker.py directly from the run tree at the workspace_path recorded for that artifact, since no formal dependency edge is possible between two experiment artifacts, and reproduce the identical row selection by regenerating the same stratified 320-natural/240-injected-pool sample from the dataset using the same seed/stratification rule documented there) so C2 runs on effectively identical inputs. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from the pass-1 subset first.\",", "           \"depends_on\": [", "-            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"reuses checker+llm_client+rows\"},", "             {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},", "-            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}", "+            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}", "           ]", "         },", "         {", "           \"type\": \"experiment\",", "           \"objective\": \"Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).\",", "-          \"approach\": \"Reuse C2's pass-budget infrastructure and C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add C2's iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.\",", "+          \"approach\": \"Re-implement the same checker module, OpenRouter client, and row selection as the C2 artifact (again reading the prior B/D/C1 experiment's method.py/checker.py from its workspace_path in the run tree as a reference implementation, since experiment artifacts cannot formally depend on each other) and reuse C1's checker-broadened localization logic (flag every invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell repair scope C1 used) but add an iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the same certificate flag and per-pass narrowing log as C2. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization, not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out). Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact and the C2 artifact's combined spend tracked against the shared $10 ceiling.\",", "           \"depends_on\": [", "-            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"reuses checker+llm_client+rows\"},", "-            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},", "-            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}", "+            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},", "+            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}", "           ]", "         },", "         {", "           \"type\": \"evaluation\",", "           \"objective\": \"Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.\",", "-          \"approach\": \"Load B/D/C1 results from the existing experiment artifact and C2/C results from the two new experiment artifacts, plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table.\",", "+          \"approach\": \"Load B/D/C1 results from the existing experiment artifact (art_7Uc5PlFctjXi) and C2/C results from the two new sibling experiment artifacts in this strategy (the executor discovers them from the shared artifact pool at run time, exactly as the prior evaluation artifact art_qUG1DIUZKEBQ already does for same-iteration siblings, since a formal dependency edge on same-iteration artifacts is not permitted), plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table. If either sibling C2 or C artifact has not yet produced output files at evaluation time, degrade that condition's fields to NOT_AVAILABLE with a stated reason, exactly as the prior evaluation artifact's graceful-degradation pattern already establishes, rather than fabricating placeholder numbers.\",", "           \"depends_on\": [", "-            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},", "-            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},", "-            {\"id\": \"art_qUG1DIUZKEBQ\", \"label\": \"reconciliation eval\"},", "             {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}", "           ]", "         }"]}], "originalFile": null, "userModified": false}
```

### [12] ASSISTANT · 2026-09-01 07:31:36 UTC

```
Fixed: experiment artifacts now depend only on the dataset and research (resource dossier) artifacts, and the evaluation artifact depends only on the dataset — all valid types per the allowed-dependency rules.
```

### [13] SYSTEM-USER prompt · 2026-09-01 07:31:38 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'evaluation_iter3_dir3' (evaluation): missing required dependency. Must have at least one dependency of type: {'experiment'}

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []

Output the corrected JSON with the fixed strategies.
</task>
```

### [14] TOOL CALL — Edit · 2026-09-01 07:31:42 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"}
          ]
        }
      ],
      "expected_outcome"
NEW:           "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 results"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"}
          ]
        }
      ],
      "expected_outcome"
```

### [15] TOOL RESULT — Edit · 2026-09-01 07:31:42 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}\n          ]\n        }\n      ],\n      \"expected_outcome\"", "newString": "          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}\n          ]\n        }\n      ],\n      \"expected_outcome\"", "originalFile": null, "structuredPatch": [{"oldStart": 28, "oldLines": 7, "newStart": 28, "newLines": 9, "lines": ["           \"objective\": \"Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation), an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed, or undetermined.\",", "           \"approach\": \"Load B/D/C1 results from the existing experiment artifact (art_7Uc5PlFctjXi) and C2/C results from the two new sibling experiment artifacts in this strategy (the executor discovers them from the shared artifact pool at run time, exactly as the prior evaluation artifact art_qUG1DIUZKEBQ already does for same-iteration siblings, since a formal dependency edge on same-iteration artifacts is not permitted), plus the checker validation artifact's full 24-cell table and the within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact, not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within 2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended to replace the paper's current three-condition Section 6.3 table. If either sibling C2 or C artifact has not yet produced output files at evaluation time, degrade that condition's fields to NOT_AVAILABLE with a stated reason, exactly as the prior evaluation artifact's graceful-degradation pattern already establishes, rather than fabricating placeholder numbers.\",", "           \"depends_on\": [", "-            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}", "+            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},", "+            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},", "+            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}", "           ]", "         }", "       ],"]}], "userModified": false, "replaceAll": false}
```

### [16] ASSISTANT · 2026-09-01 07:31:44 UTC

```
Fixed: the evaluation artifact now depends on the existing `art_7Uc5PlFctjXi` (experiment) artifact as required, alongside the dataset and checker-validation experiment.
```
