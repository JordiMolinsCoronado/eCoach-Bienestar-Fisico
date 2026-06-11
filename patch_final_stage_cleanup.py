from pathlib import Path
import shutil

python_path = Path("eCoach_Bienestar_Fisico.py")
skill_path = Path("skills/manage_physical_wellbeing.md")

python_text = python_path.read_text(encoding="utf-8")
skill_text = skill_path.read_text(encoding="utf-8")

shutil.copy2(
    python_path,
    python_path.with_suffix(".py.before_stage_cleanup_and_wearable"),
)
shutil.copy2(
    skill_path,
    skill_path.with_suffix(".md.before_stage_cleanup_and_wearable"),
)

print("Backups created.")


# ============================================================
# 1. ADD DETERMINISTIC OUTPUT CLEANERS
# ============================================================

cleaners = r'''
def clean_health_diagnostic_answer(answer: str) -> str:
    """
    Keep document analysis separate from Mi Plan.

    Doctor questions and lifestyle actions belong to Mi Plan.
    """
    import re

    text = (answer or "").strip()

    forbidden_section_patterns = [
        r"(?ims)^\s*\*{0,2}Preguntas para llevar al médico\*{0,2}\s*$.*?(?=^\s*\*{0,2}(?:Próximo paso|El siguiente paso|Siguiente paso)\*{0,2}\s*$|\Z)",
        r"(?ims)^\s*#{1,6}\s*Preguntas para llevar al médico\s*$.*?(?=^\s*#{1,6}\s|\Z)",
        r"(?ims)^\s*\*{0,2}Oportunidades seguras para actuar mientras tanto\*{0,2}\s*$.*?(?=^\s*\*{0,2}.+?\*{0,2}\s*$|\Z)",
        r"(?ims)^\s*\*{0,2}Oportunidades de acción diaria.*?\*{0,2}\s*$.*?(?=^\s*\*{0,2}.+?\*{0,2}\s*$|\Z)",
    ]

    for pattern in forbidden_section_patterns:
        text = re.sub(pattern, "", text)

    # Remove isolated lifestyle paragraphs that occasionally leak through.
    text = re.sub(
        r"(?ims)^\s*(?:Mientras tanto|Mientras llega la cita),?\s+puedes.*?(?=^\s*\*{0,2}.+?\*{0,2}\s*$|\Z)",
        "",
        text,
    )

    # Remove signatures.
    text = re.sub(
        r"(?im)^\s*(?:—|-)\s*eCoach(?: Bienestar Físico)?\s*$",
        "",
        text,
    )
    text = re.sub(r"(?im)^\s*Un abrazo[,.]?\s*$", "", text)

    # Replace any verbose transition with one fixed ending.
    text = re.sub(
        r"(?ims)^\s*\*{0,2}(?:Próximo paso|El siguiente paso)\*{0,2}.*$",
        "",
        text,
    )

    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    return (
        text
        + "\n\n"
        + "El siguiente paso es convertir esta información en un plan diario concreto."
    )


def clean_health_mi_plan_answer(answer: str) -> str:
    """Remove signatures and duplicated diagnostic material from Mi Plan."""
    import re

    text = (answer or "").strip()

    # Remove common signatures.
    text = re.sub(
        r"(?im)^\s*(?:—|-)\s*eCoach(?: Bienestar Físico)?\s*$",
        "",
        text,
    )
    text = re.sub(r"(?im)^\s*Un abrazo[,.]?\s*$", "", text)
    text = re.sub(r"(?im)^\s*Con calidez[,.]?\s*$", "", text)

    # Remove unnecessary introductory thanks.
    text = re.sub(
        r"(?im)^\s*Hola,?\s+Laura\.?\s*$",
        "",
        text,
    )
    text = re.sub(
        r"(?im)^\s*Gracias por compartir tus documentos\.?\s*$",
        "",
        text,
    )
    text = re.sub(
        r"(?im)^\s*Gracias por compartir.*?\.\s*$",
        "",
        text,
    )

    # Remove duplicated diagnostic preamble before section 1.
    text = re.sub(
        r"(?ims)(# Mi Plan para Laura\s*).*?(?=^##\s*1\.)",
        r"\1\n\n",
        text,
    )

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text
'''

if "def clean_health_diagnostic_answer(" not in python_text:
    marker = "\ndef generate_health_document_analysis("

    if marker not in python_text:
        raise SystemExit(
            "Could not find generate_health_document_analysis insertion point."
        )

    python_text = python_text.replace(
        marker,
        "\n" + cleaners.strip() + "\n\n" + marker.lstrip("\n"),
        1,
    )

    print("Inserted deterministic health-output cleaners.")
else:
    print("Health-output cleaners already exist.")


# ============================================================
# 2. CLEAN THE DOCUMENT ANALYSIS BEFORE IT IS RETURNED
# ============================================================

analysis_start = python_text.find(
    "def generate_health_document_analysis("
)

if analysis_start == -1:
    raise SystemExit("generate_health_document_analysis not found.")

analysis_end_candidates = [
    python_text.find("\ndef ", analysis_start + 10),
    python_text.find("\nasync def ", analysis_start + 10),
]

