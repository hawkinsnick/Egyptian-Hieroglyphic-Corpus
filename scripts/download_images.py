"""Download only pinned CC0 source images, rejecting changed records. CC-BY-NC-4.0."""
import hashlib,json,urllib.request
from validate import ROOT,validate,matches_acquired_bytes

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Egyptian-Hieroglyphic-Corpus/0.1.0 (open-access pilot)'})
    with urllib.request.urlopen(req,timeout=120) as response:
        return response.read()

def main():
    manifest=validate()
    for record in manifest['objects']:
        # Recheck the museum's current status rather than trusting cached metadata.
        raw=json.loads(fetch(record['metadata_api']))
        if raw.get('isPublicDomain') is not True: raise ValueError('Current object is not public domain: '+record['object_id'])
        if str(raw['objectID']) != record['object_id'].split(':')[1]: raise ValueError('Current object mismatch')
        allowed=[raw.get('primaryImage')]+raw.get('additionalImages',[])
        for image in record['images']:
            if image['source_url'] not in allowed: raise ValueError('Source image URL has changed; review required')
            path=ROOT/image['path'];path.parent.mkdir(parents=True,exist_ok=True)
            data=path.read_bytes() if path.exists() else fetch(image['source_url'])
            if not matches_acquired_bytes(data,image):
                raise ValueError('Source bytes changed; review required: '+image['path'])
            if not path.exists():
                temporary=path.with_suffix('.partial');temporary.write_bytes(data);temporary.replace(path)
            print('Verified '+image['path'])
    receipts = [{'path': image['path'], 'sha256': hashlib.sha256((ROOT/image['path']).read_bytes()).hexdigest(), 'bytes': (ROOT/image['path']).stat().st_size} for record in manifest['objects'] for image in record['images']]
    (ROOT/'images/download-receipts.json').write_text(json.dumps(receipts, indent=2)+'\n')
    validate(images=True)
if __name__=='__main__': main()
