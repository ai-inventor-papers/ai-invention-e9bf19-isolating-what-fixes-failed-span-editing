# review_hypo — create_idea

> Phase: `hypo_loop` · round 2 · `review_hypo`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 04:47:53 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
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
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first
- Screen the hypothesis for prior art before any compute is spent. Search the web for the proposed idea, its method name, and its central claim. If the idea already exists, say so and name the source — this is the cheapest point in the pipeline to catch it
- Distinguish a genuinely new idea from a restatement of known work in new vocabulary. Coining a term for an existing method is not originality, and should be scored as a major issue
- Judge ambition against what the request left OPEN. The less the request constrained, the more of that space the hypothesis was expected to claim; a safe, small study in answer to a wide-open question is a major issue, not a minor one
- Reject measurement dressed as contribution: an established measure, instrument or method applied to more cases — more models, languages, periods, countries, corpora or settings — is a table, not a finding. Say so plainly and ask for a claim that would change what someone in the field does or believes
- Ask whether the hypothesis is POSITIVE BY DESIGN — is there a mechanism that predicts the effect, or is the outcome a coin flip? If the direction is genuinely unknown, require that both outcomes be informative, or the run risks ending with an uninformative negative result

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

<hypothesis>
kind: hypothesis
title: Certified Loops Fix Failed Span Editing
hypothesis: >-
  Having now read the WMT25 Task 3 systems in full rather than from snippets, the field has already tried single-shot, QE-guided
  scoped span editing for MT correction ('mask the flagged substring, ask an LLM to fill it in, do not touch anything else')
  and, across the shared task, it measurably UNDERPERFORMS full retranslation: the one directly-reported scoped-editing system
  scored ΔCOMET = −0.0108 (a net quality loss) against a ΔCOMET = +0.0201 winner that simply retranslated from scratch and
  picked the best candidate, and the organizers attribute this specifically to two failure modes — edits that introduce new
  artifacts, and edits that miss cascading errors outside the single flagged span. We hypothesize that both failure modes
  are consequences of the single-shot, no-verification design (an edit is applied once and never checked), not of scoping
  itself, and that replacing single-shot masked-fill editing with a Counterexample-Guided-Inductive-Synthesis-style loop —
  a deterministic content-invariant checker (named entities, numbers/units/dates, negation polarity, quantifier scope) that
  (i) flags ALL failing invariants per sentence rather than one QE-flagged span, addressing the cascading-error failure, and
  (ii) re-checks after every localized repair and only stops once every invariant passes or a bound is hit, addressing the
  introduced-artifact failure — will turn scoped editing net-positive: achieving non-negative mean quality change and a lower
  true (human-confirmed) regression rate than a faithfully-reproduced single-shot masked-fill baseline, at comparable or higher
  fix rate, and without simply reducing to full retranslation's edit volume.
motivation: >-
  This is not a hypothetical gap: WMT25 Task 3 is a live, adversarial test of exactly this idea, and the specific scoped-editing
  design it tested (localize with QE explanations, mask, single LLM fill-in pass, no re-check) lost to naive full retranslation
  on the shared task's own primary metric. That is a documented negative result for 'just scope the edit,' not evidence the
  problem is solved — and the organizers' own diagnosis (introduced artifacts; missed cascading errors) points at exactly
  the two things a verify-and-iterate loop is designed to catch that a single masked-fill pass structurally cannot: it never
  re-examines its own edit, and it only ever looks at the one span a QE model flagged. If a deterministic, multi-invariant,
  iterate-to-certificate loop can convert this specific documented failure into a net-positive result, that is an actionable
  finding about which piece of the pipeline (localization signal vs. verification loop) is load-bearing — directly useful
  in regulated, terminology-heavy domains (legal, medical, financial) where a corrupted number or flipped negation is a severe
  failure independent of an aggregate COMET delta, and where an explicit per-invariant certificate is a more auditable deliverable
  than a QE confidence score.
assumptions:
- >-
  Semantically load-bearing content — named entities, numbers/units/dates, negation polarity, and quantifier scope — can be
  extracted from a source sentence and checked deterministically (NER, regex, cue lists, alignment) against a candidate translation,
  and this checker's own precision/recall against a human-annotated sample is high enough that its verdicts, not raw flags,
  can be used as ground truth for scoring both conditions.
