# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 5 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 10:28:01 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1
```

### [2] SYSTEM-USER prompt · 2026-09-01 10:28:07 UTC

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

### [3] HUMAN-USER prompt · 2026-09-01 10:28:07 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Skill · 2026-09-01 10:28:11 UTC

```
aii-web-tools
```

### [5] TOOL RESULT — Skill · 2026-09-01 10:28:11 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [6] TOOL CALL — Bash · 2026-09-01 10:28:13 UTC

```
mkdir -p /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "PY=$PY"
ls "$SKILL_DIR/scripts/"
```

### [7] TOOL RESULT — Bash · 2026-09-01 10:28:13 UTC

```
{"stdout": "PY=/ai-inventor/.claude/skills/aii-web-tools/../.ability_client_venv/bin/python\n_wayback.py\naii_fast_web_fetch.py\naii_fast_web_search.py\naii_verify_quotes.py\ncheck_env.sh\nserver_requirements.txt", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [8] TOOL CALL — Bash · 2026-09-01 10:28:19 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "=== Q1 ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "EAMT 2026 post-editing error highlights" --max-results 8
echo "=== Q2 ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "EAMT 2026 automatic post-editing error span iterative" --max-results 8
```

### [9] TOOL RESULT — Bash · 2026-09-01 10:28:19 UTC

```
{"stdout": "=== Q1 ===\nSearch: EAMT 2026 post-editing error highlights  [general via ddgs]\nFound: 8 results\n\n1. Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.41/\n   2026. Smarter edits? Post-editing with error highlights and translation suggestions. In Proceedings of the 26th Annual Conference of the European Association for Machine Translation (Volume 1), pages ...\n\n2. Programme - EAMT 2026\n   https://eamt2026.org/programme\n   June 18, 2026 - Results show that terminology is the highest-risk domain across the entire workflow (34.1%), followed by tense/aspect (15.2%) and style (13.6%). ChatGPT-related errors account for 50.8...\n\n3. [2605.21135] Smarter edits? Post-editing with error highlights and translation suggestions\n   https://arxiv.org/abs/2605.21135\n   June 16, 2026 - As MT quality increases, interest ... remains limited. In this work, we explore the usefulness of LLM-derived error highlights and correction suggestions based on automatic post-editin...\n\n4. Smarter edits? Post-editing with error highlights and translation suggestions\n   https://arxiv.org/html/2605.21135v1\n   May 21, 2026 - As MT quality increases, interest ... for their usefulness remains limited. In this work, we explore the usefulness of LLM-derived error highlights and correction suggestions based on a...\n\n5. Calls for Papers - EAMT 2026\n   https://eamt2026.org/calls-for-papers\n   Submit the paper as a PDF to the EasyChair EAMT 2026 page (submission type: EAMT2026 technical research). ... Submissions (up to 10 pages, plus unlimited references and appendices) are invited for aca...\n\n6. AI Post-Editing in Production: A 71,262-Segment Evaluation Across Five Domains, Ten Languages and Five Systems - ACL Anthology\n   https://aclanthology.org/2026.eamt-2.24/\n   LLMT does not match this quality, though it may suit less quality-sensitive domains. We observe how AIPE’s gains vary according to pre-translation type, with fuzzy translation memory matches over-repr...\n\n7. EAMT 2026 : European Association for Machine Translation Conferences/Workshops\n   http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=190116\n   EAMT 2026 : European Association for Machine Translation Conferences/Workshops...\n\n8. Tutorials - EAMT 2026\n   https://eamt2026.org/tutorials\n   June 15, 2026 - The landscape of machine translation (MT) has evolved dramatically since the advent of neural MT (NMT), which marked a breakthrough in translation quality and fluency. More recently, t...\n\n=== Q2 ===\nSearch: EAMT 2026 automatic post-editing error span iterative  [general via ddgs]\nFound: 8 results\n\n1. Programme - EAMT 2026\n   https://eamt2026.org/programme\n   June 18, 2026 - However, meeting specific stylistic and lexical requirements of end users remains challenging. This paper explores the effectiveness of an automated post-editing approach (APE) in a re...\n\n2. MQM-APE: Toward High-Quality Error Annotation Predictors with Automatic Post-Editing in LLM Translation Evaluators\n   https://arxiv.org/html/2409.14335v1\n   September 22, 2024 - Similarly, studies on self-correction (Madaan et al., 2024) enhance translation through iterative corrections (Chen et al., 2023; Pan et al., 2024), with Xu et al. (2024) proposin...\n\n3. Automatic Post Editing\n   https://www.catalyzex.com/s/Automatic+Post+Editing\n   Students translat-ed short specialised English Wikipedia texts into Catalan or Spanish, generated four system outputs, evaluated them using automatic metrics and human adequa-cy/fluency assessment, se...\n\n4. Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.41/\n   [Smarter edits? Post-editing with error highlights and translation suggestions](https://aclanthology.org/2026.eamt-1.41/) (van Tellingen et al., EAMT 2026)...\n\n5. AI Post-Editing in Production: A 71,262-Segment Evaluation Across Five Domains, Ten Languages and Five Systems - ACL Anthology\n   https://aclanthology.org/2026.eamt-2.24/\n   LLMT does not match this quality, though it may suit less quality-sensitive domains. We observe how AIPE’s gains vary according to pre-translation type, with fuzzy translation memory matches over-repr...\n\n6. Smarter edits? Post-editing with error highlights and translation suggestions\n   https://arxiv.org/html/2605.21135v2\n   June 16, 2026 - For this reason, we used the translation corrections (APE) obtained from xTower to identify error spans. We compared the raw MT output and APE’d sentence using Levenshtein distance. Th...\n\n7. ASR Error Correction: Methods & Advances\n   https://www.emergentmind.com/topics/asr-error-correction-aec\n   The post-editing algorithm based ... by segmenting ASR output into fixed-length word tokens (typically, K=6), issuing search queries to Bing, and examining the HTML response for corrections (\"Includin...\n\n8. Bridging Domains for Automatic Post-Editing: A Classifier-Guided Multi-Domain Adaptation Framework - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.31/\n   2026. Bridging Domains for Automatic Post-Editing: A Classifier-Guided Multi-Domain Adaptation Framework. In Proceedings of the 26th Annual Conference of the European Association for Machine Translati...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] ASSISTANT · 2026-09-01 10:28:23 UTC

```
Located confirmed. Now fetching the full paper and running the fetch_grep patterns.
```

### [11] TOOL CALL — Bash · 2026-09-01 10:28:23 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "=== FETCH HTML v2 (part1) ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2605.21135v2" --max-chars 12000
```

### [12] TOOL RESULT — Bash · 2026-09-01 10:28:23 UTC

```
{"stdout": "=== FETCH HTML v2 (part1) ===\nURL: https://arxiv.org/html/2605.21135v2\nType: HTML\nLength: 67562 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n×\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2605.21135v2 \"Back to abstract page\") [ Download PDF](/pdf/2605.21135v2 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Related work\n     1. 2.1 Explainable MT assessment\n     2. 2.2 Post-editing with quality estimation\n  4. 3 Methodology\n     1. 3.1 Data\n     2. 3.2 Models\n     3. 3.3 Post-editing conditions\n     4. 3.4 Participants\n     5. 3.5 Post-editing task\n     6. 3.6 Interface\n  5. 4 Results\n     1. 4.1 Productivity\n        1. Process data\n        2. Perceived effect on productivity\n     2. 4.2 Quality\n        1. DA ratings\n        2. Perceived effect on quality\n     3. 4.3 Do highlights help translators spot and fix critical errors?\n        1. Analysis of post-edits\n        2. Perceived helpfulness in spotting errors\n     4. 4.4 Are APE highlights more accurate and useful than QE highlights?\n        1. Overlap of highlights with oracle edits\n        2. Perceived usefulness and accuracy\n     5. 4.5 How useful are correction suggestions?\n        1. Percentage of accepted suggestions\n        2. Perceived usefulness and accuracy\n     6. 4.6 Are there differences between domains?\n     7. 4.7 Translator perception and confidence\n        1. Likes and dislikes\n        2. Confidence\n  6. 5 Limitations and future work\n  7. 6 Ethical considerations and impact\n  8. 7 Conclusion\n     1. Acknowledgements\n  9. References\n  10. A Overlap between highlights and human edits\n  11. B Data\n  12. C Statistical tests\n  13. D Post-editing guidelines\n     1. D.1 Interface-instructions of use\n        1. 1\\. Post-editing\n        2. 2\\. Post-editing with error annotations\n        3. 3\\. Post-editing with error annotations and suggestions\n     2. D.2 Task protocol\n        1. Setting up your work environment\n        2. Workflow\n        3. After finishing the task\n        4. Requirements\n\n\n\n[ License: CC BY-NC-ND 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2605.21135v2 [cs.CL] 16 Jun 2026\n\n# Smarter edits?   \nPost-editing with error highlights and translation suggestions\n\nFleur V.J. van Tellingen  Affiliation: Leiden University Centre for Linguistics  Email: [a.karakanta@leidenuniv.nl](mailto:) Gautam Ranka  Affiliation: Visvesvaraya National Institute of Technology  Dora Žugčić  Affiliation: Department of Bionanoscience, Faculty of Applied Sciences, Delft University of Technology  Joyce van der Wal  Affiliation: Pedagogical Sciences, Leiden University  Andrea Camasta  Affiliation: Faculty of Science, Leiden University  Livio Guerra  Affiliation: Faculty of Science, Leiden University  Alina Karakanta  Affiliation: Leiden University Centre for Linguistics \n\n###### Abstract\n\nAs MT quality increases, interest in enhanced post-editing features such as QE-derived error highlights is growing, yet evidence for their usefulness remains limited. In this work, we explore the usefulness of LLM-derived error highlights and correction suggestions based on automatic post-editing (APE). We conduct a study where professional translators (En→\\rightarrowNl) post-edit translations using APE error highlights and correction suggestions and compare productivity, quality and user experience to regular PE and PE with QE-derived highlights. While no condition yielded productivity or quality gains compared to regular PE, APE highlights were better received than QE-derived highlights, and correction suggestions improved the overall user experience.\n\n## 1 Introduction\n\nGenerative large language models (LLMs) have demonstrated remarkable proficiency not only for machine translation (MT) but across several translation-related tasks, among which assessing MT quality [19], and fine-grained error detection and correction [12, 22]. Despite the growing interest in explainable MT evaluation, the usefulness of LLM suggestions in augmenting translators’ workflows has been scarcely explored. Previous work has focused heavily on quality estimation (QE) features for enhancing translators’ productivity, but the results were inconclusive, with limited or no productivity gains [2, 31, 32], even when errors were derived from human edits rather than QE [30]. Other studies have indicated that providing more intelligible feedback, such as explicit translation suggestions, can support translators more effectively [8].\n\nIn this work, we investigate whether signals derived from automatic post-editing (APE) instead of QE can enable smarter editing decisions and enhance translators’ productivity, experience and confidence. As shown in Table 1, error highlights obtained from QE (H-QE) sometimes only cover parts of words. In addition, there is no justification why highlighted characters are considered an error. Correction suggestions (S-APE) give translators more interpretable guidance about where and how to intervene. We thus ask the following questions: Could APE suggestions enhance productivity by helping translators edit machine-translated texts more efficiently? As MT outputs improve in quality, could such features assist translators in detecting errors, resulting in higher-quality translations? What is their impact on translators’ perception and confidence?\n\nSRC |  | How to find out if you’re flying on a Boeing?  \n---  \nREF | Hoe komt u erachter of u in een Boeing vliegt?  \nPE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nH-QE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nH-APE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nS-APE |  | Hoe kunt u ontdekken(erachter komen) of u  \n---  \nvliegt in een Boeing?  \nTable 1: Example of highlights derived by QE (H-QE) and APE (H-APE), together with correction suggestions (S-APE: text in parentheses). \n\nTo answer these questions, we conducted a user study incorporating automatic error annotations and correction suggestions in a realistic post-editing setting. Eight English→\\rightarrowDutch professional translators post-edited machine translated texts in two domains (news, biomedical) in four conditions: 1) simple post-editing (PE), 2) post-editing with error highlights from quality estimation (H-QE), 3) post-editing with error highlights from automatic post-editing (H-APE) and 4) post-editing with error highlights and correction suggestions (S-APE). The PE task was conducted in SmartPE, an interface incorporating LLM suggestions, which logs granular editing data. We collected product and process data, and user ratings on perceived quality of MT, error highlights and suggestions. Lastly, translators provided qualitative feedback through semi-structured post-task interviews. Our contributions are as follows:\n\n  * •\n\nA rich multi-parallel post-editing dataset (14.400 words) combining raw MT with automatic error annotations and correction suggestions, and 8 PE versions, all of them evaluated following the ESA protocol [20], keystrokes, user perception scores and quality ratings in two domains.11 1 Data and code: https://github.com/fatalinha/smarter-edits\n\n  * •\n\nSmartPE: A new post-editing interface incorporating error highlights and translation suggestions, released open-source.22 2 https://github.com/fatalinha/SmartPE\n\n  * •\n\nAn analysis of productivity, quality, and user experience in post-editing with various degrees of LLM assistance.\n\n\n\n\nWe publicly release the data, code and post-editing interface to facilitate future work on LLM suggestions in post-editing workflows.\n\n## 2 Related work\n\n### 2.1 Explainable MT assessment\n\nAutomatic MT evaluation has shifted from string overlap metrics [27, 28], which yield a single holistic score, toward learned metrics and fine-grained QE systems providing insight into the nature or location of translation errors [16]. For instance, xCOMET [15] unifies segment-level quality prediction with span detection, identifying both the location and severity of errors within a single model. Concurrently, the LLM-as-judge paradigm [37] has been applied to MT evaluation through tools such as Auto-MQM [12], EAPrompt [22] and GEMBA-MQM [18, 20], which prompt LLMs with quality criteria to elicit span-level annotations aligned with the MQM error typology [21] or free-text explanations [34].\n\nBuilding on QE signals, a natural extension is to move from error detection to error correction through APE. In this paired paradigm, APE systems leverage QE predictions to guide targeted corrections for raw MT output [7, 12, 10, 34]. Recently, LLMs were shown to produce meaningful and targeted edits that improve overall translation quality [29, 3]. Nevertheless, LLMs show a different PE behaviour than professional translators, missing errors and producing hallucinated edits, or performing preferential edits which translators are instructed to avoid [23, 9]. Despite this, multi-agent frameworks that simulate collaborative practices in human translation workflows are increasingly used in industry [5, 36]. In this work, we leverage QE paired with APE signals to generate PE suggestions in translators’ workflows.\n\n### 2.2 Post-editing with quality estimation\n\nThe potential of QE to enhance post-editing productivity has been explored in a number of user studies, with mixed and often inconclusive results. Earlier studies focused on sentence-level QE in statistical MT, by displaying a quality score or using a traffic light systems (e.g. red, yellow, green) suggesting the amount of PE required. These approaches found QE to improve PE efficiency only under specific conditions, such as when MT output quality was low [2] or when QE predictions were sufficiently accurate [11, 35]. ?) found no significant effects on either technical or cognitive effort and suggested combining sentence-level QE scores with phrase or word-level QE indications. Taking on this direction, ?) tried to determine a quality threshold at which QE is actually beginning to be useful for PE, and how to best present word-level QE information. They reported only limited productivity gains, arguing that QE systems need an F1 score of at least 80% to support PE, an accuracy level that at the time had not been not reached.\n\nWith the increased quality brought by neural MT and LLMs, errors became even harder to detect, which renewed interest in QE for PE. Using human ratings instead of automatic QE scores, ?) found that sentence-level QE enhanced students’ PE productivity only for high-quality segments. However, this varied by expertise level while inaccurate highlighting introduced confusion. The study most closely related to our work is that of ?), who systematically compared several error highlighting conditions in two language pairs (En→\\rightarrowIt/Nl): a supervised state-of-the-art QE model trained on human annotations (xCOMET), an unsupervised method exploiting MT model uncertainty, oracle spans derived from consensus human post-edits, and a no-highlight baseline. They similarly reported limited or no overall productivity gains, even with oracle spans. Effectiveness varied considerably across language pairs, domains, and post-editors, pointing to translator attitudes, propensity to edit and working styles as confounding factors.\n\nThese findings collectively suggest that error highlighting alone is insufficient to reliably support post-editors. A complementary direction is to provide explicit translation suggestions as alternatives, either in a static [8] or interactive fashion [17, 1, 4]. This approach has been shown to increase productivity and help translators interpret suggestions more effectively. In this work, we contribute to this direction by assessing alternatives to QE-based erro", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] ASSISTANT · 2026-09-01 10:28:29 UTC

```
Good, confirming the design already. Now fetch_grep the specific patterns from Step 2.
```

### [14] TOOL CALL — Bash · 2026-09-01 10:28:29 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "=== xTower|xCOMET ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/html/2605.21135v2" --pattern "xTower|xCOMET" --max-matches 30 --context-chars 200
```

### [15] TOOL RESULT — Bash · 2026-09-01 10:28:29 UTC

```
{"stdout": "=== xTower|xCOMET ===\nURL: https://arxiv.org/html/2605.21135v2\nType: HTML\nPattern: xTower|xCOMET (14 matches in 67562 chars)\n\n--- Content ---\n\n8140:...erlap metrics [27, 28], which yield a single holistic score, toward learned metrics and fine-grained QE systems providing insight into the nature or location of translation errors [16]. For instance, xCOMET [15] unifies segment-level quality prediction with span detection, identifying both the location and severity of errors within a single model. Concurrently, the LLM-as-judge paradigm [37] has been ap...\n--\n11114:...work is that of ?), who systematically compared several error highlighting conditions in two language pairs (En→\\rightarrowIt/Nl): a supervised state-of-the-art QE model trained on human annotations (xCOMET), an unsupervised method exploiting MT model uncertainty, oracle spans derived from consensus human post-edits, and a no-highlight baseline. They similarly reported limited or no overall productivity...\n--\n12831:...n, four texts were selected from the devsets of the WMT24 news shared task and adjusted to 200-word segments.\n\n### 3.2 Models\n\nTranslation: The selected excerpts were translated into Dutch (NL) using xTower-Instruct-13B-v0.1 [34] with the default template provided on HuggingFace33 3 https://huggingface.co/Unbabel/TowerInstruct-13B-v0.1.\n\nError spans: xCOMET-XXL [14] was used to automatically identify error spans (H-QE).\n\nTranslation corrections: The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE).\n\n### 3.3 Post-editing conditions\n\nRegular post-editing (PE): Translators post-edit without any highlights.\n\nPE with QE error highlights (H-QE): Error spans obtained from xCOMET were used to highlight the text. Minor errors were highlighted in yellow, major in orange.\n\nPE with APE error highlights (H-APE): Looking at the obtained error spans from xCOMET, we noticed that the highlights were often not very informative for human post-editing since they contained highlights that were not easily interpretable, e.g. single characters (see Table 1). For this reason, we used the translation corrections (APE) obtained from xTower to identify error spans. We compared the raw MT output and APE’d sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors, regardless of whether they were marked as an error by xCOMET. As with this approach there was no way to determine the error severity, all errors were highlighted as minor (yellow). Initial tests showed that the highlights obtained with this approach better cor...\n--\n14972:...l errors were manually inserted in each text (negation, serious mistranslation, serious omission) before annotating the errors. Out of the 16 total inserted critical errors, only 11 were annotated by xCOMET and 10 by xTower. However, since we wanted to determine whether highlights really help translators spot critical errors, we manually added major error tags around the missed errors.\n\n### 3.4 Participants\n\nEight profe...\n--\n56340:...(AP) and Area Under the Curve (AUC) for the spans obtained from different methods and human (oracle) post-edit spans.\n\nThe spans obtained from automatic post-edits based on translation corrections of xTower (H-APE) demonstrated higher scores for both domains compared to those obtained from xCOMET (H-QE). This showed that APE suggestions align more closely with human post-edits than error spans identified by quality estimation methods and proved the motivation for the study.\n\n## Appendix B Dat...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] ASSISTANT · 2026-09-01 10:28:35 UTC

```
This confirms xTower runs a single pass per sentence (Translation → error spans via xCOMET-XXL → one xTower correction pass). Now check the iteration pattern.
```

### [17] TOOL CALL — Bash · 2026-09-01 10:28:35 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "=== iteration terms ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/html/2605.21135v2" --pattern "iterat|re-check|re-verif|re-flag|second pass|repeat" -i --max-matches 30 --context-chars 200
echo "=== Levenshtein|error span|highlight ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/html/2605.21135v2" --pattern "Levenshtein|error span|highlight" --max-matches 40 --context-chars 150
```

### [18] TOOL RESULT — Bash · 2026-09-01 10:28:35 UTC

```
{"stdout": "=== iteration terms ===\nURL: https://arxiv.org/html/2605.21135v2\nType: HTML\nPattern: iterat|re-check|re-verif|re-flag|second pass|repeat (2 matches in 67562 chars)\n\n--- Content ---\n\n19108:...al translation (PET) and as a group mean. The group mean is nearly flat across conditions, showing no productivity gains compared to regular PE. The results were confirmed statistically using one-way repeated measures ANOVA on log-transformed PET-level means (see Appendix, Table 8), which revealed no significant effect of condition on productivity. We observe that individual PET trajectories cross consi...\n--\n57893:... | F(3, 21) | p | partial η\\eta²  \n---|---|---|---  \nProductivity | 0.75 | .532 | .097  \nKeystrokes | 0.33 | .803 | .045  \nTime | 0.14 | .937 | .019  \nHT_DA | 0.56 | .646 | .074  \nTable 8: Results of Repeated Measures ANOVA reported in Sections 4.1 and 4.2.\n\nDomain differences were examined using a combination of Welch’s independent samples t-tests for continuous variables (MT_DA, HT_DA, productivity, a...\n=== Levenshtein|error span|highlight ===\nURL: https://arxiv.org/html/2605.21135v2\nType: HTML\nPattern: Levenshtein|error span|highlight (115 matches in 67562 chars)\n\n--- Content ---\n\n1095:...cess data\n        2. Perceived effect on productivity\n     2. 4.2 Quality\n        1. DA ratings\n        2. Perceived effect on quality\n     3. 4.3 Do highlights help translators spot and fix critical errors?\n        1. Analysis of post-edits\n        2. Perceived helpfulness in spotting errors\n     4. 4.4 Are APE highlights more accurate and useful than QE highlights?\n        1. Overlap of highlights with oracle edits\n        2. Perceived usefulness and accuracy\n     5. 4.5 How useful are correction suggestions?\n        1. Percentage of accepted ...\n--\n1864:...mitations and future work\n  7. 6 Ethical considerations and impact\n  8. 7 Conclusion\n     1. Acknowledgements\n  9. References\n  10. A Overlap between highlights and human edits\n  11. B Data\n  12. C Statistical tests\n  13. D Post-editing guidelines\n     1. D.1 Interface-instructions of use\n        1. 1\\. Post...\n--\n2484:...tps://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2605.21135v2 [cs.CL] 16 Jun 2026\n\n# Smarter edits?   \nPost-editing with error highlights and translation suggestions\n\nFleur V.J. van Tellingen  Affiliation: Leiden University Centre for Linguistics  Email: [a.karakanta@leidenuniv.nl](mai...\n--\n3230:...den University Centre for Linguistics \n\n###### Abstract\n\nAs MT quality increases, interest in enhanced post-editing features such as QE-derived error highlights is growing, yet evidence for their usefulness remains limited. In this work, we explore the usefulness of LLM-derived error highlights and correction suggestions based on automatic post-editing (APE). We conduct a study where professional translators (En→\\rightarrowNl) post-edit translations using APE error highlights and correction suggestions and compare productivity, quality and user experience to regular PE and PE with QE-derived highlights. While no condition yielded productivity or quality gains compared to regular PE, APE highlights were better received than QE-derived highlights, and correction suggestions improved the overall user experience.\n\n## 1 Introduction\n\nGenerative large language models (LLMs) have demonstrated rema...\n--\n4998:...(APE) instead of QE can enable smarter editing decisions and enhance translators’ productivity, experience and confidence. As shown in Table 1, error highlights obtained from QE (H-QE) sometimes only cover parts of words. In addition, there is no justification why highlighted characters are considered an error. Correction suggestions (S-APE) give translators more interpretable guidance about where and how to intervene. W...\n--\n6016:...unt u ontdekken of u vliegt in een Boeing?  \nS-APE |  | Hoe kunt u ontdekken(erachter komen) of u  \n---  \nvliegt in een Boeing?  \nTable 1: Example of highlights derived by QE (H-QE) and APE (H-APE), together with correction suggestions (S-APE: text in parentheses). \n\nTo answer these questions, we conducted a...\n--\n6496:...rs post-edited machine translated texts in two domains (news, biomedical) in four conditions: 1) simple post-editing (PE), 2) post-editing with error highlights from quality estimation (H-QE), 3) post-editing with error highlights from automatic post-editing (H-APE) and 4) post-editing with error highlights and correction suggestions (S-APE). The PE task was conducted in SmartPE, an interface incorporating LLM suggestions, which logs granular editing data. We collected product and process data, and user ratings on perceived quality of MT, error highlights and suggestions. Lastly, translators provided qualitative feedback through semi-structured post-task interviews. Our contributions are as follows:\n\n...\n--\n7472:...tings in two domains.11 1 Data and code: https://github.com/fatalinha/smarter-edits\n\n  * •\n\nSmartPE: A new post-editing interface incorporating error highlights and translation suggestions, released open-source.22 2 https://github.com/fatalinha/SmartPE\n\n  * •\n\nAn analysis of productivity, quality, and user e...\n--\n10841:...nd that sentence-level QE enhanced students’ PE productivity only for high-quality segments. However, this varied by expertise level while inaccurate highlighting introduced confusion. The study most closely related to our work is that of ?), who systematically compared several error highlighting conditions in two language pairs (En→\\rightarrowIt/Nl): a supervised state-of-the-art QE model trained on human annotations (xCOMET), an unsupervised method exploiting MT model uncertainty, oracle spans derived from consensus human post-edits, and a no-highlight baseline. They similarly reported limited or no overall productivity gains, even with oracle spans. Effectiveness varied considerably across language...\n--\n11580:...tors, pointing to translator attitudes, propensity to edit and working styles as confounding factors.\n\nThese findings collectively suggest that error highlighting alone is insufficient to reliably support post-editors. A complementary direction is to provide explicit translation suggestions as alternatives, ...\n--\n12002:...nd help translators interpret suggestions more effectively. In this work, we contribute to this direction by assessing alternatives to QE-based error highlighting through APE-based error highlights and correction suggestions.\n\n## 3 Methodology\n\n### 3.1 Data\n\nThe data for the PE task comes from two domains: news and biomedical. Both domains cont...\n--\n13035:...e provided on HuggingFace33 3 https://huggingface.co/Unbabel/TowerInstruct-13B-v0.1.\n\nError spans: xCOMET-XXL [14] was used to automatically identify error spans (H-QE).\n\nTranslation corrections: The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE).\n\n### 3.3 Post-editing conditions\n\nRegular post-editing (PE): Translators post-edit without any highlights.\n\nPE with QE error highlights (H-QE): Error spans obtained from xCOMET were used to highlight the text. Minor errors were highlighted in yellow, major in orange.\n\nPE with APE error highlights (H-APE): Looking at the obtained error spans from xCOMET, we noticed that the highlights were often not very informative for human post-editing since they contained highlights that were not easily interpretable, e.g. single characters (see Table 1). For this reason, we used the translation corrections (APE) obtained from xTower to identify error spans. We compared the raw MT output and APE’d sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors, regardless of whether they were marked as an error by xCOMET. As with this approach there was no way to determine the error severity, all errors were highlighted as minor (yellow). Initial tests showed that the highlights obtained with this approach better correspond to human PE edits compared to QE spans (A...\n--\n[75 more matches not shown]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [19] ASSISTANT · 2026-09-01 10:28:43 UTC

```
The two "iterat" matches are statistical ("repeated measures ANOVA"), not repair iteration. Zero genuine iteration-language hits. Now the quick Step 6 sweep and S-APE confirmation.
```

### [20] TOOL CALL — Bash · 2026-09-01 10:28:43 UTC

```
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
echo "=== S-APE def ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/html/2605.21135v2" --pattern "S-APE|suggestions? \(" --max-matches 15 --context-chars 250
echo "=== Q3 iterative repair verification ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "EAMT 2026 iterative repair verification translation" --max-results 8
echo "=== Q4 CEGIS translation post-editing ==="
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "EAMT 2026 CEGIS translation post-editing" --max-results 8
```

### [21] TOOL RESULT — Bash · 2026-09-01 10:29:05 UTC

```
{"stdout": "=== S-APE def ===\nURL: https://arxiv.org/html/2605.21135v2\nType: HTML\nPattern: S-APE|suggestions? \\( (29 matches in 67562 chars)\n\n--- Content ---\n\n5172:...lators’ productivity, experience and confidence. As shown in Table 1, error highlights obtained from QE (H-QE) sometimes only cover parts of words. In addition, there is no justification why highlighted characters are considered an error. Correction suggestions (S-APE) give translators more interpretable guidance about where and how to intervene. We thus ask the following questions: Could APE suggestions enhance productivity by helping translators edit machine-translated texts more efficiently? As MT outputs impr...\n--\n5911:...ing on a Boeing?  \n---  \nREF | Hoe komt u erachter of u in een Boeing vliegt?  \nPE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nH-QE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nH-APE | Hoe kunt u ontdekken of u vliegt in een Boeing?  \nS-APE |  | Hoe kunt u ontdekken(erachter komen) of u  \n---  \nvliegt in een Boeing?  \nTable 1: Example of highlights derived by QE (H-QE) and APE (H-APE), together with correction suggestions (S-APE: text in parentheses). \n\nTo answer these questions, we conducted a user study incorporating automatic error annotations and correction suggestions in a realistic post-editing setting. Eight English→\\rightarrowDutch professional translators post-edit...\n--\n6670:...in four conditions: 1) simple post-editing (PE), 2) post-editing with error highlights from quality estimation (H-QE), 3) post-editing with error highlights from automatic post-editing (H-APE) and 4) post-editing with error highlights and correction suggestions (S-APE). The PE task was conducted in SmartPE, an interface incorporating LLM suggestions, which logs granular editing data. We collected product and process data, and user ratings on perceived quality of MT, error highlights and suggestions. Lastly, trans...\n--\n14536:...er correspond to human PE edits compared to QE spans (Appendix A).\n\nFigure 1: SmartPE: Post editing with error highlights (H-QE and H-APE). Major errors in orange, minor in yellow. Figure 2: SmartPE: Post editing with error highlights and correction suggestions (S-APE).\n\nPE with APE error highlights and correction suggestions (S-APE): The error spans identified in H-APE were paired to their APE correction.\n\nTo test the ability of translators to identify critical errors, two critical errors were manually inserted in each text (negation, serious mistranslation, serious omission) ...\n--\n16803:...effects. The sessions were screen-recorded. After post-editing each text, the translators answered a short questionnaire on the perceived text difficulty, MT quality, error span quality and usefulness, perceived quality and usefulness of translation suggestions (where applicable). At the end of the PE task, each translator participated in a semi-structured interview to collect quantitative feedback on their user experience and confidence.\n\n### 3.6 Interface\n\nWe developed SmartPE, a basic and simple-to-use in...\n--\n17533:...lso helps control for translators’ familiarity with CAT tools. Screenshots of the interface are shown in Figures 1 and 2. The target text can contain highlights marking the type of error: light yellow for minor, orange for major. In addition, in the S-APE condition, correction suggestions appear in a black box once the user hovers the mouse over a highlight. By clicking on the suggestion, the highlighted text is substituted by the suggested text. Each interaction, including focus (which segment is ac...\n--\n20197:... 5). Most translators (3) reported reduced productivity, primarily because they had to spend additional time identifying and deleting incorrect highlights. The three other translators reported that their productivity remained about the same. For the S-APE suggestions, however, six participants thought their productivity had increased.\n\nEven though process data do not show any clear average improvements in productivity, the S-APE suggestions were beneficial for some translators and gave them the impression of improved productivity. These findings are in line with previous work which noted strong individual differences in productivity among translators [30].\n\n### 4.2 Quality\n...\n--\n[14 more matches not shown]\n=== Q3 iterative repair verification ===\nSearch: EAMT 2026 iterative repair verification translation  [general via exa]\nFound: 7 results\n\n1. Iterative Translation Refinement with Large Language Models - ACL Anthology\n   https://aclanthology.org/2024.eamt-1.17/\n   Iterative Translation Refinement with Large Language Models - ACL Anthology\n\nPinzhen Chen, Zhicheng Guo, Barry Haddow, Kenneth Heafield\n\n---\n\n##### Abstract\n\nWe propose iteratively prompting a large l...\n\n2. EAMT 2026 - European Association for Machine Translation\n   https://eamt2026.org/\n   EAMT 2026 - European Association for Machine Translation\n\n# EAMT 2026 European Association for Machine Translation \n\n 26th Annual Conference \n\n June 15–18, 2026 \n\n Schouwburg Concertzaal Tilburg \n\n###...\n\n3. Programme\n   https://eamt2026.org/programme\n   Programme - EAMT 2026\n\n## On this page\n\nDay 0 (15 June)\n\nDay 1 (16 June)\n\nDay 2 (17 June)\n\nDay 3 (18 June)\n\nBest Paper Nominees\n\nDownload the programme (PDF)\n\n## Programme\n\nBrowse the programme below ...\n\n4. TEaR: Improving LLM-based Machine Translation with Systematic Self-Refinement\n   https://doi.org/10.18653/v1/2025.findings-naacl.218\n   # TEaR: Improving LLM-based Machine Translation with Systematic Self-Refinement\n\nPublished: 2025-01-01. 19 citations.\n\n## Authors\n\n- Zhaopeng Feng: h-index 7; 213 citations\n- Yan Zhang: h-index 8; 321...\n\n5. Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.41/\n   Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n\n---\n\n##### Abstract\n\nAs MT quality increases, interest in enhanced post-editing features such as QE-deriv...\n\n6. What Does LLM Refinement Actually Improve? A Systematic Study on Document-Level Literary Translation\n   https://aclanthology.org/2026.acl-long.268.pdf\n   # What Does LLM Refinement Actually Improve? A Systematic Study on Document-Level Literary Translation\n\nPublished: 2026-01-01. 0 citations.\n\n## Authors\n\n- Shaomu Tan: h-index 2; 8 citations\n- Dawei Zh...\n\n7. AMART: A multi-agent reflective framework for detecting and correcting faithfulness errors in translation\n   https://doi.org/10.1016/j.ipm.2026.104819\n   # AMART: A multi-agent reflective framework for detecting and correcting faithfulness errors in translation\n\nInformation Processing & Management. Published: 2026-04-16. 0 citations.\n\n## Authors\n\n- Jia...\n\n=== Q4 CEGIS translation post-editing ===\nSearch: EAMT 2026 CEGIS translation post-editing  [general via exa]\nFound: 7 results\n\n1. Programme\n   https://eamt2026.org/programme\n   Programme - EAMT 2026\n\n## On this page\n\nDay 0 (15 June)\n\nDay 1 (16 June)\n\nDay 2 (17 June)\n\nDay 3 (18 June)\n\nBest Paper Nominees\n\nDownload the programme (PDF)\n\n## Programme\n\nBrowse the programme below ...\n\n2. Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.41/\n   Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\n\n---\n\n##### Abstract\n\nAs MT quality increases, interest in enhanced post-editing features such as QE-deriv...\n\n3. EAMT 2026 - European Association for Machine Translation\n   https://eamt2026.org/\n   EAMT 2026 - European Association for Machine Translation\n\n# EAMT 2026 European Association for Machine Translation \n\n 26th Annual Conference \n\n June 15–18, 2026 \n\n Schouwburg Concertzaal Tilburg \n\n###...\n\n4. Proceedings of the 26th Annual Conference of the European Association for Machine Translation\n   https://aclanthology.org/2026.eamt-2.pdf\n   ### Proceedings of the 26th Annual Conference of the European Association for Machine Translation\n\n### Volume 2: Products and Projects, Implementations and Case Studies\n\n#### 16–18 June 2026 Tilburg, ...\n\n5. BlAInded by Fluency: How Idiomatic Machine Translation Outputs Affect Student Post-Editors’ Edit Types - ACL Anthology\n   https://aclanthology.org/2026.eamt-1.56/\n   BlAInded by Fluency: How Idiomatic Machine Translation Outputs Affect Student Post-Editors’ Edit Types - ACL Anthology\n\nValentin Scourneau, Loïc De Faria Pires\n\n---\n\n##### Abstract\n\nThis study explore...\n\n6. Calls for Papers\n   https://eamt2026.org/calls-for-papers\n   Calls for Papers - EAMT 2026\n\nThe European Association for Machine Translation (EAMT) invites everyone interested in machine translation and translation-related tools and resources ― developers, resea...\n\n7. Conference of the European Association for Machine Translation (2026) - ACL Anthology\n   https://aclanthology.org/events/eamt-2026/\n   Conference of the European Association for Machine Translation (2026) - ACL Anthology\n\n---\n\n#### Volumes\n\n- Proceedings of the 26th Annual Conference of the European Association for Machine Translatio...", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [22] ASSISTANT · 2026-09-01 10:29:41 UTC

```
All planned steps are complete. Now writing the output files.
```

### [23] TOOL CALL — Write · 2026-09-01 10:29:41 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_report.md

# Verifying the EAMT 2026 "Smarter Edits" Candidate

## (a) Paper located and how

Two verbatim searches both surface the paper as the top (or co-top) hit:

- Query `"EAMT 2026 post-editing error highlights"` → top hit: *"Smarter edits? Post-editing with error highlights and translation suggestions"* — ACL Anthology `2026.eamt-1.41` (https://aclanthology.org/2026.eamt-1.41/), also arXiv:2605.21135.
- Query `"EAMT 2026 automatic post-editing error span iterative"` → same paper appears at position 4 (ACL Anthology) / 6 (arXiv HTML v2).

Full identity: van Tellingen, Ranka, Žugčić, van der Wal, Camasta, Guerra, Karakanta (Leiden University et al.), *"Smarter edits? Post-editing with error highlights and translation suggestions"*, Proceedings of the 26th Annual Conference of the European Association for Machine Translation (EAMT 2026, Tilburg), Volume 1. arXiv:2605.21135v2 (16 Jun 2026), fetched in full via `https://arxiv.org/html/2605.21135v2`.

A subsequent quick sweep (Step 6, two queries: `"EAMT 2026 iterative repair verification translation"` and `"EAMT 2026 CEGIS translation post-editing"`) turned up no distinct, closer-matching EAMT 2026 paper. The only "iterative" MT-refinement hit returned was *"Iterative Translation Refinement with Large Language Models"* (Chen et al.) — but that is **EAMT 2024**, not 2026, and is a TEaR-family self-refinement paper already covered by the prior artifact (art_QAQK2EUnuaCO). "Smarter edits?" is confirmed as the sole, definitive EAMT 2026 candidate.

## (b) Four-condition design

| Condition | Localization source | Breadth | Correction shown to translator? | Passes / iteration |
|---|---|---|---|---|
| PE (regular) | none | — | no | — |
| H-QE | xCOMET-XXL span detection | narrow (sometimes single characters) | no, highlight only | 1 (QE scoring) |
| H-APE | Levenshtein diff between raw MT and one xTower-Instruct-13B-v0.1 APE output | broader (whole differing spans, not character-level) | no, highlight only | 1 (single xTower generation) |
| S-APE | same spans as H-APE | broader | yes — xTower's replacement text shown in a hover box | 1 (single xTower generation, reused) |

Pipeline (Section 3.2, quoted): "Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE)." → "The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE)." → for H-APE, "We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors, regardless of whether they were marked as an error by xCOMET." For S-APE: "The error spans identified in H-APE were paired to their APE correction."

This is a **single xTower generation pass per sentence**: one xCOMET-XXL scoring pass feeds one xTower correction pass, and both H-APE and S-APE reuse that same one-shot output (H-APE takes only its diff-derived spans; S-APE additionally shows the correction text). There is no re-scoring, re-checking, or repeated xTower call anywhere in the pipeline.

## (c) Classification against the four-way decision rule

**Quoted evidence:**

- *Localization breadth varies across conditions* (confirmed): H-QE spans "sometimes only cover parts of words" and included "highlights that were not easily interpretable, e.g. single characters," motivating the switch to H-APE's diff-derived spans, which "better correspond to human PE edits" (Appendix A AP/AUC results: APE-derived spans score higher against oracle post-edit spans than xCOMET-derived spans in both domains). This is a genuine breadth manipulation — narrow, model-confidence-based spans (H-QE) vs. broader, diff-based spans (H-APE/S-APE).
- *Iteration/re-verification does NOT vary — it is absent from every condition* (confirmed): a full-text regex sweep for `iterat|re-check|re-verif|re-flag|second pass|repeat` (case-insensitive) over the entire paper returns exactly **2 matches**, both statistical noise — "one-way **repeated** measures ANOVA" and "Results of **Repeated** Measures ANOVA" (Section 4.1, Table 8) — referring to the ANOVA design, not to repeated correction attempts. Zero occurrences describe any re-checking, re-flagging, or iterated repair loop, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025).
- xTower is invoked exactly once per sentence to produce the APE output that both H-APE's spans and S-APE's suggestion text are derived from — confirmed by the Methods text quoted above and by the absence of any "second pass" or "N rounds" language anywhere in Sections 3–4 or the Appendix.

**Verdict: "varies only one factor."** The paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) across its H-QE vs. H-APE/S-APE conditions, but iteration/re-verification of a repair is never varied — it is simply **absent from all four conditions**, not held fixed as a controlled second factor. This is the same pattern found in all six candidates verified by art_QAQK2EUnuaCO (TEaR, the two WMT25 submissions, xTower's own paper, SSPO, TranslationCorrect, and the non-MT self-localization paper): none of the seven papers now checked (six prior + this one) independently varies both localization breadth and iteration/re-verification while holding the other fixed.

## (d) Novelty claim: no further narrowing required — plus a second, independent axis of difference

Beyond the breadth/iteration classification, "Smarter edits?" differs from this project's B/D/C1/C2/C protocol on a second, independent axis: it is a **human-translator productivity and UX study** — outcome measures are keystrokes, post-editing time (PET), DA quality ratings, translator satisfaction surveys, and semi-structured interviews (Sections 4.1–4.7) — not an **automated repair-loop study** measuring fix rate, regression rate, or ΔCOMET on LLM-generated repairs applied without a human in the loop. This is worth stating explicitly even though it does not by itself settle the localization/iteration classification: it means the paper is not even attempting the same measurement this project's C1-vs-C2 design makes, on top of not varying iteration at all.

The novelty claim as currently scoped (MT automatic post-editing / scoped span editing, per art_QAQK2EUnuaCO's recommended wording) requires **no further narrowing** from this candidate.

## (e) Final status

**EAMT 2026 lead resolved — no rescoping of the novelty claim required.** The candidate (arXiv:2605.21135 / ACL Anthology 2026.eamt-1.41, "Smarter edits? Post-editing with error highlights and translation suggestions") varies localization breadth (H-QE narrow xCOMET spans vs. H-APE/S-APE broader diff-derived spans) but contains zero occurrences of genuine iteration/re-verification language across its full text, and is additionally a human-PE productivity/UX study rather than an automated repair-loop study. This closes the project's final open literature-search item from art_QAQK2EUnuaCO; across all seven candidates now checked, none separates localization breadth from iteration/re-verification as two independently varied, separately measured factors.
```

### [24] TOOL RESULT — Write · 2026-09-01 10:29:41 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_report.md", "content": "# Verifying the EAMT 2026 \"Smarter Edits\" Candidate\n\n## (a) Paper located and how\n\nTwo verbatim searches both surface the paper as the top (or co-top) hit:\n\n- Query `\"EAMT 2026 post-editing error highlights\"` → top hit: *\"Smarter edits? Post-editing with error highlights and translation suggestions\"* — ACL Anthology `2026.eamt-1.41` (https://aclanthology.org/2026.eamt-1.41/), also arXiv:2605.21135.\n- Query `\"EAMT 2026 automatic post-editing error span iterative\"` → same paper appears at position 4 (ACL Anthology) / 6 (arXiv HTML v2).\n\nFull identity: van Tellingen, Ranka, Žugčić, van der Wal, Camasta, Guerra, Karakanta (Leiden University et al.), *\"Smarter edits? Post-editing with error highlights and translation suggestions\"*, Proceedings of the 26th Annual Conference of the European Association for Machine Translation (EAMT 2026, Tilburg), Volume 1. arXiv:2605.21135v2 (16 Jun 2026), fetched in full via `https://arxiv.org/html/2605.21135v2`.\n\nA subsequent quick sweep (Step 6, two queries: `\"EAMT 2026 iterative repair verification translation\"` and `\"EAMT 2026 CEGIS translation post-editing\"`) turned up no distinct, closer-matching EAMT 2026 paper. The only \"iterative\" MT-refinement hit returned was *\"Iterative Translation Refinement with Large Language Models\"* (Chen et al.) — but that is **EAMT 2024**, not 2026, and is a TEaR-family self-refinement paper already covered by the prior artifact (art_QAQK2EUnuaCO). \"Smarter edits?\" is confirmed as the sole, definitive EAMT 2026 candidate.\n\n## (b) Four-condition design\n\n| Condition | Localization source | Breadth | Correction shown to translator? | Passes / iteration |\n|---|---|---|---|---|\n| PE (regular) | none | — | no | — |\n| H-QE | xCOMET-XXL span detection | narrow (sometimes single characters) | no, highlight only | 1 (QE scoring) |\n| H-APE | Levenshtein diff between raw MT and one xTower-Instruct-13B-v0.1 APE output | broader (whole differing spans, not character-level) | no, highlight only | 1 (single xTower generation) |\n| S-APE | same spans as H-APE | broader | yes — xTower's replacement text shown in a hover box | 1 (single xTower generation, reused) |\n\nPipeline (Section 3.2, quoted): \"Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE).\" → \"The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE).\" → for H-APE, \"We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors, regardless of whether they were marked as an error by xCOMET.\" For S-APE: \"The error spans identified in H-APE were paired to their APE correction.\"\n\nThis is a **single xTower generation pass per sentence**: one xCOMET-XXL scoring pass feeds one xTower correction pass, and both H-APE and S-APE reuse that same one-shot output (H-APE takes only its diff-derived spans; S-APE additionally shows the correction text). There is no re-scoring, re-checking, or repeated xTower call anywhere in the pipeline.\n\n## (c) Classification against the four-way decision rule\n\n**Quoted evidence:**\n\n- *Localization breadth varies across conditions* (confirmed): H-QE spans \"sometimes only cover parts of words\" and included \"highlights that were not easily interpretable, e.g. single characters,\" motivating the switch to H-APE's diff-derived spans, which \"better correspond to human PE edits\" (Appendix A AP/AUC results: APE-derived spans score higher against oracle post-edit spans than xCOMET-derived spans in both domains). This is a genuine breadth manipulation — narrow, model-confidence-based spans (H-QE) vs. broader, diff-based spans (H-APE/S-APE).\n- *Iteration/re-verification does NOT vary — it is absent from every condition* (confirmed): a full-text regex sweep for `iterat|re-check|re-verif|re-flag|second pass|repeat` (case-insensitive) over the entire paper returns exactly **2 matches**, both statistical noise — \"one-way **repeated** measures ANOVA\" and \"Results of **Repeated** Measures ANOVA\" (Section 4.1, Table 8) — referring to the ANOVA design, not to repeated correction attempts. Zero occurrences describe any re-checking, re-flagging, or iterated repair loop, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025).\n- xTower is invoked exactly once per sentence to produce the APE output that both H-APE's spans and S-APE's suggestion text are derived from — confirmed by the Methods text quoted above and by the absence of any \"second pass\" or \"N rounds\" language anywhere in Sections 3–4 or the Appendix.\n\n**Verdict: \"varies only one factor.\"** The paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) across its H-QE vs. H-APE/S-APE conditions, but iteration/re-verification of a repair is never varied — it is simply **absent from all four conditions**, not held fixed as a controlled second factor. This is the same pattern found in all six candidates verified by art_QAQK2EUnuaCO (TEaR, the two WMT25 submissions, xTower's own paper, SSPO, TranslationCorrect, and the non-MT self-localization paper): none of the seven papers now checked (six prior + this one) independently varies both localization breadth and iteration/re-verification while holding the other fixed.\n\n## (d) Novelty claim: no further narrowing required — plus a second, independent axis of difference\n\nBeyond the breadth/iteration classification, \"Smarter edits?\" differs from this project's B/D/C1/C2/C protocol on a second, independent axis: it is a **human-translator productivity and UX study** — outcome measures are keystrokes, post-editing time (PET), DA quality ratings, translator satisfaction surveys, and semi-structured interviews (Sections 4.1–4.7) — not an **automated repair-loop study** measuring fix rate, regression rate, or ΔCOMET on LLM-generated repairs applied without a human in the loop. This is worth stating explicitly even though it does not by itself settle the localization/iteration classification: it means the paper is not even attempting the same measurement this project's C1-vs-C2 design makes, on top of not varying iteration at all.\n\nThe novelty claim as currently scoped (MT automatic post-editing / scoped span editing, per art_QAQK2EUnuaCO's recommended wording) requires **no further narrowing** from this candidate.\n\n## (e) Final status\n\n**EAMT 2026 lead resolved — no rescoping of the novelty claim required.** The candidate (arXiv:2605.21135 / ACL Anthology 2026.eamt-1.41, \"Smarter edits? Post-editing with error highlights and translation suggestions\") varies localization breadth (H-QE narrow xCOMET spans vs. H-APE/S-APE broader diff-derived spans) but contains zero occurrences of genuine iteration/re-verification language across its full text, and is additionally a human-PE productivity/UX study rather than an automated repair-loop study. This closes the project's final open literature-search item from art_QAQK2EUnuaCO; across all seven candidates now checked, none separates localization breadth from iteration/re-verification as two independently varied, separately measured factors.\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [25] TOOL CALL — Write · 2026-09-01 10:30:29 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_out.json

{
  "title": "EAMT 2026 Highlights Paper Does Not Vary Iteration",
  "layman_summary": "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.",
  "summary": "This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.",
  "out_expected_files": {
    "output": "research_out.json"
  },
  "upload_ignore_regexes": [],
  "answer": "The EAMT 2026 candidate flagged as the prior artifact's (art_QAQK2EUnuaCO) sole open item -- 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2) [1][2][3] -- was located via two verbatim searches that both return it as a top hit [4][5], fetched in full [1], and classified with quoted primary-text evidence [1].\n\nThe paper's four post-editing conditions are: (1) regular PE, no assistance; (2) H-QE, error highlights from xCOMET-XXL span detection; (3) H-APE, error highlights obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) S-APE, the H-APE spans paired with the xTower correction text itself shown to the translator [1]. Quoted methods text: 'Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE)... The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE)... We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors' [1]. This confirms xTower is invoked exactly once per sentence -- a single generation pass, with H-APE and S-APE both derived post-hoc from that one output -- not an iterated or checker-guided loop.\n\nA full-text regex sweep of the entire paper for iteration/re-verification language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both 'repeated measures ANOVA' -- a statistical test design, not repeated correction attempts [1]. Zero genuine iteration language exists anywhere in the paper, directly mirroring art_QAQK2EUnuaCO's finding that Sharma (2025) contained zero occurrences of 'iterat' [6].\n\nLocalization breadth DOES vary across conditions, confirmed by quoted text: H-QE spans 'sometimes only cover parts of words' and include 'highlights that were not easily interpretable, e.g. single characters,' while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits in the paper's own AP/AUC overlap analysis (Appendix A) [1].\n\nApplying art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) [6], the verdict is 'varies only one factor': the paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) but never varies iteration/re-verification of a repair -- iteration is absent from every one of the four conditions, not held fixed as a controlled second variable [1]. This is NOT the same as this project's C1-vs-C2 design, which requires BOTH breadth and iteration to be independently varied while holding the other fixed.\n\nA second, independent axis of difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity and user-experience study -- its outcome measures are keystrokes, post-editing time, direct-assessment quality ratings, perceived-usefulness surveys, and semi-structured interviews (Sections 4.1-4.7) [1] -- not an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs applied without a human editor. This means the paper is not even attempting the same measurement this project's protocol makes, independent of and in addition to the localization/iteration finding.\n\nA Step-6 sweep of two additional queries ('EAMT 2026 iterative repair verification translation' and 'EAMT 2026 CEGIS translation post-editing') found no closer or distinct EAMT 2026 candidate that might separate the two factors [7][8]. The only genuinely 'iterative' MT-refinement paper surfaced was 'Iterative Translation Refinement with Large Language Models' (Chen et al.) -- but this is EAMT **2024**, not 2026, and is a TEaR-family self-refinement paper already checked and classified by the prior artifact (art_QAQK2EUnuaCO found TEaR varies iteration count while holding localization/estimation scope fixed -- a one-dimensional finding, not a factor-separating design) [6][7].\n\nCONCLUSION: This closes the project's final open literature-search item. Across all seven candidates now checked (the prior artifact's six -- TEaR, two WMT25 QE-informed correction systems, xTower's own paper, SSPO, TranslationCorrect, and a non-MT self-localization paper -- plus this EAMT 2026 candidate), none independently varies both localization breadth and iteration/re-verification of a repair as two separately measured factors while holding the other fixed. The project's novelty claim, scoped specifically to MT automatic post-editing / scoped span editing (per art_QAQK2EUnuaCO's recommended wording, rather than self-correction research broadly) [6], requires NO further narrowing based on this candidate. Confidence is high: the classification rests on quoted primary-text evidence from a full fetch of the paper (not abstract-only reading), a complete regex sweep of the entire document text for iteration language (2/2 matches independently confirmed as statistical, not methodological), and a targeted secondary search that found no alternative candidate.",
  "sources": [
    {
      "index": 1,
      "url": "https://arxiv.org/html/2605.21135v2",
      "title": "Smarter edits? Post-editing with error highlights and translation suggestions (arXiv HTML v2)",
      "summary": "Full paper text fetched and fetch_grep'd. Source of all quoted methods evidence: the four-condition design (PE/H-QE/H-APE/S-APE), the single xTower-Instruct-13B-v0.1 correction pass per sentence, the Levenshtein-diff span derivation, the zero genuine iteration-language finding (2/2 regex matches were 'repeated measures ANOVA'), and the human-productivity/UX outcome measures (keystrokes, PET, DA ratings, interviews)."
    },
    {
      "index": 2,
      "url": "https://aclanthology.org/2026.eamt-1.41/",
      "title": "Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology",
      "summary": "ACL Anthology camera-ready listing confirming venue (EAMT 2026, 26th Annual Conference of the European Association for Machine Translation, Tilburg, Volume 1) and authorship (van Tellingen et al.)."
    },
    {
      "index": 3,
      "url": "https://arxiv.org/abs/2605.21135",
      "title": "[2605.21135] Smarter edits? Post-editing with error highlights and translation suggestions",
      "summary": "arXiv abstract page confirming the paper's identity and publication metadata (16 Jun 2026)."
    },
    {
      "index": 4,
      "url": "https://www.google.com (search: 'EAMT 2026 post-editing error highlights')",
      "title": "Search query 1 results",
      "summary": "General-mode search returning the target paper as the #1 result (ACL Anthology) and #3/#4 (arXiv abs/HTML) -- used as 'located via' evidence per art_QAQK2EUnuaCO's per-query logging convention."
    },
    {
      "index": 5,
      "url": "https://www.google.com (search: 'EAMT 2026 automatic post-editing error span iterative')",
      "title": "Search query 2 results",
      "summary": "General-mode search returning the target paper at positions #4 (ACL Anthology) and #6 (arXiv HTML v2), confirming the candidate independently of query 1's phrasing."
    },
    {
      "index": 6,
      "url": "art_QAQK2EUnuaCO (workspace dependency, iter_4/gen_art/gen_art_research_1/research_out.json)",
      "title": "No Prior Work Separates MT Repair Localization from Iteration",
      "summary": "Prior artifact whose exact four-way decision rule and six verified candidates (TEaR, two WMT25 submissions, xTower, SSPO, TranslationCorrect, non-MT self-localization) this artifact applies to and cross-references; source of the recommended novelty-claim wording (MT automatic post-editing / scoped span editing) and the 'zero iterat occurrences' precedent from Sharma (2025)."
    },
    {
      "index": 7,
      "url": "https://www.google.com (search: 'EAMT 2026 iterative repair verification translation')",
      "title": "Step 6 sweep query 1 results",
      "summary": "No closer or distinct EAMT 2026 candidate found; surfaced 'Iterative Translation Refinement with Large Language Models' which is EAMT 2024 (not 2026) and already covered by art_QAQK2EUnuaCO's TEaR classification, plus the target paper itself at position 5."
    },
    {
      "index": 8,
      "url": "https://www.google.com (search: 'EAMT 2026 CEGIS translation post-editing')",
      "title": "Step 6 sweep query 2 results",
      "summary": "No CEGIS-related or distinct iterative-repair EAMT 2026 paper found; confirms 'Smarter edits?' as the only relevant EAMT 2026 candidate for this topic."
    }
  ],
  "follow_up_questions": [
    "The paper's own SmartPE interface and data/code are open-sourced (github.com/fatalinha/smarter-edits, github.com/fatalinha/SmartPE) -- would this project's automated repair-loop protocol benefit from adapting SmartPE's human-annotation interface for a human-evaluation arm, even though the current project measures automated fix rate rather than human productivity?",
    "art_QAQK2EUnuaCO flagged that ACL-Anthology-native search would likely surface more candidates than the free OpenAlex/Crossref scholarly backend used across both artifacts -- should a follow-up literature pass specifically query ACL Anthology's own search interface for MT repair-localization papers before the project's Related Work section is finalized, given that this artifact's own EAMT 2026 lead was found only via general web search, not scholarly-mode search?",
    "Should the project's Related Work section explicitly cite this artifact and art_QAQK2EUnuaCO together as a paired closing statement (six-candidate sweep plus this seventh, final candidate), presenting the novelty claim as resting on seven independently verified negatives rather than presenting them as two separate literature-search efforts?"
  ]
}
```

### [26] TOOL RESULT — Write · 2026-09-01 10:30:29 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_out.json", "content": "{\n  \"title\": \"EAMT 2026 Highlights Paper Does Not Vary Iteration\",\n  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",\n  \"summary\": \"This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.\",\n  \"out_expected_files\": {\n    \"output\": \"research_out.json\"\n  },\n  \"upload_ignore_regexes\": [],\n  \"answer\": \"The EAMT 2026 candidate flagged as the prior artifact's (art_QAQK2EUnuaCO) sole open item -- 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2) [1][2][3] -- was located via two verbatim searches that both return it as a top hit [4][5], fetched in full [1], and classified with quoted primary-text evidence [1].\\n\\nThe paper's four post-editing conditions are: (1) regular PE, no assistance; (2) H-QE, error highlights from xCOMET-XXL span detection; (3) H-APE, error highlights obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) S-APE, the H-APE spans paired with the xTower correction text itself shown to the translator [1]. Quoted methods text: 'Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE)... The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE)... We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors' [1]. This confirms xTower is invoked exactly once per sentence -- a single generation pass, with H-APE and S-APE both derived post-hoc from that one output -- not an iterated or checker-guided loop.\\n\\nA full-text regex sweep of the entire paper for iteration/re-verification language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both 'repeated measures ANOVA' -- a statistical test design, not repeated correction attempts [1]. Zero genuine iteration language exists anywhere in the paper, directly mirroring art_QAQK2EUnuaCO's finding that Sharma (2025) contained zero occurrences of 'iterat' [6].\\n\\nLocalization breadth DOES vary across conditions, confirmed by quoted text: H-QE spans 'sometimes only cover parts of words' and include 'highlights that were not easily interpretable, e.g. single characters,' while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits in the paper's own AP/AUC overlap analysis (Appendix A) [1].\\n\\nApplying art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) [6], the verdict is 'varies only one factor': the paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) but never varies iteration/re-verification of a repair -- iteration is absent from every one of the four conditions, not held fixed as a controlled second variable [1]. This is NOT the same as this project's C1-vs-C2 design, which requires BOTH breadth and iteration to be independently varied while holding the other fixed.\\n\\nA second, independent axis of difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity and user-experience study -- its outcome measures are keystrokes, post-editing time, direct-assessment quality ratings, perceived-usefulness surveys, and semi-structured interviews (Sections 4.1-4.7) [1] -- not an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs applied without a human editor. This means the paper is not even attempting the same measurement this project's protocol makes, independent of and in addition to the localization/iteration finding.\\n\\nA Step-6 sweep of two additional queries ('EAMT 2026 iterative repair verification translation' and 'EAMT 2026 CEGIS translation post-editing') found no closer or distinct EAMT 2026 candidate that might separate the two factors [7][8]. The only genuinely 'iterative' MT-refinement paper surfaced was 'Iterative Translation Refinement with Large Language Models' (Chen et al.) -- but this is EAMT **2024**, not 2026, and is a TEaR-family self-refinement paper already checked and classified by the prior artifact (art_QAQK2EUnuaCO found TEaR varies iteration count while holding localization/estimation scope fixed -- a one-dimensional finding, not a factor-separating design) [6][7].\\n\\nCONCLUSION: This closes the project's final open literature-search item. Across all seven candidates now checked (the prior artifact's six -- TEaR, two WMT25 QE-informed correction systems, xTower's own paper, SSPO, TranslationCorrect, and a non-MT self-localization paper -- plus this EAMT 2026 candidate), none independently varies both localization breadth and iteration/re-verification of a repair as two separately measured factors while holding the other fixed. The project's novelty claim, scoped specifically to MT automatic post-editing / scoped span editing (per art_QAQK2EUnuaCO's recommended wording, rather than self-correction research broadly) [6], requires NO further narrowing based on this candidate. Confidence is high: the classification rests on quoted primary-text evidence from a full fetch of the paper (not abstract-only reading), a complete regex sweep of the entire document text for iteration language (2/2 matches independently confirmed as statistical, not methodological), and a targeted secondary search that found no alternative candidate.\",\n  \"sources\": [\n    {\n      \"index\": 1,\n      \"url\": \"https://arxiv.org/html/2605.21135v2\",\n      \"title\": \"Smarter edits? Post-editing with error highlights and translation suggestions (arXiv HTML v2)\",\n      \"summary\": \"Full paper text fetched and fetch_grep'd. Source of all quoted methods evidence: the four-condition design (PE/H-QE/H-APE/S-APE), the single xTower-Instruct-13B-v0.1 correction pass per sentence, the Levenshtein-diff span derivation, the zero genuine iteration-language finding (2/2 regex matches were 'repeated measures ANOVA'), and the human-productivity/UX outcome measures (keystrokes, PET, DA ratings, interviews).\"\n    },\n    {\n      \"index\": 2,\n      \"url\": \"https://aclanthology.org/2026.eamt-1.41/\",\n      \"title\": \"Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\",\n      \"summary\": \"ACL Anthology camera-ready listing confirming venue (EAMT 2026, 26th Annual Conference of the European Association for Machine Translation, Tilburg, Volume 1) and authorship (van Tellingen et al.).\"\n    },\n    {\n      \"index\": 3,\n      \"url\": \"https://arxiv.org/abs/2605.21135\",\n      \"title\": \"[2605.21135] Smarter edits? Post-editing with error highlights and translation suggestions\",\n      \"summary\": \"arXiv abstract page confirming the paper's identity and publication metadata (16 Jun 2026).\"\n    },\n    {\n      \"index\": 4,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 post-editing error highlights')\",\n      \"title\": \"Search query 1 results\",\n      \"summary\": \"General-mode search returning the target paper as the #1 result (ACL Anthology) and #3/#4 (arXiv abs/HTML) -- used as 'located via' evidence per art_QAQK2EUnuaCO's per-query logging convention.\"\n    },\n    {\n      \"index\": 5,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 automatic post-editing error span iterative')\",\n      \"title\": \"Search query 2 results\",\n      \"summary\": \"General-mode search returning the target paper at positions #4 (ACL Anthology) and #6 (arXiv HTML v2), confirming the candidate independently of query 1's phrasing.\"\n    },\n    {\n      \"index\": 6,\n      \"url\": \"art_QAQK2EUnuaCO (workspace dependency, iter_4/gen_art/gen_art_research_1/research_out.json)\",\n      \"title\": \"No Prior Work Separates MT Repair Localization from Iteration\",\n      \"summary\": \"Prior artifact whose exact four-way decision rule and six verified candidates (TEaR, two WMT25 submissions, xTower, SSPO, TranslationCorrect, non-MT self-localization) this artifact applies to and cross-references; source of the recommended novelty-claim wording (MT automatic post-editing / scoped span editing) and the 'zero iterat occurrences' precedent from Sharma (2025).\"\n    },\n    {\n      \"index\": 7,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 iterative repair verification translation')\",\n      \"title\": \"Step 6 sweep query 1 results\",\n      \"summary\": \"No closer or distinct EAMT 2026 candidate found; surfaced 'Iterative Translation Refinement with Large Language Models' which is EAMT 2024 (not 2026) and already covered by art_QAQK2EUnuaCO's TEaR classification, plus the target paper itself at position 5.\"\n    },\n    {\n      \"index\": 8,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 CEGIS translation post-editing')\",\n      \"title\": \"Step 6 sweep query 2 results\",\n      \"summary\": \"No CEGIS-related or distinct iterative-repair EAMT 2026 paper found; confirms 'Smarter edits?' as the only relevant EAMT 2026 candidate for this topic.\"\n    }\n  ],\n  \"follow_up_questions\": [\n    \"The paper's own SmartPE interface and data/code are open-sourced (github.com/fatalinha/smarter-edits, github.com/fatalinha/SmartPE) -- would this project's automated repair-loop protocol benefit from adapting SmartPE's human-annotation interface for a human-evaluation arm, even though the current project measures automated fix rate rather than human productivity?\",\n    \"art_QAQK2EUnuaCO flagged that ACL-Anthology-native search would likely surface more candidates than the free OpenAlex/Crossref scholarly backend used across both artifacts -- should a follow-up literature pass specifically query ACL Anthology's own search interface for MT repair-localization papers before the project's Related Work section is finalized, given that this artifact's own EAMT 2026 lead was found only via general web search, not scholarly-mode search?\",\n    \"Should the project's Related Work section explicitly cite this artifact and art_QAQK2EUnuaCO together as a paired closing statement (six-candidate sweep plus this seventh, final candidate), presenting the novelty claim as resting on seven independently verified negatives rather than presenting them as two separate literature-search efforts?\"\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [27] TOOL CALL — Bash · 2026-09-01 10:30:29 UTC

```
python3 -c "import json; json.load(open('research_out.json')); print('valid json')"
```

### [28] TOOL RESULT — Bash · 2026-09-01 10:30:29 UTC

```
{"stdout": "valid json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [29] TOOL CALL — Bash · 2026-09-01 10:30:33 UTC

```
ls -la && python3 -c "import json; d=json.load(open('research_out.json')); print(list(d.keys()))"
```

### [30] TOOL RESULT — Bash · 2026-09-01 10:30:33 UTC

```
{"stdout": "total 4094\ndrwxr-xr-x 2 root root 1016872 Sep  1 10:30 .\ndrwxr-xr-x 6 root root 3000214 Sep  1 10:26 ..\n-rw-r--r-- 1 root root     736 Sep  1 10:29 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 root root  151001 Sep  1 10:30 .repl_agent.ptylog\n-rw-r--r-- 1 root root   13852 Sep  1 10:30 research_out.json\n-rw-r--r-- 1 root root    7185 Sep  1 10:29 research_report.md\n['title', 'layman_summary', 'summary', 'out_expected_files', 'upload_ignore_regexes', 'answer', 'sources', 'follow_up_questions']", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [31] ASSISTANT · 2026-09-01 10:31:11 UTC

```
Good, cwd is already the workspace. Now write the struct output file.
```

### [32] TOOL CALL — Write · 2026-09-01 10:31:11 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "EAMT 2026 Highlights Paper Does Not Vary Iteration",
  "layman_summary": "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.",
  "summary": "This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.",
  "out_expected_files": {
    "output": "research_out.json"
  },
  "upload_ignore_regexes": [],
  "answer": "The EAMT 2026 candidate flagged as the prior artifact's (art_QAQK2EUnuaCO) sole open item -- 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2) [1][2][3] -- was located via two verbatim searches that both return it as a top hit [4][5], fetched in full [1], and classified with quoted primary-text evidence [1].\n\nThe paper's four post-editing conditions are: (1) regular PE, no assistance; (2) H-QE, error highlights from xCOMET-XXL span detection; (3) H-APE, error highlights obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) S-APE, the H-APE spans paired with the xTower correction text itself shown to the translator [1]. Quoted methods text: 'Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE)... The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE)... We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors' [1]. This confirms xTower is invoked exactly once per sentence -- a single generation pass, with H-APE and S-APE both derived post-hoc from that one output -- not an iterated or checker-guided loop.\n\nA full-text regex sweep of the entire paper for iteration/re-verification language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both 'repeated measures ANOVA' -- a statistical test design, not repeated correction attempts [1]. Zero genuine iteration language exists anywhere in the paper, directly mirroring art_QAQK2EUnuaCO's finding that Sharma (2025) contained zero occurrences of 'iterat' [6].\n\nLocalization breadth DOES vary across conditions, confirmed by quoted text: H-QE spans 'sometimes only cover parts of words' and include 'highlights that were not easily interpretable, e.g. single characters,' while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits in the paper's own AP/AUC overlap analysis (Appendix A) [1].\n\nApplying art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) [6], the verdict is 'varies only one factor': the paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) but never varies iteration/re-verification of a repair -- iteration is absent from every one of the four conditions, not held fixed as a controlled second variable [1]. This is NOT the same as this project's C1-vs-C2 design, which requires BOTH breadth and iteration to be independently varied while holding the other fixed.\n\nA second, independent axis of difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity and user-experience study -- its outcome measures are keystrokes, post-editing time, direct-assessment quality ratings, perceived-usefulness surveys, and semi-structured interviews (Sections 4.1-4.7) [1] -- not an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs applied without a human editor. This means the paper is not even attempting the same measurement this project's protocol makes, independent of and in addition to the localization/iteration finding.\n\nA Step-6 sweep of two additional queries ('EAMT 2026 iterative repair verification translation' and 'EAMT 2026 CEGIS translation post-editing') found no closer or distinct EAMT 2026 candidate that might separate the two factors [7][8]. The only genuinely 'iterative' MT-refinement paper surfaced was 'Iterative Translation Refinement with Large Language Models' (Chen et al.) -- but this is EAMT **2024**, not 2026, and is a TEaR-family self-refinement paper already checked and classified by the prior artifact (art_QAQK2EUnuaCO found TEaR varies iteration count while holding localization/estimation scope fixed -- a one-dimensional finding, not a factor-separating design) [6][7].\n\nCONCLUSION: This closes the project's final open literature-search item. Across all seven candidates now checked (the prior artifact's six -- TEaR, two WMT25 QE-informed correction systems, xTower's own paper, SSPO, TranslationCorrect, and a non-MT self-localization paper -- plus this EAMT 2026 candidate), none independently varies both localization breadth and iteration/re-verification of a repair as two separately measured factors while holding the other fixed. The project's novelty claim, scoped specifically to MT automatic post-editing / scoped span editing (per art_QAQK2EUnuaCO's recommended wording, rather than self-correction research broadly) [6], requires NO further narrowing based on this candidate. Confidence is high: the classification rests on quoted primary-text evidence from a full fetch of the paper (not abstract-only reading), a complete regex sweep of the entire document text for iteration language (2/2 matches independently confirmed as statistical, not methodological), and a targeted secondary search that found no alternative candidate.",
  "sources": [
    {
      "index": 1,
      "url": "https://arxiv.org/html/2605.21135v2",
      "title": "Smarter edits? Post-editing with error highlights and translation suggestions (arXiv HTML v2)",
      "summary": "Full paper text fetched and fetch_grep'd. Source of all quoted methods evidence: the four-condition design (PE/H-QE/H-APE/S-APE), the single xTower-Instruct-13B-v0.1 correction pass per sentence, the Levenshtein-diff span derivation, the zero genuine iteration-language finding (2/2 regex matches were 'repeated measures ANOVA'), and the human-productivity/UX outcome measures (keystrokes, PET, DA ratings, interviews)."
    },
    {
      "index": 2,
      "url": "https://aclanthology.org/2026.eamt-1.41/",
      "title": "Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology",
      "summary": "ACL Anthology camera-ready listing confirming venue (EAMT 2026, 26th Annual Conference of the European Association for Machine Translation, Tilburg, Volume 1) and authorship (van Tellingen et al.)."
    },
    {
      "index": 3,
      "url": "https://arxiv.org/abs/2605.21135",
      "title": "[2605.21135] Smarter edits? Post-editing with error highlights and translation suggestions",
      "summary": "arXiv abstract page confirming the paper's identity and publication metadata (16 Jun 2026)."
    },
    {
      "index": 4,
      "url": "https://www.google.com (search: 'EAMT 2026 post-editing error highlights')",
      "title": "Search query 1 results",
      "summary": "General-mode search returning the target paper as the #1 result (ACL Anthology) and #3/#4 (arXiv abs/HTML) -- used as 'located via' evidence per art_QAQK2EUnuaCO's per-query logging convention."
    },
    {
      "index": 5,
      "url": "https://www.google.com (search: 'EAMT 2026 automatic post-editing error span iterative')",
      "title": "Search query 2 results",
      "summary": "General-mode search returning the target paper at positions #4 (ACL Anthology) and #6 (arXiv HTML v2), confirming the candidate independently of query 1's phrasing."
    },
    {
      "index": 6,
      "url": "art_QAQK2EUnuaCO (workspace dependency, iter_4/gen_art/gen_art_research_1/research_out.json)",
      "title": "No Prior Work Separates MT Repair Localization from Iteration",
      "summary": "Prior artifact whose exact four-way decision rule and six verified candidates (TEaR, two WMT25 submissions, xTower, SSPO, TranslationCorrect, non-MT self-localization) this artifact applies to and cross-references; source of the recommended novelty-claim wording (MT automatic post-editing / scoped span editing) and the 'zero iterat occurrences' precedent from Sharma (2025)."
    },
    {
      "index": 7,
      "url": "https://www.google.com (search: 'EAMT 2026 iterative repair verification translation')",
      "title": "Step 6 sweep query 1 results",
      "summary": "No closer or distinct EAMT 2026 candidate found; surfaced 'Iterative Translation Refinement with Large Language Models' which is EAMT 2024 (not 2026) and already covered by art_QAQK2EUnuaCO's TEaR classification, plus the target paper itself at position 5."
    },
    {
      "index": 8,
      "url": "https://www.google.com (search: 'EAMT 2026 CEGIS translation post-editing')",
      "title": "Step 6 sweep query 2 results",
      "summary": "No CEGIS-related or distinct iterative-repair EAMT 2026 paper found; confirms 'Smarter edits?' as the only relevant EAMT 2026 candidate for this topic."
    }
  ],
  "follow_up_questions": [
    "The paper's own SmartPE interface and data/code are open-sourced (github.com/fatalinha/smarter-edits, github.com/fatalinha/SmartPE) -- would this project's automated repair-loop protocol benefit from adapting SmartPE's human-annotation interface for a human-evaluation arm, even though the current project measures automated fix rate rather than human productivity?",
    "art_QAQK2EUnuaCO flagged that ACL-Anthology-native search would likely surface more candidates than the free OpenAlex/Crossref scholarly backend used across both artifacts -- should a follow-up literature pass specifically query ACL Anthology's own search interface for MT repair-localization papers before the project's Related Work section is finalized, given that this artifact's own EAMT 2026 lead was found only via general web search, not scholarly-mode search?",
    "Should the project's Related Work section explicitly cite this artifact and art_QAQK2EUnuaCO together as a paired closing statement (six-candidate sweep plus this seventh, final candidate), presenting the novelty claim as resting on seven independently verified negatives rather than presenting them as two separate literature-search efforts?"
  ]
}
```

### [33] TOOL RESULT — Write · 2026-09-01 10:31:11 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"EAMT 2026 Highlights Paper Does Not Vary Iteration\",\n  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",\n  \"summary\": \"This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.\",\n  \"out_expected_files\": {\n    \"output\": \"research_out.json\"\n  },\n  \"upload_ignore_regexes\": [],\n  \"answer\": \"The EAMT 2026 candidate flagged as the prior artifact's (art_QAQK2EUnuaCO) sole open item -- 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2) [1][2][3] -- was located via two verbatim searches that both return it as a top hit [4][5], fetched in full [1], and classified with quoted primary-text evidence [1].\\n\\nThe paper's four post-editing conditions are: (1) regular PE, no assistance; (2) H-QE, error highlights from xCOMET-XXL span detection; (3) H-APE, error highlights obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) S-APE, the H-APE spans paired with the xTower correction text itself shown to the translator [1]. Quoted methods text: 'Error spans: xCOMET-XXL was used to automatically identify error spans (H-QE)... The texts and error spans obtained from xCOMET were put into xTower-Instruct-13B-v0.1 to generate error explanations and translation corrections (APE)... We compared the raw MT output and APE'd sentence using Levenshtein distance. The spans that differ between MT and APE were highlighted as errors' [1]. This confirms xTower is invoked exactly once per sentence -- a single generation pass, with H-APE and S-APE both derived post-hoc from that one output -- not an iterated or checker-guided loop.\\n\\nA full-text regex sweep of the entire paper for iteration/re-verification language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both 'repeated measures ANOVA' -- a statistical test design, not repeated correction attempts [1]. Zero genuine iteration language exists anywhere in the paper, directly mirroring art_QAQK2EUnuaCO's finding that Sharma (2025) contained zero occurrences of 'iterat' [6].\\n\\nLocalization breadth DOES vary across conditions, confirmed by quoted text: H-QE spans 'sometimes only cover parts of words' and include 'highlights that were not easily interpretable, e.g. single characters,' while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits in the paper's own AP/AUC overlap analysis (Appendix A) [1].\\n\\nApplying art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) [6], the verdict is 'varies only one factor': the paper varies localization breadth (narrow xCOMET spans vs. broader diff-derived spans) but never varies iteration/re-verification of a repair -- iteration is absent from every one of the four conditions, not held fixed as a controlled second variable [1]. This is NOT the same as this project's C1-vs-C2 design, which requires BOTH breadth and iteration to be independently varied while holding the other fixed.\\n\\nA second, independent axis of difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity and user-experience study -- its outcome measures are keystrokes, post-editing time, direct-assessment quality ratings, perceived-usefulness surveys, and semi-structured interviews (Sections 4.1-4.7) [1] -- not an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs applied without a human editor. This means the paper is not even attempting the same measurement this project's protocol makes, independent of and in addition to the localization/iteration finding.\\n\\nA Step-6 sweep of two additional queries ('EAMT 2026 iterative repair verification translation' and 'EAMT 2026 CEGIS translation post-editing') found no closer or distinct EAMT 2026 candidate that might separate the two factors [7][8]. The only genuinely 'iterative' MT-refinement paper surfaced was 'Iterative Translation Refinement with Large Language Models' (Chen et al.) -- but this is EAMT **2024**, not 2026, and is a TEaR-family self-refinement paper already checked and classified by the prior artifact (art_QAQK2EUnuaCO found TEaR varies iteration count while holding localization/estimation scope fixed -- a one-dimensional finding, not a factor-separating design) [6][7].\\n\\nCONCLUSION: This closes the project's final open literature-search item. Across all seven candidates now checked (the prior artifact's six -- TEaR, two WMT25 QE-informed correction systems, xTower's own paper, SSPO, TranslationCorrect, and a non-MT self-localization paper -- plus this EAMT 2026 candidate), none independently varies both localization breadth and iteration/re-verification of a repair as two separately measured factors while holding the other fixed. The project's novelty claim, scoped specifically to MT automatic post-editing / scoped span editing (per art_QAQK2EUnuaCO's recommended wording, rather than self-correction research broadly) [6], requires NO further narrowing based on this candidate. Confidence is high: the classification rests on quoted primary-text evidence from a full fetch of the paper (not abstract-only reading), a complete regex sweep of the entire document text for iteration language (2/2 matches independently confirmed as statistical, not methodological), and a targeted secondary search that found no alternative candidate.\",\n  \"sources\": [\n    {\n      \"index\": 1,\n      \"url\": \"https://arxiv.org/html/2605.21135v2\",\n      \"title\": \"Smarter edits? Post-editing with error highlights and translation suggestions (arXiv HTML v2)\",\n      \"summary\": \"Full paper text fetched and fetch_grep'd. Source of all quoted methods evidence: the four-condition design (PE/H-QE/H-APE/S-APE), the single xTower-Instruct-13B-v0.1 correction pass per sentence, the Levenshtein-diff span derivation, the zero genuine iteration-language finding (2/2 regex matches were 'repeated measures ANOVA'), and the human-productivity/UX outcome measures (keystrokes, PET, DA ratings, interviews).\"\n    },\n    {\n      \"index\": 2,\n      \"url\": \"https://aclanthology.org/2026.eamt-1.41/\",\n      \"title\": \"Smarter edits? Post-editing with error highlights and translation suggestions - ACL Anthology\",\n      \"summary\": \"ACL Anthology camera-ready listing confirming venue (EAMT 2026, 26th Annual Conference of the European Association for Machine Translation, Tilburg, Volume 1) and authorship (van Tellingen et al.).\"\n    },\n    {\n      \"index\": 3,\n      \"url\": \"https://arxiv.org/abs/2605.21135\",\n      \"title\": \"[2605.21135] Smarter edits? Post-editing with error highlights and translation suggestions\",\n      \"summary\": \"arXiv abstract page confirming the paper's identity and publication metadata (16 Jun 2026).\"\n    },\n    {\n      \"index\": 4,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 post-editing error highlights')\",\n      \"title\": \"Search query 1 results\",\n      \"summary\": \"General-mode search returning the target paper as the #1 result (ACL Anthology) and #3/#4 (arXiv abs/HTML) -- used as 'located via' evidence per art_QAQK2EUnuaCO's per-query logging convention.\"\n    },\n    {\n      \"index\": 5,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 automatic post-editing error span iterative')\",\n      \"title\": \"Search query 2 results\",\n      \"summary\": \"General-mode search returning the target paper at positions #4 (ACL Anthology) and #6 (arXiv HTML v2), confirming the candidate independently of query 1's phrasing.\"\n    },\n    {\n      \"index\": 6,\n      \"url\": \"art_QAQK2EUnuaCO (workspace dependency, iter_4/gen_art/gen_art_research_1/research_out.json)\",\n      \"title\": \"No Prior Work Separates MT Repair Localization from Iteration\",\n      \"summary\": \"Prior artifact whose exact four-way decision rule and six verified candidates (TEaR, two WMT25 submissions, xTower, SSPO, TranslationCorrect, non-MT self-localization) this artifact applies to and cross-references; source of the recommended novelty-claim wording (MT automatic post-editing / scoped span editing) and the 'zero iterat occurrences' precedent from Sharma (2025).\"\n    },\n    {\n      \"index\": 7,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 iterative repair verification translation')\",\n      \"title\": \"Step 6 sweep query 1 results\",\n      \"summary\": \"No closer or distinct EAMT 2026 candidate found; surfaced 'Iterative Translation Refinement with Large Language Models' which is EAMT 2024 (not 2026) and already covered by art_QAQK2EUnuaCO's TEaR classification, plus the target paper itself at position 5.\"\n    },\n    {\n      \"index\": 8,\n      \"url\": \"https://www.google.com (search: 'EAMT 2026 CEGIS translation post-editing')\",\n      \"title\": \"Step 6 sweep query 2 results\",\n      \"summary\": \"No CEGIS-related or distinct iterative-repair EAMT 2026 paper found; confirms 'Smarter edits?' as the only relevant EAMT 2026 candidate for this topic.\"\n    }\n  ],\n  \"follow_up_questions\": [\n    \"The paper's own SmartPE interface and data/code are open-sourced (github.com/fatalinha/smarter-edits, github.com/fatalinha/SmartPE) -- would this project's automated repair-loop protocol benefit from adapting SmartPE's human-annotation interface for a human-evaluation arm, even though the current project measures automated fix rate rather than human productivity?\",\n    \"art_QAQK2EUnuaCO flagged that ACL-Anthology-native search would likely surface more candidates than the free OpenAlex/Crossref scholarly backend used across both artifacts -- should a follow-up literature pass specifically query ACL Anthology's own search interface for MT repair-localization papers before the project's Related Work section is finalized, given that this artifact's own EAMT 2026 lead was found only via general web search, not scholarly-mode search?\",\n    \"Should the project's Related Work section explicitly cite this artifact and art_QAQK2EUnuaCO together as a paired closing statement (six-candidate sweep plus this seventh, final candidate), presenting the novelty claim as resting on seven independently verified negatives rather than presenting them as two separate literature-search efforts?\"\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [34] ASSISTANT · 2026-09-01 10:31:15 UTC

```
Verifying JSON validity as a final check.
```

### [35] TOOL CALL — Bash · 2026-09-01 10:31:15 UTC

```
python3 -c "
import json
d = json.load(open('.terminal_claude_agent_struct_out.json'))
required = ['out_expected_files','answer','sources','follow_up_questions']
for k in required:
    assert k in d, f'missing {k}'
assert 'output' in d['out_expected_files']
print('Schema check OK. Keys:', list(d.keys()))
print('num sources:', len(d['sources']))
"
ls -la /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/
```

### [36] TOOL RESULT — Bash · 2026-09-01 10:31:15 UTC

```
{"stdout": "Schema check OK. Keys: ['title', 'layman_summary', 'summary', 'out_expected_files', 'upload_ignore_regexes', 'answer', 'sources', 'follow_up_questions']\nnum sources: 8\ntotal 4153\ndrwxr-xr-x 2 root root 1022206 Sep  1 10:31 .\ndrwxr-xr-x 6 root root 3000559 Sep  1 10:26 ..\n-rw-r--r-- 1 root root     736 Sep  1 10:29 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 root root  191771 Sep  1 10:31 .repl_agent.ptylog\n-rw-r--r-- 1 root root   13852 Sep  1 10:31 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root   13852 Sep  1 10:30 research_out.json\n-rw-r--r-- 1 root root    7185 Sep  1 10:29 research_report.md", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [37] ASSISTANT · 2026-09-01 10:31:20 UTC

```
Task complete. I fetched and fully verified the EAMT 2026 candidate (arXiv:2605.21135, "Smarter edits?"), applying art_QAQK2EUnuaCO's exact decision rule with quoted evidence:

- **xTower runs once per sentence** (single generation pass, no iterated correction loop)
- **Zero genuine iteration language** in the full text (the only 2 regex hits were "repeated measures ANOVA," statistical noise)
- **Localization breadth does vary** (narrow xCOMET spans vs. broader Levenshtein-diff spans)
- **Verdict: "varies only one factor"** — no iteration axis exists in any of the 4 conditions
- It's also a human-productivity/UX study, not an automated repair-loop study — a second independent difference from this project's protocol
- A quick secondary sweep confirmed no closer/distinct EAMT 2026 paper exists

This closes the project's last open literature item: all 7 candidates checked across both artifacts fail to separate localization breadth from iteration — the novelty claim needs no rescoping. Outputs written to `research_out.json`, `research_report.md`, and `.terminal_claude_agent_struct_out.json`.
```

### [38] SYSTEM-USER prompt · 2026-09-01 10:31:23 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison." is too long (at most 250 characters, got 293)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [39] TOOL CALL — Edit · 2026-09-01 10:31:27 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json
OLD:   "layman_summary": "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.",
NEW:   "layman_summary": "A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.",
```

### [40] TOOL RESULT — Edit · 2026-09-01 10:31:27 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "oldString": "  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",", "newString": "  \"layman_summary\": \"A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.\",", "originalFile": null, "structuredPatch": [{"oldStart": 1, "oldLines": 6, "newStart": 1, "newLines": 6, "lines": [" {", "   \"title\": \"EAMT 2026 Highlights Paper Does Not Vary Iteration\",", "-  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",", "+  \"layman_summary\": \"A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.\",", "   \"summary\": \"This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.\",", "   \"out_expected_files\": {", "     \"output\": \"research_out.json\""]}], "userModified": false, "replaceAll": false}
```

### [41] TOOL CALL — Bash · 2026-09-01 10:31:29 UTC

```
cd /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1
python3 -c "
import json
d = json.load(open('.terminal_claude_agent_struct_out.json'))
print(len(d['layman_summary']), 'chars')
assert 80 <= len(d['layman_summary']) <= 250
print('OK')
"
```

### [42] TOOL RESULT — Bash · 2026-09-01 10:31:29 UTC

```
{"stdout": "185 chars\nOK", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [43] ASSISTANT · 2026-09-01 10:31:33 UTC

```
Also updating `research_out.json` to keep it consistent with the corrected struct output.
```

### [44] TOOL CALL — Edit · 2026-09-01 10:31:33 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_out.json
OLD:   "layman_summary": "We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.",
NEW:   "layman_summary": "A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.",
```

### [45] TOOL RESULT — Edit · 2026-09-01 10:31:33 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_research_1/research_out.json", "oldString": "  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",", "newString": "  \"layman_summary\": \"A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.\",", "originalFile": null, "structuredPatch": [{"oldStart": 1, "oldLines": 6, "newStart": 1, "newLines": 6, "lines": [" {", "   \"title\": \"EAMT 2026 Highlights Paper Does Not Vary Iteration\",", "-  \"layman_summary\": \"We tracked down and read a 2026 machine-translation paper that studies AI-generated error highlights for human editors, and confirmed it changes how broad the highlighted error is but never tests repeating or double-checking a fix -- so it does not overlap with this project's core comparison.\",", "+  \"layman_summary\": \"A 2026 translation-editing paper varies how broad AI error highlights are but never tests repeating or double-checking a fix, so it does not overlap with this project's core comparison.\",", "   \"summary\": \"This artifact closes the single remaining unverified lead flagged by the prior literature-search artifact (art_QAQK2EUnuaCO): the EAMT 2026 paper 'Smarter edits? Post-editing with error highlights and translation suggestions' (van Tellingen et al., ACL Anthology 2026.eamt-1.41, arXiv:2605.21135v2). The paper was located via two verbatim searches (both returning it as a top hit), fetched in full (arXiv HTML v2, 67.5k chars), and classified against art_QAQK2EUnuaCO's exact four-way decision rule (separates the factors / bundles the factors / varies only one factor / out of scope) using fetch_grep for quoted primary-text evidence. The paper studies four post-editing conditions for professional En-Nl translators: (1) regular PE with no assistance; (2) PE + QE-derived highlights (H-QE) from xCOMET-XXL spans; (3) PE + APE-derived highlights (H-APE), spans obtained by Levenshtein-diffing the raw MT output against a single xTower-Instruct-13B-v0.1 auto-post-edited version; (4) PE + APE correction suggestions (S-APE), the H-APE spans plus the xTower replacement text shown to the translator. Quoted methods text confirms xTower is invoked exactly once per sentence -- one xCOMET-XXL scoring pass feeds one xTower correction pass, reused by both H-APE and S-APE -- with no re-scoring or repeated correction call anywhere in the pipeline. A full-text regex sweep for iteration language (iterat|re-check|re-verif|re-flag|second pass|repeat, case-insensitive) returns exactly 2 matches, both referring to 'repeated measures ANOVA' (a statistical test design), not to repeated correction attempts -- zero genuine iteration/re-verification language exists in the paper, mirroring art_QAQK2EUnuaCO's finding for Sharma (2025). Localization breadth DOES vary across conditions: H-QE's xCOMET spans are narrower (sometimes single characters) while H-APE/S-APE's diff-derived spans are broader and score higher against human oracle edits (Appendix A). VERDICT: the paper 'varies only one factor' -- localization breadth via differing span-source models -- with no iteration/re-verification axis present in any of its four conditions; iteration is absent from the whole design, not held fixed as a controlled second variable. A second, independent difference from this project's protocol is also documented: the EAMT paper is a human-translator productivity/UX study (keystrokes, post-editing time, DA quality ratings, satisfaction surveys, interviews) rather than an automated repair-loop study measuring fix rate, regression rate, or delta-COMET on LLM-generated repairs -- it is not attempting the same measurement this project's C1-vs-C2 protocol makes, independent of the localization/iteration finding. A Step-6 sweep (two additional queries) found no closer or distinct EAMT 2026 candidate; the only 'iterative' MT-refinement hit returned was a 2024 (not 2026) TEaR-family paper already covered by the prior artifact. This closes the project's final open literature-search item: across all seven candidates now checked (the prior artifact's six plus this one), none independently varies both localization breadth and iteration/re-verification as two separately measured factors while holding the other fixed -- the project's novelty claim, scoped to MT automatic post-editing / scoped span editing, requires NO further narrowing.\",", "   \"out_expected_files\": {", "     \"output\": \"research_out.json\""]}], "userModified": false, "replaceAll": false}
```

### [46] ASSISTANT · 2026-09-01 10:31:33 UTC

```
Fixed — `layman_summary` is now 185 characters (within the 80–250 limit), and both `.terminal_claude_agent_struct_out.json` and `research_out.json` are updated consistently. All other fields unchanged.
```
