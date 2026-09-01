#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["loguru"]
# ///
"""Build the WMT25 translation error-correction dataset (natural + injected components).

Two source datasets (both already staged in temp/datasets/ by the earlier
discovery pass), standardized into the exp_sel_data_out schema, one row per
example:
  1. wmt25_task3_natural       -- official WMT25 Task 3 combined test set
                                   (wmt-conference/wmt25-mteval GitHub release)
  2. injected_error_augmentation -- programmatically corrupted rows built from
                                   held-out google/wmt24pp clean references
"""

import ast
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

RNG = random.Random(20260901)
ROOT = Path(__file__).parent
DATASETS_DIR = ROOT / "temp" / "datasets"
WMT25_TSV = DATASETS_DIR / "wmt25_task3_combined_test_set.tsv"
WMT24PP_DIR = DATASETS_DIR / "wmt24pp"
OUT_DIR = ROOT / "data_out"

LANG_CONFIGS = {
    "cs_CZ": "en-cs_CZ",
    "is_IS": "en-is_IS",
    "ja_JP": "en-ja_JP",
    "ru_RU": "en-ru_RU",
    "uk_UA": "en-uk_UA",
    "zh_CN": "en-zh_CN",
}

HELDOUT_FRAC = 0.18

# ---------------------------------------------------------------------------
# Category construction resources
# ---------------------------------------------------------------------------

NEGATION_CUES = {
    "cs_CZ": ["nikdy", "žádný", "žádná", "žádné", "nic", "nikoho", "není", "nejsou",
              "nemá", "nemají", "nebude", "nechce", "neví", "nemůže", "neudělal"],
    "is_IS": ["ekki", "aldrei", "enginn", "engin", "ekkert", "hvorki"],
    "ja_JP": ["ない", "ません", "なかった", "ありません", "できない"],
    "ru_RU": ["не", "нет", "никогда", "ничего", "никто", "нельзя"],
    "uk_UA": ["не", "ні", "ніколи", "нічого", "ніхто", "не можна"],
    "zh_CN": ["不", "没有", "没", "从不", "无法", "并非"],
}

QUANTIFIER_PAIRS = {
    "cs_CZ": [("všichni", "někteří"), ("všechny", "některé"), ("vždy", "nikdy"),
              ("nikdy", "vždy"), ("nikdo", "někdo"), ("nic", "něco"), ("občas", "nikdy")],
    "is_IS": [("allir", "sumir"), ("allar", "sumar"), ("alltaf", "aldrei"),
              ("aldrei", "alltaf"), ("enginn", "einhver"), ("ekkert", "eitthvað")],
    "ja_JP": [("すべて", "いくつか"), ("すべての", "一部の"), ("いつも", "決して"),
              ("誰も", "誰か"), ("常に", "時々")],
    "ru_RU": [("все", "некоторые"), ("всегда", "никогда"), ("никогда", "всегда"),
              ("никто", "кто-то"), ("ничего", "что-то"), ("каждый", "некоторые")],
    "uk_UA": [("усі", "деякі"), ("всі", "деякі"), ("завжди", "ніколи"),
              ("ніколи", "завжди"), ("ніхто", "хтось"), ("кожен", "деякі")],
    "zh_CN": [("所有", "一些"), ("总是", "从不"), ("从不", "总是"),
              ("每个", "某些"), ("从来没有", "有时"), ("没有人", "有人")],
}

