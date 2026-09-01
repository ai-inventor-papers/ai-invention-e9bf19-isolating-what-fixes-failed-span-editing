# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 05:04:37 UTC

```
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
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: WMT25 Translation Error-Correction Data
summary: >-
  Acquire the official WMT25 Task 3 test corpus (source, MT output, QE error spans, human severity/type annotations, COMET)
  across 6 English-target language pairs and 5 domains, and programmatically build a category-labeled injected-error augmentation
  set (named entities, numbers/units/dates, negation polarity, quantifier scope) with a disjoint held-out validation slice
  for later checker precision/recall estimation.
runpod_compute_profile: gpu
ideal_dataset_criteria: |-
  Two components, standardized into one row schema {source_text, target_text, language_pair, domain, qe_flagged_spans, human_error_annotations (type/severity/span), metadata_fold, provenance ('natural'|'injected'), invariant_category (null for natural rows)}:

  (1) NATURAL component: the real WMT25 Task 3 evaluation data — source segments, the specific MT system output that was scored, CometKiwi-derived QE error-span annotations (the actual input signal fed to Task 3 systems, per mteval-subtask.html), and, where available, the human MQM/ESA-style severity+type annotations and post-Task-3-scoring COMET deltas that the findings paper's Table 15 and Padmanabhan (2025) report on. Must cover all 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) and ideally the task's 5 domains, with the official test split of 1,000 segments per pair (6,000 total) as the anchor. Every row must carry enough to let a downstream executor recompute QE-flag precision/recall and fix rates against a human-checkable label, not just a QE score. If the fully-annotated post-task gold file (human severity/type labels, matched to Table 15) is not itself public, the raw test inputs (source, MT output, QE spans) from the official GitHub release ARE public and sufficient to run baseline B/D and the checker conditions; document any gap between 'what was released pre-competition' and 'what the findings paper scored' explicitly per language pair rather than silently treating the two as equivalent, and supplement natural-error density with WMT24 dev material or prior WMT General-MT MQM-annotated test sets (e.g. en-de, en-ru, en-zh, which have multi-year MQM annotation coverage) for any language pair where WMT25's own natural annotated volume is too thin to power the natural-error subset of the eventual B/D/C1/C2/C comparison — label these substituted rows with a source_dataset/provenance field so downstream analysis can report natural-error results per true-source, not blend WMT25-native and substituted rows silently.

  (2) INJECTED component: a programmatically corrupted subset built FROM held-out clean translations (references or high-quality system outputs, disjoint from the rows used for (1)'s experimental pool), each corruption falling into exactly one of the four checkable invariant categories with an explicit, machine-readable ground-truth violation span and category label: (a) named-entity swap — replace a tagged entity (person/org/location/misc, via a multilingual NER pass, e.g. spaCy or HF token-classification models per target language) with a same-type distractor entity drawn from a per-language distractor pool built from other entities seen in the same corpus, so swaps stay plausible; (b) number/unit/date alteration — regex-detect numerals, units, and dates in the target and perturb by a verifiable, reversible amount (e.g. +/-1 to the leading digit, a unit substitution from a fixed conversion table, a date field off-by-one) so the ground truth is exactly the original value; (c) negation-polarity flip — per-language cue-list based insertion/deletion of a negation marker (English not/no/never; Czech ne-; Russian не; Japanese ない/ず; Icelandic ekki; Chinese 不/没; Ukrainian не) at a syntactically valid attachment point; (d) quantifier substitution — swap a closed-class quantifier (all/some/most/none/always/sometimes/never and their per-language equivalents) for a scope-changing counterpart from a fixed list. Each corrupted row keeps the pre-corruption clean text alongside the corrupted text plus {category, original_span, corrupted_span, span_offsets} so a downstream deterministic checker's precision/recall against a KNOWN label is directly computable, and so a human spot-check of a sample can confirm the corruption is unambiguous and detectable (discard/regenerate any corruption a corpus-frequency check flags as already natural-sounding, e.g. a swapped entity that happens to also appear correctly elsewhere in the same sentence).

  Both components must be tagged with metadata_fold in {experimental_pool, checker_validation_heldout} at construction time, with the held-out validation slice (sized for a defensible precision/recall CI at the executor's discretion, roughly 15-20% of rows, natural + injected, stratified by language pair and category) kept strictly disjoint from the pool used for the eventual B/D/C1/C2/C system comparison so the checker's own validation is never contaminated by the rows it will later be run against for scoring. Total combined size should stay well under any per-artifact byte constraints (WMT25 natural test data alone is ~6k rows; injected augmentation should add a comparable few-thousand-row set, not attempt to corrupt the entire corpus) -- prioritize category and language-pair BALANCE over raw volume.
dataset_search_plan: |-
  1) PRIMARY SOURCE (official WMT25 Task 3 release): fetch the combined test set directly from the WMT organizers' GitHub repo `wmt-conference/wmt25-mteval`, specifically `data/testset/wmt25_task3_combined_test_set.tsv` (released 2025-07-24; confirmed via https://www2.statmt.org/wmt25/mteval-subtask.html and cross-checked against the Codabench competition page https://www.codabench.org/competitions/8371/, 'WMT25 Automated Translation Quality Evaluation Systems Task 3'). This file is the actual input Task 3 systems (including Padmanabhan 2025's SURREYPAI) consumed: source, MT system output, CometKiwi QE annotations, per the 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) at 1,000 segments each (6,000 rows total). Parse the TSV header carefully (columns likely include doc id, segment id, source/target language, domain/set id, system id, source segment, MT output, QE span/score fields) and record the exact schema found -- do not assume column names match this plan's terminology, map them explicitly. Check the repo's root for a LICENSE file and any DATA_LICENSE / README data-availability statement; if genuinely absent, treat as research-use-only (standard for WMT shared-task releases) and note this in metadata rather than blocking on it.
  2) GOLD/HUMAN-ANNOTATION LAYER: check the same `wmt-conference/wmt25-mteval` repo (and any `results`/`human-eval` subdirectory it may contain post-shared-task) plus the ACL Anthology page for 2025.wmt-1.24 ('Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems') for a released post-hoc human severity/type annotation file matching Table 15's per-system ΔCOMET numbers, and separately check Padmanabhan (2025)'s own repository (search 'SURREYPAI WMT25 github', the paper is arXiv/ACL-indexed as a WMT25 Task 3 system-description paper) for any processed intermediate data it published (its own severity-tagged spans, its Algorithm 1 heuristic's inputs/outputs) -- this is the most direct source for 'exact spans a real submission acted on.' If a fully gold-labeled file is not public, fall back to using the released QE spans themselves as the localization signal (this is what B/D/C1/C2/C need operationally) and treat any human severity/type layer as a bonus enrichment rather than a hard requirement, documenting the gap explicitly per language pair in the output metadata.
  3) VOLUME/DENSITY FALLBACK for natural-error power: if per-language-pair natural incidence of the four checkable invariant categories in the 1,000-segment WMT25 test set proves too sparse (a real risk the hypothesis itself flags), pull supplementary material from `zouharvi/wmt25-metrics-subtask3` on GitHub (dev data `wmt24-jun19.tsv`, ~70k WMT24-based instances with QE annotations, `wget https://media.githubusercontent.com/media/zouharvi/wmt25-metrics-subtask3/refs/heads/main/data/wmt24-jun19.tsv`) for the overlapping language pairs, and/or prior WMT General-MT MQM-annotated test sets (WMT22/23/24, which have multi-year MQM coverage for en-de/en-ru/en-zh and similar pairs, searchable via the WMT shared-task GitHub orgs and the `mt-metrics-eval` / `wmt-mqm-human-evaluation` repositories) for pairs with thin WMT25-native coverage. Any substituted row must carry a `source_dataset` field naming exactly which release it came from -- never silently merge WMT25-native and substituted rows without a traceable provenance tag.
  4) INJECTED-ERROR CONSTRUCTION (built, not searched-for): from a held-out slice of clean rows (references, or human-quality system outputs, drawn from steps 1 and 3, disjoint from the rows reserved for the eventual experimental comparison), programmatically generate the four corruption categories described in the criteria field, using: a multilingual NER tool for entity swaps (e.g. spaCy's multi-language models or an HF token-classification model per target language -- verify language coverage for all 6 targets, especially Icelandic and Ukrainian which have thinner NLP tooling support, and fall back to a curated proper-noun/number regex list where NER coverage is weak); regex-based numeral/date/unit detectors per language (numerals and dates are largely script-independent to detect, units need a small per-language lexicon); a hand-built negation-cue list per target language (six short lists, one per language, each a handful of common negation markers -- cheap to build and verify manually); and a hand-built quantifier word list per target language. Validate a sample of generated corruptions manually (or via a second independent regex/rule pass) to confirm each is unambiguous and genuinely detectable before finalizing the set, discarding any corruption that collides with an existing natural occurrence of the same word/value elsewhere in the sentence.
  5) STANDARDIZE both components into the unified row schema, assign metadata_fold (train/mini/preview plus the separate checker_validation_heldout slice, stratified by language_pair x category so no language pair or category is entirely absent from either the experimental pool or the validation slice), validate against the aii-json schema tooling, and produce full/mini/preview variants. If any step-1/step-2 file exceeds convenient in-memory handling, process per-language-pair in chunks.
