from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# Ensure timedelta is imported
if "timedelta" not in text.split("\n", 80)[0:80]:
    if re.search(r"from datetime import ([^\n]+)", text):
        def add_timedelta(match):
            imports = match.group(1)
            parts = [p.strip() for p in imports.split(",")]
            if "timedelta" not in parts:
                parts.append("timedelta")
            return "from datetime import " + ", ".join(parts)

        text = re.sub(r"from datetime import ([^\n]+)", add_timedelta, text, count=1)
    else:
        text = text.replace("import os\n", "import os\nfrom datetime import timedelta\n", 1)


def replace_last_async_def(source: str, name: str, new_code: str) -> str:
    pattern = rf'\nasync def {name}\(.*?\):.*?(?=\nasync def |\ndef |\n# ---------------------------------------------------------------------|\ndef main\(\) -> None:|\Z)'
    matches = list(re.finditer(pattern, source, flags=re.S))
    if not matches:
        raise SystemExit(f"Could not find async function: {name}")
    m = matches[-1]
    return source[:m.start()] + "\n" + new_code.rstrip() + "\n" + source[m.end():]


new_handler = r'''
async def handle_create_mi_plan_followup_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    activate_client_from_update(update)
    ensure_client_files()
    ensure_followup_triggers_file()

    tomorrow = today_app() + timedelta(days=1)
    followup_date = tomorrow.strftime("%Y-%m-%d")
    followup_time = "10:00"

    trigger = {
        "date": followup_date,
        "time": followup_time,
        "message_template": (
            "Seguimiento de agencia relacional guiada: revisar si apareció activación, "
            "separar hechos de historias, recordar valores relacionales y elegir el siguiente paso claro. "
            "Si hay algo importante, preparar material para la psicóloga."
        ),
        "reason": "Mi Plan de eCoach Relaciones — Laura",
        "source": "relaciones_mi_plan_button",
        "status": "pending",
    }

    saved_followups = save_immediate_followup_triggers(
        [trigger],
        source="relaciones_mi_plan_button",
    )

    if not saved_followups:
        await query.message.reply_text(
            "No he podido crear el seguimiento. Inténtalo de nuevo o revisa /scheduler_status.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    confirmation = """Listo, Laura. He creado el seguimiento para mañana a las 10:00.

Revisaremos:
- si apareció activación;
- si pudiste pausar antes de actuar;
- qué hechos había y qué historias construyó el miedo;
- qué valor relacional quieres cuidar ahora;
- y si conviene preparar algo para tu psicóloga.

No será para juzgarte. Si apareció ansiedad, no es un fracaso: es el momento exacto para practicar.

Mañana volvemos al siguiente paso claro."""

    await query.message.reply_text(
        confirmation,
        reply_markup=MAIN_KEYBOARD,
    )
'''

text = replace_last_async_def(text, "handle_create_mi_plan_followup_button", new_handler)

path.write_text(text, encoding="utf-8")
print("Patched relationship follow-up button to create a real pending trigger.")