# Explicit accented-letter case pairs per language (raw code-point ranges like
# A-Za-z do NOT extend correctly to Latin Extended accented characters, whose
# upper/lower forms are not laid out in a single contiguous range -- a naive
# [A-ZÀ-Ž] class matches stray lowercase letters like Icelandic "í").
CS_UPPER, CS_LOWER = "ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ", "áčďéěíňóřšťúůýž"
IS_UPPER, IS_LOWER = "ÁÐÉÍÓÚÝÞÆÖ", "áðéíóúýþæö"
LATIN_ENTITY_RE = re.compile(
    rf"[A-Z{CS_UPPER}{IS_UPPER}][a-z{CS_LOWER}{IS_LOWER}]+"
    rf"(?:\s[A-Z{CS_UPPER}{IS_UPPER}][a-z{CS_LOWER}{IS_LOWER}]+){{0,2}}"
)
CYRILLIC_ENTITY_RE = re.compile(r"[А-ЯЁІЇЄҐ][а-яёіїєґ'-]+(?:\s[А-ЯЁІЇЄҐ][а-яёіїєґ'-]+){0,2}")
YEAR_RE = re.compile(r"(?<![@\w])(1[89]\d{2}|20\d{2})(?!\w)")
NUMBER_RE = re.compile(r"(?<![@\w.])\d+(?:[.,]\d+)?(?!\w)")

STOP_WORDS_LATIN = {"The", "This", "That", "These", "Those", "A", "An", "It", "He", "She",
                     "They", "We", "You", "I"}

# Common closed-class words that get capitalized whenever they start a
# sentence/clause -- without a real NER model these are indistinguishable
# from proper nouns by capitalization alone, so they must be excluded by
# name. Demonstratives, pronouns, conjunctions, frequent adverbs.
ENTITY_STOP_WORDS = {
    "cs_CZ": {"Tato", "Tento", "Tyto", "Toto", "Ten", "Ta", "To", "Tento", "Tímto",
              "Ale", "Avšak", "Proto", "Podle", "Když", "Pokud", "Nicméně", "Také",
              "Proč", "Jak", "Kdy", "Kde", "Co", "Kdo", "My", "Vy", "Oni", "Ona",
              "On", "Jeho", "Její", "Jejich", "Náš", "Váš", "Ještě", "Už", "Teď",
              "Poté", "Potom", "Přesto", "Protože", "Takže", "Jenže", "Jinak"},
    "is_IS": {"Þetta", "Þessi", "Þessar", "Þessu", "Þessum", "Sá", "Sú", "Það", "Þau",
              "En", "Því", "Samt", "Samkvæmt", "Ef", "Þegar", "Hvers", "Hvernig",
              "Hvenær", "Hvar", "Hvað", "Hver", "Við", "Þið", "Þeir", "Hún", "Hann",
              "Hans", "Hennar", "Þeirra", "Okkar", "Ykkar", "Enn", "Núna", "Síðan"},
    "ru_RU": {"Это", "Этот", "Эта", "Эти", "Тот", "Та", "То", "Те", "Но", "Однако",
              "Поэтому", "Согласно", "Если", "Когда", "Почему", "Как", "Где", "Что",
              "Кто", "Мы", "Вы", "Они", "Она", "Он", "Его", "Её", "Их", "Наш", "Ваш",
              "Ещё", "Уже", "Теперь", "Потом", "Затем", "Тем", "Так", "Также"},
    "uk_UA": {"Це", "Цей", "Ця", "Ці", "Той", "Та", "То", "Ті", "Але", "Однак",
              "Тому", "Згідно", "Якщо", "Коли", "Чому", "Як", "Де", "Що", "Хто",
              "Ми", "Ви", "Вони", "Вона", "Він", "Його", "Її", "Їхній", "Наш", "Ваш",
              "Ще", "Вже", "Тепер", "Потім", "Отже", "Також"},
}


def _is_sentence_boundary_capitalization(text: str, start: int) -> bool:
    """True if `start` is right after sentence-ending punctuation (or the
    string start) -- i.e. the capitalization is just orthographic sentence-
    casing, not a signal of a proper noun."""
    prefix = text[:start].rstrip()
    if not prefix:
        return True
    return prefix[-1] in ".!?…”’\""


def _entity_matches(text: str, lang: str) -> list[re.Match]:
    stop = ENTITY_STOP_WORDS.get(lang, set()) | STOP_WORDS_LATIN
    out = []
    for m in entity_regex_for_lang(lang).finditer(text):
        if m.start() == 0 or len(m.group()) < 4:
            continue
        if m.group() in stop:
            continue
        if _is_sentence_boundary_capitalization(text, m.start()):
            continue
        out.append(m)
    return out


