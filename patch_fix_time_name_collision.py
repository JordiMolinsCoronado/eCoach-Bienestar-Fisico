from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_fix_time_collision")
shutil.copy2(path, backup)
print(f"Backup: {backup}")

# Fix common datetime import forms.
patterns = [
    (
        r"from datetime import datetime, timedelta, time\b",
        "from datetime import datetime, timedelta, time as dt_time",
    ),
    (
        r"from datetime import datetime, time, timedelta\b",
        "from datetime import datetime, time as dt_time, timedelta",
    ),
    (
        r"from datetime import date, datetime, time, timedelta\b",
        "from datetime import date, datetime, time as dt_time, timedelta",
    ),
    (
        r"from datetime import datetime, date, time, timedelta\b",
        "from datetime import datetime, date, time as dt_time, timedelta",
    ),
]

replacement_count = 0

for pattern, replacement in patterns:
    text, count = re.subn(pattern, replacement, text, count=1)
    replacement_count += count

if replacement_count == 0:
    raise SystemExit(
        "Could not find a supported 'from datetime import ... time ...' line. "
        "Run Select-String and inspect the exact import."
    )

# Replace calls where datetime.time(...) is intended.
# Do not alter time.sleep(...), time.monotonic(...), etc.
text = re.sub(
    r"(?<![\w.])time\((\s*\d{1,2}\s*,)",
    r"dt_time(\1",
    text,
)

path.write_text(text, encoding="utf-8")
print("Fixed datetime.time / time module collision.")
