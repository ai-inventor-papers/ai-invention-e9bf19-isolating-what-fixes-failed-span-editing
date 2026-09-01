# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_strat`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 09:18:40 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 09:18:46 UTC

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
  for the same team's primary retranslation-selection system. Across three iterations of controlled testing (fixed repair
  model google/gemma-3-12b-it throughout, since TowerPlus-9B and its assumed fallbacks are confirmed delisted; real wmt22-cometkiwi-da
  checkpoint; en-ru_RU and en-uk_UA), five conditions decompose the field's documented failure: B (faithful masked-fill baseline),
  D (B plus trivial output-hygiene retry), C1 (checker-broadened localization to every content-invariant violation in the
  sentence, single uncorrected pass), C2 (narrow QE-span-only localization, but iteratively re-checked and re-repaired against
  the checker up to a 3-pass budget), and C (broad localization plus iteration, combined). What is now MEASURED, not merely
  hypothesized: (1) D does not close B's gap (pooled ΔCOMET -0.0157 vs -0.0164, fix/regression rates identical to B) -- ruling
  out output hygiene as the explanation. (2) C1 cuts ΔCOMET degradation roughly fivefold relative to B/D (pooled -0.0035,
  95% CI [-0.0071,-0.0008]) at a real correctness cost: fix rate falls from 0.9833 to 0.6056 and true regression rate rises
  from 0.0667 to 0.1389 (both pooled excluding the negation-deletion rows that narrow-localization conditions structurally
  cannot attempt). (3) C2, this iteration's newly-executed condition, resolves the mechanism question the protocol was built
  to ask -- and resolves it in BOTH directions on different metrics, not the single clean direction the hypothesis anticipated:
  on the 240 matched injected-pool rows, C2 recovers fix rate and true regression rate to near-parity with B/D (0.9889 fix
  rate, 0.0722 regression, excluding negation) and is materially better than C1 on both (paired-bootstrap fix-rate advantage
  over C1 measured two ways -- +0.2875 [95% CI 0.2292,0.3458] on the 240-row population INCLUDING negation-deletion rows,
  where C2's structural non-attempt on those rows counts against it and narrows the gap, versus +0.3833 on Table 2's 180-row
  population EXCLUDING them, a real, disclosed, population-dependent difference in the same underlying comparison, not two
  competing numbers), but C2's pooled ΔCOMET (-0.0166) is statistically indistinguishable from B/D and, via a paired comparison
  against C1 that uses a documented normal-approximation substitute for C1's per-row variance (since only pooled ΔCOMET exists
  upstream for C1), is measurably WORSE than C1 (-0.0131, CI [-0.0214,-0.0047]). Iteration recovers targeted correctness;
  broadened localization, not iteration, is what has so far been shown to move whole-sentence quality -- these are demonstrably
  different levers, and crediting iteration for both would misdescribe the result. (4) This C2-vs-C1 mechanism finding rests
  on evidence from two structurally disjoint row populations -- ΔCOMET is scored only on the 320 natural rows (no ground-truth
  'correct fix' exists there), fix rate/regression only on the 240 injected-pool rows (no natural QE-severity distribution
  exists there) -- so no single row is ever scored on both axes, and the 'checker-invisible collateral drift' explanation
  for why iteration helps correctness without helping quality is inferred from this cross-population pattern, not directly
  observed on shared rows; this is now stated as an explicit property of the evidence, not an implicit one. (5) Condition
  C -- the combined broad-localization-plus-iteration run that would show whether C1's quality gain and C2's correctness gain
  can be captured together, the single most decision-relevant remaining experiment -- was launched this iteration on identical
  data/checker/repair-model to C2, completed checker validation, began en-ru_RU, then stalled with zero filesystem activity
  for over an hour and produced no output; this is reported as an infrastructure failure, not a result, and no estimate or
  partial-row substitute was fabricated in its place -- it is now the second execution stall/substitution across this project
  (the first being the prior iteration's HuggingFace Hub 429 forcing a temporary LLM-judge proxy for Condition B before real
  COMET was obtained), suggesting a general run-robustness gap (checkpointing, timeout, retry-with-backoff) rather than two
  unrelated incidents. (6) The four reviewer-identified prerequisites from the prior iteration are now addressed rather than
  open: the negation-deletion structural asymmetry is disclosed and quantified (every fix-rate/regression figure reported
  both pooled-including and pooled-excluding negation); the two checker-validation procedures (24-cell global vs 8-cell within-experiment)
  are named and reconciled, with the within-experiment table confirmed as the one that actually gates C1 and C2's repair scope;
  Condition B's fidelity gate now uses a pre-registered [0.5x,2.0x]-magnitude-ratio tolerance rather than an unquantified
  'same order of magnitude' criterion, and the measured 1.52x ratio is reported as a borderline, not unqualified, pass; and
  the executed comparison's scope (two Slavic pairs with the checker's strongest measured coverage, named-entity detection
  excluded outright for both) is now stated at first mention in practitioner-facing guidance, not only in Limitations. We
  hypothesize, narrowed once more by what C2 actually showed, that the genuine, separable residual gap this protocol set out
  to find is real but asymmetric: broadened one-pass localization (C1, confirmed this iteration to trade quality gain for
  correctness cost) and narrow-but-iterated repair (C2, confirmed this iteration to trade correctness gain for no quality
  improvement, at 2.3x the inference cost) are two DIFFERENT, non-dominating mechanisms rather than one mechanism (verification)
  subsuming the other -- and that Condition C, still unrun, is the only experiment that can determine whether combining them
  is additive (both gains), whether one gain crowds out the other, or whether some third interaction emerges. The mechanism-attributing
  part of the original hypothesis (iteration as THE differentiator) is now PARTIALLY DISCONFIRMED: iteration is load-bearing
  for correctness but not for quality, contrary to a single-direction prediction. What remains genuinely untested is the combined
  condition C itself.
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
  Same B/D/C1/C2/C frame; C2 executed and resolved mechanism question as MIXED not one-directional; C still outstanding
_confidence_delta: increased
_key_changes:
- >-
  Replaced 'C2 not yet run' with C2's actual, executed, mixed result: iteration recovers fix-rate/regression-rate near-parity
  with B/D and beats C1 on both, but does not improve ΔCOMET and is measurably worse than C1 on ΔCOMET -- disconfirming the
  single-direction mechanism prediction the prior hypothesis made.
- >-
  Reconciled the reviewer-flagged fix-rate discrepancy (+0.2875 paired-bootstrap vs +0.3833 in Table 2) by naming both figures
  explicitly and explaining the population difference (240 rows including negation-deletion rows, where C2 structurally cannot
  attempt a fix, vs 180 rows excluding them) rather than presenting one number as authoritative.
- >-
  Added the disjoint-population caveat as a first-class, quantified property of the evidence: ΔCOMET (320 natural rows) and
  fix-rate/regression (240 injected-pool rows) never share a scored row, so the 'checker-invisible collateral drift' explanation
  for the quality result is inferred, not directly observed.
- >-
  Noted the normal-approximation substitute used for the C2-vs-C1 ΔCOMET paired comparison is a documented, not silent, methodological
  choice, flagged as needing a formula/justification note in the next artifact round.
- >-
  Reported Condition C's stall as the second infrastructure failure this project has hit (after the prior iteration's HF Hub
  429), reframing it as a general run-robustness gap rather than an isolated incident.
- >-
  Softened the implicit novelty framing: the hypothesis no longer treats 'first to separate localization breadth from iteration'
  as an unqualified priority claim, per reviewer novelty critique -- next iteration's paper text should hedge this appropriately.
- >-
  Kept the core B/D/C1/C2/C factorial frame and the open combined-condition question (C) as the load-bearing next step, since
  nothing this iteration found contradicts the design -- only its resolution direction, which is now mixed rather than singular.
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
Current iteration: 4 of 5
Remaining (including this one): 2
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Run the iteration conditions, then reconcile the numbers
objective: >-
  Execute Conditions C2 (narrow localization, iterative verification) and C (broad localization, iterative verification) --
  the two conditions this project's entire five-condition design was originally built to compare, and the only ones that can
  test whether iteration, as opposed to broadened one-pass checking, is the load-bearing mechanism -- on the same rows, repair
  model, and checker as the already-executed B/D/C1 comparison, and pair that with a single reconciliation evaluation that
  fixes every MAJOR/MINOR methodology gap the reviewer named in the existing B/D/C1 results before any C2/C number is trusted
  alongside them.
rationale: >-
  The paper's own Discussion and Conclusion already state the next iteration's job in specific, falsifiable terms: does re-checking
  a repair against the deterministic checker recover C1's fix-rate and true-regression-rate cost while preserving its ΔCOMET
  gain. That question is the paper's central untested claim and has now been deferred twice (iteration 1 specified it, iteration
  2 executed everything except it) -- a third iteration spent only on re-analyzing B/D/C1 without ever running C2/C would
  leave the mechanism claim permanently unresolved with two iterations left after this one. At the same time, the reviewer's
  two MAJOR critiques are not resolved by running more conditions -- they are resolved by re-reading data that already exists:
  the negation-deletion asymmetry in B/D's fix-rate comparison and the unreconciled global-vs-within-experiment checker validation
  are both artifacts of how existing results were reported, not gaps that need new rows. Running C2/C without also fixing
  these would compound the problem, since C2/C reuse the exact same oracle-span-vs-checker-localization design that created
  the B/D-vs-C1 asymmetry in the first place -- so the reconciliation evaluation must run on all five conditions together,
  with category-level breakouts and an explicit negation-deletion flag baked in from the start rather than retrofitted later.
  Concretely: C2 keeps localization narrow (the QE-flagged span only, exactly as B/D use it, so it inherits the same negation-deletion
  asymmetry and must report around it identically) but adds a checker-gated repair-then-reverify loop up to a fixed pass budget,
  stopping on a certificate; C is the full combination, checker-broadened localization plus iteration. Both reuse the validated
  checker module and gemma-3-12b-it repair model from the existing C1 artifact so no new fidelity check is needed -- Condition
  B's fidelity gate already covers every condition that shares its repair model. Running both C2 and C (not just C2) matters
  because the paper's stated success criterion is a three-way comparison (C1 vs C2 vs C, not just C1 vs C2): if C1 and C2
  improve on D by statistically indistinguishable amounts, the mechanism-attributing claim is disconfirmed regardless of what
  C achieves, and only having C lets that disconfirmation (or confirmation) actually be checked rather than inferred. Both
  conditions are cheap enough to fit comfortably inside the $10 budget: the prior B/D/C1 run on the same 560 rows cost $0.066
  for roughly 1,447 calls at a single-pass budget; a bounded iteration budget of up to 3 passes multiplies call volume by
  at most 3x per condition, putting two new conditions at an estimated $0.30-0.50 total, leaving ample room to also log the
  CEGIS-relevant instrumentation (whether repeated counterexamples localize to narrower spans across iterations) the reviewer's
  optional novelty suggestion asked for at effectively zero marginal cost.
