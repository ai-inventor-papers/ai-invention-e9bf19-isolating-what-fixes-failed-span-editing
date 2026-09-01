# gen_plan_evaluation_1 — test_idea

> Phase: `invention_loop` · round 5 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_evaluation_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 10:24:43 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_evaluation_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 10:24:51 UTC

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
You are expanding an artifact direction of type: EVALUATION

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed
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

The evaluation executor has 3h total (including writing code, debugging, testing, and fixing errors).

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
title: Combining Both Repair Levers Backfires, Not Yet Why
hypothesis: >-
  Padmanabhan (2025)'s WMT25 Task 3 secondary system (SURREYPAI-S2) -- QE-flagged spans masked with a __BLANK__ token, a single
  TowerPlus-9B fill-in pass, no re-check -- scored ΔCOMET = -0.0108, the worst of eight ranked Task 3 entries, against +0.0201
  for the same team's primary retranslation-selection system. Across four iterations of controlled testing (fixed repair model
  google/gemma-3-12b-it throughout, since TowerPlus-9B and its assumed fallbacks are confirmed delisted; real wmt22-cometkiwi-da
  checkpoint for every condition except one; en-ru_RU and en-uk_UA), all five conditions in the factorial design are now EXECUTED
  to completion: B (faithful masked-fill baseline), D (B plus trivial output-hygiene retry), C1 (checker-broadened localization,
  single uncorrected pass), C2 (narrow QE-span-only localization, iteratively re-checked/re-repaired up to a 3-pass budget),
  and C (broad localization plus iteration, combined). What is now MEASURED: (1) D does not close B's gap (fix/regression
  rates identical to B, ΔCOMET statistically indistinguishable) -- ruling out output hygiene as the explanation. (2) C1 cuts
  ΔCOMET degradation roughly fivefold relative to B/D (pooled -0.0035 vs -0.0164/-0.0157) at a real correctness cost: fix
  rate 0.6056 vs 0.9833, true regression rate 0.1389 vs 0.0667 (pooled excluding negation-deletion rows, which narrow-localization
  conditions structurally cannot attempt). (3) C2 recovers fix rate and true regression rate to near-parity with B/D (0.9889/0.0722
  excluding negation) and beats C1 on both (paired-bootstrap advantage +0.2875 [CI 0.2292,0.3458] on the 240-row population
  including negation-deletion rows vs +0.3833 on the 180-row population excluding them -- now stated together with the negation-attemptability
  mechanism that produces the gap between them, not as competing numbers), but C2's pooled ΔCOMET (-0.0166) is statistically
  indistinguishable from B/D and measurably WORSE than C1's (-0.0131 by a documented normal-approximation substitute, CI [-0.0214,-0.0047]).
  Iteration recovers targeted correctness; broadened localization is what has been shown to move whole-sentence quality --
  two different, non-substitutable levers. (4) Condition C -- executed this iteration to full completion (560/560 rows, 100%,
  resumed cleanly through a mid-run agent-side crash via new per-row checkpointing, per-call timeout-and-retry, and heartbeat
  infrastructure that is now validated under a real, not simulated, failure) -- DISCONFIRMS the combined-levers hypothesis
  on every axis fully and comparably measured. Fix rate (0.6278, excluding negation) sits between C1's 0.6056 and C2's 0.9889,
  matching neither. True regression rate (0.2167) is the HIGHEST of all five conditions, exceeding C1's 0.1389 and more than
  tripling C2's 0.0722. Certificate rate -- the fraction of rows reaching a verified zero-flag state within budget, a metric
  this protocol only needed once iteration and broad localization were combined -- collapses from C2's 0.917 to 0.267 once
  the checker's surface broadens to whole-sentence scope, while edit volume (0.022) stays essentially identical to C1's (0.021),
  ruling out heavier editing as the explanation. Combining the levers does not combine their gains; it produces a genuinely
  new, worse-than-either failure mode on the correctness axes. (5) The quality axis for Condition C remains UNRESOLVED, and
  this is now the SECOND unmitigated instance of the same specific infrastructure gap: Hugging Face Hub returned HTTP 429
  on all twelve retry attempts across two backoff probes during this run, exactly as it did for Condition B's first attempt
  (resolved there only by falling back to an uncalibrated LLM-judge proxy, and here by falling back to a second, DIFFERENT
  uncalibrated proxy with no cross-condition comparability at all) -- the repair-loop robustness infrastructure built and
  validated this iteration does not address this failure class, which sits entirely on the scoring/evaluation side, and no
  pre-caching, mirrored checkpoint, or reuse of a single consistent proxy across conditions has yet been attempted despite
  this being the second occurrence. (6) The reviewer-identified mechanism gap for the certificate-rate collapse is now explicitly
  UNRESOLVED rather than implicitly asserted: the paper's own Table 1 shows checker precision on usable cells ranging 0.575-0.857,
  meaning a non-trivial share of the checker's re-flags on already-correct repairs could themselves be false positives rather
  than genuine newly-introduced violations, and the strongest available first-order evidence -- number_unit_date reaching
  the highest fix rate (0.983) of any category while having the lowest certificate rate (0.067) and highest mean pass count
  (2.90, near the 3-pass cap) -- is equally consistent with a checker-noise-driven churn story as with a genuine-cross-invariant-regression
  story; no analysis in this project's artifacts yet stratifies certificate-rate collapse by per-cell checker precision to
  distinguish the two. (7) A related scope caveat, previously stated only in a table caption, now belongs at first mention:
  of the three categories pooled into the 180-row 'every condition can attempt' comparison, only number_unit_date (and roughly
  half of quantifier_scope, ru_RU only) is genuinely checker-localized AND checker-verified for C1 and C under Table 1's within-experiment
  gating -- named_entity is excluded from repair scope in both tested languages and quantifier_scope in uk_UA, so C1/C's named-entity
  repairs in that pooled figure rely on the original QE-flagged span, not the broadened checker's own localization, despite
  being counted as 'broad localization' evidence. We hypothesize, now narrowed a final time by Condition C's disconfirming
  result, that broadened one-pass localization (C1) and narrow-but-iterated repair (C2) are two genuinely different, non-dominating,
  and NON-ADDITIVE mechanisms: naively combining them under a pass budget sized for the narrower loop does not capture both
  gains and instead produces the worst correctness profile of any condition tested, with a certificate-rate collapse whose
  cause -- genuine cross-invariant interaction versus checker-precision-driven false re-flagging -- is not yet separated by
  any measurement this project has made, and whose remedy -- a wider or checker-surface-scaled pass budget -- is proposed
  but untested. The mechanism-attributing part of the original hypothesis (iteration as THE differentiator, or the two levers
  as freely combinable) is now DISCONFIRMED on the correctness axes and UNDETERMINED on the quality axis by two compounding,
  still-unaddressed evaluation-infrastructure gaps (checkpoint access; the false-positive-versus-genuine-regression confound)
  rather than by a lack of data.
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
  Same B/D/C1/C2/C frame; C executed and DISCONFIRMS combination; mechanism + quality-axis gaps now explicit, not asserted
