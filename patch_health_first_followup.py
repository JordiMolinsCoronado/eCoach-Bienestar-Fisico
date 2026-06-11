from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_health_first_followup")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")


# ------------------------------------------------------------
# 1. Add a health-specific callback constant.
# ------------------------------------------------------------

constant_anchor = (
    'HEALTH_CREATE_PLAN_CALLBACK = "health:create_mi_plan"\n'
)

constant_code = (
    'HEALTH_CREATE_PLAN_CALLBACK = "health:create_mi_plan"\n'
    'HEALTH_FIRST_FOLLOWUP_CALLBACK = "health:create_first_followup"\n'
)

if "HEALTH_FIRST_FOLLOWUP_CALLBACK" not in text:
    if constant_anchor not in text:
        raise SystemExit("Could not find HEALTH_CREATE_PLAN_CALLBACK anchor.")

    text = text.replace(
        constant_anchor,
        constant_code,
        1,
    )
    print("Inserted HEALTH_FIRST_FOLLOWUP_CALLBACK.")
else:
    print("Health follow-up callback constant already exists.")


# ------------------------------------------------------------
# 2. Add a one-button health follow-up keyboard.
# ------------------------------------------------------------

keyboard_code = r'''
def health_first_followup_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Crear seguimiento — mañana 08:00",
                    callback_data=HEALTH_FIRST_FOLLOWUP_CALLBACK,
                )
            ]
        ]
    )
'''

