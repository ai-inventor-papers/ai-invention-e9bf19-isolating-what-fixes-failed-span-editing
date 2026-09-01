# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 09:23:30 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_research_1/results/out.json`
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

<artifact_plan>
id: gen_plan_research_1_idx3
type: research
title: Search for prior work separating MT repair localization from iteration
summary: >-
  Targeted literature search to determine whether any existing work independently varies two mechanisms this project's protocol
  separates -- how broadly a machine-translation repair localizes errors (one QE-flagged span vs. every detected content-invariant
  violation) versus whether the repair is iteratively re-verified and re-repaired to a checker-defined certificate vs. applied
  once -- as two orthogonal, separately-measured factors. The result either backs the paper's 'first controlled evidence separating
  localization breadth from iteration' claim with a logged, reproducible negative search, or surfaces a closer prior ablation
  that the current related-work section (Deoghare 2023/2025, xTower, Self-Refine, CEGIS, LaSEr-Edit) does not cover, in which
  case the paper's novelty claim must be scoped down and the paper cites the closer work explicitly.
runpod_compute_profile: cpu_light
question: >-
  Does any published system or ablation study hold 'breadth of error localization' (narrow QE-flagged span vs. broadened invariant/error
  detection) and 'iteration/re-verification of a repair' apart as two independently varied, separately measured factors in
  machine-translation automatic post-editing / scoped span editing -- the way this project's C1 (broad, single-pass) vs. C2
  (narrow, iterated) conditions do -- or does every candidate bundle the two (broaden localization AND iterate together, or
  vary only one while holding the other fixed at a single, non-varied setting)?