analysis_end_candidates = [
    value for value in analysis_end_candidates if value != -1
]

analysis_end = min(analysis_end_candidates) if analysis_end_candidates else len(python_text)
analysis_block = python_text[analysis_start:analysis_end]

if "clean_health_diagnostic_answer" not in analysis_block:
    replacements = [
        (
            "    return answer\n",
            "    return clean_health_diagnostic_answer(answer)\n",
        ),
        (
            "    return response\n",
            "    return clean_health_diagnostic_answer(response)\n",
        ),
        (
            "    return result\n",
            "    return clean_health_diagnostic_answer(result)\n",
        ),
    ]

    replaced = False

    for old, new in replacements:
        if old in analysis_block:
            analysis_block = analysis_block.replace(old, new, 1)
            replaced = True
            break

    if not replaced:
        raise SystemExit(
            "Could not find the final return variable inside "
            "generate_health_document_analysis."
        )

    python_text = (
        python_text[:analysis_start]
        + analysis_block
        + python_text[analysis_end:]
    )

    print("Document analysis now uses deterministic cleanup.")
else:
    print("Document analysis cleanup already active.")


# ============================================================
# 3. CLEAN MI PLAN INSIDE answer_callback_with_skill
# ============================================================

callback_start = python_text.find(
    "async def answer_callback_with_skill("
)

if callback_start == -1:
    raise SystemExit("answer_callback_with_skill not found.")

callback_end_candidates = [
    python_text.find("\nasync def ", callback_start + 10),
    python_text.find("\ndef ", callback_start + 10),
]

callback_end_candidates = [
    value for value in callback_end_candidates if value != -1
]

callback_end = min(callback_end_candidates) if callback_end_candidates else len(python_text)
callback_block = python_text[callback_start:callback_end]

cleanup_code = '''
    if (
        skill_name == "manage_physical_wellbeing"
        and "Create Laura's practical Mi Plan" in task
    ):
        answer = clean_health_mi_plan_answer(answer)
'''

if "clean_health_mi_plan_answer(answer)" not in callback_block:
    send_markers = [
        "    await reply_message_text_in_chunks(",
        "    await query.message.reply_text(answer",
    ]

    send_position = -1

    for marker in send_markers:
        send_position = callback_block.find(marker)
        if send_position != -1:
            break

    if send_position == -1:
        raise SystemExit(
            "Could not find the answer-send point in answer_callback_with_skill."
        )

    callback_block = (
        callback_block[:send_position]
        + cleanup_code
        + "\n"
        + callback_block[send_position:]
    )

    python_text = (
        python_text[:callback_start]
        + callback_block
        + python_text[callback_end:]
    )

    print("Mi Plan now uses deterministic cleanup.")
else:
    print("Mi Plan cleanup already active.")


# ============================================================
# 4. MOVE ALL DOCTOR QUESTIONS TO MI PLAN IN THE SKILL
# ============================================================

skill_rules = r'''

## Final stage separation — mandatory

### Document analysis

The diagnostic response must contain only:

- documents reviewed and their limitations;
- concise laboratory and genetic results;
- interpretation boundaries;
- what requires medical assessment;
- a transition to Crear Mi Plan.

The diagnostic response must not contain:

- a section called "Preguntas para llevar al médico";
- numbered questions for the doctor;
- semaglutide or tirzepatide questions;
- exercise recommendations;
- nutrition recommendations;
- sleep recommendations;
- hydration recommendations;
- weight-tracking recommendations.

### Mi Plan

Mi Plan must contain the doctor-preparation questions.

Include a section:

## Preguntas para llevar al médico

1. ¿El resultado APOE ε3/ε4 necesita confirmación clínica?
2. ¿Cómo valora mi riesgo cardiovascular global y qué objetivo personal de LDL sería adecuado?
3. ¿Sería útil medir ApoB, Lp(a), HbA1c o revisar la tensión arterial?
4. ¿Conviene hacer seguimiento de creatinina, eGFR y urea?
5. ¿La menopausia o transición menopáusica cambia algo en mi valoración?
6. Con 1,65 m, 84,4 kg y un IMC aproximado de 31, ¿soy candidata a semaglutida o tirzepatida?
7. ¿Qué opción tendría más sentido en mi caso, qué beneficio sería realista y qué contraindicaciones o efectos adversos debemos revisar?
8. ¿Cómo protegeríamos la masa muscular y la fuerza durante la pérdida de peso?
9. ¿Qué seguimiento necesitaría y sería probablemente un tratamiento prolongado?

Mi Plan must not end with:

- "— eCoach Bienestar Físico";
- "eCoach";
- "Un abrazo";
- "Con calidez";
- any signature.
'''

marker = "## Final stage separation — mandatory"

if marker in skill_text:
    skill_text = (
        skill_text.split(marker, 1)[0].rstrip()
        + "\n"
        + skill_rules
    )
else:
    skill_text = skill_text.rstrip() + "\n" + skill_rules

print("Moved all doctor questions to Mi Plan rules.")


python_path.write_text(python_text, encoding="utf-8")
skill_path.write_text(skill_text, encoding="utf-8")

print()
print("Stage cleanup patch completed.")