def entity_regex_for_lang(lang: str) -> re.Pattern:
    if lang in ("cs_CZ", "is_IS"):
        return LATIN_ENTITY_RE
    if lang in ("ru_RU", "uk_UA"):
        return CYRILLIC_ENTITY_RE
    return LATIN_ENTITY_RE  # zh_CN / ja_JP: catches embedded Latin-script entities only


def extract_entities(text: str, lang: str) -> list[str]:
    return [m.group() for m in _entity_matches(text, lang)]


ENTITY_MAX_CORPUS_FREQ = 3  # a real proper noun is rare across ~960 rows; a
# capitalization false positive (function word capitalized by clause
# position) recurs far more often -- this is a corpus-frequency check in
# the same spirit as the plan's "collides with an existing natural
# occurrence" discard rule, generalized to catch stopword-heuristic misses
# no hand-built per-language stoplist would fully cover.


def build_entity_pools(rows_by_lang: dict) -> dict:
    """First pass: collect same-language distractor entity candidates from clean
    text, keeping only candidates that are RARE corpus-wide (proper-noun-like)."""
    freq = defaultdict(Counter)
    for lang, rows in rows_by_lang.items():
        for r in rows:
            for ent in extract_entities(r["target"], lang):
                freq[lang][ent] += 1
    pools = {}
    for lang, counts in freq.items():
        pools[lang] = sorted(w for w, c in counts.items() if c <= ENTITY_MAX_CORPUS_FREQ)
        logger.info(
            f"entity distractor pool[{lang}] = {len(pools[lang])} candidates "
            f"(of {len(counts)} raw capitalized candidates before frequency filter)"
        )
    return {"pool": pools, "freq": freq}


# ---------------------------------------------------------------------------
# Corruption functions -- each returns None or
# (corrupted_text, original_span, corrupted_span, (start, end)) using
# character offsets into the ORIGINAL clean text.
# ---------------------------------------------------------------------------

def corrupt_entity(text: str, lang: str, pool: list[str], freq: Counter) -> tuple | None:
    if not pool:
        return None
    ents = [m for m in _entity_matches(text, lang) if freq.get(m.group(), 0) <= ENTITY_MAX_CORPUS_FREQ]
    if not ents:
        return None
    m = RNG.choice(ents)
    original = m.group()
    candidates = [e for e in pool if e != original]
    RNG.shuffle(candidates)
    for distractor in candidates[:8]:
        # discard if the distractor already occurs naturally elsewhere in the sentence
        rest = text[:m.start()] + text[m.end():]
        if distractor in rest:
            continue
        corrupted_text = text[: m.start()] + distractor + text[m.end():]
        return corrupted_text, original, distractor, (m.start(), m.end())
    return None


def _perturb_number_str(num_str: str) -> str | None:
    digits = [c for c in num_str if c.isdigit()]
    if not digits:
        return None
    first_digit_idx = next(i for i, c in enumerate(num_str) if c.isdigit())
    d = int(num_str[first_digit_idx])
    new_d = d + 1 if d < 9 else d - 1
    if first_digit_idx == 0 and new_d == 0 and len(digits) > 1:
        new_d = 1
    return num_str[:first_digit_idx] + str(new_d) + num_str[first_digit_idx + 1:]


def corrupt_number(text: str, lang: str) -> tuple | None:
    m = YEAR_RE.search(text)
    if m:
        new_val = _perturb_number_str(m.group())
        if new_val and new_val != m.group():
            corrupted_text = text[: m.start()] + new_val + text[m.end():]
            return corrupted_text, m.group(), new_val, (m.start(), m.end())
    m = NUMBER_RE.search(text)
    if m:
        new_val = _perturb_number_str(m.group())
        if new_val and new_val != m.group():
            corrupted_text = text[: m.start()] + new_val + text[m.end():]
            return corrupted_text, m.group(), new_val, (m.start(), m.end())
    return None


