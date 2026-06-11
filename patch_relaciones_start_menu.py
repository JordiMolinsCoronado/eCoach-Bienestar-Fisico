from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------
# 1) Replace MAIN_KEYBOARD with relationship-safe labels, no emojis
# ---------------------------------------------------------------------

main_keyboard_re = r'MAIN_KEYBOARD\s*=\s*ReplyKeyboardMarkup\(\s*\[.*?\]\s*,\s*resize_keyboard=True\s*\)'
main_keyboard_new = '''MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["Quien soy", "Que quiero"],
        ["Plan de accion", "Seguimientos"],
        ["Guardar sesion"],
    ],
    resize_keyboard=True,
)'''

text, count = re.subn(main_keyboard_re, main_keyboard_new, text, count=1, flags=re.S)
print("MAIN_KEYBOARD replacements:", count)

# ---------------------------------------------------------------------
# 2) Replace old menu regex labels with no-emoji relationship labels
# ---------------------------------------------------------------------

regex_replacements = {
    r'app\.add_handler\(MessageHandler\(filters\.Regex\(r"\^👤 Quién soy\$"\),\s*show_quien_soy\)\)': 'app.add_handler(MessageHandler(filters.Regex(r"^Quien soy$"), show_quien_soy))',
    r'app\.add_handler\(MessageHandler\(filters\.Regex\(r"\^🎯 Qué quiero\$"\),\s*show_que_quiero\)\)': 'app.add_handler(MessageHandler(filters.Regex(r"^Que quiero$"), show_que_quiero))',
    r'app\.add_handler\(MessageHandler\(filters\.Regex\(r"\^✅ Plan de acción\$"\),\s*show_que_tengo_que_hacer\)\)': 'app.add_handler(MessageHandler(filters.Regex(r"^Plan de accion$"), show_que_tengo_que_hacer))',
    r'app\.add_handler\(MessageHandler\(filters\.Regex\(r"\^⏰ Seguimientos\$"\),\s*show_followups\)\)': 'app.add_handler(MessageHandler(filters.Regex(r"^Seguimientos$"), show_followups))',
    r'app\.add_handler\(MessageHandler\(filters\.Regex\(r"\^💾 Guardar sesión\$"\),\s*show_session_buffer_status\)\)': 'app.add_handler(MessageHandler(filters.Regex(r"^Guardar sesion$"), show_session_buffer_status))',
}

for pattern, replacement in regex_replacements.items():
    text, n = re.subn(pattern, replacement, text)
    if n:
        print("Updated regex:", replacement)

# ---------------------------------------------------------------------
# 3) Replace /start function with relationship-specific welcome
# ---------------------------------------------------------------------

start_re = r'\nasync def start\(update: Update, context: ContextTypes\.DEFAULT_TYPE\) -> None:\n.*?(?=\nasync def |\ndef )'

start_new = r'''
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome = """Hola. Soy eCoach Relaciones.

Puedo ayudarte a practicar agencia relacional entre sesiones de terapia.

No sustituyo a tu psicologa.
No decido por ti.
Te ayudo a pausar, separar hechos de historias, recordar tus valores y elegir el siguiente paso con mas claridad.

Idea central:

No persecucion ansiosa.
No juicio delegado.
Agencia relacional guiada.

Botones principales:

Quien soy
Ver el resumen de tu situacion y patron relacional.

Que quiero
Ver tus valores, criterios y objetivo relacional actual.

Plan de accion
Ver tu Mi Plan y el siguiente paso claro.

Seguimientos
Ver recordatorios y check-ins pendientes.

Guardar sesion
Revisar lo hablado y decidir que guardar.

Para probar la demo, puedes escribir:

Estoy saliendo con un hombre que me gusta.
Cuando estamos juntos, todo parece bien.
Pero entre citas es muy ambiguo.
A veces escribe con carino, pero otras desaparece.
Mi psicologa me dice que no persiga y que observe si hay coherencia, pero cuando me activo se me olvida todo.
"""
    await update.message.reply_text(welcome, reply_markup=MAIN_KEYBOARD)
'''

text, count = re.subn(start_re, "\n" + start_new.strip() + "\n", text, count=1, flags=re.S)
print("start() replacements:", count)

# ---------------------------------------------------------------------
# 4) Replace obvious Patrimonio wording in app texts embedded in code
# ---------------------------------------------------------------------

text = text.replace("copiloto patrimonial", "copiloto relacional")
text = text.replace("perfil patrimonial", "perfil relacional")
text = text.replace("decisiones financieras", "decisiones relacionales")
text = text.replace("perfil patrimonial resumido", "perfil relacional resumido")
text = text.replace("tus objetivos y criterios", "tus valores y criterios relacionales")
text = text.replace("tus próximas acciones", "tus proximas acciones")
text = text.replace("tus prÃ³ximas acciones", "tus proximas acciones")

path.write_text(text, encoding="utf-8")
print("Patched Relaciones start/menu text.")
