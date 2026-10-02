"""Validate museum-specific provenance and optional local image bytes. CC-BY-NC-4.0."""
import argparse, hashlib, json
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1]
def matches_acquired_bytes(data, image):
    candidates = [{'sha256': image['sha256'], 'bytes': image['bytes']}] + image.get('reviewed_byte_variants', [])
    digest = hashlib.sha256(data).hexdigest()
    return any(len(data) == c['bytes'] and digest == c['sha256'] for c in candidates)

def approved_urls(raw, source):
    if source == 'met':
        if raw.get('isPublicDomain') is not True: raise ValueError('Missing Met public-domain evidence')
        return [raw['primaryImage']] + raw['additionalImages']
    if source == 'artic':
        d = raw['data']
        if d.get('is_public_domain') is not True: raise ValueError('Missing Art Institute public-domain evidence')
        if 'description' in d or 'inscriptions' in d: raise ValueError('Prose fields excluded from this acquisition')
        base = raw['config']['iiif_url']
        if base != 'https://www.artic.edu/iiif/2': raise ValueError('Unexpected Art Institute image service')
        return [base + '/' + d['image_id'] + '/full/843,/0/default.jpg']
    raise ValueError('Unknown museum')

def validate(images=False):
    manifest = json.loads((ROOT/'data/manifest.json').read_text()); seen = set(); count = 0
    if not manifest['objects']: raise ValueError('No objects')
    for record in manifest['objects']:
        oid = record['object_id']; source, number = oid.split(':')
        if source not in ('met','artic') or not number.isdigit() or oid in seen: raise ValueError('Invalid/duplicate object')
        seen.add(oid);folder=ROOT/'data'/source/number
        raw=json.loads((folder/'museum-record.json').read_text())
        if json.loads((folder/'record.json').read_text())!=record: raise ValueError('Manifest/record disagreement')
        urls=approved_urls(raw,source)
        if record['image_rights']['license']!='CC0-1.0': raise ValueError('Wrong source license')
        d=raw if source=='met' else raw['data']
        api_id=d['objectID'] if source=='met' else d['id']
        acc=d['accessionNumber'] if source=='met' else d['main_reference_number']
        credit=d['creditLine'] if source=='met' else d['credit_line']
        if str(api_id)!=number or acc!=record['accession_number'] or credit!=record['credit_line']: raise ValueError('Wrong mapping or credit')
        if record['split_group']!=oid: raise ValueError('Invalid object grouping')
        for field in ('transcription','transliteration','translation'):
            if record[field] is not None: raise ValueError('Pilot must not claim unchecked readings')
        if not record['images']: raise ValueError('No images')
        for im in record['images']:
            url=urlparse(im['source_url']);host='images.metmuseum.org' if source=='met' else 'www.artic.edu'
            if url.scheme!='https' or url.hostname!=host or im['source_url'] not in urls: raise ValueError('Nonapproved image URL')
            path=Path(im['path'])
            if path.is_absolute() or '..' in path.parts or path.parts[:3]!=('images',source,number): raise ValueError('Unsafe image path')
            candidates=[im]+im.get('reviewed_byte_variants',[])
            for candidate in candidates:
                digest=candidate['sha256']
                if len(digest)!=64 or any(c not in '0123456789abcdef' for c in digest) or candidate['bytes']<=0: raise ValueError('Invalid checksum/size')
            if min(im['width'],im['height'])<=0: raise ValueError('Invalid dimensions')
            if images and not matches_acquired_bytes((ROOT/path).read_bytes(),im): raise ValueError('Image mismatch: '+str(path))
            count+=1
    print(f'Validated {len(seen)} objects, {count} image records'+(' and local image bytes' if images else ''))
    return manifest
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--images',action='store_true');validate(p.parse_args().images)
