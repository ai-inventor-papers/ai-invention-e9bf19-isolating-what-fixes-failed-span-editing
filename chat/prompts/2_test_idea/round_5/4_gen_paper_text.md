# gen_paper_text — test_idea

> Phase: `invention_loop` · round 5 · `gen_paper_text`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 10:49:50 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Introduction

Machine translation systems increasingly ship with an automatic quality-estimation (QE) step that flags likely errors in a translation without needing a human reference [1]. The natural next question is whether those flags can drive automatic repair: instead of retranslating a whole sentence to fix one wrong number or dropped negation, an editing system could touch only the flagged span and leave the rest of the sentence -- which the base translator already got right -- untouched. This is *scoped editing*: localize a problem with QE, then repair only that region. Scoped editing matters because a system that regenerates an entire sentence can silently break a correct number, name, or negation while fixing something else, and the total-sentence quality metrics used to score MT systems do not distinguish "improved and stayed faithful" from "improved by chance while corrupting a different part of the sentence" [2]. In a regulated, terminology-heavy domain -- legal, medical, financial translation -- a single flipped number or negation is a severe, auditable failure independent of whether the sentence's aggregate quality score went up.

The 2025 WMT shared task on automated translation evaluation (Task 3, minimal editing) gave scoped editing its first head-to-head test against full retranslation [3]. A scoped-editing system that masks each QE-flagged span with a placeholder token and fills it with one pass of a small language model finished dead last among eight ranked systems, at $-0.0108$ mean $\Delta$COMET, while a second, independently built scoped-editing system in the same ranking landed near break-even [3,4]. Two prior iterations of this project separated the design space of that losing system into two independently switchable factors -- *localization breadth* (how much of the sentence a checker is allowed to flag) and *iteration* (whether a flagged repair is re-checked and re-repaired) -- and executed three of the resulting four conditions plus a hygiene-only control: broadening localization alone in a single uncorrected pass (Condition C1) cut the reproduced quality loss roughly fivefold in $\Delta$COMET terms, but at a real cost, with fix rate on injected errors falling from 0.98 to 0.61 and true regression rate rising from 0.07 to 0.14 relative to the narrow-localization baselines; iterating alone, holding localization narrow (Condition C2), recovered that fix-rate and regression-rate cost almost completely, but did not itself move $\Delta$COMET. The fourth condition -- broadened localization combined with iteration (Condition C) -- was the one design point that could show whether these two gains combine, and it stalled during its first execution attempt, producing no output. The previous iteration reported this honestly as an unresolved infrastructure failure rather than an estimate or a negative result, leaving the protocol's central, motivating question exactly where it started: does combining both levers capture both gains at once?

This iteration answers that question, and the answer is a clear disconfirmation rather than the "best of both" outcome the original hypothesis anticipated. Condition C now runs to completion, on the identical 320 natural and 240 injected-error rows, repair model, and four-category checker used by every prior condition, under new run-robustness infrastructure -- per-row incremental checkpointing, per-call timeouts with retry, and heartbeat logging -- built specifically against the stall that killed the prior attempt. That infrastructure was tested for real, not only in principle: this iteration's own first attempt at Condition C also crashed mid-sweep, and the checkpointing let the run resume from exactly where it stopped and finish cleanly, losing no completed work. On the correctness axes that are fully and comparably measured, combining both levers does not combine their gains. Condition C's fix rate (0.628 on the 180 rows every condition can attempt) sits between broadened-localization-alone's 0.606 and iteration-alone's 0.989, matching neither strength. Its true regression rate (0.217) is not merely uncorrected -- it is the highest of all five conditions tested, exceeding broadened localization alone (0.139) and more than tripling iteration alone (0.072). The mechanism is visible in a metric no prior condition in this protocol needed: certificate rate, the fraction of rows that reach a verified, zero-flag state within the pass budget, collapses from iteration alone's 0.917 to 0.267 once the checker's surface broadens to match Condition C1's scope -- most sentences under Condition C never finish being repaired within three passes, and a partially repaired sentence is the worst state a checker-gated loop can leave a translation in.

We could not close the paper's remaining evidentiary gap on the quality axis specifically: Condition C's $\Delta$COMET could not be scored with the real `wmt22-cometkiwi-da` checkpoint used by every other condition in this protocol, because Hugging Face Hub returned HTTP 429 on all twelve retry attempts across two separate backoff probes during this run -- the second time in this project that COMET-checkpoint access has failed during execution, a pattern now worth flagging rather than treating as two unrelated incidents. A substitute proxy metric was used instead and is reported, but is explicitly not comparable in scale or sign convention to the real-COMET numbers reported for B, D, C1, and C2, so the paper's quality-axis verdict for Condition C remains undetermined by metric substitution, not by a stalled run. What is now established is that the protocol's central hypothesis -- that broadened localization and iteration are complementary levers whose combination would recover both a quality gain and a correctness gain -- fails on the two axes fully measured, and that failure has an identified mechanism: a broadened checker inside a fixed-budget iteration loop trades certification for coverage.

**Summary of contributions.**

- The first executed run of Condition C -- broadened localization combined with iterative checker-gated repair -- to completion on the identical 560-row population, repair model, and checker as every prior condition in this protocol, recovering from a mid-run crash via new checkpointing, timeout-and-retry, and heartbeat infrastructure that lost no completed progress, demonstrating the robustness fix under real, not simulated, failure conditions (Section 6.6).
- Direct evidence that combining broadened localization with iteration does not combine their separately measured gains: Condition C's fix rate lands between the two single-lever conditions without matching either, and its true regression rate is the worst of all five conditions tested, with the mechanism traced to a collapsed certificate rate -- most sentences never reach a verified state within the shared three-pass budget once the checker's surface broadens (Section 6.6).
- An honest accounting of a second COMET-checkpoint access failure in this project, disclosing that Condition C's $\Delta$COMET figure uses a non-comparable substitute metric rather than silently presenting it alongside the real-COMET figures from B, D, C1, and C2 (Section 6.6).
- A full reconciliation of the reviewer-flagged fix-rate-advantage discrepancy between a 240-row paired-bootstrap figure ($+0.2875$) and a 180-row table figure ($+0.3833$) for the same C2-versus-C1 comparison, with the negation-deletion denominator difference stated as the quantified explanation rather than left for the reader to reconstruct (Section 6.4).
- A literal, checked zero-overlap verification that this paper's quality evidence (320 natural rows) and correctness evidence (240 injected-pool rows) are scored on disjoint populations, replacing an inferred property with a computed fact (Section 6.5).
- A targeted literature search that surfaces the closest prior ablation to this protocol's iteration-versus-breadth separation -- an iteration-count-only ablation that itself found repeated refinement can hurt translation quality -- and narrows this paper's novelty claim accordingly, from "first" to a scoped, differentiated statement (Section 3).

# Related Work

**Quality-estimation-informed post-editing.** Automatic post-editing systems that use word-level QE as a training signal jointly train an encoder-decoder that regenerates the full target sentence in every variant; adding the QE signal reduces over-correction (18.30 vs. 19.39 TER) but never freezes a QE-clean span, so the model can still rewrite text no error was ever flagged in [5]. A later system replaces the auxiliary-signal approach with Grid Beam Search, forcing QE-tagged "OK" spans as lexical constraints while the decoder keeps freedom to reorder and rephrase around them; this is closer to scoped editing in spirit but is a soft constraint on regeneration rather than a frozen, iteratively verified span, and the paper's own oracle-versus-predicted-tag gap of 0.3-1.3 TER shows the method's ceiling is set by QE tag accuracy without isolating that dependency as a separate factor [6]. Prompting large language models directly with structured error annotations improves post-editing outcomes over unstructured feedback, but every condition in that study still regenerates the sentence and none tests a repair-then-verify loop against a single-pass repair with the same signal [7]. A related line automatically predicts MQM-style error spans and post-edits with them inside an LLM-as-judge evaluation pipeline, again as a one-shot correction step [10]. A third WMT25 Task 3 submission generates a natural-language explanation of each QE-flagged error with the xTower explanation model and hands that explanation to a large language model as the correction prompt [28]; like every system reviewed here, it regenerates the flagged segment in a single pass with no re-verification step.

**Iteration count as a standalone factor.** A targeted search for prior work that separates localization breadth from iteration count as two independently varied factors -- run for this iteration, using query terms this project's earlier related-work survey never used ("iterative QE-guided post-editing," "checker-in-the-loop machine translation repair," "verify-and-repair span editing translation") -- surfaces one closer prior ablation than any previously cited here. TEaR runs an estimate-and-refine loop for LLM-based machine translation and reports an explicit ablation over the number of refinement rounds, one through five, holding its estimation mechanism fixed across every round [29]. Its own Appendix D experiment on WMT23 Chinese-English finds that repeated iteration can *hurt* translation performance relative to a single round -- a one-dimensional, iteration-only finding that varies the same factor Condition C2 isolates, but never varies localization breadth as a second, separately controlled factor. Neither of the two closest WMT25 Task 3 submissions bundles or separates the two factors this protocol does: Padmanabhan (2025) is training-free and single-pass throughout, with no iteration loop of any kind [4]; Sharma (2025)'s xTower-explanation-then-correction pipeline also runs exactly once per segment [28]. On the strength of this search, we narrow this paper's earlier, stronger novelty claim: we are not aware of prior work in machine-translation automatic post-editing or scoped span editing that holds localization breadth and iteration apart as two independently varied, separately measured factors the way this protocol's C1-vs-C2-vs-C design does, though the closest analogue -- TEaR's iteration-count ablation -- independently supports this paper's own finding that more refinement rounds do not monotonically help, from a design that never tested whether broadening what is checked changes that picture.