- >-
  The WMT25 secondary system's masked-fill design (mask a QE-flagged substring with a __BLANK__ token, single LLM completion
  pass, conditional severity-based masking heuristic) can be faithfully reproduced as a baseline at the scale available to
  this run, including its conditional-masking heuristic, so the comparison is against the actual documented failure rather
  than a strawman.
- >-
  A failed invariant check can be localized to a target-language span precise enough to scope a repair (verifiable against
  human-annotated error regions), and an LLM can be instructed to revise only that span across successive iterations without
  the iterate-to-certificate loop degenerating into full-sentence regeneration by the final pass.
- >-
  A meaningful fraction of the WMT25 Task 3 test set's real errors (across its six language pairs and five domains) fall into
  these four checkable categories rather than being purely stylistic, and a modest set of injected invariant-violating errors,
  reported separately from natural ones, gives adequate power where natural incidence is low.
- >-
  COMET (or a comparable reference-based/QE metric) computed on this dataset gives a fair net-quality comparison between conditions,
  mirroring the shared task's own primary ΔCOMET metric closely enough that a result here speaks to the same documented failure
  mode.
investigation_approach: >-
  Build a deterministic content-invariant extractor/checker for four categories (named entities via NER; numbers/units/dates
  via regex plus cross-lingual matching; negation polarity via per-language cue lists; quantifier scope via a closed-class
  word list), and validate it against a held-out, human-annotated sample of source-target pairs per category, reporting precision/recall
  before using it to score anything else. Use the WMT25 Task 3 test data itself (6,000 English-to-{Chinese, Czech, Japanese,
  Icelandic, Russian, Ukrainian} machine translations across news/social/speech/literary/dialogue domains, with provided QE
  error-span annotations) plus a modest, realism-justified set of injected invariant-violating errors for statistical power
  on low-incidence categories. Run two conditions matched on maximum edit-pass budget: (B) a faithful reproduction of the
  WMT25 secondary system — QE-flagged substrings masked with __BLANK__, conditional severity-based masking heuristic, one
  LLM fill-in pass, no re-verification; (C) the proposed certified loop — the deterministic checker flags every failing invariant
  (not just the QE-flagged span), the LLM repairs only each flagged span, the checker re-verifies, and the loop iterates until
  all invariants pass or the same maximum pass count as B is exhausted. For both, measure: (i) fix rate for the four checkable
  categories, scored on all flagged repairs and on the human-confirmed subset; (ii) true (human-confirmed) regression rate
  — invariants correct pre-repair that become violated post-repair; (iii) net translation-quality change via COMET (or a comparable
  metric), reported the same way as ΔCOMET so it is directly comparable to the WMT25 secondary system's −0.0108; (iv) edit
  volume / Gain-to-Edit-ratio-style efficiency, to check that any gain is not simply C converging to full-sentence rewriting;
  (v) LLM calls/tokens per sentence for both conditions. Report all headline metrics separately for the natural-error and
  injection-augmented subsets, and separately per language pair given the WMT25 finding that results varied substantially
  by language.
success_criteria: >-
  Confirmed if condition C achieves a non-negative mean net-quality change (in clear contrast to B's replicated −0.0108-scale
  loss) together with a true regression rate substantially and statistically significantly lower than B's, at a fix rate comparable
  to or higher than B's, on the natural-error subset (not only the injected one) and without C's per-sentence edit volume
  collapsing to that of full retranslation. Disconfirmed if C's net-quality change remains negative or statistically indistinguishable
  from B's replicated result (meaning single-shot masked-fill's failure is inherent to scoping errors this narrowly at all,
  not to the lack of verification/iteration — i.e., the field's negative result generalizes past a fixable design flaw), or
  if C's fix rate is substantially lower than B's (the four-category checker's coverage is too narrow relative to what the
  QE explanations catch). A result where C is net-positive only on the injected subset but not on WMT25's real errors would
  be a partial disconfirmation, indicating the deterministic checker's advantage is confined to synthetically-clean error
  types rather than errors as they actually occur across these six language pairs.
