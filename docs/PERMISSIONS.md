# Permissions register — checked 2026-10-02

## Scope of approval evidence
- Policy: https://www.metmuseum.org/hubs/open-access
- Detailed policy: https://www.metmuseum.org/policies/image-resources
- FAQ: https://www.metmuseum.org/policies/frequently-asked-questions-image-and-data-resources
- API: https://metmuseum.github.io/

The Met makes designated Open Access images and select API data available under
CC0. Its FAQ permits sharing and commercial/noncommercial use without additional
permission, encourages citations, and prohibits implying Museum endorsement.
This is reliance on the published Open Access policy, not private permission or
an agreement with the Museum. Policy pages are cited, not copied in full.

## Per-object evidence
Every included raw API record has isPublicDomain=true. The normalized records
retain source object URLs, accession numbers, collection credit lines, original
image URLs, retrieval timestamps, dimensions and SHA-256 hashes. Only URLs in each
record's primaryImage/additionalImages were collected. No exhibition graphics,
logos, audio transcripts, essays or modern translations were scraped.

## Publication rules
- Keep Met assets CC0; do not attach the project's noncommercial license to them.
- Attribute each image to The Metropolitan Museum of Art, New York, and retain
  the collection credit line and accession number (see CREDITS.md).
- Label any later crop, enhancement or synthetic derivative as such; preserve originals.
- Inspect each new source separately. A downloadable image is not necessarily OA.
- Recheck current API status before fresh downloads; reject changed URLs or checksums.
- Any scholarly reading or translation needs its own provenance, reuse basis and
  verification status before ingestion. An image's CC0 status does not cover essays
  or modern translations associated with that image.
- Do not imply collaboration, approval, or endorsement by the Museum.

All 11 acquired files are original museum images. Their usefulness for sign-level
recognition still needs image-by-image review.

## Reviewed JPEG byte variant
During publication, several source JPEGs returned changed container/metadata
bytes. Each accepted variant was compared with its acquired original and decoded
to exactly the same RGB pixels and dimensions. Explicit reviewed checksum/size
alternatives are retained in the records;
no changed pixels were accepted. Any other checksum still stops publication.
Download receipts record the actual bytes packaged in a release.