**Localized and energy-guided editing.** Locate-and-edit approaches to controlled text generation obtain a full generation from a base model, then use an energy function to find and replace only the spans that violate a stated constraint, explicitly to avoid the semantic drift full regeneration under a constraint tends to introduce [11]. This is the closest existing mechanism to the localization half of our design, but it has not been applied to machine translation and has not been evaluated with localization breadth and iteration held apart as separately controlled factors.

**Iterative self-refinement.** Self-Refine shows that a single language model can generate an output, critique its own output, and revise it over several rounds without external supervision, improving results on tasks from code optimization to dialogue response generation [8]. Condition C2 and Condition C both iterate against a deterministic, non-learned checker rather than the repair model's own judgment, precisely to avoid the known unreliability of a model critiquing its own errors. Our results complicate the general expectation that more refinement rounds monotonically help, in two distinct ways now rather than one: C2 shows iteration against an external, deterministic verifier reliably fixes the specific things the verifier checks without improving a downstream metric it was never checking, and Condition C shows that broadening what the verifier checks, inside the same fixed-budget iteration loop, can make the loop worse at the very thing it is meant to guarantee -- a verified, certified output -- because most sentences no longer reach certification within the budget at all.

**Counterexample-guided synthesis.** Counterexample-Guided Inductive Synthesis (CEGIS) is a synthesis loop in which a candidate is checked against a specification by a verifier that either certifies it or returns a concrete counterexample scoping the next candidate, terminating on an explicit certificate rather than a fixed budget [9]. We do not claim to import CEGIS as a synthesis algorithm; our checker's "counterexample" is a flagged span, not a candidate-generalizing constraint, and nothing in our design performs unrealizability reasoning or generalizes across counterexamples. What we borrow is narrower -- the separation of concerns between what a verifier is allowed to see (localization breadth) and whether the loop runs more than once (iteration) -- and Condition C is the first executed test of both factors combined; the closer methodological kin for the mechanism this paper tests are the iterative-refinement and locate-and-edit lines above. Condition C's collapsed certificate rate under a fixed pass budget is a concrete illustration of exactly the risk CEGIS's certificate-or-counterexample loop is designed around: a budget-capped loop that broadens its own checked surface can spend its entire budget without ever reaching the certificate state CEGIS treats as the only acceptable termination condition.

**Evaluation infrastructure.** All $\Delta$COMET figures for Conditions B, D, C1, and C2 in this paper are computed with the same reference-free quality-estimation checkpoint the shared task uses, `wmt22-cometkiwi-da` [2]. Condition C's natural-row quality metric this iteration uses a substitute proxy score, disclosed in Section 6.6, because that checkpoint was not reachable from Hugging Face Hub during this run. Our natural-error data is WMT25 Task 3's released test set [3]; our injected-error data is built from WMT24++, a disjoint, human-post-edited multilingual corpus spanning 55 languages and dialects [14].

# Preliminaries

We define four terms used throughout the protocol.

A **content invariant** is a piece of source-sentence meaning -- a named entity, a number, unit, or date, a negation polarity marker, or a quantifier -- that must survive translation, and that can be checked deterministically (via named-entity recognition, regular expressions, cue-word lists, or alignment) rather than judged by a learned model. We check four invariant categories: entity identity, number/unit/date value, negation polarity, and quantifier scope.

A translation's **certificate** is the state in which every content invariant extracted from its source sentence has been checked and passes. Conditions C2 and C stop iterating as soon as a repair passes the checker (certificate reached) or a fixed pass budget is exhausted, whichever comes first; **certificate rate** is the fraction of rows that reach this state within the budget, distinct from *fix rate*, which credits a row whenever its specific ground-truth-corrupted invariant is repaired regardless of whether every other invariant in the sentence also passes.

**Localization breadth** is how much of the sentence a system is allowed to flag as needing repair. *Narrow* localization repairs only the span the original quality-estimation model flagged (Conditions B, D, and C2); *broad* localization repairs every invariant our checker finds violated, whether or not quality estimation flagged it (Conditions C1 and C).

**Iteration** is whether a flagged span, once repaired, is re-checked and re-repaired if it still fails, up to a fixed pass budget, or whether the system accepts a single repair pass unconditionally. Conditions B, D, and C1 use a single, uncorrected pass; C2 and C iterate.

# Method

## Design Rationale

Our method isolates localization from verification by construction: it fixes the repair model identically across every condition that performs a repair, and it varies localization breadth and iteration as two independently switchable factors rather than one bundled toggle, giving a two-by-two design (narrow/broad $\times$ single-pass/iterated) plus a hygiene-only control. Prior iterations established the two single-lever effects: broadening localization alone (C1) moves $\Delta$COMET substantially but costs fix rate and true regression rate; iterating alone, holding localization narrow (C2), recovers that correctness cost without moving $\Delta$COMET. This iteration completes the design's fourth cell -- both levers engaged at once -- to test directly whether the two effects are additive, whether one dominates, or whether they interact.

## Five Conditions, All Now Executed

All five conditions share one deterministic content-invariant checker (Section 6.1) and, in every condition that performs a repair, one fixed repair model, `google/gemma-3-12b-it`. Conditions B, D, and C1 were executed in an earlier iteration; Condition C2 was executed in the previous iteration; this iteration executes Condition C to completion, closing the design.

**Condition B (faithful baseline).** A reproduction of the original masked-fill system: the QE model's flagged span is masked with a placeholder token according to the original system's severity-conditioned masking rule, filled with one repair-model pass, and accepted without any check [4].

**Condition D (hygiene filter, no checker).** Condition B, plus a trivial post-hoc filter that detects and retries any output containing a leftover mask token, garbled placeholder text, or leaked instruction-format text. No content-invariant checker is involved.

**Condition C1 (broad localization, single pass).** The checker flags every invariant violation in the sentence, not only the original QE span; each flagged violation is repaired in one uncorrected pass, with no re-verification. Per-category repair scope is gated by the checker's own validated precision and recall (Section 6.1): a (language, category) cell falling below 0.5 on either metric in the within-experiment validation is excluded from repair scope.

**Condition C2 (narrow localization, iterative verification).** Localization stays restricted to the original QE-flagged span, but that span is repaired, re-checked by the checker against the specific invariant categories it flags, and re-repaired with a targeted, checker-detail-scoped prompt if it still fails, up to a fixed three-pass budget, stopping as soon as the checker certifies the repair. This isolates the effect of iteration while holding localization fixed at narrow.

**Condition C (broad localization, iterative verification, newly completed).** Both changes combined: the checker re-scans the entire current candidate text fresh on every pass, flagging every invariant violation it finds (not restricted to the row's own known-corrupted category, since Condition C's localization does not know in advance which category was corrupted), and each flagged violation is repaired and re-verified up to the same three-pass budget, stopping on a zero-flag certificate. This condition tests whether broadened localization's quality gain and iteration's correctness gain can be obtained together.

C2 and C were built by extending the checker module and OpenRouter client from the B/D/C1 artifact verbatim, so all five conditions share an identical checker, repair model, and API client. Both C2 and C regenerated the same stratified 320-natural/240-injected-pool row population using the same seed and stratification rule as B/D/C1, and row-ID identity against the prior run's logged row selection was verified true for all three subsets (natural, injected-pool, injected-heldout) before any comparison was trusted.

## Metrics

Matching the shared task's own reporting where possible, the protocol measures: (i) fix rate on the four checkable categories, scored against the human-confirmed injected-error subset, reported both pooled-with-negation and pooled-excluding-negation (Section 6.3); (ii) true regression rate, the fraction of invariants correct before repair that a repair step breaks, scored only against ground-truth-confirmed cases, using the same definition for every condition regardless of that condition's own checker verdicts; (iii) mean $\Delta$COMET using the shared task's own checkpoint where available [2]; (iv) edit volume, the mean fraction of the sentence's characters touched by a repair; (v) certificate rate, computed for the two iterating conditions (C2, C) as the fraction of rows reaching a verified, zero-flag state within the pass budget; and (vi) language-model calls per sentence, which C2 and C multiply relative to B, D, and C1 by design.

# Data

We reuse, without modification, the complete data construction validated in an earlier iteration: 6,000 natural WMT25 Task 3 rows across six English-source language pairs and five domains, carrying the QE model's released flagged spans and severity labels [3]; and 2,519 injected-error rows built by programmatically corrupting clean WMT24++ target text into one of four invariant categories (named-entity swap, number/unit/date alteration, negation polarity flip, quantifier substitution), each carrying the pre-corruption text, the corrupted text, and the exact character span of the change so a checker's precision and recall against a known answer is computable directly [14]. Both groups are split by language pair (and, for the injected set, by category) into an experimental pool and a checker-validation holdout kept strictly disjoint from it.

Condition C runs on the same 320 natural and 240 injected-pool rows, from the same two language pairs (en-ru\_RU, en-uk\_UA), as Conditions B, D, C1, and C2. This iteration's contribution to the data pipeline is again verified reuse rather than new construction: Condition C's row selection was checked for identity against Condition C2's own logged selection (not re-derived independently from the seed a second time), and all three subsets -- natural, injected-pool, injected-heldout -- matched exactly.

$\Delta$COMET for Conditions B, D, C1, and C2 throughout this protocol is computed with `wmt22-cometkiwi-da`, the same checkpoint the shared task's organizers use as the exact scorer behind every entry in its results table [2,3]. Condition C's natural-row quality metric this iteration is a substitute proxy score, not this checkpoint; Section 6.6 discloses why and reports both metrics without conflating them.

# Results

This iteration executes Condition C to completion (320 natural rows, 240 injected-pool rows, two language pairs, 100% completion fraction, zero hard failures on either fold), closing this protocol's five-condition design. We report the full B/D/C1/C2/C scorecard, reconciled onto a common, auditable statistical footing, together with two rigor fixes the prior review round required: a quantified explanation of a previously discrepant fix-rate-advantage figure, and a literal check of the paper's disjoint-population caveat.

