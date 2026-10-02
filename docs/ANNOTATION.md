# Annotation and evaluation plan

Version 0.2.0 expands the initial 5-object image acquisition pilot across museum
sources. See data/manifest.json for the actual counts and period/date fields.
Museum period metadata does not establish every inscription's language stage.

Transcription, transliteration and translation fields remain null. Empty
sign_annotations means no signs have yet been labeled, not that the image has none.

Next: review inscription-bearing views, locate exact scholarly readings and reuse
terms, annotate sign regions/identities/grouping/reading order, record damage and
disagreements, and attach cited translations with independent rights records.

The selected objects are candidates, not verified sign-recognition examples.
Some are three-dimensional or have writing on faces absent from the primary image.
The Art Institute images use its recommended cached 843-pixel width. They are
reference previews; very small hieroglyphs may need larger images or independent
close-up photographs before sign-level annotation.

## Evaluation separation
For known-object image retrieval, reference and query necessarily depict the same
object; use independently captured queries and report retrieval performance.
For unseen-inscription reading/OCR, all photographs, crops and augmentations of an
object share its split_group and stay in one training/evaluation partition.
No independent camera-test photographs or measured recognition accuracy exist yet.
Synthetic blur/perspective images are labeled derivatives, not museum originals or
independent field photographs. See PHOTO-FIELD-GUIDE.md for future capture details.
