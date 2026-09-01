# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 5 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 10:28:15 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: Rescue Condition C's Missing Quality Score
summary: >-
  Scoring-only rerun over Condition C's already-generated 320 natural-row repair outputs: attempt real wmt22-cometkiwi-da
  with genuinely new HF-429 mitigations (mirror endpoint, resumable download, widely-spaced retry windows, full attempt logging);
  if it still fails, fall back to the EXACT same LLM-judge proxy configuration used for Condition B's fidelity check, re-scoring
  B's own rows with that identical proxy in the same run so the output reports a same-proxy B-vs-C comparison rather than
  an isolated, incomparable number. No new repair generation and no new repair-model calls; this only scores text that already
  exists.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # --- Phase 0: locate inputs (no new generation) ---
  # The direction names two upstream artifacts by id that are NOT in this plan's formal
  # depends_on (only the dataset art_mhfmDpGp4z1J and the resource dossier art_5ySTX4YfxqG_
  # are). They are prior-iteration artifacts in the SAME run and must be located on disk:
  RUN_ROOT = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5'
  def find_artifact_dir(short_id):
      # short_id e.g. '6n9zJVKWXnio' or 'G9ppuk8aHUhW' (the part after 'art_')
      # search every iter_*/gen_art*/gen_art_*/ for a dir or meta file whose artifact id matches
      candidates = glob(f'{RUN_ROOT}/**/full_method_out.json', recursive=True) + \
                   glob(f'{RUN_ROOT}/**/method_out.json', recursive=True)
      matches = [c for c in candidates if short_id in read_meta_near(c).get('artifact_id','')]
      if not matches: matches = [c for c in candidates if short_id in c]  # path-based fallback
      assert matches, f'BLOCKING: could not locate artifact art_{short_id} on disk'
      return matches[0]

  condition_c_path = find_artifact_dir('6n9zJVKWXnio')   # full_method_out.json for Condition C (560 rows total)
  condition_b_path = find_artifact_dir('G9ppuk8aHUhW')   # Condition B artifact incl. its fidelity-check proxy config/code

  condition_c_rows = json.load(open(condition_c_path))
  natural_c_rows = [r for r in condition_c_rows if r['metadata_fold_or_source'] == 'wmt25_task3_natural']
  assert len(natural_c_rows) == 320, f'expected 320 natural rows, got {len(natural_c_rows)}'
  # each row must carry: source_text, pre_repair_text (or original MT hyp), post_repair_text, language_pair, row_id

  condition_b_artifact = load_artifact_bundle(condition_b_path)  # includes its .py source and full_method_out.json
  b_fidelity_config = extract_fidelity_check_config(condition_b_artifact)
  # b_fidelity_config MUST capture, verbatim from B's own code/prompt file:
  #   - the exact OpenRouter model id used as judge
  #   - the exact system/user prompt template (before/after adequacy scoring)
  #   - the exact numeric scoring convention (scale, direction, aggregation)
  #   - temperature / sampling params
  # If b_fidelity_config cannot be extracted verbatim (code missing/renamed), STOP and
  # record a blocking finding rather than inventing a proxy config from memory.
  natural_b_rows = [r for r in load_json(f'{condition_b_path}/../full_method_out.json')
                    if r['metadata_fold_or_source'] == 'wmt25_task3_natural']
  assert len(natural_b_rows) == 320

  # --- Phase 1: mitigated real-COMET attempt (time-boxed to first ~3.0h of the 6h budget) ---
  attempts_log = []  # list of {timestamp, endpoint, mode, http_status, error, elapsed_s}

  def try_comet_download(endpoint, resumable=True, timeout_s=900):
      t0 = now()
      try:
          os.environ['HF_HUB_ENDPOINT'] = endpoint
          # resumable=True relies on huggingface_hub's default etag/local-dir cache behavior:
          # a partial prior attempt's blob is kept under HF cache and resumed, not discarded
          path = huggingface_hub.snapshot_download(
              repo_id='Unbabel/wmt22-cometkiwi-da',
              local_dir='./hf_cache/wmt22-cometkiwi-da',
              resume_download=resumable,
              etag_timeout=30,
          )
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'SUCCESS', 'elapsed_s': now()-t0})
          return path
      except HfHubHTTPError as e:
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': e.response.status_code,
                                'error': str(e), 'elapsed_s': now()-t0})
          return None
      except Exception as e:
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'EXC', 'error': repr(e), 'elapsed_s': now()-t0})
          return None

  # Genuinely new mitigations vs. the prior two failed attempts:
  # (a) an alternate mirror endpoint, (b) attempts spread ACROSS SEPARATE WINDOWS with real
  #     wall-clock gaps (not back-to-back exponential backoff within one process lifetime),
  #     so a per-minute or per-hour 429 window is actually crossed.
  ENDPOINTS = ['https://huggingface.co', 'https://hf-mirror.com']
  WINDOW_OFFSETS_MIN = [0, 25, 75, 165]   # 4 windows inside a ~3h cap, deliberately spread
  comet_checkpoint_path = None
  for offset_min in WINDOW_OFFSETS_MIN:
      sleep_until(run_start_time + offset_min * 60)
      for endpoint in ENDPOINTS:
          comet_checkpoint_path = try_comet_download(endpoint)
          if comet_checkpoint_path:
              break
      if comet_checkpoint_path:
          break
      if elapsed_since(run_start_time) > 3.0 * 3600:
          break  # hard stop: leave >=2.5h for fallback scoring + writeup, no matter what

  real_comet_available = comet_checkpoint_path is not None

  # --- Phase 2a: REAL-COMET path ---
  if real_comet_available:
      from comet import load_from_checkpoint
      model = load_from_checkpoint(comet_checkpoint_path)
      def comet_score(rows, text_field):
          data = [{'src': r['source_text'], 'mt': r[text_field]} for r in rows]
          out = model.predict(data, batch_size=64, gpus=1)
          return out['scores']
      pre_scores  = comet_score(natural_c_rows, 'pre_repair_text')
      post_scores = comet_score(natural_c_rows, 'post_repair_text')
      delta_comet_c = [post - pre for pre, post in zip(pre_scores, post_scores)]
      result = {
          'quality_metric_path_taken': 'real_wmt22_cometkiwi_da',
          'attempts_log': attempts_log,
          'condition_c_delta_comet_natural_pooled_mean': mean(delta_comet_c),
          'condition_c_delta_comet_natural_per_row': delta_comet_c,
          'condition_c_delta_comet_by_language_pair': groupby_mean(natural_c_rows, delta_comet_c, key='language_pair'),
          'directly_comparable_to_C1_C2_real_comet_numbers': True,
          'bootstrap_ci_delta_comet': paired_bootstrap_ci(delta_comet_c, n_boot=10000),
      }

  # --- Phase 2b: FALLBACK path -- same proxy as Condition B, re-scoring BOTH B and C ---
  else:
      def proxy_score_pair(source_text, candidate_text, cfg):
          # cfg = b_fidelity_config: same model id, same prompt template, same convention
          prompt = cfg['prompt_template'].format(source=source_text, candidate=candidate_text)
          resp = openrouter_call(model=cfg['model_id'], prompt=prompt,
                                  temperature=cfg['temperature'], system=cfg.get('system'))
          return parse_score(resp, convention=cfg['scoring_convention'])

      cumulative_cost_usd = 0.0
      COST_CAP = 9.0  # hard stop below the $10 ceiling to leave margin

      def scored_delta(rows, cfg):
          nonlocal cumulative_cost_usd
          deltas = []
          for r in rows:
              if cumulative_cost_usd > COST_CAP:
                  raise BudgetExceeded(cumulative_cost_usd)
              pre = proxy_score_pair(r['source_text'], r['pre_repair_text'], cfg)
              post = proxy_score_pair(r['source_text'], r['post_repair_text'], cfg)
              cumulative_cost_usd += estimate_cost(cfg['model_id'], 2)  # 2 calls this row
              deltas.append(post - pre)
          return deltas

      delta_proxy_b = scored_delta(natural_b_rows, b_fidelity_config)   # RE-score B, same run, same proxy
      delta_proxy_c = scored_delta(natural_c_rows, b_fidelity_config)   # score C with IDENTICAL config

      paired_bc = bootstrap_paired_difference(delta_proxy_c, delta_proxy_b, n_boot=10000)
      result = {
          'quality_metric_path_taken': 'llm_judge_proxy_fallback_identical_to_condition_B',
          'attempts_log': attempts_log,
          'proxy_config_used': b_fidelity_config,
          'condition_b_proxy_delta_pooled_mean_natural_rerun': mean(delta_proxy_b),
          'condition_c_proxy_delta_pooled_mean_natural': mean(delta_proxy_c),
          'condition_c_minus_condition_b_proxy_delta_paired_bootstrap_ci': paired_bc,
          'cumulative_openrouter_cost_usd': cumulative_cost_usd,
          'directly_comparable_to_C1_C2_real_comet_numbers': False,
          'directly_comparable_to': 'Condition B, same-proxy, same-run rescoring only',
          'explicit_caveat': (
              'Real wmt22-cometkiwi-da was unreachable after mitigated attempts across '
              f'{len(WINDOW_OFFSETS_MIN)} time-separated windows and {len(ENDPOINTS)} endpoints '
              '(see attempts_log). This number is an LLM-judge proxy, identical in model/prompt/'
              'convention to Condition B\'s fidelity check, and must NOT be treated as numerically '
              'comparable to C1 or C2\'s real-COMET \u0394COMET figures.'
          ),
      }

  # --- Phase 3: write output, validate schema ---
  result['schema_version'] = 'exp_eval... (use aii-json to validate against the repo experiment output schema)'
  write_json('method_out.json', result)
  run_aii_json_validation('method_out.json')