## Reconciling Two Checker-Validation Tables

The checker's validity was measured twice in this project, at different scopes. The *global* table scores the checker against all 448 injected and 1,080 natural rows in the checker-validation holdout, across all six languages and four categories, using a natural-row precision proxy (any checker flag on a natural row that does not overlap a sparse QE-flagged span counts as a false positive, a noisy and conservative signal). The *within-experiment* table scores the checker against only the 175-row subset of that holdout actually available for the two language pairs this experiment runs on, using an exact single-positive-per-row precision against known ground-truth corruption spans on injected rows only -- a stricter, directly interpretable metric that is the one that actually gates C1's and Condition C's repair scope.

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

*Table 1: The two checker-validation procedures, restricted to the eight (language, category) cells this experiment runs on. $P$ is precision, $R$ is recall; usability requires both $\geq 0.5$.*

Three cells fail the within-experiment threshold and are excluded from C1's and Condition C's repair scope: ru\_RU and uk\_UA named-entity, and uk\_UA quantifier-scope. Condition C's own checker validation, run fresh against the same 175-row holdout this iteration, reproduces this table's within-experiment precision and recall values exactly (e.g. ru\_RU negation-polarity precision 0.857/recall 0.522, uk\_UA number-unit-date precision 0.575/recall 1.000) -- direct evidence that the checker is deterministic and identically configured across every condition it gates.

## Condition-B Fidelity

Before trusting any comparison built on the substitute repair model, this protocol pre-registered a quantitative tolerance for Condition B's reproduction of Padmanabhan (2025)'s $-0.0108$ mean $\Delta$COMET: the measured value must share Padmanabhan's sign, and its magnitude ratio to the original must fall in $[0.5\times, 2.0\times]$. Condition B's pooled $\Delta$COMET is $-0.0164$ (95% CI $[-0.0237,-0.0101]$), matching Padmanabhan's sign with a magnitude ratio of $1.52\times$ -- inside the tolerance band, close enough to its edge that we report this a borderline pass rather than an unqualified one.

## The B/D/C1/C2 Comparison, With the Negation Asymmetry Disclosed

Negation-polarity corruptions in the injected set are span *deletions* (the corrupted span is empty), so narrow-localization conditions (B, D, C2) structurally cannot attempt a negation repair at all -- fix\_success is trivially false for 100% of these rows by construction, not because of a repair-quality failure -- while broad-localization conditions (C1, C) can attempt them because their checker scans the whole sentence rather than masking a specific span. Every fix-rate and true-regression-rate figure below is reported both pooled including negation rows (treating the 60 structurally-unattemptable negation rows as automatic non-fixes for B, D, and C2, the convention every prior iteration used) and pooled excluding them, so the two readings are never conflated.

Pooled *including* negation (240 rows), Condition D's fix rate (0.7375) and true regression rate (0.0500) are identical to Condition B's, and its pooled $\Delta$COMET ($-0.0157$) is statistically indistinguishable from B's ($-0.0164$): basic output hygiene does not close the losing shared-task system's gap. Condition C1's pooled $\Delta$COMET is $-0.0035$, roughly a fivefold reduction relative to B and D, but its fix rate including negation (0.4542) and true regression rate (0.1250) are both worse than B/D's; Condition C2's fix rate including negation (0.7417) and true regression rate (0.0542) are essentially indistinguishable from B/D's on this reading, since the 60 negation rows drag all narrow-localization conditions' pooled figures down by the same fixed amount.

Pooled *excluding* negation (180 rows, the three categories every condition can attempt), the comparison sharpens. Table 2 places every condition side by side on this common basis, which is the one comparable across all five conditions without the negation-attemptability asymmetry diluting the picture.

| Condition | $\Delta$COMET (pooled, natural rows) | Fix rate (excl. negation) | True regr. rate (excl. negation) | Certificate rate | Edit volume | LLM calls / sentence |
|---|---|---|---|---|---|---|
| B | $-0.0164$ | 0.9833 | 0.0667 | n/a | 0.146 | $\sim$1.0 |
| D | $-0.0157$ | 0.9833 | 0.0667 | n/a | 0.146 | $\sim$1.0 |
| C1 | $-0.0035$ | 0.6056 | 0.1389 | n/a | 0.021 | 0.85 |
| C2 | $-0.0166$ | 0.9889 | 0.0722 | 0.917 | 0.164 | 2.29 |
| C | $+0.0016^{\dagger}$ | 0.6278 | **0.2167** | **0.267** | 0.022 | 2.53 |

*Table 2: Complete five-condition scorecard. Fix rate, true regression rate, and edit volume are pooled excluding negation-deletion rows, the population every condition can attempt; $\Delta$COMET is pooled over the natural-row sample, both language pairs. $^{\dagger}$Condition C's $\Delta$COMET is computed with a substitute proxy metric, not the real `wmt22-cometkiwi-da` checkpoint used by every other row, and is not numerically comparable to them (Section 6.6). n/a marks conditions with no certification loop. Bold marks Condition C's regression rate and certificate rate, the two values that most directly disconfirm the combined-condition hypothesis.*

C2's correctness metrics essentially match the simplest narrow-localization baselines: fix rate 0.9889 against B/D's 0.9833, true regression rate 0.0722 against B/D's 0.0667. What C2 dramatically improves on is C1: relative to C1's single-pass broadened localization, C2's narrow-but-iterated approach lifts fix rate by roughly 0.38 points on this excluding-negation basis and lowers true regression rate by 0.07 points, both differences confirmed by a true paired bootstrap on the 180 matched rows (true-regression-rate difference $0.0667$, 95% CI $[0.0111,0.1278]$, excluding zero). $\Delta$COMET moves the other way: C2's pooled $\Delta$COMET ($-0.0166$) is statistically indistinguishable from B and D, and a paired comparison against C1 on the same matched rows (using a documented normal-approximation substitute, since only pooled, not per-row, $\Delta$COMET is persisted for C1; formula: $\text{se}_{\text{diff}} = \sqrt{\text{se}_x^2+\text{se}_y^2}$ with each $\text{se}_i$ derived from that condition's own reported 95% CI half-width, which assumes independence between the two conditions' errors even though both are scored on the identical matched population -- a conservative-direction caveat we state explicitly rather than leave implicit) puts the C1-minus-C2 difference at $0.0131$ (95% CI $[0.0047,0.0214]$, excluding zero in the direction that C1 is better). Iteration is the load-bearing mechanism for recovering correctness, holding localization narrow; broadened localization, not iteration, is what single-lever evidence has shown moves whole-sentence quality.

## Reconciling the Fix-Rate-Advantage Discrepancy

The prior review round flagged that a paired-bootstrap fix-rate-advantage figure for C2 over C1 ($+0.2875$) did not match the difference implied by the excluding-negation table ($0.9889-0.6056=0.3833$). Both figures are correct; they differ because they are computed over different row populations, and this iteration's evaluation now states that explicitly as a first-class output rather than leaving a reader to reconstruct it. The 240-row true paired bootstrap on fix rate, computed directly from raw per-row C1 and C2 data, gives $+0.2875$ (95% CI $[0.2333,0.3458]$) when negation-deletion rows are included and scored as automatic non-fixes for C2 (which cannot structurally attempt them) while counted against C1's genuinely lower per-category performance on the rows it can attempt; the 180-row figure restricted to categories both conditions can attempt gives $+0.3833$ (95% CI $[0.3111,0.4556]$). The including-negation figure is smaller in magnitude, exactly as the negation-attemptability asymmetry predicts, because negation rows count as automatic non-fixes for C2 in that denominator while diluting nothing about C1's already-lower rate on the categories it does attempt -- a directional prediction now numerically verified rather than asserted.

## The Disjoint-Population Check

This paper's quality evidence ($\Delta$COMET, computed on the 320 natural WMT25 rows) and its correctness evidence (fix rate and true regression rate, computed on the 240 injected-pool rows with known ground-truth corruptions) are scored on structurally different populations: natural rows carry no ground-truth "correct fix" to score fix rate against, and injected rows carry no natural QE-severity distribution to score $\Delta$COMET against in the way the shared task's own reporting does. We verified this as a literal fact rather than an inferred property: a set intersection over the row IDs used for each population returns zero overlap (320 COMET-scored rows, 240 fix-rate-scored rows, intersection count 0). The paper's "iteration helps correctness but not quality" pattern therefore rests on combining evidence from two disjoint samples of the same underlying language pairs and domains, not on a single population scored simultaneously on both axes -- a materially weaker, though still informative, form of evidence than a jointly scored population would provide, and one we flag again in Limitations rather than only here.

## Condition C Completes: Combining Both Levers Does Not Combine Their Gains

Condition C -- broadened localization combined with iterative verification -- was launched on the same data, checker, and repair model as C2, under new run-robustness infrastructure built specifically against the prior iteration's silent stall: per-row, per-pass incremental JSON-lines writes fsync'd to disk immediately after each call returns; a hard 75-second per-call timeout with exponential-backoff retry (up to three attempts); synchronous checker calls offloaded to a background thread so they cannot block the event loop; and a heartbeat logged every 30 seconds. This infrastructure was validated under a real failure, not only a hypothetical one: this iteration's own first attempt at Condition C crashed mid-sweep from an agent-side busy-polling failure unrelated to the repair pipeline's own code. The incrementally-written, resumable ledger let the rerun deduplicate by row ID and pick up exactly where the crashed attempt left off, and the full 560-row sweep (320 natural, 240 injected-pool) completed in 334.7 seconds of run time for \$0.031 across 731 OpenRouter calls, well under the \$2 sub-budget this run pre-declared after a 20-row cost probe and far under the shared \$10 ceiling.

