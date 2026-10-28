"""Regenerate docs/ for GitHub Pages at the custom domain habi-digitalgroup.com."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
origin = "https://www.habi-digitalgroup.com"
old_origin = "https://habi-digital-group.whiteswan32.chatgpt.site"
legacy_origin = "https://amparooskar-prog.github.io/Habi-Digital-Group"
for source in (root / "dist").rglob("*"):
    if not source.is_file():
        continue
    target = root / "docs" / source.relative_to(root / "dist")
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix in {".html", ".js", ".css", ".xml", ".txt"}:
        text = source.read_text()
        text = text.replace(old_origin, origin).replace(legacy_origin, origin)
        text = text.replace("/Habi-Digital-Group/", "/")
        target.write_text(text)
    else:
        shutil.copy2(source, target)
(root / "docs" / ".nojekyll").write_text("")
(root / "docs" / "CNAME").write_text("www.habi-digitalgroup.com\n")
print("Generated website files in docs/ for habi-digitalgroup.com")
