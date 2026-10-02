"""Package validated source records and original images. CC-BY-NC-4.0."""
import zipfile
from validate import ROOT,validate
if __name__=='__main__':
    manifest=validate(images=True);out=ROOT/'dist';out.mkdir(exist_ok=True)
    archive=out/f'Egyptian-Hieroglyphic-Corpus-{manifest["version"]}.zip'
    paths=[]
    for folder in ('data','images','docs','scripts'):
        paths.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    paths.extend(ROOT/n for n in ('README.md','LICENSE','CREDITS.md','gallery.html'))
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(paths): z.write(path,'Egyptian-Hieroglyphic-Corpus/'+str(path.relative_to(ROOT)))
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None: raise ValueError('Corrupt archive')
    print(archive)
