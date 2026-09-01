# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 5 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 10:28:07 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

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

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

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

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<context>
<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>
</context>

<artifact_plan>
id: gen_plan_research_1_idx4
type: research
title: Verify the EAMT 2026 Highlights Paper
summary: >-
  Fetch and classify the one EAMT 2026 candidate (arXiv:2605.21135, 'Smarter edits? Post-editing with error highlights and
  translation suggestions') left unverified by art_QAQK2EUnuaCO, using that artifact's exact 6-candidate decision rule, to
  close the project's last open literature-search item.
runpod_compute_profile: cpu_light
question: >-
  Does the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (Tilburg, arXiv:2605.21135)
  vary 'breadth of error localization' (narrow QE-flagged span vs. broadened content-invariant/error detection) and 'iteration/re-verification
  of a repair' (single-pass vs. checker-guided iterated repair) as two independently varied, separately measured factors --
  the same 2x1 design this project's C1-vs-C2 conditions use -- or does it bundle them, vary only one, or fall outside MT
  scoped-repair entirely?
research_plan: |-
  STEP 0 -- Candidate is already located (skip the re-search fallback in the artifact direction): the paper is 'Smarter edits? Post-editing with error highlights and translation suggestions', EAMT 2026 (26th Annual Conference of the European Association for Machine Translation, Tilburg), also indexed as ACL Anthology 2026.eamt-1.41 and arXiv:2605.21135 (HTML at https://arxiv.org/html/2605.21135v2, abstract at https://arxiv.org/abs/2605.21135, PDF via https://arxiv.org/pdf/2605.21135). This was confirmed by two web searches ('EAMT 2026 post-editing error highlights' and 'EAMT 2026 automatic post-editing error span iterative') both returning it as the top hit -- log these two exact queries and their top hits in the report as the 'located via' evidence, matching art_QAQK2EUnuaCO's per-query logging convention. If for any reason this URL 404s or the paper is not this one, re-run those two queries verbatim first before trying anything else.

  STEP 1 -- Fetch the full paper. Use aii-web-tools fetch on https://arxiv.org/html/2605.21135v2 (HTML full text, preferred over the PDF for regex/grep reliability). Also fetch https://aclanthology.org/2026.eamt-1.41/ as a cross-check for the camera-ready venue version in case the arXiv version differs (EAMT papers sometimes get lightly revised between arXiv preprint and camera-ready). Read the full Methodology/Experimental Setup section, not just the abstract.

  STEP 2 -- Extract the exact experimental design. The paper compares four post-editing conditions for professional En-Nl translators: (1) regular PE, no assistance; (2) PE + QE-derived highlights (H-QE), error spans from xCOMET-XXL; (3) PE + APE-derived highlights (H-APE), spans derived by diffing (Levenshtein distance) the raw MT output against an xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), H-APE spans plus the xTower-produced replacement text shown to the translator. Use fetch_grep with these regex patterns against the full HTML/PDF text to pull the exact sentences (not paraphrase) for the report's quoted-evidence requirement: pattern 'xTower|xCOMET' (find every mention, to enumerate exactly how many correction passes xTower runs -- confirm it is one call per sentence, not an iterated loop), pattern 'iterat|re-check|re-verif|re-flag|second pass|repeat' (search for ANY iteration language anywhere in the paper -- if this returns zero hits across the full text, that is decisive evidence of 'varies only one factor / no iteration axis exists at all', directly mirroring art_QAQK2EUnuaCO's finding that Sharma (2025) had zero occurrences of 'iterat'), and pattern 'Levenshtein|error span|highlight' (to confirm exactly how H-QE's narrower xCOMET span and H-APE's broader diff-derived span differ in breadth, since if the paper DOES vary localization breadth as a factor -- H-QE narrow vs H-APE/S-APE broader -- that is the strongest candidate reading toward 'separates the factors', pending the iteration axis check).

  STEP 3 -- Apply art_QAQK2EUnuaCO's exact 4-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope), using the fetch_grep results as quoted evidence. Preliminary reading from the abstract and HTML fetch already done: xTower's correction is a single generation pass per sentence (spans are extracted post-hoc via Levenshtein diff against that one output, not from an iterated checker), and no re-verification or re-check loop appears in the four-condition design -- so the paper likely classifies as 'varies only one factor' (it does vary localization breadth: H-QE's model-driven xCOMET span vs. H-APE/S-APE's diff-derived span, which are different widths) while having NO iteration axis at all (all four conditions are single-pass). This is NOT the same as C1 vs. C2 in this project's design, because C1 vs C2 requires BOTH breadth and iteration to be varied while holding the other fixed -- here iteration is simply absent from every condition, not held fixed as a controlled variable. Confirm or correct this reading against the actual fetch_grep hits before writing it up -- do not assert it without the quoted text in hand, since the abstract-only read has already been shown (via the WebFetch attempts) to be insufficient to settle the iteration question by itself.

  STEP 4 -- Write up the finding with the specific evidence quoted verbatim (sentence(s) describing xTower's role, sentence(s), if any, mentioning iteration, and the sentence describing how H-QE spans vs H-APE spans are obtained). State explicitly what the design difference is from this project's B/D/C1/C2/C protocol: the EAMT paper is a human-productivity/UX study (translator time, edit distance, satisfaction surveys) evaluating whether SHOWING highlights/suggestions to a HUMAN post-editor helps, not an automated repair-loop study measuring fix rate / regression rate / ΔCOMET on LLM-generated repairs -- a second, independent axis of difference beyond the localization/iteration question, worth stating even though it does not by itself settle the classification. If fetch_grep confirms zero iteration language and confirms H-QE/H-APE differ only in span source (not in any repeat-and-recheck mechanism), state the verdict as 'varies only one factor (localization breadth via differing span-source models), no iteration axis present in any condition' and conclude the novelty claim requires NO narrowing -- this paper does not separate localization breadth from iteration as two independently varied factors on the repair/iteration axis, because it never varies iteration at all. If fetch_grep instead surfaces language contradicting this (e.g., xTower is described as applied in multiple rounds, or highlights are re-verified after a first suggestion is shown), report that specific contradicting text and reclassify accordingly -- do not force the preliminary reading if the primary text disagrees.

  STEP 5 -- Handle the failure path explicitly if fetching fails (e.g., arXiv HTML render is incomplete, ACL Anthology page is PDF-only and fetch_grep on the PDF times out, or Methodology section text is truncated in the returned markdown): retry fetch_grep on the PDF URL (https://arxiv.org/pdf/2605.21135) with the same three regex patterns from Step 2, since PDF text extraction sometimes surfaces sections HTML rendering drops. If both HTML and PDF fetches fail to yield the methodology section within two retries each, state plainly in research_out.json that the candidate was located (with URL) but could not be fetched within budget, and that this specific failure -- not a repeat of the prior artifact's generic 'top open item' flag -- is the final, resolved status: the paper cannot be verified, so the novelty claim should note EAMT 2026 as a candidate that exists but was unreachable, rather than carrying it forward as an open item for a nonexistent future iteration.

  STEP 6 -- Also spend one quick search (2-3 min, not a full re-run of the prior artifact's 10-query sweep) checking for a distinct 'iterative error highlighting' or 'incremental post-editing loop' EAMT 2026 paper, in case the prior artifact's 'EAMT 2026' flag actually pointed at a different, unindexed-by-abstract-alone paper -- query 'EAMT 2026 iterative repair verification translation' and 'EAMT 2026 CEGIS translation post-editing' via aii-web-tools search (general mode) to rule out a second, closer candidate before finalizing. If nothing closer surfaces, proceed with the Smarter Edits paper as the definitive candidate and close the item.

  OUTPUT: Populate research_out.json per the RESEARCH executor schema: {answer: the definitive classification (varies only one factor -- localization breadth differs across conditions via differing span-source models, no iteration/re-verification axis present in any of the four conditions -- plus the second-axis note that this is a human-PE-productivity study, not an automated repair-loop study, so it is not even attempting the same measurement this project makes) with the quoted supporting sentences; sources: the arXiv abstract/HTML/PDF URLs and ACL Anthology URL, each with the specific text excerpt used; follow_up_questions: none required, since this closes the project's final open literature item, but note explicitly in the text that no further verification pass is planned or needed. Also produce research_report.md summarizing: (a) the paper located and how; (b) its four-condition design in the same table format art_QAQK2EUnuaCO likely used for its six candidates, for direct comparability; (c) the explicit classification against the four-way decision rule with quoted evidence; (d) the explicit statement that the paper's novelty claim as scoped in this project's paper requires NO further narrowing, OR the specific narrowing required if the fetch_grep evidence contradicts the preliminary reading; (e) a one-line final status: 'EAMT 2026 lead resolved -- no rescoping of the novelty claim required' or the specific alternative finding, written so the paper's Related Work section can cite this artifact as the closing, not opening, statement on this candidate.
explanation: >-
  This closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): an
  EAMT 2026 paper on post-editing with error highlights was surfaced by search but never fetched, so the project's central
  novelty claim -- that no prior MT automatic-post-editing work independently varies localization breadth (narrow QE span
  vs. broadened detection) and iteration/re-verification (single-pass vs. checker-guided repeated repair) as two separate
  factors -- currently rests on six verified negatives plus one open item. Since no further iteration exists after this one,
  the paper's Related Work section needs a definitively resolved status rather than a flagged gap. Preliminary evidence from
  two searches and two fetch attempts already strongly suggests the paper (arXiv:2605.21135 / EAMT 2026, a human-translator
  productivity study comparing QE-derived vs. APE-derived error highlights and correction suggestions from a single xTower-Instruct-13B
  pass) does vary localization breadth across its four conditions but contains no iteration or re-verification mechanism in
  any of them -- consistent with the pattern already found across all six other candidates in the prior artifact, and additionally
  distinguished from this project's automated repair-loop protocol by being a human-in-the-loop UX study rather than an LLM-repair-loop
  study. Confirming this with quoted primary-text evidence (via fetch_grep on the full paper, not the abstract alone) turns
  a hedge into a citable, resolved claim for the paper's Related Work section.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-01 10:28:07 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-web-tools · 2026-09-01 10:28:11 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SYSTEM-USER prompt · 2026-09-01 10:31:23 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison." is too long (at most 250 characters, got 293)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