related_works:
- >-
  Padmanabhan 2025, 'Can QE-informed (Re)Translation lead to Error Correction?' (WMT25 Task 3 submission, read in full): reports
  the actual measured result this hypothesis is built on — a single-shot, QE-explanation-guided masked-fill scoped-editing
  system (__BLANK__-token substitution with a conditional severity-based masking heuristic, aimed at maximizing Gain-to-Edit
  ratio) scored ΔCOMET = −0.0108 (a net quality loss, roughly −0.7% to −1.4% degradation per language pair) versus ΔCOMET
  = +0.0201 for a QE-as-selector retranslation-from-scratch system on the same leaderboard. This is not a comparison this
  hypothesis invents; it is the documented failure this hypothesis's condition C is designed to fix, and no re-verification
  or iteration step exists anywhere in the published system.
- >-
  WMT25 Findings paper (Automated Translation Quality Evaluation Systems shared task overview, read in full): reports across
  Task 3 submissions generally that full retranslation often outperformed conservative span-level edits, with targeted fixes
  'sometimes introduc[ing] artifacts or fail[ing] to address cascading errors from upstream translation problems' — the two
  specific failure modes this hypothesis's checker (catches all failing invariants, not one QE-flagged span) and re-verification
  loop (catches introduced artifacts before stopping) directly target.
- >-
  Deoghare et al. 2023 (EMNLP Findings, 'Quality Estimation-Assisted Automatic Post-Editing', read in full): NOT a scoped
  span-editing system as initially assumed — it is a jointly-trained encoder-decoder APE model where word-level QE serves
  as an auxiliary multi-task training signal, and the 'QE as APE Guide' variant passes QE tags as additional decoder input;
  in every variant the decoder still generates the full target sentence from scratch. It reduces but does not eliminate over-correction
  (best variant: 18.30 vs. 19.39 TER for the QE-unassisted baseline on En-Mr) without ever freezing non-flagged spans, which
  is a materially different mechanism from this hypothesis's localized, non-regenerative repair.
- >-
  Deoghare et al. 2025 ('Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE', read in full): uses Grid
  Beam Search to force QE-tagged 'OK' spans to appear as lexical constraints in the decoder's output, but the decoder retains
  full freedom to reorder and rephrase around them — this is soft-constrained full regeneration, not frozen-span editing,
  and oracle-vs-predicted-tag gaps of 0.3–1.3 TER points show the method's ceiling is bounded by QE tag accuracy in a way
  the checker-based approach's precision/recall validation step is designed to make explicit and auditable.
- >-
  LaSEr-Edit (Localized Span-level Error Editing with Energy-based Localization) and Faithful Autoformalization via Roundtrip
  Verification and Repair: the two closest analogues to the proposed mechanism outside MT — the former for localized (though
  learned-localizer) editing over full regeneration in general controlled-text-generation, the latter for an iterate-to-certificate
  stopping rule in NL-to-formal-logic translation verified by logical equivalence. Neither is in machine translation, and
  neither has been tested against a documented real-world failure of naive scoped editing the way this hypothesis's condition
  B/C comparison is.
inspiration: >-
  Cross-field transfer from formal methods and program synthesis, specifically Counterexample-Guided Inductive Synthesis (CEGIS):
  a synthesizer proposes a candidate, a verifier either certifies it or returns a concrete counterexample that scopes the
  next refinement, and the loop terminates on an explicit certificate rather than a fixed pass count. Reading the actual WMT25
  Task 3 systems (not just their titles) showed that MT researchers have already tried the surface-level version of scoped
  editing — mask a flagged span, fill it in once — and it lost to full retranslation, with the organizers naming exactly the
  two failure modes CEGIS's missing pieces address: no verification step (so an introduced artifact is never caught) and a
  single localization signal scoped to one span (so cascading errors elsewhere go unaddressed). The transplant this hypothesis
  tests is therefore not 'add scoping to MT self-correction' — that has been tried and shown to fail — but specifically 'add
  a verifier and an iterate-to-certificate loop to the scoping MT researchers already tried,' isolating whether the documented
  failure is fixable or fundamental.
terms:
- term: Content invariant
  definition: >-
    A piece of source-sentence meaning — a named entity, a number/unit/date, a negation polarity marker, or a quantifier —
    that must be preserved in any faithful translation and can be checked deterministically (via NER, regex, cue lists, or
    alignment) rather than judged by a learned QE model.
