# gen_plan_experiment_2 — test_idea

> Phase: `invention_loop` · round 5 · `gen_plan`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_2` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 10:24:43 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_2
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

id: experiment_iter5_dir2
type: experiment
objective: >-
  Test the paper's own proposed remedy for Condition C's collapsed certificate rate -- a wider pass budget -- while tracking
  per-pass checker false-positive rate on ground-truth-labeled injected rows, so the result can distinguish 'more passes let
  genuine repairs converge' from 'more passes let checker noise churn the sentence without net improvement,' exactly as the
  reviewer requested.
approach: >-
  Reuse Condition C's checker, repair model (google/gemma-3-12b-it), OpenRouter client, and row selection verbatim from art_6n9zJVKWXnio,
  changing only MAX_PASSES from 3 to 6 (matching TEaR's own ablation range, already cited in this paper's related work). Run
  on the same 320 natural + 240 injected-pool rows. At every pass, in addition to the existing fix/regression/certificate
  bookkeeping, compute a per-pass checker false-positive count on the injected-pool rows specifically: for any row where the
  checker re-flags an invariant category that is NOT the row's own known-corrupted category and that category's pre-repair
  state was already correct per the dataset's ground truth, log it as a checker false-positive re-flag (using the same ground-truth
  spans the checker validation in art_QLpPxaqf1VzK/art_7Uc5PlFctjXi already established). Report, per pass number (1 through
  6): certificate rate reached by that pass, cumulative true regression rate, cumulative fix rate, and the false-positive
  re-flag rate -- so the paper can show whether certificate rate keeps climbing with more passes (supporting a budget-ceiling
  explanation) or plateaus while false-positive re-flags keep accumulating (supporting a checker-noise explanation). Also
  report edit volume at 6 passes versus 3, to check whether the wider budget pushes Condition C toward full-retranslation
  levels the original 3-pass version avoided. Keep this run within a small pre-declared sub-budget (following C2/C's own $2
  pilot-probe convention) against the shared $10 ceiling.
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

### [4] TOOL CALL — Glob · 2026-09-01 10:24:59 UTC

```
Pattern: "**/full_data_out.json"
```

### [5] TOOL RESULT — Glob · 2026-09-01 10:24:59 UTC

```
{"filenames": ["/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json"], "durationMs": 22, "numFiles": 1, "truncated": false, "totalMatches": 1, "countIsComplete": true}
```

### [6] TOOL CALL — Glob · 2026-09-01 10:24:59 UTC

```
Pattern: "**/*"
```

### [7] TOOL RESULT — Glob · 2026-09-01 10:24:59 UTC

```
{"filenames": [".repl_agent.ptylog"], "durationMs": 25, "numFiles": 1, "truncated": false, "totalMatches": 1, "countIsComplete": true}
```

### [8] TOOL CALL — Read · 2026-09-01 10:25:03 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json
```

### [9] TOOL RESULT — Read · 2026-09-01 10:25:03 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json", "content": "{\n  \"metadata\": {\n    \"title\": \"WMT25 Translation Error-Correction Data\",\n    \"natural_source\": \"wmt-conference/wmt25-mteval GitHub repo, data/testset/wmt25_task3_combined_test_set.tsv, WMT25 Task 3 official test set (6 en->X language pairs x 1000 segments = 6000 rows), released 2025-07-24, https://www2.statmt.org/wmt25/mteval-subtask.html\",\n    \"injected_source\": \"google/wmt24pp (HuggingFace), WMT24++: Expanding the Language Coverage of WMT24 to 55 Languages & Dialects (arXiv:2502.12404); human post-edited target text used as the clean base for programmatic corruption, wholly disjoint corpus/year from the WMT25 Task3 natural component\",\n    \"language_pairs\": [\n      \"en-cs_CZ\",\n      \"en-is_IS\",\n      \"en-ja_JP\",\n      \"en-ru_RU\",\n      \"en-uk_UA\",\n      \"en-zh_CN\"\n    ],\n    \"invariant_categories\": [\n      \"named_entity_swap\",\n      \"number_unit_date_alteration\",\n      \"negation_polarity_flip\",\n      \"quantifier_substitution\"\n    ],\n    \"metadata_fold_values\": [\n      \"experimental_pool\",\n      \"checker_validation_heldout\"\n    ],\n    \"known_gap\": \"No public post-hoc human MQM severity/type gold layer for WMT25 Task 3 was found (post_edit column of the official release is empty for all 6000 rows); qe_flagged_spans (CometKiwi-derived) is used as the operational localization signal instead, per the plan's documented fallback. named_entity_swap recall is lower for zh_CN/ja_JP because those scripts carry no capitalization signal -- entities are only detected via embedded Latin-script substrings, a documented NER-tooling coverage gap rather than a full multilingual-NER pass. named_entity_swap for cs_CZ/is_IS/ru_RU/uk_UA uses a capitalization heuristic (no spaCy/HF NER model available offline), filtered by a per-language function-word stoplist, a sentence-boundary-capitalization exclusion, and a corpus-frequency cap (a real proper noun recurs rarely across ~960 rows; a capitalized function word recurs often) -- this removes the large majority of false positives but is not equivalent to true NER, so a small residual fraction of named_entity_swap rows may swap a capitalized common word rather than a genuine entity; downstream consumers relying on exact entity-type precision should treat this category's rows as heuristic-screened, not gold-verified.\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"wmt25_task3_natural\",\n      \"examples\": [\n        {\n          \"input\": \"But not Dave Portnoy. The founder and owner of Barstool Sports - the Utne Reader for the light-domestic-swilling, backslapping, Zyn-packing, parlay-chasing American male - Portnoy has long been treated as an avatar for everything that elite media is not. Barstool might be considered the outermost ring of the so-called manosphere, the vast realm of male-oriented alternative media that has been credited with the rightward drift of the young male vote. Portnoy - a Trump supporter with a long history of misogynistic comments and bullying, who has been accused of nonconsensually filming women during uncomfortably rough sex - doesn't exactly run away from that label. (He has denied the claims about sexual misconduct and filed a suit against the outlet that published them; it was dismissed.) And what he noticed about the photos of Belichick and Hudson was the clutch Hudson wore, which was shaped like a little football: \\\"Very cool purse from BB's girlfriend,\\\" he posted on X. \\\"Football girlfriend purse.\\\"\",\n          \"output\": \"但戴夫·波特诺伊不是这样的。作为Barstool Sports——一本专为热爱啤酒、爱拍马屁、惯于用ZYN解压、喜欢押注的美国男性而设的杂志——的创始者兼所有者，波特诺伊一直被视为精英媒体所不具备的一切的化身。Barstool可以被视为所谓“男权文化圈”的最外层，这是一片以男性为导向的另类媒体的广阔领域，这些媒体被认为促成了年轻男性选票向右倾的趋势。波特诺伊——一位有长期发表女性歧视言论和欺凌行为的特朗普支持者——曾被指控在激烈性交过程中未经同意拍摄女性的视频——他对这个标签并不避讳。（他否认了关于性行为不端的指控，并对发布这些指控的媒体提起诉讼；该诉讼被驳回了。）而他对贝利奇克和哈德森照片的留意点是哈德森戴的手链，形状像一个小橄榄球：“BB女友的手袋真酷。”他在X上发帖说，“橄榄球女女友手袋。”\",\n          \"metadata_language_pair\": \"en-zh_CN\",\n          \"metadata_domain\": \"news\",\n          \"metadata_qe_flagged_spans\": [\n            {\n              \"start_i\": 3,\n              \"end_i\": 4,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 5,\n              \"end_i\": 13,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 16,\n              \"end_i\": 31,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 37,\n              \"end_i\": 60,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 82,\n              \"end_i\": 83,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 90,\n              \"end_i\": 92,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 94,\n              \"end_i\": 101,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 105,\n              \"end_i\": 113,\n              \"severity\": \"critical\"\n            },\n            {\n              \"start_i\": 121,\n              \"end_i\": 125,\n              \"severity\": \"critical\"\n            },", "numLines": 80, "startLine": 1, "totalLines": 476634}}
```

### [10] TOOL CALL — Grep · 2026-09-01 10:25:09 UTC

```
Pattern: ""dataset": "injected_error_augmentation""
```

### [11] TOOL RESULT — Grep · 2026-09-01 10:25:09 UTC

```
{"mode": "content", "numFiles": 0, "filenames": [], "content": "416173:      \"dataset\": \"injected_error_augmentation\",", "numLines": 1, "totalLines": 1}
```

### [12] TOOL CALL — Glob · 2026-09-01 10:25:09 UTC

```
Pattern: "**/preview_data_out.json"
```

### [13] TOOL RESULT — Glob · 2026-09-01 10:25:09 UTC

```
{"filenames": ["/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/preview_data_out.json"], "durationMs": 38, "numFiles": 1, "truncated": false, "totalMatches": 1, "countIsComplete": true}
```

### [14] TOOL CALL — Read · 2026-09-01 10:25:13 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json
```

