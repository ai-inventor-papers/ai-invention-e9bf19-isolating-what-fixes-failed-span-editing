# gen_demo_art_experiment_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_2` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-09-01 11:20:13 UTC

```
model: claude-sonnet-5 | effort: medium | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW
```

### [2] SYSTEM-USER prompt · 2026-09-01 11:20:19 UTC

````
<conversion_philosophy>
**MINIMAL CHANGES — PRESERVE THE ORIGINAL CODE**

The goal is to make the artifact's code READABLE, UNDERSTANDABLE, and RUNNABLE in a short time
to someone reviewing the research, with the option to easily scale parameters back to original
values for a full run (which can take much longer). Think of this as annotating and reformatting,
not refactoring.

**DO:**
- Split the original script into logical notebook cells (imports, setup, processing, results)
- Add markdown cells BETWEEN code cells explaining what each section does and why
- Add inline comments where the logic is non-obvious
- Add a visualization/summary cell at the end showing key outputs
- Fix hardcoded file paths to use the GitHub data loading pattern

**DO NOT:**
- Rewrite functions or change algorithms
- Rename variables or restructure logic
- Add error handling, type hints, or "improvements" that weren't in the original
- Simplify or "clean up" the original code
- Remove any original comments or logic
- Change the computational approach

The reader should recognize the original script when looking at the notebook — it's the
same code, just split into cells with explanatory markdown between sections.
</conversion_philosophy>

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
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<task>
Convert this artifact's Python script into a demo notebook with MINIMAL changes to the original code.
Split into cells, add markdown explanations between sections, add a visualization cell at the end.
Output: mini_demo_data.json + code_demo.ipynb (notebook that loads data from GitHub URL)
</task>

<artifact_info>
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json

URLs won't work yet — files pushed to GitHub AFTER notebook creation.
Use local fallback pattern so notebook works locally (now) and in Colab (after deployment).
</github_repo>

<data_file_sizes>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_file_sizes>

<install_dependencies_pattern>
Follow the aii-colab skill exactly. It has the install cell pattern, pre-installed package list, numpy 2.0 compat shims, and all Colab-specific rules.
</install_dependencies_pattern>

<data_loading_pattern>
`mini_demo_data.json` = curated subset for the demo.
Use this pattern for Colab compatibility (GitHub URL with local fallback):
```python
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")
```
</data_loading_pattern>

<notebook_structure>
--- Setup ---
Cell 1 (markdown): Title, description, what this artifact does.
Cell 2 (code): Install dependencies — follow the aii-colab skill's install cell pattern exactly. Fill in all packages imported by the artifact's code.
Cell 3 (code): Imports — copy original import block as-is, plus any additional imports needed for the notebook (e.g. matplotlib for visualization).
Cell 4 (code): Data loading helper — use the <data_loading_pattern> above.
Cell 5 (code): `data = load_data()`

--- Config ---
Config cell (code): Define ALL tunable parameters (iterations, epochs, n_samples, hidden_size, etc.) as variables at the top of this cell. Start with the ABSOLUTE MINIMUM values — the smallest that produce any output at all (e.g. 1 iteration, 2 samples, smallest array size). These get gradually increased during testing — see TODOs.

--- Processing ---
Remaining cells: One code cell per logical section of the original script. Add a markdown cell BEFORE each code cell. Copy code as closely as possible, with these changes:
  1. Replace file paths to use the loaded `data` variable.
  2. Use the config variables from the config cell (NOT hardcoded values).
  3. Minimal fixes are allowed if something doesn't work in notebook context (e.g. adjusting paths, removing CLI args, fixing imports), but keep changes to the absolute minimum.

--- Results ---
Visualization cell (code): Print key results in a readable table, plot numeric data with matplotlib if appropriate.
</notebook_structure>

<priority>
WORKING > OPTIMIZED. A small-scale demo that runs correctly is the goal. Once the notebook passes with minimum config values, scale up only if time permits — do NOT spend multiple retries chasing larger parameters. If a working version exists, finish and move on.
</priority>

<max_notebook_total_runtime>600s (10 min)</max_notebook_total_runtime>

<test_environment>
To test-run the notebook in a clean environment (simulating Colab), create a disposable `.nb_env` in your workspace:
```bash
/usr/local/bin/python3.12 -m venv .nb_env
.nb_env/bin/pip install -q pip jupyter ipykernel
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb
rm -rf .nb_env
```
The timeout is set to <max_notebook_total_runtime>. The entire notebook must finish within this time.

What happens: the .venv starts empty (just jupyter). When the notebook's install cell runs, `google.colab` is NOT in sys.modules, so ALL packages get installed — non-Colab packages unconditionally, and Colab packages (numpy, pandas, etc.) at Colab's exact versions via the guard block. The result mirrors Colab's environment as closely as possible. If a cell fails, fix the notebook and re-run.
</test_environment>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.


<todos>
TODO 1. Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.
TODO 2. Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.
TODO 3. Create `mini_demo_data.json`: curated subset from at most ONE dataset (no more than 100 diverse examples). CRITICAL: do NOT read/grep full output file — may crash. Use `head -c 5000` or stream first entries with Python to pick examples.
TODO 4. Create `code_demo.ipynb` via NotebookEdit following <notebook_structure>. Set ALL config parameters to ABSOLUTE MINIMUM values — the smallest that produce any output (e.g. 1 iteration, 2 samples, smallest array sizes). Test-run using <test_environment>. Fix all errors until it passes.
TODO 5. GRADUALLY SCALE (but don't overdo it): increase config params step by step (e.g. ~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful — a working small-scale demo beats a failed large-scale one. If full original params fit within <max_notebook_total_runtime> (10% margin), use them. Otherwise keep whatever works and comment out the true original values. Do NOT spend more than 2-3 scaling rounds.
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DemoExpectedFiles": {
      "description": "Expected output files from code demo notebook generation.",
      "properties": {
        "notebook": {
          "default": "",
          "description": "Path to the generated demo notebook. Example: 'code_demo.ipynb'",
          "title": "Notebook",
          "type": "string"
        },
        "mini_data_file": {
          "default": "",
          "description": "Path to the mini demo data JSON (curated subset). Example: 'mini_demo_data.json'",
          "title": "Mini Data File",
          "type": "string"
        }
      },
      "title": "DemoExpectedFiles",
      "type": "object"
    }
  },
  "description": "Dataset/experiment/evaluation \u2192 Jupyter notebook demo.\n\nTitle and summary come from the parent artifact (gen_art step),\nnot from the demo agent. The agent only outputs expected files.",
  "properties": {
    "out_expected_files": {
      "$ref": "#/$defs/DemoExpectedFiles",
      "description": "All output files you created. Must include the demo notebook."
    }
  },
  "required": [],
  "title": "CodeDemo",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-09-01 11:20:19 UTC

```
AI in translation emwrging opportunities
```

### [4] TOOL CALL — Bash · 2026-09-01 11:20:25 UTC

```
ls -la && echo "---source---" && ls -la /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/
```

### [5] TOOL CALL — Skill · 2026-09-01 11:20:25 UTC

```
aii-colab
```

### [6] TOOL RESULT — Bash · 2026-09-01 11:20:25 UTC

```
{"stdout": "total 1977\ndrwxr-xr-x 2 root root 1001872 Sep  1 11:20 .\ndrwxr-xr-x 6 root root 1002415 Sep  1 11:19 ..\n-rw-r--r-- 1 root root   19170 Sep  1 11:20 .repl_agent.ptylog\n---source---\ntotal 21214\ndrwxr-xr-x 4 root   root   3000722 Sep  1 06:35 .\ndrwxr-xr-x 6 root   root   3001557 Sep  1 05:43 ..\n-rw-r--r-- 1 165536 165536  448345 Sep  1 06:17 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 165536 165536 1117253 Sep  1 06:35 .repl_agent.ptylog\n-rw-r--r-- 1 165536 165536    4087 Sep  1 06:35 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 5 165536 165536 3000721 Sep  1 05:48 .venv\n-rw-r--r-- 1 root   root   5007851 Sep  1 06:34 full_method_out.json\ndrwxr-xr-x 2 165536 165536 1003776 Sep  1 06:10 logs\n-rw-rw-rw- 1 165536 165536   38797 Sep  1 06:11 method.py\n-rw-r--r-- 1 165536 165536 5007851 Sep  1 06:34 method_out.json\n-rw-r--r-- 1 root   root     65209 Sep  1 06:34 mini_method_out.json\n-rw-r--r-- 1 root   root     23045 Sep  1 06:34 preview_method_out.json\n-rw-rw-rw- 1 165536 165536     627 Sep  1 06:35 pyproject.toml", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] TOOL CALL — Skill · 2026-09-01 11:20:25 UTC

```
aii-long-running-tasks
```

### [8] TOOL RESULT — Skill · 2026-09-01 11:20:25 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [9] TOOL RESULT — Skill · 2026-09-01 11:20:25 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [10] TOOL CALL — Read · 2026-09-01 11:20:29 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/method.py
```

### [11] TOOL RESULT — Read · 2026-09-01 11:20:29 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/method.py", "content": "#!/usr/bin/env python3\n\"\"\"Condition B fidelity check: faithful masked-fill baseline (Padmanabhan 2025 SURREYPAI-S2).\n\nReproduces the masked-fill baseline (Algorithm 1) on the WMT25 Task 3\nen-zh_CN / en-cs_CZ experimental_pool rows using google/gemma-3-12b-it as the\nforced substitute repair model (Unbabel Tower-P... [truncated, 40714 chars total]
```

### [12] TOOL CALL — Bash · 2026-09-01 11:20:29 UTC

```
head -c 5000 /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/preview_method_out.json
```

### [13] TOOL RESULT — Bash · 2026-09-01 11:20:29 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"condition\": \"B_substitute_model_fidelity_check\",\n    \"repair_model_requested\": \"google/gemma-3-12b-it\",\n    \"repair_model_fallback_chain\": [\n      \"qwen/qwen-2.5-7b-instruct\",\n      \"mistralai/mistral-nemo\",\n      \"meta-llama/llama-3.1-8b-instruct\"\n    ],\n    \"repair_models_actually_used\": {\n      \"google/gemma-3-12b-it\": 1560\n    },\n    \"comet_model_requested\": \"Unbabel/wmt22-cometkiwi-da\",\n    \"comet_model_used\": \"llm_judge_quality_proxy_v1\",\n    \"comet_is_real_comet\": false,\n    \"comet_substitution\": {\n      \"reason\": \"persistent account-wide HF Hub 429 throttling, both COMET checkpoints unobtainable\",\n      \"substitute_scorer\": \"llm_judge_quality_proxy_v1 (openai/gpt-4o-mini, 0-1 adequacy score via OpenRouter)\",\n      \"warning\": \"NOT comparable in scale/calibration to Padmanabhan's ΔCOMET -- see limitations_if_fail\"\n    },\n    \"masking_prompt_provenance\": \"Algorithm 1 severity rule is verbatim from the resource-dossier dependency (Block A, cited to arxiv.org/html/2511.13884). The literal masking PROMPT TEXT was not retrievable in machine-readable form f...\",\n    \"mask_token\": \"__BLANK__\",\n    \"lang_pairs\": [\n      \"en-zh_CN\",\n      \"en-cs_CZ\"\n    ],\n    \"n_rows_per_pair\": {\n      \"en-zh_CN\": 779,\n      \"en-cs_CZ\": 781\n    },\n    \"n_llm_calls\": 1560,\n    \"total_cost_usd\": 0.076003,\n    \"soft_cost_cap_usd\": 6.0,\n    \"hard_cost_cap_usd\": 6.5,\n    \"pooled_mean_delta_comet\": -0.05608974358974359,\n    \"pooled_leakage_rate\": 0.09230769230769231,\n    \"per_pair_results\": {\n      \"en-zh_CN\": {\n        \"n_rows\": 779,\n        \"n_rows_with_spans_flagged\": 779,\n        \"n_rows_masked_by_condition_b\": 779,\n        \"n_llm_calls\": 779,\n        \"mean_delta_comet\": -0.04236200256739409,\n        \"n_scored\": 779,\n        \"leakage_rate\": 0.06546854942233633,\n        \"n_leaked\": 51,\n        \"example_leaked_outputs\": [\n          {\n            \"row_id\": \"en-zh_CN_#_speech_#_vid_7Aw4Q46omiM::278::Qwen3-235B\",\n            \"masked_text\": \"__BLANK__，这跟__BLANK__。但__BLANK__，如果你想要为自己__BLANK__出__BLANK__，这就是你必须去做的，对吧。 好的，那么问题是，你会给年轻__BLANK__自己什么建议？ 我想告诉自己，我随时都可以为自己留点时间。有时候我会陷入日常生活的各种事务中，比如学业、__BLANK__等等。所以，我需要提醒自己，我总可以抽出时间来照顾自己，为自己留点时间，和朋友相处...\",\n            \"repaired_text\": \"有点做他们自己的事情，你知道吗，这跟其他人做的事情很__BLANK__。但__BLANK__，如果你想要为自己__BLANK__出__BLANK__，这就是你必须去做的，对吧。 好的，那么问题是，你会给年轻__BLANK__自己什么建议？ 我想告诉自己，我随时都可以为自己留点时间。有时候我会陷入日常生活的各种事务中，比如学业、__BLANK__等等。所以，我需要提醒自己，我总可以抽出时间来照顾自己...\"\n          },\n          {\n            \"row_id\": \"en-zh_CN_#_speech_#_vid_fWRlPSl5itQ::314::UvA-MT\",\n            \"masked_text\": \"为了学习这些知识，你必须经历痛苦和折磨。但这一切都是值得的，因为当你__BLANK__顿悟时，你会意识到这就是世界的运作方式。这就是光是什么。你知道，这就是原子是如何运作的。这就是我们的身体是如何运作的。而这一切都得益于物理学。我认为这是你能体验到的最美妙的事情之一。所以我会说这是非常值得的，但不要被它的机械性吓到。\",\n            \"repaired_text\": \"为了学习这些知识，你必须经历痛苦和折磨。但这一切都是值得的，因为当你豁然__BLANK__顿悟时，你会意识到这就是世界的运作方式。这就是光是什么。你知道，这就是原子是如何运作的。这就是我们的身体是如何运作的。而这一切都得益于物理学。我认为这是你能体验到的最美妙的事情之一。所以我会说这是非常值得的，但不要被它的机械性吓到。\"\n          },\n          {\n            \"row_id\": \"en-zh_CN_#_speech_#_vid_rU8nY03Lo5s::325::Wenyiil\",\n            \"masked_text\": \"__BLANK__，而且很多人其实并没有足够的__BLANK__在网上__BLANK__露脆弱的一面，所以他们会联系你，说“非常感谢你分享这个，因为我一直有这种感觉，但我不确定是否也有别人和我一样__BLANK__，__BLANK__我想是不言自明的。在社交媒体上，我们很容易感到被排斥，也很容易__BLANK__排斥别人。我觉得这是我们大家都在__BLANK__的事情，__BLANK__的。\",\n            \"repaired_text\": \"当然，而且很多人其实并没有足够的勇气在网上坦诚露脆弱的一面，所以他们会联系你，说“非常感谢你分享这个，因为我一直有这种感觉，但我不确定是否也有别人和我一样经历过类似的事情，这__BLANK__我想是不言自明的。在社交媒体上，我们很容易�", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] TOOL CALL — Bash · 2026-09-01 11:20:35 UTC

```
cat /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_2/gen_art/gen_art_experiment_2/pyproject.toml
echo "---"
python3 -c "
import json
p='/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/mini_data_out.json'
d=json.load(open(p))
print([ds['dataset'] for ds in d['datasets']])
nat = next(ds for ds in d['datasets'] if ds['dataset']=='wmt25_task3_natural')
print(len(nat['examples']))
print(json.dumps(nat['examples'][0], indent=2, ensure_ascii=False)[:2000])
"
```

### [15] TOOL RESULT — Bash · 2026-09-01 11:20:35 UTC

```
{"stdout": "[project]\nname = \"gen-art-experiment-2\"\nversion = \"0.1.0\"\ndescription = \"Condition B masked-fill baseline fidelity check (Padmanabhan 2025 SURREYPAI-S2 reproduction)\"\nrequires-python = \">=3.12\"\ndependencies = [\n    \"loguru==0.7.3\",\n    \"requests==2.34.2\",\n    \"aiohttp==3.14.3\",\n    \"tenacity==9.1.4\",\n    \"numpy==1.26.4\",\n    \"huggingface_hub==1.29.0\",\n    \"unbabel-comet==2.2.7\",\n    \"torch==2.6.0\",\n    \"sentence-transformers==6.0.1\",\n    \"setuptools==80.10.2\",\n]\n\n[tool.uv.sources]\ntorch = { index = \"pytorch-cu124\" }\n\n[[tool.uv.index]]\nname = \"pytorch-cu124\"\nurl = \"https://download.pytorch.org/whl/cu124\"\nexplicit = true\n---\n['wmt25_task3_natural', 'injected_error_augmentation']\n3\n{\n  \"input\": \"But not Dave Portnoy. The founder and owner of Barstool Sports - the Utne Reader for the light-domestic-swilling, backslapping, Zyn-packing, parlay-chasing American male - Portnoy has long been treated as an avatar for everything that elite media is not. Barstool might be considered the outermost ring of the so-called manosphere, the vast realm of male-oriented alternative media that has been credited with the rightward drift of the young male vote. Portnoy - a Trump supporter with a long history of misogynistic comments and bullying, who has been accused of nonconsensually filming women during uncomfortably rough sex - doesn't exactly run away from that label. (He has denied the claims about sexual misconduct and filed a suit against the outlet that published them; it was dismissed.) And what he noticed about the photos of Belichick and Hudson was the clutch Hudson wore, which was shaped like a little football: \\\"Very cool purse from BB's girlfriend,\\\" he posted on X. \\\"Football girlfriend purse.\\\"\",\n  \"output\": \"但戴夫·波特诺伊不是这样的。作为Barstool Sports——一本专为热爱啤酒、爱拍马屁、惯于用ZYN解压、喜欢押注的美国男性而设的杂志——的创始者兼所有者，波特诺伊一直被视为精英媒体所不具备的一切的化身。Barstool可以被视为所谓“男权文化圈”的最外层，这是一片以男性为导向的另类媒体的广阔领域，这些媒体被认为促成了年轻男性选票向右倾的趋势。波特诺伊——一位有长期发表女性歧视言论和欺凌行为的特朗普支持者——曾被指控在激烈性交过程中未经同意拍摄女性的视频——他对这个标签并不避讳。（他否认了关于性行为不端的指控，并对发布这些指控的媒体提起诉讼；该诉讼被驳回了。）而他对贝利奇克和哈德森照片的留意点是哈德森戴的手链，形状像一个小橄榄球：“BB女友的手袋真酷。”他在X上发帖说，“橄榄球女女友手袋。”\",\n  \"metadata_language_pair\": \"en-zh_CN\",\n  \"metadata_domain\": \"news\",\n  \"metadata_qe_flagged_spans\": [\n    {\n      \"start_i\": 3,\n      \"end_i\": 4,\n      \"severity\": \"critical\"\n    },\n    {\n      \"start_i\": 5,\n      \"end_i\": 13,\n      \"severity\": \"critical\"\n    },\n    {\n      \"start_i\": 16,\n      \"end_i\": 31,\n      \"severity\": \"critical\"\n    },\n    {\n      \"start_i\": 37,\n      \"end_i\": 60,\n      \"severity\": \"critical\"\n    },\n    {\n      \"start_i\": 82,\n      \"end_i\": 83,\n      \"severity\": \"critical\"\n    },\n    {\n      \"start_i\": 90,\n      \"end_i\": 92,\n      \"severity\": \"critical\"\n    },\n    {", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] TOOL CALL — Bash · 2026-09-01 11:20:43 UTC

