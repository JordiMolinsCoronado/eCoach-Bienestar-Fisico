from pathlib import Path
import re
import shutil

python_path = Path("eCoach_Bienestar_Fisico.py")
initial_skill_path = Path("skills/initial_discovery.md")
health_skill_path = Path("skills/manage_physical_wellbeing.md")

python_text = python_path.read_text(encoding="utf-8")
initial_text = initial_skill_path.read_text(encoding="utf-8")
health_text = health_skill_path.read_text(encoding="utf-8")

shutil.copy2(
    python_path,
    python_path.with_suffix(".py.before_demo_text_cleanup"),
)
shutil.copy2(
    initial_skill_path,
    initial_skill_path.with_suffix(".md.before_demo_text_cleanup"),
)
shutil.copy2(
    health_skill_path,
    health_skill_path.with_suffix(".md.before_demo_text_cleanup"),
)

print("Backups created.")


# ============================================================
# 1. CLEAN /START
# ============================================================

start_pattern = re.compile(
    r'(?ms)^async def start\(.*?'
    r'(?=^async def |^def |\Z)'
)

start_matches = list(start_pattern.finditer(python_text))

if len(start_matches) != 1:
    raise SystemExit(
        f"Expected one start() function, found {len(start_matches)}."
    )

new_start = r'''
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    activate_client_from_update(update)

    message = update.effective_message
    if message is None:
        return

    welcome = """Hola. Soy eCoach Bienestar Físico.

Te ayudo a convertir recomendaciones médicas generales en un plan diario claro, seguro y sostenible.

No sustituyo a tu médico.
No diagnostico.
No prescribo tratamientos.

El médico mantiene la autoridad clínica.
Tú recuperas agencia diaria.
Yo mantengo vivo el hilo entre consultas.

Puedo ayudarte con:

Quién soy
Ver tu contexto y situación de salud.

Qué quiero
Ver tus objetivos de bienestar físico.

Plan de acción
Ver tu Mi Plan y el siguiente paso concreto.

Seguimientos
Ver recordatorios y revisiones pendientes."""

    await message.reply_text(
        welcome,
        reply_markup=MAIN_KEYBOARD,
    )
'''

match = start_matches[0]

python_text = (
    python_text[:match.start()]
    + new_start.strip()
    + "\n\n"
    + python_text[match.end():]
)

print("Cleaned /start message.")


# ============================================================
# 2. REMOVE THE REDUNDANT SECOND UPLOAD MESSAGE
# ============================================================

redundant_upload_message = '''    await update.message.reply_text(
        "Perfecto. Sube ahora la analítica y el informe genético usando el icono del clip de Telegram.\\n\\n"
        "Antes de enviarlos, comprueba que has eliminado o tapado nombre, DNI/NIE, dirección, teléfono, email, número de historia clínica, códigos QR o de barras y firmas.\\n\\n"
        "Cuando hayas subido todos los documentos, te indicaré el siguiente paso.",
'''

if redundant_upload_message in python_text:
    start = python_text.find(redundant_upload_message)
    end = python_text.find(
        "    )",
        start,
    )

    if end == -1:
        raise SystemExit(
            "Found redundant upload message but could not find its closing parenthesis."
        )

    end += len("    )")

    python_text = (
        python_text[:start]
        + python_text[end:]
    )

    print("Removed redundant upload instruction message.")
else:
    print(
        "Exact redundant upload message not found. "
        "The initial-discovery skill will still prevent it in generated text."
    )


# ============================================================
# 3. REWRITE INITIAL DISCOVERY INSTRUCTIONS
# ============================================================

initial_cleanup_section = r'''

## Bienestar Físico demo — initial response rules

For Laura's initial message:

- Respond warmly and briefly.
- Explain that a short medical consultation may give direction without enough time to build a practical plan.
- State briefly that eCoach does not replace the doctor and does not diagnose or prescribe.
- Confirm that Laura may upload:
  - the recent blood-test PDF;
  - the genetic-test TXT or report.
- Ask her to anonymise personal identifiers before uploading.

The anonymisation explanation must be concise.

Say:

"Antes de subirlos, tapa o elimina nombre, DNI/NIE, dirección, teléfono, email, número de historia clínica, códigos QR o de barras y firmas.

Si quieres, te puedo decir cómo tapar datos de un PDF de manera fácil y segura."

Do not include a long technical explanation of PDF redaction unless Laura explicitly asks for it.

Do not include:

- step-by-step PDF editing instructions;
- Ctrl+A instructions;
- repeated upload instructions;
- "Antes de enviarlos, comprueba...";
- "Cuando hayas subido todos...";
- "Un abrazo";
- "Con calidez";
- signatures such as "eCoach".

End simply by inviting Laura to upload the anonymised files.
'''