Row-ID identity against Condition C2's logged selection was verified true for all three subsets before any number below was trusted, and Condition C's checker validation exactly reproduces Table 1's within-experiment values, confirming the two runs share an identical, deterministically configured checker.

On the correctness axes -- the ones fully and comparably measured -- Condition C disconfirms the combined-levers hypothesis directly. Its fix rate (0.6278, excluding negation) sits between C1's 0.6056 and C2's 0.9889, a marginal improvement over single-pass broadened localization alone but nowhere near iteration alone's near-total fix rate. Its true regression rate (0.2167) is not merely uncorrected relative to C1 -- it is the highest of all five conditions in this protocol, exceeding C1's 0.1389 by more than half again and more than tripling C2's 0.0722. The mechanism is directly visible in certificate rate, a metric no single-lever iterating condition before this one needed to explain: C2 reaches a verified, zero-flag state on 91.7% of its rows within the shared three-pass budget; Condition C reaches that state on only 26.7%. Broadening the checker's surface to match C1's scope means each pass can surface new violations the previous pass's repair did not address -- or introduced -- so a fixed budget that comfortably certifies a single narrow span most of the time is nowhere near sufficient to certify an entire sentence's worth of checked invariants. Most rows under Condition C are left in a partially repaired state: some invariants fixed, others still flagged or newly broken, which is consistent with both the middling fix rate and the elevated regression rate observed. Edit volume rules out the simplest alternative explanation: Condition C's mean edit volume (0.022, natural rows pooled) is essentially identical to C1's (0.021) and nowhere near C2's (0.164) or B/D's (0.146), so the elevated regression is not explained by heavier or more repeated editing -- Condition C edits as narrowly, per pass, as single-pass broadened localization does; it simply does not converge to a verified state as reliably within the same budget iteration alone does.

Condition C's checker-based localization uniquely attempts negation-deletion rows, which B, D, and C2's oracle-span localization structurally cannot even target: of the 60 such rows in the injected pool, the broadened checker flagged 58.3% (35/60; 53.3% for en-ru\_RU, 63.3% for en-uk\_UA) on its first pass, before any repair -- a genuinely new number with no counterpart in any narrow-localization condition, reported separately from fix rate because the "fixed" verdict this protocol uses is undefined for a deletion with no corrupted substring to check the absence of. This localization capability is real but does not translate into the combined-condition success this design was built to test: Condition C's fix rate and true regression rate, on the population every condition can attempt, are still worse than iteration alone's, and the newly measurable negation-localization capability does not offset that.

Table 3 breaks the pooled Condition C figures down by the three attemptable categories, pooled across both language pairs, showing that the elevated regression rate is not concentrated in one category but spread across all three.

| Category | Fix rate | True regr. rate | Certificate rate | Passes / calls (mean) |
|---|---|---|---|---|
| named\_entity\_swap | 0.217 | 0.233 | 0.500 | 1.57 |
| number\_unit\_date\_alteration | 0.983 | 0.183 | 0.067 | 2.90 |
| quantifier\_substitution | 0.683 | 0.233 | 0.233 | 2.42 |

*Table 3: Condition C's injected-pool metrics by category, pooled across en-ru\_RU and en-uk\_UA (30 rows per language pair per category, 60 rows per category total). Named-entity is a checker-excluded category per Table 1 (repair is still attempted from the original QE flag where present, but the broadened checker cannot itself localize or re-verify it), which is consistent with its lower certificate rate and the weakest fix rate of the three; number-unit-date reaches the highest fix rate but also spends the most passes and shows the lowest certificate rate of the three, reflecting a category the checker keeps re-flagging even after a nominally correct repair.*

The quality axis could not be conclusively evaluated. Condition C's natural-row $\Delta$COMET metric is a substitute proxy score ($+0.0016$ pooled, 95% CI $[0.0005,0.0027]$), not the real `wmt22-cometkiwi-da` checkpoint every other condition in this protocol uses, because Hugging Face Hub returned HTTP 429 on all twelve retry attempts across two separate multi-minute backoff probes during this run -- a persistent, not transient, failure. This is the second time in this project that COMET-checkpoint access from Hugging Face Hub has failed during an execution run; we flag this now as a recurring infrastructure risk for this pipeline's evaluation stage specifically, not a one-off. The proxy metric's positive sign cannot be read as evidence that Condition C improves whole-sentence quality relative to B, D, C1, or C2, whose $\Delta$COMET figures are all negative on the real checkpoint: the two metrics are not on a shared scale, and no calibration between them exists in this project's artifacts. We report the proxy figure for completeness and directional interest only, and we do not use it in the verdict below.

**Verdict.** The pre-registered success test for Condition C required three conditions together: a non-negative-or-near-zero $\Delta$COMET, a true regression rate significantly below B's at a comparable-or-higher fix rate, and no collapse of edit volume toward full-retranslation levels. On the two criteria measurable with real, comparable data, the test fails outright: true regression rate (0.2167) is not below B's (0.0667) -- it is more than triple it and the highest of any condition tested -- and fix rate (0.6278) is not comparable-or-higher than B's (0.9833). Edit volume does not collapse, the one sub-criterion Condition C satisfies. The $\Delta$COMET criterion is undetermined, not satisfied, because the metric available this run is not the one the test specifies. We therefore report the protocol's central combined-condition hypothesis as **DISCONFIRMED on the measurable correctness axes, undetermined on the quality axis by forced metric substitution** -- a materially different, and more decisive, outcome than the "undetermined, pending completion" verdict the prior iteration was limited to reporting.

## The Six-Language-Pair Reconciliation

An earlier iteration replaced this project's original three-point comparison of published numbers with the complete six-language-pair record for both Task 3 scoped-editing systems from the WMT25 findings paper [3]: the losing system, SURREYPAI-S2, is negative on all six pairs ($-0.007$ to $-0.014$ $\Delta$COMET), while the stronger-model system, BASELINE-S2, is non-negative on four of six and negative on the remaining two (English-Japanese, English-Chinese). That record still supports the diagnosis this project's protocol is built to test -- capability and implementation maturity explain most, though not all, of the gap between the two published systems -- and our own Condition B, run under the real COMET checkpoint on two of these six pairs, reproduces SURREYPAI-S2's negative direction and rough magnitude, giving the diagnosis an independently measured data point beyond the two systems' self-reports. Nothing in this iteration's Condition C result changes that reconciliation; it bears on localization and iteration as levers within the scoped-editing design, a question the six-language-pair record cannot address on its own.

# Discussion

**What this iteration establishes, and what it does not.** Combining broadened localization with iteration does not combine their separately measured gains. On the correctness axes -- fix rate and true regression rate, scored identically across all five conditions -- Condition C is dominated by iteration alone on every measure that matters (regression rate, certificate rate) and only marginally improves on broadened localization alone's fix rate while inheriting none of C2's near-total certification. Whether Condition C also fails to recover C1's quality gain, or whether it might have matched or exceeded it, remains genuinely undetermined, because the checkpoint needed to measure that axis on a comparable scale was not reachable this run. What is now established is narrower and more decisive than what the prior iteration could report: this is not an open question awaiting a rerun; it is a measured interaction effect between the two levers, on the axes where measurement was possible, and that effect is negative.

**Why combining the levers backfires.** The mechanism is the fixed pass budget interacting with a broadened check surface. C2's checker only ever needs to verify the specific invariant category or categories the original QE flag identified within one narrow span, which a three-pass budget resolves to a certificate 91.7% of the time. Condition C's checker re-scans the whole sentence every pass, so a repair that successfully fixes the one invariant it targeted can leave -- or, on inspection of the elevated regression rate, sometimes introduce -- a violation elsewhere in the same sentence that the next pass must then also address, all within the same budget C2 needed for a single span. The certificate rate falling from 0.917 to 0.267 is the direct symptom: broadening what is checked does not just add more things to fix, it adds more things that can interact with each other across a fixed number of retries, and a sentence left mid-repair when the budget runs out is scored on whatever invariants the last pass happened to leave broken, not on the invariant the row was originally corrupted on. This is a different failure mode from C1's single-pass cost (which comes from never re-checking a repair at all) and from C2's flat-quality result (which comes from a checker that cannot see anything outside the categories it tracks) -- it is a genuinely new, interaction-specific cost that neither single-lever condition's own result predicted.

**What this means for a practitioner.** The trade-off this protocol has established through Condition C2 -- C1's whole-sentence quality gain against C2's near-total, auditable correctness -- still holds, and Condition C's result adds a caution rather than a resolution: naively combining the two mechanisms, with a pass budget sized for the narrower of the two loops, is measurably worse on correctness than either mechanism run alone, within the two Slavic language pairs and checker categories validated here. A practitioner who wants both a broadened check's coverage and an iteration loop's ability to retry should not assume the budget that works for a single-span loop transfers to a whole-sentence loop; this result suggests the pass budget itself, not merely the presence of iteration, may need to scale with how much of the sentence the checker is allowed to see, a question this protocol's fixed three-pass budget was not designed to isolate and that we flag as the clearest next experiment rather than resolve here.