artifact_directions:
- id: experiment_iter3_dir1
  type: experiment
  objective: >-
    Run Condition C2 (narrow localization restricted to the original QE-flagged span, but iteratively repaired and re-verified
    by the deterministic content-invariant checker up to a fixed pass budget, stopping on a certificate or budget exhaustion)
    on the identical en-ru_RU/en-uk_UA rows, repair model (google/gemma-3-12b-it), and checker used for the existing B/D/C1
    comparison, isolating the effect of iteration while holding localization fixed at narrow.
  approach: >-
    Re-implement the B/D/C1 pipeline's checker module and OpenRouter client (the executor should read the prior experiment's
    method.py/checker.py directly from the run tree at the workspace_path recorded for that artifact, since no formal dependency
    edge is possible between two experiment artifacts, and reproduce the identical row selection by regenerating the same
    stratified 320-natural/240-injected-pool sample from the dataset using the same seed/stratification rule documented there)
    so C2 runs on effectively identical inputs. For each row, mask the original QE-flagged span (or, for injected rows, the
    oracle span exactly as B/D define it -- inheriting and explicitly flagging the same negation-deletion structural limit:
    negation rows have a zero-width oracle span and C2 therefore cannot attempt them either, which must be logged per-row,
    not silently pooled away), repair with one gemma-3-12b-it call, then run the checker against the repaired span; if it
    still fails and the category is checker-covered, issue one more targeted repair call scoped to exactly what the checker
    flagged, up to a hard cap of 3 total repair passes per span, and stop early with an explicit 'certificate' flag the moment
    a pass verifies clean. Log, per row and per pass: whether the span passed the checker before/after each pass, edit volume
    per pass, and whether repeated failures on the same span narrow in character length across iterations (the concrete CEGIS-narrowing
    signal). Score with the real wmt22-cometkiwi-da checkpoint (already confirmed working in the prior run) for ΔCOMET, plus
    fix rate and true regression rate on the injected-pool subset using the same ground-truth definitions as B/D/C1, broken
    out by invariant category (not pooled) so the negation asymmetry is visible from first report rather than needing later
    reconstruction. Track and cap OpenRouter spend explicitly against a pre-declared $2 sub-budget for this artifact before
    running the full sweep, estimating cost from the pass-1 subset first.
  depends_on:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_5ySTX4YfxqG_
    label: resource dossier
    relation_type:
    relation_rationale:
