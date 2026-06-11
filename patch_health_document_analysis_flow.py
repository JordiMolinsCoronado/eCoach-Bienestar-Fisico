from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_health_document_flow")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")


def replace_top_level_function(source: str, name: str, replacement: str) -> str:
    """
    Replace every top-level def/async def with this exact name.
    Uses indentation boundaries rather than a broad global cleanup.
    """
    pattern = re.compile(
        rf"(?ms)^(?:async\s+def|def)\s+{re.escape(name)}\s*\(.*?"
        rf"(?=^(?:async\s+def|def)\s+\w+\s*\(|^# ---|\Z)"
    )

    matches = list(pattern.finditer(source))
    if not matches:
        raise SystemExit(f"Could not find function: {name}")

    for match in reversed(matches):
        source = (
            source[:match.start()]
            + replacement.rstrip()
            + "\n\n"
            + source[match.end():]
        )

    print(f"Replaced {name}: {len(matches)} definition(s)")
    return source


# ---------------------------------------------------------------------
# 1. Health-specific keyboards
# ---------------------------------------------------------------------

health_keyboards = r'''
HEALTH_CREATE_PLAN_CALLBACK = "health:create_mi_plan"
HEALTH_PREPARE_DOCTOR_CALLBACK = "health:prepare_doctor"
HEALTH_REVIEW_DATA_CALLBACK = "health:review_data"


def health_document_analysis_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Crear Mi Plan",
                    callback_data=HEALTH_CREATE_PLAN_CALLBACK,
                )
            ],
            [
                InlineKeyboardButton(
                    "Preparar consulta médica",
                    callback_data=HEALTH_PREPARE_DOCTOR_CALLBACK,
                )
            ],
            [
                InlineKeyboardButton(
                    "Revisar analítica y genética",
                    callback_data=HEALTH_REVIEW_DATA_CALLBACK,
                )
            ],
        ]
    )


def health_last_document_context_file(client_dir: Path | None = None) -> Path:
    base = client_dir or active_client_dir()
    base.mkdir(parents=True, exist_ok=True)
    return base / "last_health_document_context.txt"


def save_health_document_context(
    extracted_context: str,
    client_dir: Path | None = None,
) -> None:
    health_last_document_context_file(client_dir).write_text(
        extracted_context,
        encoding="utf-8",
    )


def load_health_document_context(
    client_dir: Path | None = None,
) -> str:
    context_file = health_last_document_context_file(client_dir)

    if not context_file.exists():
        return ""

    return context_file.read_text(
        encoding="utf-8",
        errors="ignore",
    ).strip()
'''

