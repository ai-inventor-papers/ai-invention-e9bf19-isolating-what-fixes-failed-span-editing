# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 5 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 10:24:43 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_1
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

id: experiment_iter5_dir1
type: experiment
objective: >-
  Resolve Condition C's quality-axis metric gap: attempt real wmt22-cometkiwi-da scoring of Condition C's already-generated
  natural-row repair outputs with mitigations specifically targeting the twice-observed HF Hub 429 failure, and if that genuinely
  still fails, fall back to the SAME LLM-judge proxy metric that scored Condition B's fidelity check (not a new, third, incomparable
  proxy) so Condition C's quality number is at least directly comparable to one other condition's.
approach: >-
  This is a scoring-only rerun -- no new repair generation, no new OpenRouter repair calls -- over the 320 natural-row post-repair
  texts already produced and persisted in art_6n9zJVKWXnio's full_method_out.json. First, attempt the real checkpoint download
  with mitigations the prior two attempts did not try: a longer wall-clock budget spread across widely-separated retry windows
  (not just back-to-back backoff), an alternate Hugging Face endpoint if one is reachable (e.g. HF_HUB_ENDPOINT mirror), and
  resumable/partial-download support so a rate-limited attempt does not discard progress. Log every attempt (timestamp, endpoint,
  error code) so a persistent 429 versus a transient one is distinguishable this time. If the real checkpoint remains unreachable
  after this genuinely mitigated attempt, fall back explicitly to the exact LLM-judge proxy configuration (same model, same
  prompt, same before/after adequacy scoring convention) used in art_G9ppuk8aHUhW's Condition-B fidelity check -- re-score
  Condition B's own natural rows with this identical proxy alongside Condition C's, so the output reports a same-proxy, same-run
  B-vs-C comparison rather than Condition C's proxy in isolation. Output must state explicitly which path was taken (real
  checkpoint vs. same-proxy fallback) and, if the fallback path was used, must not claim numerical comparability to C1/C2's
  real-COMET figures -- only to B's proxy-scored figure from this same rerun.
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