### [15] TOOL RESULT — Read · 2026-09-01 10:25:13 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json", "content": "      \"dataset\": \"injected_error_augmentation\",\n      \"examples\": [\n        {\n          \"input\": \"Moscow maintains that such laws violate the rights of Russian-speaking people, who make up around half of Ukraine's population. Russian Foreign Ministry spokeswoman Maria Zakharova said in February that Kiev's \\\"discriminatory campaign\\\" against the language was growing more and more \\\"indignant.\\\" In a survey conducted last September by the Kiev International Institute of Sociology, respondents cited language discrimination as the most common type of prejudice in Ukraine, with 45% saying it was a problem.\",\n          \"output\": \"Moskva tvrdí, že tyto zákony porušují práva rusky mluvících obyvatel, kteří tvoří okolo poloviny ukrajinského obyvatelstva. Ve studii Kyjevského mezinárodního sociologického institutu z minulého září respondenti uvádí, že jazyková diskriminace je nejběžnějším typem předsudků na Cohenovi, a 45 % tvrdí, že to je problém.\",\n          \"metadata_language_pair\": \"en-cs_CZ\",\n          \"metadata_domain\": \"news\",\n          \"metadata_qe_flagged_spans\": null,\n          \"metadata_human_error_annotations\": null,\n          \"metadata_provenance\": \"injected\",\n          \"metadata_invariant_category\": \"named_entity_swap\",\n          \"metadata_source_dataset\": \"google/wmt24pp\",\n          \"metadata_doc_id\": \"test-en-news_rt.com.54499\",\n          \"metadata_segment_id\": 77,\n          \"metadata_system_id\": null,\n          \"metadata_overall_qe_score\": null,\n          \"metadata_clean_target_text\": \"Moskva tvrdí, že tyto zákony porušují práva rusky mluvících obyvatel, kteří tvoří okolo poloviny ukrajinského obyvatelstva. Ve studii Kyjevského mezinárodního sociologického institutu z minulého září respondenti uvádí, že jazyková diskriminace je nejběžnějším typem předsudků na Ukrajině, a 45 % tvrdí, že to je problém.\",\n          \"metadata_original_span\": \"Ukrajině\",\n          \"metadata_corrupted_span\": \"Cohenovi\",\n          \"metadata_span_offsets\": {\n            \"start\": 279,\n            \"end\": 287\n          },\n          \"metadata_notes\": \"Programmatically corrupted from a held-out wmt24pp (google/wmt24pp, WMT24++ human post-edited target, a corpus wholly disjoint from the WMT25 Task 3 test set used for the natural component) clean reference. Category=named_entity_swap. Ground truth = metadata_clean_target_text.\",\n          \"metadata_fold\": \"experimental_pool\"\n        },\n        {\n          \"input\": \"Moscow maintains that such laws violate the rights of Russian-speaking people, who make up around half of Ukraine's population. Russian Foreign Ministry spokeswoman Maria Zakharova said in February that Kiev's \\\"discriminatory campaign\\\" against the language was growing more and more \\\"indignant.\\\" In a survey conducted last September by the Kiev International Institute of Sociology, respondents cited language discrimination as the most common type of prejudice in Ukraine, with 45% saying it was a problem.\",\n          \"output\": \"Moskva tvrdí, že tyto zákony porušují práva rusky mluvících obyvatel, kteří tvoří okolo poloviny ukrajinského obyvatelstva. Ve studii Kyjevského mezinárodního sociologického institutu z minulého září respondenti uvádí, že jazyková diskriminace je nejběžnějším typem předsudků na Ukrajině, a 55 % tvrdí, že to je problém.\",\n          \"metadata_language_pair\": \"en-cs_CZ\",\n          \"metadata_domain\": \"news\",\n          \"metadata_qe_flagged_spans\": null,\n          \"metadata_human_error_annotations\": null,\n          \"metadata_provenance\": \"injected\",\n          \"metadata_invariant_category\": \"number_unit_date_alteration\",\n          \"metadata_source_dataset\": \"google/wmt24pp\",\n          \"metadata_doc_id\": \"test-en-news_rt.com.54499\",\n          \"metadata_segment_id\": 77,\n          \"metadata_system_id\": null,\n          \"metadata_overall_qe_score\": null,", "numLines": 40, "startLine": 416173, "totalLines": 476634}}
```

### [16] ASSISTANT · 2026-09-01 10:26:32 UTC

```
Good, I have enough concrete field-level detail now. Let me write the plan.
```

### [17] TOOL CALL — Write · 2026-09-01 10:26:32 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_2/.terminal_claude_agent_struct_out.json

{
  "title": "Wider Repair Budget: More Passes or More Noise?",
  "summary": "Re-run Condition C (broad checker localization + iterative repair-and-reverify) with MAX_PASSES raised from 3 to 6 on the identical 560-row population (320 natural + 240 injected-pool), reusing the checker, repair model (google/gemma-3-12b-it), and OpenRouter client verbatim. The new instrumentation is a per-pass, per-row checker false-positive re-flag counter computed only on injected-pool rows against their known ground truth (metadata_clean_target_text / metadata_invariant_category / metadata_corrupted_span from art_mhfmDpGp4z1J's injected_error_augmentation dataset). Reporting per pass number 1-6: certificate rate, cumulative true (human/ground-truth-confirmed) regression rate, cumulative fix rate, and false-positive re-flag rate, plus edit volume at 6 vs 3 passes -- to let the paper distinguish 'certificate rate keeps climbing (budget-ceiling explanation)' from 'certificate rate plateaus while false-positive re-flags accumulate (checker-noise explanation)'.",
  "runpod_compute_profile": "cpu_light",
  "implementation_pseudocode": "# File: method.py (uv inline script; pin the SAME pyproject deps art_6n9zJVKWXnio's Condition C used --\n# httpx/requests for OpenRouter, loguru, pydantic if used for the checker; do NOT re-derive versions,\n# copy them from that artifact's lockfile/pyproject header if reachable, else from art_5ySTX4YfxqG_'s\n# resource dossier recommended-model table).\n\nimport json, time, random\nfrom pathlib import Path\nfrom loguru import logger\n\nMAX_PASSES = 6                     # was 3 in Condition C -- the ONLY loop-budget change\nREPAIR_MODEL = \"google/gemma-3-12b-it\"   # fixed, matches B/D/C1/C2/C exactly -- no model swap\nSUB_BUDGET_USD = 2.00              # pre-declared sub-budget vs the shared $10 ceiling\nCHECKPOINT_PATH = Path(\"checkpoint_c6.jsonl\")\nHEARTBEAT_PATH = Path(\"heartbeat_c6.json\")\n\n# ---------- 1. Load exact same 560-row population as Condition C ----------\n# Load art_mhfmDpGp4z1J/data_out/full_data_out.json.\n# natural pool: dataset==\"wmt25_task3_natural\", metadata_fold==\"experimental_pool\" --\n#   select the SAME 320 rows Condition C used. If art_6n9zJVKWXnio's method_out.json or its\n#   input row-id list is readable, load that exact id list (row identity = doc/segment/system id\n#   tuple, or whatever key that artifact persisted) so the comparison is apples-to-apples.\n#   If the exact row-id list is not recoverable, reproduce it deterministically: same fixed\n#   random seed (reuse Condition C's seed value, documented in its method.py header) applied to\n#   the same filtered pool in the same order -- log a WARNING and flag\n#   \"row_selection_reconstructed=true\" in output metadata if reconstruction, not reuse, was used.\n# injected pool: dataset==\"injected_error_augmentation\", metadata_fold==\"experimental_pool\" --\n#   same 240-row selection logic (up to the per-category/per-language cap already used).\nnatural_rows = load_condition_c_natural_rows()   # 320 rows, exact reuse or seeded reconstruction\ninjected_rows = load_condition_c_injected_rows()  # 240 rows, carries ground truth fields\nall_rows = natural_rows + injected_rows          # 560 total\n\n# ---------- 2. Reuse checker + repair call verbatim from Condition C's code ----------\n# Import or copy (do not reimplement) art_6n9zJVKWXnio's:\n#   - run_checker(sentence, lang) -> list[Violation(category, span, severity)]\n#   - repair_span(sentence, violation, model=REPAIR_MODEL) -> str   (OpenRouter call)\n#   - localize_broad(sentence, lang) -> list[Violation]  (the C-specific checker-driven,\n#     not QE-span-only, localization used by C1/C, per Table 1's per-cell eligibility gating)\n# Any deviation in checker logic between this run and Condition C invalidates the comparison,\n# so diff the checker module's source hash against Condition C's before running; abort and log\n# a hard error if they differ instead of silently proceeding.\n\n# ---------- 3. Per-row iterate-to-certificate loop, now instrumented per pass ----------\ndef run_condition_c6(row):\n    lang = row[\"metadata_language_pair\"]\n    sentence = row[\"output\"]              # current translation, mutates across passes\n    pre_repair_violations = run_checker(sentence, lang)   # pass-0 baseline flags\n    is_injected = row[\"metadata_provenance\"] == \"injected\"\n    known_category = row.get(\"metadata_invariant_category\")      # e.g. \"number_unit_date_alteration\"\n    ground_truth_text = row.get(\"metadata_clean_target_text\")     # only present for injected rows\n\n    pass_log = []   # one entry per pass: {pass_num, n_flags, certificate, fixed_ids, regressed_ids, fp_reflags}\n    prior_state = {v.category: True for v in [] }  # track per-category correctness before each pass\n    # initialize per-category correctness from pre_repair_violations vs ground truth (injected rows only)\n\n    for pass_num in range(1, MAX_PASSES + 1):\n        violations = localize_broad(sentence, lang)     # Condition C's broad localization, re-run each pass\n        if not violations:\n            pass_log.append(make_pass_record(pass_num, certificate=True, n_flags=0,\n                                              fixed=[], regressed=[], fp_reflags=[]))\n            break   # certificate reached -- stop iterating, matches C's original stopping rule\n\n        # --- false-positive re-flag instrumentation (injected rows only) ---\n        # A checker re-flag is a FP re-flag iff:\n        #   (a) row is injected (ground truth known),\n        #   (b) the flagged violation's category != row's OWN known_category (i.e. the checker is\n        #       re-flagging a category that was never corrupted in this row), AND\n        #   (c) that category's span, compared against ground_truth_text, was ALREADY correct\n        #       before this pass's repair edit (i.e. no genuine violation existed there pre-pass).\n        # This directly operationalizes art_QLpPxaqf1VzK/art_7Uc5PlFctjXi's checker validation\n        # ground truth spans -- do not re-derive precision/recall, import their per-language,\n        # per-category precision table and cross-reference by (language_pair, category).\n        fp_reflags = []\n        if is_injected:\n            for v in violations:\n                if v.category != known_category:\n                    if category_was_correct_pre_pass(sentence_before_this_pass, v.category,\n                                                       ground_truth_text, lang):\n                        fp_reflags.append(v)\n\n        repaired_sentence = sentence\n        fixed_this_pass, regressed_this_pass = [], []\n        for v in violations:\n            candidate = repair_span(repaired_sentence, v, model=REPAIR_MODEL)\n            repaired_sentence = candidate\n        # re-check after this pass's batch of edits to compute fixed/regressed sets\n        post_edit_violations = run_checker(repaired_sentence, lang)\n        fixed_this_pass = [v for v in violations if v.category not in\n                            {p.category for p in post_edit_violations}]\n        # true regression = a category that was CORRECT before this pass (per ground truth for\n        # injected rows, per human_error_annotations / checker-validated state for natural rows)\n        # and is VIOLATED after -- score only against the human/ground-truth-confirmed layer,\n        # never against raw re-flags, exactly as C1/C2/C's true_regression_rate was scored.\n        regressed_this_pass = compute_true_regressions(sentence, repaired_sentence, lang,\n                                                         is_injected, ground_truth_text)\n\n        pass_log.append(make_pass_record(pass_num, certificate=False,\n                                          n_flags=len(violations),\n                                          fixed=fixed_this_pass,\n                                          regressed=regressed_this_pass,\n                                          fp_reflags=fp_reflags))\n        sentence = repaired_sentence\n\n    edit_volume = compute_edit_distance(row[\"output\"], sentence) / len(row[\"output\"])\n    return {\n        \"row_id\": row_identity(row),\n        \"final_sentence\": sentence,\n        \"pass_log\": pass_log,           # full per-pass trace, 1..min(MAX_PASSES, stop_pass)\n        \"certificate_reached\": pass_log[-1][\"certificate\"],\n        \"stop_pass\": len(pass_log),\n        \"edit_volume\": edit_volume,\n    }\n\n# ---------- 4. Robustness infrastructure, reused from Condition C's validated design ----------\n# - Per-row checkpointing: append each row's result to CHECKPOINT_PATH as one JSON line\n#   immediately after run_condition_c6(row) returns; on restart, skip row_ids already checkpointed.\n# - Per-call timeout + retry: wrap every OpenRouter call (checker LLM calls, if any, and repair_span)\n#   in a timeout (e.g. 60s) with exponential backoff, max 4 attempts, matching C's validated pattern.\n# - Heartbeat: write HEARTBEAT_PATH with {last_row_index, timestamp, cumulative_cost_usd} every\n#   10 rows, so a stall is visible without re-deriving Condition C's crash-recovery design from scratch.\n# - Cost tracking: sum OpenRouter usage.cost (or token counts x published price) after every call;\n#   hard-stop (raise, checkpoint, exit cleanly) if cumulative_cost_usd > SUB_BUDGET_USD, logging\n#   which rows were completed vs skipped due to budget exhaustion.\n\n# ---------- 5. Aggregate per-pass-number report across all 560 rows ----------\nfor pass_num in range(1, MAX_PASSES + 1):\n    rows_still_active_at_pass_num = [r for r in results if r[\"stop_pass\"] >= pass_num]\n    cert_rate_by_pass_num = fraction_with_certificate_by(pass_num, results)\n    cumulative_fix_rate_by_pass_num = ...\n    cumulative_true_regression_rate_by_pass_num = ...\n    fp_reflag_rate_by_pass_num = (\n        sum(len(r[\"pass_log\"][pass_num-1][\"fp_reflags\"]) for r in results if len(r[\"pass_log\"]) >= pass_num)\n        / sum(r[\"pass_log\"][pass_num-1][\"n_flags\"] for r in results if len(r[\"pass_log\"]) >= pass_num and r[\"pass_log\"][pass_num-1][\"n_flags\"] > 0)\n    )\n    # bootstrap 95% CI (1000 resamples, same method as C1 vs C2's paired-bootstrap CIs) on each rate\n\n# ---------- 6. Compare 6-pass run against the ORIGINAL 3-pass Condition C ----------\n# Load art_6n9zJVKWXnio/method_out.json's Condition C results directly (do not re-simulate them).\n# Report side by side at pass=3 (this run's pass-3 cumulative numbers) vs the ORIGINAL 3-pass run's\n# final numbers, as an internal consistency check -- they should closely match (same checker, same\n# model, same rows, only difference is whether the loop was told it COULD continue past pass 3, which\n# should not change pass-1..3 behavior since the loop only knows a budget, not the outcome).\n# A material mismatch here (e.g. >0.05 absolute difference in pass-3 fix rate) signals a checker\n# hash mismatch or row-selection drift and must be investigated BEFORE trusting the pass-4..6 numbers.\n\n# ---------- 7. Edit volume at 6 vs 3 passes ----------\n# edit_volume_6pass = mean over 560 rows of edit_distance(original_output, final_sentence_at_pass6)/len\n# edit_volume_3pass = same quantity truncating each row's trace at its pass-3 state (or original C's\n# recorded edit_volume=0.022, whichever is more directly comparable) -- report the ratio and an\n# explicit flag if edit_volume_6pass exceeds ~0.5 (i.e., roughly half the sentence rewritten),\n# the threshold this hypothesis line treats as 'approaching full retranslation'.\n\nwrite_json(\"method_out.json\", {\n    \"per_pass_report\": [...],   # pass 1..6: certificate_rate, cum_fix_rate, cum_true_regression_rate,\n                                  #            fp_reflag_rate, each with bootstrap CI\n    \"pass3_consistency_check\": {...},   # this run's pass-3 numbers vs original Condition C's numbers\n    \"edit_volume\": {\"at_3_passes\": ..., \"at_6_passes\": ..., \"ratio\": ...},\n    \"interpretation_signal\": \"budget_ceiling\" | \"checker_noise\" | \"ambiguous\",  # computed, not asserted:\n        # budget_ceiling if certificate_rate keeps rising >=X% between pass 4-6 while fp_reflag_rate\n        # stays flat or falls; checker_noise if certificate_rate plateaus (<X% rise) while fp_reflag_rate\n        # keeps rising; ambiguous otherwise -- state the exact numeric thresholds used, do not hand-wave\n    \"cost_usd\": cumulative_cost_usd,\n    \"row_selection_reconstructed\": bool,\n    \"n_rows\": 560,\n})",
  "fallback_plan": "(1) If art_6n9zJVKWXnio's exact 320+240 row-id list or checker source is not locatable/readable, do NOT silently resample -- deterministically reconstruct via the same documented seed and filtering rule from that artifact's method.py header (natural: experimental_pool fold, first-N under seed; injected: experimental_pool fold, same per-category/per-language cap), log row_selection_reconstructed=true, and treat the pass-3 consistency check (step 6) as the acceptance gate: if pass-3 numbers from this run diverge from the original Condition C's reported numbers by more than 0.05 absolute on fix rate or true regression rate, stop, report the divergence explicitly as a scope-limiting caveat, and do NOT present pass 4-6 results as continuous with C's original 3-pass results -- report them as a fresh, standalone 6-pass run instead. (2) If OpenRouter cost tracking shows the sub-budget ($2) will be exceeded before finishing all 560 rows at 6 passes, reduce scope in this order: first drop to the 240 injected-pool rows only (since the false-positive instrumentation, the artifact's core new contribution, only applies there and natural rows only support the certificate/fix/regression side already measured in Condition C), then if still over budget reduce MAX_PASSES to 5, documenting exactly which reduction was applied and why. (3) If the Hugging Face Hub / wmt22-cometkiwi-da checkpoint access failure recurs (documented twice already, Condition B and Condition C both hit HTTP 429), do NOT attempt a third different uncalibrated proxy -- this artifact does not need COMET at all (its scope is fix/regression/certificate/false-positive rates, not ΔCOMET), so simply omit any quality-axis metric entirely rather than compounding the cross-condition-comparability problem the hypothesis already flags as unresolved; state this omission explicitly in the output metadata as a deliberate scope decision, not a failure. (4) If category_was_correct_pre_pass (comparing an injected row's non-corrupted-category span against ground truth) proves ambiguous for some category/language combinations (e.g. quantifier_scope in uk_UA, already flagged in the hypothesis as not checker-verified for that pair), restrict the false-positive re-flag computation to only the categories/languages Table 1 marks as genuinely checker-localized-and-verified (number_unit_date across both languages, quantifier_scope in ru_RU only) and state this restricted scope explicitly rather than computing a noisy or misleading rate over ineligible cells. (5) If per-row checkpointing/heartbeat infrastructure from Condition C is not directly reusable (different file layout, different row identity scheme), reimplement the same three primitives (per-row JSONL checkpoint, per-call timeout+retry with exponential backoff, periodic heartbeat file) rather than skipping them -- Condition C's mid-run crash was real, not hypothetical, and a 6-pass run has strictly more LLM calls per row than the 3-pass run that crashed.",
  "testing_plan": "Before the 560-row run: (1) Smoke-test on 3 rows (1 natural, 2 injected covering 2 different invariant categories) at MAX_PASSES=6, verifying the loop actually runs to 6 passes when violations persist (not silently capped at 3 by a stale constant copied from Condition C's code) and that pass_log has exactly stop_pass entries with monotonically non-increasing n_flags in the typical case. (2) Verify checker source-hash match against Condition C's checker module explicitly fails loudly (raises, does not warn-and-continue) if the two differ, since a silent mismatch would invalidate every downstream comparison. (3) On the same 3-row smoke test, manually inspect one false-positive-re-flag classification end to end -- pick one row, print its known_category, the flagged categories at each pass, and the ground-truth comparison result for each non-matching category -- to confirm the fp_reflags logic is not systematically over- or under-counting (e.g. check it doesn't flag a category that was never checkable for that row's language per Table 1's eligibility gating). (4) Scale to 20 rows (10 natural + 10 injected, spanning at least 3 of the 4 invariant categories and at least 3 of the 6 language pairs) and confirm cost-per-row extrapolates to comfortably under the $2 sub-budget at 560 rows and 6 passes (worst case: 560 x 6 x cost-per-repair-call, using art_5ySTX4YfxqG_'s live OpenRouter pricing for google/gemma-3-12b-it) -- if the extrapolation exceeds budget, apply the fallback-plan scope reduction BEFORE the full run, not after. (5) Confirm the pass-3 consistency check (step 6) is computable at this 20-row scale by cross-referencing against the corresponding 20 rows' pass-3 state in the original Condition C's method_out.json, and that the values are close (not necessarily identical, given any nondeterminism in the repair model's sampling) -- treat this as the go/no-go signal before committing the full sub-budget to the 560-row, 6-pass run. Only after (1)-(5) pass does the full run proceed, and it must run under the checkpoint/heartbeat infrastructure from the start (not bolted on after a crash), given Condition C's own history of a real mid-run failure."
}
```