_confidence_delta: increased
_key_changes:
- >-
  Replaced 'C still outstanding' with Condition C's executed, disconfirming result: fix rate between C1/C2 matching neither,
  true regression rate the worst of all five conditions, certificate rate collapsing from 0.917 (C2) to 0.267 once localization
  broadens -- combining the levers produces a new, worse-than-either failure mode rather than additive gains.
- >-
  Demoted the certificate-rate-collapse mechanism from an asserted 'genuine new/introduced violations' claim to an explicitly
  UNRESOLVED question, per reviewer critique 1: Table 1's 0.575-0.857 checker precision on usable cells means checker-false-positive-driven
  re-flagging is an equally consistent explanation, and number_unit_date's own pattern (highest fix rate, lowest certificate
  rate, most passes) does not distinguish the two stories with data this project has actually analyzed.
- >-
  Named the recurring, unmitigated HuggingFace Hub checkpoint-access failure explicitly as a second occurrence with no attempted
  fix (pre-caching, mirror, or a consistent proxy carried across conditions), per reviewer critique 2, rather than reporting
  it as an isolated bad-luck event.
- >-
  Added the checker-eligibility scope caveat (only number_unit_date, plus ru_RU quantifier_scope, is genuinely checker-localized
  AND checker-verified for C1/C in the 180-row pooled comparison; named-entity relies on the original QE span, not the broadened
  checker) as a first-class stated property, per reviewer critique 3, rather than a footnote encountered late.
- >-
  Kept the reconciled fix-rate-advantage figures (+0.2875 including negation vs +0.3833 excluding it) but now presents them
  together with the mechanism that explains the gap, rather than as two figures requiring separate justification.
- >-
  Narrowed the overall verdict: the combined-levers claim is now DISCONFIRMED on the correctness axes (not merely undetermined),
  while the quality axis and the certificate-collapse mechanism are both explicitly flagged as open, unresolved questions
  for the next iteration rather than settled findings.