- term: Single-shot masked-fill editing (condition B)
  definition: >-
    The WMT25 Task 3 secondary-system design this hypothesis directly reproduces as a baseline: a QE-flagged error substring
    is masked with a __BLANK__ token, an LLM fills it in once, and no step re-verifies the result — measured in the literature
    at ΔCOMET = −0.0108, a net quality loss.
- term: Certificate (translation)
  definition: >-
    A translation for which every extracted content invariant has been checked by the deterministic checker and passes; an
    explicit, checkable, auditable stopping condition absent from both holistic reflect-and-regenerate loops and single-shot
    masked-fill editing.
- term: True (human-confirmed) regression rate
  definition: >-
    The fraction of content invariants that were correctly rendered before a repair step and become violated after it, scored
    only against human-confirmed violations so the metric is not inflated by checker or QE-explanation false positives — this
    is the quantitative form of the 'introduced artifacts' failure mode the WMT25 organizers reported qualitatively.
- term: Cascading-error miss
  definition: >-
    The WMT25-reported failure where a scoped edit fixes the one span a QE model flagged but leaves other, unflagged errors
    in the same sentence untouched; addressed here by having the checker enumerate every failing invariant per sentence rather
    than acting on a single localization signal.
summary: >-
  Reading the actual WMT25 Task 3 systems (not just their abstracts) shows single-shot, QE-guided scoped span editing for
  MT correction has already been tried and lost to full retranslation (ΔCOMET −0.0108 vs. +0.0201), with the organizers blaming
  introduced artifacts and missed cascading errors; this hypothesis borrows counterexample-guided synthesis from formal methods
  to test whether adding a deterministic multi-invariant checker and an iterate-to-certificate verification loop — the two
  things a single masked-fill pass structurally lacks — can turn that documented failure into a net-positive result.
</hypothesis>

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the hypothesis is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<previous_hypothesis>
The hypothesis from the PREVIOUS iteration (before the revision under review).
Use this to classify how the current hypothesis relates to it (see the H↔H
edge instructions in the task).

kind: hypothesis
title: Certified Local Patches for Translation
hypothesis: >-
  Current LLM translation self-refine loops (reflect, critique, regenerate) improve average quality by having the model holistically
  judge and then rewrite the ENTIRE segment, with no explicit, checkable specification of what must be preserved and no guarantee
  the rewrite stays local. Replacing this with a Counterexample-Guided-Inductive-Synthesis-style loop — a deterministic cross-lingual
  checker that extracts source-side content invariants (named entities, numbers/units/dates, negation polarity, quantifier
  scope) and verifies each against the draft translation, localizing any failure to a specific target span and repairing ONLY
  that span, then re-checking until every invariant passes (a certificate) or a bound is hit — will match or exceed the current
  fix rate for these invariant categories while producing substantially fewer NEW invariant violations introduced into previously-correct
  spans, compared to the field's current holistic reflect-and-regenerate baselines.
motivation: >-
  Reflection-based self-correction (ReflectMT, Reflective Translation, TEaR) is the field's current mechanism for improving
  LLM translation quality, and it works by having the model produce a free-form, holistic critique and then regenerate the
  full segment. This is exactly the failure shape identified in adjacent controlled-generation work: full regeneration 'may
  introduce new violations that were not present in the original output,' especially when multiple constraints must hold jointly.
  That risk has been named and measured for toxicity/contradiction/consistency constraints, and separately, localized (non-regenerative)
  editing has been shown to retain far more of the source than full rewrites in a source-rewriting RL setting — but no work
  measures this specific regression risk, using a deterministic, checkable set of cross-lingual content invariants, inside
  machine translation self-correction itself. As agentic reflect-and-refine pipelines become the default way LLMs are pushed
  to production-quality translation, and as translation demand concentrates in regulated, terminology- and fact-heavy domains
  (legal, medical, financial) where a wrong number, flipped negation, or corrupted entity is a severe failure regardless of
  the average quality score, an explicit, checkable notion of 'this translation certifiably preserves X, Y, Z' rather than
  only a holistic quality score becomes an increasingly practical need.
assumptions:
- >-
  Semantically load-bearing content — named entities, numbers/units/dates, negation polarity, and quantifier scope — can be
  extracted from a source sentence and checked for presence/correct rendering in a candidate translation using deterministic
  or lightweight cross-lingual matching (NER, number/date regex, negation-cue lists, word alignment), without requiring a
  learned judge model for these specific categories.