target_num_datasets: 2
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 16 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 8 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 4 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-09-01 05:04:37 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-python · 2026-09-01 05:04:49 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: "Applies this repo's Python conventions to experiment and evaluation scripts: uv-only environment setup (never pip), loguru logging with stdout plus a rotating file sink, @logger.catch(reraise=True) with explicit exception types, pathlib file access, type hints, and a standard main() script skeleton. ALWAYS read before writing or editing any Python script that runs an experiment, evaluation, or data-processing job. Triggers: writing or refactoring a Python script, uv venv, uv pip install, pyproject dependencies, loguru, logging setup, try/except and error handling, pathlib, script structure, Python 3.12. NOT for: parallelism, GPU throughput or hardware sizing (use aii-parallel-computing and aii-use-hardware), scaling long autonomous jobs (use aii-long-running-tasks), splitting oversized output files (use aii-file-size-limit), calling LLMs (use aii-openrouter-llms), or notebooks meant for Colab (use aii-colab)."
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-web-tools · 2026-09-01 05:04:49 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-09-01 05:04:49 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: "Validates JSON files against this repo's experiment-pipeline schemas (exp_sel_data_out, exp_gen_sol_out, exp_eval_sol_out, exp_proof_out) and generates size-optimized full, mini and preview variants of any JSON array file. ALWAYS use before treating a pipeline stage output as finished, whenever a schema or required-property error must be fixed, and whenever a large JSON file needs a small truncated version safe to read. Triggers: JSON schema validation, schema compliance, required property errors, pipeline stage outputs, the exp_*_out format names, mini and preview JSON generation, shrinking a large JSON before inspection. NOT for: discovering or downloading new datasets, which aii-hf-datasets and aii-owid-datasets cover; splitting oversized output files, which aii-file-size-limit covers; plotting JSON data, which aii-data-fig-gen covers; spreadsheet and .csv tabular data, which anthropic-xlsx covers."
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-09-01 05:04:49 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: "Splits an oversized generated output file into numbered parts that each fit a size limit: checks sizes with ls -lh, writes full_data_out_1.json, full_data_out_2.json and so on into a matching directory, deletes the original, repoints the reading code at a sorted glob, and regenerates mini and preview variants per part. ALWAYS run right after a script writes JSON output, and whenever a file is too big to keep, exceeds a stated file size limit, or gets rejected for its size. Triggers: file too large, output exceeds the size limit, oversized or huge JSON, ls -lh size check after generating results, splitting or chunking an output file into parts, output directory instead of one file. NOT for: schema validation or making mini and preview variants of a file already within the limit (use aii-json), or general Python script conventions (use aii-python)."
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-hf-datasets · 2026-09-01 05:04:49 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: "Searches, previews, and downloads machine-learning datasets from the HuggingFace Hub catalogue — configs, splits, features and a loadable flag — saving full, mini and preview JSON files. Use whenever a task needs training data, an evaluation corpus, or a named public benchmark hosted on HuggingFace, and whenever candidate datasets must be discovered, compared and sampled before one is chosen. Triggers: HuggingFace, HF Hub, datasets library, dataset search or discovery, training data, benchmark corpus, parquet shards, configs and splits, dataset card, org/name dataset repo ids. NOT for: country-level global indicator statistics on energy, health, economics or demographics, which aii-owid-datasets covers; validating or reshaping JSON already on disk, which aii-json covers; plotting the numbers, which aii-data-fig-gen covers."
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [8] SYSTEM-USER prompt · 2026-09-01 05:17:24 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: WMT25 Translation Error-Correction Data
summary: >-
  Acquire the official WMT25 Task 3 test corpus (source, MT output, QE error spans, human severity/type annotations, COMET)
  across 6 English-target language pairs and 5 domains, and programmatically build a category-labeled injected-error augmentation
  set (named entities, numbers/units/dates, negation polarity, quantifier scope) with a disjoint held-out validation slice
  for later checker precision/recall estimation.
