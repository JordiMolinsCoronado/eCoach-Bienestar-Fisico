from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_disable_patrimonio_controls")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

replacement = r'''
async def try_handle_ecoach_control_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_text: str,
) -> bool:
    """
    eCoach Bienestar Físico does not use inherited Patrimonio
    free-text control branches.

    Health messages, explicit reminders and follow-up replies must
    continue through the health/router flow.
    """
    return False
'''

pattern = re.compile(
    r"(?ms)^async def try_handle_ecoach_control_message\(.*?"
    r"(?=^async def |^def |\Z)"
)

matches = list(pattern.finditer(text))

if len(matches) != 1:
    raise SystemExit(
        f"Expected exactly one try_handle_ecoach_control_message function, "
        f"found {len(matches)}."
    )

match = matches[0]

text = (
    text[:match.start()]
    + replacement.strip()
    + "\n\n"
    + text[match.end():]
)

path.write_text(text, encoding="utf-8")

print("Disabled inherited Patrimonio free-text control branches.")