```
python3 -c "
import json
p='/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/mini_data_out.json'
d=json.load(open(p))
nat = next(ds for ds in d['datasets'] if ds['dataset']=='wmt25_task3_natural')
e = nat['examples'][0]
print(sorted(e.keys()))
for ex in nat['examples']:
    print(ex.get('metadata_fold'), ex.get('metadata_language_pair'), ex.get('metadata_overall_qe_score'))
"
ls -la /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/
```

### [17] TOOL RESULT — Bash · 2026-09-01 11:20:43 UTC

```
{"stdout": "['input', 'metadata_doc_id', 'metadata_domain', 'metadata_fold', 'metadata_human_error_annotations', 'metadata_invariant_category', 'metadata_language_pair', 'metadata_notes', 'metadata_overall_qe_score', 'metadata_provenance', 'metadata_qe_flagged_spans', 'metadata_segment_id', 'metadata_source_dataset', 'metadata_system_id', 'output']\nexperimental_pool en-zh_CN 0.7515233159065247\nexperimental_pool en-zh_CN 0.7515233159065247\nchecker_validation_heldout en-zh_CN 0.7872632741928101\ntotal 32398\ndrwxr-xr-x 2 165536 165536  2002781 Sep  1 05:22 .\ndrwxr-xr-x 5 root   root    2004618 Sep  1 05:23 ..\n-rw-r--r-- 1 165536 165536 29122264 Sep  1 05:22 full_data_out.json\n-rw-r--r-- 1 root   root      31541 Sep  1 05:22 mini_data_out.json\n-rw-r--r-- 1 root   root      12752 Sep  1 05:22 preview_data_out.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] TOOL CALL — Bash · 2026-09-01 11:20:53 UTC

```
python3 -c "
import json, random

FULL = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json'
d = json.load(open(FULL))
nat = next(ds for ds in d['datasets'] if ds['dataset'] == 'wmt25_task3_natural')
rows = [e for e in nat['examples'] if e['metadata_fold']=='experimental_pool' and e['metadata_language_pair'] in ('en-zh_CN','en-cs_CZ') and e['metadata_overall_qe_score'] is not None]
print('total eligible', len(rows))

def bucket(q):
    if q >= 0.90: return 'high'
    if q >= 0.50: return 'mid'
    return 'low'

from collections import defaultdict
groups = defaultdict(list)
for r in rows:
    groups[(r['metadata_language_pair'], bucket(r['metadata_overall_qe_score']))].append(r)
for k,v in groups.items():
    print(k, len(v))

rng = random.Random(42)
selected = []
per_group_target = 8
for k, v in groups.items():
    rng.shuffle(v)
    selected.extend(v[:per_group_target])
print('selected', len(selected))

# cap sentence length for a snappy demo (avoid huge speech transcripts)
selected = [r for r in selected if len(r['input']) < 600]
print('after length filter', len(selected))
selected = selected[:60]
print('final n', len(selected))