fallback_plan: |-
  Layered fallbacks, in order of what can go wrong:
  1. If art_6n9zJVKWXnio or art_G9ppuk8aHUhW cannot be located anywhere under the run directory tree (renamed, moved, or genuinely absent), do NOT reconstruct their contents from the hypothesis text or fabricate row-level data. Instead write method_out.json with quality_metric_path_taken='blocked_missing_upstream_artifact', list every glob pattern tried, and stop -- this is a real data-availability finding worth reporting, not a excuse to skip validation.
  2. If Condition B's fidelity-check proxy config cannot be extracted verbatim from art_G9ppuk8aHUhW's own code (e.g. the prompt was inlined ad hoc and not saved as a reusable template), reconstruct it as literally as possible from that artifact's method_out.json plus any saved prompt/log fields, and explicitly flag reconstructed_from_partial_evidence=true in the output rather than silently presenting it as identical.
  3. If the real COMET checkpoint download succeeds but model.predict() fails at inference time (OOM, CUDA driver mismatch, corrupted partial download despite a 200 on manifest fetch), fall back immediately to CPU inference (gpus=0) before giving up on the real-metric path entirely -- 640 segments is small enough that CPU COMET inference (no throughput benchmark exists per the resource dossier, but architecture is a small XLM-R encoder) is very likely to finish within the remaining time budget even if slow.
  4. If the mirror endpoint (hf-mirror.com or any other reachable HF mirror discovered during Phase 1) also 429s or is unreachable entirely (DNS failure, org-blocked), record that explicitly as its own attempts_log entries -- a mirror being blocked is itself informative and should not be silently conflated with the primary endpoint's 429s.
  5. If even the proxy fallback blows past the $9 internal cost cap partway through (e.g., a pricier judge model than expected), stop scoring immediately, report partial results for however many rows completed under budget with n reported honestly (not padded or extrapolated), and mark condition_b_proxy_delta and condition_c_proxy_delta as PARTIAL with the exact n scored.
  6. If OpenRouter itself returns errors for the judge model (deprecated/delisted, mirroring the TowerPlus-9B and gemma-2-9b-it delisting pattern already seen twice in this project), re-verify the model id is still live via the aii-openrouter-llms skill's model search before assuming a transient error; if it is genuinely gone, use the resource dossier's or aii-openrouter-llms search to pick the closest still-available substitute, and flag this explicitly as a SECOND-DEGREE proxy deviation from B's original config (not silently swapped in).
