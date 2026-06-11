import os
from pathlib import Path

os.environ.setdefault("TELEGRAM_BOT_TOKEN", "LOCAL_TEST_TOKEN")

import eCoach_Bienestar_Fisico as app

pdf = Path(
    r"C:\Dev\eCoach_Bienestar_Fisico\DemoConversations\Analisi_Sang_Cerba_ANONIMIZADO_20250808.pdf"
)

text = app.extract_uploaded_file(pdf)

print("Extracted characters:", len(text))
print("Contains LDL:", "Colesterol LDL" in text)
print("Contains 119:", "119" in text)
print("Contains glucose 97.3:", "97.3" in text)
print()
print(text[:1200])
