# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 3 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 07:31:48 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 07:31:56 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

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

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter3_dir1
type: experiment
objective: >-
  Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified
  by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion)
  on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1
  comparison, isolating the effect of iteration while holding localization fixed at narrow.
approach: >-
  Re-implement the B/D/C1 pipeline's checker module and OpenRouter client (the executor should read the prior experiment's
  method.py/checker.py directly from the run tree at the workspace_path recorded for that artifact, since no formal dependency
  edge is possible between two experiment artifacts, and reproduce the identical row selection by regenerating the same stratified
  320-natural/240-injected-pool sample from the dataset using the same seed/stratification rule documented there) so C2 runs
  on effectively identical inputs. For each row, mask the original QE-flagged span (or, for injected rows, the oracle span
  exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit: negation rows
  have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row, not silently pooled
  away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it still fails and the category
  is checker-covered, issue one more targeted repair call scoped to exactly what the checker flagged, up to a hard cap of
  3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment a pass verifies clean. Log,
  per row and per pass: whether the span passed the checker before/after each pass, edit volume per pass, and whether repeated
  failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing signal). Score with
  the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus fix rate and true regression
  rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken out by invariant category (not
  pooled) so the negation asymmetry is visible from first report rather than needing later reconstruction. Track and cap OpenRouter
  spend explicitly against a pre-declared $2 sub-budget for this artifact before running the full sweep, estimating cost from
  the pass-1 subset first.
depends_on:
- id: art_mhfmDpGp4z1J
  label: dataset
  relation_type:
  relation_rationale:
- id: art_5ySTX4YfxqG_
  label: resource dossier
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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

--- Dependency 2 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 07:31:56 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Write · 2026-09-01 07:33:00 UTC

