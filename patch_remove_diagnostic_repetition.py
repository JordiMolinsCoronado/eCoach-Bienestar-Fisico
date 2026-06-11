from pathlib import Path
import shutil

python_path = Path("eCoach_Bienestar_Fisico.py")
initial_skill_path = Path("skills/initial_discovery.md")
health_skill_path = Path("skills/manage_physical_wellbeing.md")

python_text = python_path.read_text(encoding="utf-8")
initial_text = initial_skill_path.read_text(encoding="utf-8")
health_text = health_skill_path.read_text(encoding="utf-8")

shutil.copy2(
    python_path,
    python_path.with_suffix(".py.before_remove_diagnostic_repetition"),
)
shutil.copy2(
    initial_skill_path,
    initial_skill_path.with_suffix(".md.before_remove_diagnostic_repetition"),
)
shutil.copy2(
    health_skill_path,
    health_skill_path.with_suffix(".md.before_remove_diagnostic_repetition"),
)

print("Backups created.")


# ============================================================
# 1. REMOVE THE REDUNDANT SECOND UPLOAD MESSAGE FROM PYTHON
# ============================================================

redundant_fragments = [
    (
        "Antes de enviarlos, comprueba que has eliminado o tapado nombre, "
        "DNI/NIE, dirección, teléfono, email, número de historia clínica, "
        "códigos QR o de barras y firmas."
    ),
    (
        "Cuando hayas subido todos los documentos, te indicaré el siguiente paso."
    ),
]

for fragment in redundant_fragments:
    if fragment in python_text:
        python_text = python_text.replace(fragment, "")
        print(f"Removed Python text: {fragment[:55]}...")
    else:
        print(f"Python text not found: {fragment[:55]}...")


# Remove the whole hardcoded upload message when it now contains
# only the first sentence plus empty separators.

old_upload_block = '''    await update.message.reply_text(
        "Perfecto. Sube ahora la analítica y el informe genético usando el icono del clip de Telegram.\\n\\n"
        "\\n\\n"
        "",
        reply_markup=health_upload_keyboard(),
    )'''

new_upload_block = '''    await update.message.reply_text(
        "Sube la analítica y el informe genético usando el icono del clip de Telegram.",
        reply_markup=health_upload_keyboard(),
    )'''

if old_upload_block in python_text:
    python_text = python_text.replace(
        old_upload_block,
        new_upload_block,
        1,
    )
    print("Simplified the upload invitation.")
else:
    print(
        "Exact upload block not found. "
        "The generated text rules below will still prevent repetition."
    )


# ============================================================
# 2. STRENGTHEN INITIAL-DISCOVERY RULES
# ============================================================

initial_rules = r'''

## No repeated anonymisation instructions

After the first response has already told Laura which personal data to remove:

- do not repeat the list of identifiers;
- do not say "Antes de enviarlos, comprueba...";
- do not say "Cuando hayas subido todos los documentos...";
- do not repeat technical anonymisation instructions;
- do not provide a second privacy warning.

The following upload prompt should be only:

"Sube la analítica y el informe genético usando el icono del clip de Telegram."

If Laura explicitly asks how to anonymise a PDF, then explain it separately.
'''

marker = "## No repeated anonymisation instructions"

if marker in initial_text:
    initial_text = (
        initial_text.split(marker, 1)[0].rstrip()
        + "\n"
        + initial_rules
    )
else:
    initial_text = (
        initial_text.rstrip()
        + "\n"
        + initial_rules
    )

print("Added no-repetition rules to initial discovery.")


# ============================================================
# 3. FORBID LIFESTYLE ACTIONS IN THE DIAGNOSTIC AREA
# ============================================================

diagnostic_rules = r'''

## Diagnostic-stage content boundary

The document-analysis response must interpret the uploaded documents.

It must not give the daily lifestyle plan.

Do not include sections such as:

- "Oportunidades seguras para actuar mientras tanto";
- "Oportunidades de acción diaria";
- walking targets;
- five-, ten-, fifteen-, twenty- or thirty-minute movement targets;
- resistance-training frequency;
- exercise examples;
- protein recommendations;
- fibre recommendations;
- food substitutions;
- reducing sugary drinks or processed foods;
- sleep-duration targets;
- screen routines;
- hydration targets;
- weighing frequency;
- waist tracking;
- motivational adherence instructions.

All of those belong exclusively in Mi Plan.

The diagnostic response should contain only:

1. Documents reviewed and their limitations.
2. Concise results summary.
3. What the results may mean and what requires medical interpretation.
4. Questions to take to the doctor, including semaglutide and tirzepatide.
5. A brief transition to the Crear Mi Plan button.

End with:

"El siguiente paso es convertir esta información en un plan diario concreto."
'''

marker = "## Diagnostic-stage content boundary"

if marker in health_text:
    health_text = (
        health_text.split(marker, 1)[0].rstrip()
        + "\n"
        + diagnostic_rules
    )
else:
    health_text = (
        health_text.rstrip()
        + "\n"
        + diagnostic_rules
    )

print("Added strict diagnostic-stage boundary.")


# ============================================================
# 4. ADD THE SAME RULE DIRECTLY TO THE ANALYSIS PROMPT
# ============================================================

analysis_anchor = '''Do not include:
- walking targets;
- resistance-training plans;
- protein/fibre plans;
- sleep routines;
- hydration;
- weight-tracking routines;
- adherence coaching.'''

analysis_replacement = '''Do not include:
- any section called "Oportunidades seguras para actuar mientras tanto";
- any section called "Oportunidades de acción diaria";
- walking or movement targets;
- resistance-training plans or exercise examples;
- protein or fibre plans;
- nutrition rules or food substitutions;
- sleep routines or sleep-duration targets;
- hydration;
- weight or waist tracking;
- adherence coaching.

All lifestyle and behaviour-change recommendations belong only in Mi Plan.'''

if analysis_anchor in python_text:
    python_text = python_text.replace(
        analysis_anchor,
        analysis_replacement,
        1,
    )
    print("Strengthened the health-analysis prompt.")
elif analysis_replacement in python_text:
    print("Health-analysis prompt already strengthened.")
else:
    print(
        "Exact analysis-prompt anchor not found. "
        "The skill boundary will still apply."
    )


# ============================================================
# 5. PREVENT THESE PHRASES IN GENERATED ANALYSIS
# ============================================================

phrase_anchor = '''Do not thank Laura for sharing the documents.
Do not sign the answer.
Do not say "Un abrazo".
Do not ask her to type a choice.'''

phrase_replacement = '''Do not thank Laura for sharing the documents.
Do not sign the answer.
Do not say "Un abrazo".
Do not ask her to type a choice.
Do not say "Mientras tanto, puedes empezar...".
Do not offer exercise, food, sleep, hydration or weight-tracking actions in this stage.'''

if phrase_anchor in python_text:
    python_text = python_text.replace(
        phrase_anchor,
        phrase_replacement,
        1,
    )
    print("Added explicit diagnostic phrase restrictions.")
elif phrase_replacement in python_text:
    print("Diagnostic phrase restrictions already present.")
else:
    print("Diagnostic phrase anchor not found.")


python_path.write_text(python_text, encoding="utf-8")
initial_skill_path.write_text(initial_text, encoding="utf-8")
health_skill_path.write_text(health_text, encoding="utf-8")

print()
print("Diagnostic repetition and misplaced lifestyle content removed.")
