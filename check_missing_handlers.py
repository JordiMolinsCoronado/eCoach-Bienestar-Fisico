from pathlib import Path
import re

text = Path("eCoach_Relaciones.py").read_text(encoding="utf-8")
registered = set(re.findall(r"CallbackQueryHandler\((handle_[A-Za-z0-9_]+)", text))
defined = set(re.findall(r"async def (handle_[A-Za-z0-9_]+)\(", text))
missing = sorted(registered - defined)

print("Missing callback handlers:")
for name in missing:
    print("-", name)
print("Count:", len(missing))
