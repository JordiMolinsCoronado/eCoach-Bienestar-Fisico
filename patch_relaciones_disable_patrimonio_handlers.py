from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# Relationship project metadata
text = re.sub(
    r'ECOACH_PROJECT_ID = ".*?"',
    'ECOACH_PROJECT_ID = "saturday_demo_relationships_guided_agency"',
    text,
    count=1,
)

text = re.sub(
    r'ECOACH_PROJECT_TITLE = ".*?"',
    'ECOACH_PROJECT_TITLE = "Piloto sábado - agencia relacional guiada"',
    text,
    count=1,
)

# Visible board labels
replacements = {
    'label="Cartera guiada"': 'label="Agencia relacional guiada"',
    'label="Cartera guiada con eCoach"': 'label="Agencia relacional guiada con eCoach"',
    'label="Entender cartera antes de mover dinero"': 'label="Entender la dinámica antes de actuar"',
    'label="Esperando extracto, PDFs, Excel, ISINs o listado de fondos"': 'label="Esperando relato, mensajes o hechos concretos"',
    'label="Esperando documentos de cartera"': 'label="Esperando relato o hechos de la situación"',
}

for old, new in replacements.items():
    text = text.replace(old, new)

# Disable Patrimonio-specific handlers in main()
disabled_patterns = [
    "handle_uploaded_document",
    "analyze_uploaded_documents_handler",
    "handle_public_enrichment_button",
    "handle_private_bank_data_button",
    "handle_search_funds_button",
    "PROVIDER_MYINVESTOR_CALLBACK",
    "PROVIDER_RENTA4_CALLBACK",
    "PROVIDER_OPENBANK_CALLBACK",
    "PROVIDER_DIAPHANUM_CALLBACK",
    "PROVIDER_EBN_CALLBACK",
    "PUBLIC_ENRICHMENT_CALLBACK",
    "PRIVATE_BANK_DATA_CALLBACK",
    "SEARCH_FUNDS_CALLBACK",
]

new_lines = []
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith("app.add_handler(") and any(pattern in line for pattern in disabled_patterns):
        if "Disabled in eCoach Relaciones demo" not in line:
            new_lines.append("    # Disabled in eCoach Relaciones demo: " + stripped)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

text = "\n".join(new_lines) + "\n"

path.write_text(text, encoding="utf-8")
print("Patched Relaciones metadata and disabled Patrimonio-specific handlers.")
