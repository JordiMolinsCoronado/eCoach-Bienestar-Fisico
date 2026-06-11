from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_pymupdf_extraction")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

# Ensure PyMuPDF import.
if "import fitz" not in text:
    import_anchor = "from pathlib import Path"
    if import_anchor not in text:
        raise SystemExit("Could not find pathlib import anchor.")

    text = text.replace(
        import_anchor,
        import_anchor + "\nimport fitz  # PyMuPDF",
        1,
    )
    print("Inserted PyMuPDF import.")
else:
    print("PyMuPDF already imported.")

extractor_code = r'''
def extract_pdf_text_with_pymupdf(pdf_path: Path) -> str:
    """
    Extract readable text from a PDF using PyMuPDF.

    This is used for laboratory and medical reports whose layout may not
    be extracted correctly by simpler PDF libraries.
    """
    document = fitz.open(str(pdf_path))

    try:
        pages = []

        for page_number, page in enumerate(document, start=1):
            page_text = page.get_text("text") or ""

            pages.append(
                f"\n===== PÁGINA {page_number} =====\n{page_text.strip()}"
            )

        return "\n".join(pages).strip()

    finally:
        document.close()
'''

if "def extract_pdf_text_with_pymupdf(" not in text:
    markers = [
        "\ndef extract_file_text",
        "\ndef extract_text_from_file",
        "\ndef extract_uploaded",
        "\ndef extract_latest_upload_session",
    ]

    marker = next((item for item in markers if item in text), None)

    if marker is None:
        raise SystemExit(
            "Could not locate a safe extraction-function insertion point."
        )

    text = text.replace(
        marker,
        "\n" + extractor_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted PyMuPDF PDF extractor.")
else:
    print("PyMuPDF extractor already exists.")

path.write_text(text, encoding="utf-8")
print("Stage 1 complete. PDF extractor added.")
