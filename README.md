# Egyptian Hieroglyphic Corpus

Version **0.1.0** — an open-image acquisition pilot supporting research and a future
camera-assisted reading app. This independent project is not affiliated with or
endorsed by The Metropolitan Museum of Art.

## What is available
- **5 Egyptian stelae; 11 original high-resolution museum photographs.**
- Museum API records and normalized source records.
- Accession numbers, credit lines, original image URLs, retrieval timestamps,
  image dimensions and SHA-256 hashes.
- Download/validation tools and a browsable source gallery.

**No verified sign annotations, transcriptions, transliterations or translations
are included yet.** This is not a trained recognizer or translation app.

## Browse and download
Open [the source gallery](gallery.html) locally after downloading the repository;
it displays images from the recorded Met URLs and links to each museum record.
The [manifest](data/manifest.json) lists every acquired image.

A GitHub Actions publication job downloads and verifies the 11 originals, then
publishes a versioned ZIP on the [Releases page](../../releases). Check the job's
status if a release is not yet present; a failed job does not mean a release exists.

To reproduce locally with Python 3.10+ (standard library only):

```sh
python scripts/validate.py
python scripts/download_images.py
python scripts/validate.py --images
python scripts/package.py
```

The resulting ZIP contains images and source records. Re-downloaded files must
match the acquired checksums. Changed source files require a reviewed manifest
update; the script does not silently accept replacements.

## Permissions and attribution
**Met images and API data remain CC0.** Original project work is CC BY-NC 4.0;
that restriction does not apply to the museum assets. See [LICENSE](LICENSE),
[permissions evidence](docs/PERMISSIONS.md), and [object credits](CREDITS.md).
No modern museum essays or scholarly translations are reproduced.

## Research roadmap
1. Review image suitability and select legible passages.
2. Link exact scholarly readings with independent rights checks.
3. Annotate signs, layout, reading order, damage and uncertainty.
4. Benchmark known-object photo matching on independent photographs.
5. Develop sign recognition and translation as separately evaluated capabilities.

The corpus remains independent of the camera application. See
[annotation and evaluation notes](docs/ANNOTATION.md).
