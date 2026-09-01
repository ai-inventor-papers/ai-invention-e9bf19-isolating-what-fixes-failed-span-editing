#!/usr/bin/env python3
"""checker_module.py -- importable, deterministic content-invariant checker.

Implements the four-category checker (named_entity_swap, number_unit_date_alteration,
negation_polarity_flip, quantifier_substitution) across {zh_CN, cs_CZ, ja_JP, is_IS,
ru_RU, uk_UA}, plus a language-naive BASELINE checker for comparison.

Every detector is a pure function ``detect(source_text, target_text, lang) -> list[(start, end)]``
returning character-offset spans INTO `target_text` that the checker flags as candidate
sites of that invariant category. Detectors are independent of any specific dataset row;
they only see the (English source, target-language output) pair, exactly as a checker
would at inference/QE time -- they never see the ground-truth corruption metadata.

Resourcing decisions (see the resource dossier, art_5ySTX4YfxqG_):
  - named_entity_swap: stanza NER for languages stanza covers with a trained NER model
    (zh, ja, ru, uk per the dossier's correction of Stanza's coverage); a documented
    regex/capitalization fallback for languages stanza does NOT ship NER for (cs, is --
    exactly the gap the dossier flags: NameTag3/IceBERT would close it but require a
    non-Python API dependency / gated download respectively, so per FALLBACK_PLAN this
    substitutes a heuristic and logs it rather than silently degrading).
  - number_unit_date_alteration: regex only, uniformly across all six languages, per
    FALLBACK_PLAN ("if Duckling is not installable/reachable ... fall back uniformly to
    the regex-based number/unit/date parser for all six languages"). Digits, dates and
    currency symbols are script-independent, so one regex set serves every language.
  - negation_polarity_flip: corruption is a DELETION (the single negation cue in the
    segment is removed -- construction guarantees exactly one cue was present, so
    target-only presence detection at the ground-truth offset is structurally impossible:
    there is nothing left there to point at). Implemented instead as a CROSS-LINGUAL
    polarity-mismatch check: English negation-cue presence in `source` vs. target-language
    negation-cue presence in `target`; a mismatch flags the whole segment. This is the
    SENTENCE-LEVEL fallback the artifact plan's own fallback_plan anticipates.
  - quantifier_substitution: corruption is an IN-PLACE word swap (kept at the same start
    offset), so target-only span detection works directly: flag every occurrence of any
    known closed-class quantifier word.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

Span = tuple[int, int]

LANGUAGES = ["zh_CN", "cs_CZ", "ja_JP", "is_IS", "ru_RU", "uk_UA"]

WORD_BOUNDARY_LANGS = {"cs_CZ", "is_IS", "ru_RU", "uk_UA"}  # space-delimited scripts

# ---------------------------------------------------------------------------
# Category 2: number / unit / date alteration -- regex, script-independent
# ---------------------------------------------------------------------------

_YEAR_RE = re.compile(r"(?<![@\w])(1[5-9]\d{2}|20\d{2}|21\d{2})(?!\w)")
_DATE_RE = re.compile(r"(?<!\w)\d{1,4}[./-]\d{1,2}[./-]\d{1,4}(?!\w)")
_CURRENCY_RE = re.compile(
    r"[$€£¥₽₴]\s?\d[\d,.\s]*"
    r"|\d[\d,.\s]*\s?(?:USD|EUR|CZK|ISK|RUB|UAH|JPY|CNY|Kč|kr)\b",
    re.IGNORECASE,
)
_NUMBER_RE = re.compile(r"(?<![@\w.,])\d+(?:[.,]\d+)?%?(?!\w)")


def _dedup_overlaps(spans: set[Span]) -> list[Span]:
    """Keep the widest span at each overlapping cluster (e.g. a date subsumes a bare year)."""
    ordered = sorted(spans, key=lambda s: (s[0], -(s[1] - s[0])))
    out: list[Span] = []
    for s in ordered:
        if any(s[0] >= o[0] and s[1] <= o[1] for o in out):
            continue
        out.append(s)
    return sorted(out)


def detect_number_unit_date(source: str, target: str, lang: str) -> list[Span]:
    spans: set[Span] = set()
    for rx in (_DATE_RE, _CURRENCY_RE, _YEAR_RE, _NUMBER_RE):
        for m in rx.finditer(target):
            if m.end() > m.start():
                spans.add((m.start(), m.end()))
    return _dedup_overlaps(spans)


def detect_number_unit_date_baseline(source: str, target: str, lang: str) -> list[Span]:
    """Language-naive baseline: bare digit runs only, no date/currency/year awareness."""
    return _dedup_overlaps({(m.start(), m.end()) for m in re.finditer(r"\d+(?:[.,]\d+)?", target)})


# ---------------------------------------------------------------------------
# Category 1: named entity swap
# ---------------------------------------------------------------------------

CS_UPPER, CS_LOWER = "ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ", "áčďéěíňóřšťúůýž"
IS_UPPER, IS_LOWER = "ÁÐÉÍÓÚÝÞÆÖ", "áðéíóúýþæö"
_LATIN_ENTITY_RE = re.compile(
    rf"[A-Z{CS_UPPER}{IS_UPPER}][a-z{CS_LOWER}{IS_LOWER}]+(?:\s[A-Z{CS_UPPER}{IS_UPPER}][a-z{CS_LOWER}{IS_LOWER}]+){{0,2}}"
)
_CYRILLIC_ENTITY_RE = re.compile(r"[А-ЯЁІЇЄҐ][а-яёіїєґ'-]+(?:\s[А-ЯЁІЇЄҐ][а-яёіїєґ'-]+){0,2}")

# Independently-curated closed-class stopwords (demonstratives / pronouns / conjunctions /
# frequent sentence-initial adverbs) that a naive capitalization heuristic must exclude for
# cs_CZ / is_IS -- these are the two languages stanza has no trained NER model for.
_ENTITY_STOPWORDS = {
    "cs_CZ": {"Tato", "Tento", "Tyto", "Toto", "Ten", "Ta", "To", "Ale", "Avšak", "Proto",
              "Podle", "Když", "Pokud", "Nicméně", "Také", "Proč", "Jak", "Kdy", "Kde", "Co",
              "Kdo", "My", "Vy", "Oni", "Ona", "On", "Jeho", "Její", "Jejich", "Náš", "Váš",
              "Ještě", "Už", "Teď", "Poté", "Potom", "Přesto", "Protože", "Takže"},
    "is_IS": {"Þetta", "Þessi", "Þessar", "Þessu", "Sá", "Sú", "Það", "Þau", "En", "Því",
              "Samt", "Samkvæmt", "Ef", "Þegar", "Hvers", "Hvernig", "Hvenær", "Hvar", "Hvað",
              "Hver", "Við", "Þið", "Þeir", "Hún", "Hann", "Hans", "Hennar", "Þeirra", "Okkar",
              "Enn", "Núna", "Síðan"},
}
_STOP_LATIN_GENERIC = {"The", "This", "That", "These", "Those", "A", "An", "It", "He", "She",
                        "They", "We", "You", "I"}


def _is_sentence_start(text: str, start: int) -> bool:
    prefix = text[:start].rstrip()
    return not prefix or prefix[-1] in ".!?…”’\""


def detect_entity_regex(source: str, target: str, lang: str) -> list[Span]:
    """Capitalization-heuristic entity detector used where no trained NER model is available."""
    if lang in ("ru_RU", "uk_UA"):
        rx = _CYRILLIC_ENTITY_RE
        stop: set[str] = set()
    else:
        rx = _LATIN_ENTITY_RE
        stop = _ENTITY_STOPWORDS.get(lang, set()) | _STOP_LATIN_GENERIC
    out = []
    for m in rx.finditer(target):
        if len(m.group()) < 3 or m.group() in stop:
            continue
        if _is_sentence_start(target, m.start()):
            continue
        out.append((m.start(), m.end()))
    return out


def detect_entity_baseline(source: str, target: str, lang: str) -> list[Span]:
    """Language-naive baseline: Latin-capitalization regex applied uniformly to every
    language regardless of script, with no stopword filtering -- a generic off-the-shelf
    heuristic with zero localization effort."""
    return [(m.start(), m.end()) for m in _LATIN_ENTITY_RE.finditer(target) if len(m.group()) >= 3]


# ---------------------------------------------------------------------------
# Category 3: negation polarity flip -- cross-lingual sentence-level check
# ---------------------------------------------------------------------------

_EN_NEG_RE = re.compile(
    r"\b(?:not|never|none|nobody|nothing|neither|nor|without|hardly|barely|scarcely|"
    r"cannot|no)\b|n't",
    re.IGNORECASE,
)

NEGATION_CUES = {
    "cs_CZ": ["nikdy", "žádný", "žádná", "žádné", "žádného", "žádnou", "nic", "nikoho",
              "není", "nejsou", "nemá", "nemají", "nebude", "nechce", "neví", "nemůže",
              "neudělal", "nedělá"],
    "is_IS": ["ekki", "aldrei", "enginn", "engin", "ekkert", "hvorki", "engum", "engan"],
    "ja_JP": ["ない", "ません", "なかった",
              "ありません", "できない"],
    "ru_RU": ["не", "нет", "никогда", "ничего", "никто", "нельзя"],
    "uk_UA": ["не", "ні", "ніколи", "нічого", "ніхто"],
    "zh_CN": ["不", "没有", "没", "从不", "无法", "并非", "未"],
}


def _cue_occurrences(text: str, cue: str, lang: str) -> list[re.Match]:
    if lang in WORD_BOUNDARY_LANGS:
        return list(re.finditer(rf"\b{re.escape(cue)}\b", text))
    return list(re.finditer(re.escape(cue), text))


def detect_negation_flip(source: str, target: str, lang: str) -> list[Span]:
    src_hits = len(list(_EN_NEG_RE.finditer(source)))
    cues = NEGATION_CUES.get(lang, [])
    tgt_hits = sum(len(_cue_occurrences(target, c, lang)) for c in cues)
    src_has_neg = src_hits >= 1
    tgt_has_neg = tgt_hits >= 1
    if src_has_neg != tgt_has_neg:
        return [(0, len(target))]  # sentence-level flag: polarity mismatch, per fallback_plan
    return []


def detect_negation_baseline(source: str, target: str, lang: str) -> list[Span]:
    """Language-naive baseline: no per-language negation-cue resource -> never fires."""
    return []


# ---------------------------------------------------------------------------
# Category 4: quantifier substitution -- target-only closed-class word list
# ---------------------------------------------------------------------------

QUANTIFIER_WORDS = {
    "cs_CZ": ["všichni", "všechny", "všechna", "někteří", "některé", "některá", "vždy",
              "nikdy", "nikdo", "někdo", "nic", "něco", "občas", "každý", "žádný"],
    "is_IS": ["allir", "allar", "öll", "sumir", "sumar", "alltaf", "aldrei", "enginn",
              "einhver", "ekkert", "eitthvað", "hver"],
    "ja_JP": ["すべて", "すべての", "一部の",
              "いつも", "決して", "誰も", "誰か",
              "常に", "時々"],
    "ru_RU": ["все", "некоторые", "всегда", "никогда", "никто", "кто-то", "ничего",
              "что-то", "каждый", "любой"],
    "uk_UA": ["усі", "всі", "деякі", "завжди", "ніколи", "ніхто", "хтось", "кожен",
              "будь-який"],
    "zh_CN": ["所有", "一些", "总是", "从不", "每个",
              "某些", "从来没有", "有时", "任何"],
}


def detect_quantifier(source: str, target: str, lang: str) -> list[Span]:
    words = QUANTIFIER_WORDS.get(lang, [])
    out = []
    for w in words:
        for m in _cue_occurrences(target, w, lang):
            out.append((m.start(), m.end()))
    return _dedup_overlaps(set(out))


def detect_quantifier_baseline(source: str, target: str, lang: str) -> list[Span]:
    """Language-naive baseline: no per-language quantifier-word resource -> never fires."""
    return []


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CATEGORY_KEYS = [
    "named_entity_swap",
    "number_unit_date_alteration",
    "negation_polarity_flip",
    "quantifier_substitution",
]

BASELINE_DETECTORS = {
    "named_entity_swap": detect_entity_baseline,
    "number_unit_date_alteration": detect_number_unit_date_baseline,
    "negation_polarity_flip": detect_negation_baseline,
    "quantifier_substitution": detect_quantifier_baseline,
}


@dataclass
class CheckerRegistry:
    """Holds the resolved entity detector per language (stanza NER where available,
    regex fallback otherwise) plus the three regex/rule detectors shared across languages."""

    entity_fn_by_lang: dict = field(default_factory=dict)
    substitutions: dict = field(default_factory=dict)  # lang -> reason string, logged

    def detect(self, category: str, source: str, target: str, lang: str) -> list[Span]:
        if category == "named_entity_swap":
            fn = self.entity_fn_by_lang.get(lang, detect_entity_regex)
            return fn(source, target, lang)
        if category == "number_unit_date_alteration":
            return detect_number_unit_date(source, target, lang)
        if category == "negation_polarity_flip":
            return detect_negation_flip(source, target, lang)
        if category == "quantifier_substitution":
            return detect_quantifier(source, target, lang)
        raise ValueError(f"unknown category {category}")

    def detect_baseline(self, category: str, source: str, target: str, lang: str) -> list[Span]:
        return BASELINE_DETECTORS[category](source, target, lang)


def overlaps(a: Span, b: Span) -> bool:
    return a[0] < b[1] and b[0] < a[1]


def any_overlap(spans: list[Span], gt: Span) -> bool:
    return any(overlaps(s, gt) for s in spans)
