# gen_plan_experiment_3 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_3` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 05:40:56 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_3
```

### [2] SYSTEM-USER prompt · 2026-09-01 05:41:04 UTC

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

id: experiment_iter2_dir3
type: experiment
objective: >-
  Run conditions D (condition B plus a trivial post-hoc hygiene filter, no invariant checker) and C1 (checker flags every
  invariant violation in the sentence, each repaired in one uncorrected pass, no re-verification) on the same 2 language pairs
  and same rows as the condition-B run, using the same fixed substitute repair model and the validated checker from the first
  artifact, so all three conditions (B, D, C1) are directly comparable on identical inputs.
approach: >-
  Reuse condition B's outputs and reproduce/extend the pipeline: for D, add a deterministic post-generation filter (regex/string
  checks for leftover __BLANK__-style tokens, garbled placeholder patterns, and leaked instruction-format strings like 'Corrected
  words: [...]') that triggers exactly one retry pass within the same single-pass budget when triggered. For C1, run the validated
  checker (from artifact 1) over the full sentence rather than only the QE-flagged span, and repair every category violation
  the checker flags -- excluding any (language, category) cell the checker-validation artifact flagged as below-threshold
  (documenting the Chinese/Japanese entity exclusion explicitly here too, not just in the checker report) -- each in one uncorrected
  repair pass with the same fixed model and prompt style as B/D. Score all three conditions identically: fix rate (against
  checker-verdict and, where available, QE/human-confirmed subset), true regression rate on the injected-error subset (known
  ground truth), mean ΔCOMET per language pair and pooled, edit volume relative to gain, and LLM calls/tokens per sentence.
  Report results separately per language pair and separately for natural vs injected subsets, matching the paper's stated
  reporting protocol.
depends_on:
- id: art_5ySTX4YfxqG_
  label: resource dossier
  relation_type:
  relation_rationale:
- id: art_mhfmDpGp4z1J
  label: dataset
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

### [3] HUMAN-USER prompt · 2026-09-01 05:41:04 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Write · 2026-09-01 05:41:56 UTC

```
File: /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-3-invention-loop-iter-2-gen-plan-gen-plan-experiment-3/feb669ec-9c3b-42f6-91e1-0ac86da51480/scratchpad/plan_output.json

placeholder
```

### [5] TOOL RESULT — Write · 2026-09-01 05:41:56 UTC

```
{"type": "create", "filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-3-invention-loop-iter-2-gen-plan-gen-plan-experiment-3/feb669ec-9c3b-42f6-91e1-0ac86da51480/scratchpad/plan_output.json", "content": "placeholder", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] TOOL CALL — Write · 2026-09-01 05:42:52 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_3/.terminal_claude_agent_struct_out.json

