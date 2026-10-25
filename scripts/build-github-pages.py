"""Regenerate docs/ for this repository's GitHub Pages project path."""
from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parents[1]
base='/Habi-Digital-Group'
origin='https://amparooskar-prog.github.io'+base
old='https://habi-digital-group.whiteswan32.chatgpt.site'
for p in (root/'dist').rglob('*'):
 if not p.is_file():continue
 target=root/'docs'/p.relative_to(root/'dist');target.parent.mkdir(parents=True,exist_ok=True)
 if p.suffix in {'.html','.js','.css','.xml','.txt'}:
  s=p.read_text().replace(old,origin)
  s=re.sub(r'((?:href|src|action)=["\'])/(?!/)',lambda m:m.group(1)+base+'/',s)
  target.write_text(s)
 else:shutil.copy2(p,target)
(root/'docs/.nojekyll').write_text('')
print('Generated GitHub Pages files in docs/')
