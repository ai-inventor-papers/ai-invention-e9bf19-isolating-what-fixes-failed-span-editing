# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 05:39:32 UTC

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 5
Remaining (including this one): 4
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: 'Ground the checker: data and method scoping before any repair runs'
objective: >-
  Lay the two foundations the whole B/D/C1/C2/C factorial design depends on before spending any repair-model budget: (1) a
  precise, reproducible methodology for a deterministic four-category content-invariant checker (entities, numbers/units/dates,
  negation polarity, quantifier scope) across six typologically diverse target languages (Chinese, Czech, Japanese, Icelandic,
  Russian, Ukrainian), including how to faithfully replicate Padmanabhan's severity-skip heuristic and matched ΔCOMET scoring;
  and (2) a standardized dataset combining WMT25 Task 3's real QE-annotated test data with a separately-labeled injected-error
  augmentation set, split into a checker-validation held-out sample and a main experimental pool. Getting these wrong (e.g.
  picking a negation-cue approach with no coverage in Japanese, or a dataset that conflates natural and injected errors so
  fix-rate and regression-rate cannot be reported per Padmanabhan's own protocol) would silently invalidate every downstream
  condition in iterations 2+, so this iteration is deliberately not yet running any repair model.
rationale: >-
  The hypothesis's own success criteria require reporting metrics separately for natural-error vs. injection-augmented subsets
  and per language pair, and require the checker's precision/recall to be validated against a human-annotated sample BEFORE
  it is trusted as scoring ground truth (assumption 1). Multilingual invariant detection is genuinely uneven in difficulty
  -- negation cue lists and off-the-shelf NER differ sharply in maturity between, say, Russian and Icelandic or Japanese --
  so committing to a checker design without first surveying what actually exists per language risks building condition C1/C2/C
  on a checker that silently fails on 2 of 6 languages, which would contaminate every headline comparison in later iterations.
  Likewise, WMT25 Task 3 data plus a matching injected-error set is a REQUIRED input for every condition (B, D, C1, C2, C)
  and for the checker validation step itself; per the dependency rules, an EXPERIMENT this iteration cannot yet depend_on
  a DATASET produced in this same iteration (no existing artifacts to reference), so the correct sequencing is to finish research
  and data acquisition now and let iteration 2's experiments formally depend on this iteration's dataset artifact. This keeps
  the artifact pool focused and avoids the common failure mode of scattering shallow work across five artifacts when only
  two well-executed ones are load-bearing right now.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Produce an implementation-ready methodology dossier for (a) the deterministic four-category content-invariant checker
    across all six WMT25 Task 3 target languages, (b) faithful replication of Padmanabhan's masked-fill baseline including
    the exact severity-skip heuristic (Algorithm 1) and prompt format that produced the '__HEARTBREAK__' and 'Corrected words:'
    leakage bugs, (c) TowerPlus-9B access via OpenRouter (exact model id, pricing, context window, whether it supports the
    six target languages at comparable quality) so the SAME model can be held fixed across every repair-performing condition,
    and (d) the exact COMET model/version and scoring protocol needed to reproduce ΔCOMET numbers directly comparable to Padmanabhan's
    -0.0108 and the WMT25 findings paper's Table 15.
  approach: >-
    Re-fetch and fetch_grep Padmanabhan (2025) Appendix B and Algorithm 1 for the precise severity-skip logic and prompt templates
    (not paraphrase); fetch_grep the WMT25 findings paper Section 6.4/Table 15 for exact per-language-pair ΔCOMET figures
    to target for comparison; search for and evaluate off-the-shelf NER (e.g. multilingual spaCy/stanza/Flair models covering
    Zh/Cs/Ja/Is/Ru/Uk), negation-cue-list resources or existing negation-scope datasets per language, quantifier closed-class
    word lists per language, and cross-lingual number/unit/date alignment approaches (regex plus a lightweight NL number-word
    normalizer); confirm on OpenRouter the exact identifier and per-token pricing for TowerPlus-9B (or the closest available
    equivalent if unlisted, documenting the substitution honestly) and for the COMET scoring path (a HuggingFace COMET checkpoint
    run locally, since COMET itself is not an LLM call); document known weak spots per language (e.g. Japanese lacking a clean
    morphological negation marker inventory, quantifier scope ambiguity in Russian aspect) so the checker experiment in the
    next iteration is not designed blind. Output a decision table: language x invariant-category x proposed detection method
    x expected precision/recall ceiling x known failure modes.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Acquire and standardize the real WMT25 Task 3 evaluation data (source segments, MT system outputs, QE-flagged error spans,
    human severity/error-type annotations, and reference-free QE scores where available) for all six language pairs (En->Zh,
    Cs, Ja, Is, Ru, Uk) across the task's five domains, plus a separately-flagged injected-error augmentation set covering
    the four checkable invariant categories (named entities, numbers/units/dates, negation polarity, quantifier scope), built
    by programmatically corrupting a held-out subset of otherwise-clean human/reference translations with category-labeled,
    human-verifiable violations.
  approach: >-
    Locate and download the official WMT25 Quality Estimation / Automated Translation Evaluation shared task data release
    (test sets, MQM/ESA-style human annotations, QE error-span annotations) from its official repository/OSF/WMT page -- the
    same release Padmanabhan (2025) and the WMT25 findings paper use -- verifying license and completeness for all six pairs
    and five domains; if the official annotated test set is not fully public, substitute the closest available equivalent
    (e.g. prior WMT MQM-annotated test sets for the same language pairs) and document the substitution and its limitations
    explicitly rather than silently degrading scope. Standardize to rows of {source_text, target_text, language_pair, domain,
    qe_flagged_spans, human_error_annotations (type/severity/span), metadata_fold} with a clean train/mini/preview split.
    Separately construct the injected-error subset: sample clean translations, apply deterministic category-specific corruptions
    (swap a named entity for a distractor of the same type, alter a number/unit/date by a verifiable amount, flip a negation
    cue, substitute a quantifier), and store the exact ground-truth violation span and category alongside each corrupted row
    so downstream fix-rate and true-regression-rate metrics can be scored against known-correct labels, not just checker output.
    Reserve an explicit held-out validation slice (natural + injected, human-checkable) sized for a defensible precision/recall
    estimate of the checker to be built next iteration, kept disjoint from the main experimental pool used for the B/D/C1/C2/C
    comparison.
  depends_on: []
expected_outcome: >-
  A methodology dossier that commits to a concrete, per-language, per-invariant-category detection approach and a faithful
  replication plan for Padmanabhan's baseline and OpenRouter-hosted TowerPlus-9B, plus a standardized, schema-validated dataset
  artifact (natural WMT25 Task 3 data with QE/human annotations across six language pairs and five domains, an injected-error
  augmentation set with ground-truth violation labels, and a disjoint checker-validation slice) that the next iteration's
  checker-build experiment and the full B/D/C1/C2/C conditions experiment can both depend on directly.
summary: >-
  Iteration 1 deliberately does no repair-model or checker experiments yet: it scopes the multilingual invariant-checking
  methodology and Padmanabhan-replication details via research, and acquires and standardizes the real WMT25 Task 3 data plus
  an injected-error augmentation set via a dataset artifact, so that iteration 2 can build and validate the checker and run
  the full five-condition experiment against a dependency graph that actually exists.
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
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Introduction

Machine translation systems increasingly ship with an automatic quality-estimation (QE) step that flags likely errors in a translation without needing a human reference [1]. The natural next question is whether those flags can drive automatic repair: instead of retranslating a whole sentence to fix one wrong number or dropped negation, an editing system could touch only the flagged span and leave the rest of the sentence -- which the base translator already got right -- untouched. This is *scoped editing*: localize a problem with QE, then repair only that region.

Scoped editing matters because full retranslation is not free, and because the two failure modes are not equivalent. A model that regenerates an entire sentence can silently break a correct number, a correct name, or a correct negation while fixing something else; the total-sentence quality metrics used to score MT systems, such as COMET, do not distinguish "improved and stayed faithful" from "improved by chance while corrupting a different part of the sentence" [2]. In a regulated, terminology-heavy domain -- legal, medical, financial translation -- a single flipped number or negation is a severe, auditable failure independent of whether the sentence's aggregate quality score went up. A repair strategy that only ever touches what it is told is broken, and that can prove it did not break anything else, is the more defensible tool for that setting even when its aggregate quality gain is smaller than full retranslation's.

The 2025 WMT shared task on automated translation evaluation (Task 3, minimal editing) gave scoped editing its first head-to-head test against full retranslation and QE-informed selection, scored the same way across eight submitted systems [3]. The result looked bad for the idea: a scoped-editing system that masks each QE-flagged span with a placeholder token and fills it with one pass of a small (9-billion-parameter) language model scored -0.0108 mean $\Delta$COMET, the single worst result in the ranking -- while the same team's sibling system, which retranslates the whole sentence with six candidate large language models and keeps the QE-best one, scored +0.0201 [4]. Read as a single data point, this is a clean argument against scoped editing: check one span, touch one span, and you still do worse than not checking anything and just regenerating everything.

That reading does not survive reading the losing system's own account of itself. The paper documents concrete implementation failures behind its number: a literal, unfilled placeholder token surviving into the output as garbled text, bracketed prompt-format instructions ("Corrected words: [...]") leaking into the translated string, and a severity heuristic that skips minor-severity spans whenever a more severe span is present in the same sentence, silently narrowing what actually gets edited [4]. None of these are failures of scoped editing as a strategy; they are bugs and a resource shortfall (one 9B model, chosen for this system alone, against a six-model pool for its sibling). More decisively, the same shared-task ranking contains a second, independently built scoped-editing system -- an organizer baseline that feeds a fine-grained error detector into a 27-billion-parameter correction model -- and it lands in third place with mixed, near-zero $\Delta$COMET (0.000 on English-Czech, +0.007 on English-Icelandic, +0.002 on English-Russian) rather than the first system's consistently negative range (-0.007 to -0.014 on the same three pairs) [3]. Two systems attempting the same strategy on the same data landed in opposite territory. That task-internal contrast is the evidence this paper builds on: scoped editing's apparent failure in this shared task is confounded with model capability and implementation hygiene, and the confound has to be removed before any claim about the strategy itself -- including a claim in its favor -- is credible.

Existing machine-translation post-editing work does not isolate that confound because none of it holds localization and iteration apart as separate, independently switchable ingredients. QE-assisted post-editing systems fold word-level QE into a jointly trained encoder-decoder that still regenerates the full target sentence in every configuration, reducing but not eliminating over-correction rather than freezing untouched spans [5]. A follow-up system constrains decoding to keep QE-marked "OK" tokens fixed while a beam search still reorders and rephrases around them, and its own ablation shows the ceiling is bounded by QE tag accuracy in a way that is never made explicit or separately measured [6]. Prompting a large language model with error annotations improves post-editing quality but does not test whether verifying the model's own edit and looping back on failure adds anything beyond a single corrective pass [7]. None of these designs match a fixed repair model across conditions, so a capability difference and a mechanism difference are never disentangled -- exactly the ambiguity this shared-task result exposes. The general pattern of iterating a language model's own output against feedback until it passes a check, without an external verifier, is known to be unreliable when the model must judge its own work [8]; a deterministic, non-learned checker is a cleaner instrument for the specific question of whether iteration helps, but no prior scoped-editing study uses one this way.

This paper's contribution is a controlled protocol for asking the load-bearing-mechanism question honestly, plus the infrastructure to run it without further design decisions. Borrowing the structure of counterexample-guided inductive synthesis (CEGIS) from program synthesis -- propose a candidate, let a verifier either certify it or return a concrete counterexample that scopes the next repair, and stop on an explicit certificate rather than a fixed number of passes [9] -- we specify five conditions that share one repair model and vary exactly two things: how much of the sentence a deterministic checker is allowed to flag, and whether a flagged span is repaired once or iteratively re-verified. A condition that only fixes output hygiene (leftover placeholder tokens, leaked prompt text), with no invariant checker at all, is included specifically to measure how much of the original system's gap a one-line filter would close before crediting anything more sophisticated. This iteration delivers the diagnostic reading above, a fully resolved replication specification for the losing system (exact masking prompt, exact scorer, and a documented, unavoidable model substitution forced by a change in third-party model hosting since the original study), and a validated dataset built to run all five conditions. The comparative run itself is left to the next iteration, and we say so plainly rather than presenting protocol work as if it answered the mechanism question.

[FIGURE:fig1]

**Summary of contributions.**

- A reconciled, source-verified account of WMT25 Task 3's evidence, showing that a stronger-model scoped-editing system in the same ranking lands near break-even where the weaker one lands last, which locates the field's negative result in model capability and implementation hygiene rather than settling whether scoped editing with verification can work (Section 1, Section 6).
- A factorial protocol -- baseline, hygiene-only, broadened localization, iterative verification, and both combined -- that fixes the repair model across every repair-performing condition specifically so no measured difference can be attributed to model capability (Section 4).
- A fully resolved replication specification for the original masked-fill system, including a documented, forced substitution of the original 9-billion-parameter repair model after confirming its absence from every third-party hosting route we checked (Section 4.4).
- A validated 8,519-row dataset combining the complete WMT25 Task 3 test set with its released quality-estimation flags and a controlled, category-labeled error-injection set built from a disjoint, human-post-edited corpus, split so that checker validation and system comparison never draw on the same rows (Section 5).
- An explicit statement of what this iteration does and does not establish: the confound diagnosis is evidence-backed; the localization-versus-verification question is specified but not yet run (Section 7).

# Related Work

**Quality-estimation-informed post-editing.** Automatic post-editing systems that use word-level QE as a training signal jointly train an encoder-decoder that regenerates the full target sentence in every variant; adding the QE signal reduces over-correction (18.30 vs. 19.39 TER) but never freezes a QE-clean span, so the model can still rewrite text no error was ever flagged in [5]. A later system replaces the auxiliary-signal approach with Grid Beam Search, forcing QE-tagged "OK" spans as lexical constraints while the decoder keeps freedom to reorder and rephrase around them; this is closer to scoped editing in spirit but is a soft constraint on regeneration rather than a frozen, iteratively verified span, and the paper's own oracle-versus-predicted-tag gap of 0.3-1.3 TER shows the method's ceiling is set by QE tag accuracy without ever isolating that dependency as a separate factor [6]. Prompting large language models directly with structured error annotations improves post-editing outcomes over unstructured feedback, establishing that the format of the correction signal matters, but every condition in that study still regenerates the sentence and none tests a repair-then-verify loop against a single-pass repair with the same signal [7]. A related line automatically predicts MQM-style error spans and post-edits with them inside an LLM-as-judge evaluation pipeline, again as a one-shot correction step rather than an iterated one [10].

**Localized and energy-guided editing.** Locate-and-edit approaches to controlled text generation obtain a full generation from a base model, then use an energy function to find and replace only the spans that violate a stated constraint, explicitly to avoid the semantic drift full regeneration under a constraint tends to introduce [11]. This is the closest existing mechanism to the localization half of our design, but it has not been applied to machine translation, is not paired with an explicit stopping certificate, and -- like the MT-specific systems above -- has not been evaluated against a documented real-world failure of naive scoped editing with localization breadth and iteration held apart as separate variables.

**Iterative self-refinement.** Self-Refine shows that a single language model can generate an output, critique its own output, and revise it over several rounds without external supervision, improving results on tasks from code optimization to dialogue response generation [8]. The mechanism we test for machine translation -- iterate a repair against a check until it passes -- is structurally related, but Self-Refine's critique step is the same model judging its own work, which is known to be an unreliable verifier of the model's own errors; our design instead iterates against a deterministic, non-learned checker precisely to avoid that confound, and treats the presence versus absence of any re-verification (learned or not) as the variable under test rather than assuming it helps.

**Counterexample-guided synthesis.** CEGIS is a synthesis loop in which a candidate is checked against a specification by a verifier that either certifies it or returns a concrete counterexample scoping the next candidate, terminating on an explicit certificate rather than a fixed budget [9]. We do not import CEGIS as a synthesis algorithm; we import its separation of concerns -- what the verifier is allowed to see (localization breadth) versus whether the loop is allowed to run more than once (iteration) -- as the factorial structure of our protocol, which to our knowledge has not been applied to machine-translation post-editing.

**Evaluation infrastructure.** All $\Delta$COMET figures in this paper and in the shared task we build on are computed with the same reference-free quality-estimation checkpoint, `wmt22-cometkiwi-da` [2], distinct in both purpose and license from the neural framework it descends from [2] and from the fine-grained error-detection model, xCOMET, that a subsequent quality-estimation shared task and one Task 3 baseline use as an input signal rather than a scoring metric [12,13]. Our natural-error data is WMT25 Task 3's released test set [3]; our injected-error data is built from WMT24++, a disjoint, human-post-edited multilingual corpus spanning 55 languages and dialects [14].

# Preliminaries

We define four terms used throughout the protocol.

A **content invariant** is a piece of source-sentence meaning -- a named entity, a number, unit, or date, a negation polarity marker, or a quantifier -- that must survive translation, and that can be checked deterministically (via named-entity recognition, regular expressions, cue-word lists, or alignment) rather than judged by a learned model. We check four invariant categories: entity identity, number/unit/date value, negation polarity, and quantifier scope.

A translation's **certificate** is the state in which every content invariant extracted from its source sentence has been checked and passes. A certificate is an explicit, auditable stopping condition; a system either produces one or exhausts its edit budget without producing one, and which of the two happened is itself a recorded outcome, not something a $\Delta$COMET number alone can distinguish.

**Localization breadth** is how much of the sentence a system is allowed to flag as needing repair. *Narrow* localization repairs only the span the original quality-estimation model flagged; *broad* localization repairs every invariant our checker finds violated, whether or not quality estimation flagged it.

**Iteration** is whether a flagged span, once repaired, is re-checked and re-repaired if it still fails, up to a fixed pass budget, or whether the system accepts a single repair pass unconditionally. These two factors -- localization breadth and iteration -- are the two ingredients this protocol holds apart.

# Method

## Design Rationale

Our method isolates localization from verification by construction. The shared-task contrast in Section 1 leaves two explanations for the losing system's failure open at once: it could be that scoped editing without any re-verification is fundamentally worse than full retranslation, or it could be that a small, buggy, single-pass repair model was simply going to fail regardless of what strategy wrapped it. A protocol that changes both the localization scope and the presence of iteration at the same time as it changes the repair model, as the shared task's two natural systems effectively do, cannot separate these. Our protocol removes the confound in two steps: it fixes the repair model identically across every condition that performs a repair, and it varies localization breadth and iteration as two independently switchable factors rather than one bundled "use the improved system" toggle.

## Five Conditions

All five conditions share one deterministic content-invariant checker (Section 5.3) and, in every condition that performs a language-model repair, one fixed repair model.

**Condition B (faithful baseline).** A reproduction of the original masked-fill system: the quality-estimation model's flagged span is masked with a placeholder token according to the paper's severity-conditioned masking rule (mask nothing above a 0.90 QE score; mask only major-severity spans, or all spans if only minor-severity ones exist, between 0.50 and 0.90; mask everything below 0.50), filled with one repair-model pass, and accepted without any check [4]. This condition is expected to reproduce the original failure modes, including leftover placeholder tokens and skipped minor-severity spans, and is scored the same way to confirm the reproduction before anything else is measured.

**Condition D (hygiene filter, no checker).** Condition B, plus a trivial post-hoc filter that detects and retries -- within the same single-pass budget -- any output containing a leftover mask token, garbled placeholder text, or leaked instruction-format text. No content-invariant checker is involved. This condition measures how much of condition B's gap to full retranslation is explained by basic output hygiene alone, before any credit goes to a more sophisticated mechanism -- crediting a certified verification loop for catching a bug a regular-expression filter would also catch is not an interesting finding, and condition D is designed specifically to rule that out.

**Condition C1 (broad localization, single pass).** The checker flags every invariant violation in the sentence, not only the original quality-estimation span; each flagged violation is repaired in one uncorrected pass, with no re-verification. This condition isolates the effect of broadening what gets checked while holding iteration fixed at "none."

**Condition C2 (narrow localization, iterative verification).** Localization stays restricted to the original quality-estimation-flagged span, but that span is repaired, re-checked by the checker, and re-repaired if it still fails, up to the shared pass budget, stopping on a certificate. This condition isolates the effect of iteration while holding localization fixed at "narrow."

**Condition C (broad localization, iterative verification).** Both changes combined: every checker-flagged invariant is repaired and re-verified to a certificate or budget exhaustion.

A severity-matched variant of C1, C2, and C additionally respects condition B's minor-severity-skip rule, to check whether any gain from broadened localization is partly just "repair more things" rather than a change specific to the checker's mechanism.

## Metrics

For all five conditions and their severity-matched variants, the protocol measures, matching the shared task's own reporting where possible for direct comparability to its -0.0108 and +0.0201 figures: (i) fix rate on the four checkable categories, scored against both all flagged repairs and the human-confirmed subset; (ii) true regression rate, the fraction of invariants correct before repair that a repair step breaks, scored only against human-confirmed violations so the metric is not inflated by the checker's own false positives; (iii) mean $\Delta$COMET using the same checkpoint the shared task used [2]; (iv) edit volume relative to gain, to confirm condition C does not degenerate into full-sentence regeneration by its final pass; and (v) language-model calls and tokens per sentence, since conditions C2 and C multiply calls relative to B, D, and C1.

## Repair-Model Resolution

The original system's repair model, a 9-billion-parameter machine-translation-tuned language model built on a Gemma-2 base, is required to be identical across every repair-performing condition so that no measured difference can be attributed to model capability rather than protocol design. Confirming this model's continued availability through the third-party hosting route the original plan assumed took three independent checks [ARTIFACT:art_5ySTX4YfxqG_]: a full regular-expression sweep of that route's live model catalog (over 700,000 characters of listing text) returned zero matches for the model or its publisher; the model's own hosting page listed no active serving provider; and a targeted search of major inference hosts found no listing anywhere. A second, independent check found that the specific same-base substitute the original plan had assumed was still available had also since been delisted from the same catalog. This is not a data artifact but a real and reproducible constraint: the third-party model catalog this protocol depends on changed between the shared task's publication and this replication attempt, on a timescale of weeks. We resolve it with a documented substitution to a same-lineage, similarly-sized instruction-tuned model with confirmed live pricing and context length, while recording as an explicit limitation that the substitute lacks the original model's machine-translation-specific fine-tuning -- a difference that could itself confound a measured gap and that the next iteration must report alongside, not instead of, the protocol's own comparison.

# Data

## Natural Errors: WMT25 Task 3

We use the complete WMT25 Task 3 combined test set: 6,000 translations, 1,000 for each of six English-source language pairs (Chinese, Czech, Icelandic, Japanese, Russian, Ukrainian), spanning five domains -- news (1,808 rows), social media (1,684), speech (1,416), literary text (1,064), and dialogue (28) [ARTIFACT:art_mhfmDpGp4z1J]. Every row carries the quality-estimation model's flagged error spans as released with the test set: character offsets and a severity label in \{minor, major, critical\}. 5,700 of the 6,000 rows carry at least one flagged span; across all flagged spans, 45,611 are labeled major, 14,741 critical, and 1,336 minor. This last figure matters directly for condition B's severity-skip rule: only 2.2% of all flagged spans are minor-severity, so the rule that skips minor spans whenever a more severe span co-occurs in the same sentence affects a small but not negligible fraction of the data, and its effect is measured explicitly by the severity-matched C1/C2/C variants rather than assumed away.

[FIGURE:fig5]

We searched for a post-hoc human-annotated error-type layer to use as scoring ground truth beyond the released quality-estimation flags and did not find one publicly available for this test set; the release's designated field for this is empty across all 6,000 rows. We record this gap explicitly rather than treating the quality-estimation flags as equivalent to human-verified ground truth -- they are what the original system was localized against, and we use them the same way, but "true regression rate" (Section 4.3) is scored only where a human check is possible, which the natural-error subset alone cannot fully provide.

## Injected Errors: A Controlled Complement

Because natural incidence of any single invariant category can be low and because natural rows have no ground truth for the checker itself, we built a controlled complement from WMT24++, a corpus of human post-edited translations across 55 languages and dialects that is wholly disjoint from WMT25 Task 3 in both source year and content [14]. We took clean, human-authored target text for the same six language pairs and programmatically corrupted it into one of four invariant categories: named-entity swap, number/unit/date alteration, negation polarity flip, and quantifier substitution, producing 2,519 rows balanced up to 130 per language-pair-by-category cell (negation flips: 724 rows; entity swaps: 656; number/unit/date alterations: 651; quantifier substitutions: 488) [ARTIFACT:art_mhfmDpGp4z1J]. Each injected row carries the pre-corruption clean text, the corrupted text, and the exact character span of the change, so a checker's precision and recall against a known answer can be computed directly rather than estimated.

Category construction used language-appropriate methods rather than one rule applied uniformly: negation and quantifier corruptions use per-language cue-word lists and only fire when a sentence contains exactly one negation marker, because several of the target languages permit multiple co-occurring negation markers (negative concord), where removing one does not reliably flip the sentence's polarity. Entity detection for the four space-delimited, capitalization-marking languages (Czech, Icelandic, Russian, Ukrainian) uses a capitalization heuristic filtered by a per-language function-word stoplist, a sentence-boundary exclusion, and a corpus-frequency cap, since genuine proper nouns recur rarely across roughly 960 rows per language while capitalized function words recur often. Chinese and Japanese carry no capitalization signal at all, so entity detection there is limited to embedded Latin-script substrings -- a documented, lower-recall gap relative to a full multilingual named-entity pass rather than a claim of equivalent coverage, and it is reported as such in the dataset's own metadata rather than silently assumed to match the other four languages.

Both dataset groups are split by language pair (and, for the injected set, by language pair and category) into an experimental pool (4,920 of 6,000 natural rows, 2,071 of 2,519 injected rows -- roughly 82% of each) and a checker-validation holdout (1,080 natural, 448 injected -- roughly 18% of each), kept strictly disjoint so that validating the checker's precision and recall never draws on the same rows used for the five-condition system comparison.

[FIGURE:fig2]

Figure 2 summarizes this composition: 6,000 natural WMT25 Task 3 rows across six language pairs and five domains, and 2,519 injected-error rows across the same six language pairs and four invariant categories. Every category and language pair the protocol needs is represented, including the two smallest injected cells (Japanese number/unit/date alterations at 18 rows and Japanese named-entity swaps at 55 rows), both below the 130-row target because Japanese has no capitalization signal to drive the corpus-frequency-capped entity heuristic and a script-independent numeral count that is genuinely lower in the source corpus for that pair -- a limitation the dataset's own metadata documents rather than concealing behind a rebalanced total.

## Scoring and Repair Infrastructure

$\Delta$COMET throughout this protocol is computed with `wmt22-cometkiwi-da`, the same checkpoint the shared task's organizers footnote as the exact scorer behind every entry in its results table, confirmed against the organizers' findings paper rather than inferred from the shared task's name [2,3] [ARTIFACT:art_5ySTX4YfxqG_]. The checkpoint is released under a non-commercial license and requires accepting its terms before download, separately from the Apache-licensed scoring package that runs it [15,16]. A throughput benchmark from an independent evaluation-tooling paper, timing the same underlying scorer on over 360,000 real segments, reports approximately 155 segments per second on one GPU and approximately 648 on eight [17]; no CPU-only benchmark for this checkpoint exists in any source we checked, and we report that absence rather than filling it with an estimate.

For the checker's four invariant categories, we identified real, licensed, and -- where reported -- precision/recall-evaluated resources for every language: multilingual named-entity models spanning all six languages with published F1 from 71.19% (Japanese) to 95.30% (Russian) [18-22,27], a rule-based date/number/unit parser covering four of the six languages natively [23], and per-language negation and quantifier cue resources with linguistically grounded starting points for the two languages (Japanese, and the Slavic/Icelandic genitive-of-negation and verb-placement phenomena) whose scope-marking behavior does not reduce to a simple word list [24-26]. None of these resources report precision or recall on WMT25 Task 3's specific error-detection use case, only on their own training corpora; the checker-validation holdout described above exists specifically to close that gap before the checker's verdicts are trusted as scoring ground truth, and doing so is the first step of the next iteration rather than a claim made here.

# Results

This iteration's results are the diagnostic evidence motivating the method and the validation of the infrastructure built to run it (the dataset composition itself, Figure 2, is reported in Section 5 alongside its construction); the five-condition comparison has not yet been executed and no $\Delta$COMET number attributed to conditions B, D, C1, C2, or C in this paper is a new measurement -- every $\Delta$COMET figure reported below is quoted from the shared task's own published results [3,4], reproduced here to make the confound explicit rather than remeasured.

[FIGURE:fig3]

Figure 3 lays out every $\Delta$COMET figure available from primary sources for the three relevant shared-task systems. The masked-fill system that inspired condition B scored -0.0108 on average across all six language pairs, and -0.007 specifically on English-Czech, the one pair where its own paper reports a value directly comparable to the organizer baseline's per-pair figures [4]. Its sibling full-retranslation system scored +0.0201 on average [4]. The organizer's own QE-informed scoped-editing baseline, which pairs fine-grained automatic error detection with a 27-billion-parameter correction model rather than the masked-fill system's 9-billion-parameter model, scored 0.000 on English-Czech, +0.007 on English-Icelandic, and +0.002 on English-Russian -- near break-even on every pair with a directly reported value, in contrast to the masked-fill system's negative range on the same three pairs [3]. Three systems attempting closely related strategies on the same evaluation land in three different places, and the two scoped-editing systems -- differing in repair-model scale and implementation maturity, not in whether they attempt scoped editing at all -- land on opposite sides of break-even. This is the pattern our protocol is built to explain: it is consistent with model capability and hygiene driving most of the observed gap, but it does not by itself establish that a verification loop is what closes it, since the organizer baseline being compared here has no iterative re-verification either. Settling that question is the specific job of conditions C1 and C2, run against a single, fixed repair model, which this iteration's infrastructure is built for but has not yet run.

# Discussion

**What this iteration establishes, and what it does not.** The evidence in Section 1 and Figure 3 is real and task-internal: it is not a claim we are making about scoped editing in general, but a direct reading of two systems that attempted a similar strategy on the same shared task and landed in opposite places. That is enough to say the field's single worst-ranked result on scoped editing is confounded with model capability and cannot, by itself, be read as evidence against scoped editing with verification. It is not enough to say verification is what would close the gap for a fixed, weak model -- that is exactly the comparison conditions C2 and C1 exist to run, and it has not been run in this iteration. We are stating this directly rather than letting a well-supported diagnostic finding read as a completed mechanism result.

**Why the protocol is built the way it is.** Fixing the repair model across every repair-performing condition is the single design choice that makes the eventual comparison interpretable. Without it, a measured gain for condition C over condition B could always be attributed to using a better model rather than to broadened localization or iteration, exactly the ambiguity the shared task's own two scoped-editing systems already illustrate. Similarly, condition D exists to prevent a cheap explanation -- basic output hygiene -- from being mistaken for evidence of a more interesting mechanism; a result where D alone closes most of B's gap would be a legitimate, if less exciting, finding, and the protocol is built to detect that outcome rather than to assume it away.

**Limitations.** The most consequential limitation of this iteration is that it reports infrastructure and a reread of prior evidence, not new experimental outcomes on the central hypothesis. A second is the forced substitution of the original system's repair model: the substitute keeps the same base-model lineage but lacks machine-translation-specific fine-tuning, which is a real difference between what this protocol will measure and what the original system used, and must be reported alongside any future comparative result rather than treated as equivalent. A third is that the deterministic checker's precision and recall against WMT25 Task 3's specific error types is not yet validated; every resource behind it is real and licensed, but validated only against its own training corpus, not this task, and the checker-validation holdout exists to close that gap before its verdicts are used as scoring ground truth. A fourth is coverage asymmetry within the injected-error set: named-entity detection for Chinese and Japanese relies only on embedded Latin-script substrings, a materially lower-recall signal than the capitalization-based heuristic used for the other four languages, so checker performance on entity swaps in those two languages should be expected to look different for tooling reasons distinct from the underlying mechanism question.

**What the next iteration must do.** Three things, in order: validate the checker's precision and recall on the checker-validation holdout before trusting its verdicts anywhere else; confirm the substitute repair model's continued third-party availability immediately before running the comparison, given that the originally planned model and its intended fallback both disappeared from the same hosting catalog within weeks of each other; and run the five-condition comparison itself, reporting fix rate, true regression rate, $\Delta$COMET, edit volume, and inference cost exactly as specified in Section 4.3, separately for the natural and injected subsets and separately per language pair, so that a result favoring verification is not an artifact of injected errors being easier to fix than real ones.

# Conclusion

A shared task's worst-ranked result on scoped machine-translation editing turns out, on a full reading of the primary sources, to sit next to a same-task, same-strategy system that lands near break-even -- evidence that the failure is confounded with model capability and implementation maturity rather than settled proof that scoped editing cannot work. We built a factorial protocol that holds the repair model fixed and separately varies localization breadth and iterative verification specifically to ask, once that confound is controlled, whether verification is the piece that matters. This iteration delivers the diagnostic case, a fully resolved and implementation-ready replication specification including a documented and necessary repair-model substitution, and a validated 8,519-row dataset built to run the comparison without further design decisions. The comparison itself -- and with it, the answer to whether an editing pipeline needs a costlier verify-and-repair loop or can get most of the benefit from a cheaper, broader one-pass scanner -- is the explicit target of the next iteration.

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

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (scope) The paper's own stated core question -- whether localization breadth and/or iterative verification explains scoped editing's failure -- is never tested. Every quantitative number in the paper (the -0.0108, +0.0201, 0.000/+0.007/+0.002 figures) is quoted from two prior publications, not measured by this work. The 'five conditions' that form the paper's headline method are specified but zero of them have been run.
  Action: Either run at least a partial version of the comparison (conditions B, D, C1 minimum, on one or two language pairs) before resubmission, or explicitly re-scope the paper as a resource/infrastructure contribution (dataset + protocol + confound analysis) and target a venue/track that accepts that framing rather than implying a completed comparative study.
- [MAJOR] (evidence) The central 'evidence' motivating the whole paper (Figure 3, Section 1, Section 6) is a comparison of exactly three data points drawn from two papers' self-reported numbers, on overlapping but not identical language-pair subsets (the organizer baseline reports only 3 of 6 pairs directly comparable). Concluding that the field's negative result is 'confounded with model capability and implementation hygiene' from three numbers, two of which come from the same paper describing its own two systems, is a thin evidentiary base for a paper's primary claim, even framed as a diagnosis rather than a proof.
  Action: Explicitly quantify the uncertainty in this three-point comparison (e.g. note the small number of comparable pairs, absence of confidence intervals in the original sources, and that only one language pair, English-Czech, has directly comparable values across all three systems) rather than presenting the pattern as decisively 'locating' the cause. Consider whether additional shared-task entries or related published scoped-editing systems could be added to strengthen this to more than 3 points.
- [MAJOR] (methodology) The forced substitution of the original 9B repair model (TowerPlus-9B, per the artifact) with a same-lineage but non-MT-fine-tuned model (google/gemma-3-12b-it per the artifact) is a serious threat to the eventual comparison's validity, since the entire point of the protocol is to hold model capability fixed and attribute differences to localization/iteration. Using a model with no MT-specific fine-tuning as the shared repair model in all conditions could produce a completely different capability floor than the original system, potentially making even condition B behave very differently from the reproduction target, undermining the 'faithful baseline' condition's fidelity.
  Action: Before running the five-condition comparison, validate that condition B with the substitute model reproduces the original system's failure signature (leftover placeholders, similar direction and rough magnitude of ΔCOMET) as a sanity check; if it does not, report that explicitly as a further limitation on interpretability of the eventual comparison, and consider whether a smaller but MT-fine-tuned model (even if it requires local hosting rather than a third-party API) would better preserve the original conditions.
- [MAJOR] (rigor) The deterministic content-invariant checker -- the instrument the entire protocol depends on for localization, fix-rate, and true-regression-rate measurement -- is explicitly stated to be unvalidated against WMT25 Task 3's actual error types; every underlying resource (NER models, Duckling, negation/quantifier cue lists) is only validated on its own training corpus. Chinese and Japanese entity detection is reduced to embedded Latin-script substrings, a severe recall gap for two of the six target languages that will make 'broad localization' (conditions C1/C/severity-matched variants) systematically under-detect entity errors in exactly those languages.
  Action: Run the checker-validation step (already planned as 'next iteration's first job') and report per-category, per-language precision/recall before or alongside any comparative claim; for Chinese/Japanese entity detection specifically, either integrate a proper CJK NER model (e.g. spaCy's own zh_core_web_lg/ja_core_news_lg already cited for F1 numbers could presumably also do entity extraction, not just report F1) or explicitly exclude entity-swap results for those two languages from headline claims rather than reporting them alongside better-covered languages.
- [MINOR] (novelty) The CEGIS framing (Section 1, Related Work) is evocative but the actual methodological borrowing is thin: the paper imports only the general idea of 'verify, and if it fails, return something that scopes the next repair' -- which is also just standard iterative refinement with a checker rather than a synthesis loop with candidate generalization, unrealizability proofs, or counterexample generalization, the properties that distinguish CEGIS from generic iterative repair. The paper appropriately hedges this ('we do not import CEGIS as a synthesis algorithm') but the framing in the abstract/intro risks overstating the connection.
  Action: Either substantiate a deeper structural parallel to CEGIS (e.g. does the checker's counterexample genuinely scope/localize the next repair attempt the way a CEGIS counterexample restricts the search space, or is it simply 're-check the same span')? or tone down the CEGIS framing in the introduction to 'a verify-and-retry loop analogous in spirit to CEGIS' and rely on the more directly relevant iterative-refinement literature (Self-Refine, and the locate-and-edit / energy-guided editing work already cited) as the primary framing.
- [MINOR] (clarity) The paper cites reference [4] (Padmanabhan, WMT 2025) as reporting -0.0108 average ΔCOMET and -0.007/-0.014 per-pair figures, but never states how many of the six language pairs this per-pair range spans, nor gives the full per-pair breakdown for the losing system the way it does (implicitly) for the organizer baseline's three pairs. This makes the 'opposite territory' claim in the conclusion harder for a reader to verify directly from the numbers given.
  Action: Report the full six-pair ΔCOMET breakdown for both the masked-fill system and its full-retranslation sibling in Figure 3 (or an accompanying table), not just the -0.007/-0.014 range and the three overlapping pairs from the organizer baseline, so the reader can see the complete picture the paper's argument rests on.
- [MINOR] (evidence) The paper states the release's post-edit/human-annotation field is 'empty across all 6,000 rows' and treats this as confirmed via the dataset artifact, but does not report whether other WMT MQM-annotated resources for the same six language pairs (e.g. from prior WMT General MT shared tasks, which often carry MQM annotations for overlapping language pairs and domains) were checked as an alternative ground-truth source before concluding no human-annotated layer exists.
  Action: Briefly note in Section 5 whether MQM annotations from adjacent/prior WMT General shared tasks (not Task 3 itself) were considered and ruled out as a ground-truth substitute, to preempt a reviewer wondering why an external MQM corpus wasn't used instead of accepting the gap.
- [MINOR] (methodology) Condition B's severity-skip rule (skip minor spans when a more-severe span co-occurs) is inherited from the original system for faithful reproduction, but the paper does not explain why the severity-matched C1/C2/C variants are the right way to test whether this specific heuristic (rather than, say, the placeholder-fill mechanism itself) is what drives the original system's failure -- i.e. whether the severity-matched conditions isolate the skip-rule's effect cleanly from other differences between B and the broad-localization conditions.
  Action: Add one sentence in Section 4.2 clarifying exactly what the severity-matched vs. non-severity-matched comparison is designed to isolate (presumably: whether broadened localization's gain is attributable to 'covering minor spans B skips' vs. 'genuinely different invariant coverage'), since as written the reader must infer this from the metrics section rather than the method section.
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

### [2] HUMAN-USER prompt · 2026-09-01 05:39:32 UTC

```
AI in translation emwrging opportunities
```

### [3] SYSTEM-USER prompt · 2026-09-01 05:40:36 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'evaluation_iter2_dir4' (evaluation): dependency 'art_5ySTX4YfxqG_' has type 'research' which is not allowed (allowed: {'experiment', 'dataset'})

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