- >-
  Retained the core B/D/C1/C2/C factorial frame, the fixed-repair-model control, and the disjoint-population caveat, since
  nothing this iteration found contradicts the design -- only the completeness and interpretation of its final cell.
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

id: evaluation_iter5_dir3
type: evaluation
objective: >-
  Produce the paper's final, consolidated reviewer-response analysis: separate checker-false-positive-driven certificate collapse
  from genuine cross-invariant regression using Table 1's per-cell precision against Table 3's per-category certificate rate
  and pass counts (cross-referenced against the widened-budget experiment's per-pass false-positive tracking where available);
  state the 180-row checker-eligibility caveat at first mention with a secondary restricted-population table; clarify what
  'certificate' means for checker-excluded categories; and give an explicit, justified statement of the normal-approximation
  substitute's bias direction.
approach: >-
  Load art_AHSm43w1MzxX's scorecard, art_6n9zJVKWXnio's Condition C per-category results (Table 3's source data), and the
  Table 1 precision/recall values from art_7Uc5PlFctjXi's checker_validation.json. First, the precision-vs-collapse analysis:
  group the usable (language, category) cells by checker precision tier (high: negation_polarity ~0.78-0.86; low: number_unit_date
  ~0.575) and compare certificate rate and mean pass count within each tier; state explicitly whether the collapse is roughly
  uniform across tiers (supporting genuine new/introduced violations) or concentrated in the low-precision tier (supporting
  checker-noise-driven churn) -- report this as a first-order, non-causal correlational bound, exactly as the reviewer's action
  item specifies, not as a definitive causal claim. If the widened-pass-budget experiment (this strategy's second artifact)
  completed, use its per-pass false-positive tracking as direct, stronger evidence for the same question and reconcile it
  with the precision-tier estimate. Second, the eligibility caveat: restate, in the output's summary of what the paper's Section
  6.4 should say before Table 2, that only number_unit_date (and roughly half of quantifier_scope, ru_RU only) is genuinely
  checker-localized and checker-verified for C1/C under Table 1's gating, and compute a secondary restricted-population table
  (fix rate, true regression rate, certificate rate, per condition) over only the fully checker-eligible cells, so a reader
  can check whether the headline C1-vs-C2-vs-C pattern holds when the checker's own localization claim is uncontested. Third,
  add an explicit clarifying field stating that a row's certificate status is computed over the checker-tracked invariants
  only, independent of whether that row's own known-corrupted category (e.g. named_entity) falls in an excluded cell. Fourth,
  either give a concrete one-sentence argument for why treating two positively-correlated measurements as independent widens
  (not narrows) the estimated variance of their difference, using the actual C1/C2 per-condition CI half-widths as a worked
  numeric example, or -- if that argument cannot be made rigorously from available data -- explicitly soften the paper's 'conservative-direction'
  claim to 'direction of bias not established.' Output every one of these four analyses as first-class, separately labeled
  fields so the paper text can cite them directly.
depends_on:
- id: art_6n9zJVKWXnio
  label: condition-c-results
  relation_type:
  relation_rationale:
- id: art_7Uc5PlFctjXi
  label: checker-validation
  relation_type:
  relation_rationale:
- id: art_K8koUmGFDlLN
  label: condition-c2-results
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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

--- Dependency 2 ---
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

--- Dependency 3 ---
id: art_6n9zJVKWXnio
type: experiment
title: 'Condition C: Combined Checker-Repair Sweep'
summary: >-
  Executes Condition C (checker-broadened localization + iterative repair-and-reverify, MAX_PASSES=3, google/gemma-3-12b-it
  via OpenRouter) on the identical 560-row population (320 natural WMT25 rows + 240 injected-error rows) used by prior conditions
  B/D/C1/C2, with row-ID identity verified True against C2 for all three sub-folds. This run resumed a prior attempt that
  crashed mid-sweep due to an agent-side busy-polling failure (not a code defect): the resume-aware, incrementally-fsynced
  JSONL ledger (condition_c_progress.jsonl) let this execution pick up exactly where it left off, deduplicate by row_id, and
  finish cleanly. The full 560/560-row sweep completed (completion_fraction=1.0, 0 hard failures on either fold) for $0.031
  of the $10 OpenRouter budget (731 calls). method.py implements the full pipeline: stratified data loading with row-ID identity
  checks vs C2, the four-category deterministic checker (NER/number-unit-date/negation/quantifier) with an 8-cell usability-gated
  exclusion table refit each run, the C1+C2 combined repair loop (checker re-run fresh every pass, stopping on a zero-flag
  certificate), a hard per-call timeout+retry wrapper, heartbeat logging, and a full scoring stage producing method_out.json's
  per-row and pooled metrics plus a direct B/D/C1/C2-vs-C comparison table. Key results: pooled injected-pool fix_rate=0.628,
  true_regression_rate=0.217, certificate_rate=0.267 (vs C2's 0.989/0.072/0.917 and C1's 0.454/0.125/n.a.), n_llm_calls_mean=2.29/row.
  Condition C's checker-based localization uniquely attempts negation-DELETION rows (which B/D/C2's oracle-span localization
  structurally cannot address at all): 60 such rows existed, and the broadened checker flagged 58.3% of them pre-repair, a
  genuinely new number with no B/D/C2 counterpart -- reported separately since the row-level 'fixed' verdict is undefined
  without a corrupted span to check absence of. KNOWN LIMITATION, honestly flagged in method_out.json (comet_available=false,
  delta_comet_metric='DeltaCOMET-proxy (NOT COMET)'): the real Unbabel/wmt22-cometkiwi-da checkpoint that scored every prior
  condition (B/D/C1/C2) could not be downloaded this run -- Hugging Face Hub returned HTTP 429 on every retry across two separate
  multi-minute backoff probes (12 attempts total, persistent not transient), so natural-row DeltaCOMET here (+0.0016 pooled)
  was computed with a non-gated proxy QE score instead and is NOT directly numerically comparable to C1/C2's real-COMET deltas
  (both negative) in the comparison table -- a downstream evaluation artifact should either retry the COMET download when
  HF access is available or treat Condition C's natural-row deltas as directionally-suggestive only. Every other metric (fix
  rate, true regression rate, certificate rate, edit volume, call counts) uses the same scoring functions as C1/C2 and is
  fully comparable. Outputs: method.py (pipeline), full/mini/preview_method_out.json (schema-validated against exp_gen_sol_out,
  2 datasets: natural_repair_C with 320 examples, injected_pool_repair_C with 240), checker.py, llm_client.py, selected_rows.json
  (persisted row IDs for future identity checks), condition_c_progress.jsonl (raw per-row ledger), dry_run_test.py (the 3-row/timeout-injection/resume
  tests specified in the testing plan, all passed and logged).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1
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

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle
</artifact_executor_scope>

<artifact_planning_rules>
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for evaluation artifacts:
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
  "description": "Plan for an EVALUATION artifact.",
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
    "metrics_descriptions": {
      "description": "What metrics will be computed and how they're defined",
      "title": "Metrics Descriptions",
      "type": "string"
    },
    "metrics_justification": {
      "description": "Why these metrics are the right ones - what do they tell us about the hypothesis",
      "title": "Metrics Justification",
      "type": "string"
    }
  },
  "required": [
    "title",
    "metrics_descriptions",
    "metrics_justification"
  ],
  "title": "EvaluationPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 10:24:51 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Write · 2026-09-01 10:25:39 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json