def corrupt_negation(text: str, lang: str) -> tuple | None:
    cues = NEGATION_CUES.get(lang, [])
    # Slavic/Czech/Ukrainian and colloquial Chinese use negative concord --
    # multiple negation markers can co-occur in one clause without cancelling
    # each other (e.g. cs "Nikdy nic není snadné" = triple negation, still
    # negative after removing one marker). Only flip when exactly one marker
    # total is present, so removing/inserting it is guaranteed to change polarity.
    total_hits = sum(len(_cue_occurrences(text, cue, lang)) for cue in cues)
    if total_hits != 1:
        return None
    for cue in cues:
        matches = _cue_occurrences(text, cue, lang)
        if not matches:
            continue
        idx, end = matches[0].start(), matches[0].end()
        # collapse one adjacent space if present, to keep the sentence well-formed
        new_end = end + 1 if end < len(text) and text[end] == " " else end
        new_start = idx - 1 if new_end == end and idx > 0 and text[idx - 1] == " " else idx
        corrupted_text = text[:new_start] + text[new_end:]
        return corrupted_text, text[idx:end], "", (idx, end)
    return None


def corrupt_quantifier(text: str, lang: str) -> tuple | None:
    pairs = QUANTIFIER_PAIRS.get(lang, [])
    for orig, repl in pairs:
        matches = _cue_occurrences(text, orig, lang)
        if not matches:
            continue
        idx, end = matches[0].start(), matches[0].end()
        corrupted_text = text[:idx] + repl + text[end:]
        return corrupted_text, orig, repl, (idx, end)
    return None


CATEGORY_FUNCS = {
    "named_entity_swap": corrupt_entity,
    "number_unit_date_alteration": corrupt_number,
    "negation_polarity_flip": corrupt_negation,
    "quantifier_substitution": corrupt_quantifier,
}

MAX_PER_CELL = 130  # cap per (language_pair, category) for balance, not raw volume

# cs_CZ/is_IS/ru_RU/uk_UA are space-delimited -- match cue/quantifier tokens on
# word boundaries so e.g. Cyrillic "не" does not fire inside "нервах", or
# Czech "nic" inside "nich". zh_CN/ja_JP have no inter-word spaces, so cues
# are matched as substrings (a single Han/kana negation morpheme is itself
# the semantic unit there, unlike a Latin/Cyrillic root).
WORD_BOUNDARY_LANGS = {"cs_CZ", "is_IS", "ru_RU", "uk_UA"}


def _cue_occurrences(text: str, cue: str, lang: str) -> list[re.Match]:
    if lang in WORD_BOUNDARY_LANGS:
        return list(re.finditer(rf"\b{re.escape(cue)}\b", text))
    return [m for m in re.finditer(re.escape(cue), text)]


# ---------------------------------------------------------------------------
# Natural component (WMT25 Task 3)
# ---------------------------------------------------------------------------

def load_wmt25_natural() -> list[dict]:
    csv.field_size_limit(10_000_000)
    with WMT25_TSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)
    logger.info(f"loaded {len(rows)} natural WMT25 Task3 rows")

    examples = []
    for r in rows:
        lang = r["target_lang"]
        lp = f"en-{lang}"
        try:
            spans = ast.literal_eval(r["error_spans"]) if r["error_spans"] else []
        except (ValueError, SyntaxError):
            spans = []
        examples.append(
            {
                "input": r["source_segment"],
                "output": r["hypothesis_segment"],
                "metadata_language_pair": lp,
                "metadata_domain": r["domain_name"],
                "metadata_qe_flagged_spans": spans,
                "metadata_human_error_annotations": None,
                "metadata_provenance": "natural",
                "metadata_invariant_category": None,
                "metadata_source_dataset": "wmt-conference/wmt25-mteval:wmt25_task3_combined_test_set",
                "metadata_doc_id": r["doc_id"],
                "metadata_segment_id": r["segment_id"],
                "metadata_system_id": r["system_id"],
                "metadata_overall_qe_score": float(r["overall"]) if r["overall"] else None,
                "metadata_notes": (
                    "QE error spans are the CometKiwi-derived spans released pre-scoring "
                    "(character offsets into output/hypothesis_segment, severity in "
                    "{minor,major,critical}). No post-hoc human MQM severity/type gold "
                    "layer matching the findings-paper Table 15 is publicly released as of "
                    "this build (post_edit column empty for all 6000 rows) -- treat "
                    "qe_flagged_spans as the operational localization signal, per the "
                    "dataset_search_plan's documented fallback."
                ),
            }
        )
    return examples