marker = "## Bienestar Físico demo — initial response rules"

if marker in initial_text:
    initial_text = (
        initial_text.split(marker, 1)[0].rstrip()
        + "\n"
        + initial_cleanup_section
    )
else:
    initial_text = (
        initial_text.rstrip()
        + "\n"
        + initial_cleanup_section
    )

print("Updated initial-discovery response rules.")


# ============================================================
# 4. REWRITE DOCUMENT-DIAGNOSIS RULES
# ============================================================

diagnostic_section = r'''

## Health-document analysis — strict structure

The document-analysis response is the diagnostic and interpretation stage.

It must contain:

### 1. Documents and limitations

Briefly identify:

- the clinical blood-test report;
- the direct-to-consumer ancestry genetic extract;
- the fact that the genetic result is not a clinical diagnosis and may require confirmation.

### 2. Concise results summary

Include the important document-derived facts here:

- LDL: 3.09 mmol/L / 119 mg/dL, slightly above the laboratory reference.
- Total cholesterol: 4.88 mmol/L.
- HDL: 1.46 mmol/L.
- Triglycerides: 0.77 mmol/L.
- Fasting glucose: 5.4 mmol/L, within the laboratory reference interval.
- APOE markers compatible with ε3/ε4.
- TSH, iron, vitamin B12 and folate within the report's ranges.
- eGFR: 76 mL/min, for the doctor to interpret in clinical context.
- Mention only other findings that are genuinely relevant.

### 3. Clinical interpretation boundary

Explain briefly:

- APOE ε3/ε4 is susceptibility information, not a diagnosis or destiny.
- LDL and APOE should be brought together to the doctor.
- The doctor must assess overall cardiovascular risk and personal targets.
- The direct-to-consumer result may need clinical confirmation.
- Do not alarm Laura.

### 4. Questions for the doctor

Include:

1. "¿El resultado APOE ε3/ε4 necesita confirmación clínica?"
2. "¿Cómo valora mi riesgo cardiovascular global y qué objetivo personal de LDL sería adecuado?"
3. "¿Sería útil medir ApoB, Lp(a), HbA1c o revisar la tensión arterial?"
4. "¿Conviene revisar la función renal o repetir creatinina/eGFR?"
5. "¿La menopausia o transición menopáusica cambia algo en mi valoración?"
6. "Con 1,65 m, 84,4 kg y un IMC aproximado de 31, ¿soy candidata a semaglutida o tirzepatida?"
7. "¿Qué opción podría tener más sentido, qué beneficio sería realista y qué contraindicaciones o efectos adversos habría que revisar?"
8. "¿Cómo protegeríamos masa muscular y fuerza durante la pérdida de peso?"

The diagnostic response must not contain a lifestyle plan.

Do not include here:

- daily walking targets;
- fallback movement targets;
- resistance-training prescriptions;
- protein or fibre anchors;
- food rules;
- sleep routines;
- hydration routines;
- weighing routines;
- motivational adherence rules.

Those belong only in Mi Plan.

Do not say:

- "Gracias por confiarme tus documentos";
- "Gracias por compartir";
- "Un abrazo";
- "Dime cuál prefieres".

End briefly:

"El siguiente paso es convertir esta información en un plan diario concreto."

The Telegram interface will show one button:

Crear Mi Plan
'''

diagnostic_marker = "## Health-document analysis — strict structure"

if diagnostic_marker in health_text:
    health_text = (
        health_text.split(diagnostic_marker, 1)[0].rstrip()
        + "\n"
        + diagnostic_section
    )
else:
    health_text = (
        health_text.rstrip()
        + "\n"
        + diagnostic_section
    )

print("Added strict diagnostic-stage structure.")


# ============================================================
# 5. ADD STRICT MI PLAN RULES AFTER THE DIAGNOSTIC SECTION
# ============================================================

