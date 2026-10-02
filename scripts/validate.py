"""Validate provenance and optional local image bytes. CC-BY-NC-4.0."""
import argparse, hashlib, json
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1]
def validate(images=False):
    manifest = json.loads((ROOT/'data/manifest.json').read_text())
    objects = manifest['objects']; seen = set(); count = 0
    if not objects: raise ValueError('No objects')
    for record in objects:
        oid = record['object_id']; number = oid.split(':')[1]
        if oid in seen: raise ValueError('Duplicate object')
        seen.add(oid)
        raw = json.loads((ROOT/'data/met'/number/'museum-record.json').read_text())
        normalized = json.loads((ROOT/'data/met'/number/'record.json').read_text())
        if normalized != record: raise ValueError('Manifest/record disagreement')
        if raw['isPublicDomain'] is not True: raise ValueError('Missing public-domain evidence')
        if record['image_rights']['license'] != 'CC0-1.0': raise ValueError('Wrong source license')
        if str(raw['objectID']) != number or raw['accessionNumber'] != record['accession_number']: raise ValueError('Wrong object mapping')
        if raw['creditLine'] != record['credit_line']: raise ValueError('Missing credit line')
        if record['split_group'] != oid: raise ValueError('Invalid object grouping')
        for field in ('transcription','transliteration','translation'):
            if record[field] is not None: raise ValueError('Pilot must not claim unchecked readings')
        urls = [raw['primaryImage']] + raw['additionalImages']
        if not record['images']: raise ValueError('No images')
        for image in record['images']:
            url = urlparse(image['source_url'])
            if url.scheme != 'https' or url.hostname != 'images.metmuseum.org' or image['source_url'] not in urls: raise ValueError('Nonapproved image URL')
            path = Path(image['path'])
            if path.is_absolute() or '..' in path.parts or path.parts[:3] != ('images','met',number): raise ValueError('Unsafe image path')
            if len(image['sha256']) != 64 or any(c not in '0123456789abcdef' for c in image['sha256']): raise ValueError('Invalid checksum')
            if min(image['width'],image['height'],image['bytes']) <= 0: raise ValueError('Invalid dimensions')
            if images:
                data = (ROOT/path).read_bytes()
                if len(data) != image['bytes'] or hashlib.sha256(data).hexdigest() != image['sha256']: raise ValueError('Image mismatch: '+str(path))
            count += 1
    print(f'Validated {len(objects)} objects, {count} image records'+(' and local image bytes' if images else ''))
    return manifest
if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--images',action='store_true')
    validate(parser.parse_args().images)
