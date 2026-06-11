from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_fix_health_plan_button")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")


# ------------------------------------------------------------------
# 1. Replace the health analysis keyboard with one button only.
# ------------------------------------------------------------------

keyboard_pattern = re.compile(
    r"(?ms)^def health_document_analysis_keyboard\(\) -> InlineKeyboardMarkup:\n"
    r".*?"
    r"(?=^def |^async def |\Z)"
)

keyboard_replacement = '''
def health_document_analysis_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Crear Mi Plan",
                    callback_data=HEALTH_CREATE_PLAN_CALLBACK,
                )
            ]
        ]
    )
'''

matches = list(keyboard_pattern.finditer(text))

if len(matches) != 1:
    raise SystemExit(
        f"Expected one health_document_analysis_keyboard, found {len(matches)}."
    )

match = matches[0]
text = (
    text[:match.start()]
    + keyboard_replacement.strip()
    + "\n\n"
    + text[match.end():]
)

print("Health analysis keyboard now has only Crear Mi Plan.")


# ------------------------------------------------------------------
# 2. Reactivate the correct Telegram client in every health callback.
# ------------------------------------------------------------------

handler_names = [
    "handle_health_create_plan_button",
    "handle_health_prepare_doctor_button",
    "handle_health_review_data_button",
]

for handler_name in handler_names:
    pattern = re.compile(
        rf"(?m)^(async def {re.escape(handler_name)}\(update, context\):\n)"
    )

    replacement = (
        rf"\1"
        "    activate_client_from_update(update)\n"
    )

    text, count = pattern.subn(replacement, text, count=1)

    if count == 1:
        print(f"Added client activation to {handler_name}.")
    else:
        print(
            f"Warning: could not patch {handler_name}; "
            "it may already be patched or have another signature."
        )


# ------------------------------------------------------------------
# 3. Change the document-analysis prompt from three choices to one.
# ------------------------------------------------------------------

old_prompt = '''9. End by inviting the user to choose:
   - Crear Mi Plan;
   - Preparar consulta médica;
   - Revisar analítica y genética.'''

new_prompt = '''9. End briefly by saying that the next step is to create Mi Plan.
Do not list several choices.
Do not ask the user to type a preference.
The Telegram interface will show one real button: Crear Mi Plan.'''

if old_prompt in text:
    text = text.replace(old_prompt, new_prompt, 1)
    print("Changed LLM analysis ending to one next step.")
else:
    print("Exact three-choice prompt not found; inspect generator if needed.")


# ------------------------------------------------------------------
# 4. Make the small UI line singular and explicit.
# ------------------------------------------------------------------

text = text.replace(
    '"Elige el siguiente paso:",',
    '"Siguiente paso:",',
)

path.write_text(text, encoding="utf-8")
print("Health Mi Plan button/state patch completed.")