- id: experiment_iter3_dir2
  type: experiment
  objective: >-
    Run Condition C (broad checker-based localization combined with iterative repair-and-reverify to a certificate or budget
    exhaustion) on the same rows, repair model, and checker as C2, completing the five-condition design and giving the paper
    its first genuine three-way comparison among C1 (broad, single-pass), C2 (narrow, iterative), and C (broad, iterative).
  approach: >-
    Re-implement the same checker module, OpenRouter client, and row selection as the C2 artifact (again reading the prior
    B/D/C1 experiment's method.py/checker.py from its workspace_path in the run tree as a reference implementation, since
    experiment artifacts cannot formally depend on each other) and reuse C1's checker-broadened localization logic (flag every
    invariant violation in the sentence the checker's within-experiment validation deems usable for that language, same 5/8-cell
    repair scope C1 used) but add an iterate-and-reverify loop per flagged span, capped at the same 3-pass budget, with the
    same certificate flag and per-pass narrowing log as C2. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da, fix rate
    and true regression rate on the injected-pool subset broken out by invariant category and by whether the row's negation
    span is a deletion (structurally unattemptable for B/D, attemptable here since this condition uses checker localization,
    not oracle spans -- record this explicitly as a design difference, not a repair-quality difference, exactly per the reviewer's
    action item). Report edit volume and LLM-calls-per-sentence per pass and cumulative, to check directly whether C's iteration
    loop degenerates toward full-sentence regeneration by the final pass (the paper's own stated failure mode to rule out).
    Cap spend at a pre-declared $2 sub-budget, estimated from a small pilot subset before the full run, with both this artifact
    and the C2 artifact's combined spend tracked against the shared $10 ceiling.
  depends_on:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_5ySTX4YfxqG_
    label: resource dossier
    relation_type:
    relation_rationale:
- id: evaluation_iter3_dir3
  type: evaluation
  objective: >-
    Produce the paper's first apples-to-apples five-condition (B/D/C1/C2/C) comparison with the reviewer's exact requested
    fixes applied: fix rate and true regression rate broken out by invariant category (and pooled excluding vs including negation),
    an explicit named-and-reconciled account of the global versus within-experiment checker validation procedures and which
    one governs each reported repair scope, a stated numeric tolerance for the Condition-B fidelity gate's 'same order of
    magnitude' criterion with the measured 1.5x deviation assessed against it, and the mechanism-attributing statistical test
    (does C2 improve on D by materially more than C1 does; does C achieve a non-negative or near-zero ΔCOMET with lower true
    regression rate than B at comparable fix rate) that determines whether the hypothesis's central claim is confirmed, disconfirmed,
    or undetermined.
  approach: >-
    Load B/D/C1 results from the existing experiment artifact (art_7Uc5PlFctjXi) and C2/C results from the two new sibling
    experiment artifacts in this strategy (the executor discovers them from the shared artifact pool at run time, exactly
    as the prior evaluation artifact art_qUG1DIUZKEBQ already does for same-iteration siblings, since a formal dependency
    edge on same-iteration artifacts is not permitted), plus the checker validation artifact's full 24-cell table and the
    within-experiment 8-cell table C1/C2/C actually used for gating. First, name and reconcile the two validation procedures
    explicitly: report both side by side, state the exact methodological differences (holdout size 448+1080 vs 175 rows; natural-QE-proxy
    precision vs single-positive-per-row precision/recall; 0.5 threshold applied to which numerator), and state which one
    governed C1/C2/C's actual repair scope in this run -- resolving the reviewer's MAJOR rigor critique as a stated fact,
    not an implicit tension. Second, recompute every fix-rate and true-regression-rate headline broken out per invariant category
    for all five conditions, and separately report a pooled-excluding-negation number alongside the pooled-including-negation
    number, with the negation asymmetry (B/D/C2 structurally cannot attempt injected negation-deletion rows under oracle-span
    localization; C1/C use checker localization and can) stated as a sentence directly in the results table's note, not only
    in prose. Third, define a pre-registered tolerance for the Condition-B fidelity gate (e.g., substitute-model ΔCOMET within
    2x the original paper's magnitude and same sign) and report whether the measured 1.5x deviation passes it, explicitly
    as a borderline-not-unqualified pass. Fourth, run the mechanism test the hypothesis's success criteria specify: paired
    bootstrap comparison of (C2-D) vs (C1-D) ΔCOMET and true-regression-rate deltas to test whether iteration materially outperforms
    broadened localization alone; and report whether full Condition C clears non-negative or near-zero ΔCOMET with true regression
    rate significantly below B's at a comparable-or-better fix rate, stating the CONFIRMED / DISCONFIRMED / MIXED verdict
    per the hypothesis's own pre-specified success/disconfirmation criteria. Produce a single five-condition summary table
    (B, D, C1, C2, C x ΔCOMET/fix-rate/true-regression-rate/edit-volume/calls-per-sentence, category-broken-out) intended
    to replace the paper's current three-condition Section 6.3 table. If either sibling C2 or C artifact has not yet produced
    output files at evaluation time, degrade that condition's fields to NOT_AVAILABLE with a stated reason, exactly as the
    prior evaluation artifact's graceful-degradation pattern already establishes, rather than fabricating placeholder numbers.
  depends_on:
  - id: art_mhfmDpGp4z1J
    label: dataset
    relation_type:
    relation_rationale:
  - id: art_7Uc5PlFctjXi
    label: B/D/C1 results
    relation_type:
    relation_rationale:
  - id: art_QLpPxaqf1VzK
    label: checker validation
    relation_type:
    relation_rationale:
expected_outcome: >-
  Real, measured ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count results for Conditions C2 and C on the
  same rows/model/checker as the existing B/D/C1 comparison, giving the paper its first genuine test of the mechanism-attributing
  claim (iteration vs. broadened localization) with a CONFIRMED/DISCONFIRMED/MIXED verdict against the hypothesis's own pre-specified
  success criteria; a single reconciled five-condition results table with category-level fix-rate/regression-rate breakouts
  that eliminates the negation-deletion confound the reviewer flagged as a MAJOR issue; an explicit, named reconciliation
  of the two previously-conflicting checker-validation procedures stating which one governs repair scope; and a quantified,
  pre-registered tolerance for the Condition-B fidelity gate that turns the previously unqualified PASS into a stated borderline-pass
  judgment -- collectively resolving both MAJOR and two of three MINOR reviewer critiques while advancing the paper from a
  three-condition partial result to the complete five-condition comparison the protocol was designed around.
summary: >-
  Runs the two conditions (C2, C) this project's entire design was built to compare -- iterative verification versus broadened
  localization -- on the same controlled setup as the existing B/D/C1 result, and pairs them with one evaluation artifact
  that fixes the reviewer's category-breakout, validation-reconciliation, and fidelity-tolerance critiques on all five conditions
  at once, turning the paper's central untested claim into a measured, verdict-bearing result.
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

--- Item 7 ---
id: art_K8koUmGFDlLN
type: experiment
title: Does Iteration Alone Fix Span Edits?
summary: >-
  Implements and executes Condition C2: the same narrow, QE-span-only localization used by conditions B and D in the prior
  B/D/C1 comparison (gen_art_experiment_3, iter_2), but with the repaired span iteratively re-verified by the 4-category content-invariant
  checker (named_entity, number_unit_date, negation_polarity, quantifier_scope) and re-repaired with a targeted, checker-detail-scoped
  prompt, up to MAX_PASSES=3, stopping as soon as a certificate is achieved. checker.py and llm_client.py are copied VERBATIM
  from the prior B/D/C1 run (PRIOR_RUN_PATH = gen_art_experiment_3, iter_2) so the checker, repair model (google/gemma-3-12b-it),
  and OpenRouter client are byte-identical to that run. The exact same seed (42) and stratification code regenerate the 320-natural/240-injected-pool
  row population, and row-ID identity against the prior run's logged selected_rows.json was verified True for all three subsets
  (natural, injected-pool, injected-heldout) -- this is a fully row-matched, controlled comparison, not merely population-matched.
  A pre-declared $2 sub-budget was estimated from a live 20-row pass-1 probe (projected worst-case $0.0956) before the full
  sweep, and the sweep hard-stops on cumulative spend; actual total spend was $0.045 across 930 OpenRouter calls, well under
  both the $2 sub-budget and the $10 artifact-wide cap. Results are reported both pooled and broken out by invariant category
  x language pair (not pooled-only), with negation_polarity_flip rows -- which are DELETIONS carrying no contiguous substring
  to mask (metadata_corrupted_span==''), so they get c2_attempted=False, skip_reason='negation_deletion_zero_width_span' --
  shown as 'N/A (structural non-attempt)' rather than folded into a misleading 0% fix rate; they remain in n_rows denominators
  throughout. Headline pooled comparison against the prior run's B/D/C1 numbers: ΔCOMET (natural subsample, Unbabel/wmt22-cometkiwi-da,
  same checkpoint) B=-0.0164, D=-0.0157, C1=-0.0035, C2=-0.0166; fix_rate (injected-pool, among rows C2 actually attempted)
  B=0.7375, D=0.7375, C1=0.4542, C2=0.9889; true_regression_rate B=0.05, D=0.05, C1=0.125, C2=0.0722. The finding is genuinely
  mixed and reported as such: iteration alone (same narrow oracle-span localization as B/D, no checker-broadened localization
  unlike C1) drives fix_rate far above B/D/C1 and regression well below C1's, but does NOT improve -- in fact slightly worsens
  -- ΔCOMET relative to B/D, contradicting a naive expectation that more verification passes would monotonically improve translation
  quality. Also reports: pooled and per-pair bootstrapped ΔCOMET (95% CI, 1000 iterations, same method as B/D/C1), edit volume
  and gain-to-edit ratio, mean LLM calls/passes per sentence (natural=2.29, injected=1.09), and a descriptive CEGIS-narrowing
  signal (edit-distance trend across passes for multi-pass rows) explicitly caveated as a weak proxy rather than a formal
  convergence claim, since exact span boundaries drift as the whole sentence is rewritten each pass. checker.py's Stanza NER
  resources were not pre-cached in this workspace (unlike the prior run's environment), so they are downloaded once at startup
  via stanza.download() without modifying checker.py itself; checker validation on the injected_heldout fold was re-run and
  produced the same exclusion set (ru_RU/named_entity, uk_UA/named_entity, uk_UA/quantifier_scope) as the prior run. Output
  method_out.json (and its full/mini/preview variants) is schema-validated against exp_gen_sol_out, contains per-row results,
  the per-category/per-language breakdowns, the full B/D/C1-vs-C2 comparison table (loaded live from the prior run's method_out.json),
  the cost ledger, and an explicit metadata block naming every place C2's setup could not be verified byte-identical to B/D/C1
  (found to be none -- row-ID identity was fully verified). pyproject.toml pins every dependency to the exact version installed
  in the .venv this ran in (via uv pip freeze), including torch==2.6.0+cu124 with an install-order note since it is not resolvable
  from plain PyPI.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_art/gen_art_experiment_1
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

--- Item 8 ---
id: art__bfSxpVnFUc8
type: evaluation
title: Reconciled Five-Condition Repair Scorecard
summary: >-
  Reconciled five-condition (B/D/C1/C2/C) translation repair evaluation, built entirely from existing/sibling artifact JSON
  outputs (zero OpenRouter calls, no GPU, no re-execution of any method). Loads art_7Uc5PlFctjXi's full_method_out.json for
  conditions B/D/C1 (per-row fix_success/true_regression on the 240-row injected pool, plus pooled/per-language ΔCOMET on
  the 320-row natural pool), art_QLpPxaqf1VzK's full_method_out.json for the 24-cell global checker validation, and art_7Uc5PlFctjXi's
  checker_validation.json for the 8-cell within-experiment validation. Discovers the two iteration-3 sibling artifacts for
  conditions C2 and C at run time by matching gen_plan titles (no formal dependency edge exists on them), since they were
  built by extending B/D/C1's method.py. Condition C2's sibling artifact (iter_3 gen_art_experiment_1, 'Testing Whether Iteration
  Alone Fixes Span Edits') completed during this run and was successfully loaded, including handling a genuinely different
  output schema (natural_pooled/injected_category_table with per-row metadata_c2_fixed/metadata_c2_true_regression fields,
  rather than B/D/C1's metrics.pooled.<cond> convention) via schema-agnostic accessor functions. Condition C's sibling artifact
  (iter_3 gen_art_experiment_2, 'Condition C: broad checker plus iterative repair') was still running after being polled repeatedly
  for over an hour with zero file-system activity (stalled after checker validation, mid-way through the en-ru_RU pass); per
  the plan's explicit fallback, its metrics were set to the literal string 'NOT_AVAILABLE' with a not_available_reason rather
  than fabricated, and this degradation propagates into every downstream table cell and the final verdict. Produces four metric
  groups: (1) an 8-cell validation-reconciliation table naming the within-experiment (175-row) table, not the global (24-cell)
  table, as the one that actually gated C1's repair scope, with an explicit reconciliation_note on why the two n's and two
  precision definitions differ and confirming directional (not numerical) agreement; (2) category-broken-out (named_entity/number_unit_date/negation_polarity/quantifier_scope)
  fix_rate and true_regression_rate per condition, pooled with and without negation rows, each with a 2000-resample bootstrap
  95% CI stratified by language_pair, reproducing B/D/C1's original headline numbers exactly (B/D 0.7375 fix_rate / 0.050
  true_regression_rate, C1 0.4542/0.125) as a correctness check before extending to C2; (3) a pre-registered numeric tolerance
  test (same-sign AND magnitude ratio in [0.5x, 2.0x]) for Condition B's fidelity replication of Padmanabhan (2025), applied
  to the measured -0.0164 vs -0.0108 (ratio 1.52x, PASS, labeled a borderline pass), plus a secondary CI-containment check;
  (4) a mechanism test comparing C2 against C1 on 240 matched injected-pool rows via paired bootstrap on true_regression_rate
  and fix_rate (C2-C1 true_regression_rate = -0.071, 95% CI [-0.117,-0.025], i.e. C2 has materially LOWER true regression
  than C1) plus a ΔCOMET comparison via a documented normal-approximation substitute (since only pooled ΔCOMET, not per-row,
  exists upstream) that favors C1 (C2-C1 ΔCOMET = -0.013, CI excludes 0 against C2), yielding an explicit MIXED mechanism_verdict
  since the two outcome axes point in different directions; the net_positive_verdict for full condition C could not be computed
  (UNDETERMINED) because condition C's sibling artifact never produced output, so the overall top-level verdict is 'UNDETERMINED
  — condition C2/C data unavailable' rather than a forced CONFIRMED/DISCONFIRMED. Assembles a unified 5-row (B/D/C1/C2/C)
  JSON table with pooled/per-language ΔCOMET, fix/true-regression rates (including/excluding negation), per-category breakdowns,
  edit-volume/LLM-call stats, and an availability_flag per condition, explicitly marked as intended to replace the paper's
  current three-condition Section 6.3 table. Deliverables: eval.py (schema-agnostic across the two upstream output conventions,
  deterministic seed=42), full/mini/preview eval_out.json validated against the exp_eval_sol_out schema, and a pinned pyproject.toml
  (numpy==2.5.2, loguru==0.7.3). Downstream GEN_PAPER_TEXT should report the MIXED mechanism finding (C2 lowers true regression
  but at some COMET cost relative to C1) as the primary result, present the overall verdict as genuinely undetermined pending
  condition C's completion rather than papering over the gap, and reuse the validation-reconciliation table's stated fact
  (within-experiment table gates C1's scope, not the global table) verbatim rather than re-deriving it.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/gen_art/gen_art_evaluation_1
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

The 2025 WMT shared task on automated translation evaluation (Task 3, minimal editing) gave scoped editing its first head-to-head test against full retranslation [3]. A scoped-editing system that masks each QE-flagged span with a placeholder token and fills it with one pass of a small language model finished dead last among eight ranked systems, at $-0.0108$ mean $\Delta$COMET, while a second, independently built scoped-editing system in the same ranking landed near break-even [3,4]. Two prior iterations of this project established that the losing system's own account of itself documents concrete implementation failures -- leaked placeholder text, a single weak repair model versus a six-model sibling pool, a severity heuristic that skips minor-severity spans -- and that a controlled reproduction (Condition B), a hygiene-only control (Condition D), and a broadened-localization single-pass repair (Condition C1), run on real WMT25 translations with one repair model held fixed, showed hygiene explains almost none of the gap while broadened localization cuts it roughly fivefold in $\Delta$COMET terms, at a real cost: C1's fix rate on injected errors it was scored against fell from 0.74 to 0.45 and its true regression rate rose from 0.05 to 0.13 relative to B and D. That left the protocol's original, still-unanswered question open: does iterating a repair against a deterministic check recover the fix-rate and regression cost broadened localization pays, while keeping its quality gain?

This iteration answers that question directly, and the answer is genuinely mixed rather than a clean win. We executed Condition C2 -- localization held narrow, exactly as in B and D, but each repair iteratively re-checked and re-repaired against the same content-invariant checker up to a fixed pass budget -- on the identical rows, repair model, and checker as the B/D/C1 comparison, with row-level identity to the prior run verified rather than assumed. Iteration recovers correctness almost completely: C2's fix rate on non-negation categories reaches 0.9889, matching B/D's 0.9833 and far exceeding C1's 0.6056, and its true regression rate (0.0722) sits far below C1's 0.1389, close to B/D's 0.0667. But iteration does not recover $\Delta$COMET. C2's pooled $\Delta$COMET is $-0.0166$, statistically indistinguishable from B's $-0.0164$ and D's $-0.0157$, and a paired bootstrap against C1 on the same 240 matched rows shows C2 is measurably *worse* than C1 in $\Delta$COMET terms (difference $-0.0131$, 95% CI $[-0.0214,-0.0047]$) while being measurably *better* on true regression rate (difference $-0.0708$, CI $[-0.1167,-0.025]$). The two axes of the mechanism test this protocol was built to run point in opposite directions.

We could not close the remaining question -- whether combining broadened localization with iteration (Condition C) captures both C1's quality gain and C2's correctness gain -- because that condition's run stalled during execution and never produced output, an infrastructure failure disclosed here rather than papered over with an estimate. The paper's overall verdict on whether iterative verification makes scoped editing net-positive is therefore explicitly undetermined, not negative: what is now measured is that iteration, holding localization narrow, buys correctness parity with the simplest baseline at more than double its inference cost, and that broadened localization, not iteration, is what has so far been shown to move $\Delta$COMET.

**Summary of contributions.**

- The first executed run of Condition C2 -- narrow, QE-span-only localization with iterative checker-gated repair, up to a three-pass budget -- on 320 natural and 240 injected-error WMT25 rows across two language pairs, row-matched to the prior B/D/C1 comparison with row-ID identity verified rather than assumed (Section 6.4).
- Direct evidence that iteration recovers fix rate and true regression rate to near-parity with the simplest narrow-localization baselines (B, D), but does not reduce $\Delta$COMET relative to those same baselines, and is measurably worse in $\Delta$COMET than broadened one-pass localization (C1) despite being measurably better in true regression rate -- a mechanism-level result the protocol's original hypothesis predicted would resolve in one direction and instead resolves in both, on different metrics (Section 6.4).
- An honest report of Condition C's non-completion: the combined broad-localization-plus-iteration run stalled after checker validation with no filesystem activity for over an hour and produced no output, so the question of whether broadened localization's quality gain and iteration's correctness gain can be obtained together remains open, not resolved either way (Section 6.5).
- A reconciliation of this project's two checker-validation procedures -- a 24-cell global validation and an 8-cell within-experiment validation with different sample pools and different precision definitions -- confirming they agree in direction (negation-polarity strongest, named-entity weakest) despite disagreeing numerically, and establishing which one actually gated C1 and C2's repair scope (Section 6.1).
- An explicit, quantified accounting of the negation-deletion structural asymmetry the prior iteration's reviewer flagged: narrow-localization conditions (B, D, C2) structurally cannot attempt any negation repair because negation corruptions are deletions with no contiguous span to mask, and every fix-rate and regression-rate figure in this paper is now reported both pooled-with-negation and pooled-excluding-negation so the two are not conflated (Section 6.3).

# Related Work

**Quality-estimation-informed post-editing.** Automatic post-editing systems that use word-level QE as a training signal jointly train an encoder-decoder that regenerates the full target sentence in every variant; adding the QE signal reduces over-correction (18.30 vs. 19.39 TER) but never freezes a QE-clean span, so the model can still rewrite text no error was ever flagged in [5]. A later system replaces the auxiliary-signal approach with Grid Beam Search, forcing QE-tagged "OK" spans as lexical constraints while the decoder keeps freedom to reorder and rephrase around them; this is closer to scoped editing in spirit but is a soft constraint on regeneration rather than a frozen, iteratively verified span, and the paper's own oracle-versus-predicted-tag gap of 0.3-1.3 TER shows the method's ceiling is set by QE tag accuracy without isolating that dependency as a separate factor [6]. Prompting large language models directly with structured error annotations improves post-editing outcomes over unstructured feedback, but every condition in that study still regenerates the sentence and none tests a repair-then-verify loop against a single-pass repair with the same signal [7]. A related line automatically predicts MQM-style error spans and post-edits with them inside an LLM-as-judge evaluation pipeline, again as a one-shot correction step [10]. A third WMT25 Task 3 submission generates a natural-language explanation of each QE-flagged error with the xTower explanation model and hands that explanation to a large language model as the correction prompt [28]; like every system reviewed here, it regenerates the flagged segment in a single pass with no re-verification step. Our Condition C2 result is, to our knowledge, the first controlled evidence in this literature that separates "check more of the sentence once" (C1) from "iterate on the same narrow check" (C2) as distinct levers, and finds they move different metrics: broadened one-pass checking is what has been shown to move whole-sentence quality, while iteration is what closes the correctness gap broadened checking opens.

**Localized and energy-guided editing.** Locate-and-edit approaches to controlled text generation obtain a full generation from a base model, then use an energy function to find and replace only the spans that violate a stated constraint, explicitly to avoid the semantic drift full regeneration under a constraint tends to introduce [11]. This is the closest existing mechanism to the localization half of our design, but it has not been applied to machine translation and has not been evaluated with localization breadth and iteration held apart as separately controlled factors.

**Iterative self-refinement.** Self-Refine shows that a single language model can generate an output, critique its own output, and revise it over several rounds without external supervision, improving results on tasks from code optimization to dialogue response generation [8]. Condition C2 iterates against a deterministic, non-learned checker rather than the repair model's own judgment, precisely to avoid the known unreliability of a model critiquing its own errors. Our result complicates the general expectation that more refinement rounds monotonically help: C2 shows iteration against an external, deterministic verifier reliably fixes the specific things the verifier checks, but does not by itself improve a downstream metric (whole-sentence $\Delta$COMET) the verifier was never checking -- a distinction the self-refinement literature's usual single-metric evaluations do not surface.

**Counterexample-guided synthesis.** Counterexample-Guided Inductive Synthesis (CEGIS) is a synthesis loop in which a candidate is checked against a specification by a verifier that either certifies it or returns a concrete counterexample scoping the next candidate, terminating on an explicit certificate rather than a fixed budget [9]. We do not claim to import CEGIS as a synthesis algorithm; our checker's "counterexample" is a flagged span, not a candidate-generalizing constraint, and nothing in our design performs unrealizability reasoning or generalizes across counterexamples. What we borrow is narrower -- the separation of concerns between what a verifier is allowed to see (localization breadth) and whether the loop runs more than once (iteration) -- and Condition C2 is the first executed test of the iteration half of that separation; the closer methodological kin for the mechanism this paper tests are the iterative-refinement and locate-and-edit lines above.

**Evaluation infrastructure.** All $\Delta$COMET figures in this paper are computed with the same reference-free quality-estimation checkpoint the shared task uses, `wmt22-cometkiwi-da` [2]. Our natural-error data is WMT25 Task 3's released test set [3]; our injected-error data is built from WMT24++, a disjoint, human-post-edited multilingual corpus spanning 55 languages and dialects [14].

# Preliminaries

We define four terms used throughout the protocol.

A **content invariant** is a piece of source-sentence meaning -- a named entity, a number, unit, or date, a negation polarity marker, or a quantifier -- that must survive translation, and that can be checked deterministically (via named-entity recognition, regular expressions, cue-word lists, or alignment) rather than judged by a learned model. We check four invariant categories: entity identity, number/unit/date value, negation polarity, and quantifier scope.

A translation's **certificate** is the state in which every content invariant extracted from its source sentence has been checked and passes. This iteration is the first to produce certificates: Condition C2 stops iterating as soon as a repair passes the checker (certificate reached) or a fixed pass budget is exhausted, whichever comes first.

**Localization breadth** is how much of the sentence a system is allowed to flag as needing repair. *Narrow* localization repairs only the span the original quality-estimation model flagged (Conditions B, D, and C2); *broad* localization repairs every invariant our checker finds violated, whether or not quality estimation flagged it (Conditions C1 and C).

**Iteration** is whether a flagged span, once repaired, is re-checked and re-repaired if it still fails, up to a fixed pass budget, or whether the system accepts a single repair pass unconditionally. Conditions B, D, and C1 use a single, uncorrected pass; C2 and C iterate.

# Method

## Design Rationale

Our method isolates localization from verification by construction: it fixes the repair model identically across every condition that performs a repair, and it varies localization breadth and iteration as two independently switchable factors rather than one bundled toggle. Prior iterations established that broadening localization alone (C1), with no iteration, moves $\Delta$COMET substantially but costs fix rate and true regression rate relative to narrow-localization baselines. This iteration asks the complementary question the design was built to answer: holding localization narrow, does adding iteration alone recover what C1 lost, and does it do so without giving back C1's quality gain?

## Five Conditions, Three Now Executed With Two More Attempted

All five conditions share one deterministic content-invariant checker (Section 6.1) and, in every condition that performs a repair, one fixed repair model, `google/gemma-3-12b-it`. Conditions B, D, and C1 were executed and reported in the prior iteration and are reproduced here as the comparison baseline; this iteration executes Condition C2 to completion and attempts Condition C, which stalls before producing output (Section 6.5).

**Condition B (faithful baseline).** A reproduction of the original masked-fill system: the QE model's flagged span is masked with a placeholder token according to the original system's severity-conditioned masking rule, filled with one repair-model pass, and accepted without any check [4].

**Condition D (hygiene filter, no checker).** Condition B, plus a trivial post-hoc filter that detects and retries any output containing a leftover mask token, garbled placeholder text, or leaked instruction-format text. No content-invariant checker is involved.

**Condition C1 (broad localization, single pass).** The checker flags every invariant violation in the sentence, not only the original QE span; each flagged violation is repaired in one uncorrected pass, with no re-verification. Per-category repair scope is gated by the checker's own validated precision and recall (Section 6.1): a (language, category) cell falling below 0.5 on either metric in the within-experiment validation is excluded from C1's repair scope.

**Condition C2 (narrow localization, iterative verification, newly executed).** Localization stays restricted to the original QE-flagged span, but that span is repaired, re-checked by the checker against the specific invariant categories it flags, and re-repaired with a targeted, checker-detail-scoped prompt if it still fails, up to a fixed three-pass budget, stopping as soon as the checker certifies the repair. This isolates the effect of iteration while holding localization fixed at narrow -- the comparison this paper's original design most wanted to run.

**Condition C (broad localization, iterative verification, attempted, not completed).** Both changes combined: every checker-flagged invariant is repaired and re-verified to a certificate or budget exhaustion. This condition is designed to test whether broadened localization's quality gain and iteration's correctness gain can be obtained together; it is reported in Section 6.5 as not completed.

C2 and C were built by extending the checker module and OpenRouter client from the B/D/C1 artifact verbatim, so both share an identical checker, repair model, and API client with the conditions they are compared against. C2 regenerated the same stratified 320-natural/240-injected-pool row population using the same seed and stratification rule as B/D/C1, and row-ID identity against the prior run's logged row selection was verified true for all three subsets (natural, injected-pool, injected-heldout) before any C2 number was trusted alongside B/D/C1's.

## Metrics

Matching the shared task's own reporting where possible, the protocol measures: (i) fix rate on the four checkable categories, scored against the human-confirmed injected-error subset, reported both pooled-with-negation and pooled-excluding-negation (Section 6.3); (ii) true regression rate, the fraction of invariants correct before repair that a repair step breaks, scored only against ground-truth-confirmed cases; (iii) mean $\Delta$COMET using the shared task's own checkpoint [2]; (iv) edit volume, the mean fraction of the sentence's characters touched by a repair; and (v) language-model calls per sentence, which C2 and C multiply relative to B, D, and C1 by design.

# Data

We reuse, without modification, the complete data construction validated in the prior iteration: 6,000 natural WMT25 Task 3 rows across six English-source language pairs and five domains, carrying the QE model's released flagged spans and severity labels [3]; and 2,519 injected-error rows built by programmatically corrupting clean WMT24++ target text into one of four invariant categories (named-entity swap, number/unit/date alteration, negation polarity flip, quantifier substitution), each carrying the pre-corruption text, the corrupted text, and the exact character span of the change so a checker's precision and recall against a known answer is computable directly [14]. Both groups are split by language pair (and, for the injected set, by category) into an experimental pool and a checker-validation holdout kept strictly disjoint from it.

Condition C2 runs on the same 320 natural and 240 injected-pool rows, from the same two language pairs (en-ru\_RU, en-uk\_UA), as Conditions B, D, and C1. This iteration's contribution to the data pipeline is not new construction but verified reuse: because C2 was implemented independently of the artifact that produced B/D/C1, we regenerated the row selection from the same seed and stratification code and confirmed row-ID identity against the prior run's logged selection for all three subsets before trusting any cross-condition comparison, rather than assuming the same seed produces the same rows.

$\Delta$COMET throughout this protocol is computed with `wmt22-cometkiwi-da`, the same checkpoint the shared task's organizers use as the exact scorer behind every entry in its results table [2,3].

# Results

This iteration executes Condition C2 to completion (320 natural rows, 240 injected-pool rows, two language pairs) and attempts Condition C, which does not complete. We report C2 alongside the prior iteration's B, D, and C1 results, reconciled into a single five-condition scorecard, and report Condition C's non-completion directly rather than omitting it.

## Reconciling Two Checker-Validation Tables

The checker's validity was measured twice in this project, at different scopes, and the two measurements were never reconciled by name in the prior draft -- a gap the prior review flagged. The *global* table scores the checker against all 448 injected and 1,080 natural rows in the checker-validation holdout, across all six languages and four categories, using a natural-row precision proxy (any checker flag on a natural row that does not overlap a sparse QE-flagged span counts as a false positive, a noisy and conservative signal). The *within-experiment* table scores the checker against only the 175-row subset of that holdout actually available for the two language pairs this experiment runs on, using an exact single-positive-per-row precision against known ground-truth corruption spans on injected rows only -- a stricter, directly interpretable metric.

| Language | Category | Global $P$ / $R$ | Within-exp $P$ / $R$ | Usable (within-exp) |
|---|---|---|---|---|
| ru\_RU | named\_entity | 0.039 / 1.000 | 0.324 / 1.000 | No |
| ru\_RU | number\_unit\_date | 0.184 / 1.000 | 0.575 / 1.000 | Yes |
| ru\_RU | negation\_polarity | 0.867 / 0.565 | 0.857 / 0.522 | Yes |
| ru\_RU | quantifier\_scope | 0.152 / 1.000 | 0.591 / 0.565 | Yes |
| uk\_UA | named\_entity | 0.029 / 0.696 | 0.370 / 0.696 | No |
| uk\_UA | number\_unit\_date | 0.132 / 1.000 | 0.575 / 1.000 | Yes |
| uk\_UA | negation\_polarity | 0.824 / 0.609 | 0.778 / 0.609 | Yes |
| uk\_UA | quantifier\_scope | 0.197 / 1.000 | 0.500 / 0.429 | No |

*Table 1: The two checker-validation procedures, restricted to the eight (language, category) cells this experiment actually runs on. $P$ is precision, $R$ is recall; usability requires both $\geq 0.5$.*

The two tables disagree numerically -- the global table's noisier natural-row proxy clears the 0.5 threshold for only 2 of these 8 cells, the within-experiment table for 5 of 8 -- but agree in direction: negation-polarity detection is the strongest-clearing category and named-entity detection the weakest in both. It is the within-experiment table, not the global one, that actually gated C1 and C2's repair scope in this run, because it matches the exact languages and categories these conditions run on and uses the stricter, exact-match metric; the global table's natural-row proxy was never used as a gating criterion anywhere in this pipeline. Three cells fail the within-experiment threshold and are excluded from both C1's and C2's repair scope: ru\_RU and uk\_UA named-entity, and uk\_UA quantifier-scope.

## Condition-B Fidelity: A Pre-Registered Tolerance, Not an Assumed Pass

Before trusting any comparison built on the substitute repair model, we pre-registered a quantitative tolerance for Condition B's reproduction of Padmanabhan (2025)'s $-0.0108$ mean $\Delta$COMET, rather than relying on the prior iteration's unquantified "same order of magnitude" language: the measured value must share Padmanabhan's sign, and its magnitude ratio to the original must fall in $[0.5\times, 2.0\times]$. Condition B's pooled $\Delta$COMET is $-0.0164$ (95% CI $[-0.0237,-0.0101]$), matching Padmanabhan's sign with a magnitude ratio of $1.52\times$ -- inside the tolerance band, but close enough to its edge that we report this a borderline pass rather than an unqualified one. A secondary check confirms Padmanabhan's point value falls inside our measured 95% CI, at its edge. This tolerance was chosen for this evaluation, pre-registered relative to seeing any C2 or C result but not literature-derived, which we record as a limitation of the tolerance itself rather than of the measurement it gates.

## The B/D/C1 Comparison, With the Negation Asymmetry Disclosed

The prior review correctly identified that negation-polarity corruptions in the injected set are span *deletions* (the corrupted span is empty), so narrow-localization conditions (B, D, C2) structurally cannot attempt a negation repair at all -- fix\_success is trivially false for 100% of these rows by construction, not because of a repair-quality failure -- while broad-localization conditions (C1, C) can attempt them because their checker scans the whole sentence rather than masking a specific span. We now report every fix-rate and true-regression-rate figure both pooled including negation rows and pooled excluding them, so the two readings are never conflated.

Pooled *including* negation (240 rows, all four categories), Condition D's fix rate (0.7375) and true regression rate (0.0500) are identical to Condition B's, and its pooled $\Delta$COMET ($-0.0157$, CI $[-0.0226,-0.0097]$) is statistically indistinguishable from B's ($-0.0164$): basic output hygiene does not close the losing shared-task system's gap. Condition C1's pooled $\Delta$COMET is $-0.0035$ (CI $[-0.0071,-0.0008]$), roughly a fivefold reduction relative to B and D, but its fix rate including negation (0.4542) and true regression rate (0.1250) are both worse than B/D's.

Pooled *excluding* negation (180 rows, the three categories every condition can attempt), the picture sharpens: B and D's fix rate rises to 0.9833 and true regression rate to 0.0667, since the excluded negation rows were dragging both toward the middle; C1's fix rate rises to 0.6056 and its true regression rate to 0.1389. The gap between C1 and the narrow-localization baselines on categories C1 genuinely can attempt is therefore somewhat larger, not smaller, once the structurally-unattemptable negation rows are removed from B/D's denominator -- the negation asymmetry was inflating B/D's apparent advantage in the pooled-including reading, and excluding it reveals C1's correctness cost more starkly rather than explaining it away.

## Does Iteration Help? The Condition C2 Result

Condition C2 completed on the full 320-natural/240-injected-pool population, at a cost of \$0.045 across 930 OpenRouter calls -- well under budget. Table 2 places it alongside B, D, and C1.

| Condition | $\Delta$COMET (pooled) | Fix rate (excl. negation) | True regr. rate (excl. negation) | LLM calls / sentence |
|---|---|---|---|---|
| B | $-0.0164$ | 0.9833 | 0.0667 | $\sim$1.0 |
| D | $-0.0157$ | 0.9833 | 0.0667 | $\sim$1.0 |
| C1 | $-0.0035$ | 0.6056 | 0.1389 | 0.85 |
| C2 | $-0.0166$ | 0.9889 | 0.0722 | 2.29 (natural) |

*Table 2: Five-condition scorecard restricted to the four now-executed conditions. Fix rate and true regression rate are pooled excluding negation-deletion rows, which narrow-localization conditions (B, D, C2) cannot structurally attempt; $\Delta$COMET is pooled over the natural-row sample, both language pairs.*

C2's correctness metrics essentially match the simplest narrow-localization baselines: fix rate 0.9889 against B/D's 0.9833, true regression rate 0.0722 against B/D's 0.0667 -- both within a few points, neither a dramatic improvement over the baseline it iterates on top of. What C2 does dramatically improve on is C1: relative to C1's single-pass broadened localization, C2's narrow-but-iterated approach lifts fix rate by 0.29 points and lowers true regression rate by 0.07 points, both differences confirmed by a paired bootstrap on the 240 matched injected-pool rows (fix-rate difference $+0.2875$, 95% CI $[0.2292,0.3458]$; true-regression-rate difference $-0.0708$, CI $[-0.1167,-0.025]$, both excluding zero).

$\Delta$COMET moves the other way. C2's pooled $\Delta$COMET is $-0.0166$ (95% CI $[-0.0243,-0.0088]$), statistically indistinguishable from B and D, and a paired bootstrap against C1 on the same matched rows (using a normal-approximation substitute since only pooled, not per-row, $\Delta$COMET exists for C1) puts the C2-minus-C1 difference at $-0.0131$ (95% CI $[-0.0214,-0.0047]$), excluding zero in the direction that C2 is worse. Iterating a narrow, single-span repair against the checker does not, on this evidence, translate into a better-scoring sentence than checking the whole sentence once and stopping.

The mechanism test this protocol's original hypothesis specified therefore returns a mixed verdict, not the one-directional result the hypothesis anticipated: true regression rate and $\Delta$COMET move in opposite directions when C2 is compared against C1. Iteration is the load-bearing mechanism for recovering correctness -- fix rate and true regression rate -- but broadened localization, not iteration, is what has so far been shown to move whole-sentence quality. The two are not the same lever.

Part of the explanation is visible in edit volume and call count. C2's mean edit volume is 0.164 pooled -- close to B/D's 0.146 and nearly eight times C1's 0.021 -- despite C2's localization being nominally as narrow as B/D's. Each iteration pass re-repairs the same span, and across a mean 2.29 language-model calls per natural sentence (against C1's 0.85 and B/D's roughly 1.0), the cumulative text touched inside that one narrow span grows with every pass even though the span's boundaries do not. A checker that only verifies the categories it already knows to check cannot detect a repair that fixes the target invariant while degrading fluency or introducing an unrelated word choice elsewhere in the same short span -- exactly the kind of drift a whole-sentence reference-free metric like COMET is sensitive to and a narrow, category-scoped checker is not built to catch.

## Condition C Did Not Complete

Condition C -- broadened localization combined with iterative verification, the condition that would show whether C1's quality gain and C2's correctness gain can be obtained together -- was launched on the same data, checker, and repair model as C2. It completed checker validation (reproducing the identical eight-cell result in Table 1) and began processing the first language pair, en-ru\_RU. It then stalled: repeated polling over more than an hour showed zero filesystem activity, no error, and no output file. We report this as an infrastructure failure, not a null or negative result for Condition C itself, and we did not substitute an estimate, a partial run, or a proxy metric in its place. Every table and verdict in this paper that depends on Condition C is marked accordingly: the paper's overall assessment of whether iterative verification makes scoped editing net-positive is undetermined, specifically because the one condition designed to answer that combined question has not yet produced a result.

## The Six-Language-Pair Reconciliation

The prior iteration replaced this project's original three-point comparison of published numbers with the complete six-language-pair record for both Task 3 scoped-editing systems from the WMT25 findings paper [3]: the losing system, SURREYPAI-S2, is negative on all six pairs ($-0.007$ to $-0.014$ $\Delta$COMET), while the stronger-model system, BASELINE-S2, is non-negative on four of six and negative on the remaining two (English-Japanese, English-Chinese). That record still supports the diagnosis this project's protocol is built to test -- capability and implementation maturity explain most, though not all, of the gap between the two published systems -- and our own Condition B, run under the real COMET checkpoint on two of these six pairs, reproduces SURREYPAI-S2's negative direction and rough magnitude, giving the diagnosis an independently measured data point beyond the two systems' self-reports. Nothing in this iteration's C2 result or Condition C's non-completion changes that reconciliation; it bears on localization and iteration, questions the six-language-pair record cannot address on its own.

# Discussion

**What this iteration establishes, and what it does not.** Iteration, holding localization narrow, recovers fix rate and true regression rate to near-parity with the simplest baselines, at more than double the inference cost and with no improvement in $\Delta$COMET. Broadened localization without iteration (C1) remains the only condition executed so far that measurably improves $\Delta$COMET. Whether combining both -- broadened localization checked and re-verified across multiple passes -- captures C1's quality gain without C2's correctness shortfall, or inherits C2's flat quality result despite broader coverage, remains exactly as open as it was before this iteration, because Condition C did not complete.

**Why iteration helps correctness but not quality.** C2's fix rate and true regression rate improve over C1 because iteration lets the system catch and retry a repair the checker still flags, which single-pass C1 cannot do. But each retry edits the same narrow span again, and C2's mean edit volume (0.164) approaches B/D's despite starting from the same narrow localization -- iteration substitutes for breadth as a way of accumulating edits, not as a way of avoiding them. A checker that verifies only the specific invariant categories it tracks has no way to detect when a retry, in the process of fixing that invariant, degrades fluency or introduces a different, unflagged problem nearby; a whole-sentence metric like $\Delta$COMET is sensitive to exactly that kind of collateral drift. This suggests iteration's value is real but narrower than the protocol's original hypothesis anticipated: it is a mechanism for recovering targeted correctness on the specific things a checker is built to check, not a general-purpose quality improver, and crediting it for both would have been the wrong lesson to draw from a result that, on inspection, moves the two axes in opposite directions.

**What this means for a practitioner.** C1 and C2 are not one dominating the other; they trade off. A deployment that is scored primarily on aggregate translation quality, and where an occasional uncaught error is tolerable, is better served by C1's single-pass broadened check. A deployment in a regulated, terminology-heavy domain, where a single wrong number, name, or negation is a severe and auditable failure independent of the sentence's aggregate score, is better served by C2's near-total fix rate and low regression rate, even at a measured cost in $\Delta$COMET and roughly $2.3\times$ the inference calls of a single pass. Neither condition is a strict improvement on the shared task's own worst-ranked system in every metric simultaneously; each is an improvement on a different axis of it.

**Limitations.** The most consequential limitation is that Condition C, the one condition that could show whether C1's and C2's gains combine, did not complete, so this paper cannot state whether the protocol's central question -- what actually fixes scoped machine translation editing -- has a "both" answer or a "trade-off" answer at the level the original design was built to distinguish. A second is coverage: the executed comparison, now including C2, still runs on two of six language pairs, both Slavic-family languages with capitalization-based entity detection, the setting where the checker performs best per Table 1. A third is the repair-model substitution: `google/gemma-3-12b-it` passes the pre-registered fidelity tolerance in Section 6.2 as a borderline rather than unqualified pass, and it still lacks the original TowerPlus-9B's machine-translation-specific fine-tuning. A fourth is that the C2-versus-C1 $\Delta$COMET comparison in Section 6.4 uses a normal-approximation substitute for a paired test, since only pooled, not per-row, $\Delta$COMET exists for C1 in the artifact this iteration builds on; a genuinely paired per-row comparison would need C1 re-scored at row level.

**What the next iteration must do.** One thing, directly enabled by this iteration's infrastructure: re-run Condition C with whatever caused the stall diagnosed and fixed -- most plausibly a per-language-pair checkpointing and timeout mechanism the C2 run did not need because it completed within a single continuous pass -- so the paper can finally report whether broadened localization and iteration combine, trade off, or interact in some third way. A second, lower-priority extension is the remaining four language pairs, prioritizing Chinese and Japanese because that is where Table 1's checker validation is weakest and a CJK-capable entity extractor, not just more compute, is the prerequisite for a fair test there.

# Conclusion

This iteration ran the comparison the protocol was originally built to run -- narrow localization with iteration (C2) against broad localization without it (C1) -- and found a genuinely mixed result rather than the clean confirmation its hypothesis anticipated. Iteration recovers fix rate and true regression rate to near-parity with the simplest baselines, at more than double the inference cost, while broadened localization remains the only mechanism so far shown to move whole-sentence translation quality. Condition C, the run that would show whether these two gains combine, stalled before producing output, and we report that honestly as an open question rather than an answer. What is now established is narrower than what was hypothesized, and more useful for exactly that reason: a practitioner choosing between these two mechanisms is choosing between quality and auditable correctness, not choosing a strictly dominant option, until the combined condition finally runs.

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The paper's central open question -- whether broadened localization (C1's quality gain) and iteration (C2's correctness gain) can be captured together -- is exactly the question Condition C was designed to answer, and it did not complete. Every headline framing in the Abstract-equivalent contributions list, Discussion, and Conclusion correctly flags this as undetermined, which is honest, but it also means this iteration's actual deliverable is 'C2 alone does not dominate C1' plus an open combined-condition question, not a resolution of the protocol's motivating hypothesis. A reviewer weighing this paper against the bar of a completed mechanism study will find the single most decision-relevant experiment missing.
  Action: Prioritize re-running Condition C with the checkpointing/timeout fix the paper already proposes in 'What the next iteration must do,' before the next review round. If a re-run is not possible in the available budget, consider reporting whatever partial output exists from the stalled en-ru_RU pass (even a handful of completed rows) as a heavily-caveated directional signal, clearly separated from the paper's confirmed results, rather than leaving Condition C as a total blank.
- [MAJOR] (rigor) The text reports the C2-vs-C1 fix-rate advantage as '0.29 points' with a paired-bootstrap difference of +0.2875 (95% CI [0.2292, 0.3458]) computed 'on the 240 matched injected-pool rows.' But Table 2's pooled-excluding-negation fix rates for the same two conditions are C1=0.6056 and C2=0.9889, a difference of 0.3833 -- roughly 33% larger than the paired-bootstrap figure. The likely explanation is that the 240-row paired bootstrap includes negation-deletion rows (where C2 structurally cannot attempt a repair and therefore counts as a non-fix, while C1's checker-based localization can attempt them), narrowing the observed gap relative to the excluding-negation table. But the paper never states this, so the two numbers -- both presented as authoritative comparisons of the exact same two conditions -- appear to contradict each other, and a reader has no way to know which one is 'the' C2-vs-C1 fix-rate advantage without independently reconstructing the arithmetic.
  Action: State explicitly, next to the paired-bootstrap fix-rate result, which row population it is computed over (240 rows including negation, where C2's structural non-attempt on negation rows counts against it) and that this differs from Table 2's excluding-negation comparison for that reason. Either report both figures side by side with this explanation, or pick one consistent denominator for both the table and the paired-bootstrap test and state which was chosen and why.
- [MAJOR] (methodology) The paper's two outcome axes are measured on two structurally disjoint populations: ΔCOMET (the 'quality' evidence) is computed on the 320 natural WMT25 rows, while fix rate and true regression rate (the 'correctness' evidence) are computed on the 240 injected-pool rows with known ground-truth corruptions. No row is ever scored on both axes simultaneously. Table 2 and the Discussion nonetheless synthesize these into a single narrative ('iteration recovers correctness but not quality') as if they describe the same underlying repair behavior on the same sentences. This is methodologically defensible as a design choice (natural rows have no ground-truth 'correct fix' to score against; injected rows have no natural QE-severity distribution), but the paper never surfaces the fact that its central 'mixed verdict' rests on combining evidence from two different samples, which is a materially different (and weaker) form of evidence than a single population scored on both axes would provide.
  Action: Add an explicit statement in Section 6.4 or the Discussion's mechanism paragraph noting that ΔCOMET and fix-rate/regression are measured on disjoint populations (natural vs. injected), and discuss what this implies for the causal story being told (e.g., that the 'checker-invisible collateral drift' explanation for the ΔCOMET result is inferred, not directly observed, since no natural row's per-row correctness is ever checked against a ground truth).
- [MINOR] (rigor) The C2-vs-C1 ΔCOMET paired-bootstrap comparison (the basis for the claim that C2 is 'measurably worse' than C1 in ΔCOMET, CI [-0.0214, -0.0047]) is described only as using 'a normal-approximation substitute since only pooled, not per-row, ΔCOMET exists for C1.' No formula, variance-imputation method, or justification for the normal approximation's validity is given, even though this is the statistical basis for one of the paper's two headline directional claims.
  Action: Add a short methods note (even a sentence with the imputed per-row variance assumption, e.g. 'C1's per-row ΔCOMET distribution is approximated as Gaussian with the pooled mean and an assumed variance derived from B/D's per-row spread') so the comparison is auditable, or footnote why this substitute is expected to be conservative/anti-conservative relative to a true paired test.
- [MINOR] (scope) The executed comparison remains restricted to en-ru_RU and en-uk_UA -- the two language pairs where the checker performs best per Table 1 (capitalization-based NER, strongest negation-polarity detection). This is disclosed in Limitations, but the Discussion's practitioner guidance ('a deployment... is better served by C2's near-total fix rate...') is phrased as general advice without a scope caveat at the point it is given, which risks a reader over-generalizing the trade-off to language pairs where the checker's own validation (Table 1) shows it performs far worse (e.g., named-entity detection excluded outright for both tested languages).
  Action: Add a one-clause scope qualifier directly in the practitioner-guidance paragraph (e.g., 'within the two Slavic pairs and checker categories validated here') rather than relying on the separate Limitations section to carry that caveat.
- [MINOR] (novelty) The Related Work claims this is 'to our knowledge, the first controlled evidence in this literature that separates check more of the sentence once (C1) from iterate on the same narrow check (C2) as distinct levers.' This is a strong priority claim that is plausible given the related-work survey shown, but it is not independently verifiable from the paper alone, and the surveyed related work (APE-with-QE-signal, Grid Beam Search, LLM-as-judge post-editing, xTower explanation-based correction, Self-Refine, CEGIS, locate-and-edit energy-guided generation) is broad enough that a closely related ablation could plausibly exist in venues not covered by this search (e.g., iterative constrained decoding literature, or QE-guided automatic post-editing surveys).
  Action: Soften the priority claim slightly (e.g., 'we are not aware of' rather than 'the first') unless an additional targeted search specifically for 'iterative QE-guided post-editing' or 'checker-in-the-loop machine translation repair' turns up nothing closer, in which case keep the stronger claim but note the specific search terms used.
- [MINOR] (clarity) The recurring pattern of infrastructure failures across this project's iterations (this iteration's Condition C stall; the prior iteration's HuggingFace Hub 429 forcing a substitute LLM-judge proxy for Condition B, later redone with real COMET) is each individually well-disclosed, but the paper never steps back to note this as a pattern worth a sentence of its own -- e.g., whether the checkpointing fix proposed for Condition C would also have prevented the earlier COMET-checkpoint-access failure, or whether these are unrelated infrastructure risks.
  Action: Optional: add one sentence in Limitations or 'What the next iteration must do' acknowledging that this is the second execution stall/substitution across this project's iterations, and that a general run-robustness mechanism (checkpointing, timeout, retry-with-backoff) would benefit the whole pipeline, not just Condition C specifically.
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

### [3] HUMAN-USER prompt · 2026-09-01 09:18:46 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Bash · 2026-09-01 09:19:14 UTC

```
Check working directory:
mkdir -p "$(dirname ./.terminal_claude_agent_struct_out.json)" 2>/dev/null; pwd
```

### [5] TOOL RESULT — Bash · 2026-09-01 09:19:14 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [6] TOOL CALL — Write · 2026-09-01 09:20:12 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Finish Condition C and Make the Mixed Result Auditable",
      "objective": "Complete the protocol's one still-missing, most decision-relevant experiment -- Condition C (broad localization plus iterative verification) -- with a run-robustness fix that survives the exact stall observed last iteration, then rebuild the five-condition scorecard on a genuinely paired, disjoint-population-disclosed statistical footing so every reviewer MAJOR/MINOR critique from this iteration is closed with evidence rather than caveat prose alone.",
      "rationale": "The reviewer's two MAJOR-rigor/methodology critiques and its one MAJOR-evidence critique all point at the same root cause: this project has been reporting a mixed mechanism finding (C2 recovers correctness, C1 moves quality) without ever running the one condition that tests whether the two combine, and without ever computing the one statistic (a true paired C1-vs-C2 ΔCOMET test) that the paper's current normal-approximation substitute stands in for. Both gaps are closeable with real data already sitting in this project's artifacts. First, art_7Uc5PlFctjXi's bootstrap CIs for C1's pooled ΔCOMET could only have been computed from per-row ΔCOMET values that were never surfaced pooled-only in the summary -- if those per-row values are recoverable from full_method_out.json (they must exist to have produced a bootstrap CI at all), a genuine paired bootstrap against C2's per-row values (already reported per-row in art_K8koUmGFDlLN) replaces the documented-but-unjustified normal-approximation substitute with an auditable, no-imputation comparison; if the per-row array turns out not to be persisted after all, the evaluation must say so explicitly and fall back to a documented, formula-stated approximation rather than the current undocumented one -- either outcome is strictly better than what exists now. Second, the disjoint-population caveat the reviewer names (ΔCOMET on 320 natural rows, fix-rate/regression on 240 injected-pool rows, never the same row scored on both axes) is directly checkable and should be reported as a quantified fact (a literal zero-overlap check on row IDs) rather than left as an inferred property. Third, and most consequential: Condition C's prior stall happened with zero diagnostic instrumentation -- no per-language-pair checkpoint, no per-row incremental write, no retry-with-backoff on whatever call hung -- so a rerun using the exact same script shape would be as likely to stall again with as little evidence of why. This project has now hit two separate execution stalls (an HF Hub 429 on Condition B's COMET checkpoint, and Condition C's silent hang) across three iterations; treating that as a pattern rather than two isolated incidents means the rerun's design goal is not just 'get more rows' but 'never lose an hour of progress to an unlogged, unretried failure again,' with the fix built to generalize rather than special-cased to whatever caused the specific stall. With only one iteration left after this one, completing Condition C now -- with the robustness this iteration adds -- is the single highest-leverage action available: every other reviewer critique is a reporting fix on data that already exists, but Condition C's absence is a genuine, irreducible evidence gap that no amount of re-analysis of B/D/C1/C2 can substitute for.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Execute Condition C (checker-broadened localization combined with iterative repair-and-reverify to a certificate or a fixed pass budget) to completion on the identical 320-natural/240-injected-pool row population, repair model (google/gemma-3-12b-it), and checker used for B/D/C1/C2, with run-robustness instrumentation specifically designed to survive or clearly diagnose the exact failure mode that stalled the prior attempt.",
          "approach": "Reuse the checker module, OpenRouter async client, and row-selection/stratification code verbatim from art_K8koUmGFDlLN (the completed C2 artifact, which already regenerated and row-ID-verified the same population against B/D/C1), combining C1's checker-broadened localization logic (every checker-flagged invariant in the sentence, gated by the within-experiment usability table) with C2's iterate-and-reverify loop (checker-detail-scoped re-repair up to a 3-pass budget, stop on certificate). Before the full sweep, add four concrete robustness measures the prior C artifact lacked: (1) per-row, per-pass incremental JSON-lines writes to disk immediately after each OpenRouter call returns, so a stall anywhere loses at most one in-flight call rather than an hour of unwritten progress; (2) a hard per-call timeout (e.g. 60-90s) with exponential-backoff retry (3 attempts) wrapping every OpenRouter request, since the prior stall showed zero filesystem activity for over an hour with no error -- consistent with a hung network call that never returned and never raised; (3) a watchdog that logs a heartbeat every N rows/seconds so a rerun's own logs can show whether progress is steady or has stopped, turning a future stall into a diagnosable event rather than a repeat of 'no error, no output'; (4) resumability from the last successfully-written row so a restart after any failure does not repeat already-completed work. Run the full sweep under this instrumentation, with the same $2 pre-declared sub-budget methodology C2 used (a small pilot-subset cost probe before committing to the full run), tracked against the shared $10 ceiling with C2's $0.045 spend as the reference point. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da on the 320 natural rows (persisting PER-ROW ΔCOMET values, not only pooled, explicitly so a downstream evaluation can run a true paired test against C1/C2 rather than an approximation), fix rate and true regression rate on the 240 injected-pool rows broken out by invariant category and by pooled-including/excluding-negation (negation rows are attemptable under this condition's checker-based localization, unlike B/D/C2's oracle-span localization -- log this per-row, not just in aggregate), edit volume per pass and cumulative, and LLM calls per sentence. If, despite the robustness measures, the run still cannot complete within a generous wall-clock budget, write out whatever rows did complete (even a partial subset) with an explicit completion-fraction field and per-language-pair breakdown, rather than producing nothing -- but attempt the full run first and only fall back to a partial report if it is genuinely still incomplete after retries and the extended budget.",
          "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_K8koUmGFDlLN", "label": "reference implementation"},
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 baseline"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Produce the paper's first genuinely complete, statistically-auditable five-condition (B/D/C1/C2/C) scorecard: replace the normal-approximation C1-vs-C2 substitute with a true per-row paired test wherever the underlying per-row data can be recovered, quantify the disjoint-population caveat as a checked fact rather than an inferred one, reconcile the two fix-rate-advantage figures the reviewer flagged as apparently contradictory, and compute the net-positive verdict for Condition C now that it exists.",
          "approach": "Load B/D/C1 from art_7Uc5PlFctjXi's full_method_out.json and inspect it for a persisted per-row ΔCOMET array (the bootstrap CI reported there could only have been computed from one); if present, use it directly for a true paired bootstrap of C1-vs-C2 and C1-vs-C ΔCOMET on matched natural rows, replacing the documented normal-approximation substitute entirely and stating so explicitly; if genuinely absent, fall back to an explicitly formula-stated approximation (state the imputed variance assumption in the output, e.g. derived from B/D's measured per-row spread) rather than the prior undocumented one, and flag this as a methods note for the paper. Load C2 from art_K8koUmGFDlLN and Condition C from this strategy's new experiment artifact (discovered at run time by matching gen_plan title, per this project's established same-iteration-sibling pattern, since no formal dependency edge is possible); if Condition C produced only a partial run, degrade its fields explicitly to a stated completion fraction rather than treating partial output as final, per this project's established graceful-degradation convention. Compute and report, as a first-class output field, a literal zero-overlap verification between the row-ID sets used for ΔCOMET scoring (320 natural rows) and fix-rate/regression scoring (240 injected-pool rows), stating this as the quantified basis for the paper's disjoint-population caveat rather than an inferred property. Reconcile the two fix-rate-advantage numbers the reviewer flagged (paired-bootstrap +0.2875 on 240 rows including negation vs Table 2's +0.3833 on 180 rows excluding it): report both explicitly side by side, labeled by exact row population and denominator, with the arithmetic explanation (negation rows count against C2 in the including-negation population since C2 structurally cannot attempt them, narrowing the observed gap) stated as a field, not left for the paper text to reconstruct. Finally, run the hypothesis's own pre-specified success/disconfirmation test for full Condition C: non-negative-or-near-zero mean ΔCOMET together with a true regression rate significantly below B's at a comparable-or-higher fix rate, without edit volume collapsing toward full-retranslation levels (compare C's mean edit volume against C1's 0.021 and B/D's 0.146 baselines) -- and state a CONFIRMED / DISCONFIRMED / MIXED verdict for the protocol's central combined-condition question, rather than leaving it UNDETERMINED as the prior iteration's evaluation did.",
          "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 results"},
            {"id": "art_K8koUmGFDlLN", "label": "C2 results"},
            {"id": "art__bfSxpVnFUc8", "label": "prior reconciliation"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"}
          ]
        },
        {
          "type": "research",
          "objective": "Run a targeted, specifically-worded literature search for the exact mechanism this protocol separates -- iterative, checker- or verifier-gated repair of a narrowly localized machine-translation span, held apart from broadened one-pass error localization -- to either support the paper's current 'first controlled evidence separating these two levers' claim with a stated negative search result, or surface a closer prior ablation that the existing related-work survey (APE-with-QE-signal, Grid Beam Search, LLM-as-judge post-editing, xTower, Self-Refine, CEGIS, locate-and-edit) missed.",
          "approach": "Search specifically for terms the existing related-work survey did not use as primary query terms: 'iterative QE-guided post-editing', 'checker-in-the-loop machine translation repair', 'verify-and-repair span editing translation', 'iterative constrained decoding machine translation error correction', and 'localization breadth versus iteration machine translation', across both general and scholarly search modes. For any candidate that surfaces, fetch and read closely enough to determine whether it (a) holds localization breadth and iteration apart as two separately varied, independently measured factors the way this protocol's C1-vs-C2 design does, or (b) bundles them (as every paper in the current related-work section does) or tests only one. Report a clear verdict: either no candidate found that separates the two factors (supporting the paper's current strong claim, with the exact search terms used logged so the claim can cite its own search scope rather than asserting novelty unconditionally), or a specific closer paper found (in which case report its exact mechanism, venue, and how it differs from this protocol's design, so the paper can be revised from 'first' to a scoped, differentiated novelty claim). Do not fabricate a verdict either way -- report exactly what was and was not found, with citations.",
          "depends_on": []
        }
      ],
      "expected_outcome": "A completed Condition C run with real per-row ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count numbers on the same rows/model/checker as B/D/C1/C2, produced under run-robustness instrumentation that either survives the prior stall or diagnoses it clearly instead of reproducing an hour of silent, unlogged failure; a rebuilt five-condition scorecard that replaces the undocumented normal-approximation C1-vs-C2 substitute with a true paired test wherever the underlying per-row data exists (or an explicitly formula-stated approximation where it does not), reports a literal, checked zero-overlap verification for the disjoint-population caveat rather than an inferred claim, reconciles the two previously-discrepant fix-rate-advantage figures side by side with their exact row populations named, and returns a CONFIRMED/DISCONFIRMED/MIXED verdict for the protocol's central combined-condition question instead of leaving it undetermined; and a targeted-search resolution of the paper's novelty claim about separating localization breadth from iteration, either strengthening it with a stated search scope or narrowing it to a specific closer prior work -- collectively closing all three MAJOR reviewer critiques and two of the three MINOR ones with new evidence rather than caveat language alone.",
      "summary": "Reruns Condition C -- the protocol's single missing, most decision-relevant experiment -- with checkpointing, retries, and heartbeats designed against the exact stall that killed the prior attempt, pairs it with a reconciliation evaluation that replaces the paper's normal-approximation statistical substitute with a true paired test and turns two reviewer-flagged apparent contradictions into explicitly reconciled, quantified facts, and runs one targeted search to settle the paper's novelty claim rather than leaving it asserted."
    }
  ]
}
```

### [7] TOOL RESULT — Write · 2026-09-01 09:20:12 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Finish Condition C and Make the Mixed Result Auditable\",\n      \"objective\": \"Complete the protocol's one still-missing, most decision-relevant experiment -- Condition C (broad localization plus iterative verification) -- with a run-robustness fix that survives the exact stall observed last iteration, then rebuild the five-condition scorecard on a genuinely paired, disjoint-population-disclosed statistical footing so every reviewer MAJOR/MINOR critique from this iteration is closed with evidence rather than caveat prose alone.\",\n      \"rationale\": \"The reviewer's two MAJOR-rigor/methodology critiques and its one MAJOR-evidence critique all point at the same root cause: this project has been reporting a mixed mechanism finding (C2 recovers correctness, C1 moves quality) without ever running the one condition that tests whether the two combine, and without ever computing the one statistic (a true paired C1-vs-C2 ΔCOMET test) that the paper's current normal-approximation substitute stands in for. Both gaps are closeable with real data already sitting in this project's artifacts. First, art_7Uc5PlFctjXi's bootstrap CIs for C1's pooled ΔCOMET could only have been computed from per-row ΔCOMET values that were never surfaced pooled-only in the summary -- if those per-row values are recoverable from full_method_out.json (they must exist to have produced a bootstrap CI at all), a genuine paired bootstrap against C2's per-row values (already reported per-row in art_K8koUmGFDlLN) replaces the documented-but-unjustified normal-approximation substitute with an auditable, no-imputation comparison; if the per-row array turns out not to be persisted after all, the evaluation must say so explicitly and fall back to a documented, formula-stated approximation rather than the current undocumented one -- either outcome is strictly better than what exists now. Second, the disjoint-population caveat the reviewer names (ΔCOMET on 320 natural rows, fix-rate/regression on 240 injected-pool rows, never the same row scored on both axes) is directly checkable and should be reported as a quantified fact (a literal zero-overlap check on row IDs) rather than left as an inferred property. Third, and most consequential: Condition C's prior stall happened with zero diagnostic instrumentation -- no per-language-pair checkpoint, no per-row incremental write, no retry-with-backoff on whatever call hung -- so a rerun using the exact same script shape would be as likely to stall again with as little evidence of why. This project has now hit two separate execution stalls (an HF Hub 429 on Condition B's COMET checkpoint, and Condition C's silent hang) across three iterations; treating that as a pattern rather than two isolated incidents means the rerun's design goal is not just 'get more rows' but 'never lose an hour of progress to an unlogged, unretried failure again,' with the fix built to generalize rather than special-cased to whatever caused the specific stall. With only one iteration left after this one, completing Condition C now -- with the robustness this iteration adds -- is the single highest-leverage action available: every other reviewer critique is a reporting fix on data that already exists, but Condition C's absence is a genuine, irreducible evidence gap that no amount of re-analysis of B/D/C1/C2 can substitute for.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Execute Condition C (checker-broadened localization combined with iterative repair-and-reverify to a certificate or a fixed pass budget) to completion on the identical 320-natural/240-injected-pool row population, repair model (google/gemma-3-12b-it), and checker used for B/D/C1/C2, with run-robustness instrumentation specifically designed to survive or clearly diagnose the exact failure mode that stalled the prior attempt.\",\n          \"approach\": \"Reuse the checker module, OpenRouter async client, and row-selection/stratification code verbatim from art_K8koUmGFDlLN (the completed C2 artifact, which already regenerated and row-ID-verified the same population against B/D/C1), combining C1's checker-broadened localization logic (every checker-flagged invariant in the sentence, gated by the within-experiment usability table) with C2's iterate-and-reverify loop (checker-detail-scoped re-repair up to a 3-pass budget, stop on certificate). Before the full sweep, add four concrete robustness measures the prior C artifact lacked: (1) per-row, per-pass incremental JSON-lines writes to disk immediately after each OpenRouter call returns, so a stall anywhere loses at most one in-flight call rather than an hour of unwritten progress; (2) a hard per-call timeout (e.g. 60-90s) with exponential-backoff retry (3 attempts) wrapping every OpenRouter request, since the prior stall showed zero filesystem activity for over an hour with no error -- consistent with a hung network call that never returned and never raised; (3) a watchdog that logs a heartbeat every N rows/seconds so a rerun's own logs can show whether progress is steady or has stopped, turning a future stall into a diagnosable event rather than a repeat of 'no error, no output'; (4) resumability from the last successfully-written row so a restart after any failure does not repeat already-completed work. Run the full sweep under this instrumentation, with the same $2 pre-declared sub-budget methodology C2 used (a small pilot-subset cost probe before committing to the full run), tracked against the shared $10 ceiling with C2's $0.045 spend as the reference point. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da on the 320 natural rows (persisting PER-ROW ΔCOMET values, not only pooled, explicitly so a downstream evaluation can run a true paired test against C1/C2 rather than an approximation), fix rate and true regression rate on the 240 injected-pool rows broken out by invariant category and by pooled-including/excluding-negation (negation rows are attemptable under this condition's checker-based localization, unlike B/D/C2's oracle-span localization -- log this per-row, not just in aggregate), edit volume per pass and cumulative, and LLM calls per sentence. If, despite the robustness measures, the run still cannot complete within a generous wall-clock budget, write out whatever rows did complete (even a partial subset) with an explicit completion-fraction field and per-language-pair breakdown, rather than producing nothing -- but attempt the full run first and only fall back to a partial report if it is genuinely still incomplete after retries and the extended budget.\",\n          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"reference implementation\"},\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 baseline\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Produce the paper's first genuinely complete, statistically-auditable five-condition (B/D/C1/C2/C) scorecard: replace the normal-approximation C1-vs-C2 substitute with a true per-row paired test wherever the underlying per-row data can be recovered, quantify the disjoint-population caveat as a checked fact rather than an inferred one, reconcile the two fix-rate-advantage figures the reviewer flagged as apparently contradictory, and compute the net-positive verdict for Condition C now that it exists.\",\n          \"approach\": \"Load B/D/C1 from art_7Uc5PlFctjXi's full_method_out.json and inspect it for a persisted per-row ΔCOMET array (the bootstrap CI reported there could only have been computed from one); if present, use it directly for a true paired bootstrap of C1-vs-C2 and C1-vs-C ΔCOMET on matched natural rows, replacing the documented normal-approximation substitute entirely and stating so explicitly; if genuinely absent, fall back to an explicitly formula-stated approximation (state the imputed variance assumption in the output, e.g. derived from B/D's measured per-row spread) rather than the prior undocumented one, and flag this as a methods note for the paper. Load C2 from art_K8koUmGFDlLN and Condition C from this strategy's new experiment artifact (discovered at run time by matching gen_plan title, per this project's established same-iteration-sibling pattern, since no formal dependency edge is possible); if Condition C produced only a partial run, degrade its fields explicitly to a stated completion fraction rather than treating partial output as final, per this project's established graceful-degradation convention. Compute and report, as a first-class output field, a literal zero-overlap verification between the row-ID sets used for ΔCOMET scoring (320 natural rows) and fix-rate/regression scoring (240 injected-pool rows), stating this as the quantified basis for the paper's disjoint-population caveat rather than an inferred property. Reconcile the two fix-rate-advantage numbers the reviewer flagged (paired-bootstrap +0.2875 on 240 rows including negation vs Table 2's +0.3833 on 180 rows excluding it): report both explicitly side by side, labeled by exact row population and denominator, with the arithmetic explanation (negation rows count against C2 in the including-negation population since C2 structurally cannot attempt them, narrowing the observed gap) stated as a field, not left for the paper text to reconstruct. Finally, run the hypothesis's own pre-specified success/disconfirmation test for full Condition C: non-negative-or-near-zero mean ΔCOMET together with a true regression rate significantly below B's at a comparable-or-higher fix rate, without edit volume collapsing toward full-retranslation levels (compare C's mean edit volume against C1's 0.021 and B/D's 0.146 baselines) -- and state a CONFIRMED / DISCONFIRMED / MIXED verdict for the protocol's central combined-condition question, rather than leaving it UNDETERMINED as the prior iteration's evaluation did.\",\n          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},\n            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"C2 results\"},\n            {\"id\": \"art__bfSxpVnFUc8\", \"label\": \"prior reconciliation\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Run a targeted, specifically-worded literature search for the exact mechanism this protocol separates -- iterative, checker- or verifier-gated repair of a narrowly localized machine-translation span, held apart from broadened one-pass error localization -- to either support the paper's current 'first controlled evidence separating these two levers' claim with a stated negative search result, or surface a closer prior ablation that the existing related-work survey (APE-with-QE-signal, Grid Beam Search, LLM-as-judge post-editing, xTower, Self-Refine, CEGIS, locate-and-edit) missed.\",\n          \"approach\": \"Search specifically for terms the existing related-work survey did not use as primary query terms: 'iterative QE-guided post-editing', 'checker-in-the-loop machine translation repair', 'verify-and-repair span editing translation', 'iterative constrained decoding machine translation error correction', and 'localization breadth versus iteration machine translation', across both general and scholarly search modes. For any candidate that surfaces, fetch and read closely enough to determine whether it (a) holds localization breadth and iteration apart as two separately varied, independently measured factors the way this protocol's C1-vs-C2 design does, or (b) bundles them (as every paper in the current related-work section does) or tests only one. Report a clear verdict: either no candidate found that separates the two factors (supporting the paper's current strong claim, with the exact search terms used logged so the claim can cite its own search scope rather than asserting novelty unconditionally), or a specific closer paper found (in which case report its exact mechanism, venue, and how it differs from this protocol's design, so the paper can be revised from 'first' to a scoped, differentiated novelty claim). Do not fabricate a verdict either way -- report exactly what was and was not found, with citations.\",\n          \"depends_on\": []\n        }\n      ],\n      \"expected_outcome\": \"A completed Condition C run with real per-row ΔCOMET, fix-rate, true-regression-rate, edit-volume, and call-count numbers on the same rows/model/checker as B/D/C1/C2, produced under run-robustness instrumentation that either survives the prior stall or diagnoses it clearly instead of reproducing an hour of silent, unlogged failure; a rebuilt five-condition scorecard that replaces the undocumented normal-approximation C1-vs-C2 substitute with a true paired test wherever the underlying per-row data exists (or an explicitly formula-stated approximation where it does not), reports a literal, checked zero-overlap verification for the disjoint-population caveat rather than an inferred claim, reconciles the two previously-discrepant fix-rate-advantage figures side by side with their exact row populations named, and returns a CONFIRMED/DISCONFIRMED/MIXED verdict for the protocol's central combined-condition question instead of leaving it undetermined; and a targeted-search resolution of the paper's novelty claim about separating localization breadth from iteration, either strengthening it with a stated search scope or narrowing it to a specific closer prior work -- collectively closing all three MAJOR reviewer critiques and two of the three MINOR ones with new evidence rather than caveat language alone.\",\n      \"summary\": \"Reruns Condition C -- the protocol's single missing, most decision-relevant experiment -- with checkpointing, retries, and heartbeats designed against the exact stall that killed the prior attempt, pairs it with a reconciliation evaluation that replaces the paper's normal-approximation statistical substitute with a true paired test and turns two reviewer-flagged apparent contradictions into explicitly reconciled, quantified facts, and runs one targeted search to settle the paper's novelty claim rather than leaving it asserted.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [8] ASSISTANT · 2026-09-01 09:20:16 UTC

```
Strategy written to `.terminal_claude_agent_struct_out.json`. It plans three parallel artifacts for iteration 4:

1. **Experiment** — a robustness-hardened rerun of Condition C (checkpointing, per-call timeout/retry, heartbeats, resumability) to finally complete the protocol's missing combined localization+iteration condition, addressing the MAJOR "Condition C never finished" critique.
2. **Evaluation** — reconciles the five-condition scorecard: replaces the undocumented normal-approximation C1-vs-C2 statistic with a true paired test if per-row data can be recovered, quantifies the disjoint-population caveat as a checked zero-overlap fact, reconciles the two discrepant fix-rate-advantage numbers side by side, and issues a real verdict for Condition C.
3. **Research** — a targeted search to either back up or narrow the paper's "first to separate localization breadth from iteration" novelty claim.
```

### [9] SYSTEM-USER prompt · 2026-09-01 09:20:19 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'experiment_iter4_dir1' (experiment): dependency 'art_K8koUmGFDlLN' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter4_dir1' (experiment): dependency 'art_7Uc5PlFctjXi' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'evaluation_iter4_dir2' (evaluation): dependency 'art__bfSxpVnFUc8' has type 'evaluation' which is not allowed (allowed: {'experiment', 'dataset'})

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

### [10] TOOL CALL — Edit · 2026-09-01 09:20:25 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_K8koUmGFDlLN", "label": "reference implementation"},
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 baseline"}
          ]
        },
        {
          "type": "evaluation",
NEW:           "depends_on": [
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"},
            {"id": "art_5ySTX4YfxqG_", "label": "resource dossier"}
          ]
        },
        {
          "type": "evaluation",
```