research_plan: |-
  GOAL: Determine, via a specifically-worded and logged literature search (not a repeat of the existing broad MT/APE survey), whether any prior work varies error-localization breadth and repair iteration as two separate, independently measured factors in machine-translation automatic post-editing or scoped span editing. Produce a clear verdict with exact search terms, exact candidates checked, and exact reasons each was ruled in or out.

  STEP 0 -- Reuse-not-repeat check (5 min): Before searching, re-read this project's own related_works list (Padmanabhan 2025, WMT25 findings paper, Deoghare et al. 2023, Deoghare et al. 2025, LaSEr-Edit, roundtrip-verification autoformalization, CEGIS) so the search below is additive, not duplicative. Do not re-search these six directly; instead search terms specifically chosen NOT to be in that list.

  STEP 1 -- Primary targeted searches (general + scholarly mode, run in parallel where independent). Use aii-web-tools search with mode=scholarly for citation-grounded results and mode=general as a complement (Google Scholar / arXiv often index papers general web search misses, and vice versa). Exact query strings to run, verbatim, and log each one in the final report even if it returns nothing useful:
    1. "iterative QE-guided post-editing machine translation" (both modes)
    2. "checker-in-the-loop machine translation repair" (both modes)
    3. "verify-and-repair span editing translation" (both modes)
    4. "iterative constrained decoding machine translation error correction" (both modes)
    5. "localization breadth versus iteration machine translation" (both modes)
    6. "error localization scope ablation automatic post-editing" (general)
    7. "single-pass versus iterative automatic post-editing ablation" (scholarly)
    8. "scoped span repair verification loop translation quality estimation" (general)
    9. "self-refine machine translation iteration ablation number of rounds" (scholarly) -- to check whether any Self-Refine-for-MT ablation varies localization scope alongside iteration count, since round-count ablations are common but scope ablations are not
    10. "WMT25 Task 3 error correction system iterative" and "WMT25 automatic post-editing shared task ablation localization" -- to catch any other Task 3 participant paper beyond Padmanabhan (2025) and the findings paper already read

  STEP 2 -- Specific candidates already surfaced by exploratory searches this planning pass, to fetch and check FIRST since they are the closest hits found so far (do not treat these as the final answer -- verify each by fetching, not by title alone):
    a. Deoghare et al., "Quality-Informed Segment-Level Error Correction Using..." (WMT25 Task 3 submission, https://aclanthology.org/2025.wmt-1.75.pdf) -- a third WMT25 Task 3 team's system not yet checked for a localization-breadth-vs-iteration ablation; fetch in full and fetch_grep for 'iterat', 'ablation', 'span', 'localiz' to see if it varies these two factors independently or only reports one fixed pipeline.
    b. TEaR: "Improving LLM-based Machine Translation with Systematic Self-Refinement" (NAACL 2025 Findings, https://aclanthology.org/2025.findings-naacl.218/ and its earlier arXiv 2402.16379 version "Improving LLM-based Machine Translation with Systematic Self-Correction") -- has an explicit iteration-round ablation; fetch_grep specifically for whether it also varies what fraction of the sentence / how many error spans are located per pass, or whether localization scope is held fixed while only the iteration count varies (if fixed, it does NOT separate the two factors and should be cited as a single-factor iteration study, distinct from this protocol).
    c. "Enhancing Machine Translation with Self-Supervised Preference Data" (SSPO, ACL 2025, https://aclanthology.org/2025.acl-long.1165/) -- trains an iterative error-detector/translator loop; check whether its error-detection stage's scope (span-level vs whole-sentence) is ever varied independently of how many DPO/refinement iterations are run, or whether detection scope and iteration count are coupled by construction.
    d. "Structure Enables Effective Self-Localization of Errors in LLMs" (arXiv 2602.02416) -- check relevance despite not being MT-specific; if it is a general LLM self-correction paper, note explicitly why it is out of scope (no MT translation-quality evaluation) rather than silently dropping it.
    e. xTower's two-stage refinement description surfaced in this planning pass ("first stage corrects major errors via implicit refinement... second stage introduces quality-oriented feedback to identify and revise remaining errors iteratively") sounds closer to a breadth-then-iteration DESIGN than the existing related-work entry credits -- re-fetch the xTower paper (arXiv 2406.19482 / ACL Findings EMNLP 2024) specifically for whether stage 1 vs stage 2 differ in localization scope (implicit/major-error correction vs targeted quality-feedback revision) and whether these two stages are ever run as an ISOLATED ablation (stage 2 alone vs stage 1 alone vs both) with breadth and iteration count reported as separate independent variables, or whether they are always run in sequence as one fixed pipeline (which would NOT count as separating the factors, only as motivating the idea that they might be separable).

  STEP 3 -- For every candidate surfaced in Steps 1-2 that survives a title/abstract screen, fetch the full paper (or fetch_grep the PDF for 'ablat', 'iterat', 'localiz', 'scope', 'span', 'factorial', 'independent' if it is long) and apply this exact decision rule, recorded per-paper in the output:
    - CLASSIFY AS 'separates the factors' only if the paper reports at least two conditions that hold localization scope fixed while varying iteration (or vice versa), with both varied independently at least once each -- i.e., a design with >=3 of the 4 cells {narrow+single, narrow+iterated, broad+single, broad+iterated}, or an explicit statement that iteration count and localization scope were varied as separate ablation axes.
    - CLASSIFY AS 'bundles the factors' if the paper's iteration mechanism inherently re-scopes what it looks at on each pass (e.g., re-running the same detector see more errors each round because errors moved), making breadth and iteration count causally entangled by the method's own design rather than experimentally separated.
    - CLASSIFY AS 'varies only one factor' if the paper ablates iteration count (holding localization/detection scope fixed at one setting) or ablates detection breadth (running a single pass only), but never both together.
    - CLASSIFY AS 'out of scope' if it is not machine translation, not automatic post-editing / scoped span repair, or not an empirical ablation (e.g., a survey, a position paper, or a system description with no ablation table).

  STEP 4 -- Verdict and write-up. Produce research_out.json {answer, sources, follow_up_questions} plus research_report.md structured as:
    1. Exact list of search queries run (Step 1's 10 strings, both modes noted), one line each, with a one-line note on hit quality -- so the paper can cite its own search scope verbatim rather than asserting novelty unconditionally.
    2. A table of every candidate fetched (Steps 1-2), each with: title, venue/year, URL, one-sentence mechanism description, and its Step-3 classification with the specific quoted or paraphrased evidence (e.g., an exact ablation-table description or a quoted sentence) that justifies the classification -- not just the label.
    3. THE VERDICT, stated in one unambiguous sentence: either (a) 'No candidate found across N queries and M fetched papers holds localization breadth and iteration apart as independently varied factors in MT post-editing/scoped editing; the closest are [list, with why each still falls short]' -- supporting the paper's current strong claim -- or (b) 'Paper X (full citation) separates these factors via [exact mechanism]; it differs from this protocol's C1/C2/C design in [specific ways: language pairs, checker type, whether it reports true regression rate, whether it uses a matched repair model, whether the localization axis is content-invariants specifically vs generic QE spans, etc.]' -- in which case state precisely how the paper's novelty claim should be rescoped for the next draft (e.g., from 'first to separate these mechanisms' to 'first to separate these mechanisms specifically for content-invariant checkers with a matched-repair-model design and a true-regression-rate metric').
    4. Do not fabricate a verdict either way. If a search returns ambiguous or paywalled results that could not be resolved by fetch/fetch_grep within the time available, say so explicitly and list those as open items in follow_up_questions rather than guessing their classification.

  BUDGET: Stay near $0 -- this is pure web search/fetch, no OpenRouter LLM calls are required for the search itself (only use OpenRouter, if at all, for a final synthesis pass well under $1). Time budget: roughly 45 min for Steps 1-2 searches/fetches, 45 min for Step 3 classification, 30 min for the Step 4 write-up, leaving slack inside the 3h ceiling for follow-up fetches on ambiguous candidates.
explanation: >-
  The hypothesis's central mechanism claim -- that C2 (narrow localization, iterated repair) and C1 (broad localization, single-pass
  repair) isolate two genuinely different levers, with C2 shown this iteration to trade quality for correctness and C1 to
  trade correctness for quality -- is only a *novel* factorial separation if no prior paper already ran this same 2x1 (or
  2x2) design in MT automatic post-editing / scoped span editing. The current related-work section (APE-with-QE-signal papers
  like Deoghare 2023/2025, xTower's explain-then-correct loop, Self-Refine-style iterative MT refinement, Grid Beam Search
  constrained decoding, and the CEGIS inspiration itself) was assembled without a dedicated adversarial search specifically
  for this cross of terms. Getting this wrong either lets the paper overclaim novelty it does not have (a reviewer will find
  the paper the search missed) or leaves the paper under-defending a genuinely clean contribution because the survey looks
  incomplete. This artifact's sole job is to close that gap with a citable, reproducible search record before the next paper
  draft is written.
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

### [2] HUMAN-USER prompt · 2026-09-01 09:23:30 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-web-tools · 2026-09-01 09:23:34 UTC

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
