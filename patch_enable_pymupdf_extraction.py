from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_enable_pymupdf")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

old = '''    if suffix == ".pdf":
        return extract_pdf_text_and_tables(path)'''

new = '''    if suffix == ".pdf":
        return extract_pdf_text_with_pymupdf(path)'''

count = text.count(old)

if count != 1:
    raise SystemExit(
        f"Expected exactly one PDF extraction branch, found {count}."
    )

text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")

print("PDF uploads now use PyMuPDF.")