**Limitations.** The most consequential limitation is the metric gap on the quality axis: Condition C's $\Delta$COMET is a substitute proxy, not the checkpoint every other condition uses, so this paper cannot state whether broadened-localization's quality gain survives combination with iteration -- only that its correctness cost does not improve, and gets worse. A second is the disjoint-population structure quantified in Section 6.5: $\Delta$COMET and fix-rate/regression are never scored on the same rows for any condition in this protocol, natural or otherwise, so even a hypothetical future run with real COMET for Condition C would still combine two disjoint samples into one narrative, not a single jointly-scored population. A third is coverage: the executed comparison runs on two of six language pairs, both Slavic-family languages with capitalization-based entity detection, the setting where the checker performs best per Table 1; named-entity detection is excluded from repair scope entirely for both tested languages. A fourth is the repair-model substitution: `google/gemma-3-12b-it` passes the pre-registered fidelity tolerance in Section 6.2 as a borderline rather than unqualified pass, and it still lacks the original TowerPlus-9B's machine-translation-specific fine-tuning. A fifth is that the C1-versus-C2 $\Delta$COMET comparison in Section 6.4 uses a documented normal-approximation substitute for a true paired test, since only pooled, not per-row, $\Delta$COMET is persisted for C1 or C2 in this project's artifacts; a genuinely paired per-row comparison would need both conditions re-scored at row level, which no artifact in this project has yet done. A sixth, procedural limitation is now a pattern rather than an isolated incident: Hugging Face Hub access to the `wmt22-cometkiwi-da` checkpoint has failed twice during execution across this project's iterations -- once for Condition B's initial attempt, resolved on retry, and once for Condition C this iteration, not resolved within this run's budget -- suggesting a general dependency risk in this pipeline's evaluation stage that the checkpointing infrastructure built for repair execution does not address, since it was designed against silent stalls in the repair loop, not against a scoring dependency being unreachable.

**What the next iteration must do.** Two things follow directly. First, re-score Condition C's natural rows with the real `wmt22-cometkiwi-da` checkpoint once Hugging Face Hub access is available, which is a scoring-only rerun over already-generated repair output rather than a full re-execution, and would close this paper's one remaining open axis without touching any of the correctness evidence already measured. Second, given that a fixed pass budget appears to interact with checker breadth rather than being neutral to it, test whether widening Condition C's pass budget (for instance to five or six passes, matching TEaR's own ablation range [29]) recovers certificate rate and, with it, regression rate -- directly testing whether this iteration's disconfirmation reflects a genuine ceiling on combining the two levers or an artifact of a budget sized for the narrower loop.

# Conclusion

This iteration completed the one condition this protocol was originally built to run -- broadened localization combined with iterative verification -- recovering from the same class of infrastructure failure that stalled the prior attempt via checkpointing that was tested under a real, not simulated, crash. The result disconfirms the hypothesis it was designed to test: combining the two levers does not combine their gains. On the correctness axes fully and comparably measured, Condition C is dominated by iteration alone, with a true regression rate higher than any other condition in this protocol and a certificate rate that collapses once the checker's surface broadens to match single-pass broadened localization's scope, while its edit volume shows the elevated regression is not simply a matter of heavier editing. The quality axis remains undetermined, honestly, because of a second Hugging Face Hub checkpoint-access failure this project has now encountered, not because the run failed to produce data. What began three iterations ago as an open question about whether two repair strategies could be combined for free now has a specific, mechanistic answer on the axes where measurement was possible: they cannot, at least not within a pass budget sized for the narrower of the two loops, and the reason is that broadening what a verifier checks makes verification itself the bottleneck a fixed budget cannot clear.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (rigor) The mechanistic explanation for Condition C's collapsed certificate rate (0.917 -> 0.267) attributes the collapse entirely to genuinely new or newly-introduced violations surfacing each pass ('a repair that successfully fixes the one invariant it targeted can leave -- or ... sometimes introduce -- a violation elsewhere'). But the paper's own Table 1 shows the checker's precision on the usable cells ranges from 0.575 to 0.857 -- meaning the checker itself generates a substantial rate of false-positive flags even on invariants that are already correct. Table 3 shows number_unit_date_alteration reaching the highest fix rate (0.983) of any category while having the lowest certificate rate (0.067) and the most passes (2.90, near the 3-pass cap) -- a pattern equally consistent with the checker repeatedly (falsely) re-flagging an already-correct repair as the true regression rate is with genuinely new damage each pass. The paper does not attempt to separate these two mechanisms, even though it has the data (per-cell precision from Table 1, per-category pass counts from Table 3) to make a first-order estimate.
  Action: Add an analysis using Table 1's per-cell precision to bound how much of the certificate-rate collapse is checker-false-positive-driven versus genuine cross-invariant regression -- e.g., compare certificate rate for the highest-precision cells (negation_polarity, ~0.78-0.86) against the lowest-precision usable cells (number_unit_date, ~0.575), and state explicitly whether the collapse is uniform across precision levels (supporting the 'genuine new violations' story) or concentrated in low-precision cells (supporting a checker-noise confound).
- [MAJOR] (evidence) This is the second time in this project that HuggingFace Hub access to the `wmt22-cometkiwi-da` checkpoint has failed during execution (the first hit Condition B in an earlier iteration and was resolved on retry). The paper discloses this honestly and builds real run-robustness infrastructure against a different failure class (silent repair-loop stalls), but does not report attempting any mitigation specific to the recurring checkpoint-access failure itself -- e.g., a pre-cached local copy of the checkpoint (which the project's own resource dossier confirms is CC-BY-NC-SA-4.0 gated but downloadable), a mirror host, or the paper's own previously-used substitute-but-consistent LLM-judge proxy carried forward from Condition B for a fair (if still-substituted) comparison across all five conditions rather than leaving Condition C on an unrelated, uncalibrated proxy scale. As a result, the paper's own pre-registered three-part success test for its central hypothesis cannot be fully evaluated on this run, a direct consequence of a now-known, recurring infrastructure risk that went unmitigated a second time.
  Action: Before the next execution attempt, pre-download and cache the wmt22-cometkiwi-da checkpoint locally (or resolve access via an alternate host/mirror) specifically because this failure mode is now known to recur; if a rerun before the next deadline is infeasible, at minimum use the same LLM-judge proxy metric that scored Condition B's fidelity check (rather than a different, uncalibrated proxy) so Condition C's quality-axis number is at least comparable to one other condition's, and state that comparison explicitly rather than reporting Condition C's proxy in isolation.
- [MAJOR] (methodology) Table 2's headline 'pooled excluding negation (180 rows, the three categories every condition can attempt)' framing implies named_entity, number_unit_date, and quantifier_scope are uniformly attemptable across all five conditions. But per Table 1, the checker excludes named_entity from repair scope in BOTH tested languages and excludes quantifier_scope in uk_UA -- meaning for C1 and Condition C specifically, only number_unit_date (and roughly half of quantifier_scope) is genuinely checker-localized and checker-verified across the full 180-row population; named-entity repairs under C1/C rely on the original QE-flagged span where present, not the broadened checker's own localization, despite being pooled into the 'broad localization' comparison. This caveat appears only in Table 3's caption, well after Table 2 and the main text have already used the 180-row figure as the comparison's common basis.
  Action: State the checker-eligibility caveat where the 180-row comparison is first introduced (Section 6.4, before Table 2), not only in Table 3's caption three subsections later, and consider reporting a secondary Table 2 restricted to the fully checker-eligible cells only (effectively number_unit_date plus ru_RU quantifier_scope) so a reader can see whether the headline C1-vs-C2-vs-C pattern holds on a population where the checker's own localization claim is uncontested.
- [MINOR] (clarity) Table 3's certificate-rate values are not explained for the named_entity category: since named-entity is checker-excluded from repair scope/re-verification per Table 1, it is not obvious what it means for 50% of named-entity rows to reach a 'verified, zero-flag certificate' when the checker cannot itself verify that category. The most likely reading is that a row's overall certificate status depends on all invariants the checker DOES track, and named-entity rows happen to pass on the categories that are checked -- but the paper never states this, leaving the number ambiguous.
  Action: Add one clause to Table 3's caption or the surrounding text clarifying what 'certificate' means for a row whose ground-truth-corrupted category is itself checker-excluded (i.e., certification is computed over the checker-tracked invariants only, independent of whether the row's own known corruption falls in an excluded category).
- [MINOR] (rigor) The C1-vs-C2 ΔCOMET paired comparison's normal-approximation substitute now includes the se_diff formula and an explicit independence-assumption caveat (an improvement over the prior draft, which gave neither), but the paper still asserts the caveat is 'conservative-direction' without justifying why the independence assumption should bias the interval in that direction rather than the other, or leaving the direction of bias unstated as unknown.
  Action: Either give a one-sentence argument for why treating two positively-correlated measurements as independent widens (rather than narrows) the estimated variance of their difference, or soften the claim to state that the direction of the resulting bias is not established, only that the substitute is documented and used consistently.
- [MINOR] (novelty) The paper's own literature-search artifact (art_QAQK2EUnuaCO) flags a promising, unfetched EAMT 2026 paper on post-editing with error highlights as 'the top open item for any follow-up pass,' but the paper's Related Work section does not mention this open item to the reader, so the novelty claim reads as more thoroughly checked than the underlying search process actually completed.
  Action: Add a brief clause noting that one candidate (an EAMT 2026 post-editing-with-highlights paper) was surfaced but not yet fetched and verified, so the novelty claim should be read as provisional pending that check, consistent with the paper's otherwise careful practice of disclosing incomplete verification elsewhere.
- [MINOR] (scope) The paper's 'What the next iteration must do' section proposes widening the pass budget to 5-6 rounds as the clearest next experiment, correctly identifying this as the key open test. But it does not note the risk that a wider budget interacts with the same checker-precision confound raised above (critique 1): more passes give a noisy, imperfect checker more opportunities to re-flag already-correct invariants, potentially inflating edit volume and introducing new regressions through sheer exposure rather than resolving genuine violations, which could produce an ambiguous result even if the budget experiment is run.
  Action: When proposing the budget-widening experiment, also propose tracking checker false-positive rate per pass (using the ground-truth-labeled injected rows, which the paper already has) so a wider-budget rerun can distinguish 'more passes let genuine repairs converge' from 'more passes let checker noise churn the sentence without net improvement.'
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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