mi_plan_section = r'''

## Mi Plan — strict structure

Mi Plan is the action stage.

Do not repeat the diagnostic explanation.

Do not begin with:

- "Gracias por compartir tus documentos";
- a summary of LDL;
- a summary of APOE;
- a summary of glucose;
- a summary of kidney, thyroid, iron or vitamin results;
- "No necesitas alarmarte";
- another explanation of why the reports should go to the doctor.

That information has already been given in the document-analysis stage.

Start directly:

"# Mi Plan para Laura"

Then include:

### 1. First two weeks

Give a concrete, sustainable starting plan:

- daily movement target;
- fallback target for difficult days;
- two resistance-training sessions weekly if medically appropriate;
- protein and fibre anchors;
- reduction of sugary drinks and highly processed snacks;
- sleep routine;
- hydration;
- low-frequency weight and waist tracking.

### 2. Modern obesity medicines

Laura is:

- 48 years old;
- 1.65 m;
- 84.4 kg;
- BMI approximately 31.

Explain:

- semaglutide and tirzepatide may be medically relevant because BMI is approximately 31;
- semaglutide produced roughly 15% mean weight loss in a major obesity trial;
- tirzepatide produced roughly 15% to 21% mean weight loss across studied doses;
- at 84.4 kg, this corresponds only illustratively to approximately 13–18 kg;
- these are trial averages, not personal predictions;
- the doctor must assess eligibility, contraindications, adverse effects, expected benefit, long-term treatment and muscle preservation;
- do not prescribe or recommend dosing.

### 3. Consultation preparation

Do not repeat the complete laboratory summary.

Only provide a compact carry-list:

- blood-test report;
- genetic extract;
- wearable trend summary;
- any relevant symptoms;
- written questions.

The detailed medical questions have already appeared in the diagnostic stage, so do not reproduce the full numbered list again.

You may say:

"Guarda también las preguntas que preparamos en el análisis anterior."

### 4. Adherence and follow-up

Explain briefly:

- the plan does not require perfection;
- after a missed day, resume at the next opportunity;
- eCoach can check in the following morning.

Do not include:

- "Un abrazo";
- a signature;
- invented names;
- claims that a follow-up has already been created.

The real Telegram follow-up button appears separately.
'''

health_text = (
    health_text.rstrip()
    + "\n"
    + mi_plan_section
)

print("Added strict Mi Plan structure.")


# ============================================================
# 6. STRENGTHEN THE HEALTH-ANALYSIS GENERATOR PROMPT
# ============================================================

analysis_task_marker = (
    "The user uploaded anonymised health documents."
)

analysis_position = python_text.find(analysis_task_marker)

if analysis_position == -1:
    raise SystemExit(
        "Could not find the health-document analysis facts block."
    )

analysis_insert_marker = "Write the answer in Spanish."

analysis_insert_position = python_text.find(
    analysis_insert_marker,
    analysis_position,
)

if analysis_insert_position != -1:
    analysis_insert_position += len(analysis_insert_marker)

    extra_analysis_rules = '''

This is the diagnostic stage, not Mi Plan.

Include:
- a concise results summary;
- medical interpretation boundaries;
- doctor questions, including semaglutide and tirzepatide because Laura is 1.65 m, 84.4 kg and BMI approximately 31.

Do not include:
- walking targets;
- resistance-training plans;
- protein/fibre plans;
- sleep routines;
- hydration;
- weight-tracking routines;
- adherence coaching.

Do not thank Laura for sharing the documents.
Do not sign the answer.
Do not say "Un abrazo".
Do not ask her to type a choice.
'''

    python_text = (
        python_text[:analysis_insert_position]
        + extra_analysis_rules
        + python_text[analysis_insert_position:]
    )

    print("Strengthened document-analysis generator prompt.")
else:
    print(
        "Could not find 'Write the answer in Spanish.' "
        "The skill rules will still apply."
    )


# ============================================================
# 7. STRENGTHEN MI PLAN PROMPT
# ============================================================

mi_plan_task_marker = (
    'task="Create Laura\'s practical Mi Plan from the analysed health documents.",'
)

mi_plan_position = python_text.find(mi_plan_task_marker)

if mi_plan_position == -1:
    raise SystemExit(
        "Could not find the health Mi Plan task."
    )

facts_start = python_text.rfind(
    'facts = """',
    0,
    mi_plan_position,
)

if facts_start == -1:
    raise SystemExit(
        "Could not find the Mi Plan facts block."
    )

facts_end = python_text.find(
    '"""',
    facts_start + len('facts = """'),
)

if facts_end == -1:
    raise SystemExit(
        "Could not find the end of the Mi Plan facts block."
    )

mi_plan_rules = '''

Critical stage separation:

- The previous document-analysis message already explained LDL, APOE, glucose, kidney function and clinical limitations.
- Do not repeat the diagnostic summary.
- Do not thank Laura for sharing documents.
- Start directly with "# Mi Plan para Laura".
- Focus on concrete daily action.
- Include semaglutide and tirzepatide as topics to discuss with the doctor because BMI is approximately 31.
- Do not repeat the complete numbered doctor-question list.
- Refer back briefly to the questions prepared in the previous analysis.
- Do not sign with "Un abrazo", "eCoach" or similar.
'''

python_text = (
    python_text[:facts_end]
    + mi_plan_rules
    + python_text[facts_end:]
)

print("Strengthened Mi Plan stage separation.")


python_path.write_text(python_text, encoding="utf-8")
initial_skill_path.write_text(initial_text, encoding="utf-8")
health_skill_path.write_text(health_text, encoding="utf-8")

print()
print("Demo-text cleanup completed.")
