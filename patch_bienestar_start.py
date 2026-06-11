from pathlib import Path
import re
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_bienestar_start")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

replacement = r'''
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

Puedo ayudarte a:

- ordenar analíticas e informes de salud;
- preparar preguntas para el médico;
- entender qué está claro y qué necesita confirmación;
- crear un Mi Plan de hábitos;
- hacer seguimiento de ejercicio, alimentación, sueño y progreso;
- preparar mejor la próxima consulta.

Botones principales:

Quién soy
Ver tu contexto y situación de salud.

Qué quiero
Ver tus objetivos de bienestar físico.

Plan de acción
Ver tu Mi Plan y el siguiente paso concreto.

Seguimientos
Ver recordatorios y revisiones pendientes.

Guardar sesión
Revisar lo hablado y decidir qué guardar.

Para probar la demo, puedes escribir:

Me llamo Laura, tengo 48 años y vivo en Barcelona. He ido al médico porque quiero perder peso. En la analítica tengo el colesterol y el azúcar un poco elevados. La consulta duró quince minutos y no tengo un plan concreto. Tengo la analítica y una prueba genética. ¿Puedo subirlas?"""

    await message.reply_text(
        welcome,
        reply_markup=MAIN_KEYBOARD,
    )
'''

pattern = re.compile(
    r"(?ms)^async def start\(.*?"
    r"(?=^async def |^def |\Z)"
)

matches = list(pattern.finditer(text))

if len(matches) != 1:
    raise SystemExit(
        f"Expected exactly one start() function, found {len(matches)}."
    )

match = matches[0]

text = (
    text[:match.start()]
    + replacement.strip()
    + "\n\n"
    + text[match.end():]
)

path.write_text(text, encoding="utf-8")
print("Replaced /start with Bienestar Físico startup text.")