if "def health_document_analysis_keyboard()" not in text:
    marker = "\ndef build_uploaded_docs_orchestrator_message"
    if marker not in text:
        raise SystemExit(
            "Could not find build_uploaded_docs_orchestrator_message marker."
        )

    text = text.replace(
        marker,
        "\n" + health_keyboards.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted health document keyboards and context storage.")
else:
    print("Health document keyboards already exist.")


# ---------------------------------------------------------------------
# 2. Health-specific LLM analysis
# ---------------------------------------------------------------------

health_generator = r'''
def generate_health_document_analysis(extracted_context: str) -> str:
    facts = f"""
The user uploaded anonymised health documents.

The uploaded content may include:
- a recent blood test;
- cholesterol and glucose values;
- an ancestry-oriented genetic test;
- possible APOE information;
- other health information.

EXTRACTED DOCUMENT CONTENT:
{extracted_context}

The user's known context:
- Laura is 48.
- She wants to lose weight.
- Her doctor said cholesterol and glucose were slightly elevated but not currently alarming.
- The doctor recommended more exercise, better nutrition and lifestyle changes.
- The consultation lasted around 15 minutes and no detailed daily plan was created.
- The user asks for help understanding what to discuss with the doctor and how to act safely between appointments.

Required analysis:
1. Brief confirmation that the documents were read.
2. Sources and limitations:
   - distinguish blood-test data from genetic-test data;
   - say if data are missing or unclear;
   - do not invent values.
3. What the documents clearly show.
4. What requires medical interpretation.
5. If APOE ε3/ε4 appears:
   - describe it as a susceptibility factor, not a diagnosis;
   - do not imply disease or destiny;
   - explain that an ancestry test may need clinical confirmation;
   - say it is worth taking to the doctor;
   - do not claim that APOE automatically defines one cholesterol threshold.
6. Intelligent emotional framing:
   - no panic;
   - no dismissal;
   - context, sustainable action and medical follow-up.
7. Safe lifestyle opportunities consistent with the doctor's general advice:
   - movement;
   - resistance training if appropriate;
   - protein and fibre anchors;
   - fewer sugary drinks and refined snacks;
   - sleep;
   - gradual weight-loss habits.
8. Questions for the doctor:
   - whether APOE needs clinical confirmation;
   - overall cardiovascular-risk assessment;
   - personal cholesterol and glucose objectives;
   - whether ApoB, Lp(a), HbA1c, blood pressure or other tests are useful.
9. End by inviting the user to choose:
   - Crear Mi Plan;
   - Preparar consulta médica;
   - Revisar analítica y genética.

Safety:
- Do not diagnose.
- Do not prescribe.
- Do not recommend medication or HRT.
- Do not replace the doctor.
- Use Spanish.
- Mobile-friendly Telegram format.
- Avoid wide Markdown tables.
"""

    return generate_skill_client_reply(
        "manage_physical_wellbeing",
        "Analyse the anonymised health documents and write the client-facing response.",
        facts,
    )
'''

if "def generate_health_document_analysis(" not in text:
    marker = "\nasync def handle_uploaded_document"
    if marker not in text:
        raise SystemExit("Could not find handle_uploaded_document marker.")

    text = text.replace(
        marker,
        "\n" + health_generator.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted health document LLM generator.")
else:
    print("Health document generator already exists.")


# ---------------------------------------------------------------------
# 3. Replace both analysis handlers
# ---------------------------------------------------------------------

message_handler = r'''
async def analyze_uploaded_documents_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    client_name = client_name_from_update(update)
    set_current_client_name(client_name)
    ensure_client_files()

    message = update.effective_message
    if message is None:
        return

    thinking_message = await message.reply_text("Pensando...")

    try:
        session_dir, extracted_context = await asyncio.to_thread(
            extract_latest_upload_session
        )

        if (
            session_dir is None
            or not extracted_context.strip()
            or extracted_context.startswith("No hay")
        ):
            try:
                await thinking_message.delete()
            except Exception:
                pass

            await message.reply_text(extracted_context)
            return

        save_health_document_context(
            extracted_context,
            active_client_dir(),
        )

        answer = await asyncio.to_thread(
            generate_health_document_analysis,
            extracted_context,
        )

        marker = active_upload_session_marker_file()
        if marker.exists():
            marker.unlink()

        ecoach_mark_documents_analyzed(active_client_dir())
        ecoach_mark_diagnosis_complete(
            active_client_dir(),
            source="uploaded_health_documents_message",
        )

        try:
            await thinking_message.delete()
        except Exception:
            pass

        await send_long_message(
            update,
            answer,
            reply_markup=health_document_analysis_keyboard(),
        )

    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        await message.reply_text(
            f"No he podido analizar los documentos de salud: {error}",
            reply_markup=MAIN_KEYBOARD,
        )
'''

callback_handler = r'''
async def analyze_uploaded_documents_callback_handler(
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

    client_name = client_name_from_update(update)
    set_current_client_name(client_name)
    ensure_client_files()

    message = query.message if query is not None else update.effective_message
    if message is None:
        return

    thinking_message = await message.reply_text("Pensando...")

    try:
        session_dir, extracted_context = await asyncio.to_thread(
            extract_latest_upload_session
        )

        if (
            session_dir is None
            or not extracted_context.strip()
            or extracted_context.startswith("No hay")
        ):
            try:
                await thinking_message.delete()
            except Exception:
                pass

            await message.reply_text(extracted_context)
            return

        save_health_document_context(
            extracted_context,
            active_client_dir(),
        )

        answer = await asyncio.to_thread(
            generate_health_document_analysis,
            extracted_context,
        )

        marker = active_upload_session_marker_file()
        if marker.exists():
            marker.unlink()

        ecoach_mark_documents_analyzed(active_client_dir())
        ecoach_mark_diagnosis_complete(
            active_client_dir(),
            source="uploaded_health_documents_callback",
        )

        try:
            await thinking_message.delete()
        except Exception:
            pass

        await reply_message_text_in_chunks(message, answer)

        await message.reply_text(
            "Elige el siguiente paso:",
            reply_markup=health_document_analysis_keyboard(),
        )

    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        await message.reply_text(
            f"No he podido analizar los documentos de salud: {error}",
            reply_markup=MAIN_KEYBOARD,
        )
'''

text = replace_top_level_function(
    text,
    "analyze_uploaded_documents_handler",
    message_handler,
)

text = replace_top_level_function(
    text,
    "analyze_uploaded_documents_callback_handler",
    callback_handler,
)


# ---------------------------------------------------------------------
# 4. Change upload-summary button and text
# ---------------------------------------------------------------------

text = text.replace(
    'InlineKeyboardButton("📄 Analizar documentos", '
    'callback_data="analyze_uploaded_documents")',
    'InlineKeyboardButton("Analizar documentos de salud", '
    'callback_data="analyze_uploaded_documents")',
)

text = text.replace(
    "Cuando haya subido todos, pulse el botón de abajo.",
    "Cuando haya subido todos, pulsa el botón de abajo.",
)

print("Updated upload summary button text.")


# ---------------------------------------------------------------------
# 5. Health action handlers
# ---------------------------------------------------------------------

action_handlers = r'''
async def handle_health_create_plan_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    extracted_context = load_health_document_context(active_client_dir())

    if not extracted_context:
        await query.message.reply_text(
            "No encuentro el análisis de salud anterior. "
            "Sube de nuevo los documentos y analízalos primero.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    facts = f"""
Create Mi Plan for Laura using the uploaded health-document context.

DOCUMENT CONTEXT:
{extracted_context}

Known situation:
- Laura is 48.
- She wants to lose weight.
- Her doctor recommended more exercise, better nutrition and lifestyle change.
- Cholesterol and glucose were described as slightly elevated but not alarming.
- The plan must support daily agency without replacing the doctor.

Mi Plan must include:
1. A small realistic movement target.
2. A fallback target for difficult days.
3. Around two resistance-training sessions weekly if appropriate.
4. Simple protein and fibre anchors.
5. Reducing sugary drinks and refined snacks.
6. Sleep and recovery.
7. A low-frequency weight/waist trend.
8. Medical questions and what to take to the doctor.
9. APOE safety and possible clinical confirmation if relevant.
10. Follow-up logic.

Do not prescribe medication, supplements or HRT.
Do not define medical targets.
Use Spanish and keep it practical.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_physical_wellbeing",
        task="Create Laura's practical Mi Plan from the analysed health documents.",
        facts=facts,
        reply_markup=None,
    )


async def handle_health_prepare_doctor_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    extracted_context = load_health_document_context(active_client_dir())

    if not extracted_context:
        await query.message.reply_text(
            "No encuentro el análisis anterior. "
            "Sube y analiza los documentos de nuevo.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    facts = f"""
Prepare a concise doctor-appointment brief for Laura.

DOCUMENT CONTEXT:
{extracted_context}

Include:
- short summary of the blood-test findings;
- genetic-test source and limitations;
- APOE questions if relevant;
- symptoms and family-history questions;
- possible questions about ApoB, Lp(a), HbA1c and blood pressure;
- personal cholesterol and glucose objectives;
- what lifestyle changes Laura has started.

Do not diagnose or prescribe.
Use Spanish.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_physical_wellbeing",
        task="Prepare Laura's concise doctor appointment brief and questions.",
        facts=facts,
        reply_markup=None,
    )


async def handle_health_review_data_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    extracted_context = load_health_document_context(active_client_dir())

    if not extracted_context:
        await query.message.reply_text(
            "No encuentro los documentos analizados. "
            "Sube y analiza los archivos de nuevo.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    facts = f"""
Review the blood-test and genetic information in greater detail.

DOCUMENT CONTEXT:
{extracted_context}

Structure:
1. Clearly observed values.
2. Missing or unclear information.
3. What may be relevant.
4. What requires medical confirmation.
5. APOE source-quality and safety explanation if relevant.
6. Questions for the doctor.

Do not diagnose.
Do not prescribe.
Do not catastrophise.
Use Spanish.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_physical_wellbeing",
        task="Give a focused review of Laura's blood-test and genetic data.",
        facts=facts,
        reply_markup=health_document_analysis_keyboard(),
    )
'''

if "async def handle_health_create_plan_button" not in text:
    marker = "\ndef main() -> None:"
    if marker not in text:
        raise SystemExit("Could not find main() marker.")

    text = text.replace(
        marker,
        "\n" + action_handlers.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )
    print("Inserted health action handlers.")
else:
    print("Health action handlers already exist.")


# ---------------------------------------------------------------------
# 6. Ensure live registrations exist
# ---------------------------------------------------------------------

registrations = '''
    app.add_handler(
        CallbackQueryHandler(
            analyze_uploaded_documents_callback_handler,
            pattern=r"^analyze_uploaded_documents$",
        )
    )
    app.add_handler(MessageHandler(filters.Document.ALL, handle_uploaded_document))

    app.add_handler(
        CallbackQueryHandler(
            handle_health_create_plan_button,
            pattern=f"^{HEALTH_CREATE_PLAN_CALLBACK}$",
        )
    )
    app.add_handler(
        CallbackQueryHandler(
            handle_health_prepare_doctor_button,
            pattern=f"^{HEALTH_PREPARE_DOCTOR_CALLBACK}$",
        )
    )
    app.add_handler(
        CallbackQueryHandler(
            handle_health_review_data_button,
            pattern=f"^{HEALTH_REVIEW_DATA_CALLBACK}$",
        )
    )
'''

registration_marker = (
    'app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_free_text))'
)

if "pattern=f\"^{HEALTH_CREATE_PLAN_CALLBACK}$\"" not in text:
    if registration_marker not in text:
        raise SystemExit(
            "Could not find active generic handle_free_text registration."
        )

    text = text.replace(
        registration_marker,
        registrations.rstrip() + "\n\n    " + registration_marker,
        1,
    )
    print("Registered document and health action handlers.")
else:
    print("Health handlers already registered.")


path.write_text(text, encoding="utf-8")
print("Health document-analysis flow patch complete.")
