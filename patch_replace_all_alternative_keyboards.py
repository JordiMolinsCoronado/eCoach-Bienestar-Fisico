from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

replacement = '''def alternatives_path_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Agencia Relacional Guiada",
                    callback_data=GUIDED_PATH_CALLBACK,
                )
            ]
        ]
    )

'''

pattern = r'def alternatives_path_keyboard\(\) -> InlineKeyboardMarkup:\n.*?(?=\ndef |\nasync def |\n# ---------------------------------------------------------------------|\n[A-Z_]+\s*=|\Z)'

text, count = re.subn(pattern, replacement, text, flags=re.S)

print("alternatives_path_keyboard replacements:", count)

if count < 1:
    raise SystemExit("ERROR: no alternatives_path_keyboard definitions found.")

path.write_text(text, encoding="utf-8")
print("Replaced all alternatives_path_keyboard definitions with one-button version.")