def assign_natural_folds(examples: list[dict]) -> None:
    by_lp = defaultdict(list)
    for ex in examples:
        by_lp[ex["metadata_language_pair"]].append(ex)
    for lp, group in by_lp.items():
        RNG.shuffle(group)
        n_heldout = max(1, round(len(group) * HELDOUT_FRAC))
        for ex in group[:n_heldout]:
            ex["metadata_fold"] = "checker_validation_heldout"
        for ex in group[n_heldout:]:
            ex["metadata_fold"] = "experimental_pool"
        logger.info(f"natural[{lp}]: {len(group)} total, {n_heldout} heldout")


# ---------------------------------------------------------------------------
# Injected component (built from wmt24pp clean references)
# ---------------------------------------------------------------------------

def load_wmt24pp_clean() -> dict:
    rows_by_lang = {}
    for lang, cfg in LANG_CONFIGS.items():
        path = WMT24PP_DIR / f"full_google_wmt24pp_{cfg}_train.json"
        data = json.loads(path.read_text())
        clean = [
            r for r in data
            if not r["is_bad_source"] and r["domain"] != "canary" and r["target"].strip()
        ]
        rows_by_lang[lang] = clean
        logger.info(f"wmt24pp[{lang}]: {len(clean)} usable clean rows (of {len(data)})")
    return rows_by_lang


def build_injected_examples(rows_by_lang: dict, pools: dict) -> list[dict]:
    examples = []
    counts = defaultdict(int)
    for lang, rows in rows_by_lang.items():
        lp = f"en-{lang}"
        shuffled = rows[:]
        RNG.shuffle(shuffled)
        for r in shuffled:
            target = r["target"]
            for category, func in CATEGORY_FUNCS.items():
                cell = (lp, category)
                if counts[cell] >= MAX_PER_CELL:
                    continue
                if category == "named_entity_swap":
                    result = func(target, lang, pools["pool"].get(lang, []), pools["freq"].get(lang, Counter()))
                else:
                    result = func(target, lang)
                if result is None:
                    continue
                corrupted_text, orig_span, corrupted_span, (start, end) = result
                if corrupted_text.strip() == target.strip():
                    continue
                examples.append(
                    {
                        "input": r["source"],
                        "output": corrupted_text,
                        "metadata_language_pair": lp,
                        "metadata_domain": r["domain"],
                        "metadata_qe_flagged_spans": None,
                        "metadata_human_error_annotations": None,
                        "metadata_provenance": "injected",
                        "metadata_invariant_category": category,
                        "metadata_source_dataset": "google/wmt24pp",
                        "metadata_doc_id": r["document_id"],
                        "metadata_segment_id": r["segment_id"],
                        "metadata_system_id": None,
                        "metadata_overall_qe_score": None,
                        "metadata_clean_target_text": target,
                        "metadata_original_span": orig_span,
                        "metadata_corrupted_span": corrupted_span,
                        "metadata_span_offsets": {"start": start, "end": end},
                        "metadata_notes": (
                            f"Programmatically corrupted from a held-out wmt24pp "
                            f"(google/wmt24pp, WMT24++ human post-edited target, "
                            f"a corpus wholly disjoint from the WMT25 Task 3 test set "
                            f"used for the natural component) clean reference. Category="
                            f"{category}. Ground truth = metadata_clean_target_text."
                        ),
                    }
                )
                counts[cell] += 1
    for cell, n in sorted(counts.items()):
        logger.info(f"injected[{cell[0]}][{cell[1]}] = {n}")
    logger.info(f"total injected examples: {len(examples)}")
    return examples


