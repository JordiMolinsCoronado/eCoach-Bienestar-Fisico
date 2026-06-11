from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_fix_time_annotations")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

replacements = {
    "-> time | None": "-> dt_time | None",
    ": time | None": ": dt_time | None",
    "-> time:": "-> dt_time:",
    ": time,": ": dt_time,",
    ": time)": ": dt_time)",
}

total = 0

for old, new in replacements.items():
    count = text.count(old)
    if count:
        text = text.replace(old, new)
        total += count
        print(f"Replaced {count}: {old} -> {new}")

path.write_text(text, encoding="utf-8")
print(f"Total replacements: {total}")
