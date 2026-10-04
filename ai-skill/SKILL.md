---
name: egyptian-hieroglyphic-corpus-research
description: Evidence-first AI research skill for the Egyptian Hieroglyphic Corpus and its open-image acquisition layer.
version: 0.3.1
---

# Egyptian Hieroglyphic Corpus Research Skill

The repository is the canonical source of truth. The current corpus is an open-image acquisition and provenance corpus, not yet a verified transcription or translation corpus.

## Governing rules
1. Separate physical object metadata, museum image evidence, sign observation, scholarly transcription, transliteration, translation, and AI inference.
2. Never infer a verified reading merely because signs are visually recognizable.
3. Preserve museum accession identifiers, image hashes, retrieval dates, source URLs, public-domain flags, and per-component rights.
4. Met/Art Institute CC0 assets remain CC0. Project NonCommercial terms never restrict upstream CC0/public-domain rights.
5. Art Institute descriptive prose is not part of the current selected-field import; do not silently import it as project text.
6. Future scholarly editions/readings retain their own rights and source dependence. Citation is not redistribution permission.
7. Do not treat Gardiner/Unicode/Thot/JSesh sign identifiers as automatically interchangeable; mappings require explicit evidence.
8. AI-generated sign recognition, segmentation, reading direction, transliteration, translation, dating, or attribution must be labeled as inference until source-checked.
9. Missing transcription/transliteration/translation means UNKNOWN, not an invitation to complete it.
10. Camera/OCR performance is a separate application-evaluation problem from corpus scholarly correctness.

## Current academic gates
- Verified sign annotations: BLOCKED/PENDING SOURCE-CHECKED ANNOTATION.
- Verified transcriptions/transliterations/translations: ABSENT in current 0.2.x acquisition corpus.
- Exhaustive object coverage: NOT CLAIMED.
- Museum image rights: record-specific; current admitted images require explicit public-domain evidence.
- Cross-signary equivalence: requires explicit concordance evidence.

## Default research response
Give the direct answer, then as relevant: Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Collection source work and review handoff

Read `research/collection-work-ledger.json` and `review/collection-packet.json` when preparing a source-work plan or expert request. Check their evidence fingerprint against current inputs with `python scripts/build_collection_handoff.py`. Select exact record keys and retain native units; overlapping views are not additional physical objects. Follow native review links for scientific decisions and admission. Ledger coverage does not establish completed collation, independent review or a terminal pre-expert ceiling. Use `review/collection-decision-template.json` for revision-bound submissions; structural validation cannot authenticate the reviewer or approve the science. Keep restricted local A/B derivatives local.