runpod_compute_profile: gpu
ideal_dataset_criteria: |-
  Two components, standardized into one row schema {source_text, target_text, language_pair, domain, qe_flagged_spans, human_error_annotations (type/severity/span), metadata_fold, provenance ('natural'|'injected'), invariant_category (null for natural rows)}:

  (1) NATURAL component: the real WMT25 Task 3 evaluation data — source segments, the specific MT system output that was scored, CometKiwi-derived QE error-span annotations (the actual input signal fed to Task 3 systems, per mteval-subtask.html), and, where available, the human MQM/ESA-style severity+type annotations and post-Task-3-scoring COMET deltas that the findings paper's Table 15 and Padmanabhan (2025) report on. Must cover all 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) and ideally the task's 5 domains, with the official test split of 1,000 segments per pair (6,000 total) as the anchor. Every row must carry enough to let a downstream executor recompute QE-flag precision/recall and fix rates against a human-checkable label, not just a QE score. If the fully-annotated post-task gold file (human severity/type labels, matched to Table 15) is not itself public, the raw test inputs (source, MT output, QE spans) from the official GitHub release ARE public and sufficient to run baseline B/D and the checker conditions; document any gap between 'what was released pre-competition' and 'what the findings paper scored' explicitly per language pair rather than silently treating the two as equivalent, and supplement natural-error density with WMT24 dev material or prior WMT General-MT MQM-annotated test sets (e.g. en-de, en-ru, en-zh, which have multi-year MQM annotation coverage) for any language pair where WMT25's own natural annotated volume is too thin to power the natural-error subset of the eventual B/D/C1/C2/C comparison — label these substituted rows with a source_dataset/provenance field so downstream analysis can report natural-error results per true-source, not blend WMT25-native and substituted rows silently.

  (2) INJECTED component: a programmatically corrupted subset built FROM held-out clean translations (references or high-quality system outputs, disjoint from the rows used for (1)'s experimental pool), each corruption falling into exactly one of the four checkable invariant categories with an explicit, machine-readable ground-truth violation span and category label: (a) named-entity swap — replace a tagged entity (person/org/location/misc, via a multilingual NER pass, e.g. spaCy or HF token-classification models per target language) with a same-type distractor entity drawn from a per-language distractor pool built from other entities seen in the same corpus, so swaps stay plausible; (b) number/unit/date alteration — regex-detect numerals, units, and dates in the target and perturb by a verifiable, reversible amount (e.g. +/-1 to the leading digit, a unit substitution from a fixed conversion table, a date field off-by-one) so the ground truth is exactly the original value; (c) negation-polarity flip — per-language cue-list based insertion/deletion of a negation marker (English not/no/never; Czech ne-; Russian не; Japanese ない/ず; Icelandic ekki; Chinese 不/没; Ukrainian не) at a syntactically valid attachment point; (d) quantifier substitution — swap a closed-class quantifier (all/some/most/none/always/sometimes/never and their per-language equivalents) for a scope-changing counterpart from a fixed list. Each corrupted row keeps the pre-corruption clean text alongside the corrupted text plus {category, original_span, corrupted_span, span_offsets} so a downstream deterministic checker's precision/recall against a KNOWN label is directly computable, and so a human spot-check of a sample can confirm the corruption is unambiguous and detectable (discard/regenerate any corruption a corpus-frequency check flags as already natural-sounding, e.g. a swapped entity that happens to also appear correctly elsewhere in the same sentence).

  Both components must be tagged with metadata_fold in {experimental_pool, checker_validation_heldout} at construction time, with the held-out validation slice (sized for a defensible precision/recall CI at the executor's discretion, roughly 15-20% of rows, natural + injected, stratified by language pair and category) kept strictly disjoint from the pool used for the eventual B/D/C1/C2/C system comparison so the checker's own validation is never contaminated by the rows it will later be run against for scoring. Total combined size should stay well under any per-artifact byte constraints (WMT25 natural test data alone is ~6k rows; injected augmentation should add a comparable few-thousand-row set, not attempt to corrupt the entire corpus) -- prioritize category and language-pair BALANCE over raw volume.
dataset_search_plan: |-
  1) PRIMARY SOURCE (official WMT25 Task 3 release): fetch the combined test set directly from the WMT organizers' GitHub repo `wmt-conference/wmt25-mteval`, specifically `data/testset/wmt25_task3_combined_test_set.tsv` (released 2025-07-24; confirmed via https://www2.statmt.org/wmt25/mteval-subtask.html and cross-checked against the Codabench competition page https://www.codabench.org/competitions/8371/, 'WMT25 Automated Translation Quality Evaluation Systems Task 3'). This file is the actual input Task 3 systems (including Padmanabhan 2025's SURREYPAI) consumed: source, MT system output, CometKiwi QE annotations, per the 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) at 1,000 segments each (6,000 rows total). Parse the TSV header carefully (columns likely include doc id, segment id, source/target language, domain/set id, system id, source segment, MT output, QE span/score fields) and record the exact schema found -- do not assume column names match this plan's terminology, map them explicitly. Check the repo's root for a LICENSE file and any DATA_LICENSE / README data-availability statement; if genuinely absent, treat as research-use-only (standard for WMT shared-task releases) and note this in metadata rather than blocking on it.
  2) GOLD/HUMAN-ANNOTATION LAYER: check the same `wmt-conference/wmt25-mteval` repo (and any `results`/`human-eval` subdirectory it may contain post-shared-task) plus the ACL Anthology page for 2025.wmt-1.24 ('Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems') for a released post-hoc human severity/type annotation file matching Table 15's per-system ΔCOMET numbers, and separately check Padmanabhan (2025)'s own repository (search 'SURREYPAI WMT25 github', the paper is arXiv/ACL-indexed as a WMT25 Task 3 system-description paper) for any processed intermediate data it published (its own severity-tagged spans, its Algorithm 1 heuristic's inputs/outputs) -- this is the most direct source for 'exact spans a real submission acted on.' If a fully gold-labeled file is not public, fall back to using the released QE spans themselves as the localization signal (this is what B/D/C1/C2/C need operationally) and treat any human severity/type layer as a bonus enrichment rather than a hard requirement, documenting the gap explicitly per language pair in the output metadata.
  3) VOLUME/DENSITY FALLBACK for natural-error power: if per-language-pair natural incidence of the four checkable invariant categories in the 1,000-segment WMT25 test set proves too sparse (a real risk the hypothesis itself flags), pull supplementary material from `zouharvi/wmt25-metrics-subtask3` on GitHub (dev data `wmt24-jun19.tsv`, ~70k WMT24-based instances with QE annotations, `wget https://media.githubusercontent.com/media/zouharvi/wmt25-metrics-subtask3/refs/heads/main/data/wmt24-jun19.tsv`) for the overlapping language pairs, and/or prior WMT General-MT MQM-annotated test sets (WMT22/23/24, which have multi-year MQM coverage for en-de/en-ru/en-zh and similar pairs, searchable via the WMT shared-task GitHub orgs and the `mt-metrics-eval` / `wmt-mqm-human-evaluation` repositories) for pairs with thin WMT25-native coverage. Any substituted row must carry a `source_dataset` field naming exactly which release it came from -- never silently merge WMT25-native and substituted rows without a traceable provenance tag.
  4) INJECTED-ERROR CONSTRUCTION (built, not searched-for): from a held-out slice of clean rows (references, or human-quality system outputs, drawn from steps 1 and 3, disjoint from the rows reserved for the eventual experimental comparison), programmatically generate the four corruption categories described in the criteria field, using: a multilingual NER tool for entity swaps (e.g. spaCy's multi-language models or an HF token-classification model per target language -- verify language coverage for all 6 targets, especially Icelandic and Ukrainian which have thinner NLP tooling support, and fall back to a curated proper-noun/number regex list where NER coverage is weak); regex-based numeral/date/unit detectors per language (numerals and dates are largely script-independent to detect, units need a small per-language lexicon); a hand-built negation-cue list per target language (six short lists, one per language, each a handful of common negation markers -- cheap to build and verify manually); and a hand-built quantifier word list per target language. Validate a sample of generated corruptions manually (or via a second independent regex/rule pass) to confirm each is unambiguous and genuinely detectable before finalizing the set, discarding any corruption that collides with an existing natural occurrence of the same word/value elsewhere in the sentence.
  5) STANDARDIZE both components into the unified row schema, assign metadata_fold (train/mini/preview plus the separate checker_validation_heldout slice, stratified by language_pair x category so no language pair or category is entirely absent from either the experimental pool or the validation slice), validate against the aii-json schema tooling, and produce full/mini/preview variants. If any step-1/step-2 file exceeds convenient in-memory handling, process per-language-pair in chunks.
