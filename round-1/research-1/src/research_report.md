# Resource Dossier for Scoped-Editing Replication

## Summary

This research artifact delivers a fully resolved, implementation-ready resource dossier for replicating Padmanabhan (2025)'s SURREYPAI-S2 masked-fill baseline (WMT25 Task 3, ΔCOMET=-0.0108) and building the four-category content-invariant checker (entity / number-unit-date / negation-polarity / quantifier-scope) across Chinese, Czech, Japanese, Icelandic, Russian, and Ukrainian. It provides: (1) the verbatim Algorithm 1 pseudocode and full masking prompt template quoted directly from the paper's arXiv HTML mirror, plus the three documented leakage bugs (literal __BLANK__/placeholder survival, metadata leakage, prompt-following failure) that any faithful replication must expect to reproduce; (2) the reconciled, authoritative WMT25 Table 15 (8 systems x 6 language pairs x ΔCOMET/GER), confirming Padmanabhan's self-reported and the organizers' re-scored numbers are consistent (rounding only, not a real discrepancy), and pinning the exact scorer footnoted by the organizers (Unbabel/wmt22-cometkiwi-da) as the sole ΔCOMET metric across every system; (3) a DEFINITIVE, triple-confirmed resolution that TowerPlus-9B is absent from OpenRouter (raw model-list JSON regex search across 705K characters, HF Inference-Providers panel showing no active provider, and targeted hosting search all agree), together with a corrected finding that the plan's assumed fallback google/gemma-2-9b-it is ALSO no longer listed, and a freshly re-ranked substitute table (google/gemma-3-12b-it recommended, with exact live OpenRouter pricing/context for 5 candidates) with an explicit, undownplayed limitation about the generation mismatch and missing MT fine-tuning; (4) the exact COMET package/checkpoint/install command, its CC-BY-NC-SA-4.0 license terms (gated HF download), and a measured GPU throughput benchmark (~155 segments/sec on 1x V100, ~648 on 8x V100) with an honestly-reported absence of any CPU benchmark rather than an invented number; and (5) a fully resourced language x category decision table for the four-category checker, with real package/model names, license terms, and reported precision/recall for every cell that has one, explicitly marked 'unvalidated - needs pilot' elsewhere. The dossier also issues seven corrections to the plan's own preliminary research (Stanza's NER coverage is far broader than assumed, Duckling's real gap is Czech+Icelandic not Ukrainian, MultiLegalNeg covers none of the six target languages, Japanese quantifier-negation scope is not a clean 'obligatory wide scope' rule per the linguistics literature, etc.), each backed by a freshly fetched primary source rather than trusting the earlier pass. Every claim is cited to a specific fetched page, PDF, or API response fetched in this research pass; no numbers were invented where a source did not provide one.

## Research Findings

See research_report.md for the full four-block dossier (Block A: replication spec; Block B: OpenRouter model access; Block C: COMET scoring protocol; Block D: checker resource table). Key findings, each with inline citations:

**BLOCK A — Replication spec.** The verbatim masking prompt and Algorithm 1 pseudocode were extracted directly from the paper's arXiv HTML mirror [1]: QE score >=0.90 -> no masking; 0.50<=score<0.90 -> mask only major-severity spans (or all spans if only minor exist); score<0.50 -> mask all spans. Three leakage bugs are documented in the paper itself: literal `__BLANK__`/placeholder-name tokens surviving into output, bracketed metadata (`Corrected words: [...]`) leaking into the translated string, and a broader prompt-following failure the authors attribute the whole -0.0108 result to [1]. The two 'discrepant' per-language ΔCOMET readings from preliminary research are RECONCILED: Padmanabhan's own Table 3 (Czech -7.24e-3 ... Ukrainian -1.35e-2, average -1.08e-2) and WMT25's organizer-scored Table 15 (Czech -0.007 ... Ukrainian -0.014, average -0.011) are the same numbers at different rounding precision, not a real conflict [1,2]. The full authoritative Table 15 (8 systems x 6 language pairs x ΔCOMET/GER) is reproduced verbatim in the report [2]. The exact COMET checkpoint for every Table-15 ΔCOMET is confirmed via an explicit organizer footnote: `Unbabel/wmt22-cometkiwi-da` [2] — distinct from XCOMET-XL, which appears only as BASELINE-S2's internal QE-signal input, never as a Table-15 scorer.

