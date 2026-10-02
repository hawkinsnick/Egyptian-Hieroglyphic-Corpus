# Egyptian Hieroglyphic Corpus

Version **0.2.0** — an open-image acquisition collection supporting research and a
future camera-assisted reading app. Independent project; no museum affiliation
or endorsement.

## Available now
- **25 objects and 32 museum-supplied image files**, up from 5 objects/11 images.
- 10 Met objects with 17 images; 15 Art Institute objects with 15 images.
- Source records, accession numbers, credit lines, source URLs, retrieval times,
  dimensions and SHA-256 hashes; reviewed identical-pixel JPEG variants where needed.
- Museum-specific permission checks, download receipts, and a source gallery.
- [Art Institute photo checklist](docs/PHOTO-FIELD-GUIDE.md), a
  [five-object target list](docs/ART-INSTITUTE-TARGETS.md), and a capture manifest template.

**No verified sign annotations, transcriptions, transliterations or translations
are included yet.** Object matching and sign-level recognition are future work.
Candidate objects have visible writing or sign examples, but each passage still
needs detailed suitability review. The collection is not exhaustive.

## Download and browse
Download the image ZIP from [v0.2.0 Releases](https://github.com/hawkinsnick/Egyptian-Hieroglyphic-Corpus/releases/tag/v0.2.0),
unzip, then open `gallery.html`. The release ZIP contains local images. A source-only
repository download uses museum URLs as a fallback and requires internet access.
If the release is absent, check the publication job; it only publishes after checks pass.

Art Institute images are its recommended 843px cached-width references. Met files
are the acquired original-resolution images. Do not assume all files are suitable
for reading very small signs. Larger public-domain images can be considered later
where the detail is necessary and the institution's guidance allows it.

To reproduce locally with Python 3.10+ (standard library only):

```sh
python scripts/validate.py
python scripts/download_images.py
python scripts/validate.py --images
python scripts/package.py
```

The downloader rechecks current museum public-domain status and source identity.
It rejects unreviewed byte changes. Art Institute requests run sequentially with
one-second delays; no parallel scraping. The release records actual image hashes.

## Permissions
Source images and basic metadata remain **CC0**, including commercial reuse.
Original project work is **CC BY-NC 4.0**; this does not restrict source CC0 assets.
See [LICENSE](LICENSE), [permissions register](docs/PERMISSIONS.md), and
[CREDITS.md](CREDITS.md). Art Institute `description` and `inscriptions` prose fields
were excluded from the selected-field import; no modern translations were copied.

Visitor photography is a separate permission question. Do not treat online CC0
image status as authorization to publish visitor photos or museum labels. The photo
guide explains how to confirm the intended public dataset use before a visit.

## Next research work
Review inscription regions, locate exact editions and their reuse terms, annotate
signs and reading order, and evaluate retrieval separately from unseen-text OCR.
See [evaluation notes](docs/ANNOTATION.md). The camera app remains a separate project.
