"""Publish a new GitHub Release in Actions; never overwrite a release. CC-BY-NC-4.0."""
import hashlib,json,os,urllib.request,urllib.parse
from validate import ROOT,validate

def request(url,body,token,content_type='application/json',method='POST'):
    req=urllib.request.Request(url,data=body,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':content_type,'X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req,timeout=180) as response: return json.load(response)
if __name__=='__main__':
    manifest=validate(images=True);version=manifest['version'];repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN']
    archive=ROOT/'dist'/f'Egyptian-Hieroglyphic-Corpus-{version}.zip'
    data=archive.read_bytes()
    release=request(f'https://api.github.com/repos/{repo}/releases',json.dumps({'tag_name':'v'+version,'target_commitish':os.environ['GITHUB_SHA'],'name':'v'+version+' — open-image acquisition pilot','draft':True,'body':f'{len(manifest["objects"])} objects; {sum(len(r["images"]) for r in manifest["objects"])} museum Open Access images and source records. Museum assets remain CC0. Original project material is CC BY-NC 4.0. No verified readings or translations yet. Independent project; no Museum endorsement.\n\nZIP SHA-256: '+hashlib.sha256(data).hexdigest()}).encode(),token)
    url=release['upload_url'].split('{')[0]+'?name='+urllib.parse.quote(archive.name)
    asset=request(url,data,token,'application/zip')
    if asset['size']!=len(data): raise ValueError('Uploaded asset size mismatch; draft retained')
    request(f'https://api.github.com/repos/{repo}/releases/{release["id"]}',b'{"draft":false}',token,method='PATCH')
    print('Published '+release['html_url'])