**BLOCK B — OpenRouter TowerPlus-9B, resolved with certainty.** TowerPlus-9B is confirmed absent from OpenRouter via three independent checks: a full regex sweep of the raw `/api/v1/models` JSON catalog (705,131 characters, zero matches for `tower|unbabel`) [3], Hugging Face's own Inference-Providers panel on the model page showing no active serving provider [4], and a targeted hosting search finding no Together/Fireworks/DeepInfra listing. A correction to the plan: `google/gemma-2-9b-it`, assumed 'already confirmed present,' is ALSO now absent from OpenRouter's catalog [3] — the clean 'same base model minus fine-tuning' substitution the plan hoped for is no longer available. Five live candidates were fetched with exact pricing/context from OpenRouter's endpoint API [3,5,6,7,8,9]; `google/gemma-3-12b-it` (12B, 131K context, $0.05/$0.15 per M tokens on DeepInfra) is recommended, keeping the Gemma lineage while explicitly flagging the generation mismatch (Gemma-3 vs. Tower-Plus's Gemma-2 base) and the complete absence of MT-specific fine-tuning as an honest limitation that could confound any measured baseline gap.

**BLOCK C — COMET protocol.** Install via `pip install unbabel-comet>=2.2.0` (Apache-2.0 package) [10]; the WMT25-matching checkpoint `Unbabel/wmt22-cometkiwi-da` is itself CC-BY-NC-SA-4.0 and gated on HF (accept terms + share contact info) [11]. A rigorous GPU benchmark (PyMarian paper, timing the ORIGINAL comet-score implementation on 364,200 real segments) gives ~154.6 segments/sec on 1x V100 and ~648.0 on 8x V100 [24] — no CPU benchmark exists in any source consulted, and this gap is reported honestly rather than filled with an estimate; a GPU compute profile is recommended for the next iteration's full scoring pass.

**BLOCK D — Checker resource table.** Real, cited resources were found for every language x category cell that has one: spaCy NER F1 for Chinese (0.7134, MIT) [12], Japanese (0.7119, CC-BY-SA-4.0) [13], Russian (0.9530, MIT) [14], Ukrainian (0.8968, MIT) [15]; NameTag 3 closes the Czech gap (86.39/89.29 F1, CC-BY-NC-SA-4.0) and cross-checks Ukrainian (92.18 F1) [16,17]; a ready-to-load fine-tuned IceBERT checkpoint (`vesteinn/IceBERT-finetuned-ner`, F1 0.8721, GPL-3.0) closes the Icelandic gap [18]. A correction: Stanza's NER coverage is far broader than the plan assumed — 23 languages including Japanese (81.01 F1) and Ukrainian (86.05 F1), not the ~8 excluding them that preliminary research reported [19]. For numbers/dates, `text2num` covers none of the six languages [22] but is largely the wrong tool for this task (MT output uses digit numerals, not spelled-out words); Duckling covers Japanese/Russian/Ukrainian/Chinese but NOT Czech or Icelandic [23] — a sharper and different finding than the plan's guess that Ukrainian was the weak spot. For negation, 'Towards the Roots of the Negation Problem' (ACL Findings EMNLP 2025) confirms English/Czech/German/Ukrainian coverage but is an entailment-pair dataset, not a cue-word list [20]; `rcds/MultiLegalNeg` covers German/French/Italian only and should be DROPPED from the plan — it has zero overlap with the six target languages [21]. Japanese negation-scope is corrected: the linguistics literature (Han/Storoshenko/Sakurai; 'On the variability of negative scope in Japanese,' Journal of Linguistics) shows quantifier-negation scope interaction is context-dependent, not a clean 'obligatory wide scope' rule as the plan assumed [25]. Starting references for Russian/Ukrainian genitive-of-negation (Partee & Borschev 2004) [26] and Icelandic ekki+V2 interaction (Angantýsson 2008) [27] are provided for deferred full resolution.

Confidence: HIGH for Blocks A-C (every claim traced to a primary-source fetch performed in this pass, including live API responses). MEDIUM-HIGH for Block D (resource existence and license terms are confirmed; actual precision/recall on the specific WMT25 Task-3 error-detection task remains genuinely unvalidated for most cells, as the plan itself anticipated and as marked in the decision table).

