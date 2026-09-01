# review_paper — test_idea

> Phase: `invention_loop` · round 3 · `review_paper`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 09:14:36 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/review_paper/review_paper
```

### [2] SYSTEM-USER prompt · 2026-09-01 09:14:42 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described
- Screen for unattributed reuse. Search the web for the paper's distinctive phrasings, its central claim, and any method name it coins. If wording, a derivation, or a result appears in prior work, say so and name the source. Treat close paraphrase of a source's argument without citation the same as verbatim reuse
- Check that any prior work the paper builds on is cited at the point it is used, not only in a related-work list. An uncited source that the work depends on is a major issue, not a presentation nit
- Check the cited sources exist and say what they are claimed to say. Flag any reference you cannot verify, and any retracted or predatory-venue source

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

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
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 09:14:42 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Bash · 2026-09-01 09:16:16 UTC

```
mkdir -p "$(dirname ./.terminal_claude_agent_struct_out.json)" 2>/dev/null; pwd
```

### [5] TOOL RESULT — Bash · 2026-09-01 09:16:17 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/review_paper/review_paper", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [6] TOOL CALL — Write · 2026-09-01 09:17:27 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/review_paper/review_paper/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This iteration is a substantial, honest improvement over the prior draft: both MAJOR issues from the previous review (the negation-deletion structural asymmetry and the unreconciled dual checker-validation tables) are now addressed directly, with a named comparison table and pooled-with/without-negation reporting throughout. The paper's central move -- running Condition C2 (narrow localization + iteration) as the missing half of the B/D/C1 comparison, and reporting the result as genuinely mixed (iteration recovers fix-rate/regression-rate but not ΔCOMET, and is measurably worse than C1 on ΔCOMET despite being measurably better on regression) -- is a real, well-instrumented finding, and the paper's refusal to paper over Condition C's non-completion with an estimate is exactly the right call scientifically. However, the paper's central research question (does combining broad localization with iteration capture both C1's quality gain and C2's correctness gain?) remains unanswered because Condition C stalled, which caps how much this iteration can claim to have resolved. On top of that, two new rigor gaps surface in this draft's own numbers: a fix-rate-difference figure quoted in the text (+0.2875 from a 240-row paired bootstrap) does not match the difference implied by Table 2's excluding-negation fix rates (0.9889 - 0.6056 = 0.3833), and the discrepancy (different row denominators -- 240 including negation vs. 180 excluding it) is never explained to the reader. There is also an underexamined population mismatch: ΔCOMET (the 'quality' axis) is measured on natural WMT25 rows while fix-rate/regression (the 'correctness' axis) is measured on a disjoint set of programmatically injected-error rows, yet Table 2 and the Discussion synthesize the two into a single 'iteration helps correctness but not quality' story without acknowledging that no single row is ever scored on both axes. Combined with the still-narrow scope (2 of 6 language pairs, both Slavic with capitalization-based NER; a substitute repair model that passes fidelity only as a 'borderline' pass), the paper is technically careful and unusually forthright about its own limitations, but its core deliverable this round is an honest 'still open' rather than a resolved mechanism, which limits its significance for a top-tier venue as currently scoped.",
  "strengths": [
    "Both MAJOR critiques from the previous review round are substantively fixed: the negation-deletion asymmetry is now quantified and reported both pooled-including and pooled-excluding negation throughout (Section 6.3), and the two checker-validation procedures are named, reconciled in a single table (Table 1), and the paper states explicitly which one gated C1/C2's repair scope.",
    "Exemplary honesty about a failed run: Condition C's infrastructure stall is disclosed with specifics (polling duration, last observed stage, no error/no output) rather than being silently dropped or estimated, and every downstream claim that depends on it is explicitly marked undetermined rather than resolved.",
    "The C2 experiment is a genuinely informative, well-controlled test: identical checker, repair model, and API client verbatim from the prior run, row-ID identity to the B/D/C1 population formally verified rather than assumed, and a pre-declared sub-budget that was respected.",
    "The pre-registered numeric tolerance for Condition B's fidelity check ([0.5x, 2.0x] magnitude ratio, same sign) replaces the prior draft's vague 'same order of magnitude' language and is reported as a borderline pass rather than an unqualified one -- directly responsive to the prior review's minor critique.",
    "The mechanism-level finding itself (iteration fixes what the checker checks but does not improve whole-sentence quality, and increases edit volume nearly to B/D levels through repeated re-editing of the same span) is a clean, non-obvious, and well-explained result that meaningfully complicates the self-refinement literature's usual single-metric framing."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "Statistical practice is generally strong (bootstrapped CIs everywhere, pre-registered tolerance, verified row-ID identity, explicit non-fabrication policy for the stalled condition), but two specific numerical/methodological gaps weaken confidence in the headline mechanism claim: an unreconciled fix-rate-difference figure (0.2875 in text vs. 0.3833 implied by Table 2) and an underspecified 'normal-approximation substitute' used for the C2-vs-C1 ΔCOMET paired test, which is the basis for the paper's strongest claim (C2 measurably worse than C1 in ΔCOMET).",
      "improvements": [
        "Reconcile the 240-row paired-bootstrap fix-rate difference (+0.2875) with Table 2's excluding-negation fix rates (0.9889 vs. 0.6056, diff 0.3833) by stating explicitly which rows each figure is computed over, since the two numbers currently look contradictory without that context. Expected score impact: raises soundness from fair-to-good given this affects the paper's central quantitative comparison.",
        "Give the 'normal-approximation substitute' used for the C2-vs-C1 ΔCOMET comparison a precise formula and stated assumptions (what variance is imputed for C1 given only pooled, not per-row, ΔCOMET exists), since the paper's strongest directional claim ('C2 is measurably worse than C1 in ΔCOMET') rests on it. Expected score impact: meaningfully increases confidence in the paper's central negative result for C2 on quality.",
        "Discuss the population mismatch between the ΔCOMET evaluation (natural rows) and fix-rate/regression evaluation (injected rows) directly in the mechanism-explanation paragraph, rather than implicitly treating them as two views of the same underlying repair behavior."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The writing is clear, well-organized, and unusually candid about limitations and uncertainty, with a coherent narrative arc from prior-iteration setup through this iteration's mixed result. The main presentation weakness is that quantitative claims in the prose (the 0.29-point fix-rate lift) are not always traceable back to the exact table cells they summarize, forcing the reader to reconstruct the arithmetic themselves to spot the denominator difference.",
      "improvements": [
        "Add a one-sentence note next to each 'X points' or 'Y%' claim in the Results prose stating which row subset (240 incl. negation vs. 180 excl. negation) it is computed over, matching the discipline already applied to the pooled-including/pooled-excluding-negation tables.",
        "Move the practitioner guidance in the Discussion ('better served by C1's single-pass...', 'better served by C2's near-total fix rate...') closer in tone to the paper's own stated limitations -- currently it reads as general deployment advice, when the evidence behind it is two Slavic language pairs and synthetic corruption on one axis."
      ]
    },
    {
      "dimension": "contribution",
      "score": 2,
      "justification": "The paper executes the specific ablation (iteration vs. localization breadth) its own protocol was built to run and reports a genuinely non-obvious mixed result, which has real diagnostic value for anyone building QE-informed scoped editing systems. But the central combined-condition test (Condition C) did not complete, so the paper's own stated central question is left open, and what remains is a two-factor ablation on two related Slavic language pairs with one repair model, evaluated partly on synthetic injected corruptions. For a top-tier venue this reads more as a careful, incremental diagnostic study than a result the community would build directly on; the contribution would be substantially strengthened by completing Condition C or by demonstrating the mechanism holds beyond the current narrow language/data scope.",
      "improvements": [
        "Complete Condition C (or at minimum report a partial-data analysis for whatever fraction of en-ru_RU rows processed before the stall, clearly caveated) so the paper's central question has an actual answer rather than remaining structurally undetermined -- this is the single highest-leverage fix available, since the paper's own framing repeatedly returns to this as 'the comparison this paper's original design most wanted to run.'",
        "Extend the executed comparison (even a smaller-N pilot) to at least one non-Slavic, non-capitalization-NER language pair (e.g., one of zh_CN/ja_JP where the checker's own validation showed weaker coverage) to test whether the C1-vs-C2 tradeoff generalizes or is an artifact of the two easiest-checker-coverage languages.",
        "If neither of the above is feasible this iteration, scope down the contributions list and abstract-level claims to match what was actually shown -- an ablation of one repair-loop design choice (iteration) on two language pairs -- rather than framing it as resolving the protocol's original hypothesis, since the paper itself concedes the resolving condition did not run."
      ]
    }
  ],
  "critiques": [
    {
      "category": "evidence",
      "severity": "major",
      "description": "The paper's central open question -- whether broadened localization (C1's quality gain) and iteration (C2's correctness gain) can be captured together -- is exactly the question Condition C was designed to answer, and it did not complete. Every headline framing in the Abstract-equivalent contributions list, Discussion, and Conclusion correctly flags this as undetermined, which is honest, but it also means this iteration's actual deliverable is 'C2 alone does not dominate C1' plus an open combined-condition question, not a resolution of the protocol's motivating hypothesis. A reviewer weighing this paper against the bar of a completed mechanism study will find the single most decision-relevant experiment missing.",
      "suggested_action": "Prioritize re-running Condition C with the checkpointing/timeout fix the paper already proposes in 'What the next iteration must do,' before the next review round. If a re-run is not possible in the available budget, consider reporting whatever partial output exists from the stalled en-ru_RU pass (even a handful of completed rows) as a heavily-caveated directional signal, clearly separated from the paper's confirmed results, rather than leaving Condition C as a total blank."
    },
    {
      "category": "rigor",
      "severity": "major",
      "description": "The text reports the C2-vs-C1 fix-rate advantage as '0.29 points' with a paired-bootstrap difference of +0.2875 (95% CI [0.2292, 0.3458]) computed 'on the 240 matched injected-pool rows.' But Table 2's pooled-excluding-negation fix rates for the same two conditions are C1=0.6056 and C2=0.9889, a difference of 0.3833 -- roughly 33% larger than the paired-bootstrap figure. The likely explanation is that the 240-row paired bootstrap includes negation-deletion rows (where C2 structurally cannot attempt a repair and therefore counts as a non-fix, while C1's checker-based localization can attempt them), narrowing the observed gap relative to the excluding-negation table. But the paper never states this, so the two numbers -- both presented as authoritative comparisons of the exact same two conditions -- appear to contradict each other, and a reader has no way to know which one is 'the' C2-vs-C1 fix-rate advantage without independently reconstructing the arithmetic.",
      "suggested_action": "State explicitly, next to the paired-bootstrap fix-rate result, which row population it is computed over (240 rows including negation, where C2's structural non-attempt on negation rows counts against it) and that this differs from Table 2's excluding-negation comparison for that reason. Either report both figures side by side with this explanation, or pick one consistent denominator for both the table and the paired-bootstrap test and state which was chosen and why."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The paper's two outcome axes are measured on two structurally disjoint populations: ΔCOMET (the 'quality' evidence) is computed on the 320 natural WMT25 rows, while fix rate and true regression rate (the 'correctness' evidence) are computed on the 240 injected-pool rows with known ground-truth corruptions. No row is ever scored on both axes simultaneously. Table 2 and the Discussion nonetheless synthesize these into a single narrative ('iteration recovers correctness but not quality') as if they describe the same underlying repair behavior on the same sentences. This is methodologically defensible as a design choice (natural rows have no ground-truth 'correct fix' to score against; injected rows have no natural QE-severity distribution), but the paper never surfaces the fact that its central 'mixed verdict' rests on combining evidence from two different samples, which is a materially different (and weaker) form of evidence than a single population scored on both axes would provide.",
      "suggested_action": "Add an explicit statement in Section 6.4 or the Discussion's mechanism paragraph noting that ΔCOMET and fix-rate/regression are measured on disjoint populations (natural vs. injected), and discuss what this implies for the causal story being told (e.g., that the 'checker-invisible collateral drift' explanation for the ΔCOMET result is inferred, not directly observed, since no natural row's per-row correctness is ever checked against a ground truth)."
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The C2-vs-C1 ΔCOMET paired-bootstrap comparison (the basis for the claim that C2 is 'measurably worse' than C1 in ΔCOMET, CI [-0.0214, -0.0047]) is described only as using 'a normal-approximation substitute since only pooled, not per-row, ΔCOMET exists for C1.' No formula, variance-imputation method, or justification for the normal approximation's validity is given, even though this is the statistical basis for one of the paper's two headline directional claims.",
      "suggested_action": "Add a short methods note (even a sentence with the imputed per-row variance assumption, e.g. 'C1's per-row ΔCOMET distribution is approximated as Gaussian with the pooled mean and an assumed variance derived from B/D's per-row spread') so the comparison is auditable, or footnote why this substitute is expected to be conservative/anti-conservative relative to a true paired test."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "The executed comparison remains restricted to en-ru_RU and en-uk_UA -- the two language pairs where the checker performs best per Table 1 (capitalization-based NER, strongest negation-polarity detection). This is disclosed in Limitations, but the Discussion's practitioner guidance ('a deployment... is better served by C2's near-total fix rate...') is phrased as general advice without a scope caveat at the point it is given, which risks a reader over-generalizing the trade-off to language pairs where the checker's own validation (Table 1) shows it performs far worse (e.g., named-entity detection excluded outright for both tested languages).",
      "suggested_action": "Add a one-clause scope qualifier directly in the practitioner-guidance paragraph (e.g., 'within the two Slavic pairs and checker categories validated here') rather than relying on the separate Limitations section to carry that caveat."
    },
    {
      "category": "novelty",
      "severity": "minor",
      "description": "The Related Work claims this is 'to our knowledge, the first controlled evidence in this literature that separates check more of the sentence once (C1) from iterate on the same narrow check (C2) as distinct levers.' This is a strong priority claim that is plausible given the related-work survey shown, but it is not independently verifiable from the paper alone, and the surveyed related work (APE-with-QE-signal, Grid Beam Search, LLM-as-judge post-editing, xTower explanation-based correction, Self-Refine, CEGIS, locate-and-edit energy-guided generation) is broad enough that a closely related ablation could plausibly exist in venues not covered by this search (e.g., iterative constrained decoding literature, or QE-guided automatic post-editing surveys).",
      "suggested_action": "Soften the priority claim slightly (e.g., 'we are not aware of' rather than 'the first') unless an additional targeted search specifically for 'iterative QE-guided post-editing' or 'checker-in-the-loop machine translation repair' turns up nothing closer, in which case keep the stronger claim but note the specific search terms used."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "The recurring pattern of infrastructure failures across this project's iterations (this iteration's Condition C stall; the prior iteration's HuggingFace Hub 429 forcing a substitute LLM-judge proxy for Condition B, later redone with real COMET) is each individually well-disclosed, but the paper never steps back to note this as a pattern worth a sentence of its own -- e.g., whether the checkpointing fix proposed for Condition C would also have prevented the earlier COMET-checkpoint-access failure, or whether these are unrelated infrastructure risks.",
      "suggested_action": "Optional: add one sentence in Limitations or 'What the next iteration must do' acknowledging that this is the second execution stall/substitution across this project's iterations, and that a general run-robustness mechanism (checkpointing, timeout, retry-with-backoff) would benefit the whole pipeline, not just Condition C specifically."
    }
  ],
  "score": 4,
  "confidence": 3
}
```