```
File: ./.terminal_claude_agent_struct_out.json

{
  "title": "Testing Whether Iteration Alone Fixes Span Edits",
  "summary": "Runs Condition C2 (narrow QE-span localization, but iteratively repaired and re-verified by the content-invariant checker, up to 3 passes, stopping on a certificate) on the same en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used in the prior B/D/C1 comparison. Reuses the prior experiment's checker.py and OpenRouter client verbatim by reading them from that artifact's workspace_path, regenerates the identical stratified 320-natural/240-injected-pool sample with the same seed, and reports ΔCOMET, fix rate, and true regression rate broken out by invariant category (not pooled) so the negation-deletion structural asymmetry is visible from first report. Spend is capped at a pre-declared $2 sub-budget, estimated from a pass-1 subset before the full sweep.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# === STEP 0: Locate and reuse the prior B/D/C1 artifact's code (no formal dep edge exists between two experiment artifacts) ===\nPRIOR_RUN_PATH = read from run tree: the workspace_path of the iter2 (or most recent completed) experiment artifact that produced the B/D/C1 comparison for this hypothesis lineage.\n  # Locate it by scanning sibling gen_art directories under .../3_invention_loop/iter_2/gen_art/ (or wherever the plan/orchestrator records it) for a method_out.json whose metadata names conditions B/D/C1 and this hypothesis's run_id.\n  # FAIL LOUD if not found: do not silently reimplement from scratch with different assumptions -- log a WARNING and fall back to re-deriving the checker/client from the resource dossier (Dependency 1) + this plan's spec, flagging every design choice as 'not verified identical to prior run' in metadata.\nASSERT prior method.py, checker.py, and any prompt-template constants exist at PRIOR_RUN_PATH; COPY (not re-derive) them into this workspace as checker.py, openrouter_client.py, verbatim, changing only import paths.\nASSERT the prior run's row-selection seed/stratification rule (natural=320, injected-pool=240, language_pair in {en-ru_RU, en-uk_UA}, fold=experimental_pool) is documented (in prior method_out.json metadata or method.py constants) -- COPY the exact seed value and stratification code, do not re-derive from the dataset independently, or C2's row set may silently diverge from B/D/C1's and invalidate paired comparison.\n\n# === STEP 1: Load and regenerate identical inputs ===\nLOAD full_data_out.json from Dependency 2 (dataset), both wmt25_task3_natural and injected_error_augmentation groups.\nFILTER language_pair in {en-ru_RU, en-uk_UA}, metadata_fold == 'experimental_pool'.\nREGENERATE the stratified sample using the copied seed/stratification code -> expect exactly 320 natural + 240 injected-pool rows (matching B/D/C1's N). ASSERT row IDs match if the prior run's row-ID list was logged; if not available, log this as a known limitation (comparison is population-matched, not row-matched) rather than silently assuming identity.\nFOR each injected row: extract invariant_category (named_entity_swap | number_unit_date_alteration | negation_polarity_flip | quantifier_substitution) and the corrupted_span/original_span/span_offsets fields, exactly as B/D/C1 consumed them.\n\n# === STEP 2: Define the oracle/QE span per row, INHERITING B/D's negation limitation explicitly ===\nFOR each row:\n  IF row is natural: span = row.qe_flagged_spans[0] (or the same span-selection rule B used, e.g. highest-severity span) -- COPY B's exact selection logic, do not invent a new one.\n  IF row is injected:\n    IF invariant_category == 'negation_polarity_flip':\n      span = ZERO-WIDTH (the corruption is a deletion: the negation marker was removed, so there is no contiguous substring in the corrupted text to mask/target).\n      LOG row.c2_attempted = False, row.skip_reason = 'negation_deletion_zero_width_span' -- do NOT silently drop the row from denominators; keep it in the per-category breakdown as a structural non-attempt, matching B/D's own treatment.\n    ELSE:\n      span = row.corrupted_span / row.span_offsets (the oracle span, exactly as B/D define it).\n\n# === STEP 3: C2 repair loop, per row (skip rows with c2_attempted = False) ===\nMAX_PASSES = 3\nFOR each eligible row:\n  pass_log = []\n  current_span_text = row.hypothesis_text[span.start:span.end]  # or corrupted_text slice for injected rows\n  certificate_achieved = False\n  FOR pass_num in 1..MAX_PASSES:\n    IF pass_num == 1:\n      repaired_span = call_openrouter(model='google/gemma-3-12b-it', prompt=MASK_AND_FILL_PROMPT(source_sentence, masked_span=='__BLANK__' substituted for current_span_text, context))\n      # Use the SAME masking prompt template as B/D (copied in Step 0), not a new one -- localization/model must be identical across B/D/C1/C2 per the hypothesis's factorial design.\n    ELSE:\n      # targeted re-repair: scope the prompt to exactly what the checker flagged on the previous pass\n      checker_verdict = run_checker(category=row.invariant_category, source=source_sentence, candidate_span=repaired_span, prior_pass=pass_log[-1])\n      IF checker_verdict.passed: BREAK  # should already have broken at end of prior pass; this is a safety re-check\n      repaired_span = call_openrouter(model='google/gemma-3-12b-it', prompt=TARGETED_REPAIR_PROMPT(source_sentence, current_span=repaired_span, checker_flag_detail=checker_verdict.detail))\n    checker_verdict = run_checker(category=row.invariant_category, source=source_sentence, candidate_span=repaired_span)\n    edit_volume = char_edit_distance(current_span_text_before_this_pass, repaired_span)\n    pass_log.append({pass_num, repaired_span, checker_verdict.passed, checker_verdict.detail, edit_volume, span_char_length=len(repaired_span)})\n    IF checker_verdict.passed:\n      certificate_achieved = True\n      BREAK\n    IF row.invariant_category NOT IN checker_covered_categories (per Dependency 1's language x category coverage table):\n      BREAK  # do not iterate on categories the checker cannot verify -- log as 'uncheckable_category_single_pass_only'\n    current_span_text = repaired_span\n  final_repaired_sentence = splice(row.hypothesis_text or row.corrupted_text, span, pass_log[-1].repaired_span) if pass_log else original\n  row.c2_result = {n_passes=len(pass_log), certificate_achieved, pass_log, final_repaired_sentence, char_length_trend=[p.span_char_length for p in pass_log]}\n\n# === STEP 4: Cost tracking gate (pre-declared $2 sub-budget) ===\nBEFORE full sweep: run STEP 3 on a 15-20 row pass-1-only subset (natural + injected, both languages), measure actual $/row from OpenRouter usage response, extrapolate to full N (560 rows x up to 3 passes worst case) -- if projected cost > $2, REDUCE either MAX_PASSES or row count and log the reduction with rationale BEFORE running the full sweep, not after overrunning.\nTRACK running cumulative spend after every batch of ~25 calls; HARD STOP the sweep if cumulative spend hits $2, logging which rows were skipped and why.\n\n# === STEP 5: Scoring ===\nFOR each row with a repair attempted: compute COMET(source, original_hypothesis) and COMET(source, final_repaired_sentence) via wmt22-cometkiwi-da (same checkpoint/install as B/D/C1, confirmed working per Dependency 1) -> row.delta_comet = repaired - original.\nFOR injected-pool rows: fix_rate = fraction where final checker_verdict.passed == True (among c2_attempted == True rows, denominator excludes negation zero-width rows but reports negation's exclusion count explicitly); true_regression_rate = fraction of rows where the span was checker-verified CORRECT pre-repair (i.e., natural rows or injected rows where corruption didn't actually break that specific checked property) but checker-verified VIOLATED post-repair, scored only against human-confirmed ground truth per Dependency 1/2's definitions.\nBREAK OUT fix_rate and true_regression_rate BY invariant_category (4 categories x 2 languages), NOT pooled -- report both the pooled figure AND the per-category table, with negation shown as 'N/A (structural non-attempt)' rather than folded into a 0% fix rate that would misleadingly count as failure.\nALSO report: pooled ΔCOMET (mean + 95% CI via bootstrap, same method as B/D/C1) per language pair and combined; edit volume per pass and gain-to-edit ratio; LLM calls/tokens per sentence (mean n_passes, since C2 multiplies calls vs single-pass B/D/C1); the CEGIS-narrowing signal (char_length_trend across passes for multi-pass rows -- does span length shrink toward a stable point, or diverge?).\n\n# === STEP 6: Direct comparability outputs ===\nBuild a side-by-side table: B, D, C1 (loaded from PRIOR_RUN_PATH/method_out.json) vs C2 (this run), same metrics, same row population, same language pairs -- this table is the artifact's primary deliverable, since the hypothesis's success criteria (b) requires C2 vs C1's comparison on regression rate and ΔCOMET improvement over D.\nWrite method_out.json with: per-row results, per-category/per-language breakdowns, the B/D/C1/C2 comparison table, cost log, and an explicit metadata block listing every place C2's setup could not be verified byte-identical to B/D/C1 (row IDs, seed provenance) as a limitations note.",
  "fallback_plan": "If PRIOR_RUN_PATH's checker.py/method.py cannot be located or read (workspace was pruned, path recorded incorrectly, or file structure differs from expected): fall back to re-implementing the checker and masking-prompt template directly from Dependency 1 (the resource dossier), using its verbatim Algorithm 1 pseudocode and masking prompt template quotes -- but explicitly log this as 'checker re-derived, not verified identical to prior B/D/C1 run' in method_out.json metadata, and treat any C2-vs-C1 comparison in this case as suggestive rather than a controlled paired comparison, flagging it prominently rather than presenting it as equivalent to a same-code rerun. If google/gemma-3-12b-it is unavailable on OpenRouter at run time (models get delisted, per Dependency 1's finding about TowerPlus-9B and gemma-2-9b-it), fall back to the next-ranked substitute from Dependency 1's re-ranked candidate table, and re-verify B's fidelity gate is not silently invalidated by noting the model swap explicitly (do not proceed as if nothing changed, since B/D/C1 were run on gemma-3-12b-it specifically). If the $2 sub-budget proves too tight after the pass-1 subset estimate (e.g., projected cost is $4+), first cut MAX_PASSES from 3 to 2 (losing some of the iteration signal but preserving the core narrow-vs-broad comparison), and if still over budget, reduce to a stratified subsample of ~150 rows (75 natural + 75 injected) balanced across both languages and all 4 categories rather than dropping a language pair entirely (dropping a language pair would break comparability with B/D/C1, which both cover en-ru_RU and en-uk_UA). If checker_covered_categories from Dependency 1 turns out not to cover a category for one of the two languages at acceptable precision/recall (per the within-experiment validation that gated C1), restrict C2's category scope to match exactly what C1 was validated and run on -- do not silently extend C2 to categories C1 itself was not permitted to touch, since that would make the C1-vs-C2 comparison apples-to-oranges. If wmt22-cometkiwi-da fails to load or run (checkpoint access issue, gated HF download problem despite Dependency 1's confirmed install command), fall back to a smaller COMET variant only if Dependency 1 lists one with reported behavior, log the substitution prominently, and flag any ΔCOMET comparison against B/D/C1's published −0.0108-scale numbers as not directly comparable.",
  "testing_plan": "1) Dry run on 5 rows (mix of natural and injected, both languages, covering at least 2 of the 4 invariant categories) using a hardcoded/mocked checker.py import to confirm the code successfully locates and imports checker.py + openrouter_client.py from PRIOR_RUN_PATH without modification -- if import fails, resolve the path/dependency issue before writing any new logic. 2) Run STEP 2-3's span-selection and negation-zero-width-skip logic on the full 240-row injected-pool sample WITHOUT calling any LLM (dry pass, mask/print only) and verify the negation_polarity_flip subset (expected ~12.5% x 240 ≈ 30 rows across both languages) is correctly flagged c2_attempted=False with the right skip_reason, and that this matches B/D's documented treatment of the same rows (cross-check against PRIOR_RUN_PATH/method_out.json's per-row logs if available) -- this is the single most error-prone piece of the design and must be verified before spending any budget. 3) Run the real pass-1-only cost-estimation subset (15-20 rows) with live OpenRouter calls to google/gemma-3-12b-it, confirm actual per-call cost and latency, and extrapolate to the full ~530 eligible-row x up-to-3-pass worst case against the $2 cap; adjust MAX_PASSES/row count per the fallback plan BEFORE proceeding if projected cost exceeds budget. 4) On that same 15-20 row subset, manually inspect 5-10 individual repair passes' checker verdicts and pass_log.char_length_trend for sanity (e.g., does a passing verdict actually correspond to a plausible-looking correct span; does a still-failing verdict after pass 2 show a narrower or at least different edit than pass 1, ruling out the model simply repeating the same wrong answer) -- this catches prompt-template bugs (e.g., wrong context window, garbled masking) before the full sweep. 5) Confirm COMET scoring on this pilot subset produces ΔCOMET values in a plausible range (roughly -0.05 to +0.05 per sentence, not wildly out of range like ±1.0, which would indicate a sentence-alignment or tokenization bug) before scaling to the full sample. 6) Only after 1-5 pass, run the full eligible-row sweep (~530 rows within budget), then verify the final method_out.json's B/D/C1-vs-C2 comparison table has non-degenerate per-category and per-language cells (no category/language cell with zero attempted rows going unnoted) and that cumulative spend logged in metadata is at or under the $2 sub-budget."
}
```

