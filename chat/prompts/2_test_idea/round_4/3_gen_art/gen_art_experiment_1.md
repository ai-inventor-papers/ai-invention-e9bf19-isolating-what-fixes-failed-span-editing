# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 4 · `gen_art`
> Run: `run_VO5kqjjB2Uk5` — When Repair Levers Combine, Machine Translation Editing Gets Worse
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-09-01 09:24:27 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
title: Run Combined Fix Condition, This Time Robustly
summary: >-
  Execute Condition C (checker-broadened localization + iterative repair-and-reverify) on the exact B/D/C1/C2 row population,
  repair model, and checker, wrapped in incremental-write, timeout/retry, heartbeat, and resume instrumentation specifically
  designed to survive or diagnose the silent hour-long stall that killed the prior attempt. Score identically to C2 (per-row
  ΔCOMET, fix rate, true regression rate, edit volume, call counts) so C1/C2/C become a directly comparable triple.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # === SETUP (reuse verbatim from art_K8koUmGFDlLN, the completed C2 artifact) ===
  # 1. Load population: 320 natural rows (wmt25_task3_natural, metadata_fold=='experimental_pool')
  #    + 240 injected-pool rows (injected_error_augmentation, metadata_fold=='experimental_pool',
  #    subsampled/stratified exactly as C2 did -- read C2's row-selection code and its logged
  #    row-id list from method_out.json / a saved row_ids.json, and diff against a fresh load
  #    of full_data_out.json to assert IDENTICAL row IDs before running anything. If C2's
  #    artifact did not persist row IDs explicitly, treat any drift as a hard blocker: log it
  #    and use C2's exact stratification code path, not a re-derivation, since re-deriving from
  #    a random seed alone is not verifiably identical.
  # 2. Load the deterministic content-invariant checker module unmodified from C1/C2 (NER +
  #    number/unit/date regex + negation cue lists + quantifier word lists), and the same
  #    within-experiment 8-cell usability/gating table C1/C2 used to decide which
  #    (language_pair, category) cells the checker is trusted to repair-gate on. Do NOT re-derive
  #    or re-tune the checker; import it.
  # 3. Repair model: google/gemma-3-12b-it via OpenRouter, matching B/D/C1/C2 exactly (same
  #    temperature/decoding params -- copy them verbatim from C2's method.py, do not re-guess).
  # 4. Config constants:
  #    MAX_PASSES = 3          # matches C2's iteration budget
  #    CALL_TIMEOUT_S = 75      # hard per-call timeout (60-90s range)
  #    MAX_RETRIES = 3          # exponential backoff: 2s, 8s, 20s
  #    HEARTBEAT_EVERY_S = 30   # watchdog log interval
  #    OUT_JSONL = 'condition_c_progress.jsonl'   # append-only, one line per completed (row, pass)
  #    RESUME = os.path.exists(OUT_JSONL)

  # === ROBUSTNESS WRAPPER (new this iteration -- the actual point of this artifact) ===
  async def call_with_timeout_and_retry(prompt, row_id, pass_num):
      for attempt in range(MAX_RETRIES):
          try:
              t0 = time.monotonic()
              result = await asyncio.wait_for(
                  openrouter_client.complete(model='google/gemma-3-12b-it', prompt=prompt),
                  timeout=CALL_TIMEOUT_S)
              log_call_cost(row_id, pass_num, result.usage, time.monotonic()-t0)
              return result
          except asyncio.TimeoutError:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} TIMEOUT after {CALL_TIMEOUT_S}s')
              await asyncio.sleep(2 * (4 ** attempt))  # 2s, 8s, 32s
          except Exception as e:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} ERROR {type(e).__name__}: {e}')
              await asyncio.sleep(2 * (4 ** attempt))
      logger.error(f'row={row_id} pass={pass_num} EXHAUSTED {MAX_RETRIES} retries -- marking row FAILED, continuing')
      return None  # caller must treat None as a hard per-row failure, log it, and move on -- never block the sweep on one row

  def load_completed_rows(jsonl_path):
      # RESUME: read every already-written line, build a set of (row_id) that reached a
      # terminal state (certificate OR pass-budget exhausted OR hard-failed), skip them entirely
      completed = {}
      if os.path.exists(jsonl_path):
          for line in open(jsonl_path):
              rec = json.loads(line)
              completed[rec['row_id']] = rec
      logger.info(f'resume: {len(completed)} rows already complete, skipping')
      return completed

  async def heartbeat_task(state):
      while not state['done']:
          logger.info(f"HEARTBEAT rows_done={state['rows_done']}/{state['total']} "
                      f"last_progress_ts={state['last_progress_ts']} "
                      f"elapsed_since_last_progress={time.monotonic()-state['last_progress_ts']:.0f}s")
          await asyncio.sleep(HEARTBEAT_EVERY_S)

  # === CONDITION C CORE LOGIC (C1's localization + C2's iterate-and-reverify) ===
  async def run_condition_c_on_row(row, checker, state):
      if row['row_id'] in completed_rows:
          return completed_rows[row['row_id']]  # resume short-circuit
      text = row['hypothesis_or_target']
      edit_log = []
      for pass_num in range(1, MAX_PASSES + 1):
          # C1-style broadened localization: re-run the checker on the CURRENT text every pass,
          # gated by the within-experiment usability table (same gate C1/C2 used)
          violations = checker.find_all_violations(row['source'], text, usability_table)
          if not violations:
              record = {'row_id': row['row_id'], 'status': 'certificate', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          repair_prompt = build_repair_prompt(row['source'], text, violations)  # same template as C1/C2
          result = await call_with_timeout_and_retry(repair_prompt, row['row_id'], pass_num)
          if result is None:
              record = {'row_id': row['row_id'], 'status': 'hard_failed_at_pass', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          text = extract_repaired_text(result)
          edit_log.append({'pass': pass_num, 'violations_targeted': violations, 'output': text,
                            'usage': result.usage})
      else:
          record = {'row_id': row['row_id'], 'status': 'budget_exhausted', 'final_pass': MAX_PASSES,
                     'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
      # INCREMENTAL WRITE: append this row's terminal record to disk THE INSTANT it completes,
      # never batched, so a stall anywhere loses at most one in-flight row
      with open(OUT_JSONL, 'a') as f:
          f.write(json.dumps(record) + '\n')
          f.flush(); os.fsync(f.fileno())
      state['rows_done'] += 1
      state['last_progress_ts'] = time.monotonic()
      return record

  async def main():
      completed_rows = load_completed_rows(OUT_JSONL)
      all_rows = natural_rows_320 + injected_rows_240   # exact same 560-row union as C1/C2
      remaining = [r for r in all_rows if r['row_id'] not in completed_rows]
      logger.info(f'{len(remaining)} rows remaining of {len(all_rows)} total')
      state = {'rows_done': len(completed_rows), 'total': len(all_rows), 'done': False,
               'last_progress_ts': time.monotonic()}
      hb = asyncio.create_task(heartbeat_task(state))
      sem = asyncio.Semaphore(8)  # bounded concurrency, matches C2's OpenRouter client config
      async def bounded(row):
          async with sem:
              return await run_condition_c_on_row(row, checker, state)
      await asyncio.gather(*[bounded(r) for r in remaining])
      state['done'] = True
      await hb

  # === PILOT COST PROBE (before committing to full run, same $2 methodology as C2) ===
  # Run main() restricted to a fixed 20-row pilot subset (10 natural + 10 injected, stratified
  # across language pairs). Measure: wall-clock for 20 rows, $ spent (sum of result.usage costs),
  # extrapolate to 560 rows. If extrapolated cost > $2, stop and re-budget before the full run
  # (reference point: C2's actual full-run spend was $0.045, so >$2 for a comparable condition
  # is itself a red flag worth investigating, not just paying).

  # === SCORING (run only after the full 560-row sweep in condition_c_progress.jsonl is complete
  #     or explicitly declared partial) ===
  # 1. Load condition_c_progress.jsonl, split back into natural (320) vs injected-pool (240) by row_id.
  # 2. ΔCOMET: score final_text vs source/reference for all 320 natural rows using the real
  #    wmt22-cometkiwi-da checkpoint (same install/checkpoint path as B/D/C1/C2 -- read from the
  #    resource dossier art_5ySTX4YfxqG_ if the exact checkpoint path/env is not obvious from C2's
  #    code). PERSIST PER-ROW ΔCOMET (not just the pooled mean) explicitly so a downstream
  #    evaluation artifact can run a true paired bootstrap against C1's and C2's per-row ΔCOMET
  #    arrays, rather than reusing C1-vs-C2's documented normal-approximation substitute.
  # 3. Fix rate / true regression rate: on the 240 injected-pool rows, compare each row's
  #    final_text against its known ground-truth original_span/corrupted_span using the SAME
  #    scoring function C1/C2 used (import it, do not reimplement). Report:
  #      - overall fix rate, overall true regression rate
  #      - broken out by invariant category (entity/number/negation/quantifier)
  #      - pooled INCLUDING negation-deletion rows and pooled EXCLUDING them (both numbers,
  #        matching C1/C2's reporting convention) -- log the negation-attemptability flag PER ROW
  #        (condition C's checker-based localization CAN attempt negation rows, unlike B/D/C2's
  #        oracle-span localization, so this is a genuinely new number, not a copy of C2's)
  # 4. Edit volume: token-level diff size between original hypothesis and final_text, per pass
  #    and cumulative; flag any row whose final edit distance approaches full-sentence rewrite
  #    (>80% of tokens changed) as a possible full-retranslation collapse.
  # 5. LLM calls per sentence: mean/median n_calls across all 560 rows, compare directly to B/D
  #    (1 call), C1 (1 call per violation), C2 (up to 3 calls).
  # 6. Write method_out.json with: per-row arrays for all above metrics, pooled summary stats with
  #    95% CIs (paired bootstrap where a shared population with C1/C2 exists), completion_fraction
  #    field (1.0 if all 560 rows reached a terminal state, else the actual fraction), and an
  #    explicit per-language-pair breakdown table.
fallback_plan: |-
  1. TIMEOUT/HANG RECURRENCE (the exact prior failure mode): the heartbeat log makes a stall diagnosable within HEARTBEAT_EVERY_S=30s instead of after an hour of silence -- if rows_done stops advancing for more than ~5 minutes despite the semaphore having in-flight slots, kill the process (PID-based, per process_isolation rules), inspect the last heartbeat and the last few JSONL lines to identify which row_id(s) were in flight, and restart: RESUME logic in load_completed_rows() means the restart skips every already-terminal row and only retries what was truly in-flight, so no work is lost. If the SAME row_id hangs again on restart, that specific row is the culprit (not general infra) -- log it, skip it with a 'poison_row' status, and continue the sweep; do not let one row block the other 559.
  2. WALL-CLOCK BUDGET EXCEEDED even with robustness measures: if the full 560-row sweep has not reached completion_fraction=1.0 after a generous cap (e.g. 2x the pilot-extrapolated wall-clock, or 90 minutes, whichever is larger), stop the sweep, run the scoring step on whatever rows ARE in condition_c_progress.jsonl, and write method_out.json with completion_fraction < 1.0 explicitly set, plus a per-language-pair breakdown showing which pairs are under-represented in the partial sample -- per the direction's explicit partial-report fallback. Do not silently pad missing rows with any placeholder value.
  3. COST OVERRUN: if the pilot 20-row probe extrapolates to more than $2, first check whether MAX_PASSES=3 combined with C1-style per-sentence multi-violation repair (more violations found per sentence than C2's single-span repair) is driving more calls than expected -- this is a real, expected cost increase over C2 relative to C1's flat 1-call/violation, not necessarily a bug. If it still exceeds the shared $10 ceiling headroom (checking C1+C2's prior spend first), reduce MAX_PASSES to 2 for the full run and note the deviation from C2's budget in method_out.json, rather than skip the condition entirely.
  4. ROW-ID MISMATCH against C1/C2: if C2's exact 560-row population cannot be reconstructed byte-for-byte (e.g. C2 did not persist row IDs), fall back to re-deriving the population using C2's documented stratification code path with the SAME random seed, and explicitly flag in method_out.json that population identity is asserted-by-code-reuse rather than verified-by-row-ID-diff, so downstream evaluation knows the strength of the comparability claim.
  5. CHECKER/REPAIR-MODEL API FAILURE (OpenRouter outage, not a single hung call): if MAX_RETRIES is exhausted on a majority of rows in the pilot probe (not just one poison row), treat this as an upstream outage, pause, and retry the pilot after a delay before committing to the full sweep -- do not burn the full budget against a broken endpoint.
  6. If google/gemma-3-12b-it itself becomes unavailable on OpenRouter (mirroring the TowerPlus-9B delisting that forced this model choice in the first place), the resource dossier's re-ranked substitute table (art_5ySTX4YfxqG_) names the next candidate -- switch to it, note the deviation explicitly (this would break the fixed-repair-model-across-conditions design B/D/C1/C2/C rely on for comparability), and flag this prominently rather than silently swapping models.
testing_plan: |-
  1. DRY RUN ON 3 ROWS FIRST (before the 20-row pilot): pick 3 rows by hand (1 natural, 2 injected with clean single-violation cases) and run the full per-row loop synchronously with verbose logging. Manually inspect: does checker.find_all_violations() return a sensible violation list against the current pass's text (not the original), does the repair prompt look correct, does extract_repaired_text() correctly parse gemma-3-12b-it's output format (check for the same leaked-format issues B/D had to guard against -- gemma may format repairs differently than TowerPlus-9B did), does the JSONL line get written and is it valid JSON, does a certificate correctly trigger early-exit before MAX_PASSES.
  2. INSTRUMENTATION UNIT TEST: deliberately inject an artificial 90-second sleep into ONE mocked OpenRouter call (bypassing the real API) to confirm the CALL_TIMEOUT_S=75s timeout actually fires, the retry/backoff sequence logs correctly, and after MAX_RETRIES the row is marked hard-failed and the sweep continues past it rather than hanging -- this is the single most important test given what killed the prior attempt, so it must be verified BEFORE the full sweep, not inferred from the code reading correctly.
  3. RESUME TEST: run the 3-row dry run to completion, then re-invoke main() with the same OUT_JSONL present -- confirm load_completed_rows() correctly skips all 3 and logs 'resume: 3 rows already complete', proving resumability actually works before relying on it during a real stall recovery.
  4. 20-ROW PILOT (cost + timing probe, matches C2's $2 methodology): run the full pipeline (not mocked) on 20 stratified rows, record actual wall-clock and actual $ spent from OpenRouter usage fields, extrapolate linearly to 560 rows, and confirm the extrapolate stays under the shared $10 ceiling with C2's $0.045 as a sanity reference (a Condition-C extrapolate of low-single-digit-dollars is expected and fine; anything approaching $2+ warrants investigating why before scaling up, per the fallback plan).
  5. SANITY-CHECK PILOT RESULTS AGAINST C1/C2 BEFORE THE FULL RUN: on the 20 pilot rows, compute fix rate and ΔCOMET-direction (not full COMET, just spot-check whether repaired text looks more or less faithful than input) and confirm it is broadly consistent with C1/C2's established ranges (fix rate somewhere between C1's 0.6056 and C2's ~0.99, since C combines both mechanisms) -- if the pilot shows fix rate near 0 or wildly outside this envelope, stop and debug the repair/checker integration rather than scaling a broken pipeline to 560 rows.
  6. FULL SWEEP with heartbeat monitoring: launch the 560-row run as a background process per process_isolation rules (PID-tracked, never grep-by-name), tail the log for heartbeat lines to confirm steady rows_done progress every ~30s, and only proceed to scoring once completion_fraction reaches 1.0 or the wall-clock fallback cap is hit.
  7. POST-HOC VALIDATION: after scoring, confirm the output row counts match expectations exactly (320 natural + 240 injected = 560 total records in condition_c_progress.jsonl, no duplicates by row_id, no missing row_ids relative to the input population minus any explicitly-logged hard-failures), and confirm per-row ΔCOMET array length equals 320 exactly before treating the paired-bootstrap capability as available downstream.
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

### [2] HUMAN-USER prompt · 2026-09-01 09:24:27 UTC

```
AI in translation emwrging opportunities
```

### [3] SKILL-INPUT — aii-python · 2026-09-01 09:24:31 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-09-01 09:24:31 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-09-01 09:24:31 UTC

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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-09-01 09:24:31 UTC

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

### [7] SKILL-INPUT — aii-use-hardware · 2026-09-01 09:24:31 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-09-01 09:24:31 UTC

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

### [9] SYSTEM-USER prompt · 2026-09-01 09:44:50 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
title: Run Combined Fix Condition, This Time Robustly
summary: >-
  Execute Condition C (checker-broadened localization + iterative repair-and-reverify) on the exact B/D/C1/C2 row population,
  repair model, and checker, wrapped in incremental-write, timeout/retry, heartbeat, and resume instrumentation specifically
  designed to survive or diagnose the silent hour-long stall that killed the prior attempt. Score identically to C2 (per-row
  ΔCOMET, fix rate, true regression rate, edit volume, call counts) so C1/C2/C become a directly comparable triple.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # === SETUP (reuse verbatim from art_K8koUmGFDlLN, the completed C2 artifact) ===
  # 1. Load population: 320 natural rows (wmt25_task3_natural, metadata_fold=='experimental_pool')
  #    + 240 injected-pool rows (injected_error_augmentation, metadata_fold=='experimental_pool',
  #    subsampled/stratified exactly as C2 did -- read C2's row-selection code and its logged
  #    row-id list from method_out.json / a saved row_ids.json, and diff against a fresh load
  #    of full_data_out.json to assert IDENTICAL row IDs before running anything. If C2's
  #    artifact did not persist row IDs explicitly, treat any drift as a hard blocker: log it
  #    and use C2's exact stratification code path, not a re-derivation, since re-deriving from
  #    a random seed alone is not verifiably identical.
  # 2. Load the deterministic content-invariant checker module unmodified from C1/C2 (NER +
  #    number/unit/date regex + negation cue lists + quantifier word lists), and the same
  #    within-experiment 8-cell usability/gating table C1/C2 used to decide which
  #    (language_pair, category) cells the checker is trusted to repair-gate on. Do NOT re-derive
  #    or re-tune the checker; import it.
  # 3. Repair model: google/gemma-3-12b-it via OpenRouter, matching B/D/C1/C2 exactly (same
  #    temperature/decoding params -- copy them verbatim from C2's method.py, do not re-guess).
  # 4. Config constants:
  #    MAX_PASSES = 3          # matches C2's iteration budget
  #    CALL_TIMEOUT_S = 75      # hard per-call timeout (60-90s range)
  #    MAX_RETRIES = 3          # exponential backoff: 2s, 8s, 20s
  #    HEARTBEAT_EVERY_S = 30   # watchdog log interval
  #    OUT_JSONL = 'condition_c_progress.jsonl'   # append-only, one line per completed (row, pass)
  #    RESUME = os.path.exists(OUT_JSONL)

  # === ROBUSTNESS WRAPPER (new this iteration -- the actual point of this artifact) ===
  async def call_with_timeout_and_retry(prompt, row_id, pass_num):
      for attempt in range(MAX_RETRIES):
          try:
              t0 = time.monotonic()
              result = await asyncio.wait_for(
                  openrouter_client.complete(model='google/gemma-3-12b-it', prompt=prompt),
                  timeout=CALL_TIMEOUT_S)
              log_call_cost(row_id, pass_num, result.usage, time.monotonic()-t0)
              return result
          except asyncio.TimeoutError:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} TIMEOUT after {CALL_TIMEOUT_S}s')
              await asyncio.sleep(2 * (4 ** attempt))  # 2s, 8s, 32s
          except Exception as e:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} ERROR {type(e).__name__}: {e}')
              await asyncio.sleep(2 * (4 ** attempt))
      logger.error(f'row={row_id} pass={pass_num} EXHAUSTED {MAX_RETRIES} retries -- marking row FAILED, continuing')
      return None  # caller must treat None as a hard per-row failure, log it, and move on -- never block the sweep on one row

  def load_completed_rows(jsonl_path):
      # RESUME: read every already-written line, build a set of (row_id) that reached a
      # terminal state (certificate OR pass-budget exhausted OR hard-failed), skip them entirely
      completed = {}
      if os.path.exists(jsonl_path):
          for line in open(jsonl_path):
              rec = json.loads(line)
              completed[rec['row_id']] = rec
      logger.info(f'resume: {len(completed)} rows already complete, skipping')
      return completed

  async def heartbeat_task(state):
      while not state['done']:
          logger.info(f"HEARTBEAT rows_done={state['rows_done']}/{state['total']} "
                      f"last_progress_ts={state['last_progress_ts']} "
                      f"elapsed_since_last_progress={time.monotonic()-state['last_progress_ts']:.0f}s")
          await asyncio.sleep(HEARTBEAT_EVERY_S)

  # === CONDITION C CORE LOGIC (C1's localization + C2's iterate-and-reverify) ===
  async def run_condition_c_on_row(row, checker, state):
      if row['row_id'] in completed_rows:
          return completed_rows[row['row_id']]  # resume short-circuit
      text = row['hypothesis_or_target']
      edit_log = []
      for pass_num in range(1, MAX_PASSES + 1):
          # C1-style broadened localization: re-run the checker on the CURRENT text every pass,
          # gated by the within-experiment usability table (same gate C1/C2 used)
          violations = checker.find_all_violations(row['source'], text, usability_table)
          if not violations:
              record = {'row_id': row['row_id'], 'status': 'certificate', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          repair_prompt = build_repair_prompt(row['source'], text, violations)  # same template as C1/C2
          result = await call_with_timeout_and_retry(repair_prompt, row['row_id'], pass_num)
          if result is None:
              record = {'row_id': row['row_id'], 'status': 'hard_failed_at_pass', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          text = extract_repaired_text(result)
          edit_log.append({'pass': pass_num, 'violations_targeted': violations, 'output': text,
                            'usage': result.usage})
      else:
          record = {'row_id': row['row_id'], 'status': 'budget_exhausted', 'final_pass': MAX_PASSES,
                     'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
      # INCREMENTAL WRITE: append this row's terminal record to disk THE INSTANT it completes,
      # never batched, so a stall anywhere loses at most one in-flight row
      with open(OUT_JSONL, 'a') as f:
          f.write(json.dumps(record) + '\n')
          f.flush(); os.fsync(f.fileno())
      state['rows_done'] += 1
      state['last_progress_ts'] = time.monotonic()
      return record

  async def main():
      completed_rows = load_completed_rows(OUT_JSONL)
      all_rows = natural_rows_320 + injected_rows_240   # exact same 560-row union as C1/C2
      remaining = [r for r in all_rows if r['row_id'] not in completed_rows]
      logger.info(f'{len(remaining)} rows remaining of {len(all_rows)} total')
      state = {'rows_done': len(completed_rows), 'total': len(all_rows), 'done': False,
               'last_progress_ts': time.monotonic()}
      hb = asyncio.create_task(heartbeat_task(state))
      sem = asyncio.Semaphore(8)  # bounded concurrency, matches C2's OpenRouter client config
      async def bounded(row):
          async with sem:
              return await run_condition_c_on_row(row, checker, state)
      await asyncio.gather(*[bounded(r) for r in remaining])
      state['done'] = True
      await hb

  # === PILOT COST PROBE (before committing to full run, same $2 methodology as C2) ===
  # Run main() restricted to a fixed 20-row pilot subset (10 natural + 10 injected, stratified
  # across language pairs). Measure: wall-clock for 20 rows, $ spent (sum of result.usage costs),
  # extrapolate to 560 rows. If extrapolated cost > $2, stop and re-budget before the full run
  # (reference point: C2's actual full-run spend was $0.045, so >$2 for a comparable condition
  # is itself a red flag worth investigating, not just paying).

  # === SCORING (run only after the full 560-row sweep in condition_c_progress.jsonl is complete
  #     or explicitly declared partial) ===
  # 1. Load condition_c_progress.jsonl, split back into natural (320) vs injected-pool (240) by row_id.
  # 2. ΔCOMET: score final_text vs source/reference for all 320 natural rows using the real
  #    wmt22-cometkiwi-da checkpoint (same install/checkpoint path as B/D/C1/C2 -- read from the
  #    resource dossier art_5ySTX4YfxqG_ if the exact checkpoint path/env is not obvious from C2's
  #    code). PERSIST PER-ROW ΔCOMET (not just the pooled mean) explicitly so a downstream
  #    evaluation artifact can run a true paired bootstrap against C1's and C2's per-row ΔCOMET
  #    arrays, rather than reusing C1-vs-C2's documented normal-approximation substitute.
  # 3. Fix rate / true regression rate: on the 240 injected-pool rows, compare each row's
  #    final_text against its known ground-truth original_span/corrupted_span using the SAME
  #    scoring function C1/C2 used (import it, do not reimplement). Report:
  #      - overall fix rate, overall true regression rate
  #      - broken out by invariant category (entity/number/negation/quantifier)
  #      - pooled INCLUDING negation-deletion rows and pooled EXCLUDING them (both numbers,
  #        matching C1/C2's reporting convention) -- log the negation-attemptability flag PER ROW
  #        (condition C's checker-based localization CAN attempt negation rows, unlike B/D/C2's
  #        oracle-span localization, so this is a genuinely new number, not a copy of C2's)
  # 4. Edit volume: token-level diff size between original hypothesis and final_text, per pass
  #    and cumulative; flag any row whose final edit distance approaches full-sentence rewrite
  #    (>80% of tokens changed) as a possible full-retranslation collapse.
  # 5. LLM calls per sentence: mean/median n_calls across all 560 rows, compare directly to B/D
  #    (1 call), C1 (1 call per violation), C2 (up to 3 calls).
  # 6. Write method_out.json with: per-row arrays for all above metrics, pooled summary stats with
  #    95% CIs (paired bootstrap where a shared population with C1/C2 exists), completion_fraction
  #    field (1.0 if all 560 rows reached a terminal state, else the actual fraction), and an
  #    explicit per-language-pair breakdown table.
fallback_plan: |-
  1. TIMEOUT/HANG RECURRENCE (the exact prior failure mode): the heartbeat log makes a stall diagnosable within HEARTBEAT_EVERY_S=30s instead of after an hour of silence -- if rows_done stops advancing for more than ~5 minutes despite the semaphore having in-flight slots, kill the process (PID-based, per process_isolation rules), inspect the last heartbeat and the last few JSONL lines to identify which row_id(s) were in flight, and restart: RESUME logic in load_completed_rows() means the restart skips every already-terminal row and only retries what was truly in-flight, so no work is lost. If the SAME row_id hangs again on restart, that specific row is the culprit (not general infra) -- log it, skip it with a 'poison_row' status, and continue the sweep; do not let one row block the other 559.
  2. WALL-CLOCK BUDGET EXCEEDED even with robustness measures: if the full 560-row sweep has not reached completion_fraction=1.0 after a generous cap (e.g. 2x the pilot-extrapolated wall-clock, or 90 minutes, whichever is larger), stop the sweep, run the scoring step on whatever rows ARE in condition_c_progress.jsonl, and write method_out.json with completion_fraction < 1.0 explicitly set, plus a per-language-pair breakdown showing which pairs are under-represented in the partial sample -- per the direction's explicit partial-report fallback. Do not silently pad missing rows with any placeholder value.
  3. COST OVERRUN: if the pilot 20-row probe extrapolates to more than $2, first check whether MAX_PASSES=3 combined with C1-style per-sentence multi-violation repair (more violations found per sentence than C2's single-span repair) is driving more calls than expected -- this is a real, expected cost increase over C2 relative to C1's flat 1-call/violation, not necessarily a bug. If it still exceeds the shared $10 ceiling headroom (checking C1+C2's prior spend first), reduce MAX_PASSES to 2 for the full run and note the deviation from C2's budget in method_out.json, rather than skip the condition entirely.
  4. ROW-ID MISMATCH against C1/C2: if C2's exact 560-row population cannot be reconstructed byte-for-byte (e.g. C2 did not persist row IDs), fall back to re-deriving the population using C2's documented stratification code path with the SAME random seed, and explicitly flag in method_out.json that population identity is asserted-by-code-reuse rather than verified-by-row-ID-diff, so downstream evaluation knows the strength of the comparability claim.
  5. CHECKER/REPAIR-MODEL API FAILURE (OpenRouter outage, not a single hung call): if MAX_RETRIES is exhausted on a majority of rows in the pilot probe (not just one poison row), treat this as an upstream outage, pause, and retry the pilot after a delay before committing to the full sweep -- do not burn the full budget against a broken endpoint.
  6. If google/gemma-3-12b-it itself becomes unavailable on OpenRouter (mirroring the TowerPlus-9B delisting that forced this model choice in the first place), the resource dossier's re-ranked substitute table (art_5ySTX4YfxqG_) names the next candidate -- switch to it, note the deviation explicitly (this would break the fixed-repair-model-across-conditions design B/D/C1/C2/C rely on for comparability), and flag this prominently rather than silently swapping models.
testing_plan: |-
  1. DRY RUN ON 3 ROWS FIRST (before the 20-row pilot): pick 3 rows by hand (1 natural, 2 injected with clean single-violation cases) and run the full per-row loop synchronously with verbose logging. Manually inspect: does checker.find_all_violations() return a sensible violation list against the current pass's text (not the original), does the repair prompt look correct, does extract_repaired_text() correctly parse gemma-3-12b-it's output format (check for the same leaked-format issues B/D had to guard against -- gemma may format repairs differently than TowerPlus-9B did), does the JSONL line get written and is it valid JSON, does a certificate correctly trigger early-exit before MAX_PASSES.
  2. INSTRUMENTATION UNIT TEST: deliberately inject an artificial 90-second sleep into ONE mocked OpenRouter call (bypassing the real API) to confirm the CALL_TIMEOUT_S=75s timeout actually fires, the retry/backoff sequence logs correctly, and after MAX_RETRIES the row is marked hard-failed and the sweep continues past it rather than hanging -- this is the single most important test given what killed the prior attempt, so it must be verified BEFORE the full sweep, not inferred from the code reading correctly.
  3. RESUME TEST: run the 3-row dry run to completion, then re-invoke main() with the same OUT_JSONL present -- confirm load_completed_rows() correctly skips all 3 and logs 'resume: 3 rows already complete', proving resumability actually works before relying on it during a real stall recovery.
  4. 20-ROW PILOT (cost + timing probe, matches C2's $2 methodology): run the full pipeline (not mocked) on 20 stratified rows, record actual wall-clock and actual $ spent from OpenRouter usage fields, extrapolate linearly to 560 rows, and confirm the extrapolate stays under the shared $10 ceiling with C2's $0.045 as a sanity reference (a Condition-C extrapolate of low-single-digit-dollars is expected and fine; anything approaching $2+ warrants investigating why before scaling up, per the fallback plan).
  5. SANITY-CHECK PILOT RESULTS AGAINST C1/C2 BEFORE THE FULL RUN: on the 20 pilot rows, compute fix rate and ΔCOMET-direction (not full COMET, just spot-check whether repaired text looks more or less faithful than input) and confirm it is broadly consistent with C1/C2's established ranges (fix rate somewhere between C1's 0.6056 and C2's ~0.99, since C combines both mechanisms) -- if the pilot shows fix rate near 0 or wildly outside this envelope, stop and debug the repair/checker integration rather than scaling a broken pipeline to 560 rows.
  6. FULL SWEEP with heartbeat monitoring: launch the 560-row run as a background process per process_isolation rules (PID-tracked, never grep-by-name), tail the log for heartbeat lines to confirm steady rows_done progress every ~30s, and only proceed to scoring once completion_fraction reaches 1.0 or the wall-clock fallback cap is hit.
  7. POST-HOC VALIDATION: after scoring, confirm the output row counts match expectations exactly (320 natural + 240 injected = 560 total records in condition_c_progress.jsonl, no duplicates by row_id, no missing row_ids relative to the input population minus any explicitly-logged hard-failures), and confirm per-row ΔCOMET array length equals 320 exactly before treating the paired-bootstrap capability as available downstream.
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

### [10] SYSTEM-USER prompt · 2026-09-01 09:45:04 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [11] SYSTEM-USER prompt · 2026-09-01 09:45:58 UTC

```
<task-notification>
<task-id>brca7d1dd</task-id>
<summary>Monitor event: "Condition C 560-row sweep progress"</summary>
<event>progress: 231/560 rows</event>
</task-notification>
```

### [12] SYSTEM-USER prompt · 2026-09-01 09:45:58 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [13] SYSTEM-USER prompt · 2026-09-01 09:49:03 UTC

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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 1516s.
Error: output_format validation failed after 3 retries: The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Last messages before the crash:
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "73", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Bash] Tool: Bash
cat /tmp/freeze.txt
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "aiohappyeyeballs==2.7.1\naiohttp==3.14.3\naiosignal==1.4.0\nattrs==26.1.0\ncertifi==2026.7.22\ncharset-normalizer==3.5.1\ncolorama==0.4.6\nemoji==2.15.0\nentmax==1.3\nfilelock==3.32.3\nfrozenlist==1.8.0\nfsspec==2026.7.0\nhf-xet==1.6.0\nhuggingface-hub==0.36.2\nidna==3.19\njinja2==3.1.6\njsonargparse==3.13.1\nlightning-utilities==0.15.3\nloguru==0.7.3\nlxml==6.1.2\nmarkupsafe==3.0.3\nmpmath==1.3.0\nmultidict==6.7.1\nnetworkx==3.6.1\nnumpy==1.26.4\nnvidia-cublas-cu12==12.4.5.8\nnvidia-cuda-cupti-cu12==12.4.127\nnvidia-cuda-nvrtc-cu12==12.4.127\nnvidia-cuda-runtime-cu12==12.4.127\nnvidia-cudnn-cu12==9.1.0.70\nnvidia-cufft-cu12==11.2.1.3\nnvidia-curand-cu12==10.3.5.147\nnvidia-cusolver-cu12==11.6.1.9\nnvidia-cusparse-cu12==12.3.1.170\nnvidia-cusparselt-cu12==0.6.2\nnvidia-nccl-cu12==2.21.5\nnvidia-nvjitlink-cu12==12.4.127\nnvidia-nvtx-cu12==12.4.127\npackaging==26.3\npandas==3.0.5\nplatformdirs==4.11.6\nportalocker==4.3.0\npropcache==0.5.2\nprotobuf==4.25.9\npsutil==7.2.2\npython-dateutil==2.9.0.post0\npython-dotenv==1.2.3\npytorch-lightning==2.6.5\npyyaml==6.0.3\nregex==2026.9.3\nrequests==2.34.2\nsacrebleu==2.6.0\nsafetensors==0.8.0\nscipy==1.17.1\nsentencepiece==0.2.2\nsetuptools==78.1.0\nsix==1.17.0\nstanza==1.14.0\nsympy==1.13.1\ntabulate==0.10.0\ntermcolor==3.3.0\ntokenizers==0.22.2\ntorch==2.6.0+cu124\ntorchmetrics==0.10.3\ntqdm==4.70.0\ntransformers==4.57.6\ntriton==3.2.0\ntyping-extensions==4.16.0\nudapi==0.5.2\nudtools==0.2.8\nunbabel-comet==2.2.7\nurllib3==2.7.0\nyarl==1.24.5", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] This matches the pyproject.toml I copied exactly (identical pins). Let me confirm the pyproject.toml [project] section is well-formed.
  - [agent_tool_call: Read] Tool: Read
/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/pyproject.toml
  - [agent_tool_result: Read] Tool: Read
Result:
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/pyproject.toml", "content": "[project]\nname = \"gen-art-experiment-1-iter4\"\nversion = \"0.1.0\"\nrequires-python = \">=3.12\"\ndependencies = [\n    # Exact versions pinned via `uv pip freeze` against the .venv this\n    # artifact actually ran in (reproducibility requirement). Install order\n    # matters for torch/CUDA -- see the note below.\n    \"aiohappyeyeballs==2.7.1\",\n    \"aiohttp==3.14.3\",", "numLines": 10, "startLine": 1, "totalLines": 97}}
  - [agent_response] pyproject.toml is already correctly pinned and matches the live freeze exactly (TODO 3 satisfied). Now waiting for the scoring pass to finish.
  - [agent_tool_call: Bash] Tool: Bash
cd /ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1
kill -0 1306 2>/dev/null && echo RUNNING || echo ENDED
tail -20 logs/score_partial.log 2>/dev/null
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "RUNNING\n09:47:14|INFO   |Natural subsample [en-uk_UA]: 160 rows across 4 domains\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-ru_RU,named_entity_swap]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-ru_RU,number_unit_date_alteration]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-ru_RU,negation_polarity_flip]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-ru_RU,quantifier_substitution]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-uk_UA,named_entity_swap]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-uk_UA,number_unit_date_alteration]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-uk_UA,negation_polarity_flip]: 30 rows\n09:47:14|INFO   |Injected [experimental_pool] subsample [en-uk_UA,quantifier_substitution]: 30 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-ru_RU,named_entity_swap]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-ru_RU,number_unit_date_alteration]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-ru_RU,negation_polarity_flip]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-ru_RU,quantifier_substitution]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-uk_UA,named_entity_swap]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-uk_UA,number_unit_date_alteration]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-uk_UA,negation_polarity_flip]: 23 rows\n09:47:14|INFO   |Injected [checker_validation_heldout] subsample [en-uk_UA,quantifier_substitution]: 14 rows\n09:47:14|INFO   |Row-ID identity check vs C2 [natural_match]: True\n09:47:14|INFO   |Row-ID identity check vs C2 [injected_pool_match]: True\n09:47:14|INFO   |Row-ID identity check vs C2 [injected_heldout_match]: True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Good, it's running through checker validation now. Let me wait for the monitor's next events.
  - [agent_tool_call: Bash] Tool: Bash
true
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Bash] Tool: Bash
true
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Waiting for the scoring monitor to report completion.

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
title: Run Combined Fix Condition, This Time Robustly
summary: >-
  Execute Condition C (checker-broadened localization + iterative repair-and-reverify) on the exact B/D/C1/C2 row population,
  repair model, and checker, wrapped in incremental-write, timeout/retry, heartbeat, and resume instrumentation specifically
  designed to survive or diagnose the silent hour-long stall that killed the prior attempt. Score identically to C2 (per-row
  ΔCOMET, fix rate, true regression rate, edit volume, call counts) so C1/C2/C become a directly comparable triple.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # === SETUP (reuse verbatim from art_K8koUmGFDlLN, the completed C2 artifact) ===
  # 1. Load population: 320 natural rows (wmt25_task3_natural, metadata_fold=='experimental_pool')
  #    + 240 injected-pool rows (injected_error_augmentation, metadata_fold=='experimental_pool',
  #    subsampled/stratified exactly as C2 did -- read C2's row-selection code and its logged
  #    row-id list from method_out.json / a saved row_ids.json, and diff against a fresh load
  #    of full_data_out.json to assert IDENTICAL row IDs before running anything. If C2's
  #    artifact did not persist row IDs explicitly, treat any drift as a hard blocker: log it
  #    and use C2's exact stratification code path, not a re-derivation, since re-deriving from
  #    a random seed alone is not verifiably identical.
  # 2. Load the deterministic content-invariant checker module unmodified from C1/C2 (NER +
  #    number/unit/date regex + negation cue lists + quantifier word lists), and the same
  #    within-experiment 8-cell usability/gating table C1/C2 used to decide which
  #    (language_pair, category) cells the checker is trusted to repair-gate on. Do NOT re-derive
  #    or re-tune the checker; import it.
  # 3. Repair model: google/gemma-3-12b-it via OpenRouter, matching B/D/C1/C2 exactly (same
  #    temperature/decoding params -- copy them verbatim from C2's method.py, do not re-guess).
  # 4. Config constants:
  #    MAX_PASSES = 3          # matches C2's iteration budget
  #    CALL_TIMEOUT_S = 75      # hard per-call timeout (60-90s range)
  #    MAX_RETRIES = 3          # exponential backoff: 2s, 8s, 20s
  #    HEARTBEAT_EVERY_S = 30   # watchdog log interval
  #    OUT_JSONL = 'condition_c_progress.jsonl'   # append-only, one line per completed (row, pass)
  #    RESUME = os.path.exists(OUT_JSONL)

  # === ROBUSTNESS WRAPPER (new this iteration -- the actual point of this artifact) ===
  async def call_with_timeout_and_retry(prompt, row_id, pass_num):
      for attempt in range(MAX_RETRIES):
          try:
              t0 = time.monotonic()
              result = await asyncio.wait_for(
                  openrouter_client.complete(model='google/gemma-3-12b-it', prompt=prompt),
                  timeout=CALL_TIMEOUT_S)
              log_call_cost(row_id, pass_num, result.usage, time.monotonic()-t0)
              return result
          except asyncio.TimeoutError:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} TIMEOUT after {CALL_TIMEOUT_S}s')
              await asyncio.sleep(2 * (4 ** attempt))  # 2s, 8s, 32s
          except Exception as e:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} ERROR {type(e).__name__}: {e}')
              await asyncio.sleep(2 * (4 ** attempt))
      logger.error(f'row={row_id} pass={pass_num} EXHAUSTED {MAX_RETRIES} retries -- marking row FAILED, continuing')
      return None  # caller must treat None as a hard per-row failure, log it, and move on -- never block the sweep on one row

  def load_completed_rows(jsonl_path):
      # RESUME: read every already-written line, build a set of (row_id) that reached a
      # terminal state (certificate OR pass-budget exhausted OR hard-failed), skip them entirely
      completed = {}
      if os.path.exists(jsonl_path):
          for line in open(jsonl_path):
              rec = json.loads(line)
              completed[rec['row_id']] = rec
      logger.info(f'resume: {len(completed)} rows already complete, skipping')
      return completed

  async def heartbeat_task(state):
      while not state['done']:
          logger.info(f"HEARTBEAT rows_done={state['rows_done']}/{state['total']} "
                      f"last_progress_ts={state['last_progress_ts']} "
                      f"elapsed_since_last_progress={time.monotonic()-state['last_progress_ts']:.0f}s")
          await asyncio.sleep(HEARTBEAT_EVERY_S)

  # === CONDITION C CORE LOGIC (C1's localization + C2's iterate-and-reverify) ===
  async def run_condition_c_on_row(row, checker, state):
      if row['row_id'] in completed_rows:
          return completed_rows[row['row_id']]  # resume short-circuit
      text = row['hypothesis_or_target']
      edit_log = []
      for pass_num in range(1, MAX_PASSES + 1):
          # C1-style broadened localization: re-run the checker on the CURRENT text every pass,
          # gated by the within-experiment usability table (same gate C1/C2 used)
          violations = checker.find_all_violations(row['source'], text, usability_table)
          if not violations:
              record = {'row_id': row['row_id'], 'status': 'certificate', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          repair_prompt = build_repair_prompt(row['source'], text, violations)  # same template as C1/C2
          result = await call_with_timeout_and_retry(repair_prompt, row['row_id'], pass_num)
          if result is None:
              record = {'row_id': row['row_id'], 'status': 'hard_failed_at_pass', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          text = extract_repaired_text(result)
          edit_log.append({'pass': pass_num, 'violations_targeted': violations, 'output': text,
                            'usage': result.usage})
      else:
          record = {'row_id': row['row_id'], 'status': 'budget_exhausted', 'final_pass': MAX_PASSES,
                     'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
      # INCREMENTAL WRITE: append this row's terminal record to disk THE INSTANT it completes,
      # never batched, so a stall anywhere loses at most one in-flight row
      with open(OUT_JSONL, 'a') as f:
          f.write(json.dumps(record) + '\n')
          f.flush(); os.fsync(f.fileno())
      state['rows_done'] += 1
      state['last_progress_ts'] = time.monotonic()
      return record

  async def main():
      completed_rows = load_completed_rows(OUT_JSONL)
      all_rows = natural_rows_320 + injected_rows_240   # exact same 560-row union as C1/C2
      remaining = [r for r in all_rows if r['row_id'] not in completed_rows]
      logger.info(f'{len(remaining)} rows remaining of {len(all_rows)} total')
      state = {'rows_done': len(completed_rows), 'total': len(all_rows), 'done': False,
               'last_progress_ts': time.monotonic()}
      hb = asyncio.create_task(heartbeat_task(state))
      sem = asyncio.Semaphore(8)  # bounded concurrency, matches C2's OpenRouter client config
      async def bounded(row):
          async with sem:
              return await run_condition_c_on_row(row, checker, state)
      await asyncio.gather(*[bounded(r) for r in remaining])
      state['done'] = True
      await hb

  # === PILOT COST PROBE (before committing to full run, same $2 methodology as C2) ===
  # Run main() restricted to a fixed 20-row pilot subset (10 natural + 10 injected, stratified
  # across language pairs). Measure: wall-clock for 20 rows, $ spent (sum of result.usage costs),
  # extrapolate to 560 rows. If extrapolated cost > $2, stop and re-budget before the full run
  # (reference point: C2's actual full-run spend was $0.045, so >$2 for a comparable condition
  # is itself a red flag worth investigating, not just paying).

  # === SCORING (run only after the full 560-row sweep in condition_c_progress.jsonl is complete
  #     or explicitly declared partial) ===
  # 1. Load condition_c_progress.jsonl, split back into natural (320) vs injected-pool (240) by row_id.
  # 2. ΔCOMET: score final_text vs source/reference for all 320 natural rows using the real
  #    wmt22-cometkiwi-da checkpoint (same install/checkpoint path as B/D/C1/C2 -- read from the
  #    resource dossier art_5ySTX4YfxqG_ if the exact checkpoint path/env is not obvious from C2's
  #    code). PERSIST PER-ROW ΔCOMET (not just the pooled mean) explicitly so a downstream
  #    evaluation artifact can run a true paired bootstrap against C1's and C2's per-row ΔCOMET
  #    arrays, rather than reusing C1-vs-C2's documented normal-approximation substitute.
  # 3. Fix rate / true regression rate: on the 240 injected-pool rows, compare each row's
  #    final_text against its known ground-truth original_span/corrupted_span using the SAME
  #    scoring function C1/C2 used (import it, do not reimplement). Report:
  #      - overall fix rate, overall true regression rate
  #      - broken out by invariant category (entity/number/negation/quantifier)
  #      - pooled INCLUDING negation-deletion rows and pooled EXCLUDING them (both numbers,
  #        matching C1/C2's reporting convention) -- log the negation-attemptability flag PER ROW
  #        (condition C's checker-based localization CAN attempt negation rows, unlike B/D/C2's
  #        oracle-span localization, so this is a genuinely new number, not a copy of C2's)
  # 4. Edit volume: token-level diff size between original hypothesis and final_text, per pass
  #    and cumulative; flag any row whose final edit distance approaches full-sentence rewrite
  #    (>80% of tokens changed) as a possible full-retranslation collapse.
  # 5. LLM calls per sentence: mean/median n_calls across all 560 rows, compare directly to B/D
  #    (1 call), C1 (1 call per violation), C2 (up to 3 calls).
  # 6. Write method_out.json with: per-row arrays for all above metrics, pooled summary stats with
  #    95% CIs (paired bootstrap where a shared population with C1/C2 exists), completion_fraction
  #    field (1.0 if all 560 rows reached a terminal state, else the actual fraction), and an
  #    explicit per-language-pair breakdown table.
fallback_plan: |-
  1. TIMEOUT/HANG RECURRENCE (the exact prior failure mode): the heartbeat log makes a stall diagnosable within HEARTBEAT_EVERY_S=30s instead of after an hour of silence -- if rows_done stops advancing for more than ~5 minutes despite the semaphore having in-flight slots, kill the process (PID-based, per process_isolation rules), inspect the last heartbeat and the last few JSONL lines to identify which row_id(s) were in flight, and restart: RESUME logic in load_completed_rows() means the restart skips every already-terminal row and only retries what was truly in-flight, so no work is lost. If the SAME row_id hangs again on restart, that specific row is the culprit (not general infra) -- log it, skip it with a 'poison_row' status, and continue the sweep; do not let one row block the other 559.
  2. WALL-CLOCK BUDGET EXCEEDED even with robustness measures: if the full 560-row sweep has not reached completion_fraction=1.0 after a generous cap (e.g. 2x the pilot-extrapolated wall-clock, or 90 minutes, whichever is larger), stop the sweep, run the scoring step on whatever rows ARE in condition_c_progress.jsonl, and write method_out.json with completion_fraction < 1.0 explicitly set, plus a per-language-pair breakdown showing which pairs are under-represented in the partial sample -- per the direction's explicit partial-report fallback. Do not silently pad missing rows with any placeholder value.
  3. COST OVERRUN: if the pilot 20-row probe extrapolates to more than $2, first check whether MAX_PASSES=3 combined with C1-style per-sentence multi-violation repair (more violations found per sentence than C2's single-span repair) is driving more calls than expected -- this is a real, expected cost increase over C2 relative to C1's flat 1-call/violation, not necessarily a bug. If it still exceeds the shared $10 ceiling headroom (checking C1+C2's prior spend first), reduce MAX_PASSES to 2 for the full run and note the deviation from C2's budget in method_out.json, rather than skip the condition entirely.
  4. ROW-ID MISMATCH against C1/C2: if C2's exact 560-row population cannot be reconstructed byte-for-byte (e.g. C2 did not persist row IDs), fall back to re-deriving the population using C2's documented stratification code path with the SAME random seed, and explicitly flag in method_out.json that population identity is asserted-by-code-reuse rather than verified-by-row-ID-diff, so downstream evaluation knows the strength of the comparability claim.
  5. CHECKER/REPAIR-MODEL API FAILURE (OpenRouter outage, not a single hung call): if MAX_RETRIES is exhausted on a majority of rows in the pilot probe (not just one poison row), treat this as an upstream outage, pause, and retry the pilot after a delay before committing to the full sweep -- do not burn the full budget against a broken endpoint.
  6. If google/gemma-3-12b-it itself becomes unavailable on OpenRouter (mirroring the TowerPlus-9B delisting that forced this model choice in the first place), the resource dossier's re-ranked substitute table (art_5ySTX4YfxqG_) names the next candidate -- switch to it, note the deviation explicitly (this would break the fixed-repair-model-across-conditions design B/D/C1/C2/C rely on for comparability), and flag this prominently rather than silently swapping models.
testing_plan: |-
  1. DRY RUN ON 3 ROWS FIRST (before the 20-row pilot): pick 3 rows by hand (1 natural, 2 injected with clean single-violation cases) and run the full per-row loop synchronously with verbose logging. Manually inspect: does checker.find_all_violations() return a sensible violation list against the current pass's text (not the original), does the repair prompt look correct, does extract_repaired_text() correctly parse gemma-3-12b-it's output format (check for the same leaked-format issues B/D had to guard against -- gemma may format repairs differently than TowerPlus-9B did), does the JSONL line get written and is it valid JSON, does a certificate correctly trigger early-exit before MAX_PASSES.
  2. INSTRUMENTATION UNIT TEST: deliberately inject an artificial 90-second sleep into ONE mocked OpenRouter call (bypassing the real API) to confirm the CALL_TIMEOUT_S=75s timeout actually fires, the retry/backoff sequence logs correctly, and after MAX_RETRIES the row is marked hard-failed and the sweep continues past it rather than hanging -- this is the single most important test given what killed the prior attempt, so it must be verified BEFORE the full sweep, not inferred from the code reading correctly.
  3. RESUME TEST: run the 3-row dry run to completion, then re-invoke main() with the same OUT_JSONL present -- confirm load_completed_rows() correctly skips all 3 and logs 'resume: 3 rows already complete', proving resumability actually works before relying on it during a real stall recovery.
  4. 20-ROW PILOT (cost + timing probe, matches C2's $2 methodology): run the full pipeline (not mocked) on 20 stratified rows, record actual wall-clock and actual $ spent from OpenRouter usage fields, extrapolate linearly to 560 rows, and confirm the extrapolate stays under the shared $10 ceiling with C2's $0.045 as a sanity reference (a Condition-C extrapolate of low-single-digit-dollars is expected and fine; anything approaching $2+ warrants investigating why before scaling up, per the fallback plan).
  5. SANITY-CHECK PILOT RESULTS AGAINST C1/C2 BEFORE THE FULL RUN: on the 20 pilot rows, compute fix rate and ΔCOMET-direction (not full COMET, just spot-check whether repaired text looks more or less faithful than input) and confirm it is broadly consistent with C1/C2's established ranges (fix rate somewhere between C1's 0.6056 and C2's ~0.99, since C combines both mechanisms) -- if the pilot shows fix rate near 0 or wildly outside this envelope, stop and debug the repair/checker integration rather than scaling a broken pipeline to 560 rows.
  6. FULL SWEEP with heartbeat monitoring: launch the 560-row run as a background process per process_isolation rules (PID-tracked, never grep-by-name), tail the log for heartbeat lines to confirm steady rows_done progress every ~30s, and only proceed to scoring once completion_fraction reaches 1.0 or the wall-clock fallback cap is hit.
  7. POST-HOC VALIDATION: after scoring, confirm the output row counts match expectations exactly (320 natural + 240 injected = 560 total records in condition_c_progress.jsonl, no duplicates by row_id, no missing row_ids relative to the input population minus any explicitly-logged hard-failures), and confirm per-row ΔCOMET array length equals 320 exactly before treating the paired-bootstrap capability as available downstream.
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

### [14] HUMAN-USER prompt · 2026-09-01 09:49:03 UTC

```
AI in translation emwrging opportunities
```

### [15] SYSTEM-USER prompt · 2026-09-01 10:05:26 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_VO5kqjjB2Uk5/3_invention_loop/iter_4/gen_art/gen_art_experiment_1/results/out.json`
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
title: Run Combined Fix Condition, This Time Robustly
summary: >-
  Execute Condition C (checker-broadened localization + iterative repair-and-reverify) on the exact B/D/C1/C2 row population,
  repair model, and checker, wrapped in incremental-write, timeout/retry, heartbeat, and resume instrumentation specifically
  designed to survive or diagnose the silent hour-long stall that killed the prior attempt. Score identically to C2 (per-row
  ΔCOMET, fix rate, true regression rate, edit volume, call counts) so C1/C2/C become a directly comparable triple.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # === SETUP (reuse verbatim from art_K8koUmGFDlLN, the completed C2 artifact) ===
  # 1. Load population: 320 natural rows (wmt25_task3_natural, metadata_fold=='experimental_pool')
  #    + 240 injected-pool rows (injected_error_augmentation, metadata_fold=='experimental_pool',
  #    subsampled/stratified exactly as C2 did -- read C2's row-selection code and its logged
  #    row-id list from method_out.json / a saved row_ids.json, and diff against a fresh load
  #    of full_data_out.json to assert IDENTICAL row IDs before running anything. If C2's
  #    artifact did not persist row IDs explicitly, treat any drift as a hard blocker: log it
  #    and use C2's exact stratification code path, not a re-derivation, since re-deriving from
  #    a random seed alone is not verifiably identical.
  # 2. Load the deterministic content-invariant checker module unmodified from C1/C2 (NER +
  #    number/unit/date regex + negation cue lists + quantifier word lists), and the same
  #    within-experiment 8-cell usability/gating table C1/C2 used to decide which
  #    (language_pair, category) cells the checker is trusted to repair-gate on. Do NOT re-derive
  #    or re-tune the checker; import it.
  # 3. Repair model: google/gemma-3-12b-it via OpenRouter, matching B/D/C1/C2 exactly (same
  #    temperature/decoding params -- copy them verbatim from C2's method.py, do not re-guess).
  # 4. Config constants:
  #    MAX_PASSES = 3          # matches C2's iteration budget
  #    CALL_TIMEOUT_S = 75      # hard per-call timeout (60-90s range)
  #    MAX_RETRIES = 3          # exponential backoff: 2s, 8s, 20s
  #    HEARTBEAT_EVERY_S = 30   # watchdog log interval
  #    OUT_JSONL = 'condition_c_progress.jsonl'   # append-only, one line per completed (row, pass)
  #    RESUME = os.path.exists(OUT_JSONL)

  # === ROBUSTNESS WRAPPER (new this iteration -- the actual point of this artifact) ===
  async def call_with_timeout_and_retry(prompt, row_id, pass_num):
      for attempt in range(MAX_RETRIES):
          try:
              t0 = time.monotonic()
              result = await asyncio.wait_for(
                  openrouter_client.complete(model='google/gemma-3-12b-it', prompt=prompt),
                  timeout=CALL_TIMEOUT_S)
              log_call_cost(row_id, pass_num, result.usage, time.monotonic()-t0)
              return result
          except asyncio.TimeoutError:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} TIMEOUT after {CALL_TIMEOUT_S}s')
              await asyncio.sleep(2 * (4 ** attempt))  # 2s, 8s, 32s
          except Exception as e:
              logger.warning(f'row={row_id} pass={pass_num} attempt={attempt} ERROR {type(e).__name__}: {e}')
              await asyncio.sleep(2 * (4 ** attempt))
      logger.error(f'row={row_id} pass={pass_num} EXHAUSTED {MAX_RETRIES} retries -- marking row FAILED, continuing')
      return None  # caller must treat None as a hard per-row failure, log it, and move on -- never block the sweep on one row

  def load_completed_rows(jsonl_path):
      # RESUME: read every already-written line, build a set of (row_id) that reached a
      # terminal state (certificate OR pass-budget exhausted OR hard-failed), skip them entirely
      completed = {}
      if os.path.exists(jsonl_path):
          for line in open(jsonl_path):
              rec = json.loads(line)
              completed[rec['row_id']] = rec
      logger.info(f'resume: {len(completed)} rows already complete, skipping')
      return completed

  async def heartbeat_task(state):
      while not state['done']:
          logger.info(f"HEARTBEAT rows_done={state['rows_done']}/{state['total']} "
                      f"last_progress_ts={state['last_progress_ts']} "
                      f"elapsed_since_last_progress={time.monotonic()-state['last_progress_ts']:.0f}s")
          await asyncio.sleep(HEARTBEAT_EVERY_S)

  # === CONDITION C CORE LOGIC (C1's localization + C2's iterate-and-reverify) ===
  async def run_condition_c_on_row(row, checker, state):
      if row['row_id'] in completed_rows:
          return completed_rows[row['row_id']]  # resume short-circuit
      text = row['hypothesis_or_target']
      edit_log = []
      for pass_num in range(1, MAX_PASSES + 1):
          # C1-style broadened localization: re-run the checker on the CURRENT text every pass,
          # gated by the within-experiment usability table (same gate C1/C2 used)
          violations = checker.find_all_violations(row['source'], text, usability_table)
          if not violations:
              record = {'row_id': row['row_id'], 'status': 'certificate', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          repair_prompt = build_repair_prompt(row['source'], text, violations)  # same template as C1/C2
          result = await call_with_timeout_and_retry(repair_prompt, row['row_id'], pass_num)
          if result is None:
              record = {'row_id': row['row_id'], 'status': 'hard_failed_at_pass', 'final_pass': pass_num,
                         'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
              break
          text = extract_repaired_text(result)
          edit_log.append({'pass': pass_num, 'violations_targeted': violations, 'output': text,
                            'usage': result.usage})
      else:
          record = {'row_id': row['row_id'], 'status': 'budget_exhausted', 'final_pass': MAX_PASSES,
                     'final_text': text, 'edit_log': edit_log, 'n_calls': len(edit_log)}
      # INCREMENTAL WRITE: append this row's terminal record to disk THE INSTANT it completes,
      # never batched, so a stall anywhere loses at most one in-flight row
      with open(OUT_JSONL, 'a') as f:
          f.write(json.dumps(record) + '\n')
          f.flush(); os.fsync(f.fileno())
      state['rows_done'] += 1
      state['last_progress_ts'] = time.monotonic()
      return record

  async def main():
      completed_rows = load_completed_rows(OUT_JSONL)
      all_rows = natural_rows_320 + injected_rows_240   # exact same 560-row union as C1/C2
      remaining = [r for r in all_rows if r['row_id'] not in completed_rows]
      logger.info(f'{len(remaining)} rows remaining of {len(all_rows)} total')
      state = {'rows_done': len(completed_rows), 'total': len(all_rows), 'done': False,
               'last_progress_ts': time.monotonic()}
      hb = asyncio.create_task(heartbeat_task(state))
      sem = asyncio.Semaphore(8)  # bounded concurrency, matches C2's OpenRouter client config
      async def bounded(row):
          async with sem:
              return await run_condition_c_on_row(row, checker, state)
      await asyncio.gather(*[bounded(r) for r in remaining])
      state['done'] = True
      await hb

  # === PILOT COST PROBE (before committing to full run, same $2 methodology as C2) ===
  # Run main() restricted to a fixed 20-row pilot subset (10 natural + 10 injected, stratified
  # across language pairs). Measure: wall-clock for 20 rows, $ spent (sum of result.usage costs),
  # extrapolate to 560 rows. If extrapolated cost > $2, stop and re-budget before the full run
  # (reference point: C2's actual full-run spend was $0.045, so >$2 for a comparable condition
  # is itself a red flag worth investigating, not just paying).

  # === SCORING (run only after the full 560-row sweep in condition_c_progress.jsonl is complete
  #     or explicitly declared partial) ===
  # 1. Load condition_c_progress.jsonl, split back into natural (320) vs injected-pool (240) by row_id.
  # 2. ΔCOMET: score final_text vs source/reference for all 320 natural rows using the real
  #    wmt22-cometkiwi-da checkpoint (same install/checkpoint path as B/D/C1/C2 -- read from the
  #    resource dossier art_5ySTX4YfxqG_ if the exact checkpoint path/env is not obvious from C2's
  #    code). PERSIST PER-ROW ΔCOMET (not just the pooled mean) explicitly so a downstream
  #    evaluation artifact can run a true paired bootstrap against C1's and C2's per-row ΔCOMET
  #    arrays, rather than reusing C1-vs-C2's documented normal-approximation substitute.
  # 3. Fix rate / true regression rate: on the 240 injected-pool rows, compare each row's
  #    final_text against its known ground-truth original_span/corrupted_span using the SAME
  #    scoring function C1/C2 used (import it, do not reimplement). Report:
  #      - overall fix rate, overall true regression rate
  #      - broken out by invariant category (entity/number/negation/quantifier)
  #      - pooled INCLUDING negation-deletion rows and pooled EXCLUDING them (both numbers,
  #        matching C1/C2's reporting convention) -- log the negation-attemptability flag PER ROW
  #        (condition C's checker-based localization CAN attempt negation rows, unlike B/D/C2's
  #        oracle-span localization, so this is a genuinely new number, not a copy of C2's)
  # 4. Edit volume: token-level diff size between original hypothesis and final_text, per pass
  #    and cumulative; flag any row whose final edit distance approaches full-sentence rewrite
  #    (>80% of tokens changed) as a possible full-retranslation collapse.
  # 5. LLM calls per sentence: mean/median n_calls across all 560 rows, compare directly to B/D
  #    (1 call), C1 (1 call per violation), C2 (up to 3 calls).
  # 6. Write method_out.json with: per-row arrays for all above metrics, pooled summary stats with
  #    95% CIs (paired bootstrap where a shared population with C1/C2 exists), completion_fraction
  #    field (1.0 if all 560 rows reached a terminal state, else the actual fraction), and an
  #    explicit per-language-pair breakdown table.
fallback_plan: |-
  1. TIMEOUT/HANG RECURRENCE (the exact prior failure mode): the heartbeat log makes a stall diagnosable within HEARTBEAT_EVERY_S=30s instead of after an hour of silence -- if rows_done stops advancing for more than ~5 minutes despite the semaphore having in-flight slots, kill the process (PID-based, per process_isolation rules), inspect the last heartbeat and the last few JSONL lines to identify which row_id(s) were in flight, and restart: RESUME logic in load_completed_rows() means the restart skips every already-terminal row and only retries what was truly in-flight, so no work is lost. If the SAME row_id hangs again on restart, that specific row is the culprit (not general infra) -- log it, skip it with a 'poison_row' status, and continue the sweep; do not let one row block the other 559.
  2. WALL-CLOCK BUDGET EXCEEDED even with robustness measures: if the full 560-row sweep has not reached completion_fraction=1.0 after a generous cap (e.g. 2x the pilot-extrapolated wall-clock, or 90 minutes, whichever is larger), stop the sweep, run the scoring step on whatever rows ARE in condition_c_progress.jsonl, and write method_out.json with completion_fraction < 1.0 explicitly set, plus a per-language-pair breakdown showing which pairs are under-represented in the partial sample -- per the direction's explicit partial-report fallback. Do not silently pad missing rows with any placeholder value.
  3. COST OVERRUN: if the pilot 20-row probe extrapolates to more than $2, first check whether MAX_PASSES=3 combined with C1-style per-sentence multi-violation repair (more violations found per sentence than C2's single-span repair) is driving more calls than expected -- this is a real, expected cost increase over C2 relative to C1's flat 1-call/violation, not necessarily a bug. If it still exceeds the shared $10 ceiling headroom (checking C1+C2's prior spend first), reduce MAX_PASSES to 2 for the full run and note the deviation from C2's budget in method_out.json, rather than skip the condition entirely.
  4. ROW-ID MISMATCH against C1/C2: if C2's exact 560-row population cannot be reconstructed byte-for-byte (e.g. C2 did not persist row IDs), fall back to re-deriving the population using C2's documented stratification code path with the SAME random seed, and explicitly flag in method_out.json that population identity is asserted-by-code-reuse rather than verified-by-row-ID-diff, so downstream evaluation knows the strength of the comparability claim.
  5. CHECKER/REPAIR-MODEL API FAILURE (OpenRouter outage, not a single hung call): if MAX_RETRIES is exhausted on a majority of rows in the pilot probe (not just one poison row), treat this as an upstream outage, pause, and retry the pilot after a delay before committing to the full sweep -- do not burn the full budget against a broken endpoint.
  6. If google/gemma-3-12b-it itself becomes unavailable on OpenRouter (mirroring the TowerPlus-9B delisting that forced this model choice in the first place), the resource dossier's re-ranked substitute table (art_5ySTX4YfxqG_) names the next candidate -- switch to it, note the deviation explicitly (this would break the fixed-repair-model-across-conditions design B/D/C1/C2/C rely on for comparability), and flag this prominently rather than silently swapping models.
testing_plan: |-
  1. DRY RUN ON 3 ROWS FIRST (before the 20-row pilot): pick 3 rows by hand (1 natural, 2 injected with clean single-violation cases) and run the full per-row loop synchronously with verbose logging. Manually inspect: does checker.find_all_violations() return a sensible violation list against the current pass's text (not the original), does the repair prompt look correct, does extract_repaired_text() correctly parse gemma-3-12b-it's output format (check for the same leaked-format issues B/D had to guard against -- gemma may format repairs differently than TowerPlus-9B did), does the JSONL line get written and is it valid JSON, does a certificate correctly trigger early-exit before MAX_PASSES.
  2. INSTRUMENTATION UNIT TEST: deliberately inject an artificial 90-second sleep into ONE mocked OpenRouter call (bypassing the real API) to confirm the CALL_TIMEOUT_S=75s timeout actually fires, the retry/backoff sequence logs correctly, and after MAX_RETRIES the row is marked hard-failed and the sweep continues past it rather than hanging -- this is the single most important test given what killed the prior attempt, so it must be verified BEFORE the full sweep, not inferred from the code reading correctly.
  3. RESUME TEST: run the 3-row dry run to completion, then re-invoke main() with the same OUT_JSONL present -- confirm load_completed_rows() correctly skips all 3 and logs 'resume: 3 rows already complete', proving resumability actually works before relying on it during a real stall recovery.
  4. 20-ROW PILOT (cost + timing probe, matches C2's $2 methodology): run the full pipeline (not mocked) on 20 stratified rows, record actual wall-clock and actual $ spent from OpenRouter usage fields, extrapolate linearly to 560 rows, and confirm the extrapolate stays under the shared $10 ceiling with C2's $0.045 as a sanity reference (a Condition-C extrapolate of low-single-digit-dollars is expected and fine; anything approaching $2+ warrants investigating why before scaling up, per the fallback plan).
  5. SANITY-CHECK PILOT RESULTS AGAINST C1/C2 BEFORE THE FULL RUN: on the 20 pilot rows, compute fix rate and ΔCOMET-direction (not full COMET, just spot-check whether repaired text looks more or less faithful than input) and confirm it is broadly consistent with C1/C2's established ranges (fix rate somewhere between C1's 0.6056 and C2's ~0.99, since C combines both mechanisms) -- if the pilot shows fix rate near 0 or wildly outside this envelope, stop and debug the repair/checker integration rather than scaling a broken pipeline to 560 rows.
  6. FULL SWEEP with heartbeat monitoring: launch the 560-row run as a background process per process_isolation rules (PID-tracked, never grep-by-name), tail the log for heartbeat lines to confirm steady rows_done progress every ~30s, and only proceed to scoring once completion_fraction reaches 1.0 or the wall-clock fallback cap is hit.
  7. POST-HOC VALIDATION: after scoring, confirm the output row counts match expectations exactly (320 natural + 240 injected = 560 total records in condition_c_progress.jsonl, no duplicates by row_id, no missing row_ids relative to the input population minus any explicitly-logged hard-failures), and confirm per-row ΔCOMET array length equals 320 exactly before treating the paired-bootstrap capability as available downstream.
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