<all_artifacts>
FULL EVIDENCE BASE: All 14 research artifacts across all iterations.

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

--- Item 9 ---
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

--- Item 10 ---
id: art_AHSm43w1MzxX
type: evaluation
title: B/D/C1/C2/C Scorecard and Verdict
summary: >-
  Consolidates the five-condition (B/D/C1/C2/C) span-editing comparison into one statistically-audited scorecard via eval.py,
  loading full_method_out.json from art_7Uc5PlFctjXi (B/D/C1), art_K8koUmGFDlLN (C2), art_QLpPxaqf1VzK (checker validation),
  and art_mhfmDpGp4z1J (dataset), plus scanning this iteration's gen_art siblings at run time for a Condition C artifact.
  Step 1 performs a falsifiable per-row-COMET-availability gate: it enumerates the actual top-level and per-row keys of every
  upstream JSON and finds NO per-row COMET array anywhere (only pooled/per-language-pair delta_comet_mean + delta_comet_ci95
  are stored), recording per_row_comet_{b,d,c1,c2,c}_available=false with the exact keys inspected. Step 2 therefore runs
  a TRUE paired bootstrap (2000 resamples, seed=42, matching B/D/C1's own recorded seed) on fix_rate and true_regression_rate,
  which DO exist per-row (metadata_{cond}_fixed / metadata_{cond}_true_regression on the 240 matched injected-pool rows),
  for the pairs C1-vs-C2/C, C2-vs-C, C-vs-B, C-vs-D, both including and excluding the 60 structural-non-attempt negation rows;
  DeltaCOMET pairwise comparisons instead use a documented normal-approximation fallback (se_diff formula spelled out, independence-assumption
  caveat stated explicitly) since no per-row COMET exists to pair. Step 3 computes the disjoint-population check as a literal
  set intersection: comet_population_n=320, fix_rate_population_n=240, overlap_count=0, verified=true. Step 4 recomputes the
  reviewer-flagged fix-rate-advantage discrepancy directly from raw per-row C1/C2 data and reconciles it exactly: fix_rate_advantage_240_including_negation=+0.2875
  (95% CI [0.233, 0.346]) vs fix_rate_advantage_180_excluding_negation=+0.3833 (95% CI [0.311, 0.456]), numerically verifying
  the including-negation number is smaller in magnitude as the mechanism explanation predicts. Step 5 evaluates the hypothesis's
  three pre-registered success sub-criteria: (a) D closes only part of B's gap -- PASS (CI on B-D includes 0, |D|<|B|); (b)
  C2 shows materially larger regression-rate reduction than C1 (CI excludes 0, correct sign) but NOT materially larger DeltaCOMET
  improvement (C2's DeltaCOMET is actually worse than C1's) -- criterion b FAILS; (c) Condition C's own three-part success
  test could not be evaluated because NO Condition C sibling artifact was found in this iteration's gen_art directory by evaluation
  run time (the concurrent Condition C run had not produced method_out.json/full_method_out.json when this evaluation executed)
  -- condition_c_status='not_found'. The combined condition_c_verdict is therefore UNDETERMINED_NO_ARTIFACT, with the rationale
  field citing the scan log and confirming steps (1)-(4) plus the B/D/C1/C2-only five-row scorecard (step 6, minus the C row)
  are a complete, standalone deliverable regardless of Condition C's availability. Step 6 renders the full scorecard: pooled
  DeltaCOMET (point+CI), fix_rate and true_regression_rate both including/excluding negation, mean edit volume, mean LLM calls/sentence,
  total OpenRouter cost, and a per-language-pair (en-ru_RU/en-uk_UA) breakdown of fix_rate/regression for every condition
  -- B=(-0.01644, fix 0.7375/0.9833, reg 0.05/0.0667), D=(-0.01569, fix identical to B), C1=(-0.00355, fix 0.4542/0.6056,
  reg 0.125/0.1389), C2=(-0.01664, fix 0.7417/0.9889, reg 0.0542/0.0722), C=not_found. Output full_eval_out.json (1.09MB,
  560 examples across 2 datasets: injected_pool_fix_rate_and_regression_paired with per-row eval_* diff fields, and natural_rows_edit_volume_and_calls)
  validated against exp_eval_sol_out schema (PASSED). Downstream GEN_PAPER_TEXT should cite the reconciled 0.2875/0.3833 fix-rate
  figures side by side rather than either alone, treat the C1-vs-C2 pattern as 'iteration helps correctness/regression but
  not whole-sentence quality, checker-broadened localization is the reverse' (materially confirmed via true paired tests),
  and note Condition C's verdict is UNDETERMINED pending that artifact's completion -- if it becomes available later, re-running
  eval.py (which dynamically re-scans for it) will upgrade the verdict without any other code changes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 11 ---
id: art_QAQK2EUnuaCO
type: research
title: No Prior Work Separates MT Repair Localization from Iteration
summary: >-
  This research artifact executes a targeted, logged literature search to determine whether any prior work in machine-translation
  automatic post-editing (APE) or scoped span editing varies 'breadth of error localization' (a narrow QE-flagged span vs.
  broadened content-invariant/error detection) and 'iteration/re-verification of a repair' (single-pass vs. checker-guided
  iterated repair) as two independently varied, separately measured factors -- the same 2x1 design this project's C1 (broad,
  single-pass) vs. C2 (narrow, iterated) conditions use. It runs 10 verbatim search queries (general + scholarly mode where
  specified) via the aii-web-tools skill, logs hit quality for each, and fetches/fetch_greps 6 candidate papers in full: TEaR
  (Wang et al., NAACL 2025 Findings), two WMT25 Task 3 submissions (Padmanabhan 2025, already in related work, and Sharma
  2025, newly surfaced), xTower (Treviso et al., ACL Findings EMNLP 2024), SSPO (Sun et al., ACL 2025), TranslationCorrect
  (ACL 2025 Demo), and a general (non-MT) LLM self-localization paper (Samanta et al., arXiv 2602.02416). Each candidate is
  classified per an explicit decision rule (separates the factors / bundles the factors / varies only one factor / out of
  scope) with quoted or paraphrased evidence from the fetched text. The verdict: no candidate across all queries and fetched
  papers separates localization breadth from iteration as independently varied factors. TEaR is the closest prior ablation,
  varying iteration count (1-5 rounds, Tables 12-13) while holding localization/estimation scope fixed, and its own Appendix
  D finds that repeated iteration can hurt performance -- a one-dimensional finding. The two WMT25 QE-informed correction
  systems use localization purely as a fixed input signal to a single correction pass, with Sharma (2025) containing zero
  occurrences of 'iterat' anywhere in its full text. xTower, flagged in planning as a possible two-stage breadth-then-iteration
  design, does not support that reading on inspection -- it is a single explain step, not an isolated two-stage ablation --
  and the related-work section's characterization of it should be corrected. Downstream, this artifact supports the paper's
  novelty claim as currently scoped (no rescoping required) but recommends wording the claim specifically about MT automatic
  post-editing / scoped span editing rather than about self-correction research broadly, since the free OpenAlex/Crossref
  scholarly search backend returned systematically off-topic results for 4 of 5 scholarly-mode queries due to term collisions
  on words like 'checker,' 'repair,' and 'localization.' One promising lead (an EAMT 2026 paper on post-editing with error
  highlights) was surfaced but not fetched within the time budget and is flagged as the top open item for any follow-up pass,
  along with a note that ACL-Anthology-native search would likely surface more than the free scholarly backend used here.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 12 ---
id: art_Z2n1W5YNDnR5
type: experiment
title: Rescue Condition C's Missing Quality Score
summary: >-
  This is a scoring-only rerun over Condition C's (art_6n9zJVKWXnio) already-generated 320 natural-row repair outputs (en-ru_RU
  / en-uk_UA, iterative checker-gated span repair, up to 3 passes). It generates no new repair text and makes no new repair-model
  calls; it only tries -- with genuinely new mitigations versus the two prior failed attempts (an alternate mirror endpoint
  hf-mirror.com, and attempts spread across real wall-clock-separated windows [0, 25, 75, 165] minutes rather than in-process
  exponential backoff) -- to obtain the real Unbabel/wmt22-cometkiwi-da checkpoint from HuggingFace Hub and score the pre-repair
  vs. post-repair text pairs. Both Condition C (art_6n9zJVKWXnio) and Condition B (art_G9ppuk8aHUhW) were located on disk
  via content-signature verification (unique metadata keys and exact row counts, since no artifact id is embedded in any filename),
  not by hardcoded path, so the script fails loudly with a BLOCKING assertion if either artifact cannot be found. On this
  run, the real COMET checkpoint downloaded successfully on the very first attempt (window offset=0, primary huggingface.co
  endpoint, 0.26s, single attempts_log entry, no 429) -- the prior HF-Hub throttling that blocked Condition B and the earlier
  Condition C attempt was NOT reproduced. The real-COMET path (Phase 2a) was therefore taken: the wmt22-cometkiwi-da XLM-R-based
  QE model scored all 320 pre-repair and 320 post-repair texts on GPU (RTX 4090), giving condition_c_delta_comet_natural_pooled_mean
  = -0.01725 with a 10,000-resample bootstrap 95% CI of [-0.02514, -0.01030], broken out per language pair (en-ru_RU: -0.02280
  n=160; en-uk_UA: -0.01170 n=160), plus a full per-row table (row_id, language_pair, comet_before, comet_after, delta_comet,
  certificate_achieved, n_passes). directly_comparable_to_C1_C2_real_comet_numbers is set to True since this is the same real
  metric used elsewhere in the study. The script also implements, but did not need to exercise, a fully-coded fallback path
  (Phase 2b): if real COMET is genuinely unobtainable within a 3-hour time-boxed mitigation window, it falls back to the EXACT
  SAME LLM-judge proxy configuration Condition B's own fidelity check used -- openai/gpt-4o-mini, the JUDGE_PROMPT string
  copied character-for-character from Condition B's method.py (temperature=0.0, 0-1 adequacy scale, regex-parsed score) --
  and re-scores a fresh 320-row seeded sample of Condition B's own rows with that identical proxy in the SAME run (not just
  Condition C), so any fallback report would be an explicit same-proxy, same-run B-vs-C comparison (via an unpaired bootstrap
  of the two independent means, since B and C share no row ids) rather than an isolated, incomparable number, with a hard
  $9 OpenRouter cost cap and honest partial-n reporting if the cap is hit. One deviation from the plan's literal pseudocode,
  both documented in-code: (1) the source data has no metadata_fold_or_source field -- Condition C's row-id prefix wmt25_task3_natural:
  and dataset-slot structure serve the same filtering role, and Condition B's own row population is 1560 rows (not 320) since
  it covers different language pairs (en-zh_CN/en-cs_CZ) than Condition C (en-ru_RU/en-uk_UA), so a 320-row stratified sample
  of B's own rows is drawn rather than asserting a nonexistent 320-row B subset. Environment notes for reproducibility: torch==2.13.0
  required setuptools pinned <81 (setuptools>=81 dropped pkg_resources, which pytorch_lightning/torchmetrics still import
  at load time) -- this is pinned in pyproject.toml. Output validated against the exp_gen_sol_out schema via aii-json; full/mini/preview
  variants generated; method_out.json and full_method_out.json are 1.2MB each, well under the 100MB split threshold so no
  splitting was needed. hf_cache/ (the 2.2GB downloaded COMET checkpoint) and .venv/ (7.6GB) are excluded from repo upload
  as pure scratch/cache bulk, not deliverables.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 13 ---