### [11] TOOL RESULT — Edit · 2026-09-01 09:20:25 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"reference implementation\"},\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 baseline\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",", "newString": "          \"depends_on\": [\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},\n            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",", "originalFile": null, "structuredPatch": [{"oldStart": 11, "oldLines": 8, "newStart": 11, "newLines": 7, "lines": ["           \"approach\": \"Reuse the checker module, OpenRouter async client, and row-selection/stratification code verbatim from art_K8koUmGFDlLN (the completed C2 artifact, which already regenerated and row-ID-verified the same population against B/D/C1), combining C1's checker-broadened localization logic (every checker-flagged invariant in the sentence, gated by the within-experiment usability table) with C2's iterate-and-reverify loop (checker-detail-scoped re-repair up to a 3-pass budget, stop on certificate). Before the full sweep, add four concrete robustness measures the prior C artifact lacked: (1) per-row, per-pass incremental JSON-lines writes to disk immediately after each OpenRouter call returns, so a stall anywhere loses at most one in-flight call rather than an hour of unwritten progress; (2) a hard per-call timeout (e.g. 60-90s) with exponential-backoff retry (3 attempts) wrapping every OpenRouter request, since the prior stall showed zero filesystem activity for over an hour with no error -- consistent with a hung network call that never returned and never raised; (3) a watchdog that logs a heartbeat every N rows/seconds so a rerun's own logs can show whether progress is steady or has stopped, turning a future stall into a diagnosable event rather than a repeat of 'no error, no output'; (4) resumability from the last successfully-written row so a restart after any failure does not repeat already-completed work. Run the full sweep under this instrumentation, with the same $2 pre-declared sub-budget methodology C2 used (a small pilot-subset cost probe before committing to the full run), tracked against the shared $10 ceiling with C2's $0.045 spend as the reference point. Score identically to C2: ΔCOMET via wmt22-cometkiwi-da on the 320 natural rows (persisting PER-ROW ΔCOMET values, not only pooled, explicitly so a downstream evaluation can run a true paired test against C1/C2 rather than an approximation), fix rate and true regression rate on the 240 injected-pool rows broken out by invariant category and by pooled-including/excluding-negation (negation rows are attemptable under this condition's checker-based localization, unlike B/D/C2's oracle-span localization -- log this per-row, not just in aggregate), edit volume per pass and cumulative, and LLM calls per sentence. If, despite the robustness measures, the run still cannot complete within a generous wall-clock budget, write out whatever rows did complete (even a partial subset) with an explicit completion-fraction field and per-language-pair breakdown, rather than producing nothing -- but attempt the full run first and only fall back to a partial report if it is genuinely still incomplete after retries and the extended budget.\",", "           \"depends_on\": [", "             {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"},", "-            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"reference implementation\"},", "-            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 baseline\"}", "+            {\"id\": \"art_5ySTX4YfxqG_\", \"label\": \"resource dossier\"}", "           ]", "         },", "         {"]}], "userModified": false, "replaceAll": false}
```

### [12] TOOL CALL — Edit · 2026-09-01 09:20:31 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 results"},
            {"id": "art_K8koUmGFDlLN", "label": "C2 results"},
            {"id": "art__bfSxpVnFUc8", "label": "prior reconciliation"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"}
          ]
        },
        {
          "type": "research",
NEW:           "depends_on": [
            {"id": "art_7Uc5PlFctjXi", "label": "B/D/C1 results"},
            {"id": "art_K8koUmGFDlLN", "label": "C2 results"},
            {"id": "art_QLpPxaqf1VzK", "label": "checker validation"},
            {"id": "art_mhfmDpGp4z1J", "label": "dataset"}
          ]
        },
        {
          "type": "research",
```