testing_plan: |-
  1. Dry-run the artifact-location logic first, standalone: confirm find_artifact_dir resolves to real, readable files for both art_6n9zJVKWXnio and art_G9ppuk8aHUhW, and print the row counts and a sample row's keys from each before doing anything else -- this is the single most likely blocking failure and must be confirmed in the first few minutes, not discovered after burning time on COMET mitigation.
  2. Test the COMET download mitigation logic on a 2-minute time budget first (WINDOW_OFFSETS_MIN=[0] only, one endpoint) purely to confirm the retry/logging code runs without exceptions and produces a well-formed attempts_log entry, before committing to the full multi-hour spread -- this catches code bugs (wrong repo_id, wrong local_dir permissions, huggingface_hub API signature mismatch across versions) cheaply.
  3. Before running the full 320-row proxy fallback (which costs real OpenRouter money), test proxy_score_pair on exactly 3 hand-picked rows from Condition B's natural set and manually inspect the parsed scores against what B's own original fidelity-check output reports for those same rows if row-level scores are still available in art_G9ppuk8aHUhW's output -- if the reconstructed config produces materially different scores on rows B already scored, the config was not extracted correctly and must be fixed before spending on all 320+320 rows.
  4. Confirm cost estimation is realistic: after the 3-row test, compute actual OpenRouter spend from the API response's reported usage and extrapolate to 640 rows x 2 calls before greenlighting the full run; abort and pick a cheaper judge model if extrapolated cost would exceed the $9 cap.
  5. Only after both the artifact-location and small-scale proxy tests pass, run the full Phase 1 mitigation window schedule and, depending on its outcome, the full Phase 2a or 2b scoring pass; validate the final method_out.json with the aii-json skill before declaring done.
  6. Sanity-check the final numbers against known bounds regardless of which path was taken: COMET/proxy deltas should be small (roughly in [-1, 1] for a 0-1-scaled metric, or in whatever bounded range the chosen proxy's convention defines) -- a wildly out-of-range mean signals a parsing bug in parse_score(), not a real finding, and should be caught before reporting.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-09-01 10:28:15 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-python · 2026-09-01 10:28:19 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-09-01 10:28:19 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: "Scales an experiment or evaluation up in stages — mini, 10, 50, 100, 200, then the largest run that fits — recording runtime at each step and extrapolating time-per-example against the remaining time budget before growing further, with background execution and hard RLIMIT_AS and RLIMIT_CPU caps. ALWAYS read before launching any script expected to run for many minutes or hours over a dataset. Triggers: long-running job, overnight or unattended run, time budget, how many examples fit, extrapolate runtime, start small then scale up, run in background and poll, avoid a timeout, full-dataset evaluation, resource limits. NOT for choosing the concurrency mechanism itself (aii-parallel-computing), measuring the machine's CPU, RAM or GPU (aii-use-hardware), or provisioning cloud pods (aii-runpod)."
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-09-01 10:28:23 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-09-01 10:28:23 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: "Detects the CPU, RAM, GPU and VRAM actually available — cgroup v1 and v2 container quotas and CPU affinity rather than misleading host values — then sets RAM and VRAM budgets via resource.setrlimit and torch.cuda.set_per_process_memory_fraction so a script raises a catchable error instead of being OOM-killed, and picks the right torch wheel for the detected device. ALWAYS read before loading a large dataset, installing torch, or sizing batches and worker counts. Triggers: how much RAM or CPU or GPU is available, container memory limit, cgroup, OOM killed, MemoryError, os.cpu_count reports host cores, nproc, VRAM, CUDA available, CPU-only torch build, dataset too big for memory, chunking. NOT for spreading work across that hardware once measured (aii-parallel-computing), staged scale-up runs against a time budget (aii-long-running-tasks), or renting cloud machines (aii-runpod)."
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [7] SKILL-INPUT — aii-parallel-computing · 2026-09-01 10:28:23 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "Parallelises compute-heavy Python: asyncio with aiohttp and a bounded Semaphore for I/O-bound work, ProcessPoolExecutor under the spawn start method for CPU-bound work, NumPy vectorisation and batched PyTorch on GPU with an out-of-memory halving fallback. ALWAYS read before writing any script that loops over data, issues many API calls, downloads many files, or runs heavy computation — sequential loops are the default failure mode. Triggers: parallelise, make a slow script faster, concurrency, async, aiohttp, asyncio.gather, semaphore, multiprocessing, ProcessPoolExecutor, fork deadlock with loguru, worker count, batch size, CUDA out of memory, idle GPU, retries and rate limits. NOT for detecting what hardware exists or setting RAM and VRAM budgets (aii-use-hardware), staged scale-up against a time budget (aii-long-running-tasks), or provisioning cloud pods (aii-runpod)."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [8] SYSTEM-USER prompt · 2026-09-01 10:42:48 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_5/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx1
type: experiment
title: Rescue Condition C's Missing Quality Score
summary: >-
  Scoring-only rerun over Condition C's already-generated 320 natural-row repair outputs: attempt real wmt22-cometkiwi-da
  with genuinely new HF-429 mitigations (mirror endpoint, resumable download, widely-spaced retry windows, full attempt logging);
  if it still fails, fall back to the EXACT same LLM-judge proxy configuration used for Condition B's fidelity check, re-scoring
  B's own rows with that identical proxy in the same run so the output reports a same-proxy B-vs-C comparison rather than
  an isolated, incomparable number. No new repair generation and no new repair-model calls; this only scores text that already
  exists.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # --- Phase 0: locate inputs (no new generation) ---
  # The direction names two upstream artifacts by id that are NOT in this plan's formal
  # depends_on (only the dataset art_mhfmDpGp4z1J and the resource dossier art_5ySTX4YfxqG_
  # are). They are prior-iteration artifacts in the SAME run and must be located on disk:
  RUN_ROOT = '/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5'
  def find_artifact_dir(short_id):
      # short_id e.g. '6n9zJVKWXnio' or 'G9ppuk8aHUhW' (the part after 'art_')
      # search every iter_*/gen_art*/gen_art_*/ for a dir or meta file whose artifact id matches
      candidates = glob(f'{RUN_ROOT}/**/full_method_out.json', recursive=True) + \
                   glob(f'{RUN_ROOT}/**/method_out.json', recursive=True)
      matches = [c for c in candidates if short_id in read_meta_near(c).get('artifact_id','')]
      if not matches: matches = [c for c in candidates if short_id in c]  # path-based fallback
      assert matches, f'BLOCKING: could not locate artifact art_{short_id} on disk'
      return matches[0]

  condition_c_path = find_artifact_dir('6n9zJVKWXnio')   # full_method_out.json for Condition C (560 rows total)
  condition_b_path = find_artifact_dir('G9ppuk8aHUhW')   # Condition B artifact incl. its fidelity-check proxy config/code

  condition_c_rows = json.load(open(condition_c_path))
  natural_c_rows = [r for r in condition_c_rows if r['metadata_fold_or_source'] == 'wmt25_task3_natural']
  assert len(natural_c_rows) == 320, f'expected 320 natural rows, got {len(natural_c_rows)}'
  # each row must carry: source_text, pre_repair_text (or original MT hyp), post_repair_text, language_pair, row_id

  condition_b_artifact = load_artifact_bundle(condition_b_path)  # includes its .py source and full_method_out.json
  b_fidelity_config = extract_fidelity_check_config(condition_b_artifact)
  # b_fidelity_config MUST capture, verbatim from B's own code/prompt file:
  #   - the exact OpenRouter model id used as judge
  #   - the exact system/user prompt template (before/after adequacy scoring)
  #   - the exact numeric scoring convention (scale, direction, aggregation)
  #   - temperature / sampling params
  # If b_fidelity_config cannot be extracted verbatim (code missing/renamed), STOP and
  # record a blocking finding rather than inventing a proxy config from memory.
  natural_b_rows = [r for r in load_json(f'{condition_b_path}/../full_method_out.json')
                    if r['metadata_fold_or_source'] == 'wmt25_task3_natural']
  assert len(natural_b_rows) == 320

  # --- Phase 1: mitigated real-COMET attempt (time-boxed to first ~3.0h of the 6h budget) ---
  attempts_log = []  # list of {timestamp, endpoint, mode, http_status, error, elapsed_s}

  def try_comet_download(endpoint, resumable=True, timeout_s=900):
      t0 = now()
      try:
          os.environ['HF_HUB_ENDPOINT'] = endpoint
          # resumable=True relies on huggingface_hub's default etag/local-dir cache behavior:
          # a partial prior attempt's blob is kept under HF cache and resumed, not discarded
          path = huggingface_hub.snapshot_download(
              repo_id='Unbabel/wmt22-cometkiwi-da',
              local_dir='./hf_cache/wmt22-cometkiwi-da',
              resume_download=resumable,
              etag_timeout=30,
          )
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'SUCCESS', 'elapsed_s': now()-t0})
          return path
      except HfHubHTTPError as e:
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': e.response.status_code,
                                'error': str(e), 'elapsed_s': now()-t0})
          return None
      except Exception as e:
          attempts_log.append({'ts': t0, 'endpoint': endpoint, 'status': 'EXC', 'error': repr(e), 'elapsed_s': now()-t0})
          return None

  # Genuinely new mitigations vs. the prior two failed attempts:
  # (a) an alternate mirror endpoint, (b) attempts spread ACROSS SEPARATE WINDOWS with real
  #     wall-clock gaps (not back-to-back exponential backoff within one process lifetime),
  #     so a per-minute or per-hour 429 window is actually crossed.
  ENDPOINTS = ['https://huggingface.co', 'https://hf-mirror.com']
  WINDOW_OFFSETS_MIN = [0, 25, 75, 165]   # 4 windows inside a ~3h cap, deliberately spread
  comet_checkpoint_path = None
  for offset_min in WINDOW_OFFSETS_MIN:
      sleep_until(run_start_time + offset_min * 60)
      for endpoint in ENDPOINTS:
          comet_checkpoint_path = try_comet_download(endpoint)
          if comet_checkpoint_path:
              break
      if comet_checkpoint_path:
          break
      if elapsed_since(run_start_time) > 3.0 * 3600:
          break  # hard stop: leave >=2.5h for fallback scoring + writeup, no matter what

  real_comet_available = comet_checkpoint_path is not None

  # --- Phase 2a: REAL-COMET path ---
  if real_comet_available:
      from comet import load_from_checkpoint
      model = load_from_checkpoint(comet_checkpoint_path)
      def comet_score(rows, text_field):
          data = [{'src': r['source_text'], 'mt': r[text_field]} for r in rows]
          out = model.predict(data, batch_size=64, gpus=1)
          return out['scores']
      pre_scores  = comet_score(natural_c_rows, 'pre_repair_text')
      post_scores = comet_score(natural_c_rows, 'post_repair_text')
      delta_comet_c = [post - pre for pre, post in zip(pre_scores, post_scores)]
      result = {
          'quality_metric_path_taken': 'real_wmt22_cometkiwi_da',
          'attempts_log': attempts_log,
          'condition_c_delta_comet_natural_pooled_mean': mean(delta_comet_c),
          'condition_c_delta_comet_natural_per_row': delta_comet_c,
          'condition_c_delta_comet_by_language_pair': groupby_mean(natural_c_rows, delta_comet_c, key='language_pair'),
          'directly_comparable_to_C1_C2_real_comet_numbers': True,
          'bootstrap_ci_delta_comet': paired_bootstrap_ci(delta_comet_c, n_boot=10000),
      }

  # --- Phase 2b: FALLBACK path -- same proxy as Condition B, re-scoring BOTH B and C ---
  else:
      def proxy_score_pair(source_text, candidate_text, cfg):
          # cfg = b_fidelity_config: same model id, same prompt template, same convention
          prompt = cfg['prompt_template'].format(source=source_text, candidate=candidate_text)
          resp = openrouter_call(model=cfg['model_id'], prompt=prompt,
                                  temperature=cfg['temperature'], system=cfg.get('system'))
          return parse_score(resp, convention=cfg['scoring_convention'])

      cumulative_cost_usd = 0.0
      COST_CAP = 9.0  # hard stop below the $10 ceiling to leave margin

      def scored_delta(rows, cfg):
          nonlocal cumulative_cost_usd
          deltas = []
          for r in rows:
              if cumulative_cost_usd > COST_CAP:
                  raise BudgetExceeded(cumulative_cost_usd)
              pre = proxy_score_pair(r['source_text'], r['pre_repair_text'], cfg)
              post = proxy_score_pair(r['source_text'], r['post_repair_text'], cfg)
              cumulative_cost_usd += estimate_cost(cfg['model_id'], 2)  # 2 calls this row
              deltas.append(post - pre)
          return deltas

      delta_proxy_b = scored_delta(natural_b_rows, b_fidelity_config)   # RE-score B, same run, same proxy
      delta_proxy_c = scored_delta(natural_c_rows, b_fidelity_config)   # score C with IDENTICAL config

      paired_bc = bootstrap_paired_difference(delta_proxy_c, delta_proxy_b, n_boot=10000)
      result = {
          'quality_metric_path_taken': 'llm_judge_proxy_fallback_identical_to_condition_B',
          'attempts_log': attempts_log,
          'proxy_config_used': b_fidelity_config,
          'condition_b_proxy_delta_pooled_mean_natural_rerun': mean(delta_proxy_b),
          'condition_c_proxy_delta_pooled_mean_natural': mean(delta_proxy_c),
          'condition_c_minus_condition_b_proxy_delta_paired_bootstrap_ci': paired_bc,
          'cumulative_openrouter_cost_usd': cumulative_cost_usd,
          'directly_comparable_to_C1_C2_real_comet_numbers': False,
          'directly_comparable_to': 'Condition B, same-proxy, same-run rescoring only',
          'explicit_caveat': (
              'Real wmt22-cometkiwi-da was unreachable after mitigated attempts across '
              f'{len(WINDOW_OFFSETS_MIN)} time-separated windows and {len(ENDPOINTS)} endpoints '
              '(see attempts_log). This number is an LLM-judge proxy, identical in model/prompt/'
              'convention to Condition B\'s fidelity check, and must NOT be treated as numerically '
              'comparable to C1 or C2\'s real-COMET \u0394COMET figures.'
          ),
      }

  # --- Phase 3: write output, validate schema ---
  result['schema_version'] = 'exp_eval... (use aii-json to validate against the repo experiment output schema)'
  write_json('method_out.json', result)
  run_aii_json_validation('method_out.json')