target_num_datasets: 2
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 4 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 2 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [9] SYSTEM-USER prompt · 2026-09-01 05:21:38 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: WMT25 Translation Error-Correction Data
summary: >-
  Acquire the official WMT25 Task 3 test corpus (source, MT output, QE error spans, human severity/type annotations, COMET)
  across 6 English-target language pairs and 5 domains, and programmatically build a category-labeled injected-error augmentation
  set (named entities, numbers/units/dates, negation polarity, quantifier scope) with a disjoint held-out validation slice
  for later checker precision/recall estimation.
runpod_compute_profile: gpu
ideal_dataset_criteria: |-
  Two components, standardized into one row schema {source_text, target_text, language_pair, domain, qe_flagged_spans, human_error_annotations (type/severity/span), metadata_fold, provenance ('natural'|'injected'), invariant_category (null for natural rows)}:

  (1) NATURAL component: the real WMT25 Task 3 evaluation data — source segments, the specific MT system output that was scored, CometKiwi-derived QE error-span annotations (the actual input signal fed to Task 3 systems, per mteval-subtask.html), and, where available, the human MQM/ESA-style severity+type annotations and post-Task-3-scoring COMET deltas that the findings paper's Table 15 and Padmanabhan (2025) report on. Must cover all 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) and ideally the task's 5 domains, with the official test split of 1,000 segments per pair (6,000 total) as the anchor. Every row must carry enough to let a downstream executor recompute QE-flag precision/recall and fix rates against a human-checkable label, not just a QE score. If the fully-annotated post-task gold file (human severity/type labels, matched to Table 15) is not itself public, the raw test inputs (source, MT output, QE spans) from the official GitHub release ARE public and sufficient to run baseline B/D and the checker conditions; document any gap between 'what was released pre-competition' and 'what the findings paper scored' explicitly per language pair rather than silently treating the two as equivalent, and supplement natural-error density with WMT24 dev material or prior WMT General-MT MQM-annotated test sets (e.g. en-de, en-ru, en-zh, which have multi-year MQM annotation coverage) for any language pair where WMT25's own natural annotated volume is too thin to power the natural-error subset of the eventual B/D/C1/C2/C comparison — label these substituted rows with a source_dataset/provenance field so downstream analysis can report natural-error results per true-source, not blend WMT25-native and substituted rows silently.

  (2) INJECTED component: a programmatically corrupted subset built FROM held-out clean translations (references or high-quality system outputs, disjoint from the rows used for (1)'s experimental pool), each corruption falling into exactly one of the four checkable invariant categories with an explicit, machine-readable ground-truth violation span and category label: (a) named-entity swap — replace a tagged entity (person/org/location/misc, via a multilingual NER pass, e.g. spaCy or HF token-classification models per target language) with a same-type distractor entity drawn from a per-language distractor pool built from other entities seen in the same corpus, so swaps stay plausible; (b) number/unit/date alteration — regex-detect numerals, units, and dates in the target and perturb by a verifiable, reversible amount (e.g. +/-1 to the leading digit, a unit substitution from a fixed conversion table, a date field off-by-one) so the ground truth is exactly the original value; (c) negation-polarity flip — per-language cue-list based insertion/deletion of a negation marker (English not/no/never; Czech ne-; Russian не; Japanese ない/ず; Icelandic ekki; Chinese 不/没; Ukrainian не) at a syntactically valid attachment point; (d) quantifier substitution — swap a closed-class quantifier (all/some/most/none/always/sometimes/never and their per-language equivalents) for a scope-changing counterpart from a fixed list. Each corrupted row keeps the pre-corruption clean text alongside the corrupted text plus {category, original_span, corrupted_span, span_offsets} so a downstream deterministic checker's precision/recall against a KNOWN label is directly computable, and so a human spot-check of a sample can confirm the corruption is unambiguous and detectable (discard/regenerate any corruption a corpus-frequency check flags as already natural-sounding, e.g. a swapped entity that happens to also appear correctly elsewhere in the same sentence).

  Both components must be tagged with metadata_fold in {experimental_pool, checker_validation_heldout} at construction time, with the held-out validation slice (sized for a defensible precision/recall CI at the executor's discretion, roughly 15-20% of rows, natural + injected, stratified by language pair and category) kept strictly disjoint from the pool used for the eventual B/D/C1/C2/C system comparison so the checker's own validation is never contaminated by the rows it will later be run against for scoring. Total combined size should stay well under any per-artifact byte constraints (WMT25 natural test data alone is ~6k rows; injected augmentation should add a comparable few-thousand-row set, not attempt to corrupt the entire corpus) -- prioritize category and language-pair BALANCE over raw volume.
dataset_search_plan: |-
  1) PRIMARY SOURCE (official WMT25 Task 3 release): fetch the combined test set directly from the WMT organizers' GitHub repo `wmt-conference/wmt25-mteval`, specifically `data/testset/wmt25_task3_combined_test_set.tsv` (released 2025-07-24; confirmed via https://www2.statmt.org/wmt25/mteval-subtask.html and cross-checked against the Codabench competition page https://www.codabench.org/competitions/8371/, 'WMT25 Automated Translation Quality Evaluation Systems Task 3'). This file is the actual input Task 3 systems (including Padmanabhan 2025's SURREYPAI) consumed: source, MT system output, CometKiwi QE annotations, per the 6 language pairs (En->Zh, Cs, Ja, Is, Ru, Uk) at 1,000 segments each (6,000 rows total). Parse the TSV header carefully (columns likely include doc id, segment id, source/target language, domain/set id, system id, source segment, MT output, QE span/score fields) and record the exact schema found -- do not assume column names match this plan's terminology, map them explicitly. Check the repo's root for a LICENSE file and any DATA_LICENSE / README data-availability statement; if genuinely absent, treat as research-use-only (standard for WMT shared-task releases) and note this in metadata rather than blocking on it.
  2) GOLD/HUMAN-ANNOTATION LAYER: check the same `wmt-conference/wmt25-mteval` repo (and any `results`/`human-eval` subdirectory it may contain post-shared-task) plus the ACL Anthology page for 2025.wmt-1.24 ('Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems') for a released post-hoc human severity/type annotation file matching Table 15's per-system ΔCOMET numbers, and separately check Padmanabhan (2025)'s own repository (search 'SURREYPAI WMT25 github', the paper is arXiv/ACL-indexed as a WMT25 Task 3 system-description paper) for any processed intermediate data it published (its own severity-tagged spans, its Algorithm 1 heuristic's inputs/outputs) -- this is the most direct source for 'exact spans a real submission acted on.' If a fully gold-labeled file is not public, fall back to using the released QE spans themselves as the localization signal (this is what B/D/C1/C2/C need operationally) and treat any human severity/type layer as a bonus enrichment rather than a hard requirement, documenting the gap explicitly per language pair in the output metadata.
  3) VOLUME/DENSITY FALLBACK for natural-error power: if per-language-pair natural incidence of the four checkable invariant categories in the 1,000-segment WMT25 test set proves too sparse (a real risk the hypothesis itself flags), pull supplementary material from `zouharvi/wmt25-metrics-subtask3` on GitHub (dev data `wmt24-jun19.tsv`, ~70k WMT24-based instances with QE annotations, `wget https://media.githubusercontent.com/media/zouharvi/wmt25-metrics-subtask3/refs/heads/main/data/wmt24-jun19.tsv`) for the overlapping language pairs, and/or prior WMT General-MT MQM-annotated test sets (WMT22/23/24, which have multi-year MQM coverage for en-de/en-ru/en-zh and similar pairs, searchable via the WMT shared-task GitHub orgs and the `mt-metrics-eval` / `wmt-mqm-human-evaluation` repositories) for pairs with thin WMT25-native coverage. Any substituted row must carry a `source_dataset` field naming exactly which release it came from -- never silently merge WMT25-native and substituted rows without a traceable provenance tag.
  4) INJECTED-ERROR CONSTRUCTION (built, not searched-for): from a held-out slice of clean rows (references, or human-quality system outputs, drawn from steps 1 and 3, disjoint from the rows reserved for the eventual experimental comparison), programmatically generate the four corruption categories described in the criteria field, using: a multilingual NER tool for entity swaps (e.g. spaCy's multi-language models or an HF token-classification model per target language -- verify language coverage for all 6 targets, especially Icelandic and Ukrainian which have thinner NLP tooling support, and fall back to a curated proper-noun/number regex list where NER coverage is weak); regex-based numeral/date/unit detectors per language (numerals and dates are largely script-independent to detect, units need a small per-language lexicon); a hand-built negation-cue list per target language (six short lists, one per language, each a handful of common negation markers -- cheap to build and verify manually); and a hand-built quantifier word list per target language. Validate a sample of generated corruptions manually (or via a second independent regex/rule pass) to confirm each is unambiguous and genuinely detectable before finalizing the set, discarding any corruption that collides with an existing natural occurrence of the same word/value elsewhere in the sentence.
  5) STANDARDIZE both components into the unified row schema, assign metadata_fold (train/mini/preview plus the separate checker_validation_heldout slice, stratified by language_pair x category so no language pair or category is entirely absent from either the experimental pool or the validation slice), validate against the aii-json schema tooling, and produce full/mini/preview variants. If any step-1/step-2 file exceeds convenient in-memory handling, process per-language-pair in chunks.
target_num_datasets: 2
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 2 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
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
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````
