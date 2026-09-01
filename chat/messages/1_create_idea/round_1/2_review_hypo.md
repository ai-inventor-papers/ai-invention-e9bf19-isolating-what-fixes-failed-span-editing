# review_hypo — create_idea

> Phase: `hypo_loop` · round 1 · `review_hypo`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 04:40:19 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/iter_1/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-09-01 04:40:25 UTC

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

STEP 3 — H↔H EDGE:
This is the first iteration — there is no previous hypothesis. Leave
``relation_type`` null and ``relation_rationale`` empty.

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

### [3] HUMAN-USER prompt · 2026-09-01 04:40:25 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Skill · 2026-09-01 04:40:31 UTC

```
aii-web-tools
```

### [5] TOOL RESULT — Skill · 2026-09-01 04:40:31 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [6] TOOL CALL — Bash · 2026-09-01 04:40:37 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"; export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "localized span repair machine translation self-correction content invariants" --max-results 10
echo "---"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "CEGIS counterexample guided inductive synthesis LLM translation verification repair" --max-results 10
echo "---"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "ReflectMT reflective translation self-refine machine translation" --max-results 10
```

### [7] TOOL RESULT — Bash · 2026-09-01 04:40:39 UTC

```
{"stdout": "Search: localized span repair machine translation self-correction content invariants  [general via ddgs]\nFound: 10 results\n\n1. LaSEr-Edit: Localized Span-level Error Editing with Energy-based Localization\n   https://arxiv.org/html/2407.00740v2\n   July 22, 2026 - By contrast, restricting edits to the spans responsible for constraint violations would enable targeted corrections and make iterative efforts toward constraint satisfaction more manag...\n\n2. Improving LLM-based Machine Translation with Systematic Self-Correction\n   https://arxiv.org/html/2402.16379v2\n   February 28, 2024 - Our findings demonstrate that 1) our self-correction framework successfully assists LLMs in improving their translation quality across a wide range of languages, whether it’s from ...\n\n3. Explorations of Self-Repair in Language Models\n   https://arxiv.org/html/2402.15390v2\n   May 26, 2024 - As adding a constant to the logits ... is translation invariant), centered logits are more amenable to analysis. As such, we cannot measure parts of self-repair coming from adding a con...\n\n4. Processing self corrections in a speech to speech system | Proceedings of the 18th conference on Computational linguistics - Volume 2\n   https://dl.acm.org/doi/10.3115/992730.992816\n   The basic idea is to reduce the search space for repairs as soon as possible by cascading filters that involve more and more features. At first an acoustic module generates hypotheses about the existe...\n\n5. Improving LLM-based Machine Translation with Systematic Self-Correction\n   https://openreview.net/pdf/e42e378b6ea082e2d1faa950d2a84ebb15616c3f.pdf\n   Improving LLM-based Machine Translation with Systematic · Anonymous ACL submission...\n\n6. (PDF) Processing Self Corrections in a speech to speech system\n   https://www.researchgate.net/publication/1955066_Processing_Self_Corrections_in_a_speech_to_speech_system\n   December 5, 2024 - We present here criteria and techniques for automatically detecting the presence of a repair, its location, and making the appropriate correction. The criteria involve integration o...\n\n7. Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang\n   https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf\n   Here, we present a set of programs that require NLA invariants to prove their functional correctness...\n\n8. GitHub - fzp0424/self_correct_mt: [NAACL'25] TEaR framework for paper \"TEaR: Improving LLM-based Machine Translation with Systematic Self-Refinement\" · GitHub\n   https://github.com/fzp0424/self_correct_mt\n   The TEaR (Translate, Estimate, and Refine) framework is designed as a self-correcting translation agent that leverages Large Language Models (LLMs) to refine its original translation....\n\n9. Span Corruption Pre-Training\n   https://www.emergentmind.com/topics/span-corruption-pre-training\n   February 9, 2026 - DeltaLM: In monolingual objectives, masks 15% of tokens in spans (average length 3), whereas in translation, 50% of tokens are masked in short spans (length=3), reflecting increased...\n\n10. Assessing the Latent Automated Program Repair Capabilities of Large Language Models using Round-Trip Translation\n   https://arxiv.org/html/2401.07994v2\n   October 15, 2025 - Research shows that errors in natural language can be corrected by translating texts to another language and back using language models. We explore to what extent this latent correc...\n\n---\nSearch: CEGIS counterexample guided inductive synthesis LLM translation verification repair  [general via ddgs]\nFound: 10 results\n\n1. GitHub - pmorvalho/LLM-CEGIS-Repair: AAAI 2025: Counterexample Guided Program Repair Using Zero-Shot Learning and MaxSAT-based Fault Localization · GitHub\n   https://github.com/pmorvalho/LLM-CEGIS-Repair\n   Our method uses MaxSAT-based fault localization to identify buggy parts of a program, then presents the LLM with a program sketch devoid of these buggy statements. This hybrid approach follows a Count...\n\n2. Counterexample Guided Program Repair Using Zero-Shot Learning and\n   https://pmorvalho.github.io/uploads/papers/aaai25-LLM-CEGIS-Repair.pdf\n   the-self LLM with a program sketch devoid of these buggy · statements. This hybrid approach follows a Counterexample · Guided Inductive Synthesis (CEGIS) loop (Solar-Lezama...\n\n3. Counterexample Guided Inductive Synthesis Modulo Theories⋆\n   https://www.kroening.com/papers/cav2018-synthesis.pdf\n   we must synthesize. A plausible scenario for a run of CEGIS is presented next: the synthesis phase guesses f(x) = ite (x < 0) −1 0, for which the veriﬁcation · phase returns x = 0 as a counterexample....\n\n4. Counterexample-Guided Inductive Synthesis (CEGIS)\n   https://www.emergentmind.com/topics/counterexample-guided-inductive-synthesis-cegis-loop\n   September 29, 2025 - The CEGIS loop comprises two core agents: (i) a synthesizer or learner that proposes a candidate solution from a hypothesis space, and (ii) a verifier (or teacher) that formally c...\n\n5. Assignment: Counterexample-Guided Inductive Synthesis\n   https://pages.cs.wisc.edu/~qhu28/homework/assignment_cegis.html\n   CEGIS is a form of generating and check, where a synthesizer generates candidate programs that are checked by an off-the-shelf checking procedure. The key idea in CEGIS, however, is to use a checker c...\n\n6. CEGIS(T) CounterExample Guided Inductive Synthesis modulo Theories\n   https://polgreen.github.io/pdfs/cegist.pdf\n   CounterExample Guided Inductive Synthesis · Alessandro Abate1, Cristina David2, Pascal Kesseli3, Daniel Kroening13,...\n\n7. Are There Good Mistakes? A Theoretical Analysis of CEGIS\n   https://susmitjha.github.io/papers/synt14.pdf\n   Guided Inductive Synthesis MinCEGIS where the validation engine returns minimal counterexam- ... This choice of counterexamples is motivated by literature on debugging1. Signiﬁcant effort has · been m...\n\n8. Counterexample-Guided Inductive Synthesis\n   https://www.emergentmind.com/topics/counterexample-guided-inductive-synthesis-cegis\n   CEGIS alternates between synthesizing a candidate solution valid on a (typically finite) set of examples and employing a verifier to either certify the candidate or produce a new counterexample that e...\n\n9. GitHub - marcelwa/CEGIS: Counter-example guided inductive synthesis (CEGIS) implementation for the SMT solver Z3 by Microsoft Research · GitHub\n   https://github.com/marcelwa/CEGIS\n   Therefore CEGIS uses one satisfiability solver to generate new implementations based on all the inputs considered so far (starting with zero); and another one to generate counter examples that uncover...\n\n10. Counterexample-guided inductive synthesis for ...\n   https://dl.acm.org/doi/pdf/10.1007/s00165-021-00547-2\n   Abstract. This paper presents counterexample-guided inductive synthesis (CEGIS) to automatically synthesise...\n\n---\nSearch: ReflectMT reflective translation self-refine machine translation  [general via ddgs]\nFound: 10 results\n\n1. [2601.19871] Reflective Translation: Improving Low-Resource Machine Translation via Structured Self-Reflection\n   https://arxiv.org/abs/2601.19871\n   January 27, 2026 - Building on this idea, this paper introduces Reflective Translation, a prompt-based framework in which a model generates an initial translation, produces a structured self-critique,...\n\n2. ReflectMT: Internalizing Reflection for Efficient and High-Quality Machine Translation\n   https://arxiv.org/html/2604.19144\n   April 21, 2026 - Unlike the “think-first-then... during the training stage: the model first generates an initial translation, then initiates a structured reflection process to critically evaluate it, ...\n\n3. Reflective Translation: Enhancing Low-Resource Machine Translation through Self-Reflection | OpenReview\n   https://openreview.net/forum?id=T7By0t6yaf\n   December 14, 2025 - TL;DR: Reflective Translation uses LLMs to self-review and correct translations, improving BLEU and COMET scores for low-resource languages like isiZulu and isiXhosa. Corresponding...\n\n4. Reflective Translation for Low-Resource Machine Translation via Structured Self-Reflection\n   https://arxiv.org/html/2601.19871\n   January 27, 2026 - Low-resource languages such as ... resources. Recent work on large language models (LLMs) suggests that self-reflection—the ability of a model to critique and revise its own outputs...\n\n5. (PDF) Reflective Translation: Improving Low-Resource Machine Translation via Structured Self-Reflection\n   https://www.researchgate.net/publication/400119314_Reflective_Translation_Improving_Low-Resource_Machine_Translation_via_Structured_Self-Reflection\n   January 28, 2026 - Building on this idea, this paper introduces Reflective Translation, a prompt-based framework in which a model generates an initial translation, produces a structured self-critique,...\n\n6. GitHub - Nickcheng123/reflective-translation-mt: Code and data for “Reflective Translation: Enhancing Low-Resource Machine Translation through Self-Reflection” (English→isiZulu/isiXhosa, BLEU/COMET, reflection + Self-Refine baselines).\n   https://github.com/Nickcheng123/reflective-translation-mt\n   January 28, 2026 - Code and data for “Reflective Translation: Enhancing Low-Resource Machine Translation through Self-Reflection” (English→isiZulu/isiXhosa, BLEU/COMET, reflection + Self-Refine baseli...\n\n7. [2604.19144] ReflectMT: Internalizing Reflection for Efficient and High-Quality Machine Translation\n   https://arxiv.org/abs/2604.19144\n   April 21, 2026 - To address these limitations, we propose ReflectMT, a two-stage reflection internalization algorithm for machine translation that employs a \"translate-first-think-later\" paradigm....\n\n8. [2411.02791] Language Models and Cycle Consistency for Self-Reflective Machine Translation\n   https://arxiv.org/abs/2411.02791\n   November 5, 2024 - This work provide methods for, 1) to implicitly evaluate translation quality of a sentence in the target language, 2), to evaluate capability of LLM for any-to-any-language translat...\n\n9. [2406.08434] TasTe: Teaching Large Language Models to Translate through Self-Reflection\n   https://arxiv.org/abs/2406.08434\n   June 12, 2024 - The self-reflection process includes two stages of inference. In the first stage, LLMs are instructed to generate preliminary translations and conduct self-assessments on these transla...\n\n10. TasTe: Teaching Large Language Models to Translate through Self-Reflection - ACL Anthology\n   https://aclanthology.org/2024.acl-long.333/\n   The self-reflection process includes two stages of inference. In the first stage, LLMs are instructed to generate preliminary translations and conduct self-assessments on these translations simultaneo...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [8] TOOL CALL — Bash · 2026-09-01 04:40:49 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"; export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "word-level quality estimation guided localized correction LLM machine translation critical errors" --max-results 10
echo "---"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "critical error detection machine translation numbers named entities negation quantifiers checklist" --max-results 10
```

### [9] TOOL RESULT — Bash · 2026-09-01 04:40:49 UTC

```
{"stdout": "Search: word-level quality estimation guided localized correction LLM machine translation critical errors  [general via ddgs]\nFound: 10 results\n\n1. Can QE-informed (Re)Translation lead to Error Correction?\n   https://arxiv.org/html/2511.13884v1\n   July 27, 2026 - As such, Automatic Post-Editing (APE) is vital to fixing MT errors. However, they are prone to overcorrecting. One such example of mitigating over-correcting, proposed by Deoghare et a...\n\n2. Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement\n   https://arxiv.org/html/2505.23183\n   May 29, 2025 - Word-level quality estimation (WQE) aims to automatically identify fine-grained error spans in machine-translated outputs and has found many uses, including assisting translators during...\n\n3. Enhancing Machine Translation Quality Estimation via Fine-Grained Error Analysis and Large Language Model\n   https://www.mdpi.com/2227-7390/11/19/4169\n   October 5, 2023 - Prompt-based learning effectively leverages pre-trained knowledge by reformulating the task at hand [3,4,5,6]. This approach validates QE tasks that determine the presence or absence...\n\n4. From Handcrafted Features to LLMs: A Brief Survey for Machine Translation Quality Estimation\n   https://arxiv.org/html/2403.14118v1\n   It divides MT errors into 7 dimensions: Terminology, Accuracy, Linguistic conventions, Style, Locale conventions, Audience appropriateness, and Design and markup. Each dimension is subdivided into dif...\n\n5. [Literature Review] Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement\n   https://www.themoonlight.io/en/review/unsupervised-word-level-quality-estimation-for-machine-translation-through-the-lens-of-annotators-disagreement\n   A continuous variant, XCOMETCONF, is introduced by summing the probabilities of all error types for a token $s(t^*) = p(\\text{MINOR}) + p(\\text{MAJOR}) + p(\\text{CRITICAL})$, allowing for calibrated p...\n\n6. Can QE-informed (Re)Translation lead to Error Correction?\n   https://aclanthology.org/2025.wmt-1.73.pdf\n   François Yvon. 2019. Quality estimation for machine...\n\n7. [2505.23183] Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement\n   https://arxiv.org/abs/2505.23183\n   May 29, 2025 - In this work, we investigate efficient alternatives exploiting recent advances in language model interpretability and uncertainty quantification to identify translation errors from the ...\n\n8. Towards Reliable Machine Translation: Scaling LLMs for Critical Error Detection and Safety\n   https://arxiv.org/html/2602.11444\n   February 11, 2026 - T introduces a meaning-critical error (ERR/BAD) or preserves the intended meaning (NOT/OK). Unlike traditional Quality Estimation frameworks [36, 9], which assign continuous adequa...\n\n9. Paper page - Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement\n   https://huggingface.co/papers/2505.23183\n   Evaluation of word-level quality estimation techniques leverages model interpretability and uncertainty quantification to identify translation errors with a focus on the impact of label variation and ...\n\n10. Machine Translation Quality Estimation\n   https://www.emergentmind.com/topics/machine-translation-quality-estimation-mtqe\n   February 4, 2026 - Reward Modeling for Policy Optimization: QE models (COMET-DA, COMETKiwi) serve as reference-based or reference-free reward functions for GRPO/REINFORCE fine-tuning of LLM translatio...\n\n---\nSearch: critical error detection machine translation numbers named entities negation quantifiers checklist  [general via ddgs]\nFound: 10 results\n\n1. SynCED-EnDe 2025: A Synthetic and Curated English - German Dataset for Critical Error Detection in Machine Translation\n   https://arxiv.org/html/2510.05144\n   October 1, 2025 - Preprocessing consisted of sentence cleaning, splitting, and de-duplication, with a maximum length of 30 tokens. During harvesting, four trigger flags were automatically tagged for l...\n\n2. Critical error categories and examples\n   https://statmt.org/wmt21/quality-estimation-task_critical-error-examples.html\n   Reason: there are no critical issues; while the MT got some of the content incorrectly, the named entity was preserved. (d) (SEN) Deviation in sentiment polarity or negation. The MT either introduces ...\n\n3. Critical Errors in Machine Translation: A 2026 Guide\n   https://www.adverbum.com/post/critical-errors-in-machine-translation-a-2026-guide\n   July 13, 2026 - Critical errors in machine translation are output deviations that cause serious meaning loss, legal exposure, or compliance failure. They include semantic hallucinations, omissions, ne...\n\n4. A Taxonomy and Study of Critical Errors in Machine Translation\n   https://aclanthology.org/2022.eamt-1.20.pdf\n   A Taxonomy and Study of Critical Errors in Machine Translation · Khetam Al Sharou1 and Lucia Specia1, 2...\n\n5. GitHub - haeggee/error-detection-mt: Critical Error Detection in Machine Translation - Project for Computational Semantics for NLP, ETH Zurich, 2021.\n   https://github.com/haeggee/error-detection-mt\n   The goal of this task is to predict sentence-level binary scores indicating whether or not a translation contains (at least one) critical error....\n\n6. GitHub - alan-turing-institute/ARC-MTQE: Critical Error Detection for Machine Translation · GitHub\n   https://github.com/alan-turing-institute/ARC-MTQE\n   Code to train and evaluate models for detecting critical errors in machine translations using only the original source text and the machine translated text as described in Knight et al....\n\n7. How Small Can You Go? Compact Language Models for On-Device Critical Error Detection in Machine Translation This research has been funded by the Federal Ministry of Education and Research of Germany and the state of North-Rhine Westphalia as part of the Lamarr Institute for Machine Learning and Artificial Intelligence.\n   https://arxiv.org/html/2511.09748v1\n   July 27, 2026 - \\rightarrowERR. Text is normalised with Unicode NFC, numbers/dates are preserved verbatim, and we keep case and punctuation (critical for entity/negation cues)....\n\n8. A negation detection assessment of GPTs: analysis with the xNot360 dataset\n   https://arxiv.org/pdf/2306.16638\n   quantifiers, such as “Few judges ruled in favor of the defendant,”...\n\n9. Automatic Reference-Free Fine-Grained Machine Translation Error Detection via Named Entity Recognition and Back-Translation | Springer Nature Link\n   https://link.springer.com/chapter/10.1007/978-981-97-5672-8_26\n   To address this limitation, we propose an Automatic Reference-Free Fine-Grained Neural Machine Translation Error Detection method (ARFGED) that leverages Named Entity Recognition and Back-Translation....\n\n10. Towards Reliable Machine Translation: Scaling LLMs for Critical Error Detection and Safety\n   https://arxiv.org/html/2602.11444\n   February 11, 2026 - However, critical meaning errors, such as factual distortions, intent reversals, or biased translations, can undermine the reliability, fairness, and safety of multilingual systems...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] TOOL CALL — Bash · 2026-09-01 04:40:57 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"; export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2511.13884v1" --max-chars 6000
```

### [11] TOOL RESULT — Bash · 2026-09-01 04:40:57 UTC

```
{"stdout": "URL: https://arxiv.org/html/2511.13884v1\nType: HTML\nLength: 36915 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n×\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2511.13884v1 \"Back to abstract page\") [ Download PDF](/pdf/2511.13884v1 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Related Work\n     1. Quality Estimation (QE)\n     2. Automatic Post-Editing (APE)\n     3. WMT24 QE-APE\n     4. ‣ 2 Related Work\n  4. 3 Methodology\n     1. 3.1 Dataset Analysis\n     2. 3.2 Approaches\n        1. 3.2.1 Primary Approach - “Best MT Wins”\n        2. 3.2.2  Secondary Approach - “Fill in the Blanks”\n  5. 4 Results and Discussion\n     1. 4.1 Primary Approach - “Best MT Wins”\n     2. 4.2 Secondary Approach - “Fill in the Blanks”\n  6. 5 Conclusion and Future Work\n  7. 6 Acknowledgements\n  8. References\n  9. A Example of Primary Approach\n  10. B Negative Example for Secondary Approach\n  11. C Positive Example for Secondary Approach\n\n\n\n[ License: CC BY-NC-SA 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2511.13884v1 [cs.CL] 17 Nov 2025\n\n# Can QE-informed (Re)Translation lead to Error Correction?\n\nGovardhan Padmanabhan Affiliation: Institute for People-Centred AI Affiliation: University of Surrey, United Kingdom Email: [gp00816@surrey.ac.uk](mailto:)\n\n###### Abstract\n\nThe paper presents two approaches submitted to the WMT 2025 Automated Translation Quality Evaluation Systems Task 3 - Quality Estimation (QE)-informed Segment-level Error Correction. While jointly training QE systems with Automatic Post-Editing (APE) has shown improved performance for both tasks, APE systems are still known to overcorrect the output of Machine Translation (MT), leading to a degradation in performance. We investigate a simple training-free approach - QE-informed Retranslation, and compare it with another within the same training-free paradigm. Our winning approach selects the highest-quality translation from multiple candidates generated by different LLMs. The second approach, more akin to APE, instructs an LLM to replace error substrings as specified in the provided QE explanation(s). A conditional heuristic was employed to minimise the number of edits, with the aim of maximising the Gain-to-Edit ratio. The two proposed approaches achieved a Δ\\DeltaCOMET score of 0.02010.0201 and −0.0108-0.0108, respectively, leading the first approach to achieve the winning position on the subtask leaderboard.\n\n## 1 Introduction\n\nLarge Language Models (LLMs) have advanced the field of Machine Translation (MT), given their support for longer input context length and ability to generate text in a natural tone. However, translation quality is still limited for languages other than English and for domain-specific translations Fernandes et al. (2025). Evaluating MT output for quality is critical to understand the reliability and suitability of translation systems, and more importantly, to be able to perform accurate corrections. The WMT24 Metrics Shared Task found that neural-based learned metrics like COMET or xCOMET were superior when evaluating LLM-generated translations, compared to the traditional statistical metrics like BLEU, or chrF Freitag et al. (2024).\n\nAs LLMs are typically trained on a large general dataset, performance in domain-specific MT can often fall short as they may not properly render key terminologies or stylistic conventions. As such, Automatic Post-Editing (APE) is vital to fixing MT errors. However, they are prone to overcorrecting. One such example of mitigating over-correcting, proposed by Deoghare et al. (2025), is to utilize word-level Quality Estimation (QE) to limit edits only on the specified error segments. Despite recent efforts to reduce overcorrection Deoghare et al. (2023); Deoghare et al. (2024), APE models still fall short of the required semantically coherent output. Therefore, we ask the titular question - “Can QE-informed re-translation help overcome MT errors?”, and discuss two approaches as a comparative evaluation.   \n\n\nThis paper describes two participation systems, both utilizing pre-trained and open-source LLMs, for the WMT 2025 Automated Translation Quality Evaluation Systems Task 3 - QE-informed Segment-level Error Correction. The primary approach leverages multiple LLMs for MT and selects the best output using QE. In the secondary approach, an LLM is prompted to replace error-segments in the provided MT. These error segments are identified by the explainable QE provided within the dataset.\n\n## 2 Related Work\n\nFigure 1: Domain distribution within each language\n\n##### Quality Estimation (QE)\n\nQE is an automated evaluation framework that predicts a score indicating whether the translation is good or not Yvon (2019). COMET (Cross-Lingual Optimized Metric for Evaluation of Translation) is an automatic metric to evaluate the quality of machine translation using deep learning models Rei et al. (2020). COMETKiwi is a hybrid machine translation quality estimation (MTQE) model that combines COMET and OpenKiwi Rei et al. (2022). It achieved top performance in the WMT 2022 shared task and has since been widely adopted as a state-of-the-art benchmark in MTQE.\n\n##### Automatic Post-Editing (APE)\n\nAPE is an automated system that corrects MT output, without human involvement do Carmo et al. (2021). Chatterjee et al. (2018) describe combining QE and APE in three ways: using QE as an APE activator when the MT output is poor, as guidance to help the APE decoder decide which tokens to change, and as a selector to choose between the raw MT and post-edited output.\n\n##### WMT24 QE-APE\n\nThe previous year’s WMT competition focused on sentence-level quali", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [12] TOOL CALL — Bash · 2026-09-01 04:41:11 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"; export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Deoghare word-level quality estimation guided automatic post-editing overcorrection" --max-results 10
echo "---"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "WMT 2025 QE-informed segment-level error correction shared task" --max-results 6
```

### [13] TOOL RESULT — Bash · 2026-09-01 04:41:11 UTC

```
{"stdout": "Search: Deoghare word-level quality estimation guided automatic post-editing overcorrection  [general via ddgs]\nFound: 10 results\n\n1. Quality Estimation-Assisted Automatic Post-Editing - ACL Anthology\n   https://aclanthology.org/2023.findings-emnlp.115/\n   @inproceedings{deoghare-etal-2... pages = \"1686--1698\", abstract = \"Automatic Post-Editing (APE) systems are prone to over-correction of the Machine Translation (MT) outputs.......\n\n2. Giving the Old a Fresh Spin: Quality Estimation-Assisted Constrained Decoding for Automatic Post-Editing\n   https://arxiv.org/html/2501.17265v1\n   January 28, 2025 - Lee (2020a); Deoghare and Bhattacharyya (2022); Yu et al. (2023) mitigate over-correction by reverting to the original translation based on QE speculation. Chatterjee et al. (2018b)...\n\n3. Together We Can: Multilingual Automatic Post-Editing for Low-Resource Languages | Request PDF\n   https://www.researchgate.net/publication/386196899_Together_We_Can_Multilingual_Automatic_Post-Editing_for_Low-Resource_Languages\n   January 1, 2024 - (2025), is to utilize word-level Quality Estimation (QE) to limit edits only on the specified error segments. Despite recent efforts to reduce overcorrection (Deoghare et al., 2023...\n\n4. Smarter edits? Post-editing with error highlights and translation suggestions\n   https://arxiv.org/html/2605.21135\n   May 20, 2026 - [Deoghare et al., 2025] Deoghare, Sourabh, Diptesh Kanojia, and Pushpak Bhattacharyya. 2025. Giving the old a fresh spin: Quality estimation-assisted constrained decoding for automatic ...\n\n5. QE4PE: Word-level Quality Estimation for Human Post-Editing\n   https://arxiv.org/html/2503.03044v1\n   March 4, 2025 - Word-level quality estimation (QE) detects erroneous spans in machine translations, which can direct and facilitate human post-editing. While the accuracy of word-level QE systems has ...\n\n6. (PDF) Combining Quality Estimation and Automatic Post-editing to Enhance Machine Translation Output\n   https://www.researchgate.net/publication/333014997_Combining_Quality_Estimation_and_Automatic_Post-editing_to_Enhance_Machine_Translation_Output\n   May 11, 2019 - (2018) describe combining QE and APE in three ways: using QE as an APE activator when the MT output is poor, as guidance to help the APE decoder decide which tokens to change, and as a ...\n\n7. Quality Estimation-Assisted Automatic Post-Editing | OpenReview\n   https://openreview.net/forum?id=v2wbkddf52\n   December 1, 2023 - Automatic Post-Editing (APE) systems are prone to over-correction of the Machine Translation (MT) outputs. While Word-level Quality Estimation (QE) system can provide a way to curta...\n\n8. Quality Estimation-Assisted Automatic Post-Editing - Tilburg University Research Portal\n   https://research.tilburguniversity.edu/en/publications/quality-estimation-assisted-automatic-post-editing\n   February 6, 2024 - Deoghare, S., Kanojia, D., Ranasinghe, T., Blain, F., & Bhattacharyya, P. (2023). Quality Estimation-Assisted Automatic Post-Editing. In Findings of the Association for Computationa...\n\n9. Introducing Quality Estimation to Machine Translation Post- ...\n   https://aclanthology.org/2025.mtsummit-1.38.pdf\n   Diptesh Kanojia, Sourabh Deoghare, Nuno M....\n\n10. Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement\n   https://arxiv.org/html/2505.23183\n   May 29, 2025 - Word-level quality estimation (WQE) aims to automatically identify fine-grained error spans in machine-translated outputs and has found many uses, including assisting translators during...\n\n---\nSearch: WMT 2025 QE-informed segment-level error correction shared task  [general via ddgs]\nFound: 6 results\n\n1. Shared task: Automated Translation Quality Evaluation Systems\n   https://www2.statmt.org/wmt25/mteval-subtask.html\n   The shared task this year consists of three primary subtasks that address translation quality assessment from three perspectives: (1) segment-level quality score prediction, (2) span-level translation...\n\n2. WMT 2025 Shared Task on Automated Translation Quality Evaluation: Now Open for Participation!\n   https://groups.google.com/g/wmt-tasks/c/rhTEupvaksQ\n   Full description: https://www2... · Task 3: Quality-informed segment-level error correction Automatically post-edit machine-translated text using quality annotations to generate minimal and accurate c...\n\n3. WMT25 Automated Translation Quality Evaluation Systems Task 3 - QE-informed Segment-level Error Correction – Codabench\n   https://www.codabench.org/competitions/8371/\n   The objective is to explore how quality information (both error annotations and scores) can inform automated error correction. For instance, sentence-level quality scores may help identify which segme...\n\n4. QE-informed Segment-level Error Correction\n   https://www2.statmt.org/wmt25/mteval-subtask3.html\n   Following last year’s QE-informed APE subtask, we invite participants to submit systems capable of automatically generating corrections to machine-translated text, given the source, the MT-generated t...\n\n5. Can QE-informed (Re)Translation lead to Error Correction?\n   https://arxiv.org/html/2511.13884\n   November 17, 2025 - This paper describes two participation ... Evaluation Systems Task 3 - QE-informed Segment-level Error Correction. The primary approach leverages multiple LLMs for MT and selects t...\n\n6. Quality-Informed Segment-Level Error Correction Using Natural Language Explanations from xTower and Large Language Models - ACL Anthology\n   https://aclanthology.org/2025.wmt-1.75/\n   %0 Conference Proceedings %T Quality-Informed Segment-Level Error Correction Using Natural Language Explanations from xTower and Large Language Models %A Sharma, Prashant %Y Haddow, Barry %Y Kocmi, To...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] TOOL CALL — Bash · 2026-09-01 04:41:53 UTC

```
pwd
```

### [15] TOOL RESULT — Bash · 2026-09-01 04:41:53 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/iter_1/review_hypo", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] TOOL CALL — Write · 2026-09-01 04:42:55 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/iter_1/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is a clearly written, well-scoped hypothesis with a genuinely nice cross-field mapping (CEGIS -> content-invariant checker as verifier -> localized span repair as scoped refinement) and unusually honest, falsifiable success/disconfirmation criteria. However, a targeted prior-art search surfaces a substantial, directly on-topic line of MT research that the hypothesis's related-work section misses entirely: the WMT QE-informed Automatic Post-Editing / Segment-level Error Correction lineage (Deoghare et al. 2023 EMNLP-Findings 'Quality Estimation-Assisted Automatic Post-Editing', explicitly motivated by APE 'over-correction'; Deoghare et al. 2025 'Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE'; and the WMT25 shared task 'Task 3: QE-informed Segment-level Error Correction', which multiple 2025 systems (e.g. Padmanabhan 2025, Sharma 2025) competed on with the explicit goal of producing 'minimal and accurate corrections' scoped to QE-flagged error spans to avoid overcorrection). That is precisely the mechanism this hypothesis frames as a novel transplant from general controlled-text-generation (LaSEr-Edit) into MT: detect an error span, edit only that span, don't touch the rest, and measure whether localization reduces collateral damage relative to full regeneration/re-decoding. The cited related work (ReflectMT, Reflective Translation, one NER-correction paper, LaSEr-Edit, an autoformalization paper) is accurately characterized but is the wrong comparison set — it omits the MT-specific localized-correction lineage that already exists and already measures something very close to 'regression rate' under names like overcorrection and gain-to-edit ratio. The hypothesis's real, defensible differentiators — (1) a deterministic/interpretable checker in place of a learned QE model as both localizer and stopping criterion, and (2) an explicit iterate-until-certificate CEGIS loop rather than a single-shot edit — survive this prior art, but they need to be stated and tested AGAINST it, not framed as if no MT work had tried scoped, non-regenerative repair before. The methodology itself is reasonable and mostly sound, but has a few real confounds (checker precision/recall is never measured, span-width/localization-precision is asserted rather than measured as an outcome, and compute/call-budget parity between the iterative certified loop and the single-pass baseline is not addressed) that should be fixed before running, since each could produce a result that looks like a locality effect but is actually an artifact.",
  "strengths": [
    "The CEGIS transplant is genuinely apt and precisely specified: source-side content invariants as the specification, a deterministic cross-lingual checker as the verifier, a localized span edit as the scoped refinement, and an explicit certificate as the stopping condition — this is a real structural analogy, not just a rebranded pipeline, and it correctly identifies what current holistic reflect-and-regenerate loops lack (an explicit, checkable termination condition).",
    "The three-way outcome design (fix rate, regression rate, COMET) with a pre-specified, symmetric disconfirmation condition ('regression rates statistically indistinguishable' OR 'fix rate substantially lower') is unusually honest scientific hygiene for a hypothesis at this stage — both possible negative outcomes are informative rather than the study only being able to fail silently.",
    "Grounding the four invariant categories (entities, numbers/units/dates, negation polarity, quantifier scope) in the field's own established critical-error taxonomy (WMT critical-error categories, SynCED-EnDe, the 2022 EAMT critical-errors taxonomy) rather than inventing an ad hoc list is a credible methodological choice that should transfer to real error distributions reasonably well.",
    "The assumptions section is unusually explicit and independently falsifiable (extractability, localizability, instruction-following locality, baseline fidelity, category coverage), which makes it easy to see exactly which premise a negative result would implicate."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 3,
      "justification": "The core comparison (localized-certified loop vs. holistic reflect-regenerate) is well-posed and the metrics are appropriate, but several confounds are left unaddressed: checker false positives are never separated from true violations before computing fix/regression rates, span-localization precision (the actual mechanism claimed to bound blast radius) is never measured as its own outcome, and the iterative certified loop is not obviously compute/call-matched against the single-pass baseline.",
      "improvements": [
        "Report the deterministic checker's own precision/recall against a human-annotated sample of invariant violations before using it to score either condition, and report regression-rate results both on all checker-flagged violations and on the human-confirmed subset, since a noisy checker can manufacture spurious 'repairs' that inflate the regression-rate metric independent of the localization-vs-holistic manipulation. Expected impact: closes the most likely reviewer objection to the entire result and would likely raise soundness by 1 point.",
        "Add a directly-measured localization-precision outcome (span width relative to the ground-truth error region) and show it predicts regression rate, so the paper demonstrates the mechanism rather than only reporting its downstream effect. Expected impact: turns an assumption into evidence, meaningful soundness gain.",
        "Match or report call/token budget between condition A (1 critique + 1 regeneration) and condition B (up to the iteration bound), and include a compute-matched ablation (e.g., cap A at the same number of passes, or aggregate A's per-pass edits into a fair single comparison), so a positive result for B cannot be attributed to B simply doing more LLM work. Expected impact: removes an obvious confound, moderate soundness gain."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The writing is clear, terms are defined precisely in a glossary, and the CEGIS mapping is explained at the right level of abstraction for a reader unfamiliar with program synthesis, but the related-work section is materially incomplete for an MT-specific reader (see novelty critique), which will read as a positioning gap to any MT-fluent reviewer.",
      "improvements": [
        "Add the WMT QE-informed APE / segment-level error correction lineage (Deoghare et al. 2023, 2025; WMT25 Task 3 and its 2025 system papers) to related work, and explicitly state what changes relative to it (deterministic vs. learned localization; iterate-to-certificate vs. single-shot edit). Expected impact: this is the single highest-value fix in the whole hypothesis — without it, an MT-track reviewer will likely flag the core mechanism as already explored and score the paper down on originality regardless of how the experiment turns out."
      ]
    },
    {
      "dimension": "contribution",
      "score": 2,
      "justification": "As framed, the hypothesis claims a novel transplant of localized, certified repair into MT self-correction, but a directly on-topic MT literature (QE-guided, span-scoped post-editing explicitly designed to curb 'over-correction') already exists and already tests almost the same locality-vs-full-rewrite trade-off, just with a learned localizer instead of a deterministic checker and without an explicit iterate-to-certificate loop. That leaves a real but narrower contribution than currently advertised.",
      "improvements": [
        "Reframe the contribution explicitly as a comparison between three conditions, not two: (A) holistic reflect-regenerate, (B) the proposed deterministic-checker CEGIS loop, and (C) a single-shot QE/LLM-critique-guided localized edit matching the WMT25 winning approach's design (detect error span via a learned/LLM judge, edit only that span, no iteration, no certificate). This isolates which of the two claimed novelties — deterministic vs. learned localization, and iterate-to-certificate vs. single-shot — actually drives any locality benefit, which is now the genuinely open and citable question. Expected impact: this is the change most likely to move the paper from 'the localized-editing effect is already known' to 'here is what specifically survives once you control for that,' which is the paper's real shot at a top-tier-worthy contribution."
      ]
    }
  ],
  "critiques": [
    {
      "category": "novelty",
      "severity": "major",
      "description": "The related-work section omits the WMT QE-informed Automatic Post-Editing / Segment-level Error Correction lineage, which already implements the hypothesis's core mechanism for MT specifically: scope edits to a detected error span rather than regenerating the whole segment, explicitly to reduce 'over-correction' (the same phenomenon this hypothesis calls 'regression rate'). This includes Deoghare et al. 2023 (EMNLP Findings, 'Quality Estimation-Assisted Automatic Post-Editing'), Deoghare et al. 2025 ('Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE'), and the WMT25 shared task 'Task 3: QE-informed Segment-level Error Correction' with multiple 2025 competing systems (e.g. Padmanabhan 2025's 'Fill in the Blanks' approach explicitly instructs an LLM to replace only QE-flagged error substrings, using a 'Gain-to-Edit ratio' metric that is a close cousin of the proposed regression-rate metric). None of this is cited or discussed, so the hypothesis currently overstates its novelty by comparing only against holistic-regeneration baselines and a general (non-MT) controlled-text-generation paper (LaSEr-Edit), while the closest, most damaging comparison is MT-native localized correction work that already exists.",
      "suggested_action": "Add this lineage to related_works with an honest statement of what remains novel relative to it: (1) the localizer/verifier is a deterministic, checkable, interpretable content-invariant checker rather than a learned QE model or LLM judge, which changes what a 'certificate' means (reproducible and auditable rather than a confidence score); (2) the loop iterates to an explicit certificate (every invariant passes) rather than performing a single scoped edit. Then design the experiment (see the contribution-dimension suggestion) to actually isolate these two factors against the existing QE-guided single-shot baseline, not just against holistic regeneration."
      },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The baseline (condition A) is a holistic reflect-and-regenerate loop, which is a weak comparison point once the QE-guided localized-editing lineage above is acknowledged — the field has already partially moved past pure holistic regeneration toward scoped, error-guided editing. A result showing 'localized certified repair beats holistic regeneration' would therefore replicate an already-known finding (targeted edits regress less than full rewrites) rather than answering the more interesting question this hypothesis is actually positioned to answer: does a deterministic, certifiable checker do at least as well as a learned/LLM-based localizer at finding and scoping the repair, with the added benefit of an explicit stopping certificate?",
      "suggested_action": "Add a third condition: a single-shot, non-iterative localized edit guided by an LLM-based or word-level-QE-based error localizer (matching the design used in the WMT25 shared task systems), with no certificate and no re-checking loop. Compare all three conditions on fix rate, regression rate, and COMET. This turns the study from 'locality beats holism' (largely expected) into 'deterministic-and-certified beats learned-and-single-shot, or does not' (a real open question with two informative outcomes)."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The deterministic checker's own error rate is never measured or controlled for. If the checker has non-trivial false-positive rate (e.g., flagging a transliterated entity spelling, a spelled-out vs. digit number, or a legitimately reordered negation as a 'violation'), condition B will perform unnecessary repairs on already-correct spans, and any resulting 'new violation introduced' will be an artifact of checker noise rather than evidence about localization vs. holistic repair. This directly threatens the validity of the regression-rate metric, which is the hypothesis's central dependent variable.",
      "suggested_action": "Before running the two-condition comparison, validate the checker against a held-out, human-annotated sample of source-target pairs for each of the four categories and report precision/recall. Report the main regression-rate result both on all checker-flagged repairs and restricted to human-confirmed true violations, so a reviewer can see the result is not an artifact of checker imprecision."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "The mechanism the hypothesis is built around — that a marked target span can be localized precisely enough to scope a repair — is asserted as an assumption but never measured as an outcome variable in its own right. Without reporting localization precision (e.g., span width relative to the actual erroneous region, or how often the flagged span fails to contain the true error), a null result on regression rate is ambiguous between 'localization doesn't help' and 'the localizer itself is imprecise.'",
      "suggested_action": "Report span-width statistics and localization accuracy (does the flagged span actually contain the invariant-relevant tokens, verified against human annotation on a sample) alongside the main fix-rate/regression-rate/COMET results, and check whether regression rate correlates with span width as the mechanistic story predicts."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "Mixing natural MT errors with deliberately injected invariant-violating errors for statistical power risks inflating fix-rate results for the proposed method in a way that does not generalize: injected errors are, by construction, exactly the error type the deterministic checker was designed to catch, and may be easier to detect and repair than naturally occurring, more ambiguous instances of the same category (e.g., a naturally garbled date vs. a synthetically swapped one).",
      "suggested_action": "Report all three headline metrics separately for the natural-only subset and the injection-augmented subset, and briefly justify the injection procedure's realism (e.g., adversarial substitution informed by observed natural error patterns rather than random corruption) so a reviewer can judge whether the injected cases are representative rather than trivially detectable."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "The study as described uses a single LLM as both translator/critic/repairer across both conditions with no stated plan to test more than one model family. Since the mechanism the hypothesis relies on (an LLM reliably obeying a 'revise only this span' instruction) is itself an empirical claim (assumption 3) known to vary substantially by model and prompting style, a single-model result would be a narrow existence proof rather than a claim about 'the field's current holistic reflect-and-regenerate baselines' in general, which the hypothesis's title and success criteria implicitly claim to address.",
      "suggested_action": "If compute allows, replicate the core comparison (A vs. B, and the added condition C) on at least one additional model family, and report whether the direction and rough magnitude of the fix-rate/regression-rate gap holds; if only one model is feasible, soften the framing to name the specific model rather than 'the field's current baselines.'"
    }
  ],
  "score": 4,
  "confidence": 4,
  "relation_type": null,
  "relation_rationale": ""
}
```

### [17] TOOL RESULT — Write · 2026-09-01 04:42:55 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/iter_1/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is a clearly written, well-scoped hypothesis with a genuinely nice cross-field mapping (CEGIS -> content-invariant checker as verifier -> localized span repair as scoped refinement) and unusually honest, falsifiable success/disconfirmation criteria. However, a targeted prior-art search surfaces a substantial, directly on-topic line of MT research that the hypothesis's related-work section misses entirely: the WMT QE-informed Automatic Post-Editing / Segment-level Error Correction lineage (Deoghare et al. 2023 EMNLP-Findings 'Quality Estimation-Assisted Automatic Post-Editing', explicitly motivated by APE 'over-correction'; Deoghare et al. 2025 'Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE'; and the WMT25 shared task 'Task 3: QE-informed Segment-level Error Correction', which multiple 2025 systems (e.g. Padmanabhan 2025, Sharma 2025) competed on with the explicit goal of producing 'minimal and accurate corrections' scoped to QE-flagged error spans to avoid overcorrection). That is precisely the mechanism this hypothesis frames as a novel transplant from general controlled-text-generation (LaSEr-Edit) into MT: detect an error span, edit only that span, don't touch the rest, and measure whether localization reduces collateral damage relative to full regeneration/re-decoding. The cited related work (ReflectMT, Reflective Translation, one NER-correction paper, LaSEr-Edit, an autoformalization paper) is accurately characterized but is the wrong comparison set — it omits the MT-specific localized-correction lineage that already exists and already measures something very close to 'regression rate' under names like overcorrection and gain-to-edit ratio. The hypothesis's real, defensible differentiators — (1) a deterministic/interpretable checker in place of a learned QE model as both localizer and stopping criterion, and (2) an explicit iterate-until-certificate CEGIS loop rather than a single-shot edit — survive this prior art, but they need to be stated and tested AGAINST it, not framed as if no MT work had tried scoped, non-regenerative repair before. The methodology itself is reasonable and mostly sound, but has a few real confounds (checker precision/recall is never measured, span-width/localization-precision is asserted rather than measured as an outcome, and compute/call-budget parity between the iterative certified loop and the single-pass baseline is not addressed) that should be fixed before running, since each could produce a result that looks like a locality effect but is actually an artifact.\",\n  \"strengths\": [\n    \"The CEGIS transplant is genuinely apt and precisely specified: source-side content invariants as the specification, a deterministic cross-lingual checker as the verifier, a localized span edit as the scoped refinement, and an explicit certificate as the stopping condition — this is a real structural analogy, not just a rebranded pipeline, and it correctly identifies what current holistic reflect-and-regenerate loops lack (an explicit, checkable termination condition).\",\n    \"The three-way outcome design (fix rate, regression rate, COMET) with a pre-specified, symmetric disconfirmation condition ('regression rates statistically indistinguishable' OR 'fix rate substantially lower') is unusually honest scientific hygiene for a hypothesis at this stage — both possible negative outcomes are informative rather than the study only being able to fail silently.\",\n    \"Grounding the four invariant categories (entities, numbers/units/dates, negation polarity, quantifier scope) in the field's own established critical-error taxonomy (WMT critical-error categories, SynCED-EnDe, the 2022 EAMT critical-errors taxonomy) rather than inventing an ad hoc list is a credible methodological choice that should transfer to real error distributions reasonably well.\",\n    \"The assumptions section is unusually explicit and independently falsifiable (extractability, localizability, instruction-following locality, baseline fidelity, category coverage), which makes it easy to see exactly which premise a negative result would implicate.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 3,\n      \"justification\": \"The core comparison (localized-certified loop vs. holistic reflect-regenerate) is well-posed and the metrics are appropriate, but several confounds are left unaddressed: checker false positives are never separated from true violations before computing fix/regression rates, span-localization precision (the actual mechanism claimed to bound blast radius) is never measured as its own outcome, and the iterative certified loop is not obviously compute/call-matched against the single-pass baseline.\",\n      \"improvements\": [\n        \"Report the deterministic checker's own precision/recall against a human-annotated sample of invariant violations before using it to score either condition, and report regression-rate results both on all checker-flagged violations and on the human-confirmed subset, since a noisy checker can manufacture spurious 'repairs' that inflate the regression-rate metric independent of the localization-vs-holistic manipulation. Expected impact: closes the most likely reviewer objection to the entire result and would likely raise soundness by 1 point.\",\n        \"Add a directly-measured localization-precision outcome (span width relative to the ground-truth error region) and show it predicts regression rate, so the paper demonstrates the mechanism rather than only reporting its downstream effect. Expected impact: turns an assumption into evidence, meaningful soundness gain.\",\n        \"Match or report call/token budget between condition A (1 critique + 1 regeneration) and condition B (up to the iteration bound), and include a compute-matched ablation (e.g., cap A at the same number of passes, or aggregate A's per-pass edits into a fair single comparison), so a positive result for B cannot be attributed to B simply doing more LLM work. Expected impact: removes an obvious confound, moderate soundness gain.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The writing is clear, terms are defined precisely in a glossary, and the CEGIS mapping is explained at the right level of abstraction for a reader unfamiliar with program synthesis, but the related-work section is materially incomplete for an MT-specific reader (see novelty critique), which will read as a positioning gap to any MT-fluent reviewer.\",\n      \"improvements\": [\n        \"Add the WMT QE-informed APE / segment-level error correction lineage (Deoghare et al. 2023, 2025; WMT25 Task 3 and its 2025 system papers) to related work, and explicitly state what changes relative to it (deterministic vs. learned localization; iterate-to-certificate vs. single-shot edit). Expected impact: this is the single highest-value fix in the whole hypothesis — without it, an MT-track reviewer will likely flag the core mechanism as already explored and score the paper down on originality regardless of how the experiment turns out.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 2,\n      \"justification\": \"As framed, the hypothesis claims a novel transplant of localized, certified repair into MT self-correction, but a directly on-topic MT literature (QE-guided, span-scoped post-editing explicitly designed to curb 'over-correction') already exists and already tests almost the same locality-vs-full-rewrite trade-off, just with a learned localizer instead of a deterministic checker and without an explicit iterate-to-certificate loop. That leaves a real but narrower contribution than currently advertised.\",\n      \"improvements\": [\n        \"Reframe the contribution explicitly as a comparison between three conditions, not two: (A) holistic reflect-regenerate, (B) the proposed deterministic-checker CEGIS loop, and (C) a single-shot QE/LLM-critique-guided localized edit matching the WMT25 winning approach's design (detect error span via a learned/LLM judge, edit only that span, no iteration, no certificate). This isolates which of the two claimed novelties — deterministic vs. learned localization, and iterate-to-certificate vs. single-shot — actually drives any locality benefit, which is now the genuinely open and citable question. Expected impact: this is the change most likely to move the paper from 'the localized-editing effect is already known' to 'here is what specifically survives once you control for that,' which is the paper's real shot at a top-tier-worthy contribution.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"major\",\n      \"description\": \"The related-work section omits the WMT QE-informed Automatic Post-Editing / Segment-level Error Correction lineage, which already implements the hypothesis's core mechanism for MT specifically: scope edits to a detected error span rather than regenerating the whole segment, explicitly to reduce 'over-correction' (the same phenomenon this hypothesis calls 'regression rate'). This includes Deoghare et al. 2023 (EMNLP Findings, 'Quality Estimation-Assisted Automatic Post-Editing'), Deoghare et al. 2025 ('Giving the Old a Fresh Spin: QE-Assisted Constrained Decoding for APE'), and the WMT25 shared task 'Task 3: QE-informed Segment-level Error Correction' with multiple 2025 competing systems (e.g. Padmanabhan 2025's 'Fill in the Blanks' approach explicitly instructs an LLM to replace only QE-flagged error substrings, using a 'Gain-to-Edit ratio' metric that is a close cousin of the proposed regression-rate metric). None of this is cited or discussed, so the hypothesis currently overstates its novelty by comparing only against holistic-regeneration baselines and a general (non-MT) controlled-text-generation paper (LaSEr-Edit), while the closest, most damaging comparison is MT-native localized correction work that already exists.\",\n      \"suggested_action\": \"Add this lineage to related_works with an honest statement of what remains novel relative to it: (1) the localizer/verifier is a deterministic, checkable, interpretable content-invariant checker rather than a learned QE model or LLM judge, which changes what a 'certificate' means (reproducible and auditable rather than a confidence score); (2) the loop iterates to an explicit certificate (every invariant passes) rather than performing a single scoped edit. Then design the experiment (see the contribution-dimension suggestion) to actually isolate these two factors against the existing QE-guided single-shot baseline, not just against holistic regeneration.\"\n      },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The baseline (condition A) is a holistic reflect-and-regenerate loop, which is a weak comparison point once the QE-guided localized-editing lineage above is acknowledged — the field has already partially moved past pure holistic regeneration toward scoped, error-guided editing. A result showing 'localized certified repair beats holistic regeneration' would therefore replicate an already-known finding (targeted edits regress less than full rewrites) rather than answering the more interesting question this hypothesis is actually positioned to answer: does a deterministic, certifiable checker do at least as well as a learned/LLM-based localizer at finding and scoping the repair, with the added benefit of an explicit stopping certificate?\",\n      \"suggested_action\": \"Add a third condition: a single-shot, non-iterative localized edit guided by an LLM-based or word-level-QE-based error localizer (matching the design used in the WMT25 shared task systems), with no certificate and no re-checking loop. Compare all three conditions on fix rate, regression rate, and COMET. This turns the study from 'locality beats holism' (largely expected) into 'deterministic-and-certified beats learned-and-single-shot, or does not' (a real open question with two informative outcomes).\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The deterministic checker's own error rate is never measured or controlled for. If the checker has non-trivial false-positive rate (e.g., flagging a transliterated entity spelling, a spelled-out vs. digit number, or a legitimately reordered negation as a 'violation'), condition B will perform unnecessary repairs on already-correct spans, and any resulting 'new violation introduced' will be an artifact of checker noise rather than evidence about localization vs. holistic repair. This directly threatens the validity of the regression-rate metric, which is the hypothesis's central dependent variable.\",\n      \"suggested_action\": \"Before running the two-condition comparison, validate the checker against a held-out, human-annotated sample of source-target pairs for each of the four categories and report precision/recall. Report the main regression-rate result both on all checker-flagged repairs and restricted to human-confirmed true violations, so a reviewer can see the result is not an artifact of checker imprecision.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"The mechanism the hypothesis is built around — that a marked target span can be localized precisely enough to scope a repair — is asserted as an assumption but never measured as an outcome variable in its own right. Without reporting localization precision (e.g., span width relative to the actual erroneous region, or how often the flagged span fails to contain the true error), a null result on regression rate is ambiguous between 'localization doesn't help' and 'the localizer itself is imprecise.'\",\n      \"suggested_action\": \"Report span-width statistics and localization accuracy (does the flagged span actually contain the invariant-relevant tokens, verified against human annotation on a sample) alongside the main fix-rate/regression-rate/COMET results, and check whether regression rate correlates with span width as the mechanistic story predicts.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"Mixing natural MT errors with deliberately injected invariant-violating errors for statistical power risks inflating fix-rate results for the proposed method in a way that does not generalize: injected errors are, by construction, exactly the error type the deterministic checker was designed to catch, and may be easier to detect and repair than naturally occurring, more ambiguous instances of the same category (e.g., a naturally garbled date vs. a synthetically swapped one).\",\n      \"suggested_action\": \"Report all three headline metrics separately for the natural-only subset and the injection-augmented subset, and briefly justify the injection procedure's realism (e.g., adversarial substitution informed by observed natural error patterns rather than random corruption) so a reviewer can judge whether the injected cases are representative rather than trivially detectable.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The study as described uses a single LLM as both translator/critic/repairer across both conditions with no stated plan to test more than one model family. Since the mechanism the hypothesis relies on (an LLM reliably obeying a 'revise only this span' instruction) is itself an empirical claim (assumption 3) known to vary substantially by model and prompting style, a single-model result would be a narrow existence proof rather than a claim about 'the field's current holistic reflect-and-regenerate baselines' in general, which the hypothesis's title and success criteria implicitly claim to address.\",\n      \"suggested_action\": \"If compute allows, replicate the core comparison (A vs. B, and the added condition C) on at least one additional model family, and report whether the direction and rough magnitude of the fix-rate/regression-rate gap holds; if only one model is feasible, soften the framing to name the specific model rather than 'the field's current baselines.'\"\n    }\n  ],\n  \"score\": 4,\n  \"confidence\": 4,\n  \"relation_type\": null,\n  \"relation_rationale\": \"\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [18] TOOL CALL — Bash · 2026-09-01 04:42:59 UTC

```
python3 -c "import json; json.load(open('/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/iter_1/review_hypo/.terminal_claude_agent_struct_out.json'))" && echo VALID
```

### [19] TOOL RESULT — Bash · 2026-09-01 04:42:59 UTC

```
{"stdout": "VALID", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] ASSISTANT · 2026-09-01 04:43:02 UTC

```
Review complete — score 4 (Borderline Reject), confidence 4. Key finding: a targeted prior-art search turned up an established WMT lineage (QE-informed/segment-level APE, 2023–2025, including a WMT25 shared task) that already does span-scoped, error-guided editing to curb "overcorrection" in MT — the hypothesis's related-work section misses this entirely and compares only against holistic-regeneration baselines and a non-MT controlled-generation paper. The methodology is otherwise sound in intent but has real unaddressed confounds (checker precision never measured, localization precision asserted not measured, no compute parity between the iterative loop and the single-pass baseline). Output written to `.terminal_claude_agent_struct_out.json` and validated as parseable JSON.
```