### [18] TOOL RESULT — Write · 2026-09-01 10:26:32 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_plan/gen_plan_experiment_2/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Wider Repair Budget: More Passes or More Noise?\",\n  \"summary\": \"Re-run Condition C (broad checker localization + iterative repair-and-reverify) with MAX_PASSES raised from 3 to 6 on the identical 560-row population (320 natural + 240 injected-pool), reusing the checker, repair model (google/gemma-3-12b-it), and OpenRouter client verbatim. The new instrumentation is a per-pass, per-row checker false-positive re-flag counter computed only on injected-pool rows against their known ground truth (metadata_clean_target_text / metadata_invariant_category / metadata_corrupted_span from art_mhfmDpGp4z1J's injected_error_augmentation dataset). Reporting per pass number 1-6: certificate rate, cumulative true (human/ground-truth-confirmed) regression rate, cumulative fix rate, and false-positive re-flag rate, plus edit volume at 6 vs 3 passes -- to let the paper distinguish 'certificate rate keeps climbing (budget-ceiling explanation)' from 'certificate rate plateaus while false-positive re-flags accumulate (checker-noise explanation)'.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"implementation_pseudocode\": \"# File: method.py (uv inline script; pin the SAME pyproject deps art_6n9zJVKWXnio's Condition C used --\\n# httpx/requests for OpenRouter, loguru, pydantic if used for the checker; do NOT re-derive versions,\\n# copy them from that artifact's lockfile/pyproject header if reachable, else from art_5ySTX4YfxqG_'s\\n# resource dossier recommended-model table).\\n\\nimport json, time, random\\nfrom pathlib import Path\\nfrom loguru import logger\\n\\nMAX_PASSES = 6                     # was 3 in Condition C -- the ONLY loop-budget change\\nREPAIR_MODEL = \\\"google/gemma-3-12b-it\\\"   # fixed, matches B/D/C1/C2/C exactly -- no model swap\\nSUB_BUDGET_USD = 2.00              # pre-declared sub-budget vs the shared $10 ceiling\\nCHECKPOINT_PATH = Path(\\\"checkpoint_c6.jsonl\\\")\\nHEARTBEAT_PATH = Path(\\\"heartbeat_c6.json\\\")\\n\\n# ---------- 1. Load exact same 560-row population as Condition C ----------\\n# Load art_mhfmDpGp4z1J/data_out/full_data_out.json.\\n# natural pool: dataset==\\\"wmt25_task3_natural\\\", metadata_fold==\\\"experimental_pool\\\" --\\n#   select the SAME 320 rows Condition C used. If art_6n9zJVKWXnio's method_out.json or its\\n#   input row-id list is readable, load that exact id list (row identity = doc/segment/system id\\n#   tuple, or whatever key that artifact persisted) so the comparison is apples-to-apples.\\n#   If the exact row-id list is not recoverable, reproduce it deterministically: same fixed\\n#   random seed (reuse Condition C's seed value, documented in its method.py header) applied to\\n#   the same filtered pool in the same order -- log a WARNING and flag\\n#   \\\"row_selection_reconstructed=true\\\" in output metadata if reconstruction, not reuse, was used.\\n# injected pool: dataset==\\\"injected_error_augmentation\\\", metadata_fold==\\\"experimental_pool\\\" --\\n#   same 240-row selection logic (up to the per-category/per-language cap already used).\\nnatural_rows = load_condition_c_natural_rows()   # 320 rows, exact reuse or seeded reconstruction\\ninjected_rows = load_condition_c_injected_rows()  # 240 rows, carries ground truth fields\\nall_rows = natural_rows + injected_rows          # 560 total\\n\\n# ---------- 2. Reuse checker + repair call verbatim from Condition C's code ----------\\n# Import or copy (do not reimplement) art_6n9zJVKWXnio's:\\n#   - run_checker(sentence, lang) -> list[Violation(category, span, severity)]\\n#   - repair_span(sentence, violation, model=REPAIR_MODEL) -> str   (OpenRouter call)\\n#   - localize_broad(sentence, lang) -> list[Violation]  (the C-specific checker-driven,\\n#     not QE-span-only, localization used by C1/C, per Table 1's per-cell eligibility gating)\\n# Any deviation in checker logic between this run and Condition C invalidates the comparison,\\n# so diff the checker module's source hash against Condition C's before running; abort and log\\n# a hard error if they differ instead of silently proceeding.\\n\\n# ---------- 3. Per-row iterate-to-certificate loop, now instrumented per pass ----------\\ndef run_condition_c6(row):\\n    lang = row[\\\"metadata_language_pair\\\"]\\n    sentence = row[\\\"output\\\"]              # current translation, mutates across passes\\n    pre_repair_violations = run_checker(sentence, lang)   # pass-0 baseline flags\\n    is_injected = row[\\\"metadata_provenance\\\"] == \\\"injected\\\"\\n    known_category = row.get(\\\"metadata_invariant_category\\\")      # e.g. \\\"number_unit_date_alteration\\\"\\n    ground_truth_text = row.get(\\\"metadata_clean_target_text\\\")     # only present for injected rows\\n\\n    pass_log = []   # one entry per pass: {pass_num, n_flags, certificate, fixed_ids, regressed_ids, fp_reflags}\\n    prior_state = {v.category: True for v in [] }  # track per-category correctness before each pass\\n    # initialize per-category correctness from pre_repair_violations vs ground truth (injected rows only)\\n\\n    for pass_num in range(1, MAX_PASSES + 1):\\n        violations = localize_broad(sentence, lang)     # Condition C's broad localization, re-run each pass\\n        if not violations:\\n            pass_log.append(make_pass_record(pass_num, certificate=True, n_flags=0,\\n                                              fixed=[], regressed=[], fp_reflags=[]))\\n            break   # certificate reached -- stop iterating, matches C's original stopping rule\\n\\n        # --- false-positive re-flag instrumentation (injected rows only) ---\\n        # A checker re-flag is a FP re-flag iff:\\n        #   (a) row is injected (ground truth known),\\n        #   (b) the flagged violation's category != row's OWN known_category (i.e. the checker is\\n        #       re-flagging a category that was never corrupted in this row), AND\\n        #   (c) that category's span, compared against ground_truth_text, was ALREADY correct\\n        #       before this pass's repair edit (i.e. no genuine violation existed there pre-pass).\\n        # This directly operationalizes art_QLpPxaqf1VzK/art_7Uc5PlFctjXi's checker validation\\n        # ground truth spans -- do not re-derive precision/recall, import their per-language,\\n        # per-category precision table and cross-reference by (language_pair, category).\\n        fp_reflags = []\\n        if is_injected:\\n            for v in violations:\\n                if v.category != known_category:\\n                    if category_was_correct_pre_pass(sentence_before_this_pass, v.category,\\n                                                       ground_truth_text, lang):\\n                        fp_reflags.append(v)\\n\\n        repaired_sentence = sentence\\n        fixed_this_pass, regressed_this_pass = [], []\\n        for v in violations:\\n            candidate = repair_span(repaired_sentence, v, model=REPAIR_MODEL)\\n            repaired_sentence = candidate\\n        # re-check after this pass's batch of edits to compute fixed/regressed sets\\n        post_edit_violations = run_checker(repaired_sentence, lang)\\n        fixed_this_pass = [v for v in violations if v.category not in\\n                            {p.category for p in post_edit_violations}]\\n        # true regression = a category that was CORRECT before this pass (per ground truth for\\n        # injected rows, per human_error_annotations / checker-validated state for natural rows)\\n        # and is VIOLATED after -- score only against the human/ground-truth-confirmed layer,\\n        # never against raw re-flags, exactly as C1/C2/C's true_regression_rate was scored.\\n        regressed_this_pass = compute_true_regressions(sentence, repaired_sentence, lang,\\n                                                         is_injected, ground_truth_text)\\n\\n        pass_log.append(make_pass_record(pass_num, certificate=False,\\n                                          n_flags=len(violations),\\n                                          fixed=fixed_this_pass,\\n                                          regressed=regressed_this_pass,\\n                                          fp_reflags=fp_reflags))\\n        sentence = repaired_sentence\\n\\n    edit_volume = compute_edit_distance(row[\\\"output\\\"], sentence) / len(row[\\\"output\\\"])\\n    return {\\n        \\\"row_id\\\": row_identity(row),\\n        \\\"final_sentence\\\": sentence,\\n        \\\"pass_log\\\": pass_log,           # full per-pass trace, 1..min(MAX_PASSES, stop_pass)\\n        \\\"certificate_reached\\\": pass_log[-1][\\\"certificate\\\"],\\n        \\\"stop_pass\\\": len(pass_log),\\n        \\\"edit_volume\\\": edit_volume,\\n    }\\n\\n# ---------- 4. Robustness infrastructure, reused from Condition C's validated design ----------\\n# - Per-row checkpointing: append each row's result to CHECKPOINT_PATH as one JSON line\\n#   immediately after run_condition_c6(row) returns; on restart, skip row_ids already checkpointed.\\n# - Per-call timeout + retry: wrap every OpenRouter call (checker LLM calls, if any, and repair_span)\\n#   in a timeout (e.g. 60s) with exponential backoff, max 4 attempts, matching C's validated pattern.\\n# - Heartbeat: write HEARTBEAT_PATH with {last_row_index, timestamp, cumulative_cost_usd} every\\n#   10 rows, so a stall is visible without re-deriving Condition C's crash-recovery design from scratch.\\n# - Cost tracking: sum OpenRouter usage.cost (or token counts x published price) after every call;\\n#   hard-stop (raise, checkpoint, exit cleanly) if cumulative_cost_usd > SUB_BUDGET_USD, logging\\n#   which rows were completed vs skipped due to budget exhaustion.\\n\\n# ---------- 5. Aggregate per-pass-number report across all 560 rows ----------\\nfor pass_num in range(1, MAX_PASSES + 1):\\n    rows_still_active_at_pass_num = [r for r in results if r[\\\"stop_pass\\\"] >= pass_num]\\n    cert_rate_by_pass_num = fraction_with_certificate_by(pass_num, results)\\n    cumulative_fix_rate_by_pass_num = ...\\n    cumulative_true_regression_rate_by_pass_num = ...\\n    fp_reflag_rate_by_pass_num = (\\n        sum(len(r[\\\"pass_log\\\"][pass_num-1][\\\"fp_reflags\\\"]) for r in results if len(r[\\\"pass_log\\\"]) >= pass_num)\\n        / sum(r[\\\"pass_log\\\"][pass_num-1][\\\"n_flags\\\"] for r in results if len(r[\\\"pass_log\\\"]) >= pass_num and r[\\\"pass_log\\\"][pass_num-1][\\\"n_flags\\\"] > 0)\\n    )\\n    # bootstrap 95% CI (1000 resamples, same method as C1 vs C2's paired-bootstrap CIs) on each rate\\n\\n# ---------- 6. Compare 6-pass run against the ORIGINAL 3-pass Condition C ----------\\n# Load art_6n9zJVKWXnio/method_out.json's Condition C results directly (do not re-simulate them).\\n# Report side by side at pass=3 (this run's pass-3 cumulative numbers) vs the ORIGINAL 3-pass run's\\n# final numbers, as an internal consistency check -- they should closely match (same checker, same\\n# model, same rows, only difference is whether the loop was told it COULD continue past pass 3, which\\n# should not change pass-1..3 behavior since the loop only knows a budget, not the outcome).\\n# A material mismatch here (e.g. >0.05 absolute difference in pass-3 fix rate) signals a checker\\n# hash mismatch or row-selection drift and must be investigated BEFORE trusting the pass-4..6 numbers.\\n\\n# ---------- 7. Edit volume at 6 vs 3 passes ----------\\n# edit_volume_6pass = mean over 560 rows of edit_distance(original_output, final_sentence_at_pass6)/len\\n# edit_volume_3pass = same quantity truncating each row's trace at its pass-3 state (or original C's\\n# recorded edit_volume=0.022, whichever is more directly comparable) -- report the ratio and an\\n# explicit flag if edit_volume_6pass exceeds ~0.5 (i.e., roughly half the sentence rewritten),\\n# the threshold this hypothesis line treats as 'approaching full retranslation'.\\n\\nwrite_json(\\\"method_out.json\\\", {\\n    \\\"per_pass_report\\\": [...],   # pass 1..6: certificate_rate, cum_fix_rate, cum_true_regression_rate,\\n                                  #            fp_reflag_rate, each with bootstrap CI\\n    \\\"pass3_consistency_check\\\": {...},   # this run's pass-3 numbers vs original Condition C's numbers\\n    \\\"edit_volume\\\": {\\\"at_3_passes\\\": ..., \\\"at_6_passes\\\": ..., \\\"ratio\\\": ...},\\n    \\\"interpretation_signal\\\": \\\"budget_ceiling\\\" | \\\"checker_noise\\\" | \\\"ambiguous\\\",  # computed, not asserted:\\n        # budget_ceiling if certificate_rate keeps rising >=X% between pass 4-6 while fp_reflag_rate\\n        # stays flat or falls; checker_noise if certificate_rate plateaus (<X% rise) while fp_reflag_rate\\n        # keeps rising; ambiguous otherwise -- state the exact numeric thresholds used, do not hand-wave\\n    \\\"cost_usd\\\": cumulative_cost_usd,\\n    \\\"row_selection_reconstructed\\\": bool,\\n    \\\"n_rows\\\": 560,\\n})\",\n  \"fallback_plan\": \"(1) If art_6n9zJVKWXnio's exact 320+240 row-id list or checker source is not locatable/readable, do NOT silently resample -- deterministically reconstruct via the same documented seed and filtering rule from that artifact's method.py header (natural: experimental_pool fold, first-N under seed; injected: experimental_pool fold, same per-category/per-language cap), log row_selection_reconstructed=true, and treat the pass-3 consistency check (step 6) as the acceptance gate: if pass-3 numbers from this run diverge from the original Condition C's reported numbers by more than 0.05 absolute on fix rate or true regression rate, stop, report the divergence explicitly as a scope-limiting caveat, and do NOT present pass 4-6 results as continuous with C's original 3-pass results -- report them as a fresh, standalone 6-pass run instead. (2) If OpenRouter cost tracking shows the sub-budget ($2) will be exceeded before finishing all 560 rows at 6 passes, reduce scope in this order: first drop to the 240 injected-pool rows only (since the false-positive instrumentation, the artifact's core new contribution, only applies there and natural rows only support the certificate/fix/regression side already measured in Condition C), then if still over budget reduce MAX_PASSES to 5, documenting exactly which reduction was applied and why. (3) If the Hugging Face Hub / wmt22-cometkiwi-da checkpoint access failure recurs (documented twice already, Condition B and Condition C both hit HTTP 429), do NOT attempt a third different uncalibrated proxy -- this artifact does not need COMET at all (its scope is fix/regression/certificate/false-positive rates, not ΔCOMET), so simply omit any quality-axis metric entirely rather than compounding the cross-condition-comparability problem the hypothesis already flags as unresolved; state this omission explicitly in the output metadata as a deliberate scope decision, not a failure. (4) If category_was_correct_pre_pass (comparing an injected row's non-corrupted-category span against ground truth) proves ambiguous for some category/language combinations (e.g. quantifier_scope in uk_UA, already flagged in the hypothesis as not checker-verified for that pair), restrict the false-positive re-flag computation to only the categories/languages Table 1 marks as genuinely checker-localized-and-verified (number_unit_date across both languages, quantifier_scope in ru_RU only) and state this restricted scope explicitly rather than computing a noisy or misleading rate over ineligible cells. (5) If per-row checkpointing/heartbeat infrastructure from Condition C is not directly reusable (different file layout, different row identity scheme), reimplement the same three primitives (per-row JSONL checkpoint, per-call timeout+retry with exponential backoff, periodic heartbeat file) rather than skipping them -- Condition C's mid-run crash was real, not hypothetical, and a 6-pass run has strictly more LLM calls per row than the 3-pass run that crashed.\",\n  \"testing_plan\": \"Before the 560-row run: (1) Smoke-test on 3 rows (1 natural, 2 injected covering 2 different invariant categories) at MAX_PASSES=6, verifying the loop actually runs to 6 passes when violations persist (not silently capped at 3 by a stale constant copied from Condition C's code) and that pass_log has exactly stop_pass entries with monotonically non-increasing n_flags in the typical case. (2) Verify checker source-hash match against Condition C's checker module explicitly fails loudly (raises, does not warn-and-continue) if the two differ, since a silent mismatch would invalidate every downstream comparison. (3) On the same 3-row smoke test, manually inspect one false-positive-re-flag classification end to end -- pick one row, print its known_category, the flagged categories at each pass, and the ground-truth comparison result for each non-matching category -- to confirm the fp_reflags logic is not systematically over- or under-counting (e.g. check it doesn't flag a category that was never checkable for that row's language per Table 1's eligibility gating). (4) Scale to 20 rows (10 natural + 10 injected, spanning at least 3 of the 4 invariant categories and at least 3 of the 6 language pairs) and confirm cost-per-row extrapolates to comfortably under the $2 sub-budget at 560 rows and 6 passes (worst case: 560 x 6 x cost-per-repair-call, using art_5ySTX4YfxqG_'s live OpenRouter pricing for google/gemma-3-12b-it) -- if the extrapolation exceeds budget, apply the fallback-plan scope reduction BEFORE the full run, not after. (5) Confirm the pass-3 consistency check (step 6) is computable at this 20-row scale by cross-referencing against the corresponding 20 rows' pass-3 state in the original Condition C's method_out.json, and that the values are close (not necessarily identical, given any nondeterminism in the repair model's sampling) -- treat this as the go/no-go signal before committing the full sub-budget to the 560-row, 6-pass run. Only after (1)-(5) pass does the full run proceed, and it must run under the checkpoint/heartbeat infrastructure from the start (not bolted on after a crash), given Condition C's own history of a real mid-run failure.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [19] ASSISTANT · 2026-09-01 10:26:35 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json`. It details a 6-pass rerun of Condition C reusing the checker/model/rows verbatim, with new per-pass false-positive re-flag instrumentation on the injected-pool ground-truth rows, a pass-3 internal consistency check against the original 3-pass run, edit-volume tracking, and explicit fallbacks for row-selection recovery, budget overrun, the recurring COMET-checkpoint access failure, and checker-eligibility scope limits.
```