{
  "title": "Does hygiene or checking fix span-editing?",
  "summary": "Build the 4-category deterministic content-invariant checker, lightly validate it on the held-out injected-error split, then implement and run three matched conditions on identical rows from 2 language pairs (en->ru_RU, en->uk_UA) using the fixed substitute repair model google/gemma-3-12b-it: (B) faithful reproduction of Padmanabhan's masked-fill severity-skip system, (D) B plus a trivial hygiene retry filter (no checker), and (C1) checker flags every invariant in the sentence and repairs them all in one uncorrected pass (no re-verification). All three are scored identically (fix rate, human/injected-confirmed true regression rate, per-pair and pooled DeltaCOMET via Unbabel/wmt22-cometkiwi-da, edit volume, LLM calls/tokens) to establish whether D closes most of B's gap (ruling out 'just a regex bug') before the next iteration isolates the verification-loop conditions C2/C.",
  "runpod_compute_profile": "gpu",
  "implementation_pseudocode": "# uv inline script, pinned deps (loguru==0.7.3, unbabel-comet, requests), seeded RNG throughout\n\n## PHASE 0 -- Load + select scope\nload full_data_out.json from dataset artifact (art_mhfmDpGp4z1J)\nLANG_PAIRS = ['en-ru_RU', 'en-uk_UA']  # both Cyrillic-capitalization entity heuristic works, no Duckling gap reported for these two in the dossier (unlike cs_CZ/is_IS numbers, zh_CN/ja_JP entities) -- state this choice + rationale explicitly in method_out.json metadata\nnatural = filter(rows, group='wmt25_task3_natural', language_pair in LANG_PAIRS, metadata_fold == 'experimental_pool')\ninjected = filter(rows, group='injected_error_augmentation', language_pair in LANG_PAIRS)\n  split injected into: injected_heldout (metadata_fold == 'checker_validation_heldout') -- ONLY for checker P/R validation, never scored downstream\n                       injected_pool    (metadata_fold == 'experimental_pool')          -- used for true-regression-rate / fix-rate ground truth in B/D/C1\nstratified-subsample natural to ~150-200 rows/pair (balance domain) for cost control -- log exact seed + row ids kept\nstratified-subsample injected_pool to <=40 rows per (language_pair, category) cell (4 categories x 2 pairs <=320 rows)\nwrite selected_rows.json (row ids only) so B/D/C1 all consume the IDENTICAL row set\n\n## PHASE 1 -- Build + lightly validate the deterministic checker\nfor each of {named_entity, number_unit_date, negation_polarity, quantifier_scope} x {ru_RU, uk_UA}:\n    implement per resource dossier's language x category table (package/model names, cue lists, regex+boundary guards)\n    -- entity: NER (Stanza per dossier) + capitalization heuristic w/ accented-letter classes and Cyrillic-capital classes, function-word stoplist, sentence-boundary exclusion, corpus-frequency cap\n    -- number/unit/date: script-independent regex + Duckling where dossier lists no gap for ru_RU/uk_UA, else regex-only fallback, with boundary guards against handle-like tokens\n    -- negation polarity: per-language cue lists, word-boundary match, ONLY fire when exactly one negation marker present (documented negative-concord caveat)\n    -- quantifier scope: closed-class word list per dossier\nrun checker on injected_heldout (ground truth = original_span/corrupted_span/span_offsets already in the dataset)\ncompute precision/recall per (language, category) cell\nEXCLUDE any cell with recall < 0.5 OR precision < 0.5 from C1's repair scope -- document exact excluded cells (expect ru_RU/uk_UA to mostly clear this since dossier flagged them as lower-risk, but do not assume -- measure)\nwrite checker_validation.json (per-cell P/R, excluded-cell list) as part of method_out.json\n\n## PHASE 2 -- Condition B: faithful masked-fill reproduction\nfor row in natural_subsample:\n    qe_spans = row.qe_flagged_spans  # with severity in {minor, major, critical}\n    apply Algorithm 1 severity-skip heuristic verbatim from dossier: if any span severity != minor exists in the sentence, skip (do not mask) all minor-severity spans; else mask minor spans too\n    if no spans survive the skip heuristic: repair_output = original hypothesis (no edit made) -- log as 'no-op'\n    else:\n        masked_text = replace each surviving span with literal '__BLANK__' token (verbatim prompt template from dossier)\n        call google/gemma-3-12b-it ONCE via OpenRouter with the exact masking prompt template from the dossier, temperature=0 for determinism\n        repair_output = raw completion, NO post-processing, NO retry -- this is the point of condition B\n    log: row_id, spans_masked, raw_completion, repair_output, n_llm_calls=1 if masked else 0, tokens_in/out\nQUALITATIVE SANITY CHECK before trusting B further: scan repair_output for literal '__BLANK__' survival / garbled placeholder tokens / 'Corrected words:' leakage -- report the RATE of these vs Padmanabhan's documented failure signature; if the substitute model shows near-zero leakage (unlike the original weak 9B model), flag this explicitly as a fidelity caveat on all downstream B/D comparisons rather than silently proceeding\n\n## PHASE 3 -- Condition D: B + trivial hygiene retry filter\nfor row in natural_subsample:  # reuse B's masked_text and skip decisions exactly\n    same masking/skip logic as B\n    if masked: call model once -> output\n        if HYGIENE_REGEX.search(output):  # leftover '__BLANK__'/__[A-Z]+__ placeholder, or 'Corrected words:'/'Here is the corrected'-style leaked instruction text\n            call model AGAIN with the same prompt (temperature=0, or temperature=0.3 on retry only if temp=0 retry would be deterministic-identical -- document choice), single retry budget\n            output = retry_output regardless of whether the retry also fails (single-retry budget enforced, not iterate-to-verified)\n    else: output = original hypothesis (no-op, same as B)\n    log: row_id, n_llm_calls (1 or 2), hygiene_triggered bool, final output\n\n## PHASE 4 -- Condition C1: broadened localization, single uncorrected pass\nfor row in natural_subsample:\n    checker_flags = run validated checker (Phase 1, excluded cells removed) over the FULL sentence pair (source, hypothesis) -- not just qe_flagged_spans\n    if no flags: output = original hypothesis (no-op)\n    else:\n        build ONE repair prompt listing every flagged invariant (category, source span, hypothesis span, brief violation description) using the same base prompt style/model as B/D\n        call google/gemma-3-12b-it ONCE (single uncorrected pass, no re-verification against the checker after this call)\n        output = raw completion\n    log: row_id, n_flags, flag_categories, n_llm_calls=1 if flags else 0, output\n\n## PHASE 5 -- Scoring (identical protocol across B, D, C1)\nfor each condition in {B, D, C1}:\n    ΔCOMET: score(source, output) - score(source, original_hypothesis) via Unbabel/wmt22-cometkiwi-da (reference-free QE metric, matching Padmanabhan's reported metric exactly) -- report per language pair AND pooled mean with 95% bootstrap CI (row-level resample, 1000 iters)\n    fix_rate on injected_pool subset: for each injected row re-run condition's pipeline on the corrupted text, checker-verdict pass = corrupted span no longer flagged; ALSO report on the smaller human/QE-confirmed subset where available\n    true_regression_rate: fraction of invariants checker-confirmed OK pre-repair that checker-confirmed VIOLATED post-repair, computed on injected_pool (known ground truth) -- this is the paper's headline safety metric, report per condition per language pair\n    edit_volume: token-level edit distance(original_hypothesis, output) / len(original_hypothesis), to catch C1 drifting toward full retranslation\n    cost: n_llm_calls and total tokens per sentence, cumulative USD spend tracked live against the $10 cap (halt and report partial results if projected to exceed $10)\nwrite method_out.json: per-condition x per-language-pair x {natural, injected} metric tables, checker_validation.json contents, excluded-cell list, B's leakage-rate sanity-check result, full cost ledger, and an explicit STOP/reproduce-or-not verdict comparing B's ΔCOMET direction/magnitude against Padmanabhan's -0.0108 as documented fidelity evidence (not proof)",
  "fallback_plan": "If google/gemma-3-12b-it is unavailable or rate-limited on OpenRouter at execution time, fall back through the dossier's ranked substitute table in order (next-cheapest candidate with comparable parameter count) and re-run the same B fidelity sanity check before trusting D/C1 against it -- do not silently swap models mid-comparison. If COMET (wmt22-cometkiwi-da, gated HF download) fails to authenticate or download within budget, fall back to a non-gated reference-free QE proxy (e.g. wmt22-comet-qe-da or a publicly mirrored checkpoint) and clearly relabel all DeltaCOMET numbers as 'DeltaCOMET-proxy, not directly comparable to Padmanabhan's -0.0108' rather than reporting them under the original metric name. If GPU COMET throughput is far below the dossier's ~155 seg/sec V100 benchmark (e.g., a weaker RunPod GPU tier), reduce the natural/injected subsample sizes proportionally (floor: 60 rows/language pair natural, 15 rows/category/pair injected) rather than truncating the language-pair or condition coverage -- B vs D vs C1 comparability matters more than absolute row count. If the checker's precision/recall validation (Phase 1) shows BOTH language pairs failing threshold on 2+ of the 4 categories (worse than the dossier's optimistic read), do not abandon C1 -- narrow C1's repair scope to only the categories that clear threshold for that language pair, document the narrowing explicitly in method_out.json, and still report the comparison (a partial C1 that covers 2-3 of 4 categories is still informative about localization breadth vs D). If OpenRouter spend approaches $8 before all three conditions finish on both language pairs, complete condition coverage on ONE language pair fully before starting the second (uk_UA preferred to keep, since it has no known Duckling gap) rather than running both pairs partially -- a complete B/D/C1 triple on one pair is more useful than incomplete triples on two.",
  "testing_plan": "Step 1 (checker unit smoke test, $0, <2 min): run each of the 4 category detectors on 5 hand-picked injected_heldout rows per category per language pair where the ground-truth corrupted span is known; confirm the checker flags the corrupted span and does NOT flag 3 held-out clean control rows, before scaling to the full held-out fold. Step 2 (checker full validation, $0): run on the complete injected_heldout fold for both language pairs, compute per-cell P/R, and sanity-check against the dossier's stated expectations (e.g. confirm ru_RU/uk_UA entity detection is NOT hitting the zh/ja-style Latin-fallback recall gap, since these use Cyrillic capitals not that fallback path). Step 3 (condition B smoke test, ~10 rows, <$0.05): run B on 10 natural-subsample rows from one language pair, manually inspect the 10 raw completions for the documented leakage signature (literal '__BLANK__', 'Corrected words:' text) -- if leakage rate is near-zero (likely, since gemma-3-12b-it is more capable/better-instruction-following than the original TowerPlus-9B), record this explicitly as a fidelity limitation rather than treating B's near-term ΔCOMET as directly comparable to -0.0108. Step 4 (condition D/C1 smoke test, ~10 rows each, <$0.10 total): confirm D's hygiene regex actually triggers on at least one deliberately-corrupted synthetic example (unit-test the regex against a hand-crafted '__BLANK__ survived' string before trusting live retries), and confirm C1's repair prompt correctly lists multiple flagged invariants when a row has 2+ checker flags. Step 5 (cost dry run): after the 10-row smoke tests for B/D/C1, extrapolate total token cost x planned row count x 2 language pairs; if projected total exceeds $7 (leaving margin under the $10 cap), shrink the subsample sizes before committing to the full run. Step 6 (COMET sanity): score 5 known-identical (hypothesis, hypothesis) pairs and confirm ΔCOMET ≈ 0.000 as a scorer correctness check, then score 5 pairs where the injected corruption is known-severe and confirm ΔCOMET is clearly negative, before trusting the scorer on B/D/C1 outputs. Only after all six pass does the full-scale run (Phases 2-5 across both language pairs) proceed."
}
```

### [7] TOOL RESULT — Write · 2026-09-01 05:42:52 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_3/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Does hygiene or checking fix span-editing?\",\n  \"summary\": \"Build the 4-category deterministic content-invariant checker, lightly validate it on the held-out injected-error split, then implement and run three matched conditions on identical rows from 2 language pairs (en->ru_RU, en->uk_UA) using the fixed substitute repair model google/gemma-3-12b-it: (B) faithful reproduction of Padmanabhan's masked-fill severity-skip system, (D) B plus a trivial hygiene retry filter (no checker), and (C1) checker flags every invariant in the sentence and repairs them all in one uncorrected pass (no re-verification). All three are scored identically (fix rate, human/injected-confirmed true regression rate, per-pair and pooled DeltaCOMET via Unbabel/wmt22-cometkiwi-da, edit volume, LLM calls/tokens) to establish whether D closes most of B's gap (ruling out 'just a regex bug') before the next iteration isolates the verification-loop conditions C2/C.\",\n  \"runpod_compute_profile\": \"gpu\",\n  \"implementation_pseudocode\": \"# uv inline script, pinned deps (loguru==0.7.3, unbabel-comet, requests), seeded RNG throughout\\n\\n## PHASE 0 -- Load + select scope\\nload full_data_out.json from dataset artifact (art_mhfmDpGp4z1J)\\nLANG_PAIRS = ['en-ru_RU', 'en-uk_UA']  # both Cyrillic-capitalization entity heuristic works, no Duckling gap reported for these two in the dossier (unlike cs_CZ/is_IS numbers, zh_CN/ja_JP entities) -- state this choice + rationale explicitly in method_out.json metadata\\nnatural = filter(rows, group='wmt25_task3_natural', language_pair in LANG_PAIRS, metadata_fold == 'experimental_pool')\\ninjected = filter(rows, group='injected_error_augmentation', language_pair in LANG_PAIRS)\\n  split injected into: injected_heldout (metadata_fold == 'checker_validation_heldout') -- ONLY for checker P/R validation, never scored downstream\\n                       injected_pool    (metadata_fold == 'experimental_pool')          -- used for true-regression-rate / fix-rate ground truth in B/D/C1\\nstratified-subsample natural to ~150-200 rows/pair (balance domain) for cost control -- log exact seed + row ids kept\\nstratified-subsample injected_pool to <=40 rows per (language_pair, category) cell (4 categories x 2 pairs <=320 rows)\\nwrite selected_rows.json (row ids only) so B/D/C1 all consume the IDENTICAL row set\\n\\n## PHASE 1 -- Build + lightly validate the deterministic checker\\nfor each of {named_entity, number_unit_date, negation_polarity, quantifier_scope} x {ru_RU, uk_UA}:\\n    implement per resource dossier's language x category table (package/model names, cue lists, regex+boundary guards)\\n    -- entity: NER (Stanza per dossier) + capitalization heuristic w/ accented-letter classes and Cyrillic-capital classes, function-word stoplist, sentence-boundary exclusion, corpus-frequency cap\\n    -- number/unit/date: script-independent regex + Duckling where dossier lists no gap for ru_RU/uk_UA, else regex-only fallback, with boundary guards against handle-like tokens\\n    -- negation polarity: per-language cue lists, word-boundary match, ONLY fire when exactly one negation marker present (documented negative-concord caveat)\\n    -- quantifier scope: closed-class word list per dossier\\nrun checker on injected_heldout (ground truth = original_span/corrupted_span/span_offsets already in the dataset)\\ncompute precision/recall per (language, category) cell\\nEXCLUDE any cell with recall < 0.5 OR precision < 0.5 from C1's repair scope -- document exact excluded cells (expect ru_RU/uk_UA to mostly clear this since dossier flagged them as lower-risk, but do not assume -- measure)\\nwrite checker_validation.json (per-cell P/R, excluded-cell list) as part of method_out.json\\n\\n## PHASE 2 -- Condition B: faithful masked-fill reproduction\\nfor row in natural_subsample:\\n    qe_spans = row.qe_flagged_spans  # with severity in {minor, major, critical}\\n    apply Algorithm 1 severity-skip heuristic verbatim from dossier: if any span severity != minor exists in the sentence, skip (do not mask) all minor-severity spans; else mask minor spans too\\n    if no spans survive the skip heuristic: repair_output = original hypothesis (no edit made) -- log as 'no-op'\\n    else:\\n        masked_text = replace each surviving span with literal '__BLANK__' token (verbatim prompt template from dossier)\\n        call google/gemma-3-12b-it ONCE via OpenRouter with the exact masking prompt template from the dossier, temperature=0 for determinism\\n        repair_output = raw completion, NO post-processing, NO retry -- this is the point of condition B\\n    log: row_id, spans_masked, raw_completion, repair_output, n_llm_calls=1 if masked else 0, tokens_in/out\\nQUALITATIVE SANITY CHECK before trusting B further: scan repair_output for literal '__BLANK__' survival / garbled placeholder tokens / 'Corrected words:' leakage -- report the RATE of these vs Padmanabhan's documented failure signature; if the substitute model shows near-zero leakage (unlike the original weak 9B model), flag this explicitly as a fidelity caveat on all downstream B/D comparisons rather than silently proceeding\\n\\n## PHASE 3 -- Condition D: B + trivial hygiene retry filter\\nfor row in natural_subsample:  # reuse B's masked_text and skip decisions exactly\\n    same masking/skip logic as B\\n    if masked: call model once -> output\\n        if HYGIENE_REGEX.search(output):  # leftover '__BLANK__'/__[A-Z]+__ placeholder, or 'Corrected words:'/'Here is the corrected'-style leaked instruction text\\n            call model AGAIN with the same prompt (temperature=0, or temperature=0.3 on retry only if temp=0 retry would be deterministic-identical -- document choice), single retry budget\\n            output = retry_output regardless of whether the retry also fails (single-retry budget enforced, not iterate-to-verified)\\n    else: output = original hypothesis (no-op, same as B)\\n    log: row_id, n_llm_calls (1 or 2), hygiene_triggered bool, final output\\n\\n## PHASE 4 -- Condition C1: broadened localization, single uncorrected pass\\nfor row in natural_subsample:\\n    checker_flags = run validated checker (Phase 1, excluded cells removed) over the FULL sentence pair (source, hypothesis) -- not just qe_flagged_spans\\n    if no flags: output = original hypothesis (no-op)\\n    else:\\n        build ONE repair prompt listing every flagged invariant (category, source span, hypothesis span, brief violation description) using the same base prompt style/model as B/D\\n        call google/gemma-3-12b-it ONCE (single uncorrected pass, no re-verification against the checker after this call)\\n        output = raw completion\\n    log: row_id, n_flags, flag_categories, n_llm_calls=1 if flags else 0, output\\n\\n## PHASE 5 -- Scoring (identical protocol across B, D, C1)\\nfor each condition in {B, D, C1}:\\n    ΔCOMET: score(source, output) - score(source, original_hypothesis) via Unbabel/wmt22-cometkiwi-da (reference-free QE metric, matching Padmanabhan's reported metric exactly) -- report per language pair AND pooled mean with 95% bootstrap CI (row-level resample, 1000 iters)\\n    fix_rate on injected_pool subset: for each injected row re-run condition's pipeline on the corrupted text, checker-verdict pass = corrupted span no longer flagged; ALSO report on the smaller human/QE-confirmed subset where available\\n    true_regression_rate: fraction of invariants checker-confirmed OK pre-repair that checker-confirmed VIOLATED post-repair, computed on injected_pool (known ground truth) -- this is the paper's headline safety metric, report per condition per language pair\\n    edit_volume: token-level edit distance(original_hypothesis, output) / len(original_hypothesis), to catch C1 drifting toward full retranslation\\n    cost: n_llm_calls and total tokens per sentence, cumulative USD spend tracked live against the $10 cap (halt and report partial results if projected to exceed $10)\\nwrite method_out.json: per-condition x per-language-pair x {natural, injected} metric tables, checker_validation.json contents, excluded-cell list, B's leakage-rate sanity-check result, full cost ledger, and an explicit STOP/reproduce-or-not verdict comparing B's ΔCOMET direction/magnitude against Padmanabhan's -0.0108 as documented fidelity evidence (not proof)\",\n  \"fallback_plan\": \"If google/gemma-3-12b-it is unavailable or rate-limited on OpenRouter at execution time, fall back through the dossier's ranked substitute table in order (next-cheapest candidate with comparable parameter count) and re-run the same B fidelity sanity check before trusting D/C1 against it -- do not silently swap models mid-comparison. If COMET (wmt22-cometkiwi-da, gated HF download) fails to authenticate or download within budget, fall back to a non-gated reference-free QE proxy (e.g. wmt22-comet-qe-da or a publicly mirrored checkpoint) and clearly relabel all DeltaCOMET numbers as 'DeltaCOMET-proxy, not directly comparable to Padmanabhan's -0.0108' rather than reporting them under the original metric name. If GPU COMET throughput is far below the dossier's ~155 seg/sec V100 benchmark (e.g., a weaker RunPod GPU tier), reduce the natural/injected subsample sizes proportionally (floor: 60 rows/language pair natural, 15 rows/category/pair injected) rather than truncating the language-pair or condition coverage -- B vs D vs C1 comparability matters more than absolute row count. If the checker's precision/recall validation (Phase 1) shows BOTH language pairs failing threshold on 2+ of the 4 categories (worse than the dossier's optimistic read), do not abandon C1 -- narrow C1's repair scope to only the categories that clear threshold for that language pair, document the narrowing explicitly in method_out.json, and still report the comparison (a partial C1 that covers 2-3 of 4 categories is still informative about localization breadth vs D). If OpenRouter spend approaches $8 before all three conditions finish on both language pairs, complete condition coverage on ONE language pair fully before starting the second (uk_UA preferred to keep, since it has no known Duckling gap) rather than running both pairs partially -- a complete B/D/C1 triple on one pair is more useful than incomplete triples on two.\",\n  \"testing_plan\": \"Step 1 (checker unit smoke test, $0, <2 min): run each of the 4 category detectors on 5 hand-picked injected_heldout rows per category per language pair where the ground-truth corrupted span is known; confirm the checker flags the corrupted span and does NOT flag 3 held-out clean control rows, before scaling to the full held-out fold. Step 2 (checker full validation, $0): run on the complete injected_heldout fold for both language pairs, compute per-cell P/R, and sanity-check against the dossier's stated expectations (e.g. confirm ru_RU/uk_UA entity detection is NOT hitting the zh/ja-style Latin-fallback recall gap, since these use Cyrillic capitals not that fallback path). Step 3 (condition B smoke test, ~10 rows, <$0.05): run B on 10 natural-subsample rows from one language pair, manually inspect the 10 raw completions for the documented leakage signature (literal '__BLANK__', 'Corrected words:' text) -- if leakage rate is near-zero (likely, since gemma-3-12b-it is more capable/better-instruction-following than the original TowerPlus-9B), record this explicitly as a fidelity limitation rather than treating B's near-term ΔCOMET as directly comparable to -0.0108. Step 4 (condition D/C1 smoke test, ~10 rows each, <$0.10 total): confirm D's hygiene regex actually triggers on at least one deliberately-corrupted synthetic example (unit-test the regex against a hand-crafted '__BLANK__ survived' string before trusting live retries), and confirm C1's repair prompt correctly lists multiple flagged invariants when a row has 2+ checker flags. Step 5 (cost dry run): after the 10-row smoke tests for B/D/C1, extrapolate total token cost x planned row count x 2 language pairs; if projected total exceeds $7 (leaving margin under the $10 cap), shrink the subsample sizes before committing to the full run. Step 6 (COMET sanity): score 5 known-identical (hypothesis, hypothesis) pairs and confirm ΔCOMET ≈ 0.000 as a scorer correctness check, then score 5 pairs where the injected corruption is known-severe and confirm ΔCOMET is clearly negative, before trusting the scorer on B/D/C1 outputs. Only after all six pass does the full-scale run (Phases 2-5 across both language pairs) proceed.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [8] ASSISTANT · 2026-09-01 05:42:54 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json`: a self-contained experiment that builds/lightly-validates the 4-category checker, then runs conditions B (masked-fill reproduction), D (B + hygiene retry), and C1 (broadened checker localization, single-pass repair) on identical rows from en→ru_RU and en→uk_UA using the fixed substitute model `google/gemma-3-12b-it`, scored by DeltaCOMET, true regression rate, fix rate, edit volume, and cost — with staged smoke tests before the full run and explicit fallbacks for model/scorer/GPU/budget shortfalls.
```