### [13] TOOL RESULT — Edit · 2026-09-01 09:20:31 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},\n            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"C2 results\"},\n            {\"id\": \"art__bfSxpVnFUc8\", \"label\": \"prior reconciliation\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}\n          ]\n        },\n        {\n          \"type\": \"research\",", "newString": "          \"depends_on\": [\n            {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},\n            {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"C2 results\"},\n            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},\n            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}\n          ]\n        },\n        {\n          \"type\": \"research\",", "originalFile": null, "structuredPatch": [{"oldStart": 21, "oldLines": 8, "newStart": 21, "newLines": 8, "lines": ["           \"depends_on\": [", "             {\"id\": \"art_7Uc5PlFctjXi\", \"label\": \"B/D/C1 results\"},", "             {\"id\": \"art_K8koUmGFDlLN\", \"label\": \"C2 results\"},", "-            {\"id\": \"art__bfSxpVnFUc8\", \"label\": \"prior reconciliation\"},", "-            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"}", "+            {\"id\": \"art_QLpPxaqf1VzK\", \"label\": \"checker validation\"},", "+            {\"id\": \"art_mhfmDpGp4z1J\", \"label\": \"dataset\"}", "           ]", "         },", "         {"]}], "userModified": false, "replaceAll": false}
```

### [14] ASSISTANT · 2026-09-01 09:20:31 UTC

```
Fixed both dependency-type violations: the Condition C experiment now depends only on the dataset and research resource dossier (dropping the invalid experiment-type deps), and the evaluation now depends on the two experiment artifacts (B/D/C1, C2) and the checker-validation experiment plus the dataset, dropping the invalid evaluation-type dependency on the prior reconciliation artifact.
```