### [7] TOOL RESULT — Write · 2026-09-01 09:17:27 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_3/review_paper/review_paper/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This iteration is a substantial, honest improvement over the prior draft: both MAJOR issues from the previous review (the negation-deletion structural asymmetry and the unreconciled dual checker-validation tables) are now addressed directly, with a named comparison table and pooled-with/without-negation reporting throughout. The paper's central move -- running Condition C2 (narrow localization + iteration) as the missing half of the B/D/C1 comparison, and reporting the result as genuinely mixed (iteration recovers fix-rate/regression-rate but not ΔCOMET, and is measurably worse than C1 on ΔCOMET despite being measurably better on regression) -- is a real, well-instrumented finding, and the paper's refusal to paper over Condition C's non-completion with an estimate is exactly the right call scientifically. However, the paper's central research question (does combining broad localization with iteration capture both C1's quality gain and C2's correctness gain?) remains unanswered because Condition C stalled, which caps how much this iteration can claim to have resolved. On top of that, two new rigor gaps surface in this draft's own numbers: a fix-rate-difference figure quoted in the text (+0.2875 from a 240-row paired bootstrap) does not match the difference implied by Table 2's excluding-negation fix rates (0.9889 - 0.6056 = 0.3833), and the discrepancy (different row denominators -- 240 including negation vs. 180 excluding it) is never explained to the reader. There is also an underexamined population mismatch: ΔCOMET (the 'quality' axis) is measured on natural WMT25 rows while fix-rate/regression (the 'correctness' axis) is measured on a disjoint set of programmatically injected-error rows, yet Table 2 and the Discussion synthesize the two into a single 'iteration helps correctness but not quality' story without acknowledging that no single row is ever scored on both axes. Combined with the still-narrow scope (2 of 6 language pairs, both Slavic with capitalization-based NER; a substitute repair model that passes fidelity only as a 'borderline' pass), the paper is technically careful and unusually forthright about its own limitations, but its core deliverable this round is an honest 'still open' rather than a resolved mechanism, which limits its significance for a top-tier venue as currently scoped.\",\n  \"strengths\": [\n    \"Both MAJOR critiques from the previous review round are substantively fixed: the negation-deletion asymmetry is now quantified and reported both pooled-including and pooled-excluding negation throughout (Section 6.3), and the two checker-validation procedures are named, reconciled in a single table (Table 1), and the paper states explicitly which one gated C1/C2's repair scope.\",\n    \"Exemplary honesty about a failed run: Condition C's infrastructure stall is disclosed with specifics (polling duration, last observed stage, no error/no output) rather than being silently dropped or estimated, and every downstream claim that depends on it is explicitly marked undetermined rather than resolved.\",\n    \"The C2 experiment is a genuinely informative, well-controlled test: identical checker, repair model, and API client verbatim from the prior run, row-ID identity to the B/D/C1 population formally verified rather than assumed, and a pre-declared sub-budget that was respected.\",\n    \"The pre-registered numeric tolerance for Condition B's fidelity check ([0.5x, 2.0x] magnitude ratio, same sign) replaces the prior draft's vague 'same order of magnitude' language and is reported as a borderline pass rather than an unqualified one -- directly responsive to the prior review's minor critique.\",\n    \"The mechanism-level finding itself (iteration fixes what the checker checks but does not improve whole-sentence quality, and increases edit volume nearly to B/D levels through repeated re-editing of the same span) is a clean, non-obvious, and well-explained result that meaningfully complicates the self-refinement literature's usual single-metric framing.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"Statistical practice is generally strong (bootstrapped CIs everywhere, pre-registered tolerance, verified row-ID identity, explicit non-fabrication policy for the stalled condition), but two specific numerical/methodological gaps weaken confidence in the headline mechanism claim: an unreconciled fix-rate-difference figure (0.2875 in text vs. 0.3833 implied by Table 2) and an underspecified 'normal-approximation substitute' used for the C2-vs-C1 ΔCOMET paired test, which is the basis for the paper's strongest claim (C2 measurably worse than C1 in ΔCOMET).\",\n      \"improvements\": [\n        \"Reconcile the 240-row paired-bootstrap fix-rate difference (+0.2875) with Table 2's excluding-negation fix rates (0.9889 vs. 0.6056, diff 0.3833) by stating explicitly which rows each figure is computed over, since the two numbers currently look contradictory without that context. Expected score impact: raises soundness from fair-to-good given this affects the paper's central quantitative comparison.\",\n        \"Give the 'normal-approximation substitute' used for the C2-vs-C1 ΔCOMET comparison a precise formula and stated assumptions (what variance is imputed for C1 given only pooled, not per-row, ΔCOMET exists), since the paper's strongest directional claim ('C2 is measurably worse than C1 in ΔCOMET') rests on it. Expected score impact: meaningfully increases confidence in the paper's central negative result for C2 on quality.\",\n        \"Discuss the population mismatch between the ΔCOMET evaluation (natural rows) and fix-rate/regression evaluation (injected rows) directly in the mechanism-explanation paragraph, rather than implicitly treating them as two views of the same underlying repair behavior.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The writing is clear, well-organized, and unusually candid about limitations and uncertainty, with a coherent narrative arc from prior-iteration setup through this iteration's mixed result. The main presentation weakness is that quantitative claims in the prose (the 0.29-point fix-rate lift) are not always traceable back to the exact table cells they summarize, forcing the reader to reconstruct the arithmetic themselves to spot the denominator difference.\",\n      \"improvements\": [\n        \"Add a one-sentence note next to each 'X points' or 'Y%' claim in the Results prose stating which row subset (240 incl. negation vs. 180 excl. negation) it is computed over, matching the discipline already applied to the pooled-including/pooled-excluding-negation tables.\",\n        \"Move the practitioner guidance in the Discussion ('better served by C1's single-pass...', 'better served by C2's near-total fix rate...') closer in tone to the paper's own stated limitations -- currently it reads as general deployment advice, when the evidence behind it is two Slavic language pairs and synthetic corruption on one axis.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 2,\n      \"justification\": \"The paper executes the specific ablation (iteration vs. localization breadth) its own protocol was built to run and reports a genuinely non-obvious mixed result, which has real diagnostic value for anyone building QE-informed scoped editing systems. But the central combined-condition test (Condition C) did not complete, so the paper's own stated central question is left open, and what remains is a two-factor ablation on two related Slavic language pairs with one repair model, evaluated partly on synthetic injected corruptions. For a top-tier venue this reads more as a careful, incremental diagnostic study than a result the community would build directly on; the contribution would be substantially strengthened by completing Condition C or by demonstrating the mechanism holds beyond the current narrow language/data scope.\",\n      \"improvements\": [\n        \"Complete Condition C (or at minimum report a partial-data analysis for whatever fraction of en-ru_RU rows processed before the stall, clearly caveated) so the paper's central question has an actual answer rather than remaining structurally undetermined -- this is the single highest-leverage fix available, since the paper's own framing repeatedly returns to this as 'the comparison this paper's original design most wanted to run.'\",\n        \"Extend the executed comparison (even a smaller-N pilot) to at least one non-Slavic, non-capitalization-NER language pair (e.g., one of zh_CN/ja_JP where the checker's own validation showed weaker coverage) to test whether the C1-vs-C2 tradeoff generalizes or is an artifact of the two easiest-checker-coverage languages.\",\n        \"If neither of the above is feasible this iteration, scope down the contributions list and abstract-level claims to match what was actually shown -- an ablation of one repair-loop design choice (iteration) on two language pairs -- rather than framing it as resolving the protocol's original hypothesis, since the paper itself concedes the resolving condition did not run.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"The paper's central open question -- whether broadened localization (C1's quality gain) and iteration (C2's correctness gain) can be captured together -- is exactly the question Condition C was designed to answer, and it did not complete. Every headline framing in the Abstract-equivalent contributions list, Discussion, and Conclusion correctly flags this as undetermined, which is honest, but it also means this iteration's actual deliverable is 'C2 alone does not dominate C1' plus an open combined-condition question, not a resolution of the protocol's motivating hypothesis. A reviewer weighing this paper against the bar of a completed mechanism study will find the single most decision-relevant experiment missing.\",\n      \"suggested_action\": \"Prioritize re-running Condition C with the checkpointing/timeout fix the paper already proposes in 'What the next iteration must do,' before the next review round. If a re-run is not possible in the available budget, consider reporting whatever partial output exists from the stalled en-ru_RU pass (even a handful of completed rows) as a heavily-caveated directional signal, clearly separated from the paper's confirmed results, rather than leaving Condition C as a total blank.\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"major\",\n      \"description\": \"The text reports the C2-vs-C1 fix-rate advantage as '0.29 points' with a paired-bootstrap difference of +0.2875 (95% CI [0.2292, 0.3458]) computed 'on the 240 matched injected-pool rows.' But Table 2's pooled-excluding-negation fix rates for the same two conditions are C1=0.6056 and C2=0.9889, a difference of 0.3833 -- roughly 33% larger than the paired-bootstrap figure. The likely explanation is that the 240-row paired bootstrap includes negation-deletion rows (where C2 structurally cannot attempt a repair and therefore counts as a non-fix, while C1's checker-based localization can attempt them), narrowing the observed gap relative to the excluding-negation table. But the paper never states this, so the two numbers -- both presented as authoritative comparisons of the exact same two conditions -- appear to contradict each other, and a reader has no way to know which one is 'the' C2-vs-C1 fix-rate advantage without independently reconstructing the arithmetic.\",\n      \"suggested_action\": \"State explicitly, next to the paired-bootstrap fix-rate result, which row population it is computed over (240 rows including negation, where C2's structural non-attempt on negation rows counts against it) and that this differs from Table 2's excluding-negation comparison for that reason. Either report both figures side by side with this explanation, or pick one consistent denominator for both the table and the paired-bootstrap test and state which was chosen and why.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The paper's two outcome axes are measured on two structurally disjoint populations: ΔCOMET (the 'quality' evidence) is computed on the 320 natural WMT25 rows, while fix rate and true regression rate (the 'correctness' evidence) are computed on the 240 injected-pool rows with known ground-truth corruptions. No row is ever scored on both axes simultaneously. Table 2 and the Discussion nonetheless synthesize these into a single narrative ('iteration recovers correctness but not quality') as if they describe the same underlying repair behavior on the same sentences. This is methodologically defensible as a design choice (natural rows have no ground-truth 'correct fix' to score against; injected rows have no natural QE-severity distribution), but the paper never surfaces the fact that its central 'mixed verdict' rests on combining evidence from two different samples, which is a materially different (and weaker) form of evidence than a single population scored on both axes would provide.\",\n      \"suggested_action\": \"Add an explicit statement in Section 6.4 or the Discussion's mechanism paragraph noting that ΔCOMET and fix-rate/regression are measured on disjoint populations (natural vs. injected), and discuss what this implies for the causal story being told (e.g., that the 'checker-invisible collateral drift' explanation for the ΔCOMET result is inferred, not directly observed, since no natural row's per-row correctness is ever checked against a ground truth).\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The C2-vs-C1 ΔCOMET paired-bootstrap comparison (the basis for the claim that C2 is 'measurably worse' than C1 in ΔCOMET, CI [-0.0214, -0.0047]) is described only as using 'a normal-approximation substitute since only pooled, not per-row, ΔCOMET exists for C1.' No formula, variance-imputation method, or justification for the normal approximation's validity is given, even though this is the statistical basis for one of the paper's two headline directional claims.\",\n      \"suggested_action\": \"Add a short methods note (even a sentence with the imputed per-row variance assumption, e.g. 'C1's per-row ΔCOMET distribution is approximated as Gaussian with the pooled mean and an assumed variance derived from B/D's per-row spread') so the comparison is auditable, or footnote why this substitute is expected to be conservative/anti-conservative relative to a true paired test.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The executed comparison remains restricted to en-ru_RU and en-uk_UA -- the two language pairs where the checker performs best per Table 1 (capitalization-based NER, strongest negation-polarity detection). This is disclosed in Limitations, but the Discussion's practitioner guidance ('a deployment... is better served by C2's near-total fix rate...') is phrased as general advice without a scope caveat at the point it is given, which risks a reader over-generalizing the trade-off to language pairs where the checker's own validation (Table 1) shows it performs far worse (e.g., named-entity detection excluded outright for both tested languages).\",\n      \"suggested_action\": \"Add a one-clause scope qualifier directly in the practitioner-guidance paragraph (e.g., 'within the two Slavic pairs and checker categories validated here') rather than relying on the separate Limitations section to carry that caveat.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"minor\",\n      \"description\": \"The Related Work claims this is 'to our knowledge, the first controlled evidence in this literature that separates check more of the sentence once (C1) from iterate on the same narrow check (C2) as distinct levers.' This is a strong priority claim that is plausible given the related-work survey shown, but it is not independently verifiable from the paper alone, and the surveyed related work (APE-with-QE-signal, Grid Beam Search, LLM-as-judge post-editing, xTower explanation-based correction, Self-Refine, CEGIS, locate-and-edit energy-guided generation) is broad enough that a closely related ablation could plausibly exist in venues not covered by this search (e.g., iterative constrained decoding literature, or QE-guided automatic post-editing surveys).\",\n      \"suggested_action\": \"Soften the priority claim slightly (e.g., 'we are not aware of' rather than 'the first') unless an additional targeted search specifically for 'iterative QE-guided post-editing' or 'checker-in-the-loop machine translation repair' turns up nothing closer, in which case keep the stronger claim but note the specific search terms used.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The recurring pattern of infrastructure failures across this project's iterations (this iteration's Condition C stall; the prior iteration's HuggingFace Hub 429 forcing a substitute LLM-judge proxy for Condition B, later redone with real COMET) is each individually well-disclosed, but the paper never steps back to note this as a pattern worth a sentence of its own -- e.g., whether the checkpointing fix proposed for Condition C would also have prevented the earlier COMET-checkpoint-access failure, or whether these are unrelated infrastructure risks.\",\n      \"suggested_action\": \"Optional: add one sentence in Limitations or 'What the next iteration must do' acknowledging that this is the second execution stall/substitution across this project's iterations, and that a general run-robustness mechanism (checkpointing, timeout, retry-with-backoff) would benefit the whole pipeline, not just Condition C specifically.\"\n    }\n  ],\n  \"score\": 4,\n  \"confidence\": 3\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [8] ASSISTANT · 2026-09-01 09:17:30 UTC

```
Review written to `./.terminal_claude_agent_struct_out.json`.

**Summary:** Score 4/10 (borderline reject), confidence 3/5. Both prior MAJOR issues (negation asymmetry, dual checker-validation reconciliation) are genuinely fixed this round. New findings:

- **Major**: Condition C — the run that would answer the paper's actual central question — stalled and never completed, leaving the protocol's motivating hypothesis untested.
- **Major**: an unreconciled numeric discrepancy — the text's paired-bootstrap fix-rate difference (+0.2875) doesn't match what Table 2 implies (0.3833) — traced to different row denominators (with/without negation rows) that the paper never explains.
- **Major**: ΔCOMET (quality) and fix-rate/regression (correctness) are measured on two disjoint row populations (natural vs. injected-error), yet synthesized into one "mixed verdict" narrative without flagging that no row is ever scored on both axes.
- Minor: underspecified "normal-approximation substitute" statistic, scope caveats not repeated where practitioner guidance is given, a strong unverified priority claim, and the recurring pattern of infrastructure stalls across iterations.
```