def assign_injected_folds(examples: list[dict]) -> None:
    by_cell = defaultdict(list)
    for ex in examples:
        by_cell[(ex["metadata_language_pair"], ex["metadata_invariant_category"])].append(ex)
    for cell, group in by_cell.items():
        RNG.shuffle(group)
        n_heldout = max(1, round(len(group) * HELDOUT_FRAC))
        for ex in group[:n_heldout]:
            ex["metadata_fold"] = "checker_validation_heldout"
        for ex in group[n_heldout:]:
            ex["metadata_fold"] = "experimental_pool"


@logger.catch(reraise=True)
def main():
    OUT_DIR.mkdir(exist_ok=True)

    logger.info("=== building natural WMT25 Task3 component ===")
    natural_examples = load_wmt25_natural()
    assign_natural_folds(natural_examples)

    logger.info("=== building injected-error component ===")
    rows_by_lang = load_wmt24pp_clean()
    pools = build_entity_pools(rows_by_lang)
    injected_examples = build_injected_examples(rows_by_lang, pools)
    assign_injected_folds(injected_examples)

    output = {
        "metadata": {
            "title": "WMT25 Translation Error-Correction Data",
            "natural_source": (
                "wmt-conference/wmt25-mteval GitHub repo, "
                "data/testset/wmt25_task3_combined_test_set.tsv, WMT25 Task 3 official "
                "test set (6 en->X language pairs x 1000 segments = 6000 rows), released "
                "2025-07-24, https://www2.statmt.org/wmt25/mteval-subtask.html"
            ),
            "injected_source": (
                "google/wmt24pp (HuggingFace), WMT24++: Expanding the Language Coverage "
                "of WMT24 to 55 Languages & Dialects (arXiv:2502.12404); human "
                "post-edited target text used as the clean base for programmatic "
                "corruption, wholly disjoint corpus/year from the WMT25 Task3 natural "
                "component"
            ),
            "language_pairs": sorted(f"en-{k}" for k in LANG_CONFIGS),
            "invariant_categories": list(CATEGORY_FUNCS.keys()),
            "metadata_fold_values": ["experimental_pool", "checker_validation_heldout"],
            "known_gap": (
                "No public post-hoc human MQM severity/type gold layer for WMT25 Task 3 "
                "was found (post_edit column of the official release is empty for all "
                "6000 rows); qe_flagged_spans (CometKiwi-derived) is used as the "
                "operational localization signal instead, per the plan's documented "
                "fallback. named_entity_swap recall is lower for zh_CN/ja_JP because "
                "those scripts carry no capitalization signal -- entities are only "
                "detected via embedded Latin-script substrings, a documented NER-tooling "
                "coverage gap rather than a full multilingual-NER pass. named_entity_swap "
                "for cs_CZ/is_IS/ru_RU/uk_UA uses a capitalization heuristic (no spaCy/HF "
                "NER model available offline), filtered by a per-language function-word "
                "stoplist, a sentence-boundary-capitalization exclusion, and a corpus-"
                "frequency cap (a real proper noun recurs rarely across ~960 rows; a "
                "capitalized function word recurs often) -- this removes the large "
                "majority of false positives but is not equivalent to true NER, so a small "
                "residual fraction of named_entity_swap rows may swap a capitalized common "
                "word rather than a genuine entity; downstream consumers relying on exact "
                "entity-type precision should treat this category's rows as heuristic-"
                "screened, not gold-verified."
            ),
        },
        "datasets": [
            {"dataset": "wmt25_task3_natural", "examples": natural_examples},
            {"dataset": "injected_error_augmentation", "examples": injected_examples},
        ],
    }

    out_path = OUT_DIR / "full_data_out.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"wrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")
    logger.info(f"natural: {len(natural_examples)} examples, injected: {len(injected_examples)} examples")


if __name__ == "__main__":
    main()