### [5] TOOL RESULT — Write · 2026-09-01 07:33:00 UTC

```
{"type": "create", "filePath": "./.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Testing Whether Iteration Alone Fixes Span Edits\",\n  \"summary\": \"Runs Condition C2 (narrow QE-span localization, but iteratively repaired and re-verified by the content-invariant checker, up to 3 passes, stopping on a certificate) on the same en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used in the prior B/D/C1 comparison. Reuses the prior experiment's checker.py and OpenRouter client verbatim by reading them from that artifact's workspace_path, regenerates the identical stratified 320-natural/240-injected-pool sample with the same seed, and reports ΔCOMET, fix rate, and true regression rate broken out by invariant category (not pooled) so the negation-deletion structural asymmetry is visible from first report. Spend is capped at a pre-declared $2 sub-budget, estimated from a pass-1 subset before the full sweep.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# === STEP 0: Locate and reuse the prior B/D/C1 artifact's code (no formal dep edge exists between two experiment artifacts) ===\\nPRIOR_RUN_PATH = read from run tree: the workspace_path of the iter2 (or most recent completed) experiment artifact that produced the B/D/C1 comparison for this hypothesis lineage.\\n  # Locate it by scanning sibling gen_art directories under .../3_invention_loop/iter_2/gen_art/ (or wherever the plan/orchestrator records it) for a method_out.json whose metadata names conditions B/D/C1 and this hypothesis's run_id.\\n  # FAIL LOUD if not found: do not silently reimplement from scratch with different assumptions -- log a WARNING and fall back to re-deriving the checker/client from the resource dossier (Dependency 1) + this plan's spec, flagging every design choice as 'not verified identical to prior run' in metadata.\\nASSERT prior method.py, checker.py, and any prompt-template constants exist at PRIOR_RUN_PATH; COPY (not re-derive) them into this workspace as checker.py, openrouter_client.py, verbatim, changing only import paths.\\nASSERT the prior run's row-selection seed/stratification rule (natural=320, injected-pool=240, language_pair in {en-ru_RU, en-uk_UA}, fold=experimental_pool) is documented (in prior method_out.json metadata or method.py constants) -- COPY the exact seed value and stratification code, do not re-derive from the dataset independently, or C2's row set may silently diverge from B/D/C1's and invalidate paired comparison.\\n\\n# === STEP 1: Load and regenerate identical inputs ===\\nLOAD full_data_out.json from Dependency 2 (dataset), both wmt25_task3_natural and injected_error_augmentation groups.\\nFILTER language_pair in {en-ru_RU, en-uk_UA}, metadata_fold == 'experimental_pool'.\\nREGENERATE the stratified sample using the copied seed/stratification code -> expect exactly 320 natural + 240 injected-pool rows (matching B/D/C1's N). ASSERT row IDs match if the prior run's row-ID list was logged; if not available, log this as a known limitation (comparison is population-matched, not row-matched) rather than silently assuming identity.\\nFOR each injected row: extract invariant_category (named_entity_swap | number_unit_date_alteration | negation_polarity_flip | quantifier_substitution) and the corrupted_span/original_span/span_offsets fields, exactly as B/D/C1 consumed them.\\n\\n# === STEP 2: Define the oracle/QE span per row, INHERITING B/D's negation limitation explicitly ===\\nFOR each row:\\n  IF row is natural: span = row.qe_flagged_spans[0] (or the same span-selection rule B used, e.g. highest-severity span) -- COPY B's exact selection logic, do not invent a new one.\\n  IF row is injected:\\n    IF invariant_category == 'negation_polarity_flip':\\n      span = ZERO-WIDTH (the corruption is a deletion: the negation marker was removed, so there is no contiguous substring in the corrupted text to mask/target).\\n      LOG row.c2_attempted = False, row.skip_reason = 'negation_deletion_zero_width_span' -- do NOT silently drop the row from denominators; keep it in the per-category breakdown as a structural non-attempt, matching B/D's own treatment.\\n    ELSE:\\n      span = row.corrupted_span / row.span_offsets (the oracle span, exactly as B/D define it).\\n\\n# === STEP 3: C2 repair loop, per row (skip rows with c2_attempted = False) ===\\nMAX_PASSES = 3\\nFOR each eligible row:\\n  pass_log = []\\n  current_span_text = row.hypothesis_text[span.start:span.end]  # or corrupted_text slice for injected rows\\n  certificate_achieved = False\\n  FOR pass_num in 1..MAX_PASSES:\\n    IF pass_num == 1:\\n      repaired_span = call_openrouter(model='google/gemma-3-12b-it', prompt=MASK_AND_FILL_PROMPT(source_sentence, masked_span=='__BLANK__' substituted for current_span_text, context))\\n      # Use the SAME masking prompt template as B/D (copied in Step 0), not a new one -- localization/model must be identical across B/D/C1/C2 per the hypothesis's factorial design.\\n    ELSE:\\n      # targeted re-repair: scope the prompt to exactly what the checker flagged on the previous pass\\n      checker_verdict = run_checker(category=row.invariant_category, source=source_sentence, candidate_span=repaired_span, prior_pass=pass_log[-1])\\n      IF checker_verdict.passed: BREAK  # should already have broken at end of prior pass; this is a safety re-check\\n      repaired_span = call_openrouter(model='google/gemma-3-12b-it', prompt=TARGETED_REPAIR_PROMPT(source_sentence, current_span=repaired_span, checker_flag_detail=checker_verdict.detail))\\n    checker_verdict = run_checker(category=row.invariant_category, source=source_sentence, candidate_span=repaired_span)\\n    edit_volume = char_edit_distance(current_span_text_before_this_pass, repaired_span)\\n    pass_log.append({pass_num, repaired_span, checker_verdict.passed, checker_verdict.detail, edit_volume, span_char_length=len(repaired_span)})\\n    IF checker_verdict.passed:\\n      certificate_achieved = True\\n      BREAK\\n    IF row.invariant_category NOT IN checker_covered_categories (per Dependency 1's language x category coverage table):\\n      BREAK  # do not iterate on categories the checker cannot verify -- log as 'uncheckable_category_single_pass_only'\\n    current_span_text = repaired_span\\n  final_repaired_sentence = splice(row.hypothesis_text or row.corrupted_text, span, pass_log[-1].repaired_span) if pass_log else original\\n  row.c2_result = {n_passes=len(pass_log), certificate_achieved, pass_log, final_repaired_sentence, char_length_trend=[p.span_char_length for p in pass_log]}\\n\\n# === STEP 4: Cost tracking gate (pre-declared $2 sub-budget) ===\\nBEFORE full sweep: run STEP 3 on a 15-20 row pass-1-only subset (natural + injected, both languages), measure actual $/row from OpenRouter usage response, extrapolate to full N (560 rows x up to 3 passes worst case) -- if projected cost > $2, REDUCE either MAX_PASSES or row count and log the reduction with rationale BEFORE running the full sweep, not after overrunning.\\nTRACK running cumulative spend after every batch of ~25 calls; HARD STOP the sweep if cumulative spend hits $2, logging which rows were skipped and why.\\n\\n# === STEP 5: Scoring ===\\nFOR each row with a repair attempted: compute COMET(source, original_hypothesis) and COMET(source, final_repaired_sentence) via wmt22-cometkiwi-da (same checkpoint/install as B/D/C1, confirmed working per Dependency 1) -> row.delta_comet = repaired - original.\\nFOR injected-pool rows: fix_rate = fraction where final checker_verdict.passed == True (among c2_attempted == True rows, denominator excludes negation zero-width rows but reports negation's exclusion count explicitly); true_regression_rate = fraction of rows where the span was checker-verified CORRECT pre-repair (i.e., natural rows or injected rows where corruption didn't actually break that specific checked property) but checker-verified VIOLATED post-repair, scored only against human-confirmed ground truth per Dependency 1/2's definitions.\\nBREAK OUT fix_rate and true_regression_rate BY invariant_category (4 categories x 2 languages), NOT pooled -- report both the pooled figure AND the per-category table, with negation shown as 'N/A (structural non-attempt)' rather than folded into a 0% fix rate that would misleadingly count as failure.\\nALSO report: pooled ΔCOMET (mean + 95% CI via bootstrap, same method as B/D/C1) per language pair and combined; edit volume per pass and gain-to-edit ratio; LLM calls/tokens per sentence (mean n_passes, since C2 multiplies calls vs single-pass B/D/C1); the CEGIS-narrowing signal (char_length_trend across passes for multi-pass rows -- does span length shrink toward a stable point, or diverge?).\\n\\n# === STEP 6: Direct comparability outputs ===\\nBuild a side-by-side table: B, D, C1 (loaded from PRIOR_RUN_PATH/method_out.json) vs C2 (this run), same metrics, same row population, same language pairs -- this table is the artifact's primary deliverable, since the hypothesis's success criteria (b) requires C2 vs C1's comparison on regression rate and ΔCOMET improvement over D.\\nWrite method_out.json with: per-row results, per-category/per-language breakdowns, the B/D/C1/C2 comparison table, cost log, and an explicit metadata block listing every place C2's setup could not be verified byte-identical to B/D/C1 (row IDs, seed provenance) as a limitations note.\",\n  \"fallback_plan\": \"If PRIOR_RUN_PATH's checker.py/method.py cannot be located or read (workspace was pruned, path recorded incorrectly, or file structure differs from expected): fall back to re-implementing the checker and masking-prompt template directly from Dependency 1 (the resource dossier), using its verbatim Algorithm 1 pseudocode and masking prompt template quotes -- but explicitly log this as 'checker re-derived, not verified identical to prior B/D/C1 run' in method_out.json metadata, and treat any C2-vs-C1 comparison in this case as suggestive rather than a controlled paired comparison, flagging it prominently rather than presenting it as equivalent to a same-code rerun. If google/gemma-3-12b-it is unavailable on OpenRouter at run time (models get delisted, per Dependency 1's finding about TowerPlus-9B and gemma-2-9b-it), fall back to the next-ranked substitute from Dependency 1's re-ranked candidate table, and re-verify B's fidelity gate is not silently invalidated by noting the model swap explicitly (do not proceed as if nothing changed, since B/D/C1 were run on gemma-3-12b-it specifically). If the $2 sub-budget proves too tight after the pass-1 subset estimate (e.g., projected cost is $4+), first cut MAX_PASSES from 3 to 2 (losing some of the iteration signal but preserving the core narrow-vs-broad comparison), and if still over budget, reduce to a stratified subsample of ~150 rows (75 natural + 75 injected) balanced across both languages and all 4 categories rather than dropping a language pair entirely (dropping a language pair would break comparability with B/D/C1, which both cover en-ru_RU and en-uk_UA). If checker_covered_categories from Dependency 1 turns out not to cover a category for one of the two languages at acceptable precision/recall (per the within-experiment validation that gated C1), restrict C2's category scope to match exactly what C1 was validated and run on -- do not silently extend C2 to categories C1 itself was not permitted to touch, since that would make the C1-vs-C2 comparison apples-to-oranges. If wmt22-cometkiwi-da fails to load or run (checkpoint access issue, gated HF download problem despite Dependency 1's confirmed install command), fall back to a smaller COMET variant only if Dependency 1 lists one with reported behavior, log the substitution prominently, and flag any ΔCOMET comparison against B/D/C1's published −0.0108-scale numbers as not directly comparable.\",\n  \"testing_plan\": \"1) Dry run on 5 rows (mix of natural and injected, both languages, covering at least 2 of the 4 invariant categories) using a hardcoded/mocked checker.py import to confirm the code successfully locates and imports checker.py + openrouter_client.py from PRIOR_RUN_PATH without modification -- if import fails, resolve the path/dependency issue before writing any new logic. 2) Run STEP 2-3's span-selection and negation-zero-width-skip logic on the full 240-row injected-pool sample WITHOUT calling any LLM (dry pass, mask/print only) and verify the negation_polarity_flip subset (expected ~12.5% x 240 ≈ 30 rows across both languages) is correctly flagged c2_attempted=False with the right skip_reason, and that this matches B/D's documented treatment of the same rows (cross-check against PRIOR_RUN_PATH/method_out.json's per-row logs if available) -- this is the single most error-prone piece of the design and must be verified before spending any budget. 3) Run the real pass-1-only cost-estimation subset (15-20 rows) with live OpenRouter calls to google/gemma-3-12b-it, confirm actual per-call cost and latency, and extrapolate to the full ~530 eligible-row x up-to-3-pass worst case against the $2 cap; adjust MAX_PASSES/row count per the fallback plan BEFORE proceeding if projected cost exceeds budget. 4) On that same 15-20 row subset, manually inspect 5-10 individual repair passes' checker verdicts and pass_log.char_length_trend for sanity (e.g., does a passing verdict actually correspond to a plausible-looking correct span; does a still-failing verdict after pass 2 show a narrower or at least different edit than pass 1, ruling out the model simply repeating the same wrong answer) -- this catches prompt-template bugs (e.g., wrong context window, garbled masking) before the full sweep. 5) Confirm COMET scoring on this pilot subset produces ΔCOMET values in a plausible range (roughly -0.05 to +0.05 per sentence, not wildly out of range like ±1.0, which would indicate a sentence-alignment or tokenization bug) before scaling to the full sample. 6) Only after 1-5 pass, run the full eligible-row sweep (~530 rows within budget), then verify the final method_out.json's B/D/C1-vs-C2 comparison table has non-degenerate per-category and per-language cells (no category/language cell with zero attempted rows going unnoted) and that cumulative spend logged in metadata is at or under the $2 sub-budget.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-09-01 07:33:02 UTC

```
Plan written to `./.terminal_claude_agent_struct_out.json` — it specifies Condition C2 (narrow QE-span localization, iterative repair+verify up to 3 passes with the same checker/model/rows as B/D/C1), including explicit handling of the negation zero-width-span limitation, per-category (not pooled) reporting, a $2 cost-gated rollout, and a staged testing plan (dry-run negation-skip logic → cost pilot → sanity checks → full sweep).
```