id: art_ImnQ5UsI-lMB
type: evaluation
title: Why Condition C's Combined Repair Fix Collapsed
summary: >-
  Pure re-analysis (no new LLM calls, no new COMET scoring) of three prior span-editing repair experiments on WMT25 en-ru_RU/en-uk_UA
  translations (B/D/C1 from art_7Uc5PlFctjXi, C2 from art_K8koUmGFDlLN, and Condition C from art_6n9zJVKWXnio), produced as
  eval.py + eval_out.json validated against the exp_eval_sol_out schema. First verified exact row-ID identity across all three
  artifacts' selected_rows.json for all three folds (natural, injected-pool, injected-heldout), including the B/D/C1-vs-C
  pair that had never been directly cross-checked before -- confirmed byte-identical. Produces four separately labeled, source-traced
  analyses. (1) precision_tier_collapse_analysis: splits the 5 checker-eligible (language,category) cells (of 8) into a high-precision
  tier (negation_polarity, checker precision 0.78-0.86) and a low-precision tier (number_unit_date, quantifier_scope, precision
  0.575-0.65), recomputing Condition C's per-cell certificate_rate directly from raw per-row fields (validated as an exact
  superset of Condition C's own pre-aggregated table for the 3 categories it does report, and additionally recovers negation_polarity's
  certificate rate, which that table reports as null). Finds collapse_pattern='concentrated_in_low_precision_tier': mean certificate_rate
  0.35 in the high-precision tier vs 0.089 in the low-precision tier (n=2 vs n=3 cells, explicitly flagged as low statistical
  power), consistent with checker-noise-driven churn rather than uniform cross-invariant regression, reported with fully hedged,
  non-causal language. No fourth widened-pass-budget artifact was found among the actual dependencies, so this is documented
  as the best available evidence rather than silently omitted. (2) checker_eligibility_restricted_analysis: derives the exact
  eligibility scope from checker_validation.json's own recall>=0.5 AND precision>=0.5 threshold rule (5 of 8 cells: number_unit_date
  both languages, negation_polarity both languages, quantifier_scope in ru_RU only) -- noting this is wider than the plan
  text's own restatement, which omitted negation_polarity -- then computes fix_rate/true_regression_rate/certificate_rate
  for B, D, C1, C2, and C restricted to only these cells, side by side with the full pooled figures. The headline ordering
  (C1 worse regression than C2; Condition C worst of all on true_regression_rate; certificate_rate collapse from C2 to C)
  survives this restriction unchanged in direction. (3) certificate_definition_by_category: reads art_6n9zJVKWXnio's method.py/checker.py
  directly (excluded_cells_from_validation + Checker.detect_all(respect_exclusions=True)) and confirms via a worked example
  row that a row's certificate status is scored only over non-excluded invariant categories, independent of whether the row's
  own corrupted category is itself excluded (e.g. a named_entity_swap row in an excluded cell is never checked on its own
  corruption category) -- option (b) in the plan's decision tree. Also surfaces an incidental finding: Condition C's own re-fit
  checker validation shows named_entity recall/precision of exactly 0.0/0.0 (vs the original run's 1.0/0.32), meaning named_entity
  is never flagged at all in Condition C's environment, though this does not change the excluded_cells set or any headline
  result. (4) normal_approx_bias_direction: proves algebraically that treating two positively-correlated ΔCOMET measurements
  as independent (Var(X-Y)=Var(X)+Var(Y) instead of minus 2*Cov(X,Y)) yields a conservative (wider), not narrower, interval
  whenever Cov(X,Y)>0, with a numeric worked example using the actual reported B/C1/C2 ΔCOMET 95% CI half-widths at several
  assumed correlation values. Confirms no per-row ΔCOMET array is persisted in any of the three artifacts (checked directly),
  so the actual covariance sign cannot be estimated empirically -- the claim is explicitly downgraded from an unconditional
  assertion to a conditional one ('IF the shared row population/repair model/checker induce positive correlation, THEN the
  substitute is conservative') with plausible covariance sources named and the exact additional data (per-row paired bootstrap
  replicates) that would resolve it. eval_out.json's metadata field contains the full detail for all four analyses; metrics_agg
  carries a flat numeric summary; the datasets/examples array poses each analysis as a directly-quotable question/answer pair
  with the full analysis object attached via metadata_analysis for schema compliance. Total cost: $0 (no LLM calls). Deliverables:
  eval.py, eval_out.json (+ full/mini/preview variants, all schema-validated), pyproject.toml with pinned dependencies, deps/
  containing the copied dependency files used for computation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 14 ---
id: art_zeGV63Zf89Ql
type: research
title: EAMT 2026 Highlights Paper Does Not Vary Iteration
summary: >-
  This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO):
  the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al.,
  ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as
  a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision
  rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text
  evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance;
  (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by
  Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction
  suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms
  xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both
  H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for
  iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both
  referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine
  iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization
  breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's
  diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only
  one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in
  any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A
  second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX
  study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop
  study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement
  this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional
  queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not
  2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item:
  across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization
  breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's
  novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: experiment
id: art_Z2n1W5YNDnR5
title: Rescue Condition C's Missing Quality Score
summary: >-
  This is a scoring-only rerun over Condition C's (art_6n9zJVKWXnio) already-generated 320 natural-row repair outputs (en-ru_RU
  / en-uk_UA, iterative checker-gated span repair, up to 3 passes). It generates no new repair text and makes no new repair-model
  calls; it only tries -- with genuinely new mitigations versus the two prior failed attempts (an alternate mirror endpoint
  hf-mirror.com, and attempts spread across real wall-clock-separated windows [0, 25, 75, 165] minutes rather than in-process
  exponential backoff) -- to obtain the real Unbabel/wmt22-cometkiwi-da checkpoint from HuggingFace Hub and score the pre-repair
  vs. post-repair text pairs. Both Condition C (art_6n9zJVKWXnio) and Condition B (art_G9ppuk8aHUhW) were located on disk
  via content-signature verification (unique metadata keys and exact row counts, since no artifact id is embedded in any filename),
  not by hardcoded path, so the script fails loudly with a BLOCKING assertion if either artifact cannot be found. On this
  run, the real COMET checkpoint downloaded successfully on the very first attempt (window offset=0, primary huggingface.co
  endpoint, 0.26s, single attempts_log entry, no 429) -- the prior HF-Hub throttling that blocked Condition B and the earlier
  Condition C attempt was NOT reproduced. The real-COMET path (Phase 2a) was therefore taken: the wmt22-cometkiwi-da XLM-R-based
  QE model scored all 320 pre-repair and 320 post-repair texts on GPU (RTX 4090), giving condition_c_delta_comet_natural_pooled_mean
  = -0.01725 with a 10,000-resample bootstrap 95% CI of [-0.02514, -0.01030], broken out per language pair (en-ru_RU: -0.02280
  n=160; en-uk_UA: -0.01170 n=160), plus a full per-row table (row_id, language_pair, comet_before, comet_after, delta_comet,
  certificate_achieved, n_passes). directly_comparable_to_C1_C2_real_comet_numbers is set to True since this is the same real
  metric used elsewhere in the study. The script also implements, but did not need to exercise, a fully-coded fallback path
  (Phase 2b): if real COMET is genuinely unobtainable within a 3-hour time-boxed mitigation window, it falls back to the EXACT
  SAME LLM-judge proxy configuration Condition B's own fidelity check used -- openai/gpt-4o-mini, the JUDGE_PROMPT string
  copied character-for-character from Condition B's method.py (temperature=0.0, 0-1 adequacy scale, regex-parsed score) --
  and re-scores a fresh 320-row seeded sample of Condition B's own rows with that identical proxy in the SAME run (not just
  Condition C), so any fallback report would be an explicit same-proxy, same-run B-vs-C comparison (via an unpaired bootstrap
  of the two independent means, since B and C share no row ids) rather than an isolated, incomparable number, with a hard
  $9 OpenRouter cost cap and honest partial-n reporting if the cap is hit. One deviation from the plan's literal pseudocode,
  both documented in-code: (1) the source data has no metadata_fold_or_source field -- Condition C's row-id prefix wmt25_task3_natural:
  and dataset-slot structure serve the same filtering role, and Condition B's own row population is 1560 rows (not 320) since
  it covers different language pairs (en-zh_CN/en-cs_CZ) than Condition C (en-ru_RU/en-uk_UA), so a 320-row stratified sample
  of B's own rows is drawn rather than asserting a nonexistent 320-row B subset. Environment notes for reproducibility: torch==2.13.0
  required setuptools pinned <81 (setuptools>=81 dropped pkg_resources, which pytorch_lightning/torchmetrics still import
  at load time) -- this is pinned in pyproject.toml. Output validated against the exp_gen_sol_out schema via aii-json; full/mini/preview
  variants generated; method_out.json and full_method_out.json are 1.2MB each, well under the 100MB split threshold so no
  splitting was needed. hf_cache/ (the 2.2GB downloaded COMET checkpoint) and .venv/ (7.6GB) are excluded from repo upload
  as pure scratch/cache bulk, not deliverables.

