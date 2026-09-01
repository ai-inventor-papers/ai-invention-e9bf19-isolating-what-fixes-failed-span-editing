# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 09:20:35 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 09:20:41 UTC

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
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: research_iter4_dir3
type: research
objective: >-
  Run a targeted, specifically-worded literature search for the exact mechanism this protocol separates -- iterative, checker-
  or verifier-gated repair of a narrowly localized machine-translation span, held apart from broadened one-pass error localization
  -- to either support the paper's current 'first controlled evidence separating these two levers' claim with a stated negative
  search result, or surface a closer prior ablation that the existing related-work survey (APE-with-QE-signal, Grid Beam Search,
  LLM-as-judge post-editing, xTower, Self-Refine, CEGIS, locate-and-edit) missed.
approach: >-
  Search specifically for terms the existing related-work survey did not use as primary query terms: 'iterative QE-guided
  post-editing', 'checker-in-the-loop machine translation repair', 'verify-and-repair span editing translation', 'iterative
  constrained decoding machine translation error correction', and 'localization breadth versus iteration machine translation',
  across both general and scholarly search modes. For any candidate that surfaces, fetch and read closely enough to determine
  whether it (a) holds localization breadth and iteration apart as two separately varied, independently measured factors the
  way this protocol's C1-vs-C2 design does, or (b) bundles them (as every paper in the current related-work section does)
  or tests only one. Report a clear verdict: either no candidate found that separates the two factors (supporting the paper's
  current strong claim, with the exact search terms used logged so the claim can cite its own search scope rather than asserting
  novelty unconditionally), or a specific closer paper found (in which case report its exact mechanism, venue, and how it
  differs from this protocol's design, so the paper can be revised from 'first' to a scoped, differentiated novelty claim).
  Do not fabricate a verdict either way -- report exactly what was and was not found, with citations.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

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
  "description": "Plan for a RESEARCH artifact.",
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
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 09:20:41 UTC

```
AI in translation emwrging opportunities
```

### [4] ASSISTANT · 2026-09-01 09:20:48 UTC

```
I'll do a few grounding searches to make the plan concrete before writing it.
```

### [5] TOOL CALL — ToolSearch · 2026-09-01 09:20:48 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [6] TOOL RESULT — ToolSearch · 2026-09-01 09:20:48 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 23}
```

### [7] TOOL CALL — WebSearch · 2026-09-01 09:20:52 UTC

```
iterative QE-guided post-editing machine translation checker-in-the-loop verify repair
```

### [8] TOOL CALL — WebSearch · 2026-09-01 09:20:52 UTC

```
"verify-and-repair" OR "iterative repair" machine translation span editing localization ablation
```

### [9] TOOL CALL — WebSearch · 2026-09-01 09:20:52 UTC

```
xTower iterative machine translation error correction explanation feedback loop
```

### [10] TOOL RESULT — WebSearch · 2026-09-01 09:20:58 UTC

```
{"query": "iterative QE-guided post-editing machine translation checker-in-the-loop verify repair", "results": [{"tool_use_id": "srvtoolu_01QKZzifnwo4ETBnGoAoyXHd", "content": [{"title": "Machine Translation Post-Editing (MTPE): The Complete Guide | Crowdin Blog", "url": "https://crowdin.com/blog/mt-post-editing"}, {"title": "QE4PE: Word-level Quality Estimation for Human Post-Editing", "url": "https://arxiv.org/html/2503.03044"}, {"title": "Automatic Post-Editing for Machine Translation", "url": "https://arxiv.org/pdf/1910.08592"}, {"title": "Machine Translation Post-Editing: A Strategic Guide to Optimizing Output - Translated", "url": "https://translated.com/resources/machine-translation-post-editing-guide"}, {"title": "Sweep away messy translations: How AI is automating post-editing", "url": "https://www.rws.com/blog/how-ai-is-automating-post-editing/"}, {"title": "Machine translation post-editing: best practices, workflows, and tools in the AI era", "url": "https://phrase.com/blog/posts/machine-translation-post-editing/"}, {"title": "Translation Quality Assessment Tool - Free Translation QA Checker", "url": "https://www.tomedes.com/tools/post-translation"}, {"title": "Ensembling Factored Neural Machine Translation Models for Automatic Post-Editing and Quality Estimation", "url": "https://arxiv.org/pdf/1706.05083"}, {"title": "Identifying the Machine Translation Error Types with the Greatest Impact on Post-editing Effort - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5539081/"}]}, "Based on the search results, here's what I found regarding your query about iterative QE-guided post-editing machine translation:\n\n## Key Concepts Found\n\n**Quality Estimation (QE) in Post-Editing:**\n\nWord-level quality estimation (QE) methods aim to detect erroneous spans in machine translations, which can direct and facilitate human post-editing.\n\n**QE-Guided Approaches:**\n\nA QE+APE pipeline passes fine-grained word-level QE judgments for each MT token as additional information to the APE decoder, aiming to guide the decoder to change only those words marked as \"bad\" to retain correct MT tokens in the output.\n\n**Iterative Refinement:**\n\nThe process of iterating the evaluate/refine task loop is repeated up to three times, incorporating additional context from the source document as needed to increase the chance of enhanced translation accuracy. Additionally, edits made by the LLM are accepted only if they improve the original translation's MTQE score.\n\n**Human Oversight:**\n\nHuman-in-the-loop support ensures the right level of quality is delivered, particularly for content requiring regulatory compliance.\n\nThe search results indicate an active research area combining quality estimation, automatic post-editing, and iterative refinement to optimize machine translation workflows."], "durationSeconds": 7.001289555, "searchCount": 1}
```

### [11] TOOL RESULT — WebSearch · 2026-09-01 09:20:58 UTC

```
{"query": "xTower iterative machine translation error correction explanation feedback loop", "results": [{"tool_use_id": "srvtoolu_017j8WrSaC163SzjNNbkpwnT", "content": [{"title": "xTower: A Multilingual LLM for Explaining and Correcting Translation Errors | Request PDF", "url": "https://www.researchgate.net/publication/386196869_xTower_A_Multilingual_LLM_for_Explaining_and_Correcting_Translation_Errors"}, {"title": "[2406.19482] xTower: A Multilingual LLM for Explaining and Correcting Translation Errors", "url": "https://arxiv.org/abs/2406.19482"}, {"title": "Enhancing Machine Translation with Self-Supervised ...", "url": "https://aclanthology.org/2025.acl-long.1165.pdf"}, {"title": "xTower: A Multilingual LLM for Explaining and Correcting Translation Errors", "url": "https://arxiv.org/pdf/2406.19482"}, {"title": "[Literature Review] xTower: A Multilingual LLM for Explaining and Correcting Translation Errors", "url": "https://www.themoonlight.io/en/review/xtower-a-multilingual-llm-for-explaining-and-correcting-translation-errors"}, {"title": "xTower: A Multilingual LLM for Explaining and Correcting Translation Errors - ACL Anthology", "url": "https://aclanthology.org/2024.findings-emnlp.892/"}, {"title": "Unbabel’s New xTOWER LLM Explains Translation Errors and Suggests How to Fix Them - Slator", "url": "https://slator.com/unbabels-new-xtower-llm-explains-translation-errors-and-suggests-how-to-fix-them/"}, {"title": "Quality-Informed Segment-Level Error Correction Using ...", "url": "https://aclanthology.org/2025.wmt-1.75.pdf"}, {"title": "(PDF) xTower: A Multilingual LLM for Explaining and Correcting Translation Errors", "url": "https://www.researchgate.net/publication/381851169_xTower_A_Multilingual_LLM_for_Explaining_and_Correcting_Translation_Errors"}]}, "Based on the search results, here's an explanation of xTower's iterative machine translation error correction approach with feedback loops:\n\n## Overview\n\nxTower is an open large language model (LLM) built on top of TowerBase designed to provide free-text explanations for translation errors in order to guide the generation of a corrected translation.\n\n## Error Correction Process\n\nThe system operates through a structured feedback loop mechanism:\n\nThe process involves inputting a source text and its translation into xCOMET, which annotates the translation with error spans and assigns a quality score. The marked translation, quality score, and annotated errors are passed to xTower, which produces an explanation for each error span along with a final suggestion for a new, corrected translation.\n\n## Two-Stage Refinement Framework\n\nThe framework uses a two-stage refinement approach: the first stage focuses on correcting major translation errors through implicit refinement that exploits retrieved parallel examples together with auxiliary knowledge guidance. The second stage introduces quality-oriented feedback to identify and revise the remaining errors iteratively.\n\n## Feedback Loop Strategy\n\nThis hybrid approach mirrors a machine translation post-editing workflow, where post-editing is performed only when a quality estimation model confirms that the translation needs improvement. This approach can significantly improve translation performance and reduce inference costs by only querying xTower when necessary."], "durationSeconds": 6.752042352999999, "searchCount": 1}
```

### [12] TOOL RESULT — WebSearch · 2026-09-01 09:20:58 UTC

```
{"query": "\"verify-and-repair\" OR \"iterative repair\" machine translation span editing localization ablation", "results": [{"tool_use_id": "srvtoolu_01XCZp4ZV3hN3PkkTtVBtuto", "content": [{"title": "CURE: Code-Aware Neural Machine Translation for Automatic Program Repair | Request PDF", "url": "https://www.researchgate.net/publication/351420923_CURE_Code-Aware_Neural_Machine_Translation_for_Automatic_Program_Repair"}, {"title": "LaSEr-Edit: Localized Span-level Error Editing with Energy-based Localization", "url": "https://arxiv.org/html/2407.00740v2"}, {"title": "The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models", "url": "https://arxiv.org/html/2505.02931v1"}, {"title": "Parallel Iterative Edit Models for Local Sequence Transduction", "url": "https://arxiv.org/pdf/1910.02893"}, {"title": "Should We be Pedantic About Reasoning Errors in Machine Translation?", "url": "https://arxiv.org/pdf/2604.09890"}, {"title": "Assessing the Latent Automated Program Repair Capabilities of Large Language Models using Round-Trip Translation", "url": "https://arxiv.org/html/2401.07994v2"}, {"title": "An Empirical Study of Automatic Post-Editing", "url": "https://arxiv.org/pdf/2209.07759"}, {"title": "HELO-APR: Enhancing Low-Resource Program Repair through Cross-Lingual Knowledge Transfer", "url": "https://arxiv.org/pdf/2604.17016"}, {"title": "[2505.02931] The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models", "url": "https://ar5iv.labs.arxiv.org/html/2505.02931"}]}, "Based on the search results, here's what I found relevant to your query about machine translation and repair-related techniques:\n\n## Key Findings\n\n**Span-Level Error Editing**: Similar to automatic post-editing in machine translation, which corrects initial translations to remove translation errors, constraint enforcement can be treated as a revision problem given an initially generated text to correct constraint violations. Recent studies in automatic post-editing show that span-level error information can improve LLM-based post-editing.\n\n**Iterative Refinement**: Iterative refinements on accuracy show that out of 1312 test sentences, 832 changed in the first round and 156 in the second round, with an average of 2.7 refinement rounds per example.\n\n**Machine Translation Background**: Recent LLM-based approaches to code repair include Neural Machine Translation (NMT), cloze-style repair, instruction and chat-based methods, and frameworks with iterative LLM calls.\n\n**Ablation Studies**: The search results include references to ablation studies examining components like verification processes and architectural features in repair systems.\n\nThe results primarily cover automatic post-editing (APE) in machine translation and iterative repair techniques, though they don't specifically retrieve a paper with \"verify-and-repair\" in the title. Would you like me to search for more specific information about any of these topics?"], "durationSeconds": 8.300110835, "searchCount": 1}
```

### [13] TOOL CALL — WebSearch · 2026-09-01 09:21:04 UTC

```
"Enhancing Machine Translation with Self-Supervised" ACL 2025 two-stage refinement iterative feedback
```

### [14] TOOL CALL — WebSearch · 2026-09-01 09:21:04 UTC

```
"Quality-Informed Segment-Level Error Correction" WMT 2025 findings
```

### [15] TOOL CALL — WebSearch · 2026-09-01 09:21:04 UTC

```
Self-Refine machine translation multiple rounds feedback ablation localization breadth iteration factorial
```

### [16] TOOL RESULT — WebSearch · 2026-09-01 09:21:10 UTC

```
{"query": "\"Enhancing Machine Translation with Self-Supervised\" ACL 2025 two-stage refinement iterative feedback", "results": [{"tool_use_id": "srvtoolu_018kxCzQhScTJAGb3JGmzPCE", "content": [{"title": "TEaR: Improving LLM-based Machine Translation with Systematic Self-Refinement - ACL Anthology", "url": "https://aclanthology.org/2025.findings-naacl.218/"}, {"title": "Enhancing Machine Translation with Self-Supervised ...", "url": "https://aclanthology.org/2025.acl-long.1165.pdf"}, {"title": "Enhancing Machine Translation with Self-Supervised Preference Data - ACL Anthology", "url": "https://aclanthology.org/2025.acl-long.1165/"}, {"title": "CHILL at SemEval-2025 Task 2: You Can't Just Throw Entities and Hope -- Make Your LLM to Get Them Right", "url": "https://arxiv.org/pdf/2506.13070"}, {"title": "Machine Translation Summit (2025) - ACL Anthology", "url": "https://aclanthology.org/events/mtsummit-2025/"}, {"title": "Improving Machine Translation with Human Feedback: An Exploration of Quality Estimation as a Reward Model", "url": "https://arxiv.org/pdf/2401.12873"}, {"title": "CHORUS: Effort-Aware Multi-Agent Human-AI Collaboration for Professional Translation", "url": "https://arxiv.org/pdf/2602.19016"}]}, "I found the paper you're looking for! Based on the search results, here's what I found:\n\nThe paper proposes Self-Supervised Preference Optimization (SSPO), a novel framework which efficiently constructs translation preference data for iterative DPO training.\n\nThe process starts by training Model0 with three types of data: parallel translation pairs, augmented MQM (Multidimensional Quality Metrics) annotations with error explanation and suggested correction, and error correction samples leveraging MQM annotations for corrected translations. The framework then iteratively improves through two paths: (1) SFT with self-generated MQM annotations and corrections to get stronger Error detector ModelE (2) DPO with <initial translation, corrected translation> preference pairs to get stronger Translator ModelT.\n\nApplying SSPO to 14B parameters large language models (LLMs) achieves comparable or better performance than GPT-4o on FLORES and multi-domain test datasets.\n\nThe paper is titled **\"Enhancing Machine Translation with Self-Supervised Preference Data\"** by Haoxiang Sun, Ruize Gao, Pei Zhang, Baosong Yang, and Rui Wang, and was presented at the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in Vienna, Austria."], "durationSeconds": 7.286279893999995, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-09-01 09:21:12 UTC

```
{"query": "Self-Refine machine translation multiple rounds feedback ablation localization breadth iteration factorial", "results": [{"tool_use_id": "srvtoolu_01TsZTmruqEEqqdk1D75F4En", "content": [{"title": "MAGA-Bench: Machine-Augment-Generated Text via Alignment Detection Benchmark", "url": "https://arxiv.org/pdf/2601.04633"}, {"title": "Iterative Translation Refinement with Large Language Models - ACL Anthology", "url": "https://aclanthology.org/2024.eamt-1.17/"}, {"title": "Improving LLM-based Machine Translation with Systematic Self-Correction", "url": "https://arxiv.org/html/2402.16379v2"}, {"title": "Self-Chained Image-Language Model for Video Localization and Question Answering", "url": "https://arxiv.org/pdf/2305.06988"}, {"title": "Machine translation output reranking", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10067936"}, {"title": "Structure Enables Effective Self-Localization of Errors in LLMs", "url": "https://arxiv.org/pdf/2602.02416"}, {"title": "[2402.16379] TEaR: Improving LLM-based Machine Translation with Systematic Self-Refinement", "url": "https://arxiv.org/abs/2402.16379"}, {"title": "CHORUS: Effort-Aware Multi-Agent Human-AI Collaboration for Professional Translation", "url": "https://arxiv.org/pdf/2602.19016"}, {"title": "A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?", "url": "https://arxiv.org/pdf/2503.24235"}]}, "Based on the search results, here's what I found about Self-Refine and machine translation with multiple rounds of feedback:\n\n## Self-Refine Framework Overview\n\nSelf-Refine is an advanced technique that enables an LLM to iteratively improve its own outputs through self-generated feedback, inspired by how humans revise a draft: The model first produces an initial answer, then critiques or evaluates that answer, and finally uses the critique to refine the answer. This feedback-refinement loop can be repeated multiple times, progressively polishing the output.\n\n## Multiple Rounds & Ablation Studies\n\nInterestingly, research on multiple iteration rounds shows limited benefits:\n\n- Multiple iterations yield marginal performance variance, characterized primarily by fluctuations.\n\n- Exploring whether continuously iterating the self-correcting process could enhance performance found that this might lead to a decrease in performance, with a single round of self-correcting yielding the best results.\n\n- Multi-turn querying reduces the output's string-based metric scores, but neural metrics suggest comparable or improved quality after two or more iterations.\n\n- Two iterations of self-refinement slightly increase performance compared to single self-refinement, but the performance saturates from three iterations.\n\n## Importance of Anchoring\n\nAblation studies underscore the importance of anchoring the refinement to the source and a reasonable seed translation for quality considerations.\n\nThe research suggests that while self-refinement can improve machine translation quality, there are diminishing returns with multiple rounds, and careful experimental design is needed to evaluate the actual benefits."], "durationSeconds": 7.407829524999998, "searchCount": 1}
```

### [18] TOOL RESULT — WebSearch · 2026-09-01 09:21:12 UTC

```
{"query": "\"Quality-Informed Segment-Level Error Correction\" WMT 2025 findings", "results": [{"tool_use_id": "srvtoolu_01Htm3d2Zqh9Psm9JEMk9oDJ", "content": [{"title": "WMT 2025 Shared Task on Automated Translation Quality Evaluation: Now Open for Participation!", "url": "https://groups.google.com/g/wmt-tasks/c/rhTEupvaksQ"}, {"title": "WMT 2025 Shared Task on Automated Translation Quality Evaluation Systems: Preliminary Announcement and Call for Participation", "url": "https://groups.google.com/g/wmt-tasks/c/CMoDKYTM7ow"}, {"title": "Quality-Informed Segment-Level Error Correction Using ...", "url": "https://aclanthology.org/2025.wmt-1.75.pdf"}, {"title": "Submission for WMT25 Task 3 - ACL Anthology", "url": "https://aclanthology.org/2025.wmt-1.73/"}, {"title": "Findings of the WMT25 Shared Task on Automated ...", "url": "https://aclanthology.org/2025.wmt-1.24.pdf"}, {"title": "Can QE-informed (Re)Translation lead to Error Correction?", "url": "https://aclanthology.org/2025.wmt-1.73.pdf"}, {"title": "WMT25 Automated Translation Quality Evaluation Systems Task 3 - QE-informed Segment-level Error Correction – Codabench", "url": "https://www.codabench.org/competitions/8371/"}, {"title": "Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems: Linguistic Diversity is Challenging and References Still Help - University of Lisbon", "url": "https://researchportal.ulisboa.pt/en/publications/findings-of-the-wmt25-shared-task-on-automated-translation-evalua/"}, {"title": "WMT 2025 Shared Task on Automated Translation Quality Evaluation Systems: Preliminary Announcement and Call for Participation", "url": "https://www.mail-archive.com/mt-list@lists.eamt.org/msg00539.html"}]}, "Based on the search results, here are the key findings regarding Quality-Informed Segment-Level Error Correction at WMT 2025:\n\n## Task Overview\n\nQuality-informed segment-level error correction involves automatically post-editing machine-translated text using quality annotations to generate minimal and accurate corrections. For Task 3, CometKiwi quality annotations were released for the WMT 2023 Metrics and QE test sets along with human reference translations.\n\n## Research Approaches\n\nWhile jointly training QE systems with Automatic Post-Editing (APE) has shown improved performance for both tasks, APE systems are still known to overcorrect the output of Machine Translation (MT), leading to a degradation in performance.\n\nOne winning approach involved innovative strategies: A training-free approach called QE-informed Retranslation was investigated, with the winning approach selecting the highest-quality translation from multiple candidates generated by different LLMs. An alternative approach instructed an LLM to replace error substrings as specified in provided QE explanations, with a conditional heuristic employed to minimize the number of edits and maximize the Gain-to-Edit ratio.\n\n## Task Objectives\n\nThe objective is to explore how quality information (both error annotations and scores) can inform automated error correction, with sentence-level quality scores helping identify which segments require correction, while span-level annotations can be used for fine-grained, pinpointed corrections."], "durationSeconds": 8.189379897999995, "searchCount": 1}
```

### [19] TOOL CALL — Write · 2026-09-01 09:22:08 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "Search for prior work separating MT repair localization from iteration",
  "summary": "Targeted literature search to determine whether any existing work independently varies two mechanisms this project's protocol separates -- how broadly a machine-translation repair localizes errors (one QE-flagged span vs. every detected content-invariant violation) versus whether the repair is iteratively re-verified and re-repaired to a checker-defined certificate vs. applied once -- as two orthogonal, separately-measured factors. The result either backs the paper's 'first controlled evidence separating localization breadth from iteration' claim with a logged, reproducible negative search, or surfaces a closer prior ablation that the current related-work section (Deoghare 2023/2025, xTower, Self-Refine, CEGIS, LaSEr-Edit) does not cover, in which case the paper's novelty claim must be scoped down and the paper cites the closer work explicitly.",
  "runpod_compute_profile": "cpu_light",
  "question": "Does any published system or ablation study hold 'breadth of error localization' (narrow QE-flagged span vs. broadened invariant/error detection) and 'iteration/re-verification of a repair' apart as two independently varied, separately measured factors in machine-translation automatic post-editing / scoped span editing -- the way this project's C1 (broad, single-pass) vs. C2 (narrow, iterated) conditions do -- or does every candidate bundle the two (broaden localization AND iterate together, or vary only one while holding the other fixed at a single, non-varied setting)?",
  "explanation": "The hypothesis's central mechanism claim -- that C2 (narrow localization, iterated repair) and C1 (broad localization, single-pass repair) isolate two genuinely different levers, with C2 shown this iteration to trade quality for correctness and C1 to trade correctness for quality -- is only a *novel* factorial separation if no prior paper already ran this same 2x1 (or 2x2) design in MT automatic post-editing / scoped span editing. The current related-work section (APE-with-QE-signal papers like Deoghare 2023/2025, xTower's explain-then-correct loop, Self-Refine-style iterative MT refinement, Grid Beam Search constrained decoding, and the CEGIS inspiration itself) was assembled without a dedicated adversarial search specifically for this cross of terms. Getting this wrong either lets the paper overclaim novelty it does not have (a reviewer will find the paper the search missed) or leaves the paper under-defending a genuinely clean contribution because the survey looks incomplete. This artifact's sole job is to close that gap with a citable, reproducible search record before the next paper draft is written.",
  "research_plan": "GOAL: Determine, via a specifically-worded and logged literature search (not a repeat of the existing broad MT/APE survey), whether any prior work varies error-localization breadth and repair iteration as two separate, independently measured factors in machine-translation automatic post-editing or scoped span editing. Produce a clear verdict with exact search terms, exact candidates checked, and exact reasons each was ruled in or out.\n\nSTEP 0 -- Reuse-not-repeat check (5 min): Before searching, re-read this project's own related_works list (Padmanabhan 2025, WMT25 findings paper, Deoghare et al. 2023, Deoghare et al. 2025, LaSEr-Edit, roundtrip-verification autoformalization, CEGIS) so the search below is additive, not duplicative. Do not re-search these six directly; instead search terms specifically chosen NOT to be in that list.\n\nSTEP 1 -- Primary targeted searches (general + scholarly mode, run in parallel where independent). Use aii-web-tools search with mode=scholarly for citation-grounded results and mode=general as a complement (Google Scholar / arXiv often index papers general web search misses, and vice versa). Exact query strings to run, verbatim, and log each one in the final report even if it returns nothing useful:\n  1. \"iterative QE-guided post-editing machine translation\" (both modes)\n  2. \"checker-in-the-loop machine translation repair\" (both modes)\n  3. \"verify-and-repair span editing translation\" (both modes)\n  4. \"iterative constrained decoding machine translation error correction\" (both modes)\n  5. \"localization breadth versus iteration machine translation\" (both modes)\n  6. \"error localization scope ablation automatic post-editing\" (general)\n  7. \"single-pass versus iterative automatic post-editing ablation\" (scholarly)\n  8. \"scoped span repair verification loop translation quality estimation\" (general)\n  9. \"self-refine machine translation iteration ablation number of rounds\" (scholarly) -- to check whether any Self-Refine-for-MT ablation varies localization scope alongside iteration count, since round-count ablations are common but scope ablations are not\n  10. \"WMT25 Task 3 error correction system iterative\" and \"WMT25 automatic post-editing shared task ablation localization\" -- to catch any other Task 3 participant paper beyond Padmanabhan (2025) and the findings paper already read\n\nSTEP 2 -- Specific candidates already surfaced by exploratory searches this planning pass, to fetch and check FIRST since they are the closest hits found so far (do not treat these as the final answer -- verify each by fetching, not by title alone):\n  a. Deoghare et al., \"Quality-Informed Segment-Level Error Correction Using...\" (WMT25 Task 3 submission, https://aclanthology.org/2025.wmt-1.75.pdf) -- a third WMT25 Task 3 team's system not yet checked for a localization-breadth-vs-iteration ablation; fetch in full and fetch_grep for 'iterat', 'ablation', 'span', 'localiz' to see if it varies these two factors independently or only reports one fixed pipeline.\n  b. TEaR: \"Improving LLM-based Machine Translation with Systematic Self-Refinement\" (NAACL 2025 Findings, https://aclanthology.org/2025.findings-naacl.218/ and its earlier arXiv 2402.16379 version \"Improving LLM-based Machine Translation with Systematic Self-Correction\") -- has an explicit iteration-round ablation; fetch_grep specifically for whether it also varies what fraction of the sentence / how many error spans are located per pass, or whether localization scope is held fixed while only the iteration count varies (if fixed, it does NOT separate the two factors and should be cited as a single-factor iteration study, distinct from this protocol).\n  c. \"Enhancing Machine Translation with Self-Supervised Preference Data\" (SSPO, ACL 2025, https://aclanthology.org/2025.acl-long.1165/) -- trains an iterative error-detector/translator loop; check whether its error-detection stage's scope (span-level vs whole-sentence) is ever varied independently of how many DPO/refinement iterations are run, or whether detection scope and iteration count are coupled by construction.\n  d. \"Structure Enables Effective Self-Localization of Errors in LLMs\" (arXiv 2602.02416) -- check relevance despite not being MT-specific; if it is a general LLM self-correction paper, note explicitly why it is out of scope (no MT translation-quality evaluation) rather than silently dropping it.\n  e. xTower's two-stage refinement description surfaced in this planning pass (\"first stage corrects major errors via implicit refinement... second stage introduces quality-oriented feedback to identify and revise remaining errors iteratively\") sounds closer to a breadth-then-iteration DESIGN than the existing related-work entry credits -- re-fetch the xTower paper (arXiv 2406.19482 / ACL Findings EMNLP 2024) specifically for whether stage 1 vs stage 2 differ in localization scope (implicit/major-error correction vs targeted quality-feedback revision) and whether these two stages are ever run as an ISOLATED ablation (stage 2 alone vs stage 1 alone vs both) with breadth and iteration count reported as separate independent variables, or whether they are always run in sequence as one fixed pipeline (which would NOT count as separating the factors, only as motivating the idea that they might be separable).\n\nSTEP 3 -- For every candidate surfaced in Steps 1-2 that survives a title/abstract screen, fetch the full paper (or fetch_grep the PDF for 'ablat', 'iterat', 'localiz', 'scope', 'span', 'factorial', 'independent' if it is long) and apply this exact decision rule, recorded per-paper in the output:\n  - CLASSIFY AS 'separates the factors' only if the paper reports at least two conditions that hold localization scope fixed while varying iteration (or vice versa), with both varied independently at least once each -- i.e., a design with >=3 of the 4 cells {narrow+single, narrow+iterated, broad+single, broad+iterated}, or an explicit statement that iteration count and localization scope were varied as separate ablation axes.\n  - CLASSIFY AS 'bundles the factors' if the paper's iteration mechanism inherently re-scopes what it looks at on each pass (e.g., re-running the same detector see more errors each round because errors moved), making breadth and iteration count causally entangled by the method's own design rather than experimentally separated.\n  - CLASSIFY AS 'varies only one factor' if the paper ablates iteration count (holding localization/detection scope fixed at one setting) or ablates detection breadth (running a single pass only), but never both together.\n  - CLASSIFY AS 'out of scope' if it is not machine translation, not automatic post-editing / scoped span repair, or not an empirical ablation (e.g., a survey, a position paper, or a system description with no ablation table).\n\nSTEP 4 -- Verdict and write-up. Produce research_out.json {answer, sources, follow_up_questions} plus research_report.md structured as:\n  1. Exact list of search queries run (Step 1's 10 strings, both modes noted), one line each, with a one-line note on hit quality -- so the paper can cite its own search scope verbatim rather than asserting novelty unconditionally.\n  2. A table of every candidate fetched (Steps 1-2), each with: title, venue/year, URL, one-sentence mechanism description, and its Step-3 classification with the specific quoted or paraphrased evidence (e.g., an exact ablation-table description or a quoted sentence) that justifies the classification -- not just the label.\n  3. THE VERDICT, stated in one unambiguous sentence: either (a) 'No candidate found across N queries and M fetched papers holds localization breadth and iteration apart as independently varied factors in MT post-editing/scoped editing; the closest are [list, with why each still falls short]' -- supporting the paper's current strong claim -- or (b) 'Paper X (full citation) separates these factors via [exact mechanism]; it differs from this protocol's C1/C2/C design in [specific ways: language pairs, checker type, whether it reports true regression rate, whether it uses a matched repair model, whether the localization axis is content-invariants specifically vs generic QE spans, etc.]' -- in which case state precisely how the paper's novelty claim should be rescoped for the next draft (e.g., from 'first to separate these mechanisms' to 'first to separate these mechanisms specifically for content-invariant checkers with a matched-repair-model design and a true-regression-rate metric').\n  4. Do not fabricate a verdict either way. If a search returns ambiguous or paywalled results that could not be resolved by fetch/fetch_grep within the time available, say so explicitly and list those as open items in follow_up_questions rather than guessing their classification.\n\nBUDGET: Stay near $0 -- this is pure web search/fetch, no OpenRouter LLM calls are required for the search itself (only use OpenRouter, if at all, for a final synthesis pass well under $1). Time budget: roughly 45 min for Steps 1-2 searches/fetches, 45 min for Step 3 classification, 30 min for the Step 4 write-up, leaving slack inside the 3h ceiling for follow-up fetches on ambiguous candidates.",
  "compute_profile_note": "cpu_light is sufficient; this artifact performs no local computation, only web search/fetch and report writing."
}
```

### [20] TOOL RESULT — Write · 2026-09-01 09:22:08 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Search for prior work separating MT repair localization from iteration\",\n  \"summary\": \"Targeted literature search to determine whether any existing work independently varies two mechanisms this project's protocol separates -- how broadly a machine-translation repair localizes errors (one QE-flagged span vs. every detected content-invariant violation) versus whether the repair is iteratively re-verified and re-repaired to a checker-defined certificate vs. applied once -- as two orthogonal, separately-measured factors. The result either backs the paper's 'first controlled evidence separating localization breadth from iteration' claim with a logged, reproducible negative search, or surfaces a closer prior ablation that the current related-work section (Deoghare 2023/2025, xTower, Self-Refine, CEGIS, LaSEr-Edit) does not cover, in which case the paper's novelty claim must be scoped down and the paper cites the closer work explicitly.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"Does any published system or ablation study hold 'breadth of error localization' (narrow QE-flagged span vs. broadened invariant/error detection) and 'iteration/re-verification of a repair' apart as two independently varied, separately measured factors in machine-translation automatic post-editing / scoped span editing -- the way this project's C1 (broad, single-pass) vs. C2 (narrow, iterated) conditions do -- or does every candidate bundle the two (broaden localization AND iterate together, or vary only one while holding the other fixed at a single, non-varied setting)?\",\n  \"explanation\": \"The hypothesis's central mechanism claim -- that C2 (narrow localization, iterated repair) and C1 (broad localization, single-pass repair) isolate two genuinely different levers, with C2 shown this iteration to trade quality for correctness and C1 to trade correctness for quality -- is only a *novel* factorial separation if no prior paper already ran this same 2x1 (or 2x2) design in MT automatic post-editing / scoped span editing. The current related-work section (APE-with-QE-signal papers like Deoghare 2023/2025, xTower's explain-then-correct loop, Self-Refine-style iterative MT refinement, Grid Beam Search constrained decoding, and the CEGIS inspiration itself) was assembled without a dedicated adversarial search specifically for this cross of terms. Getting this wrong either lets the paper overclaim novelty it does not have (a reviewer will find the paper the search missed) or leaves the paper under-defending a genuinely clean contribution because the survey looks incomplete. This artifact's sole job is to close that gap with a citable, reproducible search record before the next paper draft is written.\",\n  \"research_plan\": \"GOAL: Determine, via a specifically-worded and logged literature search (not a repeat of the existing broad MT/APE survey), whether any prior work varies error-localization breadth and repair iteration as two separate, independently measured factors in machine-translation automatic post-editing or scoped span editing. Produce a clear verdict with exact search terms, exact candidates checked, and exact reasons each was ruled in or out.\\n\\nSTEP 0 -- Reuse-not-repeat check (5 min): Before searching, re-read this project's own related_works list (Padmanabhan 2025, WMT25 findings paper, Deoghare et al. 2023, Deoghare et al. 2025, LaSEr-Edit, roundtrip-verification autoformalization, CEGIS) so the search below is additive, not duplicative. Do not re-search these six directly; instead search terms specifically chosen NOT to be in that list.\\n\\nSTEP 1 -- Primary targeted searches (general + scholarly mode, run in parallel where independent). Use aii-web-tools search with mode=scholarly for citation-grounded results and mode=general as a complement (Google Scholar / arXiv often index papers general web search misses, and vice versa). Exact query strings to run, verbatim, and log each one in the final report even if it returns nothing useful:\\n  1. \\\"iterative QE-guided post-editing machine translation\\\" (both modes)\\n  2. \\\"checker-in-the-loop machine translation repair\\\" (both modes)\\n  3. \\\"verify-and-repair span editing translation\\\" (both modes)\\n  4. \\\"iterative constrained decoding machine translation error correction\\\" (both modes)\\n  5. \\\"localization breadth versus iteration machine translation\\\" (both modes)\\n  6. \\\"error localization scope ablation automatic post-editing\\\" (general)\\n  7. \\\"single-pass versus iterative automatic post-editing ablation\\\" (scholarly)\\n  8. \\\"scoped span repair verification loop translation quality estimation\\\" (general)\\n  9. \\\"self-refine machine translation iteration ablation number of rounds\\\" (scholarly) -- to check whether any Self-Refine-for-MT ablation varies localization scope alongside iteration count, since round-count ablations are common but scope ablations are not\\n  10. \\\"WMT25 Task 3 error correction system iterative\\\" and \\\"WMT25 automatic post-editing shared task ablation localization\\\" -- to catch any other Task 3 participant paper beyond Padmanabhan (2025) and the findings paper already read\\n\\nSTEP 2 -- Specific candidates already surfaced by exploratory searches this planning pass, to fetch and check FIRST since they are the closest hits found so far (do not treat these as the final answer -- verify each by fetching, not by title alone):\\n  a. Deoghare et al., \\\"Quality-Informed Segment-Level Error Correction Using...\\\" (WMT25 Task 3 submission, https://aclanthology.org/2025.wmt-1.75.pdf) -- a third WMT25 Task 3 team's system not yet checked for a localization-breadth-vs-iteration ablation; fetch in full and fetch_grep for 'iterat', 'ablation', 'span', 'localiz' to see if it varies these two factors independently or only reports one fixed pipeline.\\n  b. TEaR: \\\"Improving LLM-based Machine Translation with Systematic Self-Refinement\\\" (NAACL 2025 Findings, https://aclanthology.org/2025.findings-naacl.218/ and its earlier arXiv 2402.16379 version \\\"Improving LLM-based Machine Translation with Systematic Self-Correction\\\") -- has an explicit iteration-round ablation; fetch_grep specifically for whether it also varies what fraction of the sentence / how many error spans are located per pass, or whether localization scope is held fixed while only the iteration count varies (if fixed, it does NOT separate the two factors and should be cited as a single-factor iteration study, distinct from this protocol).\\n  c. \\\"Enhancing Machine Translation with Self-Supervised Preference Data\\\" (SSPO, ACL 2025, https://aclanthology.org/2025.acl-long.1165/) -- trains an iterative error-detector/translator loop; check whether its error-detection stage's scope (span-level vs whole-sentence) is ever varied independently of how many DPO/refinement iterations are run, or whether detection scope and iteration count are coupled by construction.\\n  d. \\\"Structure Enables Effective Self-Localization of Errors in LLMs\\\" (arXiv 2602.02416) -- check relevance despite not being MT-specific; if it is a general LLM self-correction paper, note explicitly why it is out of scope (no MT translation-quality evaluation) rather than silently dropping it.\\n  e. xTower's two-stage refinement description surfaced in this planning pass (\\\"first stage corrects major errors via implicit refinement... second stage introduces quality-oriented feedback to identify and revise remaining errors iteratively\\\") sounds closer to a breadth-then-iteration DESIGN than the existing related-work entry credits -- re-fetch the xTower paper (arXiv 2406.19482 / ACL Findings EMNLP 2024) specifically for whether stage 1 vs stage 2 differ in localization scope (implicit/major-error correction vs targeted quality-feedback revision) and whether these two stages are ever run as an ISOLATED ablation (stage 2 alone vs stage 1 alone vs both) with breadth and iteration count reported as separate independent variables, or whether they are always run in sequence as one fixed pipeline (which would NOT count as separating the factors, only as motivating the idea that they might be separable).\\n\\nSTEP 3 -- For every candidate surfaced in Steps 1-2 that survives a title/abstract screen, fetch the full paper (or fetch_grep the PDF for 'ablat', 'iterat', 'localiz', 'scope', 'span', 'factorial', 'independent' if it is long) and apply this exact decision rule, recorded per-paper in the output:\\n  - CLASSIFY AS 'separates the factors' only if the paper reports at least two conditions that hold localization scope fixed while varying iteration (or vice versa), with both varied independently at least once each -- i.e., a design with >=3 of the 4 cells {narrow+single, narrow+iterated, broad+single, broad+iterated}, or an explicit statement that iteration count and localization scope were varied as separate ablation axes.\\n  - CLASSIFY AS 'bundles the factors' if the paper's iteration mechanism inherently re-scopes what it looks at on each pass (e.g., re-running the same detector see more errors each round because errors moved), making breadth and iteration count causally entangled by the method's own design rather than experimentally separated.\\n  - CLASSIFY AS 'varies only one factor' if the paper ablates iteration count (holding localization/detection scope fixed at one setting) or ablates detection breadth (running a single pass only), but never both together.\\n  - CLASSIFY AS 'out of scope' if it is not machine translation, not automatic post-editing / scoped span repair, or not an empirical ablation (e.g., a survey, a position paper, or a system description with no ablation table).\\n\\nSTEP 4 -- Verdict and write-up. Produce research_out.json {answer, sources, follow_up_questions} plus research_report.md structured as:\\n  1. Exact list of search queries run (Step 1's 10 strings, both modes noted), one line each, with a one-line note on hit quality -- so the paper can cite its own search scope verbatim rather than asserting novelty unconditionally.\\n  2. A table of every candidate fetched (Steps 1-2), each with: title, venue/year, URL, one-sentence mechanism description, and its Step-3 classification with the specific quoted or paraphrased evidence (e.g., an exact ablation-table description or a quoted sentence) that justifies the classification -- not just the label.\\n  3. THE VERDICT, stated in one unambiguous sentence: either (a) 'No candidate found across N queries and M fetched papers holds localization breadth and iteration apart as independently varied factors in MT post-editing/scoped editing; the closest are [list, with why each still falls short]' -- supporting the paper's current strong claim -- or (b) 'Paper X (full citation) separates these factors via [exact mechanism]; it differs from this protocol's C1/C2/C design in [specific ways: language pairs, checker type, whether it reports true regression rate, whether it uses a matched repair model, whether the localization axis is content-invariants specifically vs generic QE spans, etc.]' -- in which case state precisely how the paper's novelty claim should be rescoped for the next draft (e.g., from 'first to separate these mechanisms' to 'first to separate these mechanisms specifically for content-invariant checkers with a matched-repair-model design and a true-regression-rate metric').\\n  4. Do not fabricate a verdict either way. If a search returns ambiguous or paywalled results that could not be resolved by fetch/fetch_grep within the time available, say so explicitly and list those as open items in follow_up_questions rather than guessing their classification.\\n\\nBUDGET: Stay near $0 -- this is pure web search/fetch, no OpenRouter LLM calls are required for the search itself (only use OpenRouter, if at all, for a final synthesis pass well under $1). Time budget: roughly 45 min for Steps 1-2 searches/fetches, 45 min for Step 3 classification, 30 min for the Step 4 write-up, leaving slack inside the 3h ceiling for follow-up fetches on ambiguous candidates.\",\n  \"compute_profile_note\": \"cpu_light is sufficient; this artifact performs no local computation, only web search/fetch and report writing.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [21] TOOL CALL — Read · 2026-09-01 09:22:12 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json
```

### [22] TOOL RESULT — Read · 2026-09-01 09:22:12 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{", "numLines": 1, "startLine": 1, "totalLines": 10}}
```

### [23] TOOL CALL — Edit · 2026-09-01 09:22:14 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json
OLD: ,
  "compute_profile_note": "cpu_light is sufficient; this artifact performs no local computation, only web search/fetch and report writing."
}
NEW: 
}
```

### [24] TOOL RESULT — Edit · 2026-09-01 09:22:14 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "oldString": ",\n  \"compute_profile_note\": \"cpu_light is sufficient; this artifact performs no local computation, only web search/fetch and report writing.\"\n}", "newString": "\n}", "originalFile": null, "structuredPatch": [{"oldStart": 4, "oldLines": 6, "newStart": 4, "newLines": 5, "lines": ["   \"runpod_compute_profile\": \"cpu_light\",", "   \"question\": \"Does any published system or ablation study hold 'breadth of error localization' (narrow QE-flagged span vs. broadened invariant/error detection) and 'iteration/re-verification of a repair' apart as two independently varied, separately measured factors in machine-translation automatic post-editing / scoped span editing -- the way this project's C1 (broad, single-pass) vs. C2 (narrow, iterated) conditions do -- or does every candidate bundle the two (broaden localization AND iterate together, or vary only one while holding the other fixed at a single, non-varied setting)?\",", "   \"explanation\": \"The hypothesis's central mechanism claim -- that C2 (narrow localization, iterated repair) and C1 (broad localization, single-pass repair) isolate two genuinely different levers, with C2 shown this iteration to trade quality for correctness and C1 to trade correctness for quality -- is only a *novel* factorial separation if no prior paper already ran this same 2x1 (or 2x2) design in MT automatic post-editing / scoped span editing. The current related-work section (APE-with-QE-signal papers like Deoghare 2023/2025, xTower's explain-then-correct loop, Self-Refine-style iterative MT refinement, Grid Beam Search constrained decoding, and the CEGIS inspiration itself) was assembled without a dedicated adversarial search specifically for this cross of terms. Getting this wrong either lets the paper overclaim novelty it does not have (a reviewer will find the paper the search missed) or leaves the paper under-defending a genuinely clean contribution because the survey looks incomplete. This artifact's sole job is to close that gap with a citable, reproducible search record before the next paper draft is written.\",", "-  \"research_plan\": \"GOAL: Determine, via a specifically-worded and logged literature search (not a repeat of the existing broad MT/APE survey), whether any prior work varies error-localization breadth and repair iteration as two separate, independently measured factors in machine-translation automatic post-editing or scoped span editing. Produce a clear verdict with exact search terms, exact candidates checked, and exact reasons each was ruled in or out.\\n\\nSTEP 0 -- Reuse-not-repeat check (5 min): Before searching, re-read this project's own related_works list (Padmanabhan 2025, WMT25 findings paper, Deoghare et al. 2023, Deoghare et al. 2025, LaSEr-Edit, roundtrip-verification autoformalization, CEGIS) so the search below is additive, not duplicative. Do not re-search these six directly; instead search terms specifically chosen NOT to be in that list.\\n\\nSTEP 1 -- Primary targeted searches (general + scholarly mode, run in parallel where independent). Use aii-web-tools search with mode=scholarly for citation-grounded results and mode=general as a complement (Google Scholar / arXiv often index papers general web search misses, and vice versa). Exact query strings to run, verbatim, and log each one in the final report even if it returns nothing useful:\\n  1. \\\"iterative QE-guided post-editing machine translation\\\" (both modes)\\n  2. \\\"checker-in-the-loop machine translation repair\\\" (both modes)\\n  3. \\\"verify-and-repair span editing translation\\\" (both modes)\\n  4. \\\"iterative constrained decoding machine translation error correction\\\" (both modes)\\n  5. \\\"localization breadth versus iteration machine translation\\\" (both modes)\\n  6. \\\"error localization scope ablation automatic post-editing\\\" (general)\\n  7. \\\"single-pass versus iterative automatic post-editing ablation\\\" (scholarly)\\n  8. \\\"scoped span repair verification loop translation quality estimation\\\" (general)\\n  9. \\\"self-refine machine translation iteration ablation number of rounds\\\" (scholarly) -- to check whether any Self-Refine-for-MT ablation varies localization scope alongside iteration count, since round-count ablations are common but scope ablations are not\\n  10. \\\"WMT25 Task 3 error correction system iterative\\\" and \\\"WMT25 automatic post-editing shared task ablation localization\\\" -- to catch any other Task 3 participant paper beyond Padmanabhan (2025) and the findings paper already read\\n\\nSTEP 2 -- Specific candidates already surfaced by exploratory searches this planning pass, to fetch and check FIRST since they are the closest hits found so far (do not treat these as the final answer -- verify each by fetching, not by title alone):\\n  a. Deoghare et al., \\\"Quality-Informed Segment-Level Error Correction Using...\\\" (WMT25 Task 3 submission, https://aclanthology.org/2025.wmt-1.75.pdf) -- a third WMT25 Task 3 team's system not yet checked for a localization-breadth-vs-iteration ablation; fetch in full and fetch_grep for 'iterat', 'ablation', 'span', 'localiz' to see if it varies these two factors independently or only reports one fixed pipeline.\\n  b. TEaR: \\\"Improving LLM-based Machine Translation with Systematic Self-Refinement\\\" (NAACL 2025 Findings, https://aclanthology.org/2025.findings-naacl.218/ and its earlier arXiv 2402.16379 version \\\"Improving LLM-based Machine Translation with Systematic Self-Correction\\\") -- has an explicit iteration-round ablation; fetch_grep specifically for whether it also varies what fraction of the sentence / how many error spans are located per pass, or whether localization scope is held fixed while only the iteration count varies (if fixed, it does NOT separate the two factors and should be cited as a single-factor iteration study, distinct from this protocol).\\n  c. \\\"Enhancing Machine Translation with Self-Supervised Preference Data\\\" (SSPO, ACL 2025, https://aclanthology.org/2025.acl-long.1165/) -- trains an iterative error-detector/translator loop; check whether its error-detection stage's scope (span-level vs whole-sentence) is ever varied independently of how many DPO/refinement iterations are run, or whether detection scope and iteration count are coupled by construction.\\n  d. \\\"Structure Enables Effective Self-Localization of Errors in LLMs\\\" (arXiv 2602.02416) -- check relevance despite not being MT-specific; if it is a general LLM self-correction paper, note explicitly why it is out of scope (no MT translation-quality evaluation) rather than silently dropping it.\\n  e. xTower's two-stage refinement description surfaced in this planning pass (\\\"first stage corrects major errors via implicit refinement... second stage introduces quality-oriented feedback to identify and revise remaining errors iteratively\\\") sounds closer to a breadth-then-iteration DESIGN than the existing related-work entry credits -- re-fetch the xTower paper (arXiv 2406.19482 / ACL Findings EMNLP 2024) specifically for whether stage 1 vs stage 2 differ in localization scope (implicit/major-error correction vs targeted quality-feedback revision) and whether these two stages are ever run as an ISOLATED ablation (stage 2 alone vs stage 1 alone vs both) with breadth and iteration count reported as separate independent variables, or whether they are always run in sequence as one fixed pipeline (which would NOT count as separating the factors, only as motivating the idea that they might be separable).\\n\\nSTEP 3 -- For every candidate surfaced in Steps 1-2 that survives a title/abstract screen, fetch the full paper (or fetch_grep the PDF for 'ablat', 'iterat', 'localiz', 'scope', 'span', 'factorial', 'independent' if it is long) and apply this exact decision rule, recorded per-paper in the output:\\n  - CLASSIFY AS 'separates the factors' only if the paper reports at least two conditions that hold localization scope fixed while varying iteration (or vice versa), with both varied independently at least once each -- i.e., a design with >=3 of the 4 cells {narrow+single, narrow+iterated, broad+single, broad+iterated}, or an explicit statement that iteration count and localization scope were varied as separate ablation axes.\\n  - CLASSIFY AS 'bundles the factors' if the paper's iteration mechanism inherently re-scopes what it looks at on each pass (e.g., re-running the same detector see more errors each round because errors moved), making breadth and iteration count causally entangled by the method's own design rather than experimentally separated.\\n  - CLASSIFY AS 'varies only one factor' if the paper ablates iteration count (holding localization/detection scope fixed at one setting) or ablates detection breadth (running a single pass only), but never both together.\\n  - CLASSIFY AS 'out of scope' if it is not machine translation, not automatic post-editing / scoped span repair, or not an empirical ablation (e.g., a survey, a position paper, or a system description with no ablation table).\\n\\nSTEP 4 -- Verdict and write-up. Produce research_out.json {answer, sources, follow_up_questions} plus research_report.md structured as:\\n  1. Exact list of search queries run (Step 1's 10 strings, both modes noted), one line each, with a one-line note on hit quality -- so the paper can cite its own search scope verbatim rather than asserting novelty unconditionally.\\n  2. A table of every candidate fetched (Steps 1-2), each with: title, venue/year, URL, one-sentence mechanism description, and its Step-3 classification with the specific quoted or paraphrased evidence (e.g., an exact ablation-table description or a quoted sentence) that justifies the classification -- not just the label.\\n  3. THE VERDICT, stated in one unambiguous sentence: either (a) 'No candidate found across N queries and M fetched papers holds localization breadth and iteration apart as independently varied factors in MT post-editing/scoped editing; the closest are [list, with why each still falls short]' -- supporting the paper's current strong claim -- or (b) 'Paper X (full citation) separates these factors via [exact mechanism]; it differs from this protocol's C1/C2/C design in [specific ways: language pairs, checker type, whether it reports true regression rate, whether it uses a matched repair model, whether the localization axis is content-invariants specifically vs generic QE spans, etc.]' -- in which case state precisely how the paper's novelty claim should be rescoped for the next draft (e.g., from 'first to separate these mechanisms' to 'first to separate these mechanisms specifically for content-invariant checkers with a matched-repair-model design and a true-regression-rate metric').\\n  4. Do not fabricate a verdict either way. If a search returns ambiguous or paywalled results that could not be resolved by fetch/fetch_grep within the time available, say so explicitly and list those as open items in follow_up_questions rather than guessing their classification.\\n\\nBUDGET: Stay near $0 -- this is pure web search/fetch, no OpenRouter LLM calls are required for the search itself (only use OpenRouter, if at all, for a final synthesis pass well under $1). Time budget: roughly 45 min for Steps 1-2 searches/fetches, 45 min for Step 3 classification, 30 min for the Step 4 write-up, leaving slack inside the 3h ceiling for follow-up fetches on ambiguous candidates.\",", "-  \"compute_profile_note\": \"cpu_light is sufficient; this artifact performs no local computation, only web search/fetch and report writing.\"", "+  \"research_plan\": \"GOAL: Determine, via a specifically-worded and logged literature search (not a repeat of the existing broad MT/APE survey), whether any prior work varies error-localization breadth and repair iteration as two separate, independently measured factors in machine-translation automatic post-editing or scoped span editing. Produce a clear verdict with exact search terms, exact candidates checked, and exact reasons each was ruled in or out.\\n\\nSTEP 0 -- Reuse-not-repeat check (5 min): Before searching, re-read this project's own related_works list (Padmanabhan 2025, WMT25 findings paper, Deoghare et al. 2023, Deoghare et al. 2025, LaSEr-Edit, roundtrip-verification autoformalization, CEGIS) so the search below is additive, not duplicative. Do not re-search these six directly; instead search terms specifically chosen NOT to be in that list.\\n\\nSTEP 1 -- Primary targeted searches (general + scholarly mode, run in parallel where independent). Use aii-web-tools search with mode=scholarly for citation-grounded results and mode=general as a complement (Google Scholar / arXiv often index papers general web search misses, and vice versa). Exact query strings to run, verbatim, and log each one in the final report even if it returns nothing useful:\\n  1. \\\"iterative QE-guided post-editing machine translation\\\" (both modes)\\n  2. \\\"checker-in-the-loop machine translation repair\\\" (both modes)\\n  3. \\\"verify-and-repair span editing translation\\\" (both modes)\\n  4. \\\"iterative constrained decoding machine translation error correction\\\" (both modes)\\n  5. \\\"localization breadth versus iteration machine translation\\\" (both modes)\\n  6. \\\"error localization scope ablation automatic post-editing\\\" (general)\\n  7. \\\"single-pass versus iterative automatic post-editing ablation\\\" (scholarly)\\n  8. \\\"scoped span repair verification loop translation quality estimation\\\" (general)\\n  9. \\\"self-refine machine translation iteration ablation number of rounds\\\" (scholarly) -- to check whether any Self-Refine-for-MT ablation varies localization scope alongside iteration count, since round-count ablations are common but scope ablations are not\\n  10. \\\"WMT25 Task 3 error correction system iterative\\\" and \\\"WMT25 automatic post-editing shared task ablation localization\\\" -- to catch any other Task 3 participant paper beyond Padmanabhan (2025) and the findings paper already read\\n\\nSTEP 2 -- Specific candidates already surfaced by exploratory searches this planning pass, to fetch and check FIRST since they are the closest hits found so far (do not treat these as the final answer -- verify each by fetching, not by title alone):\\n  a. Deoghare et al., \\\"Quality-Informed Segment-Level Error Correction Using...\\\" (WMT25 Task 3 submission, https://aclanthology.org/2025.wmt-1.75.pdf) -- a third WMT25 Task 3 team's system not yet checked for a localization-breadth-vs-iteration ablation; fetch in full and fetch_grep for 'iterat', 'ablation', 'span', 'localiz' to see if it varies these two factors independently or only reports one fixed pipeline.\\n  b. TEaR: \\\"Improving LLM-based Machine Translation with Systematic Self-Refinement\\\" (NAACL 2025 Findings, https://aclanthology.org/2025.findings-naacl.218/ and its earlier arXiv 2402.16379 version \\\"Improving LLM-based Machine Translation with Systematic Self-Correction\\\") -- has an explicit iteration-round ablation; fetch_grep specifically for whether it also varies what fraction of the sentence / how many error spans are located per pass, or whether localization scope is held fixed while only the iteration count varies (if fixed, it does NOT separate the two factors and should be cited as a single-factor iteration study, distinct from this protocol).\\n  c. \\\"Enhancing Machine Translation with Self-Supervised Preference Data\\\" (SSPO, ACL 2025, https://aclanthology.org/2025.acl-long.1165/) -- trains an iterative error-detector/translator loop; check whether its error-detection stage's scope (span-level vs whole-sentence) is ever varied independently of how many DPO/refinement iterations are run, or whether detection scope and iteration count are coupled by construction.\\n  d. \\\"Structure Enables Effective Self-Localization of Errors in LLMs\\\" (arXiv 2602.02416) -- check relevance despite not being MT-specific; if it is a general LLM self-correction paper, note explicitly why it is out of scope (no MT translation-quality evaluation) rather than silently dropping it.\\n  e. xTower's two-stage refinement description surfaced in this planning pass (\\\"first stage corrects major errors via implicit refinement... second stage introduces quality-oriented feedback to identify and revise remaining errors iteratively\\\") sounds closer to a breadth-then-iteration DESIGN than the existing related-work entry credits -- re-fetch the xTower paper (arXiv 2406.19482 / ACL Findings EMNLP 2024) specifically for whether stage 1 vs stage 2 differ in localization scope (implicit/major-error correction vs targeted quality-feedback revision) and whether these two stages are ever run as an ISOLATED ablation (stage 2 alone vs stage 1 alone vs both) with breadth and iteration count reported as separate independent variables, or whether they are always run in sequence as one fixed pipeline (which would NOT count as separating the factors, only as motivating the idea that they might be separable).\\n\\nSTEP 3 -- For every candidate surfaced in Steps 1-2 that survives a title/abstract screen, fetch the full paper (or fetch_grep the PDF for 'ablat', 'iterat', 'localiz', 'scope', 'span', 'factorial', 'independent' if it is long) and apply this exact decision rule, recorded per-paper in the output:\\n  - CLASSIFY AS 'separates the factors' only if the paper reports at least two conditions that hold localization scope fixed while varying iteration (or vice versa), with both varied independently at least once each -- i.e., a design with >=3 of the 4 cells {narrow+single, narrow+iterated, broad+single, broad+iterated}, or an explicit statement that iteration count and localization scope were varied as separate ablation axes.\\n  - CLASSIFY AS 'bundles the factors' if the paper's iteration mechanism inherently re-scopes what it looks at on each pass (e.g., re-running the same detector see more errors each round because errors moved), making breadth and iteration count causally entangled by the method's own design rather than experimentally separated.\\n  - CLASSIFY AS 'varies only one factor' if the paper ablates iteration count (holding localization/detection scope fixed at one setting) or ablates detection breadth (running a single pass only), but never both together.\\n  - CLASSIFY AS 'out of scope' if it is not machine translation, not automatic post-editing / scoped span repair, or not an empirical ablation (e.g., a survey, a position paper, or a system description with no ablation table).\\n\\nSTEP 4 -- Verdict and write-up. Produce research_out.json {answer, sources, follow_up_questions} plus research_report.md structured as:\\n  1. Exact list of search queries run (Step 1's 10 strings, both modes noted), one line each, with a one-line note on hit quality -- so the paper can cite its own search scope verbatim rather than asserting novelty unconditionally.\\n  2. A table of every candidate fetched (Steps 1-2), each with: title, venue/year, URL, one-sentence mechanism description, and its Step-3 classification with the specific quoted or paraphrased evidence (e.g., an exact ablation-table description or a quoted sentence) that justifies the classification -- not just the label.\\n  3. THE VERDICT, stated in one unambiguous sentence: either (a) 'No candidate found across N queries and M fetched papers holds localization breadth and iteration apart as independently varied factors in MT post-editing/scoped editing; the closest are [list, with why each still falls short]' -- supporting the paper's current strong claim -- or (b) 'Paper X (full citation) separates these factors via [exact mechanism]; it differs from this protocol's C1/C2/C design in [specific ways: language pairs, checker type, whether it reports true regression rate, whether it uses a matched repair model, whether the localization axis is content-invariants specifically vs generic QE spans, etc.]' -- in which case state precisely how the paper's novelty claim should be rescoped for the next draft (e.g., from 'first to separate these mechanisms' to 'first to separate these mechanisms specifically for content-invariant checkers with a matched-repair-model design and a true-regression-rate metric').\\n  4. Do not fabricate a verdict either way. If a search returns ambiguous or paywalled results that could not be resolved by fetch/fetch_grep within the time available, say so explicitly and list those as open items in follow_up_questions rather than guessing their classification.\\n\\nBUDGET: Stay near $0 -- this is pure web search/fetch, no OpenRouter LLM calls are required for the search itself (only use OpenRouter, if at all, for a final synthesis pass well under $1). Time budget: roughly 45 min for Steps 1-2 searches/fetches, 45 min for Step 3 classification, 30 min for the Step 4 write-up, leaving slack inside the 3h ceiling for follow-up fetches on ambiguous candidates.\"", " }"]}], "userModified": false, "replaceAll": false}
```

### [25] ASSISTANT · 2026-09-01 09:22:17 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json`. It gives the executor 10 exact search-query strings across general/scholarly modes plus 5 specific candidate papers already surfaced during planning (a third WMT25 Task 3 team's submission, TEaR, SSPO, a self-localization paper, and a closer re-read of xTower's two-stage design) with a precise 4-way classification rule for whether each separates localization breadth from iteration, and a required verdict format (clean negative-search support, or a specific closer paper with exact rescoping instructions).
```
