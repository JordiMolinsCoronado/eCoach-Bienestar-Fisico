import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

load_dotenv()

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

# Default prices for gemini-2.5-flash-lite.
# Change these in .env if you switch model.
GEMINI_INPUT_PRICE_PER_1M = float(os.getenv("GEMINI_INPUT_PRICE_PER_1M", "0.10"))
GEMINI_OUTPUT_PRICE_PER_1M = float(os.getenv("GEMINI_OUTPUT_PRICE_PER_1M", "0.40"))

PROMPTS_DIR = Path("prompts")
WEALTH_KNOWLEDGE_DIR = Path("Wealth_Knowledge")
CLIENT_WIKI_FILE = Path("Client_Wiki.md")
WEALTH_LOG_FILE = Path("Wealth_Guide_Logs.md")

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["Â¿QuiÃ©n soy yo?"],
        ["Â¿QuÃ© quiero?"],
        ["Ver mi resumen"],
    ],
    resize_keyboard=True,
    is_persistent=True,
)

WHO_AM_I, WHAT_DO_I_WANT = range(2)


# ---------------------------------------------------------------------
# File loading helpers
# ---------------------------------------------------------------------

def load_prompt(*names: str) -> str:
    """
    Load one or more Markdown prompt files from the prompts folder.
    Missing files are ignored so the bot can run during early development.
    """
    parts: list[str] = []

    for name in names:
        path = PROMPTS_DIR / name
        if path.exists():
            parts.append(path.read_text(encoding="utf-8").strip())

    return "\n\n---\n\n".join(part for part in parts if part)