type: evaluation
id: art_ImnQ5UsI-lMB
title: Why Condition C's Combined Repair Fix Collapsed
summary: >-
  Pure re-analysis (no new LLM calls, no new COMET scoring) of three prior span-editing repair experiments on WMT25 en-ru_RU/en-uk_UA
  translations (B/D/C1 from art_7Uc5PlFctjXi, C2 from art_K8koUmGFDlLN, and Condition C from art_6n9zJVKWXnio), produced as
  eval.py + eval_out.json validated against the exp_eval_sol_out schema. First verified exact row-ID identity across all three
  artifacts' selected_rows.json for all three folds (natural, injected-pool, injected-heldout), including the B/D/C1-vs-C
  pair that had never been directly cross-checked before -- confirmed byte-identical. Produces four separately labeled, source-traced
  analyses. (1) precision_tier_collapse_analysis: splits the 5 checker-eligible (language,category) cells (of 8) into a high-precision
  tier (negation_polarity, checker precision 0.78-0.86) and a low-precision tier (number_unit_date, quantifier_scope, precision
  0.575-0.65), recomputing Condition C's per-cell certificate_rate directly from raw per-row fields (validated as an exact
  superset of Condition C's own pre-aggregated table for the 3 categories it does report, and additionally recovers negation_polarity's
  certificate rate, which that table reports as null). Finds collapse_pattern='concentrated_in_low_precision_tier': mean certificate_rate
  0.35 in the high-precision tier vs 0.089 in the low-precision tier (n=2 vs n=3 cells, explicitly flagged as low statistical
  power), consistent with checker-noise-driven churn rather than uniform cross-invariant regression, reported with fully hedged,
  non-causal language. No fourth widened-pass-budget artifact was found among the actual dependencies, so this is documented
  as the best available evidence rather than silently omitted. (2) checker_eligibility_restricted_analysis: derives the exact
  eligibility scope from checker_validation.json's own recall>=0.5 AND precision>=0.5 threshold rule (5 of 8 cells: number_unit_date
  both languages, negation_polarity both languages, quantifier_scope in ru_RU only) -- noting this is wider than the plan
  text's own restatement, which omitted negation_polarity -- then computes fix_rate/true_regression_rate/certificate_rate
  for B, D, C1, C2, and C restricted to only these cells, side by side with the full pooled figures. The headline ordering
  (C1 worse regression than C2; Condition C worst of all on true_regression_rate; certificate_rate collapse from C2 to C)
  survives this restriction unchanged in direction. (3) certificate_definition_by_category: reads art_6n9zJVKWXnio's method.py/checker.py
  directly (excluded_cells_from_validation + Checker.detect_all(respect_exclusions=True)) and confirms via a worked example
  row that a row's certificate status is scored only over non-excluded invariant categories, independent of whether the row's
  own corrupted category is itself excluded (e.g. a named_entity_swap row in an excluded cell is never checked on its own
  corruption category) -- option (b) in the plan's decision tree. Also surfaces an incidental finding: Condition C's own re-fit
  checker validation shows named_entity recall/precision of exactly 0.0/0.0 (vs the original run's 1.0/0.32), meaning named_entity
  is never flagged at all in Condition C's environment, though this does not change the excluded_cells set or any headline
  result. (4) normal_approx_bias_direction: proves algebraically that treating two positively-correlated ΔCOMET measurements
  as independent (Var(X-Y)=Var(X)+Var(Y) instead of minus 2*Cov(X,Y)) yields a conservative (wider), not narrower, interval
  whenever Cov(X,Y)>0, with a numeric worked example using the actual reported B/C1/C2 ΔCOMET 95% CI half-widths at several
  assumed correlation values. Confirms no per-row ΔCOMET array is persisted in any of the three artifacts (checked directly),
  so the actual covariance sign cannot be estimated empirically -- the claim is explicitly downgraded from an unconditional
  assertion to a conditional one ('IF the shared row population/repair model/checker induce positive correlation, THEN the
  substitute is conservative') with plausible covariance sources named and the exact additional data (per-row paired bootstrap
  replicates) that would resolve it. eval_out.json's metadata field contains the full detail for all four analyses; metrics_agg
  carries a flat numeric summary; the datasets/examples array poses each analysis as a directly-quotable question/answer pair
  with the full analysis object attached via metadata_analysis for schema compliance. Total cost: $0 (no LLM calls). Deliverables:
  eval.py, eval_out.json (+ full/mini/preview variants, all schema-validated), pyproject.toml with pinned dependencies, deps/
  containing the copied dependency files used for computation.

type: research
id: art_zeGV63Zf89Ql
title: EAMT 2026 Highlights Paper Does Not Vary Iteration
summary: >-
  This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO):
  the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al.,
  ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as
  a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision
  rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text
  evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance;
  (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by
  Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction
  suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms
  xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both
  H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for
  iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both
  referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine
  iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization
  breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's
  diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only
  one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in
  any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A
  second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX
  study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop
  study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement
  this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional
  queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not
  2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item:
  across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization
  breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's
  novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Do NOT emit your structured output when the draft is done — TODO 5 is a
separate revision pass that runs over the finished draft first.
TODO 5. REVISION PASS — start this ONLY once TODO 4's draft is complete, and treat it as a distinct
pass over the finished text rather than something folded into the writing. Read
`REVISION_CHECKLIST.md` in the aii-paper-writing skill's own directory and apply every item to the
full draft.

Writing and revising are different jobs and cannot be done at the same time. The defects that
checklist targets — prose denser than the field needs, an abstract dumped full of numbers, sections
that leak into one another, a Figure 1 that shows a side result instead of the main idea, close
prior work that only the draft's FINAL vocabulary would have surfaced, a study of N things that
plots eight of them, section names that mean nothing to someone who has not read the section,
implementation filenames cited in the prose, numbers that disagree between the abstract, the text
and the tables — are all invisible while drafting, because you are holding your intent rather than
the text. Every one is obvious to the first outside reader.

Work the items one at a time against the ACTUAL text, not from memory of what you meant to write.
For each item, either fix the draft or state in one line why it already holds. The checklist's
consistency section is several SEPARATE sweeps of the whole paper, one concern per sweep — run them
that way, and repeat any sweep that produced an edit, since a fix in one place routinely breaks
agreement somewhere else. Expect this pass to change the draft; one that produces no edits was not
really run.

Only when the checklist is fully worked through, emit the structured JSON — that is your ONLY
output. Do NOT compile LaTeX or generate image/figure files at any point.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-01 10:49:50 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-09-01 10:49:52 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: "Writes the PROSE of an AI research paper: abstract, introduction, related work, methods, experiments, discussion and conclusion, with a page budget, the 5-paragraph intro pattern, writing-quality rules, inline [FIGURE:fig_id] markers plus a structured figures array, and a MANDATORY REVISION_CHECKLIST.md pass over every finished draft. Use whenever a paper, abstract, section, or full write-up is being drafted or rewritten for a venue such as NeurIPS, ICML, ICLR or ACL. Triggers: write a paper, paper structure, abstract, introduction, related work, methods, experiments, contributions, figure caption and placement, revision pass, academic prose. NOT for: assembling or compiling .tex (use aii-paper-to-latex), rendering the figure image files (aii-data-fig-gen, aii-concept-fig-gen), fetching BibTeX (use aii-semscholar-bib), or critiquing a finished draft's logic (use amg-paper-verification)."
---

## MANDATORY: the final revision pass

**`REVISION_CHECKLIST.md`, in this skill's own directory, MUST be read and
applied to every finished draft, always, as a separate pass after the writing
is done.** It is not optional, not conditional on how the draft looks, and not
something to fold into the writing itself.

Writing and revising are different jobs and cannot be done in one pass. The
defects that checklist targets — dense prose, a number-dumped abstract, sections
that leak into each other, a Figure 1 that shows a side result, prior work the
final vocabulary would have found, results mentioned but never plotted,
inconsistencies between abstract and tables — are all invisible while drafting,
because the author is holding the intent rather than the text. Every one of them
is obvious to the first outside reader. Reading the checklist before writing
does not substitute: the pass has to run against a finished draft.

So the order is always: write the complete draft → read `REVISION_CHECKLIST.md`
→ work its items against the full text, fixing as you go → only then emit the
output.

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-09-01 10:49:52 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and writes the result into references.bib, with a mandatory web-search fallback for anything not found. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX first. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
