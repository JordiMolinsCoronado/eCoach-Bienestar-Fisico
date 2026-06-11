from pathlib import Path
import fitz  # PyMuPDF

INPUT_PDF = Path(r"C:\Dev\PrivateHealthFiles\Analisi_Sang_Cerba_ANONIMIZADO_20250808.pdf")
OUTPUT_PDF = Path(r"C:\Dev\eCoach_Bienestar_Fisico\DemoDocuments\Analisi_Sang_Cerba_ANONIMIZADO_20250808.pdf")

# Add every exact text string that must disappear.
TEXT_TO_REDACT = [
    "MOLINS CORONADO, JORDI",
    "BELTRAN MARGARIT, MARIA ISABEL",
]

if not INPUT_PDF.exists():
    raise FileNotFoundError(f"Input PDF not found: {INPUT_PDF}")

OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

document = fitz.open(INPUT_PDF)
matches_found = 0

for page_number, page in enumerate(document, start=1):
    for sensitive_text in TEXT_TO_REDACT:
        rectangles = page.search_for(sensitive_text)

        for rectangle in rectangles:
            # Slight padding helps cover glyph edges.
            padded = fitz.Rect(
                rectangle.x0 - 2,
                rectangle.y0 - 1,
                rectangle.x1 + 2,
                rectangle.y1 + 1,
            )

            page.add_redact_annot(
                padded,
                fill=(0, 0, 0),
            )
            matches_found += 1
            print(
                f"Found '{sensitive_text}' on page {page_number}: "
                f"{tuple(round(value, 1) for value in padded)}"
            )

# This permanently removes the underlying text/content.
for page in document:
    page.apply_redactions()

document.save(
    OUTPUT_PDF,
    garbage=4,
    deflate=True,
    clean=True,
)

document.close()

print()
print(f"Redactions applied: {matches_found}")
print(f"Saved anonymized PDF to: {OUTPUT_PDF}")

if matches_found == 0:
    print(
        "WARNING: No matching text was found. "
        "The PDF may be scanned, or the spelling may differ."
    )