if "def health_first_followup_keyboard()" not in text:
    marker = "\ndef health_document_analysis_keyboard()"
    if marker not in text:
        raise SystemExit(
            "Could not find health_document_analysis_keyboard marker."
        )

    text = text.replace(
        marker,
        "\n" + keyboard_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted health_first_followup_keyboard.")
else:
    print("Health first-follow-up keyboard already exists.")


# ------------------------------------------------------------
# 3. Make Mi Plan end by offering the real follow-up button.
# ------------------------------------------------------------

old_markup = '''        reply_markup=None,
    )'''

new_markup = '''        reply_markup=health_first_followup_keyboard(),
    )'''

task_marker = (
    'task="Create Laura\'s practical Mi Plan from the analysed health documents.",'
)

task_position = text.find(task_marker)

if task_position == -1:
    raise SystemExit("Could not find the health Mi Plan task.")

markup_position = text.find(old_markup, task_position)

if markup_position == -1:
    if "reply_markup=health_first_followup_keyboard()" in text[task_position:task_position + 800]:
        print("Health Mi Plan follow-up keyboard already active.")
    else:
        raise SystemExit(
            "Could not find reply_markup=None after health Mi Plan task."
        )
else:
    text = (
        text[:markup_position]
        + new_markup
        + text[markup_position + len(old_markup):]
    )
    print("Health Mi Plan now offers the follow-up button.")


# ------------------------------------------------------------
# 4. Strengthen the Mi Plan prompt ending.
# ------------------------------------------------------------

prompt_anchor = '''Do not prescribe medication, supplements or HRT.
Do not define medical targets.
Use Spanish and keep it practical.'''

prompt_replacement = '''Do not prescribe medication, supplements or HRT.
Do not define medical targets.
Use Spanish and keep it practical.

At the end:
- address the user only as Laura;
- do not invent another name;
- say that eCoach can check in tomorrow morning;
- do not claim that the follow-up has already been created;
- do not print a fake button label;
- the Telegram interface will show the real follow-up button separately.'''

if prompt_anchor in text:
    text = text.replace(
        prompt_anchor,
        prompt_replacement,
        1,
    )
    print("Updated Mi Plan ending instructions.")
else:
    print("Mi Plan prompt anchor not found or already changed.")


# ------------------------------------------------------------
# 5. Add the real health follow-up callback handler.
# ------------------------------------------------------------

handler_code = r'''
async def handle_health_first_followup_button(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    activate_client_from_update(update)

    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    ensure_client_files()
    ensure_followup_triggers_file()

    tomorrow = today_app() + timedelta(days=1)
    followup_date = tomorrow.strftime("%Y-%m-%d")
    followup_time = "08:00"

    trigger = {
        "date": followup_date,
        "time": followup_time,
        "type": "physical_wellbeing_checkin",
        "message_template": (
            "Buenos días, Laura. Antes de seguir con el plan, quiero saber cómo estás.\n\n"
            "Tus registros recientes sugieren que has dormido peor y que tu frecuencia "
            "cardiaca en reposo y tu HRV se han movido respecto a tus valores habituales. "
            "Un wearable no permite saber la causa ni hacer un diagnóstico.\n\n"
            "Sé que la situación emocional con ese hombre puede estar influyendo, pero "
            "quiero comprobar si hay algo más: ¿has notado palpitaciones persistentes, "
            "mareo, dolor en el pecho, falta de aire, fiebre, enfermedad reciente, "
            "deshidratación, alcohol, cambios de medicación o algún otro cambio?\n\n"
            "Si el cambio persiste o aparece algún síntoma preocupante, sería prudente "
            "consultarlo con un profesional. Si tu pulsera permite registrar un ECG, "
            "puedes guardar una lectura para enseñársela al médico, pero no sustituye "
            "una valoración clínica.\n\n"
            "Y sobre Mi Plan: ¿pudiste hacer ayer una sola acción pequeña, aunque fueran "
            "cinco o diez minutos?"
        ),
        "reason": "Primer seguimiento de Mi Plan — eCoach Bienestar Físico",
        "source": "health_mi_plan_first_followup_button",
        "sensitivity": "medium",
        "requires_private_context": True,
        "status": "pending",
    }

    saved_followups = save_immediate_followup_triggers(
        [trigger],
        source="health_mi_plan_first_followup_button",
    )

    if not saved_followups:
        await query.message.reply_text(
            "No he podido crear el seguimiento. "
            "Inténtalo de nuevo o revisa /scheduler_status.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    await query.message.reply_text(
        "Listo, Laura. He creado un seguimiento para mañana a las 08:00.\n\n"
        "Comprobaremos cómo estás, cómo has dormido, si los datos de tu pulsera "
        "siguen fuera de tu patrón habitual y si pudiste empezar con una acción pequeña.\n\n"
        "No será un examen. Ajustaremos el plan sin juicio.",
        reply_markup=MAIN_KEYBOARD,
    )
'''

if "async def handle_health_first_followup_button" not in text:
    marker = "\ndef main() -> None:"
    if marker not in text:
        raise SystemExit("Could not find main() insertion marker.")

    text = text.replace(
        marker,
        "\n" + handler_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted health first-follow-up handler.")
else:
    print("Health first-follow-up handler already exists.")


# ------------------------------------------------------------
# 6. Register the new callback.
# ------------------------------------------------------------

registration = '''
    app.add_handler(
        CallbackQueryHandler(
            handle_health_first_followup_button,
            pattern=f"^{HEALTH_FIRST_FOLLOWUP_CALLBACK}$",
        )
    )
'''

registration_anchor = (
    '    app.add_handler(\n'
    '        CallbackQueryHandler(\n'
    '            handle_health_create_plan_button,'
)

if "pattern=f\"^{HEALTH_FIRST_FOLLOWUP_CALLBACK}$\"" not in text:
    anchor_position = text.find(registration_anchor)

    if anchor_position == -1:
        raise SystemExit(
            "Could not find health create-plan callback registration."
        )

    # Insert before the create-plan registration.
    text = (
        text[:anchor_position]
        + registration
        + "\n"
        + text[anchor_position:]
    )

    print("Registered health first-follow-up callback.")
else:
    print("Health follow-up callback already registered.")


path.write_text(text, encoding="utf-8")
print("Health first-follow-up patch completed.")