fallback_plan: |-
  Layered fallbacks, in order of what can go wrong:
  1. If art_6n9zJVKWXnio or art_G9ppuk8aHUhW cannot be located anywhere under the run directory tree (renamed, moved, or genuinely absent), do NOT reconstruct their contents from the hypothesis text or fabricate row-level data. Instead write method_out.json with quality_metric_path_taken='blocked_missing_upstream_artifact', list every glob pattern tried, and stop -- this is a real data-availability finding worth reporting, not a excuse to skip validation.
  2. If Condition B's fidelity-check proxy config cannot be extracted verbatim from art_G9ppuk8aHUhW's own code (e.g. the prompt was inlined ad hoc and not saved as a reusable template), reconstruct it as literally as possible from that artifact's method_out.json plus any saved prompt/log fields, and explicitly flag reconstructed_from_partial_evidence=true in the output rather than silently presenting it as identical.
  3. If the real COMET checkpoint download succeeds but model.predict() fails at inference time (OOM, CUDA driver mismatch, corrupted partial download despite a 200 on manifest fetch), fall back immediately to CPU inference (gpus=0) before giving up on the real-metric path entirely -- 640 segments is small enough that CPU COMET inference (no throughput benchmark exists per the resource dossier, but architecture is a small XLM-R encoder) is very likely to finish within the remaining time budget even if slow.
  4. If the mirror endpoint (hf-mirror.com or any other reachable HF mirror discovered during Phase 1) also 429s or is unreachable entirely (DNS failure, org-blocked), record that explicitly as its own attempts_log entries -- a mirror being blocked is itself informative and should not be silently conflated with the primary endpoint's 429s.
  5. If even the proxy fallback blows past the $9 internal cost cap partway through (e.g., a pricier judge model than expected), stop scoring immediately, report partial results for however many rows completed under budget with n reported honestly (not padded or extrapolated), and mark condition_b_proxy_delta and condition_c_proxy_delta as PARTIAL with the exact n scored.
  6. If OpenRouter itself returns errors for the judge model (deprecated/delisted, mirroring the TowerPlus-9B and gemma-2-9b-it delisting pattern already seen twice in this project), re-verify the model id is still live via the aii-openrouter-llms skill's model search before assuming a transient error; if it is genuinely gone, use the resource dossier's or aii-openrouter-llms search to pick the closest still-available substitute, and flag this explicitly as a SECOND-DEGREE proxy deviation from B's original config (not silently swapped in).