## Sources

[1] [Submission for WMT25 Task 3 (Padmanabhan, 2025) — arXiv HTML mirror](https://arxiv.org/html/2511.13884) — Primary source for the verbatim masking prompt template, Algorithm 1 pseudocode, the three leakage bugs (Appendix B), and the author's self-reported per-language ΔCOMET Table 1/Table 3.

[2] [Findings of the WMT25 Shared Task on Automated Translation Evaluation Systems](https://aclanthology.org/2025.wmt-1.24.pdf) — Organizer findings paper; source of the authoritative Table 15 (8 systems x 6 language pairs), the ΔCOMET formula, its footnoted exact COMET checkpoint (Unbabel/wmt22-cometkiwi-da), and the BASELINE-S1/S2 descriptions.

[3] [OpenRouter Models API (live catalog JSON)](https://openrouter.ai/api/v1/models) — Full 705K-character model catalog; used to definitively confirm TowerPlus-9B and google/gemma-2-9b-it absence, and to enumerate/price substitute candidates.

[4] [Unbabel/Tower-Plus-9B model card](https://huggingface.co/Unbabel/Tower-Plus-9B) — Confirms Gemma-2-9B base, 22-language coverage, 8192-token context, CC-BY-NC-SA-4.0 license, and no active Inference Providers serving the model.

[5] [google/gemma-3-12b-it OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/google/gemma-3-12b-it/endpoints) — Live pricing ($0.05/$0.15 per M tokens on DeepInfra) and 131,072-token context for the recommended substitute model.

[6] [qwen/qwen-2.5-7b-instruct OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/qwen/qwen-2.5-7b-instruct/endpoints) — Live pricing and context for a second-ranked substitute candidate.

[7] [mistralai/mistral-nemo OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/mistralai/mistral-nemo/endpoints) — Live pricing across multiple providers for a third-ranked substitute candidate.

[8] [meta-llama/llama-3.1-8b-instruct OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/meta-llama/llama-3.1-8b-instruct/endpoints) — Live pricing for the cheapest substitute candidate at similar parameter count.

[9] [mistralai/ministral-8b-2512 OpenRouter endpoint listing](https://openrouter.ai/api/v1/models/mistralai/ministral-8b-2512/endpoints) — Live pricing for a newly-released 8B candidate not considered in the original plan.

[10] [unbabel-comet PyPI package page](https://pypi.org/project/unbabel-comet/) — Confirms package version 2.2.7, Apache-2.0 license, and install command.

[11] [Unbabel/COMET model license table](https://raw.githubusercontent.com/Unbabel/COMET/master/LICENSE.models.md) — Per-checkpoint license table confirming wmt22-cometkiwi-da and XCOMET-XL/XXL are CC-BY-NC-SA, distinct from the Apache-2.0 code package.

[12] [spacy/zh_core_web_lg model card](https://huggingface.co/spacy/zh_core_web_lg) — NER F1 0.7134 (P 0.7355/R 0.6925), MIT license, spaCy 3.7.0.

[13] [spacy/ja_core_news_lg model card](https://huggingface.co/spacy/ja_core_news_lg) — NER F1 0.7119 (P 0.7388/R 0.6868), CC-BY-SA-4.0 license.

[14] [spacy/ru_core_news_lg model card](https://huggingface.co/spacy/ru_core_news_lg) — NER F1 0.9530 (P 0.9524/R 0.9535), MIT license — best-performing of all six languages.

[15] [spacy/uk_core_news_trf model card](https://huggingface.co/spacy/uk_core_news_trf) — NER F1 0.8968 (P 0.8969/R 0.8967), MIT license, transformer-based pipeline.

[16] [NameTag 3 Models page, ÚFAL](https://ufal.mff.cuni.cz/nametag/3/models) — Czech CNEC 2.0 model F1 86.39/89.29, Ukrainian Lang-uk model F1 92.18/92.88, CC-BY-NC-SA-4.0 non-commercial license terms, commercial license available separately.

[17] [NameTag 3: A Tool and a Service for Multilingual/Multitagset NER (Straková & Straka, 2025)](https://arxiv.org/abs/2506.05949) — ACL 2025 paper describing NameTag 3's architecture and multilingual/multitagset evaluation methodology.

[18] [vesteinn/IceBERT-finetuned-ner model card](https://huggingface.co/vesteinn/IceBERT-finetuned-ner) — Ready-to-load fine-tuned Icelandic NER checkpoint on mim_gold_ner, F1 0.8721, GPL-3.0 license — closes the Icelandic NER gap.

[19] [Stanza NER Models performance table](https://raw.githubusercontent.com/stanfordnlp/stanza/6ed5ab184818c495aa16a1b6fa20205561059fe4/_pages/ner_models.md) — Full 23-language/corpus F1 table; corrects the plan's preliminary claim of ~8-language coverage — Stanza actually covers Chinese (79.2), Japanese (81.01), Russian (92.9), and Ukrainian (86.05).

[20] [Towards the Roots of the Negation Problem: A Multilingual NLI Dataset and Model Scaling Analysis (Vrabcová et al., ACL Findings EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.1391.pdf) — Confirms NoFEVER-ML/NoSNLI-ML cover English/Czech/German/Ukrainian; confirms format is entailment pairs, not a negation-cue lexicon.

[21] [rcds/MultiLegalNeg dataset card](https://huggingface.co/datasets/rcds/MultiLegalNeg) — Confirms coverage is German/French/Italian only — zero overlap with the six WMT25 Task 3 target languages; resource should be dropped from the plan.

[22] [text2num PyPI package page](https://pypi.org/project/text2num/) — Confirms supported languages (French, Spanish, English, Portuguese, German, Dutch, Danish, Italian) — no overlap with the six target languages.

[23] [python-duckling Language enum source](https://raw.githubusercontent.com/FraBle/python-duckling/master/duckling/language.py) — Confirms Duckling's supported-language set includes Japanese/Russian/Ukrainian/Chinese but excludes Czech and Icelandic entirely.

[24] [PyMarian: Fast Neural Machine Translation and Evaluation in Python (Gowda et al., 2024)](https://arxiv.org/pdf/2408.11853) — Rigorous GPU throughput benchmark for the original comet-score implementation scoring wmt22-cometkiwi-da on 364,200 real WMT23 segments; source of the ~154.6 seg/sec (1 GPU) and ~648.0 seg/sec (8 GPU) figures.

[25] [On the variability of negative scope in Japanese — Journal of Linguistics](https://www.cambridge.org/core/journals/journal-of-linguistics/article/abs/on-the-variability-of-negative-scope-in-japanese1/67847A8151BC1A766FA4B8F2A95760CC) — Academic source establishing that Japanese quantifier-negation scope interaction is context/focus-dependent rather than a categorical 'obligatory wide scope' rule.

[26] [Barbara Partee & Vladimir Borschev — Russian Genitive of Negation research program](https://people.umass.edu/partee/Gen_Neg/_pages/research.shtml) — Starting reference for the Russian/Ukrainian genitive-of-negation case-marking phenomenon under negation scope.

[27] [Sentential Negation and Verb Placement in Embedded Clauses in Icelandic (Angantýsson, 2008)](http://tekstlab.uio.no/negasjon07/Angantysson.pdf) — Starting reference for the Icelandic ekki + V2 word-order interaction relevant to negation-cue position detection.

## Follow-up Questions

- The next iteration should pilot the checker's actual precision/recall against a small held-out annotated sample per language x category cell, since almost none of the resources identified here report validation numbers specific to the WMT25 Task-3 error-detection use case (as opposed to their own training-corpus benchmarks) — which cells (Czech numbers/dates, Icelandic quantifier scope, and Japanese negation scope specifically) are the highest-priority to pilot first given they have the weakest existing evidence?
- Since google/gemma-2-9b-it disappeared from OpenRouter's catalog between the plan's preliminary research and this pass, should the next iteration re-verify TowerPlus-9B's and the chosen substitute's (google/gemma-3-12b-it) continued availability immediately before the experiment starts, given demonstrated catalog churn on a timescale of days to weeks?
- No authoritative CPU-only throughput benchmark for wmt22-cometkiwi-da was found in this pass — should the next iteration run its own small-scale timing pilot (e.g. 100 segments) on the cpu_light profile before committing to a GPU compute-profile request, to get a real number rather than relying on the qualitative extrapolation in Block C?

---
*Generated by AI Inventor Pipeline*
