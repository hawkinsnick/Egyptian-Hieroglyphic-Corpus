"""Download only pinned CC0 source images; museum-specific checks. CC-BY-NC-4.0."""
import hashlib,json,time,urllib.request
from validate import ROOT,validate,matches_acquired_bytes,approved_urls

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Egyptian-Hieroglyphic-Corpus/0.2.0','AIC-User-Agent':'Egyptian-Hieroglyphic-Corpus (github.com/hawkinsnick/Egyptian-Hieroglyphic-Corpus)'})
    with urllib.request.urlopen(req,timeout=120) as response:return response.read()
def main():
    manifest=validate()
    for record in manifest['objects']:
        source,number=record['object_id'].split(':')
        endpoint=record['metadata_api']
        expected='https://collectionapi.metmuseum.org/public/collection/v1/objects/'+number if source=='met' else 'https://api.artic.edu/api/v1/artworks/'+number+'?fields='
        if (source=='met' and endpoint!=expected) or (source=='artic' and not endpoint.startswith(expected)): raise ValueError('Unexpected metadata endpoint')
        current=json.loads(fetch(endpoint));allowed=approved_urls(current,source)
        current_id=current['objectID'] if source=='met' else current['data']['id']
        if str(current_id)!=number:raise ValueError('Current object mismatch')
        if source=='artic':time.sleep(1)
        for im in record['images']:
            if im['source_url'] not in allowed:raise ValueError('Source URL changed; review required')
            path=ROOT/im['path'];path.parent.mkdir(parents=True,exist_ok=True)
            data=path.read_bytes() if path.exists() else fetch(im['source_url'])
            if not matches_acquired_bytes(data,im):raise ValueError('Source bytes changed; review required: '+im['path'])
            if not path.exists():
                tmp=path.with_suffix('.partial');tmp.write_bytes(data);tmp.replace(path)
            print('Verified '+im['path'],flush=True)
            if source=='artic':time.sleep(1)
    receipts=[{'path':im['path'],'sha256':hashlib.sha256((ROOT/im['path']).read_bytes()).hexdigest(),'bytes':(ROOT/im['path']).stat().st_size} for r in manifest['objects'] for im in r['images']]
    (ROOT/'images/download-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n');validate(images=True)
if __name__=='__main__':main()
