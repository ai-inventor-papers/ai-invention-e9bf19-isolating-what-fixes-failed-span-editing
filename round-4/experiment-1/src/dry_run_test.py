#!/usr/bin/env python3
"""Testing plan step 1-3: 3-row dry run, timeout-injection unit test, resume test.
NOT part of the production pipeline -- standalone verification, uses its own
JSONL path so it never touches condition_c_progress.jsonl."""
import asyncio
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import method as m
from checker import Checker
from llm_client import CostLedger, OpenRouterClient


def load_3_rows():
    data = m.load_data()
    by_dataset = m.index_examples(data)
    rng = random.Random(m.SEED)
    natural_rows = m.stratified_sample_natural(by_dataset["wmt25_task3_natural"], rng)
    injected_rows = m.stratified_sample_injected(by_dataset["injected_error_augmentation"], rng, "experimental_pool", m.N_INJECTED_PER_CELL)
    nat1 = natural_rows[0]
    # pick 2 injected rows: one clean single-violation (number/date), one negation-deletion if available
    inj_number = next(r for r in injected_rows if r["metadata_invariant_category"] == "number_unit_date_alteration")
    inj_negation = next((r for r in injected_rows if m.is_negation_deletion_row(r)), injected_rows[1])
    return nat1, inj_number, inj_negation


async def step1_dry_run():
    print("=== STEP 1: dry run on 3 rows ===")
    nat1, inj_number, inj_negation = load_3_rows()
    checker = Checker(excluded_cells=set())  # unrestricted for the dry run inspection
    ledger = CostLedger(cap_usd=0.5)
    sweep_state = {"rows_done": 0, "total": 3, "done": False, "last_progress_ts": time.monotonic(),
                    "in_flight": 0, "ledger": ledger}
    async with OpenRouterClient(ledger, max_concurrency=3, timeout_s=90) as client:
        for label, row, is_injected in [("natural", nat1, False), ("injected_number", inj_number, True), ("injected_negation", inj_negation, True)]:
            pair = row["metadata_language_pair"]
            lang = m.LANG_KEY_OF_PAIR[pair]
            lang_name = m.LANG_NAME_OF_PAIR[pair]
            source = row["input"]
            text = row["output"]
            print(f"\n--- {label} ({pair}) row_id={row['_row_id']} ---")
            flags = await asyncio.to_thread(m._detect_all_sync, checker, source, text, lang)
            print(f"pass-1 flags: {[(f.category, f.text) for f in flags]}")
            result = await m.run_condition_c_core(source, text, lang, lang_name, row["_row_id"], client, checker, sweep_state)
            print(f"n_passes={result['n_passes']} n_llm_calls={result['n_llm_calls']} certificate={result['certificate_achieved']} no_op={result['no_op']} hard_failed={result['hard_failed']}")
            print(f"output[:200]={result['output'][:200]!r}")
            for p in result["pass_log"]:
                print("  pass", p.get("pass_num"), "n_flags", p.get("n_flags"), "edit_dist", p.get("edit_distance_chars"), "err", p.get("error"))
            if is_injected:
                verdict = m.compute_fix_and_regression(row, result["output"], lang, checker)
                print("verdict:", verdict)
            # sanity checks
            assert isinstance(result["output"], str) and len(result["output"]) > 0
            assert "certificate_achieved" in result
    print("\nSTEP 1 PASSED")


async def step2_timeout_injection():
    print("\n=== STEP 2: timeout-injection unit test ===")
    ledger = CostLedger(cap_usd=0.5)

    class FakeClient:
        async def call(self, model, prompt, **kwargs):
            await asyncio.sleep(90)  # deliberately exceeds CALL_TIMEOUT_S=75
            return {"success": True, "text": "should never reach here", "error": None,
                    "input_tokens": 0, "output_tokens": 0}

    sweep_state = {"rows_done": 0, "total": 1, "done": False, "last_progress_ts": time.monotonic(),
                    "in_flight": 0, "ledger": ledger}
    orig_max_retries, orig_timeout = m.MAX_RETRIES, m.CALL_TIMEOUT_S
    m.MAX_RETRIES = 2  # keep the unit test fast: 2 retries x (2s backoff) instead of 3 x up-to-32s
    m.CALL_TIMEOUT_S = 2.0  # small timeout so the injected 90s sleep reliably trips it fast
    t0 = time.monotonic()
    result = await m.call_with_timeout_and_retry(FakeClient(), "fake-model", "prompt", "test_row", 1, sweep_state)
    elapsed = time.monotonic() - t0
    m.MAX_RETRIES, m.CALL_TIMEOUT_S = orig_max_retries, orig_timeout
    print(f"elapsed={elapsed:.1f}s result={result}")
    assert result is None, "expected hard-fail (None) after exhausting retries against a hung call"
    assert elapsed < 30, f"timeout+retry logic took too long ({elapsed:.1f}s) -- should be bounded, not hang"
    print("STEP 2 PASSED: timeout fired, retries exhausted, row marked hard-failed, no hang")


def step3_resume_test():
    print("\n=== STEP 3: resume test ===")
    test_jsonl = Path(__file__).parent / "dry_run_test_progress.jsonl"
    if test_jsonl.exists():
        test_jsonl.unlink()
    fake_records = [{"row_id": f"test:{i}", "kind": "natural", "status": "certificate"} for i in range(3)]
    with open(test_jsonl, "w") as f:
        for r in fake_records:
            f.write(json.dumps(r) + "\n")
    completed = m.load_completed_rows(test_jsonl)
    assert len(completed) == 3, f"expected 3 completed rows, got {len(completed)}"
    assert all(f"test:{i}" in completed for i in range(3))
    test_jsonl.unlink()
    print("STEP 3 PASSED: resume correctly skips 3/3 already-terminal rows")


async def main():
    await step1_dry_run()
    await step2_timeout_injection()
    step3_resume_test()
    print("\nALL DRY-RUN TESTS PASSED")


if __name__ == "__main__":
    asyncio.run(main())
