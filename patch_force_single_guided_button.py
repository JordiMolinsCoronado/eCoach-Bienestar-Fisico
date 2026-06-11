from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------
# 1) Force alternatives_path_keyboard to one button only
# ---------------------------------------------------------------------

pattern = r'def alternatives_path_keyboard\(\) -> InlineKeyboardMarkup:\n.*?(?=\ndef |\nasync def |\n# ---------------------------------------------------------------------|\n[A-Z_]+\s*=|\Z)'

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

text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)

print("alternatives_path_keyboard replacements:", count)
if count != 1:
    raise SystemExit("ERROR: Could not replace alternatives_path_keyboard exactly once.")


# ---------------------------------------------------------------------
# 2) Strengthen initial_discovery.md: never print fake bracket button text
# ---------------------------------------------------------------------

skill_path = Path("skills/initial_discovery.md")
skill = skill_path.read_text(encoding="utf-8")

addition = """
## One-button UI rule for eCoach Relaciones

The client-facing answer must NOT include any fake button label in the text.

Never write:
- [Agencia Relacional Guiada]
- [Agencia relacional guiada]
- "button:"
- "pulsa el botón..."

The Telegram UI will show the real inline button.

The answer should end naturally with a short question, for example:
"¿Quieres activarla?"

Only the actual Telegram inline keyboard should contain:
Agencia Relacional Guiada

Also:
- Do not mention Gestionarlo sola.
- Do not mention Delegar el juicio.
- Do not describe three paths.
- There is only one proposed support mode: Agencia Relacional Guiada.
"""

if "## One-button UI rule for eCoach Relaciones" not in skill:
    skill = skill.rstrip() + "\n\n" + addition.strip() + "\n"
    skill_path.write_text(skill, encoding="utf-8")
    print("Updated initial_discovery.md with one-button UI rule.")
else:
    print("initial_discovery.md already has one-button UI rule.")


# ---------------------------------------------------------------------
# 3) Safety: if the exact old labels appear inside alternatives keyboard
#    replacement should have removed them from that function.
# ---------------------------------------------------------------------

path.write_text(text, encoding="utf-8")
print("Patched one-button keyboard and no fake bracket button text.")
