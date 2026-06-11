from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_bienestar_initial_flow")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")


# ---------------------------------------------------------------------
# 1. Add a dedicated upload keyboard.
# ---------------------------------------------------------------------

keyboard_code = r'''
def anonymized_documents_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Subir documentos anonimizados",
                    callback_data="upload_anonymized_documents",
                )
            ]
        ]
    )
'''

if "def anonymized_documents_keyboard()" not in text:
    marker = "\nasync def reply_initial_discovery_with_llm"
    if marker not in text:
        raise SystemExit(
            "Could not find reply_initial_discovery_with_llm insertion marker."
        )

    text = text.replace(
        marker,
        "\n" + keyboard_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted anonymized_documents_keyboard.")
else:
    print("anonymized_documents_keyboard already exists.")


# ---------------------------------------------------------------------
# 2. Make the initial LLM reply use the new single button.
# ---------------------------------------------------------------------

old_reply_markup = (
    "await update.message.reply_text("
    "answer, reply_markup=alternatives_path_keyboard())"
)

new_reply_markup = (
    "await update.message.reply_text("
    "answer, reply_markup=anonymized_documents_keyboard())"
)

count = text.count(old_reply_markup)

if count == 1:
    text = text.replace(old_reply_markup, new_reply_markup, 1)
    print("Changed initial discovery keyboard.")
elif count == 0 and new_reply_markup in text:
    print("Initial discovery keyboard already changed.")
else:
    raise SystemExit(
        f"Unexpected initial discovery reply count: {count}. "
        "Inspect reply_initial_discovery_with_llm manually."
    )


# ---------------------------------------------------------------------
# 3. Add a Bienestar Físico initial-message detector.
# ---------------------------------------------------------------------

detector_code = r'''
def detect_physical_wellbeing_initial_message(user_text: str) -> bool:
    text = (user_text or "").lower()

    doctor_signals = (
        "médico",
        "medico",
        "doctora",
        "doctor",
        "consulta",
    )

    health_signals = (
        "analítica",
        "analitica",
        "colesterol",
        "azúcar",
        "azucar",
        "glucosa",
        "perder peso",
        "bajar de peso",
        "adelgazar",
        "ejercicio",
        "comer mejor",
        "hábitos",
        "habitos",
        "prueba genética",
        "prueba genetica",
        "test genético",
        "test genetico",
    )

    document_signals = (
        "pdf",
        "subir",
        "analítica",
        "analitica",
        "informe",
        "datos genéticos",
        "datos geneticos",
    )

    has_doctor = any(signal in text for signal in doctor_signals)
    has_health = any(signal in text for signal in health_signals)
    has_documents = any(signal in text for signal in document_signals)

    return has_health and (has_doctor or has_documents)
'''

if "def detect_physical_wellbeing_initial_message" not in text:
    marker = "\nasync def handle_free_text"
    if marker not in text:
        raise SystemExit("Could not find handle_free_text insertion marker.")

    text = text.replace(
        marker,
        "\n" + detector_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted physical wellbeing initial detector.")
else:
    print("Physical wellbeing initial detector already exists.")


# ---------------------------------------------------------------------
# 4. Change handle_free_text to use the new detector.
# ---------------------------------------------------------------------

old_detector_call = "if detect_relationship_initial_message(user_text):"
new_detector_call = "if detect_physical_wellbeing_initial_message(user_text):"

count = text.count(old_detector_call)

if count == 1:
    text = text.replace(old_detector_call, new_detector_call, 1)
    print("Changed handle_free_text to the Bienestar detector.")
elif count == 0 and new_detector_call in text:
    print("Bienestar detector already active.")
else:
    raise SystemExit(
        f"Unexpected relationship detector call count: {count}."
    )


# ---------------------------------------------------------------------
# 5. Add the anonymized-upload button handler.
#
# This is deterministic UI text, not a substantive coaching answer.
# Actual interpretation will later go through the wellbeing skill + LLM.
# ---------------------------------------------------------------------

upload_handler_code = r'''
async def handle_upload_anonymized_documents_button(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query

    if query is not None:
        await query.answer()

        try:
            await clear_clicked_inline_keyboard(query)
        except Exception:
            pass

    message = query.message if query is not None else update.effective_message

    if message is None:
        return

    await message.reply_text(
        "Perfecto. Sube ahora la analítica y el informe genético usando "
        "el icono del clip de Telegram.\n\n"
        "Antes de enviarlos, comprueba que has eliminado o tapado nombre, "
        "DNI/NIE, dirección, teléfono, email, número de historia clínica, "
        "códigos QR o de barras y firmas.\n\n"
        "Cuando hayas subido todos los documentos, te indicaré el siguiente paso.",
        reply_markup=MAIN_KEYBOARD,
    )
'''

if "async def handle_upload_anonymized_documents_button" not in text:
    marker = "\ndef main() -> None:"
    if marker not in text:
        raise SystemExit("Could not find main() insertion marker.")

    text = text.replace(
        marker,
        "\n" + upload_handler_code.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted anonymized-upload callback handler.")
else:
    print("Upload callback handler already exists.")


# ---------------------------------------------------------------------
# 6. Register the new callback before generic free-text handling.
# ---------------------------------------------------------------------

registration = (
    '    app.add_handler(CallbackQueryHandler('
    'handle_upload_anonymized_documents_button, '
    'pattern=r"^upload_anonymized_documents$"))\n'
)

if "pattern=r\"^upload_anonymized_documents$\"" not in text:
    anchors = [
        (
            "    app.add_handler(MessageHandler("
            "filters.TEXT & ~filters.COMMAND, handle_free_text))"
        ),
        (
            "app.add_handler(MessageHandler("
            "filters.TEXT & ~filters.COMMAND, handle_free_text))"
        ),
    ]

    anchor = next((candidate for candidate in anchors if candidate in text), None)

    if anchor is None:
        raise SystemExit(
            "Could not find generic handle_free_text registration."
        )

    text = text.replace(anchor, registration + anchor, 1)
    print("Registered anonymized-upload callback.")
else:
    print("Upload callback already registered.")


# ---------------------------------------------------------------------
# 7. Disable the old real-time Relaciones message-handler registration.
#    The function may remain as dead code for now.
# ---------------------------------------------------------------------

activation_registration_pattern = re.compile(
    r'\n\s*app\.add_handler\(MessageHandler\(\s*'
    r'filters\.Regex\(.*?\)\s*&\s*~filters\.COMMAND,\s*'
    r'client_locked_handler\(handle_real_time_relationship_activation\),\s*'
    r'\)\)',
    flags=re.S,
)

text, disabled_count = activation_registration_pattern.subn(
    "\n    # Disabled inherited Relaciones real-time activation route.",
    text,
    count=1,
)

if disabled_count == 1:
    print("Disabled old Relaciones activation registration.")
elif disabled_count == 0:
    print(
        "Old Relaciones activation registration not found or already disabled."
    )


path.write_text(text, encoding="utf-8")
print("Bienestar Físico initial flow patch completed.")
