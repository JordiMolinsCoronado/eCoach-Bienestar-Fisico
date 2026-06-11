from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------
# 1) Replace alternatives keyboard with one-button guided agency keyboard
# ---------------------------------------------------------------------

keyboard_re = r'def alternatives_path_keyboard\(\) -> InlineKeyboardMarkup:\n.*?\n(?=def |\nasync def |\n# ---------------------------------------------------------------------)'
keyboard_new = r'''def alternatives_path_keyboard() -> InlineKeyboardMarkup:
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

text, n = re.subn(keyboard_re, keyboard_new, text, count=1, flags=re.S)
print("alternatives_path_keyboard replacements:", n)


# ---------------------------------------------------------------------
# 2) Strengthen initial_discovery skill: no three paths in Relaciones
# ---------------------------------------------------------------------

skill_path = Path("skills/initial_discovery.md")
skill = skill_path.read_text(encoding="utf-8")

addition = """
## eCoach Relaciones initial response rule

Do not offer three paths.
Do not offer:
- Gestionarlo sola
- Delegar el juicio
- Agencia relacional guiada

That three-path framing belongs to Patrimonio-style portfolio choices, not to this demo.

In Relaciones, the psychologist has already recommended the core direction:
- do not pursue anxiously;
- observe coherence;
- pause before reacting.

The eCoach should present only one proposed support mode:
Agencia Relacional Guiada.

The initial answer should be short:
1. validate the difficulty;
2. say the psychologist's recommendation is clear but hard to apply during activation;
3. clarify that eCoach does not replace the psychologist;
4. explain that eCoach helps practice between sessions when anxiety appears;
5. ask whether Laura wants to activate Agencia Relacional Guiada;
6. the only inline button is "Agencia Relacional Guiada".

Avoid long lists.
Avoid fictional alternatives.
Avoid asking her to choose between paths.
"""

if "## eCoach Relaciones initial response rule" not in skill:
    skill = skill.rstrip() + "\n\n" + addition.strip() + "\n"
    skill_path.write_text(skill, encoding="utf-8")
    print("Updated initial_discovery.md")
else:
    print("initial_discovery.md already has rule.")


path.write_text(text, encoding="utf-8")
print("Patched initial response to one-button Agencia Relacional Guiada.")