- >-
  A failed check on one of these categories can be localized to a specific target-language span (the region around the missing
  or altered entity, number, or negation cue) with enough precision to scope a repair prompt to that span alone.
- >-
  An LLM can be reliably instructed to revise only a marked span while leaving the rest of the target sentence untouched,
  when given the span location and the specific violated invariant.
- >-
  A holistic reflect-and-regenerate baseline representative of current practice (single free-form critique, full-segment rewrite,
  in the style of ReflectMT/Reflective Translation) can be reproduced with an LLM at the scale available to this run, to serve
  as a fair comparison point.
- >-
  A meaningful fraction of realistic translation errors in a general-domain evaluation set fall into these four checkable
  categories, rather than being purely stylistic or register errors these invariants cannot capture, enough to measure a difference
  between the two repair strategies.
investigation_approach: >-
  Build a deterministic content-invariant extractor for source sentences covering four categories drawn from the field's own
  critical-error taxonomy (named entities via NER; numbers/units/dates via regex plus cross-lingual number/date matching;
  negation polarity via per-language cue lists; quantifier scope via a small closed-class word list). On source-target pairs
  from an existing MT evaluation set (natural errors plus a modest set of deliberately injected invariant-violating errors
  for statistical power), run two conditions: (A) a holistic reflect-and-regenerate baseline — one free-form LLM critique
  of the full draft translation followed by a full-segment rewrite, matching current published self-refine designs; (B) the
  proposed certified local-patch loop — extract invariants from the source, check each against the draft translation, and
  for every failing invariant prompt the LLM to revise only the localized span responsible, re-checking afterward and iterating
  until all invariants pass (the certificate) or a small max-iteration bound is reached. For both conditions measure: (i)
  the fraction of invariant violations present in the draft that get fixed, (ii) the fraction of NEW invariant violations
  introduced into spans that were correct in the draft (the regression rate), and (iii) overall translation quality via COMET,
  to confirm the local-patch approach is not trading quality for safety.
