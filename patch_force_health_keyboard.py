from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_force_health_keyboard")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

replacement = '''
def health_document_analysis_keyboard() -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(
        text="Crear Mi Plan",
        callback_data="health:create_mi_plan",
    )

    return InlineKeyboardMarkup(
        inline_keyboard=[[button]]
    )
'''

pattern = re.compile(
    r"(?ms)^def health_document_analysis_keyboard\(\) -> InlineKeyboardMarkup:\n"
    r".*?"
    r"(?=^def |^async def |\Z)"
)

matches = list(pattern.finditer(text))

if len(matches) != 1:
    raise SystemExit(
        f"Expected one health_document_analysis_keyboard function; found {len(matches)}."
    )

match = matches[0]

text = (
    text[:match.start()]
    + replacement.strip()
    + "\n\n"
    + text[match.end():]
)

path.write_text(text, encoding="utf-8")
print("Installed explicit one-button health keyboard.")