testing_plan: |-
  1. Dry-run the artifact-location logic first, standalone: confirm find_artifact_dir resolves to real, readable files for both art_6n9zJVKWXnio and art_G9ppuk8aHUhW, and print the row counts and a sample row's keys from each before doing anything else -- this is the single most likely blocking failure and must be confirmed in the first few minutes, not discovered after burning time on COMET mitigation.
  2. Test the COMET download mitigation logic on a 2-minute time budget first (WINDOW_OFFSETS_MIN=[0] only, one endpoint) purely to confirm the retry/logging code runs without exceptions and produces a well-formed attempts_log entry, before committing to the full multi-hour spread -- this catches code bugs (wrong repo_id, wrong local_dir permissions, huggingface_hub API signature mismatch across versions) cheaply.
  3. Before running the full 320-row proxy fallback (which costs real OpenRouter money), test proxy_score_pair on exactly 3 hand-picked rows from Condition B's natural set and manually inspect the parsed scores against what B's own original fidelity-check output reports for those same rows if row-level scores are still available in art_G9ppuk8aHUhW's output -- if the reconstructed config produces materially different scores on rows B already scored, the config was not extracted correctly and must be fixed before spending on all 320+320 rows.
  4. Confirm cost estimation is realistic: after the 3-row test, compute actual OpenRouter spend from the API response's reported usage and extrapolate to 640 rows x 2 calls before greenlighting the full run; abort and pick a cheaper judge model if extrapolated cost would exceed the $9 cap.
  5. Only after both the artifact-location and small-scale proxy tests pass, run the full Phase 1 mitigation window schedule and, depending on its outcome, the full Phase 2a or 2b scoring pass; validate the final method_out.json with the aii-json skill before declaring done.
  6. Sanity-check the final numbers against known bounds regardless of which path was taken: COMET/proxy deltas should be small (roughly in [-1, 1] for a 0-1-scaled metric, or in whatever bounded range the chosen proxy's convention defines) -- a wildly out-of-range mean signals a parsing bug in parse_score(), not a real finding, and should be caught before reporting.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
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
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [9] SKILL-INPUT — aii-file-size-limit · 2026-09-01 10:42:52 UTC

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

### [10] SYSTEM-USER prompt · 2026-09-01 10:43:38 UTC

```
<CRITICAL_ERROR>
Some files in your workspace exceed the 100MB size limit for GitHub deployment.

OVERSIZED FILES:
  - hf_cache/wmt22-cometkiwi-da/checkpoints/model.ckpt (2156.0 MB)

You MUST reduce these files to under 100MB each. Use ONE of these strategies:

=== STRATEGY 1: SPLIT FILES (PREFERRED) ===
Split large files into smaller parts and update code to read them sequentially.

For data files (JSON, JSONL, CSV, Parquet):
1. Split the file into parts under 100MB each:
   - data.jsonl -> data_part_001.jsonl, data_part_002.jsonl, ...
2. Update ALL code that reads this file to handle the split parts
3. Delete the original large file after splitting

=== STRATEGY 2: COMPRESSION (FALLBACK) ===
Only use if splitting is not feasible (e.g., binary files, model weights).

1. Compress the file with gzip
2. Update ALL code to decompress before use
3. Delete the original uncompressed file

=== REQUIRED: UPDATE AND TEST CODE ===
After applying your chosen strategy, you MUST:

1. Find ALL code files that reference the modified files (use grep/search)
2. Update each file to work with the new format (split parts or compressed)
3. Run the updated code to verify it still works correctly
4. Fix any errors that occur until the code runs successfully

Do NOT skip testing - the code must actually execute without errors.

Start by listing the oversized files with `ls -lh`, then apply the appropriate strategy.
</CRITICAL_ERROR>
```