out = {'datasets': [{'dataset': 'wmt25_task3_natural', 'examples': selected}]}
with open('mini_demo_data.json','w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('wrote', len(json.dumps(out)))
"
ls -la mini_demo_data.json
```

### [19] TOOL RESULT — Bash · 2026-09-01 11:20:53 UTC

```
{"stdout": "total eligible 1560\n('en-zh_CN', 'mid') 778\n('en-zh_CN', 'low') 1\n('en-cs_CZ', 'mid') 770\n('en-cs_CZ', 'low') 11\nselected 25\nafter length filter 8\nfinal n 8\nwrote 22513\n-rw-r--r-- 1 root root 28026 Sep  1 11:20 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] TOOL CALL — Bash · 2026-09-01 11:21:01 UTC

```
python3 -c "
import json, random

FULL = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out/full_data_out.json'
d = json.load(open(FULL))
nat = next(ds for ds in d['datasets'] if ds['dataset'] == 'wmt25_task3_natural')
rows = [e for e in nat['examples'] if e['metadata_fold']=='experimental_pool' and e['metadata_language_pair'] in ('en-zh_CN','en-cs_CZ') and e['metadata_overall_qe_score'] is not None]

def bucket(q):
    if q >= 0.90: return 'high'
    if q >= 0.50: return 'mid'
    return 'low'

from collections import defaultdict
groups = defaultdict(list)
for r in rows:
    if len(r['input']) < 400:
        groups[(r['metadata_language_pair'], bucket(r['metadata_overall_qe_score']))].append(r)
for k,v in groups.items():
    print(k, len(v))

rng = random.Random(42)
selected = []
per_group_target = 15
for k, v in groups.items():
    rng.shuffle(v)
    selected.extend(v[:per_group_target])
print('selected', len(selected))

out = {'datasets': [{'dataset': 'wmt25_task3_natural', 'examples': selected}]}
with open('mini_demo_data.json','w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('wrote bytes', len(json.dumps(out)))
print('n', len(selected))
"
ls -la mini_demo_data.json
```

### [21] TOOL RESULT — Bash · 2026-09-01 11:21:01 UTC

```
{"stdout": "('en-zh_CN', 'mid') 117\n('en-cs_CZ', 'mid') 106\nselected 30\nwrote bytes 65552\nn 30\n-rw-r--r-- 1 root root 80797 Sep  1 11:20 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [22] ASSISTANT · 2026-09-01 11:21:03 UTC

```
Good — 30 diverse rows (15 per language pair, all in the "mid" severity bucket where masking actually happens, short enough for a snappy demo). Now let's build the notebook.
```

### [23] TOOL CALL — ToolSearch · 2026-09-01 11:21:03 UTC

```
{'query': 'select:NotebookEdit', 'max_results': 1}
```

### [24] TOOL RESULT — ToolSearch · 2026-09-01 11:21:03 UTC

```
{"matches": ["NotebookEdit"], "query": "select:NotebookEdit", "total_deferred_tools": 22}
```

### [25] TOOL CALL — Bash · 2026-09-01 11:21:27 UTC

```
env | grep -i OPENROUTER | sed 's/=.*/=<set>/'; echo done
```

### [26] TOOL RESULT — Bash · 2026-09-01 11:21:27 UTC

```
{"stdout": "OPENROUTER_API_KEY=<set>\ndone", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] ASSISTANT · 2026-09-01 11:21:31 UTC

```
Good, the key is available. Now let's build the notebook.
```

### [28] TOOL CALL — Write · 2026-09-01 11:21:31 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb

{
 "cells": [],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.12.12"}
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

### [29] TOOL RESULT — Write · 2026-09-01 11:21:31 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "content": "{\n \"cells\": [],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.12\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [30] TOOL CALL — Read · 2026-09-01 11:21:33 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb
```

### [31] TOOL RESULT — Read · 2026-09-01 11:21:33 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "cells": []}}
```

### [32] TOOL CALL — NotebookEdit · 2026-09-01 11:21:45 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)\'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans — the faithful \\"Condition B\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan\'s documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the ~13-minute COMET download retry budget, which would blow the demo\'s runtime budget) — the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan\'s published ΔCOMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\"baseline\\" is the untouched hypothesis (pre-edit), \\"method\\" is Condition B\'s masked-fill edit — both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).'}
```

### [33] TOOL RESULT — NotebookEdit · 2026-09-01 11:21:45 UTC

```
{"new_source": "# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans — the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the ~13-minute COMET download retry budget, which would blow the demo's runtime budget) — the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published ΔCOMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit — both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "765a351d", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.12\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\\\n\\\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\\\n\\\\n**What it does:**\\\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans — the faithful \\\\\\\"Condition B\\\\\\\" baseline.\\\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the ~13-minute COMET download retry budget, which would blow the demo's runtime budget) — the substitution is explicit, not silent.\\\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published ΔCOMET.\\\\n\\\\nThis is a **sanity-check gate**, not a novel method: \\\\\\\"baseline\\\\\\\" is the untouched hypothesis (pre-edit), \\\\\\\"method\\\\\\\" is Condition B's masked-fill edit — both scored identically to eliminate scorer-side confounds.\\\\n\\\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [34] TOOL CALL — Bash · 2026-09-01 11:21:51 UTC

```
python3 -c "
import json
nb = json.load(open('/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb'))
print(repr(nb['cells'][0]['source'][:200]))
"
```

### [35] TOOL RESULT — Bash · 2026-09-01 11:21:51 UTC

```
{"stdout": "\"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\\\n\\\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill b\"", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [36] TOOL CALL — NotebookEdit · 2026-09-01 11:21:59 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '765a351d', 'new_source': '# Sanity-Check for the Masked-Fill Baseline (Condition B)\n\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)\'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\n\n**What it does:**\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful "Condition B" baseline.\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan\'s documented Appendix B failure mode).\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo\'s runtime budget) -- the substitution is explicit, not silent.\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan\'s published delta-COMET.\n\nThis is a **sanity-check gate**, not a novel method: "baseline" is the untouched hypothesis (pre-edit), "method" is Condition B\'s masked-fill edit -- both scored identically to eliminate scorer-side confounds.\n\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).'}
```

### [37] TOOL RESULT — NotebookEdit · 2026-09-01 11:21:59 UTC

```
{"new_source": "# Sanity-Check for the Masked-Fill Baseline (Condition B)\n\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\n\n**What it does:**\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \"Condition B\" baseline.\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\n\nThis is a **sanity-check gate**, not a novel method: \"baseline\" is the untouched hypothesis (pre-edit), \"method\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\n\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).", "old_source": "# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans — the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the ~13-minute COMET download retry budget, which would blow the demo's runtime budget) — the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published ΔCOMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit — both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).", "cell_type": "code", "language": "python", "edit_mode": "replace", "cell_id": "765a351d", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\\\n\\\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\\\n\\\\n**What it does:**\\\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans — the faithful \\\\\\\"Condition B\\\\\\\" baseline.\\\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the ~13-minute COMET download retry budget, which would blow the demo's runtime budget) — the substitution is explicit, not silent.\\\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published ΔCOMET.\\\\n\\\\nThis is a **sanity-check gate**, not a novel method: \\\\\\\"baseline\\\\\\\" is the untouched hypothesis (pre-edit), \\\\\\\"method\\\\\\\" is Condition B's masked-fill edit — both scored identically to eliminate scorer-side confounds.\\\\n\\\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [38] ASSISTANT · 2026-09-01 11:22:05 UTC

```
Good, that fixed it. Now let's add the remaining cells.
```

### [39] TOOL CALL — NotebookEdit · 2026-09-01 11:22:05 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '765a351d', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\n_pip('aiohttp==3.14.3')\n_pip('tenacity==9.1.4')\n_pip('loguru==0.7.3')\n\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\nif 'google.colab' not in sys.modules:\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')"}
```

### [40] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:05 UTC

```
{"new_source": "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\n_pip('aiohttp==3.14.3')\n_pip('tenacity==9.1.4')\n_pip('loguru==0.7.3')\n\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\nif 'google.colab' not in sys.modules:\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "47eacb5f", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [41] TOOL CALL — NotebookEdit · 2026-09-01 11:22:09 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '47eacb5f', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport os\nimport random\nimport re\nimport time\nfrom collections import Counter\nfrom typing import Any\n\nimport aiohttp\nfrom loguru import logger\n\nimport matplotlib.pyplot as plt  # for the results/visualization cell'}
```

### [42] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:09 UTC

```
{"new_source": "# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport os\nimport random\nimport re\nimport time\nfrom collections import Counter\nfrom typing import Any\n\nimport aiohttp\nfrom loguru import logger\n\nimport matplotlib.pyplot as plt  # for the results/visualization cell", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "692a0045", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [43] TOOL CALL — NotebookEdit · 2026-09-01 11:22:15 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '692a0045', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Load the demo data\n\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally."}
```

### [44] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:15 UTC

```
{"new_source": "## Load the demo data\n\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "63b8d8ed", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [45] TOOL CALL — NotebookEdit · 2026-09-01 11:22:19 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '63b8d8ed', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json"\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists("mini_demo_data.json"):\n        with open("mini_demo_data.json") as f:\n            return json.load(f)\n    raise FileNotFoundError("Could not load mini_demo_data.json")'}
```

### [46] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:19 UTC

```
{"new_source": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\"\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f:\n            return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "2c819c39", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [47] TOOL CALL — NotebookEdit · 2026-09-01 11:22:23 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '2c819c39', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'data = load_data()\nnatural = next(ds for ds in data["datasets"] if ds["dataset"] == "wmt25_task3_natural")\nprint(f"Loaded {len(natural[\'examples\'])} rows")\nprint("Language pairs present:", sorted(set(e[\'metadata_language_pair\'] for e in natural[\'examples\'])))'}
```

### [48] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:23 UTC

```
{"new_source": "data = load_data()\nnatural = next(ds for ds in data[\"datasets\"] if ds[\"dataset\"] == \"wmt25_task3_natural\")\nprint(f\"Loaded {len(natural['examples'])} rows\")\nprint(\"Language pairs present:\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "da02eb64", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [49] ASSISTANT · 2026-09-01 11:22:27 UTC

```
Now the config cell with tunable parameters.
```

### [50] TOOL CALL — NotebookEdit · 2026-09-01 11:22:27 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'da02eb64', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Configuration\n\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\n\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).'}
```

### [51] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:27 UTC

```
{"new_source": "## Configuration\n\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\n\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "fb229846", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb229846\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\\n\\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [52] TOOL CALL — NotebookEdit · 2026-09-01 11:22:45 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'fb229846', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# --- Tunable parameters (start small, scale up as time/budget allows) ---\nMAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful\nCONCURRENCY = 4            # original default was 16\nSOFT_COST_CAP_USD = 0.50\nHARD_COST_CAP_USD = 0.60\n\n# --- Original module-level config from method.py ---\nOPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")\nOPENROUTER_URL = "https://openrouter.ai/api/v1/responses"\nOPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"\nAII_COST_LEDGER = os.environ.get("AII_COST_LEDGER")\n\nRNG = random.Random(20260901)\n\nLANG_PAIRS = ["en-zh_CN", "en-cs_CZ"]\nREPAIR_MODEL = "google/gemma-3-12b-it"\nREPAIR_MODEL_FALLBACKS = [\n    "qwen/qwen-2.5-7b-instruct",\n    "mistralai/mistral-nemo",\n    "meta-llama/llama-3.1-8b-instruct",\n    "mistralai/ministral-8b-2512",\n]\n\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\n# with WMT25 organizer Table 15 (dossier Block A).\nPUBLISHED_DELTA_COMET = {\n    "en-cs_CZ": -0.00724,\n    "en-zh_CN": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\n}\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\n\n# Masking placeholder (see method.py\'s docstring on prompt provenance).\nMASK_TOKEN = "__BLANK__"\nMASKING_PROMPT_TEMPLATE = """You are repairing a machine-translated sentence. Some words or phrases in the\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\n\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\n\nEnglish source:\n{source}\n\nTranslation with blanks:\n{masked_sentence}\n\nRepaired translation:"""\n\nLEAK_PATTERNS = [\n    re.compile(r"__BLANK__"),\n    re.compile(r"__\\w+__"),\n    re.compile(r"(?i)corrected words?\\s*:"),\n    re.compile(r"(?i)here is the (corrected|fixed|revised)"),\n    re.compile(r"(?i)^(sure|okay|here\'s|here is)\\b"),\n    re.compile(r"\\[MASK\\]|\\[BLANK\\]|<blank>|<mask>", re.IGNORECASE),\n]\n\nJUDGE_MODEL = "openai/gpt-4o-mini"\nJUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\nRespond with ONLY the number, nothing else.\n\nSOURCE (English): {source}\n\nTRANSLATION: {mt}\n\nScore:"""\n\nlogger.remove()\nlogger.add(lambda msg: print(msg, end=""), level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [53] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:45 UTC

```
{"new_source": "# --- Tunable parameters (start small, scale up as time/budget allows) ---\nMAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful\nCONCURRENCY = 4            # original default was 16\nSOFT_COST_CAP_USD = 0.50\nHARD_COST_CAP_USD = 0.60\n\n# --- Original module-level config from method.py ---\nOPENROUTER_API_KEY = os.environ.get(\"OPENROUTER_API_KEY\", \"\")\nOPENROUTER_URL = \"https://openrouter.ai/api/v1/responses\"\nOPENROUTER_MODELS_URL = \"https://openrouter.ai/api/v1/models\"\nAII_COST_LEDGER = os.environ.get(\"AII_COST_LEDGER\")\n\nRNG = random.Random(20260901)\n\nLANG_PAIRS = [\"en-zh_CN\", \"en-cs_CZ\"]\nREPAIR_MODEL = \"google/gemma-3-12b-it\"\nREPAIR_MODEL_FALLBACKS = [\n    \"qwen/qwen-2.5-7b-instruct\",\n    \"mistralai/mistral-nemo\",\n    \"meta-llama/llama-3.1-8b-instruct\",\n    \"mistralai/ministral-8b-2512\",\n]\n\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\n# with WMT25 organizer Table 15 (dossier Block A).\nPUBLISHED_DELTA_COMET = {\n    \"en-cs_CZ\": -0.00724,\n    \"en-zh_CN\": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\n}\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\n\n# Masking placeholder (see method.py's docstring on prompt provenance).\nMASK_TOKEN = \"__BLANK__\"\nMASKING_PROMPT_TEMPLATE = \"\"\"You are repairing a machine-translated sentence. Some words or phrases in the\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\n\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\n\nEnglish source:\n{source}\n\nTranslation with blanks:\n{masked_sentence}\n\nRepaired translation:\"\"\"\n\nLEAK_PATTERNS = [\n    re.compile(r\"__BLANK__\"),\n    re.compile(r\"__\\w+__\"),\n    re.compile(r\"(?i)corrected words?\\s*:\"),\n    re.compile(r\"(?i)here is the (corrected|fixed|revised)\"),\n    re.compile(r\"(?i)^(sure|okay|here's|here is)\\b\"),\n    re.compile(r\"\\[MASK\\]|\\[BLANK\\]|<blank>|<mask>\", re.IGNORECASE),\n]\n\nJUDGE_MODEL = \"openai/gpt-4o-mini\"\nJUDGE_PROMPT = \"\"\"Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\nRespond with ONLY the number, nothing else.\n\nSOURCE (English): {source}\n\nTRANSLATION: {mt}\n\nScore:\"\"\"\n\nlogger.remove()\nlogger.add(lambda msg: print(msg, end=\"\"), level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "764dc8fc", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb229846\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\\n\\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb229846\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\\n\\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"764dc8fc\",\n   \"source\": \"# --- Tunable parameters (start small, scale up as time/budget allows) ---\\nMAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful\\nCONCURRENCY = 4            # original default was 16\\nSOFT_COST_CAP_USD = 0.50\\nHARD_COST_CAP_USD = 0.60\\n\\n# --- Original module-level config from method.py ---\\nOPENROUTER_API_KEY = os.environ.get(\\\"OPENROUTER_API_KEY\\\", \\\"\\\")\\nOPENROUTER_URL = \\\"https://openrouter.ai/api/v1/responses\\\"\\nOPENROUTER_MODELS_URL = \\\"https://openrouter.ai/api/v1/models\\\"\\nAII_COST_LEDGER = os.environ.get(\\\"AII_COST_LEDGER\\\")\\n\\nRNG = random.Random(20260901)\\n\\nLANG_PAIRS = [\\\"en-zh_CN\\\", \\\"en-cs_CZ\\\"]\\nREPAIR_MODEL = \\\"google/gemma-3-12b-it\\\"\\nREPAIR_MODEL_FALLBACKS = [\\n    \\\"qwen/qwen-2.5-7b-instruct\\\",\\n    \\\"mistralai/mistral-nemo\\\",\\n    \\\"meta-llama/llama-3.1-8b-instruct\\\",\\n    \\\"mistralai/ministral-8b-2512\\\",\\n]\\n\\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\\n# with WMT25 organizer Table 15 (dossier Block A).\\nPUBLISHED_DELTA_COMET = {\\n    \\\"en-cs_CZ\\\": -0.00724,\\n    \\\"en-zh_CN\\\": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\\n}\\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\\n\\n# Masking placeholder (see method.py's docstring on prompt provenance).\\nMASK_TOKEN = \\\"__BLANK__\\\"\\nMASKING_PROMPT_TEMPLATE = \\\"\\\"\\\"You are repairing a machine-translated sentence. Some words or phrases in the\\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\\n\\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\\n\\nEnglish source:\\n{source}\\n\\nTranslation with blanks:\\n{masked_sentence}\\n\\nRepaired translation:\\\"\\\"\\\"\\n\\nLEAK_PATTERNS = [\\n    re.compile(r\\\"__BLANK__\\\"),\\n    re.compile(r\\\"__\\\\w+__\\\"),\\n    re.compile(r\\\"(?i)corrected words?\\\\s*:\\\"),\\n    re.compile(r\\\"(?i)here is the (corrected|fixed|revised)\\\"),\\n    re.compile(r\\\"(?i)^(sure|okay|here's|here is)\\\\b\\\"),\\n    re.compile(r\\\"\\\\[MASK\\\\]|\\\\[BLANK\\\\]|<blank>|<mask>\\\", re.IGNORECASE),\\n]\\n\\nJUDGE_MODEL = \\\"openai/gpt-4o-mini\\\"\\nJUDGE_PROMPT = \\\"\\\"\\\"Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\\nRespond with ONLY the number, nothing else.\\n\\nSOURCE (English): {source}\\n\\nTRANSLATION: {mt}\\n\\nScore:\\\"\\\"\\\"\\n\\nlogger.remove()\\nlogger.add(lambda msg: print(msg, end=\\\"\\\"), level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [54] ASSISTANT · 2026-09-01 11:22:51 UTC

```
Now the Algorithm 1 masking rule section.
```

### [55] TOOL CALL — NotebookEdit · 2026-09-01 11:22:51 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '764dc8fc', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Algorithm 1: severity-conditioned masking rule\n\nVerbatim from the resource-dossier dependency. Given a row's overall QE score:\n- `qe_score >= 0.90` -> no spans are masked (Condition B never touches the sentence).\n- `0.50 <= qe_score < 0.90` -> only non-minor (major/critical) spans are masked.\n- `qe_score < 0.90` -> every flagged span is masked.\n\nOverlapping/adjacent spans are merged first so masking never corrupts character offsets."}
```

### [56] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:51 UTC

```
{"new_source": "## Algorithm 1: severity-conditioned masking rule\n\nVerbatim from the resource-dossier dependency. Given a row's overall QE score:\n- `qe_score >= 0.90` -> no spans are masked (Condition B never touches the sentence).\n- `0.50 <= qe_score < 0.90` -> only non-minor (major/critical) spans are masked.\n- `qe_score < 0.90` -> every flagged span is masked.\n\nOverlapping/adjacent spans are merged first so masking never corrupts character offsets.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "b6d603e4", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb229846\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\\n\\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"764dc8fc\",\n   \"source\": \"# --- Tunable parameters (start small, scale up as time/budget allows) ---\\nMAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful\\nCONCURRENCY = 4            # original default was 16\\nSOFT_COST_CAP_USD = 0.50\\nHARD_COST_CAP_USD = 0.60\\n\\n# --- Original module-level config from method.py ---\\nOPENROUTER_API_KEY = os.environ.get(\\\"OPENROUTER_API_KEY\\\", \\\"\\\")\\nOPENROUTER_URL = \\\"https://openrouter.ai/api/v1/responses\\\"\\nOPENROUTER_MODELS_URL = \\\"https://openrouter.ai/api/v1/models\\\"\\nAII_COST_LEDGER = os.environ.get(\\\"AII_COST_LEDGER\\\")\\n\\nRNG = random.Random(20260901)\\n\\nLANG_PAIRS = [\\\"en-zh_CN\\\", \\\"en-cs_CZ\\\"]\\nREPAIR_MODEL = \\\"google/gemma-3-12b-it\\\"\\nREPAIR_MODEL_FALLBACKS = [\\n    \\\"qwen/qwen-2.5-7b-instruct\\\",\\n    \\\"mistralai/mistral-nemo\\\",\\n    \\\"meta-llama/llama-3.1-8b-instruct\\\",\\n    \\\"mistralai/ministral-8b-2512\\\",\\n]\\n\\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\\n# with WMT25 organizer Table 15 (dossier Block A).\\nPUBLISHED_DELTA_COMET = {\\n    \\\"en-cs_CZ\\\": -0.00724,\\n    \\\"en-zh_CN\\\": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\\n}\\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\\n\\n# Masking placeholder (see method.py's docstring on prompt provenance).\\nMASK_TOKEN = \\\"__BLANK__\\\"\\nMASKING_PROMPT_TEMPLATE = \\\"\\\"\\\"You are repairing a machine-translated sentence. Some words or phrases in the\\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\\n\\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\\n\\nEnglish source:\\n{source}\\n\\nTranslation with blanks:\\n{masked_sentence}\\n\\nRepaired translation:\\\"\\\"\\\"\\n\\nLEAK_PATTERNS = [\\n    re.compile(r\\\"__BLANK__\\\"),\\n    re.compile(r\\\"__\\\\w+__\\\"),\\n    re.compile(r\\\"(?i)corrected words?\\\\s*:\\\"),\\n    re.compile(r\\\"(?i)here is the (corrected|fixed|revised)\\\"),\\n    re.compile(r\\\"(?i)^(sure|okay|here's|here is)\\\\b\\\"),\\n    re.compile(r\\\"\\\\[MASK\\\\]|\\\\[BLANK\\\\]|<blank>|<mask>\\\", re.IGNORECASE),\\n]\\n\\nJUDGE_MODEL = \\\"openai/gpt-4o-mini\\\"\\nJUDGE_PROMPT = \\\"\\\"\\\"Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\\nRespond with ONLY the number, nothing else.\\n\\nSOURCE (English): {source}\\n\\nTRANSLATION: {mt}\\n\\nScore:\\\"\\\"\\\"\\n\\nlogger.remove()\\nlogger.add(lambda msg: print(msg, end=\\\"\\\"), level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n   \"source\": \"# Sanity-Check for the Masked-Fill Baseline (Condition B)\\n\\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental_pool` rows (`en-zh_CN`, `en-cs_CZ`).\\n\\n**What it does:**\\n1. Applies a severity-conditioned masking rule (Algorithm 1) to QE-flagged error spans in a machine-translated sentence.\\n2. Calls an LLM (`google/gemma-3-12b-it` via OpenRouter) once per row, with no retry/re-check, to fill in the masked spans -- the faithful \\\"Condition B\\\" baseline.\\n3. Detects **leakage**: surviving placeholder tokens or generic instruction-following artifacts in the repaired text (Padmanabhan's documented Appendix B failure mode).\\n4. Scores quality before/after the edit. The original run found both COMET checkpoints (`Unbabel/wmt22-cometkiwi-da`, `Unbabel/wmt22-comet-da`) persistently rate-limited (HTTP 429) on HuggingFace Hub, so it fell back to a documented, non-COMET **LLM-judge 0-1 adequacy proxy** (`openai/gpt-4o-mini`). This notebook reproduces that same fallback path directly (skipping the multi-minute COMET download retry budget, which would blow the demo's runtime budget) -- the substitution is explicit, not silent.\\n5. Computes a three-way gate verdict (`PASS`/`FAIL`, suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` when the scorer was substituted) checking direction, magnitude, and leakage against Padmanabhan's published delta-COMET.\\n\\nThis is a **sanity-check gate**, not a novel method: \\\"baseline\\\" is the untouched hypothesis (pre-edit), \\\"method\\\" is Condition B's masked-fill edit -- both scored identically to eliminate scorer-side confounds.\\n\\n**Requires** an `OPENROUTER_API_KEY` environment variable (real API calls are made to a small subset of rows).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"47eacb5f\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# aiohttp, tenacity, loguru -- NOT pre-installed on Colab, always install\\n_pip('aiohttp==3.14.3')\\n_pip('tenacity==9.1.4')\\n_pip('loguru==0.7.3')\\n\\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\\nif 'google.colab' not in sys.modules:\\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"692a0045\",\n   \"source\": \"# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\\nfrom __future__ import annotations\\n\\nimport asyncio\\nimport json\\nimport os\\nimport random\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom typing import Any\\n\\nimport aiohttp\\nfrom loguru import logger\\n\\nimport matplotlib.pyplot as plt  # for the results/visualization cell\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"63b8d8ed\",\n   \"source\": \"## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset (30 rows: 15 per language pair, all drawn from the mid-severity QE band where Condition B's masking rule actually fires) of the `wmt25_task3_natural` dataset that `method.py` loads from its dataset dependency (`FULL_DATA_PATH` / `MINI_DATA_PATH` in the original script). This cell fetches it from GitHub with a local-file fallback so the notebook works both on Colab and locally.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c819c39\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\\\"\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"da02eb64\",\n   \"source\": \"data = load_data()\\nnatural = next(ds for ds in data[\\\"datasets\\\"] if ds[\\\"dataset\\\"] == \\\"wmt25_task3_natural\\\")\\nprint(f\\\"Loaded {len(natural['examples'])} rows\\\")\\nprint(\\\"Language pairs present:\\\", sorted(set(e['metadata_language_pair'] for e in natural['examples'])))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb229846\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from `method.py`, gathered in one place. `MAX_ROWS_PER_PAIR` is set to the smallest value that still exercises both language pairs and produces a real gate verdict; scale it up (up to 15 -- the full size of `mini_demo_data.json`) to see the metrics stabilize, subject to the OpenRouter cost caps below.\\n\\n`OPENROUTER_API_KEY` must be set as an environment variable (real API calls are made to `google/gemma-3-12b-it` for repairs and `openai/gpt-4o-mini` for quality scoring).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"764dc8fc\",\n   \"source\": \"# --- Tunable parameters (start small, scale up as time/budget allows) ---\\nMAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful\\nCONCURRENCY = 4            # original default was 16\\nSOFT_COST_CAP_USD = 0.50\\nHARD_COST_CAP_USD = 0.60\\n\\n# --- Original module-level config from method.py ---\\nOPENROUTER_API_KEY = os.environ.get(\\\"OPENROUTER_API_KEY\\\", \\\"\\\")\\nOPENROUTER_URL = \\\"https://openrouter.ai/api/v1/responses\\\"\\nOPENROUTER_MODELS_URL = \\\"https://openrouter.ai/api/v1/models\\\"\\nAII_COST_LEDGER = os.environ.get(\\\"AII_COST_LEDGER\\\")\\n\\nRNG = random.Random(20260901)\\n\\nLANG_PAIRS = [\\\"en-zh_CN\\\", \\\"en-cs_CZ\\\"]\\nREPAIR_MODEL = \\\"google/gemma-3-12b-it\\\"\\nREPAIR_MODEL_FALLBACKS = [\\n    \\\"qwen/qwen-2.5-7b-instruct\\\",\\n    \\\"mistralai/mistral-nemo\\\",\\n    \\\"meta-llama/llama-3.1-8b-instruct\\\",\\n    \\\"mistralai/ministral-8b-2512\\\",\\n]\\n\\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\\n# with WMT25 organizer Table 15 (dossier Block A).\\nPUBLISHED_DELTA_COMET = {\\n    \\\"en-cs_CZ\\\": -0.00724,\\n    \\\"en-zh_CN\\\": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\\n}\\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\\n\\n# Masking placeholder (see method.py's docstring on prompt provenance).\\nMASK_TOKEN = \\\"__BLANK__\\\"\\nMASKING_PROMPT_TEMPLATE = \\\"\\\"\\\"You are repairing a machine-translated sentence. Some words or phrases in the\\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\\n\\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\\n\\nEnglish source:\\n{source}\\n\\nTranslation with blanks:\\n{masked_sentence}\\n\\nRepaired translation:\\\"\\\"\\\"\\n\\nLEAK_PATTERNS = [\\n    re.compile(r\\\"__BLANK__\\\"),\\n    re.compile(r\\\"__\\\\w+__\\\"),\\n    re.compile(r\\\"(?i)corrected words?\\\\s*:\\\"),\\n    re.compile(r\\\"(?i)here is the (corrected|fixed|revised)\\\"),\\n    re.compile(r\\\"(?i)^(sure|okay|here's|here is)\\\\b\\\"),\\n    re.compile(r\\\"\\\\[MASK\\\\]|\\\\[BLANK\\\\]|<blank>|<mask>\\\", re.IGNORECASE),\\n]\\n\\nJUDGE_MODEL = \\\"openai/gpt-4o-mini\\\"\\nJUDGE_PROMPT = \\\"\\\"\\\"Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\\nRespond with ONLY the number, nothing else.\\n\\nSOURCE (English): {source}\\n\\nTRANSLATION: {mt}\\n\\nScore:\\\"\\\"\\\"\\n\\nlogger.remove()\\nlogger.add(lambda msg: print(msg, end=\\\"\\\"), level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"b6d603e4\",\n   \"source\": \"## Algorithm 1: severity-conditioned masking rule\\n\\nVerbatim from the resource-dossier dependency. Given a row's overall QE score:\\n- `qe_score >= 0.90` -> no spans are masked (Condition B never touches the sentence).\\n- `0.50 <= qe_score < 0.90` -> only non-minor (major/critical) spans are masked.\\n- `qe_score < 0.90` -> every flagged span is masked.\\n\\nOverlapping/adjacent spans are merged first so masking never corrupts character offsets.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [57] TOOL CALL — NotebookEdit · 2026-09-01 11:22:59 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'b6d603e4', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def merge_overlapping_spans(spans: list[dict[str, Any]]) -> list[dict[str, Any]]:\n    """Merge overlapping/adjacent char spans so masking never corrupts offsets.\n\n    Keeps the most severe severity label for a merged region (critical > major > minor).\n    """\n    if not spans:\n        return []\n    sev_rank = {"critical": 3, "major": 2, "minor": 1}\n    ordered = sorted(spans, key=lambda s: (s["start_i"], s["end_i"]))\n    merged = [dict(ordered[0])]\n    for s in ordered[1:]:\n        last = merged[-1]\n        if s["start_i"] <= last["end_i"]:\n            last["end_i"] = max(last["end_i"], s["end_i"])\n            if sev_rank.get(s["severity"], 0) > sev_rank.get(last["severity"], 0):\n                last["severity"] = s["severity"]\n        else:\n            merged.append(dict(s))\n    return merged\n\n\ndef compute_spans_to_mask(qe_score: float, spans: list[dict[str, Any]]) -> list[dict[str, Any]]:\n    """Algorithm 1, verbatim per the dossier: severity-conditioned masking rule."""\n    spans = spans or []\n    if qe_score >= 0.90:\n        return []\n    if qe_score >= 0.50:\n        non_minor = [s for s in spans if s["severity"] != "minor"]\n        return non_minor if non_minor else spans\n    return spans\n\n\ndef apply_masking(text: str, spans_to_mask: list[dict[str, Any]]) -> str:\n    """Replace each (merged) span\'s char range in text with MASK_TOKEN, right-to-left."""\n    merged = merge_overlapping_spans(spans_to_mask)\n    merged.sort(key=lambda s: s["start_i"], reverse=True)\n    out = text\n    for s in merged:\n        start, end = s["start_i"], s["end_i"]\n        start = max(0, min(start, len(out)))\n        end = max(start, min(end, len(out)))\n        out = out[:start] + MASK_TOKEN + out[end:]\n    return out'}
```

### [58] TOOL RESULT — NotebookEdit · 2026-09-01 11:22:59 UTC

```
{"new_source": "def merge_overlapping_spans(spans: list[dict[str, Any]]) -> list[dict[str, Any]]:\n    \"\"\"Merge overlapping/adjacent char spans so masking never corrupts offsets.\n\n    Keeps the most severe severity label for a merged region (critical > major > minor).\n    \"\"\"\n    if not spans:\n        return []\n    sev_rank = {\"critical\": 3, \"major\": 2, \"minor\": 1}\n    ordered = sorted(spans, key=lambda s: (s[\"start_i\"], s[\"end_i\"]))\n    merged ... [truncated, 24200 chars total]
```

### [59] ASSISTANT · 2026-09-01 11:23:05 UTC

```
Now the OpenRouter calling infra section.
```

### [60] TOOL CALL — NotebookEdit · 2026-09-01 11:23:05 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'f4480986', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## OpenRouter async calling\n\nA thin async client for the OpenRouter Responses API, plus a `CostTracker` that accumulates spend and enforces the hard cost cap. `repair_row` applies the masking rule to one row and sends a single repair call (no retry/re-check across the model chain -- a failure just falls through to the next fallback model) with `run_condition_b` fanning that out over the whole row list.'}
```

### [61] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:05 UTC

```
{"new_source": "## OpenRouter async calling\n\nA thin async client for the OpenRouter Responses API, plus a `CostTracker` that accumulates spend and enforces the hard cost cap. `repair_row` applies the masking rule to one row and sends a single repair call (no retry/re-check across the model chain -- a failure just falls through to the next fallback model) with `run_condition_b` fanning that out over the whole row list.", "cell_type": "markdown", "language": "python", ... [truncated, 25448 chars total]
```

### [62] TOOL CALL — NotebookEdit · 2026-09-01 11:23:09 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '692a0045', 'new_source': '# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport os\nimport random\nimport re\nimport time\nfrom collections import Counter\nfrom typing import Any\n\nimport aiohttp\nfrom loguru import logger\nfrom tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential\n\nimport matplotlib.pyplot as plt  # for the results/visualization cell'}
```

### [63] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:09 UTC

```
{"new_source": "# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport os\nimport random\nimport re\nimport time\nfrom collections import Counter\nfrom typing import Any\n\nimport aiohttp\nfrom loguru import logger\nfrom tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential\n\nimport matplotlib.pyplot as plt  # for the resul... [truncated, 26535 chars total]
```

### [64] TOOL CALL — NotebookEdit · 2026-09-01 11:23:29 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'b6ba0622', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'class CostTracker:\n    def __init__(self, hard_cap: float):\n        self.total_usd = 0.0\n        self.n_calls = 0\n        self.n_failed = 0\n        self.hard_cap = hard_cap\n        self._lock = asyncio.Lock()\n\n    async def add(self, cost_usd: float | None, tool: str, **meta) -> None:\n        async with self._lock:\n            if cost_usd is not None:\n                self.total_usd += cost_usd\n            self.n_calls += 1\n            if AII_COST_LEDGER and cost_usd is not None:\n                rec = {"ts": time.time(), "tool": tool, "cost_usd": float(cost_usd), **meta}\n                try:\n                    with open(AII_COST_LEDGER, "a", encoding="utf-8") as f:\n                        f.write(json.dumps(rec) + "\\n")\n                except OSError:\n                    pass\n\n    def over_cap(self) -> bool:\n        return self.total_usd >= self.hard_cap\n\n\n_pricing_cache: dict[str, tuple[float, float]] = {}\n\n\ndef load_openrouter_pricing() -> None:\n    if _pricing_cache:\n        return\n    import requests\n\n    try:\n        resp = requests.get(OPENROUTER_MODELS_URL, timeout=30)\n        for entry in resp.json().get("data", []):\n            name = entry.get("id")\n            if not name:\n                continue\n            price = entry.get("pricing") or {}\n            try:\n                _pricing_cache[name] = (float(price.get("prompt", 0) or 0), float(price.get("completion", 0) or 0))\n            except (TypeError, ValueError):\n                continue\n        logger.info(f"Loaded OpenRouter pricing catalog ({len(_pricing_cache)} models)")\n    except Exception as e:\n        logger.warning(f"Could not load OpenRouter pricing catalog: {e}")\n\n\ndef estimate_call_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:\n    priced = _pricing_cache.get(model)\n    if priced is None:\n        return None\n    return round(input_tokens * priced[0] + output_tokens * priced[1], 8)\n\n\n@retry(\n    retry=retry_if_exception_type((aiohttp.ClientError, asyncio.TimeoutError)),\n    stop=stop_after_attempt(4),\n    wait=wait_exponential(multiplier=2, min=2, max=30),\n)\nasync def call_openrouter(\n    session: aiohttp.ClientSession, model: str, prompt: str, max_tokens: int, temperature: float = 0.0\n) -> dict[str, Any]:\n    payload = {"model": model, "input": prompt, "max_output_tokens": max_tokens, "temperature": temperature}\n    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}\n    async with session.post(OPENROUTER_URL, json=payload, headers=headers, timeout=aiohttp.ClientTimeout(total=120)) as resp:\n        body = await resp.json()\n        if resp.status != 200:\n            return {"success": False, "error": f"status {resp.status}: {str(body)[:300]}"}\n\n        output_text, reasoning_text = "", ""\n        if body.get("output_text"):\n            output_text = body["output_text"]\n        for item in body.get("output", []) or []:\n            if item.get("type") == "reasoning" and isinstance(item.get("summary"), list) and item["summary"]:\n                reasoning_text = item["summary"][0].get("text", "")\n            elif item.get("type") == "message" and "content" in item:\n                content = item["content"]\n                if isinstance(content, list) and content:\n                    fc = content[0]\n                    if isinstance(fc, dict) and "text" in fc:\n                        output_text = fc["text"]\n                elif isinstance(content, str):\n                    output_text = content\n        if not output_text and reasoning_text:\n            output_text = reasoning_text\n\n        usage = body.get("usage", {}) or {}\n        input_tokens = usage.get("input_tokens", 0)\n        output_tokens = usage.get("output_tokens", 0)\n        reported_cost = usage.get("cost")\n        cost = float(reported_cost) if isinstance(reported_cost, (int, float)) else estimate_call_cost(\n            model, input_tokens, output_tokens\n        )\n        return {\n            "success": True,\n            "response": output_text,\n            "input_tokens": input_tokens,\n            "output_tokens": output_tokens,\n            "cost_usd": cost,\n        }\n\n\nasync def repair_row(\n    session: aiohttp.ClientSession,\n    sem: asyncio.Semaphore,\n    row: dict[str, Any],\n    model_chain: list[str],\n    cost_tracker: CostTracker,\n) -> dict[str, Any]:\n    source = row["input"]\n    hyp = row["output"]\n    qe_score = row["metadata_overall_qe_score"]\n    spans = row["metadata_qe_flagged_spans"] or []\n    spans_to_mask = compute_spans_to_mask(qe_score, spans)\n\n    result: dict[str, Any] = {\n        "row_id": f"{row[\'metadata_doc_id\']}::{row[\'metadata_segment_id\']}::{row[\'metadata_system_id\']}",\n        "lang_pair": row["metadata_language_pair"],\n        "qe_score": qe_score,\n        "n_spans_flagged": len(spans),\n        "n_spans_masked": len(spans_to_mask),\n        "source": hyp,  # pre-edit hypothesis (condition B\'s "before")\n        "source_en": source,\n        "masked_text": None,\n        "repaired_text": hyp,\n        "model_used": None,\n        "n_llm_calls": 0,\n        "call_error": None,\n    }\n\n    if not spans_to_mask:\n        return result  # condition B never touches the sentence when qe_score >= 0.90\n\n    if cost_tracker.over_cap():\n        result["call_error"] = "hard_cost_cap_reached_skipped"\n        return result\n\n    masked_text = apply_masking(hyp, spans_to_mask)\n    result["masked_text"] = masked_text\n    max_tokens = min(1200, max(150, int(len(source.split()) * 3) + 100))\n    prompt = MASKING_PROMPT_TEMPLATE.format(mask_token=MASK_TOKEN, source=source, masked_sentence=masked_text)\n\n    last_error = None\n    async with sem:\n        for model in model_chain:\n            try:\n                r = await call_openrouter(session, model, prompt, max_tokens=max_tokens, temperature=0.0)\n            except Exception as e:\n                last_error = str(e)\n                continue\n            if r.get("success"):\n                await cost_tracker.add(\n                    r.get("cost_usd"),\n                    tool="gen_art_experiment_2_condition_b",\n                    model=model,\n                    row_id=result["row_id"],\n                )\n                result["repaired_text"] = r["response"].strip() or hyp\n                result["model_used"] = model\n                result["n_llm_calls"] = 1\n                return result\n            last_error = r.get("error")\n            logger.warning(f"{model} failed on row {result[\'row_id\']}: {last_error} -- trying next fallback")\n\n    result["call_error"] = last_error\n    logger.error(f"All repair models failed for row {result[\'row_id\']}: {last_error}")\n    return result\n\n\nasync def run_condition_b(\n    rows: list[dict[str, Any]], model_chain: list[str], cost_tracker: CostTracker, concurrency: int\n) -> list[dict[str, Any]]:\n    sem = asyncio.Semaphore(concurrency)\n    connector = aiohttp.TCPConnector(limit=concurrency * 2)\n    async with aiohttp.ClientSession(connector=connector) as session:\n        tasks = [repair_row(session, sem, row, model_chain, cost_tracker) for row in rows]\n        results = []\n        for i, coro in enumerate(asyncio.as_completed(tasks)):\n            res = await coro\n            results.append(res)\n            if (i + 1) % 100 == 0 or (i + 1) == len(tasks):\n                logger.info(\n                    f"Condition B progress: {i + 1}/{len(tasks)} rows, "\n                    f"cumulative cost=${cost_tracker.total_usd:.4f}"\n                )\n    return results'}
```

### [65] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:29 UTC

```
{"new_source": "class CostTracker:\n    def __init__(self, hard_cap: float):\n        self.total_usd = 0.0\n        self.n_calls = 0\n        self.n_failed = 0\n        self.hard_cap = hard_cap\n        self._lock = asyncio.Lock()\n\n    async def add(self, cost_usd: float | None, tool: str, **meta) -> None:\n        async with self._lock:\n            if cost_usd is not None:\n                self.total_usd += cost_usd\n            self.n_calls += 1\n            if AI... [truncated, 42141 chars total]
```

### [66] ASSISTANT · 2026-09-01 11:23:35 UTC

```
Now leakage detection, LLM-judge scorer, gate decision, run pipeline, and results cells.
```

### [67] TOOL CALL — NotebookEdit · 2026-09-01 11:23:35 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '29374105', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Leakage detection\n\nA qualitative failure-signature check mirroring Padmanabhan\'s Appendix B: does the repaired text still contain a surviving placeholder token, a garbled token, or a generic instruction-following artifact (e.g. "Corrected words:", "Here is the revised...")?'}
```

### [68] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:35 UTC

```
{"new_source": "## Leakage detection\n\nA qualitative failure-signature check mirroring Padmanabhan's Appendix B: does the repaired text still contain a surviving placeholder token, a garbled token, or a generic instruction-following artifact (e.g. \"Corrected words:\", \"Here is the revised...\")?", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "c4b5a781", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_g... [truncated, 43532 chars total]
```

### [69] TOOL CALL — NotebookEdit · 2026-09-01 11:23:37 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'c4b5a781', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def detect_leakage(text: str) -> bool:\n    return any(p.search(text) for p in LEAK_PATTERNS)'}
```

### [70] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:37 UTC

```
{"new_source": "def detect_leakage(text: str) -> bool:\n    return any(p.search(text) for p in LEAK_PATTERNS)", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "cb599f76", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"765a351d\",\n  ... [truncated, 43999 chars total]
```

### [71] TOOL CALL — NotebookEdit · 2026-09-01 11:23:43 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'cb599f76', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Quality scorer: LLM-judge proxy (COMET substitute)\n\nThe plan called for `Unbabel/wmt22-cometkiwi-da` with `wmt22-comet-da` as fallback -- both gated HF Hub checkpoints. In the real execution, HuggingFace Hub returned a persistent, account-wide HTTP 429 on every download attempt for both (12 total attempts across a 600s + 180s retry budget), so the script cascaded to this documented non-COMET substitute: an LLM-judge 0-1 adequacy proxy (`openai/gpt-4o-mini`), scored before/after the edit. This notebook skips straight to that same fallback path (the multi-minute COMET retry budget doesn't fit the demo's runtime budget), which is exactly what the real run did anyway.\n\n**The proxy's scale/calibration is NOT comparable to Padmanabhan's ΔCOMET** -- this is called out explicitly in both the original `method_out.json` and here."}
```

### [72] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:43 UTC

```
{"new_source": "## Quality scorer: LLM-judge proxy (COMET substitute)\n\nThe plan called for `Unbabel/wmt22-cometkiwi-da` with `wmt22-comet-da` as fallback -- both gated HF Hub checkpoints. In the real execution, HuggingFace Hub returned a persistent, account-wide HTTP 429 on every download attempt for both (12 total attempts across a 600s + 180s retry budget), so the script cascaded to this documented non-COMET substitute: an LLM-judge 0-1 adequacy proxy (`openai/gpt-... [truncated, 45958 chars total]
```

### [73] TOOL CALL — NotebookEdit · 2026-09-01 11:23:49 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'db8a122f', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'async def judge_quality(session: aiohttp.ClientSession, sem: asyncio.Semaphore, source: str, mt: str) -> float | None:\n    async with sem:\n        try:\n            r = await call_openrouter(session, JUDGE_MODEL, JUDGE_PROMPT.format(source=source, mt=mt), max_tokens=10, temperature=0.0)\n        except Exception:\n            return None\n    if not r.get("success"):\n        return None\n    m = re.search(r"[01](?:\\.\\d+)?|0?\\.\\d+", r["response"])\n    if not m:\n        return None\n    try:\n        return max(0.0, min(1.0, float(m.group(0))))\n    except ValueError:\n        return None\n\n\nasync def run_llm_judge_scoring(\n    pairs: list[tuple[str, str]], concurrency: int, cost_tracker: CostTracker\n) -> list[float | None]:\n    sem = asyncio.Semaphore(concurrency)\n    connector = aiohttp.TCPConnector(limit=concurrency * 2)\n    async with aiohttp.ClientSession(connector=connector) as session:\n        tasks = [judge_quality(session, sem, src, mt) for src, mt in pairs]\n        return list(await asyncio.gather(*tasks))'}
```

### [74] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:49 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [75] ASSISTANT · 2026-09-01 11:23:55 UTC

```
Now the gate decision section.
```

### [76] TOOL CALL — NotebookEdit · 2026-09-01 11:23:55 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '081622d2', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Gate decision\n\nThe three-way verdict: direction (does the quality delta go negative, as Padmanabhan documents?), magnitude (is it roughly in range of the published ΔCOMET -- reported, not solely gating), and leakage (does any non-trivial fraction of masked rows leak masking artifacts?). When the scorer was substituted (as here), the verdict is suffixed `_UNRELIABLE_SUBSTITUTED_SCORER` so the magnitude comparison is never silently trusted.'}
```

### [77] TOOL RESULT — NotebookEdit · 2026-09-01 11:23:55 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [78] TOOL CALL — NotebookEdit · 2026-09-01 11:24:01 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '69a8f71a', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def get_published_delta(lang_pair: str) -> tuple[float, str]:\n    pinned = PUBLISHED_DELTA_COMET.get(lang_pair)\n    if pinned is not None:\n        return pinned, "per_pair_pinned"\n    return PUBLISHED_POOLED_DELTA_COMET, "pooled_fallback"\n\n\ndef compute_gate(\n    per_pair_delta_comet: dict[str, float], per_pair_leakage_rate: dict[str, float], is_real_comet: bool\n) -> dict[str, Any]:\n    direction_by_pair = {p: per_pair_delta_comet[p] < 0 for p in per_pair_delta_comet}\n    gate_passes_direction = all(direction_by_pair.values())\n\n    magnitude_by_pair = {}\n    for p, delta in per_pair_delta_comet.items():\n        published, source = get_published_delta(p)\n        magnitude_by_pair[p] = {\n            "published_delta": published,\n            "published_source": source,\n            "observed_delta": delta,\n            "abs_diff": abs(delta - published),\n            "within_tolerance": abs(delta - published) < MAGNITUDE_TOLERANCE,\n        }\n    gate_passes_magnitude = all(v["within_tolerance"] for v in magnitude_by_pair.values())\n\n    gate_passes_leakage = any(v > 0.0 for v in per_pair_leakage_rate.values())\n\n    verdict = "PASS" if (gate_passes_direction and gate_passes_leakage) else "FAIL"\n    if not is_real_comet:\n        verdict = f"{verdict}_UNRELIABLE_SUBSTITUTED_SCORER"\n\n    return {\n        "verdict": verdict,\n        "gate_component_results": {\n            "direction": {"pass": gate_passes_direction, "by_pair": direction_by_pair},\n            "magnitude": {"pass": gate_passes_magnitude, "by_pair": magnitude_by_pair, "note": "reported, not solely gating per plan"},\n            "leakage": {"pass": gate_passes_leakage, "by_pair": per_pair_leakage_rate},\n        },\n    }'}
```

### [79] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:01 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [80] ASSISTANT · 2026-09-01 11:24:07 UTC

```
Now the "run the pipeline" cells (row selection, run Condition B, leakage, judge scoring, aggregation).
```

### [81] TOOL CALL — NotebookEdit · 2026-09-01 11:24:07 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'e07397cd', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Run the pipeline\n\nThis mirrors `method.py`'s `main()`: build the per-pair row lists (capped by `MAX_ROWS_PER_PAIR`), run Condition B over OpenRouter, detect leakage, score quality before/after with the LLM-judge proxy, and aggregate per-pair and pooled statistics."}
```

### [82] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:07 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [83] TOOL CALL — NotebookEdit · 2026-09-01 11:24:13 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '35b81031', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# Rows already loaded above; equivalent of load_natural_rows() but reading from the loaded `data`\nrows = [\n    e\n    for e in natural["examples"]\n    if e["metadata_language_pair"] in LANG_PAIRS and e["metadata_overall_qe_score"] is not None\n]\n\nby_pair: dict[str, list[dict[str, Any]]] = {}\nfor r in rows:\n    by_pair.setdefault(r["metadata_language_pair"], []).append(r)\nfor p in LANG_PAIRS:\n    by_pair.setdefault(p, [])\n    RNG.shuffle(by_pair[p])\n    by_pair[p] = by_pair[p][:MAX_ROWS_PER_PAIR]\nrows = [r for p in LANG_PAIRS for r in by_pair[p]]\nprint(f"Row counts per pair after capping: { {p: len(by_pair[p]) for p in LANG_PAIRS} }")\n\nload_openrouter_pricing()'}
```

### [84] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:13 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [85] TOOL CALL — NotebookEdit · 2026-09-01 11:24:19 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'c580db1d', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# --- Condition B: run masked-fill baseline over OpenRouter ---\ncost_tracker = CostTracker(hard_cap=HARD_COST_CAP_USD)\nmodel_chain = [REPAIR_MODEL] + REPAIR_MODEL_FALLBACKS\nt0 = time.time()\nresults = asyncio.run(run_condition_b(rows, model_chain, cost_tracker, CONCURRENCY))\nprint(\n    f"Condition B complete: {len(results)} rows in {time.time() - t0:.1f}s, "\n    f"total OpenRouter cost=${cost_tracker.total_usd:.4f} ({cost_tracker.n_calls} calls)"\n)\nmodels_actually_used = Counter(r["model_used"] for r in results if r["model_used"])\nprint(f"Repair models actually used: {dict(models_actually_used)}")\nn_call_errors = sum(1 for r in results if r["call_error"])\nif n_call_errors:\n    print(f"WARNING: {n_call_errors} rows had no successful repair call (kept as untouched hypothesis)")'}
```

### [86] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:19 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [87] TOOL CALL — NotebookEdit · 2026-09-01 11:24:25 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'e6ff1d31', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# --- Leakage detection ---\nfor r in results:\n    r["leaked"] = detect_leakage(r["repaired_text"]) if r["n_spans_masked"] > 0 else False\n\n# --- Quality scoring: LLM-judge proxy (documented COMET substitution, see markdown above) ---\ncomet_model_name = "llm_judge_quality_proxy_v1"\nis_real_comet = False\nprint(f"Scoring with fallback scorer: {comet_model_name}")\njudge_pairs_before = [(r["source_en"], r["source"]) for r in results]\njudge_pairs_after = [(r["source_en"], r["repaired_text"]) for r in results]\nscores_before = asyncio.run(run_llm_judge_scoring(judge_pairs_before, CONCURRENCY, cost_tracker))\nscores_after = asyncio.run(run_llm_judge_scoring(judge_pairs_after, CONCURRENCY, cost_tracker))\nfor r, cb, ca in zip(results, scores_before, scores_after):\n    r["comet_before"] = cb\n    r["comet_after"] = ca\n    r["delta_comet"] = (ca - cb) if (cb is not None and ca is not None) else None\nprint(f"Total OpenRouter cost so far: ${cost_tracker.total_usd:.4f}")'}
```

### [88] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:25 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [89] TOOL CALL — NotebookEdit · 2026-09-01 11:24:35 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'f393bd9e', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# --- Aggregate per-pair / pooled stats ---\nper_pair_results = {}\nfor pair in LANG_PAIRS:\n    pair_rows = [r for r in results if r["lang_pair"] == pair]\n    masked_rows = [r for r in pair_rows if r["n_spans_masked"] > 0]\n    deltas = [r["delta_comet"] for r in pair_rows if r["delta_comet"] is not None]\n    leaked_rows = [r for r in masked_rows if r["leaked"]]\n    per_pair_results[pair] = {\n        "n_rows": len(pair_rows),\n        "n_rows_with_spans_flagged": sum(1 for r in pair_rows if r["n_spans_flagged"] > 0),\n        "n_rows_masked_by_condition_b": len(masked_rows),\n        "n_llm_calls": sum(r["n_llm_calls"] for r in pair_rows),\n        "mean_delta_comet": (sum(deltas) / len(deltas)) if deltas else None,\n        "n_scored": len(deltas),\n        "leakage_rate": (len(leaked_rows) / len(masked_rows)) if masked_rows else 0.0,\n        "n_leaked": len(leaked_rows),\n        "example_leaked_outputs": [\n            {"row_id": r["row_id"], "masked_text": r["masked_text"], "repaired_text": r["repaired_text"]}\n            for r in leaked_rows[:10]\n        ],\n        "example_largest_negative_delta": sorted(\n            [r for r in pair_rows if r["delta_comet"] is not None], key=lambda r: r["delta_comet"]\n        )[:5],\n    }\n\nall_deltas = [r["delta_comet"] for r in results if r["delta_comet"] is not None]\nall_masked = [r for r in results if r["n_spans_masked"] > 0]\nall_leaked = [r for r in all_masked if r["leaked"]]\npooled_mean_delta_comet = (sum(all_deltas) / len(all_deltas)) if all_deltas else None\npooled_leakage_rate = (len(all_leaked) / len(all_masked)) if all_masked else 0.0\n\ngate = compute_gate(\n    {p: per_pair_results[p]["mean_delta_comet"] for p in LANG_PAIRS if per_pair_results[p]["mean_delta_comet"] is not None},\n    {p: per_pair_results[p]["leakage_rate"] for p in LANG_PAIRS},\n    is_real_comet,\n)\nprint(f"GATE VERDICT: {gate[\'verdict\']}")\nprint(f"Pooled mean quality delta (proxy): {pooled_mean_delta_comet}, pooled leakage rate: {pooled_leakage_rate:.3f}")'}
```

### [90] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:36 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [91] ASSISTANT · 2026-09-01 11:24:39 UTC

```
Now the results/visualization cell.
```

### [92] TOOL CALL — NotebookEdit · 2026-09-01 11:24:39 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '12af41b2', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Results\n\nA readable summary table plus a plot of the per-pair quality delta (proxy) and leakage rate, mirroring the `metadata` block of `method_out.json`.'}
```

### [93] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:40 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [94] TOOL CALL — NotebookEdit · 2026-09-01 11:24:49 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': 'c0dd47a5', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'print(f"{\'lang_pair\':<12} {\'n_rows\':>7} {\'n_masked\':>9} {\'n_leaked\':>9} {\'leakage_rate\':>13} {\'mean_Δquality\':>14}")\nfor p in LANG_PAIRS:\n    s = per_pair_results[p]\n    delta_str = f"{s[\'mean_delta_comet\']:.4f}" if s["mean_delta_comet"] is not None else "n/a"\n    print(f"{p:<12} {s[\'n_rows\']:>7} {s[\'n_rows_masked_by_condition_b\']:>9} {s[\'n_leaked\']:>9} {s[\'leakage_rate\']:>13.3f} {delta_str:>14}")\n\nprint(f"\\n{\'POOLED\':<12} {len(results):>7} {len(all_masked):>9} {len(all_leaked):>9} "\n      f"{pooled_leakage_rate:>13.3f} {(pooled_mean_delta_comet if pooled_mean_delta_comet is not None else float(\'nan\')):>14.4f}")\nprint(f"\\nGate verdict: {gate[\'verdict\']}")\nprint(f"Total OpenRouter cost: ${cost_tracker.total_usd:.4f} ({cost_tracker.n_calls} calls)")\nprint(f"Padmanabhan\'s published pooled ΔCOMET: {PUBLISHED_POOLED_DELTA_COMET} (NOT directly comparable -- different scorer)")\n\nfig, axes = plt.subplots(1, 2, figsize=(10, 4))\n\npairs_with_scores = [p for p in LANG_PAIRS if per_pair_results[p]["mean_delta_comet"] is not None]\ndeltas_plot = [per_pair_results[p]["mean_delta_comet"] for p in pairs_with_scores]\ncolors = ["#d62728" if d < 0 else "#2ca02c" for d in deltas_plot]\naxes[0].bar(pairs_with_scores, deltas_plot, color=colors)\naxes[0].axhline(0, color="black", linewidth=0.8)\naxes[0].set_title("Mean quality delta (proxy), by pair")\naxes[0].set_ylabel("after - before (LLM-judge proxy, 0-1 scale)")\n\nleakage_plot = [per_pair_results[p]["leakage_rate"] for p in LANG_PAIRS]\naxes[1].bar(LANG_PAIRS, leakage_plot, color="#ff7f0e")\naxes[1].set_title("Leakage rate, by pair")\naxes[1].set_ylabel("fraction of masked rows leaking artifacts")\naxes[1].set_ylim(0, max(0.1, max(leakage_plot) * 1.3 if leakage_plot else 0.1))\n\nplt.tight_layout()\nplt.show()'}
```

### [95] TOOL RESULT — NotebookEdit · 2026-09-01 11:24:49 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [96] ASSISTANT · 2026-09-01 11:24:55 UTC

```
Now let's test-run the notebook in a clean environment.
```

### [97] TOOL CALL — Bash · 2026-09-01 11:24:55 UTC

```
\
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 && \
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -20 && echo VENV_READY
```

### [98] TOOL RESULT — Bash [ERROR] · 2026-09-01 11:27:53 UTC

```
Error: Exit code 143
Command timed out after 3m 0s
```

### [99] TOOL CALL — Bash · 2026-09-01 11:27:55 UTC

```
rm -rf .nb_env
/usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel && echo VENV_READY
```

### [100] TOOL RESULT — Bash · 2026-09-01 11:27:55 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bqqvuz540"}
```

### [101] ASSISTANT · 2026-09-01 11:27:57 UTC

```
While that installs, let me check the mini_demo_data.json row structure once more and verify pyproject/schema needs for the struct out file.
```

### [102] TOOL CALL — Bash · 2026-09-01 11:27:57 UTC

```
python3 -c "
import json
d = json.load(open('mini_demo_data.json'))
e = d['datasets'][0]['examples'][0]
print(list(e.keys()))
print(e['metadata_overall_qe_score'], e['metadata_language_pair'])
"
ls -la
```

### [103] TOOL RESULT — Bash · 2026-09-01 11:27:57 UTC

```
{"stdout": "['input', 'output', 'metadata_language_pair', 'metadata_domain', 'metadata_qe_flagged_spans', 'metadata_human_error_annotations', 'metadata_provenance', 'metadata_invariant_category', 'metadata_source_dataset', 'metadata_doc_id', 'metadata_segment_id', 'metadata_system_id', 'metadata_overall_qe_score', 'metadata_notes', 'metadata_fold']\n0.6368953585624695 en-zh_CN\ntotal 6516\ndrwxr-xr-x 3 root root 2006834 Sep  1 11:24 .\ndrwxr-xr-x 6 root root 2022517 Sep  1 11:19 ..\ndrwxr-xr-x 4 root root 2006773 Sep  1 11:27 .nb_env\n-rw-r--r-- 1 root root  520623 Sep  1 11:27 .repl_agent.ptylog\n-rw-r--r-- 1 root root   32818 Sep  1 11:24 code_demo.ipynb\n-rw-r--r-- 1 root root   80797 Sep  1 11:20 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [104] ASSISTANT · 2026-09-01 11:28:01 UTC

```
Good, data structure matches what the notebook expects. Let's wait for the venv setup to finish, then execute the notebook.
```

### [105] TOOL CALL — Bash · 2026-09-01 11:28:01 UTC

```
sleep 60; tail -20 /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output
```

### [106] TOOL RESULT — Bash [ERROR] · 2026-09-01 11:28:01 UTC

```
Error: Blocked: sleep 60 followed by: tail -20 /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [107] ASSISTANT · 2026-09-01 11:28:03 UTC

```
I'll wait for the background task notification instead.
```

### [108] TOOL CALL — ScheduleWakeup · 2026-09-01 11:28:03 UTC

```
{'delaySeconds': 90, 'noop': True, 'reason': 'Waiting for venv install background task to finish before running the notebook test.'}
```

### [109] TOOL RESULT — ScheduleWakeup [ERROR] · 2026-09-01 11:28:03 UTC

```
Error: `prompt` is required when `stop` is not true.
```

### [110] TOOL CALL — ToolSearch · 2026-09-01 11:28:07 UTC

```
{'query': 'select:Monitor', 'max_results': 1}
```

### [111] TOOL RESULT — ToolSearch · 2026-09-01 11:28:07 UTC

```
{"matches": ["Monitor"], "query": "select:Monitor", "total_deferred_tools": 22}
```

### [112] TOOL CALL — Monitor · 2026-09-01 11:28:15 UTC

```
{'command': 'until grep -q VENV_READY /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output 2>/dev/null; do sleep 3; done; echo "venv ready"', 'description': 'Waiting for .nb_env pip install to finish', 'timeout_ms': 300000, 'persistent': False}
```

### [113] TOOL RESULT — Monitor · 2026-09-01 11:28:15 UTC

```
{"taskId": "b9yu6n6st", "timeoutMs": 300000, "persistent": false}
```

### [114] ASSISTANT · 2026-09-01 11:28:21 UTC

```
I'll wait for that to finish before running the notebook execution.
```

### [115] TOOL CALL — Bash · 2026-09-01 11:28:21 UTC

```
echo waiting
```

### [116] TOOL RESULT — Bash · 2026-09-01 11:28:21 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [117] TOOL CALL — Bash · 2026-09-01 11:28:23 UTC

```
true
```

### [118] TOOL RESULT — Bash · 2026-09-01 11:28:23 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [119] ASSISTANT · 2026-09-01 11:28:25 UTC

```
I'll pause here and wait for the venv install to finish.
```

### [120] TOOL CALL — Bash · 2026-09-01 11:28:25 UTC

```
true
```

### [121] TOOL RESULT — Bash · 2026-09-01 11:28:25 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [122] ASSISTANT · 2026-09-01 11:28:27 UTC

```
Waiting for the background venv setup to complete before executing the notebook test.
```

### [123] TOOL CALL — Bash · 2026-09-01 11:28:27 UTC

```
true
```

### [124] TOOL RESULT — Bash · 2026-09-01 11:28:28 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [125] ASSISTANT · 2026-09-01 11:28:29 UTC

```
Waiting for background setup — will resume once notified.
```

### [126] SYSTEM-USER prompt · 2026-09-01 11:28:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [127] TOOL CALL — Bash · 2026-09-01 11:28:38 UTC

```
ls -la .nb_env/bin/ 2>/dev/null | head -20; echo "---"; tail -30 /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output 2>/dev/null
```

### [128] TOOL RESULT — Bash · 2026-09-01 11:28:38 UTC

```
{"stdout": "total 2954\ndrwxr-xr-x 2 root root 1001593 Sep  1 11:28 .\ndrwxr-xr-x 7 root root 2002478 Sep  1 11:28 ..\n-rw-r--r-- 1 root root    9033 Sep  1 11:28 Activate.ps1\n-rw-r--r-- 1 root root    2382 Sep  1 11:28 activate\n-rw-r--r-- 1 root root    1030 Sep  1 11:28 activate.csh\n-rw-r--r-- 1 root root    2305 Sep  1 11:28 activate.fish\n-rwxr-xr-x 1 root root     381 Sep  1 11:28 pip\n-rwxr-xr-x 1 root root     381 Sep  1 11:28 pip3\n-rwxr-xr-x 1 root root     381 Sep  1 11:28 pip3.12\nlrwxrwxrwx 1 root root      10 Sep  1 11:28 python -> python3.12\nlrwxrwxrwx 1 root root      10 Sep  1 11:28 python3 -> python3.12\nlrwxrwxrwx 1 root root      25 Sep  1 11:28 python3.12 -> /usr/local/bin/python3.12\n-rwxr-xr-x 1 root root     376 Sep  1 11:28 wsdump\n---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [129] TOOL CALL — Bash · 2026-09-01 11:28:40 UTC

```
ls .nb_env/bin/ | grep -i jupyter; echo "---"; ps aux | grep -i pip | grep -v grep
```

### [130] TOOL RESULT — Bash · 2026-09-01 11:28:40 UTC

```
{"stdout": "---\nroot         261  0.0  0.0   4496  3308 ?        Ss   11:27   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1788261623984-ljxqp3.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'rm -rf .nb_env /usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel && echo VENV_READY' < /dev/null && pwd -P >| /tmp/claude-c759-cwd\nroot         300 15.5  0.0  96808 92156 ?        S    11:28   0:02 /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [131] ASSISTANT · 2026-09-01 11:28:44 UTC

```
It's still installing. Let me wait for it properly this time.
```

### [132] TOOL CALL — Monitor · 2026-09-01 11:28:44 UTC

```
{'command': 'while ps -p 300 > /dev/null 2>&1; do sleep 5; done; echo PIP_DONE; grep -q VENV_READY /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output && echo VENV_READY_CONFIRMED', 'description': 'Waiting for pip install of jupyter/ipykernel to finish', 'timeout_ms': 600000, 'persistent': False}
```

### [133] TOOL RESULT — Monitor · 2026-09-01 11:28:44 UTC

```
{"taskId": "b3jjfq33c", "timeoutMs": 600000, "persistent": false}
```

### [134] ASSISTANT · 2026-09-01 11:28:45 UTC

```
Waiting for the pip install to complete.
```

### [135] SYSTEM-USER prompt · 2026-09-01 11:28:48 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [136] TOOL CALL — Bash · 2026-09-01 11:28:52 UTC

```
ls .nb_env/bin/ | grep -i jupyter; echo "---status---"; ps aux | grep -i "pip install" | grep -v grep; echo "---output---"; cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-VO5kqjjB2Uk5-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-G9ppuk8aHUhW/fc12d7a5-acb0-4b32-a9b7-5049bbc05f42/tasks/bqqvuz540.output 2>/dev/null
```

### [137] TOOL RESULT — Bash · 2026-09-01 11:28:52 UTC

```
{"stdout": "---status---\nroot         261  0.0  0.0   4496  3308 ?        Ss   11:27   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1788261623984-ljxqp3.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'rm -rf .nb_env /usr/local/bin/python3.12 -m venv .nb_env && .nb_env/bin/pip install -q pip jupyter ipykernel && echo VENV_READY' < /dev/null && pwd -P >| /tmp/claude-c759-cwd\nroot         300  9.4  0.0  96808 92164 ?        S    11:28   0:02 /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel\n---output---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [138] TOOL CALL — Bash · 2026-09-01 11:29:00 UTC

```
date; ps -o etimes= -p 300; echo "---"; du -sh .nb_env 2>/dev/null
```

### [139] TOOL RESULT — Bash · 2026-09-01 11:29:00 UTC

```
{"stdout": "Tue Sep  1 11:28:57 UTC 2026\n     34\n---\n276M\t.nb_env", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [140] TOOL CALL — Bash · 2026-09-01 11:29:12 UTC

```
set -e
# wait for the pip install to finish (poll, no long sleeps)
for i in $(seq 1 100); do
  if ! ps -p 300 > /dev/null 2>&1; then break; fi
  sleep 3
done
ls .nb_env/bin/ | grep -i jupyter && echo JUPYTER_INSTALLED
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -100
echo EXEC_DONE
```

### [141] TOOL RESULT — Bash · 2026-09-01 11:35:22 UTC

```
{"stdout": "jupyter\njupyter-builder\njupyter-console\njupyter-dejavu\njupyter-events\njupyter-execute\njupyter-kernel\njupyter-kernelspec\njupyter-lab\njupyter-labextension\njupyter-labhub\njupyter-migrate\njupyter-nbconvert\njupyter-notebook\njupyter-run\njupyter-server\njupyter-troubleshoot\njupyter-trust\nJUPYTER_INSTALLED\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/bin/jupyter-nbconvert\", line 10, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/jupyter_core/application.py\", line 284, in launch_instance\n    super().launch_instance(argv=argv, **kwargs)\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/traitlets/config/application.py\", line 1080, in launch_instance\n    app.start()\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 420, in start\n    self.convert_notebooks()\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 597, in convert_notebooks\n    self.convert_single_notebook(notebook_filename)\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 563, in convert_single_notebook\n    output, resources = self.export_single_notebook(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 487, in export_single_notebook\n    output, resources = self.exporter.from_filename(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 201, in from_filename\n    return self.from_file(f, resources=resources, **kw)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 220, in from_file\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\n# --- Condition B: run masked-fill baseline over OpenRouter ---\ncost_tracker = CostTracker(hard_cap=HARD_COST_CAP_USD)\nmodel_chain = [REPAIR_MODEL] + REPAIR_MODEL_FALLBACKS\nt0 = time.time()\nresults = asyncio.run(run_condition_b(rows, model_chain, cost_tracker, CONCURRENCY))\nprint(\n    f\"Condition B complete: {len(results)} rows in {time.time() - t0:.1f}s, \"\n    f\"total OpenRouter cost=${cost_tracker.total_usd:.4f} ({cost_tracker.n_calls} calls)\"\n)\nmodels_actually_used = Counter(r[\"model_used\"] for r in results if r[\"model_used\"])\nprint(f\"Repair models actually used: {dict(models_actually_used)}\")\nn_call_errors = sum(1 for r in results if r[\"call_error\"])\nif n_call_errors:\n    print(f\"WARNING: {n_call_errors} rows had no successful repair call (kept as untouched hypothesis)\")\n------------------\n\n\n\u001b[31m---------------------------------------------------------------------------\u001b[39m\n\u001b[31mRuntimeError\u001b[39m                              Traceback (most recent call last)\n\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# --- Condition B: run masked-fill baseline over OpenRouter ---\u001b[39;00m\n\u001b[32m      2\u001b[39m cost_tracker = CostTracker(hard_cap=HARD_COST_CAP_USD)\n\u001b[32m      3\u001b[39m model_chain = [REPAIR_MODEL] + REPAIR_MODEL_FALLBACKS\n\u001b[32m      4\u001b[39m t0 = time.time()\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m results = asyncio.run(run_condition_b(rows, model_chain, cost_tracker, CONCURRENCY))\n\u001b[32m      6\u001b[39m print(\n\u001b[32m      7\u001b[39m     f\"Condition B complete: {len(results)} rows in {time.time() - t0:.1f}s, \"\n\u001b[32m      8\u001b[39m     f\"total OpenRouter cost=${cost_tracker.total_usd:.4f} ({cost_tracker.n_calls} calls)\"\n\n\u001b[36mFile \u001b[39m\u001b[32m/usr/local/lib/python3.12/asyncio/runners.py:191\u001b[39m, in \u001b[36mrun\u001b[39m\u001b[34m(main, debug, loop_factory)\u001b[39m\n\u001b[32m    161\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[32m    162\u001b[39m \n\u001b[32m    163\u001b[39m \u001b[33;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m    187\u001b[39m \u001b[33;03m    asyncio.run(main())\u001b[39;00m\n\u001b[32m    188\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    189\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m events._get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m    190\u001b[39m     \u001b[38;5;66;03m# fail fast with short traceback\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m191\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[32m    192\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m    194\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m Runner(debug=debug, loop_factory=loop_factory) \u001b[38;5;28;01mas\u001b[39;00m runner:\n\u001b[32m    195\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m runner.run(main)\n\n\u001b[31mRuntimeError\u001b[39m: asyncio.run() cannot be called from a running event loop\n\nEXEC_DONE", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [142] TOOL CALL — Read · 2026-09-01 11:35:28 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb
```

### [143] TOOL RESULT — Read · 2026-09-01 11:35:28 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Sanity-Check for the Masked-Fill Baseline (Condition B)\n\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental... [truncated, 31671 chars total]
```

### [144] ASSISTANT · 2026-09-01 11:35:34 UTC

```
I'll add `nest_asyncio` to fix the nested event-loop issue in the Jupyter kernel.
```

### [145] TOOL CALL — NotebookEdit · 2026-09-01 11:35:34 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '47eacb5f', 'new_source': "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# aiohttp, tenacity, loguru, nest_asyncio -- NOT pre-installed on Colab, always install.\n# nest_asyncio is needed because both Colab and Jupyter kernels already run an event loop,\n# and the original script's `asyncio.run(...)` calls cannot nest inside one without it.\n_pip('aiohttp==3.14.3')\n_pip('tenacity==9.1.4')\n_pip('loguru==0.7.3')\n_pip('nest_asyncio==1.6.0')\n\n# requests, matplotlib -- pre-installed on Colab, install locally only (to match Colab's env)\nif 'google.colab' not in sys.modules:\n    _pip('requests==2.32.4', 'matplotlib==3.10.0')"}
```

### [146] TOOL RESULT — NotebookEdit · 2026-09-01 11:35:34 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [147] TOOL CALL — NotebookEdit · 2026-09-01 11:35:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '692a0045', 'new_source': "# Original imports from method.py (argparse/resource dropped -- not needed in notebook context)\nfrom __future__ import annotations\n\nimport asyncio\nimport json\nimport os\nimport random\nimport re\nimport time\nfrom collections import Counter\nfrom typing import Any\n\nimport aiohttp\nfrom loguru import logger\nfrom tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential\n\nimport matplotlib.pyplot as plt  # for the results/visualization cell\n\n# Jupyter/Colab kernels already run an event loop, so patch asyncio to allow\n# the original script's `asyncio.run(...)` calls to nest inside it.\nimport nest_asyncio\nnest_asyncio.apply()"}
```

### [148] TOOL RESULT — NotebookEdit · 2026-09-01 11:35:38 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [149] ASSISTANT · 2026-09-01 11:35:44 UTC

```
Now let's re-run the test (venv should still be intact; only need to re-execute since packages are already installed).
```

### [150] TOOL CALL — Bash · 2026-09-01 11:35:44 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -150
echo EXEC_DONE
```

### [151] TOOL RESULT — Bash · 2026-09-01 11:36:22 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 97255 bytes to code_demo.ipynb\nEXEC_DONE", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [152] ASSISTANT · 2026-09-01 11:36:24 UTC

```
It executed successfully. Let's inspect the outputs to verify results look sensible.
```

### [153] TOOL CALL — Bash · 2026-09-01 11:36:24 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(''.join(out['text']))
            elif out.get('output_type') == 'error':
                print('ERROR:', out['ename'], out['evalue'])
        print('---')
"
```

### [154] TOOL RESULT — Bash · 2026-09-01 11:36:24 UTC

```
{"stdout": "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n---\n---\n---\nLoaded 30 rows\nLanguage pairs present: ['en-cs_CZ', 'en-zh_CN']\n\n---\n---\n---\n---\n---\n---\n---\nRow counts per pair after capping: {'en-zh_CN': 2, 'en-cs_CZ': 2}\n\n11:36:14|INFO   |Loaded OpenRouter pricing catalog (420 models)\n\n---\n11:36:16|INFO   |Condition B progress: 4/4 rows, cumulative cost=$0.0001\nCondition B complete: 4 rows in 2.6s, total OpenRouter cost=$0.0001 (4 calls)\nRepair models actually used: {'google/gemma-3-12b-it': 4}\n\n---\nScoring with fallback scorer: llm_judge_quality_proxy_v1\n\nTotal OpenRouter cost so far: $0.0001\n\n---\nGATE VERDICT: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nPooled mean quality delta (proxy): -0.04999999999999999, pooled leakage rate: 0.000\n\n---\nlang_pair     n_rows  n_masked  n_leaked  leakage_rate  mean_Δquality\nen-zh_CN           2         2         0         0.000        -0.1500\nen-cs_CZ           2         2         0         0.000         0.0500\n\nPOOLED             4         4         0         0.000        -0.0500\n\nGate verdict: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nTotal OpenRouter cost: $0.0001 (4 calls)\nPadmanabhan's published pooled ΔCOMET: -0.0108 (NOT directly comparable -- different scorer)\n\n---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [155] TOOL CALL — Bash · 2026-09-01 11:36:32 UTC

```
sed -i 's/^MAX_ROWS_PER_PAIR = 2 /MAX_ROWS_PER_PAIR = 8 /' code_demo.ipynb 2>/dev/null; grep -o '"MAX_ROWS_PER_PAIR = [0-9]*' code_demo.ipynb | head -1
```

### [156] TOOL RESULT — Bash · 2026-09-01 11:36:32 UTC

```
{"stdout": "\"MAX_ROWS_PER_PAIR = 2", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [157] TOOL CALL — NotebookEdit · 2026-09-01 11:36:48 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '764dc8fc', 'new_source': '# --- Tunable parameters (start small, scale up as time/budget allows) ---\nMAX_ROWS_PER_PAIR = 8      # original run used all 779/781 rows per pair; this demo uses a handful (up to 15 -- the size of mini_demo_data.json -- per pair)\nCONCURRENCY = 4            # original default was 16\nSOFT_COST_CAP_USD = 0.50\nHARD_COST_CAP_USD = 0.60\n\n# --- Original module-level config from method.py ---\nOPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")\nOPENROUTER_URL = "https://openrouter.ai/api/v1/responses"\nOPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"\nAII_COST_LEDGER = os.environ.get("AII_COST_LEDGER")\n\nRNG = random.Random(20260901)\n\nLANG_PAIRS = ["en-zh_CN", "en-cs_CZ"]\nREPAIR_MODEL = "google/gemma-3-12b-it"\nREPAIR_MODEL_FALLBACKS = [\n    "qwen/qwen-2.5-7b-instruct",\n    "mistralai/mistral-nemo",\n    "meta-llama/llama-3.1-8b-instruct",\n    "mistralai/ministral-8b-2512",\n]\n\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\n# with WMT25 organizer Table 15 (dossier Block A).\nPUBLISHED_DELTA_COMET = {\n    "en-cs_CZ": -0.00724,\n    "en-zh_CN": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\n}\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\n\n# Masking placeholder (see method.py\'s docstring on prompt provenance).\nMASK_TOKEN = "__BLANK__"\nMASKING_PROMPT_TEMPLATE = """You are repairing a machine-translated sentence. Some words or phrases in the\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\n\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\n\nEnglish source:\n{source}\n\nTranslation with blanks:\n{masked_sentence}\n\nRepaired translation:"""\n\nLEAK_PATTERNS = [\n    re.compile(r"__BLANK__"),\n    re.compile(r"__\\w+__"),\n    re.compile(r"(?i)corrected words?\\s*:"),\n    re.compile(r"(?i)here is the (corrected|fixed|revised)"),\n    re.compile(r"(?i)^(sure|okay|here\'s|here is)\\b"),\n    re.compile(r"\\[MASK\\]|\\[BLANK\\]|<blank>|<mask>", re.IGNORECASE),\n]\n\nJUDGE_MODEL = "openai/gpt-4o-mini"\nJUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\nRespond with ONLY the number, nothing else.\n\nSOURCE (English): {source}\n\nTRANSLATION: {mt}\n\nScore:"""\n\nlogger.remove()\nlogger.add(lambda msg: print(msg, end=""), level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [158] TOOL RESULT — NotebookEdit [ERROR] · 2026-09-01 11:36:48 UTC

```
Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.
```

### [159] TOOL CALL — Read · 2026-09-01 11:36:52 UTC

```
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb
```

### [160] TOOL RESULT — Read · 2026-09-01 11:36:52 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Sanity-Check for the Masked-Fill Baseline (Condition B)\n\nThis notebook is a lightly-annotated, cell-split version of `method.py`, which reproduces Padmanabhan (2025)'s **SURREYPAI-S2 masked-fill baseline (Condition B)** on WMT25 Task 3 `experimental... [truncated, 35769 chars total]
```

### [161] ASSISTANT · 2026-09-01 11:36:56 UTC

```
Now let's update MAX_ROWS_PER_PAIR to 8.
```

### [162] TOOL CALL — Edit · 2026-09-01 11:36:56 UTC

```
File: /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb
OLD: MAX_ROWS_PER_PAIR = 2      # original run used all 779/781 rows per pair; this demo uses a handful
NEW: MAX_ROWS_PER_PAIR = 8      # original run used all 779/781 rows per pair; this demo uses a handful
```

### [163] TOOL RESULT — Edit [ERROR] · 2026-09-01 11:36:56 UTC

```
Error: File is a Jupyter Notebook. Use the NotebookEdit to edit this file.
```

### [164] TOOL CALL — NotebookEdit · 2026-09-01 11:37:10 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '764dc8fc', 'new_source': '# --- Tunable parameters (start small, scale up as time/budget allows) ---\nMAX_ROWS_PER_PAIR = 8      # original run used all 779/781 rows per pair; this demo uses a handful (up to 15 -- the size of mini_demo_data.json -- per pair)\nCONCURRENCY = 4            # original default was 16\nSOFT_COST_CAP_USD = 0.50\nHARD_COST_CAP_USD = 0.60\n\n# --- Original module-level config from method.py ---\nOPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")\nOPENROUTER_URL = "https://openrouter.ai/api/v1/responses"\nOPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"\nAII_COST_LEDGER = os.environ.get("AII_COST_LEDGER")\n\nRNG = random.Random(20260901)\n\nLANG_PAIRS = ["en-zh_CN", "en-cs_CZ"]\nREPAIR_MODEL = "google/gemma-3-12b-it"\nREPAIR_MODEL_FALLBACKS = [\n    "qwen/qwen-2.5-7b-instruct",\n    "mistralai/mistral-nemo",\n    "meta-llama/llama-3.1-8b-instruct",\n    "mistralai/ministral-8b-2512",\n]\n\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\n# with WMT25 organizer Table 15 (dossier Block A).\nPUBLISHED_DELTA_COMET = {\n    "en-cs_CZ": -0.00724,\n    "en-zh_CN": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\n}\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\n\n# Masking placeholder (see method.py\'s docstring on prompt provenance).\nMASK_TOKEN = "__BLANK__"\nMASKING_PROMPT_TEMPLATE = """You are repairing a machine-translated sentence. Some words or phrases in the\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\n\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\n\nEnglish source:\n{source}\n\nTranslation with blanks:\n{masked_sentence}\n\nRepaired translation:"""\n\nLEAK_PATTERNS = [\n    re.compile(r"__BLANK__"),\n    re.compile(r"__\\w+__"),\n    re.compile(r"(?i)corrected words?\\s*:"),\n    re.compile(r"(?i)here is the (corrected|fixed|revised)"),\n    re.compile(r"(?i)^(sure|okay|here\'s|here is)\\b"),\n    re.compile(r"\\[MASK\\]|\\[BLANK\\]|<blank>|<mask>", re.IGNORECASE),\n]\n\nJUDGE_MODEL = "openai/gpt-4o-mini"\nJUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\nRespond with ONLY the number, nothing else.\n\nSOURCE (English): {source}\n\nTRANSLATION: {mt}\n\nScore:"""\n\nlogger.remove()\nlogger.add(lambda msg: print(msg, end=""), level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [165] TOOL RESULT — NotebookEdit · 2026-09-01 11:37:10 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [166] ASSISTANT · 2026-09-01 11:37:16 UTC

```
Now re-run the test with the scaled-up value.
```

### [167] TOOL CALL — Bash · 2026-09-01 11:37:16 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -80
echo EXEC_DONE
```

### [168] TOOL RESULT — Bash · 2026-09-01 11:38:04 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 94939 bytes to code_demo.ipynb\nEXEC_DONE", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [169] TOOL CALL — Bash · 2026-09-01 11:38:06 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(''.join(out['text']))
            elif out.get('output_type') == 'error':
                print('ERROR:', out['ename'], out['evalue'])
"
```

### [170] TOOL RESULT — Bash · 2026-09-01 11:38:06 UTC

```
{"stdout": "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\nLoaded 30 rows\nLanguage pairs present: ['en-cs_CZ', 'en-zh_CN']\n\nRow counts per pair after capping: {'en-zh_CN': 8, 'en-cs_CZ': 8}\n\n11:37:46|INFO   |Loaded OpenRouter pricing catalog (420 models)\n\n11:37:52|INFO   |Condition B progress: 16/16 rows, cumulative cost=$0.0004\nCondition B complete: 16 rows in 5.8s, total OpenRouter cost=$0.0004 (16 calls)\nRepair models actually used: {'google/gemma-3-12b-it': 16}\n\nScoring with fallback scorer: llm_judge_quality_proxy_v1\n\nTotal OpenRouter cost so far: $0.0004\n\nGATE VERDICT: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nPooled mean quality delta (proxy): -0.10625, pooled leakage rate: 0.000\n\nlang_pair     n_rows  n_masked  n_leaked  leakage_rate  mean_Δquality\nen-zh_CN           8         8         0         0.000        -0.1625\nen-cs_CZ           8         8         0         0.000        -0.0500\n\nPOOLED            16        16         0         0.000        -0.1062\n\nGate verdict: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nTotal OpenRouter cost: $0.0004 (16 calls)\nPadmanabhan's published pooled ΔCOMET: -0.0108 (NOT directly comparable -- different scorer)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [171] TOOL CALL — NotebookEdit · 2026-09-01 11:38:24 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_G9ppuk8aHUhW/code_demo.ipynb', 'cell_id': '764dc8fc', 'new_source': '# --- Tunable parameters (start small, scale up as time/budget allows) ---\nMAX_ROWS_PER_PAIR = 15     # original run used all 779/781 rows per pair; this demo uses the full 15-per-pair mini_demo_data.json\nCONCURRENCY = 8            # original default was 16\nSOFT_COST_CAP_USD = 0.50\nHARD_COST_CAP_USD = 0.60\n\n# --- Original module-level config from method.py ---\nOPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")\nOPENROUTER_URL = "https://openrouter.ai/api/v1/responses"\nOPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"\nAII_COST_LEDGER = os.environ.get("AII_COST_LEDGER")\n\nRNG = random.Random(20260901)\n\nLANG_PAIRS = ["en-zh_CN", "en-cs_CZ"]\nREPAIR_MODEL = "google/gemma-3-12b-it"\nREPAIR_MODEL_FALLBACKS = [\n    "qwen/qwen-2.5-7b-instruct",\n    "mistralai/mistral-nemo",\n    "meta-llama/llama-3.1-8b-instruct",\n    "mistralai/ministral-8b-2512",\n]\n\n# Padmanabhan (2025) Table 3 self-reported per-language ΔCOMET, reconciled\n# with WMT25 organizer Table 15 (dossier Block A).\nPUBLISHED_DELTA_COMET = {\n    "en-cs_CZ": -0.00724,\n    "en-zh_CN": None,  # no per-pair figure in the dossier -> use pooled/range fallback below\n}\nPUBLISHED_POOLED_DELTA_COMET = -0.0108\nPUBLISHED_PER_PAIR_RANGE = (-0.014, -0.007)  # (min, max) across the 6 WMT25 pairs, dossier Block A\nMAGNITUDE_TOLERANCE = 0.02  # rough-magnitude tolerance, reported not gating alone (plan spec)\n\n# Masking placeholder (see method.py\'s docstring on prompt provenance).\nMASK_TOKEN = "__BLANK__"\nMASKING_PROMPT_TEMPLATE = """You are repairing a machine-translated sentence. Some words or phrases in the\ntranslation below were flagged as likely errors and have been replaced with the placeholder token {mask_token}.\n\nUsing the original English source sentence for reference, replace every occurrence of {mask_token} in the\ntranslation with the correct words so the translation is fluent and faithful to the source. Preserve every part\nof the translation that is NOT a {mask_token} exactly as given -- do not paraphrase, do not add commentary, do not\nexplain your edits, and do not add any markup. Output ONLY the fully repaired translation sentence, nothing else.\n\nEnglish source:\n{source}\n\nTranslation with blanks:\n{masked_sentence}\n\nRepaired translation:"""\n\nLEAK_PATTERNS = [\n    re.compile(r"__BLANK__"),\n    re.compile(r"__\\w+__"),\n    re.compile(r"(?i)corrected words?\\s*:"),\n    re.compile(r"(?i)here is the (corrected|fixed|revised)"),\n    re.compile(r"(?i)^(sure|okay|here\'s|here is)\\b"),\n    re.compile(r"\\[MASK\\]|\\[BLANK\\]|<blank>|<mask>", re.IGNORECASE),\n]\n\nJUDGE_MODEL = "openai/gpt-4o-mini"\nJUDGE_PROMPT = """Rate how adequately the TRANSLATION conveys the meaning of the SOURCE sentence, on a\ncontinuous 0.0-1.0 scale (1.0 = perfectly faithful and fluent, 0.0 = unintelligible or unrelated).\nRespond with ONLY the number, nothing else.\n\nSOURCE (English): {source}\n\nTRANSLATION: {mt}\n\nScore:"""\n\nlogger.remove()\nlogger.add(lambda msg: print(msg, end=""), level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [172] TOOL RESULT — NotebookEdit · 2026-09-01 11:38:24 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [173] TOOL CALL — Bash · 2026-09-01 11:38:28 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -40
echo EXEC_DONE
```

### [174] TOOL RESULT — Bash · 2026-09-01 11:39:16 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 93134 bytes to code_demo.ipynb\nEXEC_DONE", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [175] TOOL CALL — Bash · 2026-09-01 11:39:18 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(''.join(out['text']))
            elif out.get('output_type') == 'error':
                print('ERROR:', out['ename'], out['evalue'])
"
```

### [176] TOOL RESULT — Bash · 2026-09-01 11:39:18 UTC

```
{"stdout": "\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\nLoaded 30 rows\nLanguage pairs present: ['en-cs_CZ', 'en-zh_CN']\n\nRow counts per pair after capping: {'en-zh_CN': 15, 'en-cs_CZ': 15}\n\n11:38:59|INFO   |Loaded OpenRouter pricing catalog (420 models)\n\n11:39:05|INFO   |Condition B progress: 30/30 rows, cumulative cost=$0.0008\nCondition B complete: 30 rows in 5.8s, total OpenRouter cost=$0.0008 (30 calls)\nRepair models actually used: {'google/gemma-3-12b-it': 30}\n\nScoring with fallback scorer: llm_judge_quality_proxy_v1\n\nTotal OpenRouter cost so far: $0.0008\n\nGATE VERDICT: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nPooled mean quality delta (proxy): -0.10666666666666667, pooled leakage rate: 0.000\n\nlang_pair     n_rows  n_masked  n_leaked  leakage_rate  mean_Δquality\nen-zh_CN          15        15         0         0.000        -0.0867\nen-cs_CZ          15        15         0         0.000        -0.1267\n\nPOOLED            30        30         0         0.000        -0.1067\n\nGate verdict: FAIL_UNRELIABLE_SUBSTITUTED_SCORER\nTotal OpenRouter cost: $0.0008 (30 calls)\nPadmanabhan's published pooled ΔCOMET: -0.0108 (NOT directly comparable -- different scorer)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [177] TOOL CALL — Bash · 2026-09-01 11:39:28 UTC

```
grep -o 'GITHUB_DATA_URL = "[^"]*"' code_demo.ipynb
ls -la mini_demo_data.json code_demo.ipynb
rm -rf .nb_env
echo CLEANED
```

### [178] TOOL RESULT — Bash · 2026-09-01 11:39:40 UTC

```
{"stdout": "-rw-r--r-- 1 root root 93141 Sep  1 11:39 code_demo.ipynb\n-rw-r--r-- 1 root root 80797 Sep  1 11:20 mini_demo_data.json\nCLEANED", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [179] TOOL CALL — Bash · 2026-09-01 11:39:44 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for cell in nb['cells']:
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if 'GITHUB_DATA_URL' in src:
        for line in src.split(chr(10)):
            if 'GITHUB_DATA_URL' in line:
                print(repr(line))
"
```

### [180] TOOL RESULT — Bash · 2026-09-01 11:39:44 UTC

```
{"stdout": "'GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-e9bf19-isolating-what-fixes-failed-span-editing/main/round-2/experiment-2/demo/mini_demo_data.json\"'\n'        with urllib.request.urlopen(GITHUB_DATA_URL) as response:'", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [181] ASSISTANT · 2026-09-01 11:39:46 UTC

```
Matches exactly. All verification checks pass. Now let's write the required struct output file.
```

### [182] TOOL CALL — Bash · 2026-09-01 11:39:46 UTC

```
cat > .terminal_claude_agent_struct_out.json << 'EOF'
{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
EOF
cat .terminal_claude_agent_struct_out.json
ls -la
```

### [183] TOOL RESULT — Bash · 2026-09-01 11:39:46 UTC

```
{"stdout": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\ntotal 6180\ndrwxr-xr-x 2 root root 2000126 Sep  1 11:39 .\ndrwxr-xr-x 6 root root 3000202 Sep  1 11:19 ..\n-rw-r--r-- 1 root root    9667 Sep  1 11:39 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 root root 1142439 Sep  1 11:39 .repl_agent.ptylog\n-rw-r--r-- 1 root root     113 Sep  1 11:39 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root   93141 Sep  1 11:39 code_demo.ipynb\n-rw-r--r-- 1 root root   80797 Sep  1 11:20 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [184] ASSISTANT · 2026-09-01 11:39:51 UTC

```
The demo notebook and data file are complete and verified:

- **`mini_demo_data.json`** — 30 curated rows (15 per language pair: `en-zh_CN`, `en-cs_CZ`) from `wmt25_task3_natural`, all drawn from the QE band where Condition B's masking rule actually fires.
- **`code_demo.ipynb`** — a cell-split, minimally-annotated version of `method.py`: setup → data loading (GitHub URL with local fallback) → config → Algorithm 1 masking rule → OpenRouter async client → leakage detection → LLM-judge quality-proxy scoring (the same COMET substitution the real run used) → gate decision → pipeline run → results table + matplotlib visualization.

Tested end-to-end in a clean venv simulating Colab: real OpenRouter calls against all 30 rows complete in ~6s, producing a real gate verdict (`FAIL_UNRELIABLE_SUBSTITUTED_SCORER`, with both language pairs showing the negative quality delta direction Padmanabhan documents). `.terminal_claude_agent_struct_out.json` has been written.
```