success_criteria: >-
  Confirmed if condition B achieves a fix rate for invariant violations comparable to or higher than condition A, while its
  regression rate (newly introduced violations in previously-correct spans) is substantially and statistically significantly
  lower than condition A's, with no material COMET regression relative to A. Disconfirmed if the regression rates of A and
  B are statistically indistinguishable (meaning LLM edits 'leak' outside the marked span regardless of instruction, so locality
  does not help in practice), or if B's fix rate is substantially lower than A's (meaning the deterministic four-category
  checker's coverage is too narrow relative to what holistic critique catches, so the certificate is cheap but incomplete).
related_works:
- >-
  ReflectMT and Reflective Translation for Low-Resource Machine Translation via Structured Self-Reflection: both use a holistic,
  free-form LLM critique (error identification plus a 0-100 quality score in ReflectMT's case) followed by full-segment regeneration;
  neither defines a checkable set of content invariants, localizes failures to a span, nor stops on an explicit certificate
  rather than a fixed number of passes.
- >-
  Named Entity Correction in Neural Machine Translation Using the Attention Alignment Map: performs localized, targeted correction,
  but only for one category (named entities), via a static post-hoc lookup table rather than an iterative, multi-category,
  verify-then-repair loop covering numbers, negation, and quantifiers as well.
- >-
  LaSEr-Edit (Localized Span-level Error Editing with Energy-based Localization): a general controlled-text-generation framework
  that explicitly motivates localized editing over full regeneration ('regeneration may introduce new violations... especially
  pronounced when multiple constraints are involved'), but localizes and edits via a learned, soft energy-based model for
  arbitrary constraints (toxicity, contradiction, set-consistency) rather than a deterministic cross-lingual content-invariant
  checker, and is never applied to translation or benchmarked on the specific regression-rate question this hypothesis targets.
- >-
  Faithful Autoformalization via Roundtrip Verification and Repair: uses a closely analogous localized stage-diagnosis-and-scoped-repair
  loop, but for translating natural language into formal logic, verified by checking logical equivalence with a formal tool
  — a different domain (formalization, not cross-lingual NL-to-NL translation) and a different verifier (logical equivalence,
  not cross-lingual content-preservation).
inspiration: >-
  Cross-field transfer from formal methods and program synthesis, specifically Counterexample-Guided Inductive Synthesis (CEGIS):
  a synthesizer proposes a candidate, a verifier either certifies it or returns a concrete counterexample that scopes the
  next refinement, and the loop terminates on an explicit certificate rather than a fixed iteration budget. Mapped onto machine
  translation self-correction: extracted source-side content invariants (entities, numbers, negation, quantifiers) play the
  role of the specification, a deterministic cross-lingual checker plays the role of the verifier, and a localized target-span
  edit plays the role of the scoped refinement — replacing the field's current holistic, uncertified reflect-and-regenerate
  loops with a mechanism that has an explicit stopping condition and a bounded blast radius per repair.
terms:
- term: Content invariant
  definition: >-
    A piece of source-sentence meaning — a named entity, a number/unit/date, a negation polarity marker, or a quantifier —
    that must be preserved in any faithful translation and can be checked deterministically (via NER, regex, cue lists, or
    alignment) rather than judged holistically by another LLM.
- term: Localized span repair
  definition: >-
    Revising only the target-language region responsible for a failed invariant check, leaving the rest of the translation
    untouched, instead of regenerating the whole sentence from a holistic critique.
- term: Certificate (translation)
  definition: >-
    A translation for which every extracted content invariant has been checked and passes; an explicit, checkable stopping
    condition that current holistic self-refine loops (which stop after a fixed number of critique-and-rewrite passes) have
    no equivalent of.
- term: Regression rate
  definition: >-
    The fraction of content invariants that were correctly rendered in the draft translation but become violated as a side
    effect of a repair step — the specific collateral-damage risk that full-segment regeneration is prone to and localized
    repair is designed to avoid.
summary: >-
  Today's LLM translation self-refine loops critique and rewrite the whole sentence from a holistic, uncheckable judgment;
  borrowing counterexample-guided synthesis from formal methods, a deterministic checker for source-side content invariants
  (entities, numbers, negation, quantifiers) can instead localize exactly which target span is wrong and repair only that
  span until a certificate is reached, aiming to match today's error-fixing rate while cutting the rate at which the fix itself
  introduces new errors elsewhere.
</previous_hypothesis>

<previous_review>
Critiques from the previous review. Check which ones have been addressed
in the revised hypothesis. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (novelty) The related-work section omits the WMT QE-informed Automatic Post-Editing / Segment-level Error Correction lineage, which already implements the hypothesis's core mechanism for MT specifically: scope edits to a detected error span rather than regenerating the whole segment, explicitly to reduce 'over-correction' (the same phenomenon this hypothesis calls 'regression rate'). This includes Deoghare et al. 2023 (EMNLP Findings, 'Quality Estimation-Assisted Automatic Post-Editing'), Deoghare et al. 2025 ('Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE'), and the WMT25 shared task 'Task 3: QE-informed Segment-level Error Correction' with multiple 2025 competing systems (e.g. Padmanabhan 2025's 'Fill in the Blanks' approach explicitly instructs an LLM to replace only QE-flagged error substrings, using a 'Gain-to-Edit ratio' metric that is a close cousin of the proposed regression-rate metric). None of this is cited or discussed, so the hypothesis currently overstates its novelty by comparing only against holistic-regeneration baselines and a general (non-MT) controlled-text-generation paper (LaSEr-Edit), while the closest, most damaging comparison is MT-native localized correction work that already exists.
  Action: Add this lineage to related_works with an honest statement of what remains novel relative to it: (1) the localizer/verifier is a deterministic, checkable, interpretable content-invariant checker rather than a learned QE model or LLM judge, which changes what a 'certificate' means (reproducible and auditable rather than a confidence score); (2) the loop iterates to an explicit certificate (every invariant passes) rather than performing a single scoped edit. Then design the experiment (see the contribution-dimension suggestion) to actually isolate these two factors against the existing QE-guided single-shot baseline, not just against holistic regeneration.
- [MAJOR] (methodology) The baseline (condition A) is a holistic reflect-and-regenerate loop, which is a weak comparison point once the QE-guided localized-editing lineage above is acknowledged — the field has already partially moved past pure holistic regeneration toward scoped, error-guided editing. A result showing 'localized certified repair beats holistic regeneration' would therefore replicate an already-known finding (targeted edits regress less than full rewrites) rather than answering the more interesting question this hypothesis is actually positioned to answer: does a deterministic, certifiable checker do at least as well as a learned/LLM-based localizer at finding and scoping the repair, with the added benefit of an explicit stopping certificate?
  Action: Add a third condition: a single-shot, non-iterative localized edit guided by an LLM-based or word-level-QE-based error localizer (matching the design used in the WMT25 shared task systems), with no certificate and no re-checking loop. Compare all three conditions on fix rate, regression rate, and COMET. This turns the study from 'locality beats holism' (largely expected) into 'deterministic-and-certified beats learned-and-single-shot, or does not' (a real open question with two informative outcomes).
- [MAJOR] (methodology) The deterministic checker's own error rate is never measured or controlled for. If the checker has non-trivial false-positive rate (e.g., flagging a transliterated entity spelling, a spelled-out vs. digit number, or a legitimately reordered negation as a 'violation'), condition B will perform unnecessary repairs on already-correct spans, and any resulting 'new violation introduced' will be an artifact of checker noise rather than evidence about localization vs. holistic repair. This directly threatens the validity of the regression-rate metric, which is the hypothesis's central dependent variable.
  Action: Before running the two-condition comparison, validate the checker against a held-out, human-annotated sample of source-target pairs for each of the four categories and report precision/recall. Report the main regression-rate result both on all checker-flagged repairs and restricted to human-confirmed true violations, so a reviewer can see the result is not an artifact of checker imprecision.
- [MINOR] (methodology) The mechanism the hypothesis is built around — that a marked target span can be localized precisely enough to scope a repair — is asserted as an assumption but never measured as an outcome variable in its own right. Without reporting localization precision (e.g., span width relative to the actual erroneous region, or how often the flagged span fails to contain the true error), a null result on regression rate is ambiguous between 'localization doesn't help' and 'the localizer itself is imprecise.'
  Action: Report span-width statistics and localization accuracy (does the flagged span actually contain the invariant-relevant tokens, verified against human annotation on a sample) alongside the main fix-rate/regression-rate/COMET results, and check whether regression rate correlates with span width as the mechanistic story predicts.
- [MINOR] (methodology) Mixing natural MT errors with deliberately injected invariant-violating errors for statistical power risks inflating fix-rate results for the proposed method in a way that does not generalize: injected errors are, by construction, exactly the error type the deterministic checker was designed to catch, and may be easier to detect and repair than naturally occurring, more ambiguous instances of the same category (e.g., a naturally garbled date vs. a synthetically swapped one).
  Action: Report all three headline metrics separately for the natural-only subset and the injection-augmented subset, and briefly justify the injection procedure's realism (e.g., adversarial substitution informed by observed natural error patterns rather than random corruption) so a reviewer can judge whether the injected cases are representative rather than trivially detectable.
- [MINOR] (scope) The study as described uses a single LLM as both translator/critic/repairer across both conditions with no stated plan to test more than one model family. Since the mechanism the hypothesis relies on (an LLM reliably obeying a 'revise only this span' instruction) is itself an empirical claim (assumption 3) known to vary substantially by model and prompting style, a single-model result would be a narrow existence proof rather than a claim about 'the field's current holistic reflect-and-regenerate baselines' in general, which the hypothesis's title and success criteria implicitly claim to address.
  Action: If compute allows, replicate the core comparison (A vs. B, and the added condition C) on at least one additional model family, and report whether the direction and rough magnitude of the fix-rate/regression-rate gap holds; if only one model is feasible, soften the framing to name the specific model rather than 'the field's current baselines.'
</previous_review>

<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE (only if a <previous_hypothesis> block is present):
Classify how the current hypothesis relates to the previous iteration's hypothesis
using Moulines's structuralist typology. Set ``relation_type`` to one of:
    - "evolution": refining specialised claims while keeping the same conceptual frame
    - "embedding": the previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian, incommensurable shift)
Set ``relation_rationale`` to a brief justification (≤120 chars).

If no <previous_hypothesis> is present (this is iteration 1), leave both fields
null/empty.

Provide your review via structured output.
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
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
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
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-01 04:47:53 UTC

```
AI in translation emwrging opportunities
```

### [3] SYSTEM-USER prompt · 2026-09-01 04:50:29 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same CEGIS/certified-loop-for-span-editing frame, now retargeted at a real documented WMT25 baseline instead of a strawman holistic-regen one.' is too long (at most 120 characters, got 142)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
