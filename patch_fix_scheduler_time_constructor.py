from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_fix_scheduler_time")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

old = "time=time("
new = "time=dt_time("

count = text.count(old)

if count == 0:
    raise SystemExit("Could not find 'time=time('. Inspect the scheduler block manually.")

text = text.replace(old, new)

path.write_text(text, encoding="utf-8")

print(f"Replaced scheduler time constructor: {count} occurrence(s)")
