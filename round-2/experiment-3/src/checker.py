"""Four-category deterministic content-invariant checker for ru_RU / uk_UA.

Categories: named_entity, number_unit_date, negation_polarity, quantifier_scope.

Design (per the resource dossier, art_5ySTX4YfxqG_, Block D):
- named_entity: Stanza NER over the hypothesis text (per-language pipeline).
- number_unit_date: script-independent regex over digit sequences (+ optional
  attached unit/word token), with a boundary guard against handle-like tokens
  (e.g. @user12).
- negation_polarity: per-language cue-word list, word-boundary match, ONLY
  fires when exactly one negation marker is present in the sentence (Slavic
  negative-concord caveat documented in the dossier).
- quantifier_scope: closed-class quantifier word list per language.

The checker's role is CANDIDATE LOCALIZATION of invariant-bearing spans (it
does not itself judge cross-lingual correctness -- that judgement is
delegated to the LLM repair call in condition C1, which sees both source and
hypothesis). Precision/recall against the injected_error_augmentation
heldout fold is therefore a localization metric: does the detector's flagged
span set overlap the single known-corrupted span in that sentence. This is
an intentionally conservative precision estimate (documented in
method_out.json) because every OTHER genuine entity/number/etc. the
detector also flags in the same sentence counts against precision, even
though flagging a real invariant is exactly what a localizer should do -- the
heldout fold only labels the ONE span that was corrupted, not every
invariant-bearing span in the sentence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

CATEGORIES = (
    "named_entity",
    "number_unit_date",
    "negation_polarity",
    "quantifier_scope",
)

SUPPORTED_LANGS = ("ru_RU", "uk_UA")

# --- number/unit/date -------------------------------------------------------
# Script-independent digit-sequence regex + an optional attached unit/word
# token (letters immediately following, any script). Boundary guard: a digit
# run immediately preceded by '@' (handle-like token, e.g. @user12) is
# excluded.
_NUMBER_RE = re.compile(
    r"(?<![@\w])\d+(?:[.,]\d+)*\s?[A-Za-zА-Яа-яЁёІіЇїЄєҐґ]{0,15}\b"
)

# --- negation cue lists -------------------------------------------------
NEGATION_CUES = {
    "ru_RU": [r"не", r"нет", r"ни"],
    "uk_UA": [r"не", r"ні", r"жодн\w*"],
}

# English negation cues, used only to decide whether an ALIGNED source
# sentence plausibly carries a negation the hypothesis sentence is missing
# (see detect_negation_polarity: the injected-data negation corruption is a
# DELETION of the target-language marker, so localizing it requires noticing
# an ABSENCE relative to source, not just matching a present cue word).
_EN_NEGATION_RE = re.compile(
    r"\bnot\b|n't\b|\bnever\b|\bno\b|\bnothing\b|\bnobody\b|\bnone\b|\bneither\b|\bnor\b|\bwithout\b",
    re.IGNORECASE,
)

# --- quantifier closed-class word lists ---------------------------------
QUANTIFIER_WORDS = {
    "ru_RU": [
        "все", "всех", "всем", "всеми", "весь", "вся", "всё",
        "каждый", "каждая", "каждое", "каждые", "каждого", "каждой",
        "некоторые", "некоторых", "многие", "многих", "мало",
        "несколько", "нескольких", "любой", "любая", "любое",
        "никто", "ничто", "никакой",
    ],
    "uk_UA": [
        "всі", "весь", "вся", "все", "усі", "увесь",
        "кожен", "кожна", "кожне", "кожні", "кожного", "кожної",
        "деякі", "деяких", "багато", "багатьох", "мало",
        "декілька", "кількох", "будь-який", "будь-яка", "будь-яке",
        "ніхто", "ніщо", "жоден",
    ],
}


@dataclass
class Span:
    start: int
    end: int
    text: str
    category: str


def _regex_spans(pattern: re.Pattern, text: str, category: str) -> list[Span]:
    return [Span(m.start(), m.end(), m.group(0), category) for m in pattern.finditer(text)]


def detect_number_unit_date(hyp_text: str) -> list[Span]:
    return _regex_spans(_NUMBER_RE, hyp_text, "number_unit_date")


_SENTENCE_SPLIT_RE = re.compile(r"[^.!?\n]*[.!?\n]|[^.!?\n]+$")


def _sentence_spans(text: str) -> list[tuple[int, int]]:
    """Char (start, end) offsets for each sentence-like chunk of text (split
    on .!?/newline, terminator kept with the preceding chunk)."""
    spans = []
    for m in _SENTENCE_SPLIT_RE.finditer(text):
        if m.group(0).strip():
            spans.append((m.start(), m.end()))
    return spans or [(0, len(text))]


def detect_negation_polarity(source_text: str, hyp_text: str, lang: str) -> list[Span]:
    """Per-language cue-word match, word-boundary, applied per SENTENCE (not
    the whole multi-sentence hypothesis document): a sentence fires when it
    contains EXACTLY ONE negation marker (Slavic/Czech negative-concord
    languages allow multiple co-occurring negation markers within a sentence,
    so removing just one does not reliably flip polarity unless it is the
    only one in that sentence -- the dossier's documented caveat, scoped here
    to the sentence it actually applies to rather than the whole document).

    A second signal handles the DELETION case (the injected negation-flip
    corruption removes the target-language marker entirely, leaving nothing
    to text-match at that position): a hyp sentence with ZERO negation cues
    whose position-aligned source sentence (coarse index-proportional
    alignment -- documents are similar length, exact sentence alignment is
    not available) DOES contain an English negation cue is flagged as a
    suspected negation-deletion site (the whole hyp sentence is the span,
    since there is no token to point to)."""
    cues = NEGATION_CUES[lang]
    combined = re.compile(r"\b(?:" + "|".join(cues) + r")\b", re.IGNORECASE)
    hyp_sents = _sentence_spans(hyp_text)
    src_sents = _sentence_spans(source_text) if source_text else []
    out: list[Span] = []
    for idx, (sent_start, sent_end) in enumerate(hyp_sents):
        sentence = hyp_text[sent_start:sent_end]
        matches = list(combined.finditer(sentence))
        if len(matches) == 1:
            m = matches[0]
            out.append(Span(sent_start + m.start(), sent_start + m.end(), m.group(0), "negation_polarity"))
        elif len(matches) == 0 and src_sents:
            src_idx = min(int(idx * len(src_sents) / max(1, len(hyp_sents))), len(src_sents) - 1)
            src_st, src_en = src_sents[src_idx]
            if _EN_NEGATION_RE.search(source_text[src_st:src_en]):
                out.append(Span(sent_start, sent_end, sentence, "negation_polarity"))
    return out


def detect_quantifier_scope(hyp_text: str, lang: str) -> list[Span]:
    words = sorted(QUANTIFIER_WORDS[lang], key=len, reverse=True)
    combined = re.compile(r"\b(?:" + "|".join(re.escape(w) for w in words) + r")\b", re.IGNORECASE)
    return _regex_spans(combined, hyp_text, "quantifier_scope")


class NamedEntityDetector:
    """Wraps a per-language Stanza NER pipeline. Lazily initialized (Stanza
    pipeline construction loads model weights, so this is done once per
    language and reused for every row)."""

    def __init__(self):
        self._pipelines: dict[str, object] = {}

    def _get_pipeline(self, lang: str):
        if lang not in self._pipelines:
            import stanza

            stanza_lang = {"ru_RU": "ru", "uk_UA": "uk"}[lang]
            self._pipelines[lang] = stanza.Pipeline(
                lang=stanza_lang,
                processors="tokenize,ner",
                use_gpu=False,
                verbose=False,
                download_method=None,
            )
        return self._pipelines[lang]

    def detect(self, hyp_text: str, lang: str) -> list[Span]:
        nlp = self._get_pipeline(lang)
        doc = nlp(hyp_text)
        spans = []
        for ent in doc.ents:
            spans.append(Span(ent.start_char, ent.end_char, ent.text, "named_entity"))
        return spans


class Checker:
    """Runs the four category detectors, respecting an exclusion list of
    (lang, category) cells that failed Phase-1 validation."""

    def __init__(self, excluded_cells: set[tuple[str, str]] | None = None):
        self.excluded_cells = excluded_cells or set()
        self._ner = NamedEntityDetector()

    def detect_category(self, category: str, source_text: str, hyp_text: str, lang: str) -> list[Span]:
        if category == "named_entity":
            return self._ner.detect(hyp_text, lang)
        if category == "number_unit_date":
            return detect_number_unit_date(hyp_text)
        if category == "negation_polarity":
            return detect_negation_polarity(source_text, hyp_text, lang)
        if category == "quantifier_scope":
            return detect_quantifier_scope(hyp_text, lang)
        raise ValueError(f"Unknown category: {category}")

    def detect_all(self, source_text: str, hyp_text: str, lang: str, *, respect_exclusions: bool) -> list[Span]:
        spans: list[Span] = []
        for cat in CATEGORIES:
            if respect_exclusions and (lang, cat) in self.excluded_cells:
                continue
            spans.extend(self.detect_category(cat, source_text, hyp_text, lang))
        return spans

    def is_flagged(self, category: str, source_text: str, hyp_text: str, lang: str, start: int, end: int) -> bool:
        """True if any span from this category's detector overlaps [start, end)."""
        for s in self.detect_category(category, source_text, hyp_text, lang):
            if s.start < end and start < s.end:
                return True
        return False