def load_wealth_knowledge() -> str:
    """
    Load all Markdown files from the Wealth_Knowledge folder.
    This is the simple local-knowledge version: no embeddings, no database.
    """
    if not WEALTH_KNOWLEDGE_DIR.exists():
        return ""

    parts: list[str] = []

    for path in sorted(WEALTH_KNOWLEDGE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8").strip()
        if content:
            parts.append(f"# Archivo fuente: {path.name}\n\n{content}")

    return "\n\n---\n\n".join(parts)


def load_client_wiki() -> str:
    """
    Load the current client wiki if it exists.
    """
    if not CLIENT_WIKI_FILE.exists():
        return ""

    return CLIENT_WIKI_FILE.read_text(encoding="utf-8").strip()


def save_client_wiki(markdown_text: str) -> None:
    """
    Save the client wiki as Markdown.
    """
    CLIENT_WIKI_FILE.write_text(markdown_text.strip() + "\n", encoding="utf-8")


def save_wealth_log(user_input: str, ai_answer: str, usage: dict) -> None:
    """
    Save Wealth Guide conversations for traceability.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"""
## {timestamp}

### Pregunta / entrada del usuario

{user_input}

### Modelo

{usage.get("model", GEMINI_MODEL)}

### Tokens

- Input tokens: {usage.get("input_tokens", 0)}
- Output tokens: {usage.get("output_tokens", 0)}
- Total tokens: {usage.get("total_tokens", 0)}
- Estimated cost USD: {usage.get("estimated_cost_usd", 0):.6f}

### Respuesta

{ai_answer}

---
"""

    with WEALTH_LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(entry)


# ---------------------------------------------------------------------
# Gemini helper
# ---------------------------------------------------------------------

def gemini_llm(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """
    Send a prompt to Gemini and return:
    - answer text
    - usage/cost metadata
    """
    if gemini_client is None:
        raise RuntimeError("Gemini no estÃ¡ configurado. Revisa GEMINI_API_KEY en .env.")

    config = None
    if system_prompt:
        config = types.GenerateContentConfig(system_instruction=system_prompt)

    response = gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config,
    )

    usage = getattr(response, "usage_metadata", None)

    input_tokens = getattr(usage, "prompt_token_count", 0) if usage else 0
    output_tokens = getattr(usage, "candidates_token_count", 0) if usage else 0
    total_tokens = getattr(usage, "total_token_count", 0) if usage else 0

    estimated_cost_usd = (
        (input_tokens / 1_000_000) * GEMINI_INPUT_PRICE_PER_1M
        + (output_tokens / 1_000_000) * GEMINI_OUTPUT_PRICE_PER_1M
    )

    metadata = {
        "model": GEMINI_MODEL,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "estimated_cost_usd": estimated_cost_usd,
    }

    return response.text or "", metadata


def format_gemini_usage_note(usage: dict) -> str:
    """
    Small cost note appended to Telegram answers.
    """
    return (
        "\n\n---\n"
        "EstimaciÃ³n de uso Gemini:\n"
        f"Modelo: {usage['model']}\n"
        f"Input tokens: {usage['input_tokens']}\n"
        f"Output tokens: {usage['output_tokens']}\n"
        f"Total tokens: {usage['total_tokens']}\n"
        f"Coste estimado: ${usage['estimated_cost_usd']:.6f}"
    )


async def send_long_message(
    update: Update,
    text: str,
    reply_markup=None,
    chunk_size: int = 3500,
) -> None:
    """
    Send long Telegram messages in safe chunks.
    """
    if not text:
        await update.message.reply_text("Respuesta vacÃ­a.", reply_markup=reply_markup)
        return

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    for index, chunk in enumerate(chunks):
        if index == len(chunks) - 1:
            await update.message.reply_text(chunk, reply_markup=reply_markup)
        else:
            await update.message.reply_text(chunk)


# ---------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------

def build_system_prompt() -> str:
    """
    Build the shared system prompt for the wealth copilot.
    """
    base_prompts = load_prompt("base_rules.md", "wealth_policy.md")
    extra_rules = """
Eres un copiloto patrimonial independiente.

Idioma:
- Responde siempre en castellano.
- Usa un tono claro, sereno, humano y prÃ¡ctico.

Postura:
- No vendes productos.
- No recomiendas inversiones concretas.
- No dices "compra", "vende", "mantÃ©n" ni "esto es adecuado para ti".
- Ayudas al cliente a entenderse, ordenar su situaciÃ³n, comparar opciones del mercado y formular mejores preguntas.
- La decisiÃ³n final siempre la toma el cliente o un asesor humano regulado.

Estilo:
- SÃ© estructurado.
- SÃ© concreto.
- Haz preguntas Ãºtiles.
- Distingue hechos, hipÃ³tesis y datos pendientes.
- Termina con una acciÃ³n pequeÃ±a y clara cuando sea Ãºtil.
"""
    return "\n\n---\n\n".join(part for part in [base_prompts, extra_rules.strip()] if part)


def build_who_am_i_prompt(user_notes: str, existing_wiki: str) -> str:
    """
    Prompt for creating or updating the client wiki.
    """
    return f"""
Tu tarea es crear o actualizar un texto vivo titulado "Â¿QuiÃ©n soy yo?".

Este texto debe servir como wiki personal patrimonial del cliente.
Debe ser editable por el cliente.
No debe sonar como un informe frÃ­o, sino como un espejo claro de su situaciÃ³n.

Reglas:
- Devuelve SOLO el Markdown completo actualizado.
- No des recomendaciones de inversiÃ³n.
- No inventes datos.
- Si falta informaciÃ³n, escribe "Pendiente de aclarar".
- Conserva la informaciÃ³n Ãºtil del resumen anterior.
- Integra las nuevas notas del usuario.
- Escribe en primera persona cuando tenga sentido, como si el cliente pudiera revisar y modificar el texto.

Estructura obligatoria:

# Â¿QuiÃ©n soy yo?

## 1. Mi situaciÃ³n actual
- Edad:
- Residencia:
- Residencia fiscal:
- Familia y dependientes:
- Trabajo o actividad:
- Origen del relaciones:

## 2. Mi situaciÃ³n financiera
- Efectivo:
- Inversiones:
- Inmuebles:
- Empresa o participaciones:
- Deudas:
- Ingresos:
- Obligaciones relevantes:

## 3. Mi experiencia con el dinero y la inversiÃ³n
- QuÃ© he hecho hasta ahora:
- QuÃ© entiendo:
- QuÃ© no entiendo todavÃ­a:
- QuÃ© me genera inseguridad:

## 4. Mi relaciÃ³n con el riesgo
- QuÃ© significa para mÃ­ asumir riesgo:
- PÃ©rdida temporal que podrÃ­a tolerar:
- PÃ©rdida temporal que me harÃ­a sufrir o actuar mal:
- Diferencia entre mi capacidad real de pÃ©rdida y mi tolerancia emocional:

## 5. Mis necesidades de liquidez
- Dinero que puedo necesitar en 12 meses:
- Dinero que puedo necesitar en 2â€“5 aÃ±os:
- Dinero que puedo dejar trabajar mÃ¡s de 5 aÃ±os:

## 6. Mis preferencias y restricciones
- Simplicidad:
- Bajos costes:
- Fiscalidad y reporting en EspaÃ±a:
- Sostenibilidad / ESG:
- Liquidez:
- GestiÃ³n delegada o autÃ³noma:
- Productos o enfoques que quiero evitar:

## 7. Mis entidades, plataformas o asesores actuales
- Bancos:
- Brokers:
- Asesores:
- Productos actuales:

## 8. Lo que todavÃ­a no sÃ©
- Preguntas abiertas:
- Documentos pendientes:
- Decisiones pendientes:

## 9. PrÃ³xima acciÃ³n pequeÃ±a
- AcciÃ³n:

Resumen anterior:
{existing_wiki if existing_wiki else "No existe todavÃ­a un resumen anterior."}

Nuevas notas del usuario:
{user_notes}
"""


def build_what_do_i_want_prompt(question: str, client_wiki: str, wealth_knowledge: str) -> str:
    """
    Prompt for the main guided wealth conversation.
    """
    return f"""
Tu tarea es responder a una pregunta patrimonial del cliente.

Objetivo del modo "Â¿QuÃ© quiero?":
Ayudar al cliente a aclarar quÃ© quiere conseguir con su dinero, quÃ© opciones existen en el mercado, quÃ© criterios debe comparar y quÃ© preguntas debe responder antes de decidir.

Reglas duras:
- No recomiendes una inversiÃ³n concreta.
- No elijas una plataforma, banco, fondo, ETF, producto o cartera por el cliente.
- No digas "la mejor opciÃ³n es...".
- No digas "deberÃ­as comprar/vender/mantener".
- Puedes explicar categorÃ­as del mercado, criterios de comparaciÃ³n, riesgos, costes, fiscalidad, liquidez y preguntas relevantes.
- Puedes decir "opciones a comparar", no "opciÃ³n recomendada".
- Puedes ayudarle a prepararse para hablar con bancos, plataformas o asesores.
- Si falta informaciÃ³n del perfil del cliente, dilo.
- Si la pregunta depende de datos actuales del mercado y no los tienes, dilo y formula quÃ© habrÃ­a que comprobar.

Usa esta estructura, salvo que la pregunta pida algo muy breve:

1. Respuesta directa
2. QuÃ© revela esto sobre lo que quieres
3. Opciones del mercado a comparar
4. Criterios de decisiÃ³n
5. Riesgos y advertencias
6. InformaciÃ³n que falta
7. Preguntas que deberÃ­as hacer
8. PrÃ³xima acciÃ³n pequeÃ±a
9. Recordatorio: esto no es una recomendaciÃ³n

Perfil vivo del cliente:
{client_wiki if client_wiki else "TodavÃ­a no existe un perfil vivo. Pide primero los datos esenciales del cliente."}

Conocimiento local patrimonial:
{wealth_knowledge if wealth_knowledge else "No hay conocimiento local disponible."}

Pregunta del cliente:
{question}
"""


# ---------------------------------------------------------------------
# Telegram handlers
# ---------------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Soy tu copiloto patrimonial. Elige una opciÃ³n:",
        reply_markup=MAIN_KEYBOARD,
    )


async def who_am_i_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "CuÃ©ntame tu situaciÃ³n o pega notas del cliente. ActualizarÃ© el texto Â«Â¿QuiÃ©n soy yo?Â»."
    )
    return WHO_AM_I


async def what_do_i_want_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hazme una pregunta patrimonial o dime quÃ© decisiÃ³n quieres aclarar."
    )
    return WHAT_DO_I_WANT


async def who_am_i_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_notes = update.message.text.strip()

    if not user_notes:
        await update.message.reply_text("No he recibido notas. Prueba de nuevo.")
        return WHO_AM_I

    await update.message.reply_text("Actualizando Â«Â¿QuiÃ©n soy yo?Â»...")

    try:
        existing_wiki = load_client_wiki()
        prompt = build_who_am_i_prompt(user_notes=user_notes, existing_wiki=existing_wiki)
        answer, usage = gemini_llm(prompt, system_prompt=build_system_prompt())

        save_client_wiki(answer)

        await send_long_message(
            update,
            answer + format_gemini_usage_note(usage),
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as error:
        await update.message.reply_text(
            f"Error al actualizar Â«Â¿QuiÃ©n soy yo?Â»: {error}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END


async def what_do_i_want_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text.strip()

    if not question:
        await update.message.reply_text("No he recibido una pregunta. Prueba de nuevo.")
        return WHAT_DO_I_WANT

    await update.message.reply_text("Pensando con Gemini...")

    try:
        client_wiki = load_client_wiki()
        wealth_knowledge = load_wealth_knowledge()
        prompt = build_what_do_i_want_prompt(
            question=question,
            client_wiki=client_wiki,
            wealth_knowledge=wealth_knowledge,
        )

        answer, usage = gemini_llm(prompt, system_prompt=build_system_prompt())
        save_wealth_log(question, answer, usage)

        await send_long_message(
            update,
            answer + format_gemini_usage_note(usage),
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as error:
        await update.message.reply_text(
            f"Error en Â«Â¿QuÃ© quiero?Â»: {error}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END


async def show_summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    client_wiki = load_client_wiki()

    if not client_wiki:
        await update.message.reply_text(
            "TodavÃ­a no existe un resumen. Pulsa Â«Â¿QuiÃ©n soy yo?Â» y pega las notas del cliente.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    await send_long_message(
        update,
        client_wiki,
        reply_markup=MAIN_KEYBOARD,
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cancelado.",
        reply_markup=MAIN_KEYBOARD,
    )
    return ConversationHandler.END


# ---------------------------------------------------------------------
# App
# ---------------------------------------------------------------------

app = ApplicationBuilder().token(TOKEN).build()

conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex(r"^Â¿QuiÃ©n soy yo\?$"), who_am_i_start),
        MessageHandler(filters.Regex(r"^Â¿QuÃ© quiero\?$"), what_do_i_want_start),
    ],
    states={
        WHO_AM_I: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, who_am_i_message)
        ],
        WHAT_DO_I_WANT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, what_do_i_want_message)
        ],
    },
    fallbacks=[
        CommandHandler("cancel", cancel)
    ],
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cancel", cancel))
app.add_handler(conversation_handler)
app.add_handler(MessageHandler(filters.Regex(r"^Ver mi resumen$"), show_summary))

# Any other text gently redirects to the product flow instead of silently capturing it.
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        lambda update, context: update.message.reply_text(
            "Elige Â«Â¿QuiÃ©n soy yo?Â» para actualizar tu perfil o Â«Â¿QuÃ© quiero?Â» para hacer una pregunta patrimonial.",
            reply_markup=MAIN_KEYBOARD,
        ),
    )
)

app.run_polling()