### [3] HUMAN-USER prompt · 2026-09-01 10:24:51 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Write · 2026-09-01 10:26:34 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Rescue Condition C's Missing Quality Score",
  "summary": "Scoring-only rerun over Condition C's already-generated 320 natural-row repair outputs: attempt real wmt22-cometkiwi-da with genuinely new HF-429 mitigations (mirror endpoint, resumable download, widely-spaced retry windows, full attempt logging); if it still fails, fall back to the EXACT same LLM-judge proxy configuration used for Condition B's fidelity check, re-scoring B's own rows with that identical proxy in the same run so the output reports a same-proxy B-vs-C comparison rather than an isolated, incomparable number. No new repair generation and no new repair-model calls; this only scores text that already exists.",
  "runpod_compute_profile": "gpu",
  "implementation_pseudocode": "# --- Phase 0: locate inputs (no new generation) ---\n# The direction names two upstream artifacts by id that are NOT in this plan's formal\n# depends_on (only the dataset art_mhfmDpGp4z1J and the resource dossier art_5ySTX4YfxqG_\n# are). They are prior-iteration artifacts in the SAME run and must be located on disk:\nRUN_ROOT = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5'\ndef find_artifact_dir(short_id):\n    # short_id e.g. '6n9zJVKWXnio' or 'G9ppuk8aHUhW' (the part after 'art_')\n    # search every iter_*/gen_art*/gen_art_*/ for a dir or meta file whose artifact id matches\n    candidates = glob(f'{RUN_ROOT}/**/full_method_out.json', recursive=True) + \\\n                 glob(f'{RUN_ROOT}/**/method_out.json', recursive=True)\n    matches = [c for c in candidates if short_id in read_meta_near(c).get('artifact_id','')]\n    if not matches: matches = [c for c in candidates if short_id in c]  # path-based fallback\n    assert matches, f'BLOCKING: could not locate artifact art_{short_id} on disk'\n    return matches[0]\n\ncondition_c_path = find_artifact_dir('6n9zJVKWXnio')   # full_method_out.json for Condition C (560 rows total)\ncondition_b_path = find_artifact_dir('G9ppuk8aHUhW')   # Condition B artifact incl. its fidelity-check proxy config/code\n\ncondition_c_rows = json.load(open(condition_c_path))\nnatural_c_rows = [r for r in condition_c_rows if r['metadata_fold_or_source'] == 'wmt25_task3_natural']\nassert len(natural_c_rows) == 320, f'expected 320 natural rows, got {len(natural_c_rows)}'\n# each row must carry: source_text, pre_repair_text (or original MT hyp), post_repair_text, language_pair, row_id\n\ncondition_b_artifact = load_artifact_bundle(condition_b_path)  # includes its .py source and full_method_out.json\nb_fidelity_config = extract_fidelity_check_config(condition_b_artifact)\n# b_fidelity_config MUST capture, verbatim from B's own code/prompt file:\n#   - the exact OpenRouter model id used as judge\n#   - the exact system/user prompt template (before/after adequacy scoring)\n#   - the exact numeric scoring convention (scale, direction, aggregation)\n#   - temperature / sampling params\n# If b_fidelity_config cannot be extracted verbatim (code missing/renamed), STOP and\n# record a blocking finding rather than inventing a proxy config from memory.\nnatural_b_rows = [r for r in load_json(f'{condition_b_path}/../full_method_out.json')\n                  if r['metadata_fold_or_source'] == 'wmt25_task3_natural']\nassert len(natural_b_rows) == 320\n\n# --- Phase 1: mitigated real-COMET attempt (time-boxed to first ~3.0h of the 6h budget) ---\nattempts_log = []  # list of {timestamp, endpoint, mode, http_status, error, elapsed_s}\n\ndef try_comet_download(endpoint, resumable=True, timeout_s=900):\n    t0 = now()\n    try:\n        os.environ['HF_HUB_ENDPOINT'] = endpoint\n        # resumable=True relies on huggingface_hub's default etag/local-dir cache behavior:\n        # a partial prior attempt's blob is kept under HF cache and resumed, not discarded\n        path = huggingface_hub.snapshot_download(\n            repo_id='Unbabel/wmt22-cometkiwi-da',\n            local_dir='./hf_cache/wmt22-cometkiwi-da',\n            resume_download=resumable,\n            etag_timeout=30,\n        )\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'SUCCESS', 'elapsed_s': now()-t0})\n        return path\n    except HfHubHTTPError as e:\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': e.response.status_code,\n                              'error': str(e), 'elapsed_s': now()-t0})\n        return None\n    except Exception as e:\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'EXC', 'error': repr(e), 'elapsed_s': now()-t0})\n        return None\n\n# Genuinely new mitigations vs. the prior two failed attempts:\n# (a) an alternate mirror endpoint, (b) attempts spread ACROSS SEPARATE WINDOWS with real\n#     wall-clock gaps (not back-to-back exponential backoff within one process lifetime),\n#     so a per-minute or per-hour 429 window is actually crossed.\nENDPOINTS = ['https://huggingface.co', 'https://hf-mirror.com']\nWINDOW_OFFSETS_MIN = [0, 25, 75, 165]   # 4 windows inside a ~3h cap, deliberately spread\ncomet_checkpoint_path = None\nfor offset_min in WINDOW_OFFSETS_MIN:\n    sleep_until(run_start_time + offset_min * 60)\n    for endpoint in ENDPOINTS:\n        comet_checkpoint_path = try_comet_download(endpoint)\n        if comet_checkpoint_path:\n            break\n    if comet_checkpoint_path:\n        break\n    if elapsed_since(run_start_time) > 3.0 * 3600:\n        break  # hard stop: leave >=2.5h for fallback scoring + writeup, no matter what\n\nreal_comet_available = comet_checkpoint_path is not None\n\n# --- Phase 2a: REAL-COMET path ---\nif real_comet_available:\n    from comet import load_from_checkpoint\n    model = load_from_checkpoint(comet_checkpoint_path)\n    def comet_score(rows, text_field):\n        data = [{'src': r['source_text'], 'mt': r[text_field]} for r in rows]\n        out = model.predict(data, batch_size=64, gpus=1)\n        return out['scores']\n    pre_scores  = comet_score(natural_c_rows, 'pre_repair_text')\n    post_scores = comet_score(natural_c_rows, 'post_repair_text')\n    delta_comet_c = [post - pre for pre, post in zip(pre_scores, post_scores)]\n    result = {\n        'quality_metric_path_taken': 'real_wmt22_cometkiwi_da',\n        'attempts_log': attempts_log,\n        'condition_c_delta_comet_natural_pooled_mean': mean(delta_comet_c),\n        'condition_c_delta_comet_natural_per_row': delta_comet_c,\n        'condition_c_delta_comet_by_language_pair': groupby_mean(natural_c_rows, delta_comet_c, key='language_pair'),\n        'directly_comparable_to_C1_C2_real_comet_numbers': True,\n        'bootstrap_ci_delta_comet': paired_bootstrap_ci(delta_comet_c, n_boot=10000),\n    }\n\n# --- Phase 2b: FALLBACK path -- same proxy as Condition B, re-scoring BOTH B and C ---\nelse:\n    def proxy_score_pair(source_text, candidate_text, cfg):\n        # cfg = b_fidelity_config: same model id, same prompt template, same convention\n        prompt = cfg['prompt_template'].format(source=source_text, candidate=candidate_text)\n        resp = openrouter_call(model=cfg['model_id'], prompt=prompt,\n                                temperature=cfg['temperature'], system=cfg.get('system'))\n        return parse_score(resp, convention=cfg['scoring_convention'])\n\n    cumulative_cost_usd = 0.0\n    COST_CAP = 9.0  # hard stop below the $10 ceiling to leave margin\n\n    def scored_delta(rows, cfg):\n        nonlocal cumulative_cost_usd\n        deltas = []\n        for r in rows:\n            if cumulative_cost_usd > COST_CAP:\n                raise BudgetExceeded(cumulative_cost_usd)\n            pre = proxy_score_pair(r['source_text'], r['pre_repair_text'], cfg)\n            post = proxy_score_pair(r['source_text'], r['post_repair_text'], cfg)\n            cumulative_cost_usd += estimate_cost(cfg['model_id'], 2)  # 2 calls this row\n            deltas.append(post - pre)\n        return deltas\n\n    delta_proxy_b = scored_delta(natural_b_rows, b_fidelity_config)   # RE-score B, same run, same proxy\n    delta_proxy_c = scored_delta(natural_c_rows, b_fidelity_config)   # score C with IDENTICAL config\n\n    paired_bc = bootstrap_paired_difference(delta_proxy_c, delta_proxy_b, n_boot=10000)\n    result = {\n        'quality_metric_path_taken': 'llm_judge_proxy_fallback_identical_to_condition_B',\n        'attempts_log': attempts_log,\n        'proxy_config_used': b_fidelity_config,\n        'condition_b_proxy_delta_pooled_mean_natural_rerun': mean(delta_proxy_b),\n        'condition_c_proxy_delta_pooled_mean_natural': mean(delta_proxy_c),\n        'condition_c_minus_condition_b_proxy_delta_paired_bootstrap_ci': paired_bc,\n        'cumulative_openrouter_cost_usd': cumulative_cost_usd,\n        'directly_comparable_to_C1_C2_real_comet_numbers': False,\n        'directly_comparable_to': 'Condition B, same-proxy, same-run rescoring only',\n        'explicit_caveat': (\n            'Real wmt22-cometkiwi-da was unreachable after mitigated attempts across '\n            f'{len(WINDOW_OFFSETS_MIN)} time-separated windows and {len(ENDPOINTS)} endpoints '\n            '(see attempts_log). This number is an LLM-judge proxy, identical in model/prompt/'\n            'convention to Condition B\\'s fidelity check, and must NOT be treated as numerically '\n            'comparable to C1 or C2\\'s real-COMET \\u0394COMET figures.'\n        ),\n    }\n\n# --- Phase 3: write output, validate schema ---\nresult['schema_version'] = 'exp_eval... (use aii-json to validate against the repo experiment output schema)'\nwrite_json('method_out.json', result)\nrun_aii_json_validation('method_out.json')",
  "fallback_plan": "Layered fallbacks, in order of what can go wrong:\n1. If art_6n9zJVKWXnio or art_G9ppuk8aHUhW cannot be located anywhere under the run directory tree (renamed, moved, or genuinely absent), do NOT reconstruct their contents from the hypothesis text or fabricate row-level data. Instead write method_out.json with quality_metric_path_taken='blocked_missing_upstream_artifact', list every glob pattern tried, and stop -- this is a real data-availability finding worth reporting, not a excuse to skip validation.\n2. If Condition B's fidelity-check proxy config cannot be extracted verbatim from art_G9ppuk8aHUhW's own code (e.g. the prompt was inlined ad hoc and not saved as a reusable template), reconstruct it as literally as possible from that artifact's method_out.json plus any saved prompt/log fields, and explicitly flag reconstructed_from_partial_evidence=true in the output rather than silently presenting it as identical.\n3. If the real COMET checkpoint download succeeds but model.predict() fails at inference time (OOM, CUDA driver mismatch, corrupted partial download despite a 200 on manifest fetch), fall back immediately to CPU inference (gpus=0) before giving up on the real-metric path entirely -- 640 segments is small enough that CPU COMET inference (no throughput benchmark exists per the resource dossier, but architecture is a small XLM-R encoder) is very likely to finish within the remaining time budget even if slow.\n4. If the mirror endpoint (hf-mirror.com or any other reachable HF mirror discovered during Phase 1) also 429s or is unreachable entirely (DNS failure, org-blocked), record that explicitly as its own attempts_log entries -- a mirror being blocked is itself informative and should not be silently conflated with the primary endpoint's 429s.\n5. If even the proxy fallback blows past the $9 internal cost cap partway through (e.g., a pricier judge model than expected), stop scoring immediately, report partial results for however many rows completed under budget with n reported honestly (not padded or extrapolated), and mark condition_b_proxy_delta and condition_c_proxy_delta as PARTIAL with the exact n scored.\n6. If OpenRouter itself returns errors for the judge model (deprecated/delisted, mirroring the TowerPlus-9B and gemma-2-9b-it delisting pattern already seen twice in this project), re-verify the model id is still live via the aii-openrouter-llms skill's model search before assuming a transient error; if it is genuinely gone, use the resource dossier's or aii-openrouter-llms search to pick the closest still-available substitute, and flag this explicitly as a SECOND-DEGREE proxy deviation from B's original config (not silently swapped in).",
  "testing_plan": "1. Dry-run the artifact-location logic first, standalone: confirm find_artifact_dir resolves to real, readable files for both art_6n9zJVKWXnio and art_G9ppuk8aHUhW, and print the row counts and a sample row's keys from each before doing anything else -- this is the single most likely blocking failure and must be confirmed in the first few minutes, not discovered after burning time on COMET mitigation.\n2. Test the COMET download mitigation logic on a 2-minute time budget first (WINDOW_OFFSETS_MIN=[0] only, one endpoint) purely to confirm the retry/logging code runs without exceptions and produces a well-formed attempts_log entry, before committing to the full multi-hour spread -- this catches code bugs (wrong repo_id, wrong local_dir permissions, huggingface_hub API signature mismatch across versions) cheaply.\n3. Before running the full 320-row proxy fallback (which costs real OpenRouter money), test proxy_score_pair on exactly 3 hand-picked rows from Condition B's natural set and manually inspect the parsed scores against what B's own original fidelity-check output reports for those same rows if row-level scores are still available in art_G9ppuk8aHUhW's output -- if the reconstructed config produces materially different scores on rows B already scored, the config was not extracted correctly and must be fixed before spending on all 320+320 rows.\n4. Confirm cost estimation is realistic: after the 3-row test, compute actual OpenRouter spend from the API response's reported usage and extrapolate to 640 rows x 2 calls before greenlighting the full run; abort and pick a cheaper judge model if extrapolated cost would exceed the $9 cap.\n5. Only after both the artifact-location and small-scale proxy tests pass, run the full Phase 1 mitigation window schedule and, depending on its outcome, the full Phase 2a or 2b scoring pass; validate the final method_out.json with the aii-json skill before declaring done.\n6. Sanity-check the final numbers against known bounds regardless of which path was taken: COMET/proxy deltas should be small (roughly in [-1, 1] for a 0-1-scaled metric, or in whatever bounded range the chosen proxy's convention defines) -- a wildly out-of-range mean signals a parsing bug in parse_score(), not a real finding, and should be caught before reporting."
}
```

### [5] TOOL RESULT — Write · 2026-09-01 10:26:34 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Rescue Condition C's Missing Quality Score\",\n  \"summary\": \"Scoring-only rerun over Condition C's already-generated 320 natural-row repair outputs: attempt real wmt22-cometkiwi-da with genuinely new HF-429 mitigations (mirror endpoint, resumable download, widely-spaced retry windows, full attempt logging); if it still fails, fall back to the EXACT same LLM-judge proxy configuration used for Condition B's fidelity check, re-scoring B's own rows with that identical proxy in the same run so the output reports a same-proxy B-vs-C comparison rather than an isolated, incomparable number. No new repair generation and no new repair-model calls; this only scores text that already exists.\",\n  \"runpod_compute_profile\": \"gpu\",\n  \"implementation_pseudocode\": \"# --- Phase 0: locate inputs (no new generation) ---\\n# The direction names two upstream artifacts by id that are NOT in this plan's formal\\n# depends_on (only the dataset art_mhfmDpGp4z1J and the resource dossier art_5ySTX4YfxqG_\\n# are). They are prior-iteration artifacts in the SAME run and must be located on disk:\\nRUN_ROOT = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5'\\ndef find_artifact_dir(short_id):\\n    # short_id e.g. '6n9zJVKWXnio' or 'G9ppuk8aHUhW' (the part after 'art_')\\n    # search every iter_*/gen_art*/gen_art_*/ for a dir or meta file whose artifact id matches\\n    candidates = glob(f'{RUN_ROOT}/**/full_method_out.json', recursive=True) + \\\\\\n                 glob(f'{RUN_ROOT}/**/method_out.json', recursive=True)\\n    matches = [c for c in candidates if short_id in read_meta_near(c).get('artifact_id','')]\\n    if not matches: matches = [c for c in candidates if short_id in c]  # path-based fallback\\n    assert matches, f'BLOCKING: could not locate artifact art_{short_id} on disk'\\n    return matches[0]\\n\\ncondition_c_path = find_artifact_dir('6n9zJVKWXnio')   # full_method_out.json for Condition C (560 rows total)\\ncondition_b_path = find_artifact_dir('G9ppuk8aHUhW')   # Condition B artifact incl. its fidelity-check proxy config/code\\n\\ncondition_c_rows = json.load(open(condition_c_path))\\nnatural_c_rows = [r for r in condition_c_rows if r['metadata_fold_or_source'] == 'wmt25_task3_natural']\\nassert len(natural_c_rows) == 320, f'expected 320 natural rows, got {len(natural_c_rows)}'\\n# each row must carry: source_text, pre_repair_text (or original MT hyp), post_repair_text, language_pair, row_id\\n\\ncondition_b_artifact = load_artifact_bundle(condition_b_path)  # includes its .py source and full_method_out.json\\nb_fidelity_config = extract_fidelity_check_config(condition_b_artifact)\\n# b_fidelity_config MUST capture, verbatim from B's own code/prompt file:\\n#   - the exact OpenRouter model id used as judge\\n#   - the exact system/user prompt template (before/after adequacy scoring)\\n#   - the exact numeric scoring convention (scale, direction, aggregation)\\n#   - temperature / sampling params\\n# If b_fidelity_config cannot be extracted verbatim (code missing/renamed), STOP and\\n# record a blocking finding rather than inventing a proxy config from memory.\\nnatural_b_rows = [r for r in load_json(f'{condition_b_path}/../full_method_out.json')\\n                  if r['metadata_fold_or_source'] == 'wmt25_task3_natural']\\nassert len(natural_b_rows) == 320\\n\\n# --- Phase 1: mitigated real-COMET attempt (time-boxed to first ~3.0h of the 6h budget) ---\\nattempts_log = []  # list of {timestamp, endpoint, mode, http_status, error, elapsed_s}\\n\\ndef try_comet_download(endpoint, resumable=True, timeout_s=900):\\n    t0 = now()\\n    try:\\n        os.environ['HF_HUB_ENDPOINT'] = endpoint\\n        # resumable=True relies on huggingface_hub's default etag/local-dir cache behavior:\\n        # a partial prior attempt's blob is kept under HF cache and resumed, not discarded\\n        path = huggingface_hub.snapshot_download(\\n            repo_id='Unbabel/wmt22-cometkiwi-da',\\n            local_dir='./hf_cache/wmt22-cometkiwi-da',\\n            resume_download=resumable,\\n            etag_timeout=30,\\n        )\\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'SUCCESS', 'elapsed_s': now()-t0})\\n        return path\\n    except HfHubHTTPError as e:\\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': e.response.status_code,\\n                              'error': str(e), 'elapsed_s': now()-t0})\\n        return None\\n    except Exception as e:\\n        attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'EXC', 'error': repr(e), 'elapsed_s': now()-t0})\\n        return None\\n\\n# Genuinely new mitigations vs. the prior two failed attempts:\\n# (a) an alternate mirror endpoint, (b) attempts spread ACROSS SEPARATE WINDOWS with real\\n#     wall-clock gaps (not back-to-back exponential backoff within one process lifetime),\\n#     so a per-minute or per-hour 429 window is actually crossed.\\nENDPOINTS = ['https://huggingface.co', 'https://hf-mirror.com']\\nWINDOW_OFFSETS_MIN = [0, 25, 75, 165]   # 4 windows inside a ~3h cap, deliberately spread\\ncomet_checkpoint_path = None\\nfor offset_min in WINDOW_OFFSETS_MIN:\\n    sleep_until(run_start_time + offset_min * 60)\\n    for endpoint in ENDPOINTS:\\n        comet_checkpoint_path = try_comet_download(endpoint)\\n        if comet_checkpoint_path:\\n            break\\n    if comet_checkpoint_path:\\n        break\\n    if elapsed_since(run_start_time) > 3.0 * 3600:\\n        break  # hard stop: leave >=2.5h for fallback scoring + writeup, no matter what\\n\\nreal_comet_available = comet_checkpoint_path is not None\\n\\n# --- Phase 2a: REAL-COMET path ---\\nif real_comet_available:\\n    from comet import load_from_checkpoint\\n    model = load_from_checkpoint(comet_checkpoint_path)\\n    def comet_score(rows, text_field):\\n        data = [{'src': r['source_text'], 'mt': r[text_field]} for r in rows]\\n        out = model.predict(data, batch_size=64, gpus=1)\\n        return out['scores']\\n    pre_scores  = comet_score(natural_c_rows, 'pre_repair_text')\\n    post_scores = comet_score(natural_c_rows, 'post_repair_text')\\n    delta_comet_c = [post - pre for pre, post in zip(pre_scores, post_scores)]\\n    result = {\\n        'quality_metric_path_taken': 'real_wmt22_cometkiwi_da',\\n        'attempts_log': attempts_log,\\n        'condition_c_delta_comet_natural_pooled_mean': mean(delta_comet_c),\\n        'condition_c_delta_comet_natural_per_row': delta_comet_c,\\n        'condition_c_delta_comet_by_language_pair': groupby_mean(natural_c_rows, delta_comet_c, key='language_pair'),\\n        'directly_comparable_to_C1_C2_real_comet_numbers': True,\\n        'bootstrap_ci_delta_comet': paired_bootstrap_ci(delta_comet_c, n_boot=10000),\\n    }\\n\\n# --- Phase 2b: FALLBACK path -- same proxy as Condition B, re-scoring BOTH B and C ---\\nelse:\\n    def proxy_score_pair(source_text, candidate_text, cfg):\\n        # cfg = b_fidelity_config: same model id, same prompt template, same convention\\n        prompt = cfg['prompt_template'].format(source=source_text, candidate=candidate_text)\\n        resp = openrouter_call(model=cfg['model_id'], prompt=prompt,\\n                                temperature=cfg['temperature'], system=cfg.get('system'))\\n        return parse_score(resp, convention=cfg['scoring_convention'])\\n\\n    cumulative_cost_usd = 0.0\\n    COST_CAP = 9.0  # hard stop below the $10 ceiling to leave margin\\n\\n    def scored_delta(rows, cfg):\\n        nonlocal cumulative_cost_usd\\n        deltas = []\\n        for r in rows:\\n            if cumulative_cost_usd > COST_CAP:\\n                raise BudgetExceeded(cumulative_cost_usd)\\n            pre = proxy_score_pair(r['source_text'], r['pre_repair_text'], cfg)\\n            post = proxy_score_pair(r['source_text'], r['post_repair_text'], cfg)\\n            cumulative_cost_usd += estimate_cost(cfg['model_id'], 2)  # 2 calls this row\\n            deltas.append(post - pre)\\n        return deltas\\n\\n    delta_proxy_b = scored_delta(natural_b_rows, b_fidelity_config)   # RE-score B, same run, same proxy\\n    delta_proxy_c = scored_delta(natural_c_rows, b_fidelity_config)   # score C with IDENTICAL config\\n\\n    paired_bc = bootstrap_paired_difference(delta_proxy_c, delta_proxy_b, n_boot=10000)\\n    result = {\\n        'quality_metric_path_taken': 'llm_judge_proxy_fallback_identical_to_condition_B',\\n        'attempts_log': attempts_log,\\n        'proxy_config_used': b_fidelity_config,\\n        'condition_b_proxy_delta_pooled_mean_natural_rerun': mean(delta_proxy_b),\\n        'condition_c_proxy_delta_pooled_mean_natural': mean(delta_proxy_c),\\n        'condition_c_minus_condition_b_proxy_delta_paired_bootstrap_ci': paired_bc,\\n        'cumulative_openrouter_cost_usd': cumulative_cost_usd,\\n        'directly_comparable_to_C1_C2_real_comet_numbers': False,\\n        'directly_comparable_to': 'Condition B, same-proxy, same-run rescoring only',\\n        'explicit_caveat': (\\n            'Real wmt22-cometkiwi-da was unreachable after mitigated attempts across '\\n            f'{len(WINDOW_OFFSETS_MIN)} time-separated windows and {len(ENDPOINTS)} endpoints '\\n            '(see attempts_log). This number is an LLM-judge proxy, identical in model/prompt/'\\n            'convention to Condition B\\\\'s fidelity check, and must NOT be treated as numerically '\\n            'comparable to C1 or C2\\\\'s real-COMET \\\\u0394COMET figures.'\\n        ),\\n    }\\n\\n# --- Phase 3: write output, validate schema ---\\nresult['schema_version'] = 'exp_eval... (use aii-json to validate against the repo experiment output schema)'\\nwrite_json('method_out.json', result)\\nrun_aii_json_validation('method_out.json')\",\n  \"fallback_plan\": \"Layered fallbacks, in order of what can go wrong:\\n1. If art_6n9zJVKWXnio or art_G9ppuk8aHUhW cannot be located anywhere under the run directory tree (renamed, moved, or genuinely absent), do NOT reconstruct their contents from the hypothesis text or fabricate row-level data. Instead write method_out.json with quality_metric_path_taken='blocked_missing_upstream_artifact', list every glob pattern tried, and stop -- this is a real data-availability finding worth reporting, not a excuse to skip validation.\\n2. If Condition B's fidelity-check proxy config cannot be extracted verbatim from art_G9ppuk8aHUhW's own code (e.g. the prompt was inlined ad hoc and not saved as a reusable template), reconstruct it as literally as possible from that artifact's method_out.json plus any saved prompt/log fields, and explicitly flag reconstructed_from_partial_evidence=true in the output rather than silently presenting it as identical.\\n3. If the real COMET checkpoint download succeeds but model.predict() fails at inference time (OOM, CUDA driver mismatch, corrupted partial download despite a 200 on manifest fetch), fall back immediately to CPU inference (gpus=0) before giving up on the real-metric path entirely -- 640 segments is small enough that CPU COMET inference (no throughput benchmark exists per the resource dossier, but architecture is a small XLM-R encoder) is very likely to finish within the remaining time budget even if slow.\\n4. If the mirror endpoint (hf-mirror.com or any other reachable HF mirror discovered during Phase 1) also 429s or is unreachable entirely (DNS failure, org-blocked), record that explicitly as its own attempts_log entries -- a mirror being blocked is itself informative and should not be silently conflated with the primary endpoint's 429s.\\n5. If even the proxy fallback blows past the $9 internal cost cap partway through (e.g., a pricier judge model than expected), stop scoring immediately, report partial results for however many rows completed under budget with n reported honestly (not padded or extrapolated), and mark condition_b_proxy_delta and condition_c_proxy_delta as PARTIAL with the exact n scored.\\n6. If OpenRouter itself returns errors for the judge model (deprecated/delisted, mirroring the TowerPlus-9B and gemma-2-9b-it delisting pattern already seen twice in this project), re-verify the model id is still live via the aii-openrouter-llms skill's model search before assuming a transient error; if it is genuinely gone, use the resource dossier's or aii-openrouter-llms search to pick the closest still-available substitute, and flag this explicitly as a SECOND-DEGREE proxy deviation from B's original config (not silently swapped in).\",\n  \"testing_plan\": \"1. Dry-run the artifact-location logic first, standalone: confirm find_artifact_dir resolves to real, readable files for both art_6n9zJVKWXnio and art_G9ppuk8aHUhW, and print the row counts and a sample row's keys from each before doing anything else -- this is the single most likely blocking failure and must be confirmed in the first few minutes, not discovered after burning time on COMET mitigation.\\n2. Test the COMET download mitigation logic on a 2-minute time budget first (WINDOW_OFFSETS_MIN=[0] only, one endpoint) purely to confirm the retry/logging code runs without exceptions and produces a well-formed attempts_log entry, before committing to the full multi-hour spread -- this catches code bugs (wrong repo_id, wrong local_dir permissions, huggingface_hub API signature mismatch across versions) cheaply.\\n3. Before running the full 320-row proxy fallback (which costs real OpenRouter money), test proxy_score_pair on exactly 3 hand-picked rows from Condition B's natural set and manually inspect the parsed scores against what B's own original fidelity-check output reports for those same rows if row-level scores are still available in art_G9ppuk8aHUhW's output -- if the reconstructed config produces materially different scores on rows B already scored, the config was not extracted correctly and must be fixed before spending on all 320+320 rows.\\n4. Confirm cost estimation is realistic: after the 3-row test, compute actual OpenRouter spend from the API response's reported usage and extrapolate to 640 rows x 2 calls before greenlighting the full run; abort and pick a cheaper judge model if extrapolated cost would exceed the $9 cap.\\n5. Only after both the artifact-location and small-scale proxy tests pass, run the full Phase 1 mitigation window schedule and, depending on its outcome, the full Phase 2a or 2b scoring pass; validate the final method_out.json with the aii-json skill before declaring done.\\n6. Sanity-check the final numbers against known bounds regardless of which path was taken: COMET/proxy deltas should be small (roughly in [-1, 1] for a 0-1-scaled metric, or in whatever bounded range the chosen proxy's convention defines) -- a wildly out-of-range mean signals a parsing bug in parse_score(), not a real finding, and should be caught before reporting.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-09-01 10:26:38 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — it's a scoring-only rerun over Condition C's existing 320 natural-row outputs: a mitigated real-COMET download attempt (mirror endpoint, resumable download, time-spread retry windows, full attempt logging), falling back if that still 429s to the exact same LLM-judge proxy config used for Condition B's fidelity check, re-scoring B alongside C in the same run so the two numbers are directly comparable, with explicit non-comparability caveats to C1/C2 if the fallback path is taken.
```