{
  "title": "Untangling Why Combining Repair Fixes Failed",
  "summary": "A reviewer-response evaluation that reconciles the paper's open Condition-C findings: it separates checker-false-positive-driven certificate collapse from genuine cross-invariant regression by cross-tabulating Table 1's per-cell checker precision/recall against Table 3's per-category certificate rate and pass counts; restates the 180-row checker-eligibility caveat at first mention with a secondary restricted-population table limited to fully checker-eligible cells; clarifies what 'certificate' means for checker-excluded categories (e.g. named_entity in en-ru_RU/en-uk_UA); and gives an explicit, numerically-worked statement of the normal-approximation substitute's bias direction (or an explicit admission that the direction cannot be established). All four analyses are produced as separately labeled, directly citable fields in eval_out.json, with every number traced to a specific source file/field so the paper text can quote them verbatim.",
  "runpod_compute_profile": "cpu_light",
  "metrics_descriptions": "This is a pure re-analysis of already-computed results from three prior EXPERIMENT artifacts — no new LLM calls, no new repairs, no new COMET scoring. The executor should load: (1) art_7Uc5PlFctjXi's full_method_out.json and checker_validation.json for the B/D/C1 baseline numbers and Table 1's per-(language,category) checker precision/recall cells and the 8-cell usability-gating exclusion table; (2) art_K8koUmGFDlLN's full_method_out.json for C2's per-category/per-language fix_rate, true_regression_rate, and pass-count data, plus its row-ID identity manifest (selected_rows.json) for population matching; (3) art_6n9zJVKWXnio's full_method_out.json, condition_c_progress.jsonl, and selected_rows.json for Condition C's per-category/per-language fix_rate, true_regression_rate, certificate_rate, mean pass count, and the negation-deletion-row breakdown, plus its documented COMET-proxy caveat. Before any computation, verify row-ID identity across all three artifacts' selected_rows.json (natural, injected-pool, injected-heldout folds) exactly as art_K8koUmGFDlLN and art_6n9zJVKWXnio already did pairwise — do not assume transitivity, re-check B/D/C1 vs C directly since that pair was never directly cross-checked in the dependencies.\n\nFour first-class output analyses, each a separately labeled field in eval_out.json:\n\n(1) precision_tier_collapse_analysis — group every usable (language, category) cell (the ones NOT excluded by Table 1's recall/precision>=0.5 gate) into a high-precision tier (checker precision roughly 0.78-0.86, e.g. negation_polarity per art_7Uc5PlFctjXi's checker_validation.json) and a low-precision tier (roughly 0.575-0.65, e.g. number_unit_date). For each tier, report mean certificate_rate and mean pass_count from Condition C's per-category data (art_6n9zJVKWXnio), with the cell count and the raw per-cell numbers listed so the aggregation is auditable. State explicitly, as a single labeled verdict field (e.g. collapse_pattern: 'uniform_across_tiers' | 'concentrated_in_low_precision_tier' | 'indeterminate_too_few_cells'), which pattern the data shows — uniform supports genuine cross-invariant regression, concentration in the low-precision tier supports checker-noise-driven churn. Explicitly log the number of usable cells actually available for this comparison (likely small, since 3 of 8 language x category cells were already excluded upstream) and flag low statistical power by name rather than silently reporting a two- or three-cell comparison as decisive. Report this as a correlational, non-causal first-order bound, not a causal claim — use hedged language ('is consistent with', 'does not distinguish between') throughout, never 'proves' or 'causes'. If a widened-pass-budget experiment artifact with per-pass false-positive tracking exists among the dependencies (check the full dependency list actually provided at execution time, not just the three named here — this direction's approach references a possible fourth artifact), use its per-pass false-positive-vs-pass-number data as a second, stronger line of evidence and explicitly reconcile it with the precision-tier estimate (agree / disagree / cannot compare due to different populations). If no such artifact exists among the actual dependencies, state plainly that the stronger evidence is unavailable and the precision-tier estimate is the best available signal, rather than silently omitting the requested comparison.\n\n(2) checker_eligibility_restricted_analysis — restate as a first-class text field (not a footnote) the exact eligibility scope: which (language, category) combinations are genuinely checker-localized AND checker-verified for C1 and C under Table 1's gating (per the hypothesis text and checker_validation.json: number_unit_date in both languages, and quantifier_scope in ru_RU only — named_entity is excluded in both languages, quantifier_scope is excluded in uk_UA). Then compute a secondary restricted-population table: for B, D, C1, C2, and C, report fix_rate, true_regression_rate, and certificate_rate (where defined) computed ONLY over rows/cells that fall in this fully-eligible set, alongside the existing full pooled figures for direct side-by-side comparison. State explicitly whether the headline ordering (C1 < C2 on fix/regression; C worse than both on true_regression_rate; certificate_rate collapse C2-to-C) survives, changes magnitude, or reverses when restricted to uncontested cells. Report exact row/cell counts in the restricted population so the reader can judge its statistical power.\n\n(3) certificate_definition_by_category — a short explicit clarifying statement, as its own labeled field, that a row's certificate status (used throughout C2/C reporting) is computed over only the invariants the checker actually tracks and re-verifies for that row's included categories, independent of whether the row's OWN corrupted/target category is itself in an excluded cell. Concretely: if a row's known corruption is named_entity in en-ru_RU (an excluded cell), clarify whether that row is (a) excluded from certificate_rate denominators entirely, (b) included but scored certificate=True/False based only on the OTHER, non-excluded invariants in the sentence, or (c) something else — determine the actual behavior by reading art_6n9zJVKWXnio's method.py/checker.py scoring logic and condition_c_progress.jsonl row-level fields directly (do not guess), and state the finding plainly with a worked example row ID.\n\n(4) normal_approx_bias_direction — attempt a rigorous one-sentence argument, backed by a numeric worked example using the ACTUAL C1 and C2 per-condition ΔCOMET (or true_regression_rate/fix_rate, whichever the paper's original 'conservative-direction' claim was about — identify this from the dependency artifacts' text) 95% CI half-widths, for why treating two positively-correlated measurements as independent when computing the variance of their difference (Var(X-Y) = Var(X)+Var(Y) instead of Var(X)+Var(Y)-2*Cov(X,Y)) makes the estimated CI on the difference WIDER (i.e. more conservative), not narrower, whenever Cov(X,Y) > 0. Show the arithmetic explicitly: with positive covariance, subtracting 2*Cov(X,Y) shrinks the true variance below the independence-assumed estimate, so the independence assumption over-estimates variance and the interval is a conservative (too-wide, not too-narrow) substitute. Plug in the actual reported CI half-widths from art_7Uc5PlFctjXi/art_K8koUmGFDlLN (e.g. C1's and C2's ΔCOMET or fix-rate CIs) to show the direction holds for these specific numbers, and note any known or estimated correlation source (e.g. shared row population, shared repair model, shared checker) that makes positive covariance plausible here. If, after attempting this, the covariance sign or magnitude cannot actually be estimated or bounded from available data (no per-row paired samples were retained in a form that permits computing empirical covariance), do NOT force a conclusion — instead explicitly downgrade the paper's claim to 'direction of bias not established from available data' and say exactly what additional data (e.g. per-row paired bootstrap replicates) would be needed to establish it.\n\nEach of the four fields above must independently record: the source artifact + exact file/field path for every number used, any assumptions made when a dependency did not exactly match what the direction's approach expected (e.g. missing widened-budget artifact), and a one-line confidence caveat where sample sizes are small.",
  "metrics_justification": "These four analyses directly answer the paper's most consequential open question from Condition C's disconfirming result: whether the certificate-rate collapse (C2's 0.917 to C's 0.267) reflects a genuine new failure mode from combining broadened localization with iteration, or is instead an artifact of the checker's own imperfect precision (0.575-0.857 per Table 1) manufacturing false re-flags that look like regressions but are not. This distinction is load-bearing for the hypothesis's central mechanism claim: if collapse is checker-noise-driven, the 'combining levers backfires' conclusion is weaker than stated and the paper must say so; if collapse is roughly uniform across precision tiers, the genuine-interaction story is better supported and the paper can state it with appropriate confidence. Without this analysis, the paper would be asserting a mechanism the project's own measurements do not yet distinguish from a known confound — exactly the reviewer-identified gap the hypothesis text names explicitly as UNRESOLVED. The eligibility-restricted table matters because the pooled 180-row comparison currently mixes genuinely checker-verified evidence with cells where C1/C's 'broad localization' credit is actually borrowed from the original QE span — reporting both the full and restricted tables lets a reader judge whether the headline pattern is an artifact of pooling contested and uncontested cells together, which is a basic internal-validity check the paper currently lacks. The certificate-definition clarification prevents a latent ambiguity (does a row's certificate status silently ignore its own known-corrupted, checker-excluded category?) from making the C2/C certificate_rate numbers uninterpretable or misleading to a careful reader. The bias-direction analysis closes out a specific, previously hand-waved statistical claim ('the substitute is conservative') with either a rigorous derivation tied to the project's own numbers or an honest downgrade — both of which are more defensible in review than an unsupported directional assertion. Together, these four analyses convert four still-open reviewer-facing gaps into stated, evidenced, appropriately-hedged conclusions, which is precisely what a final consolidated reviewer-response evaluation for this paper needs to deliver before the paper text is finalized."
}
```

### [5] TOOL RESULT — Write · 2026-09-01 10:25:39 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Untangling Why Combining Repair Fixes Failed\",\n  \"summary\": \"A reviewer-response evaluation that reconciles the paper's open Condition-C findings: it separates checker-false-positive-driven certificate collapse from genuine cross-invariant regression by cross-tabulating Table 1's per-cell checker precision/recall against Table 3's per-category certificate rate and pass counts; restates the 180-row checker-eligibility caveat at first mention with a secondary restricted-population table limited to fully checker-eligible cells; clarifies what 'certificate' means for checker-excluded categories (e.g. named_entity in en-ru_RU/en-uk_UA); and gives an explicit, numerically-worked statement of the normal-approximation substitute's bias direction (or an explicit admission that the direction cannot be established). All four analyses are produced as separately labeled, directly citable fields in eval_out.json, with every number traced to a specific source file/field so the paper text can quote them verbatim.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"metrics_descriptions\": \"This is a pure re-analysis of already-computed results from three prior EXPERIMENT artifacts — no new LLM calls, no new repairs, no new COMET scoring. The executor should load: (1) art_7Uc5PlFctjXi's full_method_out.json and checker_validation.json for the B/D/C1 baseline numbers and Table 1's per-(language,category) checker precision/recall cells and the 8-cell usability-gating exclusion table; (2) art_K8koUmGFDlLN's full_method_out.json for C2's per-category/per-language fix_rate, true_regression_rate, and pass-count data, plus its row-ID identity manifest (selected_rows.json) for population matching; (3) art_6n9zJVKWXnio's full_method_out.json, condition_c_progress.jsonl, and selected_rows.json for Condition C's per-category/per-language fix_rate, true_regression_rate, certificate_rate, mean pass count, and the negation-deletion-row breakdown, plus its documented COMET-proxy caveat. Before any computation, verify row-ID identity across all three artifacts' selected_rows.json (natural, injected-pool, injected-heldout folds) exactly as art_K8koUmGFDlLN and art_6n9zJVKWXnio already did pairwise — do not assume transitivity, re-check B/D/C1 vs C directly since that pair was never directly cross-checked in the dependencies.\\n\\nFour first-class output analyses, each a separately labeled field in eval_out.json:\\n\\n(1) precision_tier_collapse_analysis — group every usable (language, category) cell (the ones NOT excluded by Table 1's recall/precision>=0.5 gate) into a high-precision tier (checker precision roughly 0.78-0.86, e.g. negation_polarity per art_7Uc5PlFctjXi's checker_validation.json) and a low-precision tier (roughly 0.575-0.65, e.g. number_unit_date). For each tier, report mean certificate_rate and mean pass_count from Condition C's per-category data (art_6n9zJVKWXnio), with the cell count and the raw per-cell numbers listed so the aggregation is auditable. State explicitly, as a single labeled verdict field (e.g. collapse_pattern: 'uniform_across_tiers' | 'concentrated_in_low_precision_tier' | 'indeterminate_too_few_cells'), which pattern the data shows — uniform supports genuine cross-invariant regression, concentration in the low-precision tier supports checker-noise-driven churn. Explicitly log the number of usable cells actually available for this comparison (likely small, since 3 of 8 language x category cells were already excluded upstream) and flag low statistical power by name rather than silently reporting a two- or three-cell comparison as decisive. Report this as a correlational, non-causal first-order bound, not a causal claim — use hedged language ('is consistent with', 'does not distinguish between') throughout, never 'proves' or 'causes'. If a widened-pass-budget experiment artifact with per-pass false-positive tracking exists among the dependencies (check the full dependency list actually provided at execution time, not just the three named here — this direction's approach references a possible fourth artifact), use its per-pass false-positive-vs-pass-number data as a second, stronger line of evidence and explicitly reconcile it with the precision-tier estimate (agree / disagree / cannot compare due to different populations). If no such artifact exists among the actual dependencies, state plainly that the stronger evidence is unavailable and the precision-tier estimate is the best available signal, rather than silently omitting the requested comparison.\\n\\n(2) checker_eligibility_restricted_analysis — restate as a first-class text field (not a footnote) the exact eligibility scope: which (language, category) combinations are genuinely checker-localized AND checker-verified for C1 and C under Table 1's gating (per the hypothesis text and checker_validation.json: number_unit_date in both languages, and quantifier_scope in ru_RU only — named_entity is excluded in both languages, quantifier_scope is excluded in uk_UA). Then compute a secondary restricted-population table: for B, D, C1, C2, and C, report fix_rate, true_regression_rate, and certificate_rate (where defined) computed ONLY over rows/cells that fall in this fully-eligible set, alongside the existing full pooled figures for direct side-by-side comparison. State explicitly whether the headline ordering (C1 < C2 on fix/regression; C worse than both on true_regression_rate; certificate_rate collapse C2-to-C) survives, changes magnitude, or reverses when restricted to uncontested cells. Report exact row/cell counts in the restricted population so the reader can judge its statistical power.\\n\\n(3) certificate_definition_by_category — a short explicit clarifying statement, as its own labeled field, that a row's certificate status (used throughout C2/C reporting) is computed over only the invariants the checker actually tracks and re-verifies for that row's included categories, independent of whether the row's OWN corrupted/target category is itself in an excluded cell. Concretely: if a row's known corruption is named_entity in en-ru_RU (an excluded cell), clarify whether that row is (a) excluded from certificate_rate denominators entirely, (b) included but scored certificate=True/False based only on the OTHER, non-excluded invariants in the sentence, or (c) something else — determine the actual behavior by reading art_6n9zJVKWXnio's method.py/checker.py scoring logic and condition_c_progress.jsonl row-level fields directly (do not guess), and state the finding plainly with a worked example row ID.\\n\\n(4) normal_approx_bias_direction — attempt a rigorous one-sentence argument, backed by a numeric worked example using the ACTUAL C1 and C2 per-condition ΔCOMET (or true_regression_rate/fix_rate, whichever the paper's original 'conservative-direction' claim was about — identify this from the dependency artifacts' text) 95% CI half-widths, for why treating two positively-correlated measurements as independent when computing the variance of their difference (Var(X-Y) = Var(X)+Var(Y) instead of Var(X)+Var(Y)-2*Cov(X,Y)) makes the estimated CI on the difference WIDER (i.e. more conservative), not narrower, whenever Cov(X,Y) > 0. Show the arithmetic explicitly: with positive covariance, subtracting 2*Cov(X,Y) shrinks the true variance below the independence-assumed estimate, so the independence assumption over-estimates variance and the interval is a conservative (too-wide, not too-narrow) substitute. Plug in the actual reported CI half-widths from art_7Uc5PlFctjXi/art_K8koUmGFDlLN (e.g. C1's and C2's ΔCOMET or fix-rate CIs) to show the direction holds for these specific numbers, and note any known or estimated correlation source (e.g. shared row population, shared repair model, shared checker) that makes positive covariance plausible here. If, after attempting this, the covariance sign or magnitude cannot actually be estimated or bounded from available data (no per-row paired samples were retained in a form that permits computing empirical covariance), do NOT force a conclusion — instead explicitly downgrade the paper's claim to 'direction of bias not established from available data' and say exactly what additional data (e.g. per-row paired bootstrap replicates) would be needed to establish it.\\n\\nEach of the four fields above must independently record: the source artifact + exact file/field path for every number used, any assumptions made when a dependency did not exactly match what the direction's approach expected (e.g. missing widened-budget artifact), and a one-line confidence caveat where sample sizes are small.\",\n  \"metrics_justification\": \"These four analyses directly answer the paper's most consequential open question from Condition C's disconfirming result: whether the certificate-rate collapse (C2's 0.917 to C's 0.267) reflects a genuine new failure mode from combining broadened localization with iteration, or is instead an artifact of the checker's own imperfect precision (0.575-0.857 per Table 1) manufacturing false re-flags that look like regressions but are not. This distinction is load-bearing for the hypothesis's central mechanism claim: if collapse is checker-noise-driven, the 'combining levers backfires' conclusion is weaker than stated and the paper must say so; if collapse is roughly uniform across precision tiers, the genuine-interaction story is better supported and the paper can state it with appropriate confidence. Without this analysis, the paper would be asserting a mechanism the project's own measurements do not yet distinguish from a known confound — exactly the reviewer-identified gap the hypothesis text names explicitly as UNRESOLVED. The eligibility-restricted table matters because the pooled 180-row comparison currently mixes genuinely checker-verified evidence with cells where C1/C's 'broad localization' credit is actually borrowed from the original QE span — reporting both the full and restricted tables lets a reader judge whether the headline pattern is an artifact of pooling contested and uncontested cells together, which is a basic internal-validity check the paper currently lacks. The certificate-definition clarification prevents a latent ambiguity (does a row's certificate status silently ignore its own known-corrupted, checker-excluded category?) from making the C2/C certificate_rate numbers uninterpretable or misleading to a careful reader. The bias-direction analysis closes out a specific, previously hand-waved statistical claim ('the substitute is conservative') with either a rigorous derivation tied to the project's own numbers or an honest downgrade — both of which are more defensible in review than an unsupported directional assertion. Together, these four analyses convert four still-open reviewer-facing gaps into stated, evidenced, appropriately-hedged conclusions, which is precisely what a final consolidated reviewer-response evaluation for this paper needs to deliver before the paper text is finalized.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-09-01 10:25:44 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — a reviewer-response evaluation that (1) cross-tabulates checker precision tiers against Condition C's certificate-rate collapse to separate checker-noise from genuine regression, (2) restates the 180-row eligibility caveat with a restricted-population table, (3) clarifies certificate semantics for checker-excluded categories, and (4) rigorously derives (or explicitly disclaims) the normal-approximation substitute's bias direction using the project's own CI numbers.
```
