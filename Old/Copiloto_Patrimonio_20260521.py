import os
import json
import re
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types, errors
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
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
GEMINI_INPUT_PRICE_PER_1M = float(os.getenv("GEMINI_INPUT_PRICE_PER_1M", "0.10"))
GEMINI_OUTPUT_PRICE_PER_1M = float(os.getenv("GEMINI_OUTPUT_PRICE_PER_1M", "0.40"))

PROMPTS_DIR = Path("prompts")
WEALTH_KNOWLEDGE_DIR = Path("Wealth_Knowledge")

CLIENTS_DIR = Path("ClientData")
ACTIVE_CLIENT_NAME = os.getenv("ACTIVE_CLIENT_NAME", "Cliente1")
ACTIVE_CLIENT_DIR = CLIENTS_DIR / ACTIVE_CLIENT_NAME

CLIENT_FILES = {
    "quien_soy": ACTIVE_CLIENT_DIR / "quien_soy.md",
    "que_quiero": ACTIVE_CLIENT_DIR / "que_quiero.md",
    "que_tengo_que_hacer": ACTIVE_CLIENT_DIR / "que_tengo_que_hacer.md",
    "estilo_respuesta": ACTIVE_CLIENT_DIR / "estilo_respuesta.md",
    "configuracion_privacidad": ACTIVE_CLIENT_DIR / "configuracion_privacidad.md",
    "historial_interacciones": ACTIVE_CLIENT_DIR / "historial_interacciones.md",
    "privacidad_log": ACTIVE_CLIENT_DIR / "privacidad_log.md",
}

WEALTH_LOG_FILE = ACTIVE_CLIENT_DIR / "wealth_logs.md"

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["ðŸ‘¤ Resumen de quiÃ©n soy yo"],
        ["ðŸŽ¯ Resumen de quÃ© quiero"],
        ["ðŸ§­ Resumen de quÃ© tengo que hacer"],
    ],
    resize_keyboard=True,
    is_persistent=True,
)


# ---------------------------------------------------------------------
# Initial client files
# ---------------------------------------------------------------------

INITIAL_CLIENT_FILES = {
    "quien_soy": """# Resumen de quiÃ©n soy yo

Este archivo recoge lo que sabemos del cliente: su situaciÃ³n personal, fiscal, profesional, patrimonial, experiencia inversora, relaciÃ³n con el riesgo, restricciones y preguntas abiertas.

## SituaciÃ³n personal y fiscal

Pendiente.

## SituaciÃ³n profesional

Pendiente.

## Origen del relaciones

Pendiente.

## SituaciÃ³n financiera actual

Pendiente.

## Experiencia con el dinero y la inversiÃ³n

Pendiente.

## RelaciÃ³n con el riesgo

Pendiente.

## Restricciones importantes

Pendiente.

## Preguntas abiertas sobre quiÃ©n es el cliente

Pendiente.
""",
    "que_quiero": """# Resumen de quÃ© quiero

Este archivo recoge lo que el cliente quiere conseguir con su relaciones: objetivos, prioridades, horizonte temporal, necesidades de liquidez, preferencias y decisiones que quiere preparar.

## Objetivos principales

Pendiente.

## Objetivos secundarios

Pendiente.

## Horizonte temporal

Pendiente.

## Necesidades de liquidez

Pendiente.

## Preferencias y restricciones

Pendiente.

## Preguntas abiertas sobre lo que quiere

Pendiente.
""",
    "que_tengo_que_hacer": """# Resumen de quÃ© tengo que hacer para conseguir lo que quiero

Este archivo recoge el mapa de acciÃ³n del cliente: informaciÃ³n pendiente, documentos necesarios, opciones a comparar, preguntas a bancos o asesores, riesgos a entender y prÃ³xima acciÃ³n.

## InformaciÃ³n que falta

Pendiente.

## Documentos necesarios

Pendiente.

## Opciones que conviene comparar

Pendiente.

## Preguntas que debe hacer a bancos, asesores o plataformas

Pendiente.

## Riesgos que debe entender antes de decidir

Pendiente.

## PrÃ³xima acciÃ³n concreta

Pendiente.
""",
    "estilo_respuesta": """# Estilo de respuesta para este cliente

El asistente debe escribir en castellano claro, sobrio y elegante.

Debe actuar como un guÃ­a independiente de clarificaciÃ³n patrimonial.

No debe vender productos.
No debe recomendar inversiones concretas.
No debe decidir por el cliente.

Debe ayudar al cliente a:
- entender su situaciÃ³n;
- aclarar lo que quiere;
- comparar opciones disponibles en el mercado;
- formular mejores preguntas;
- detectar riesgos, costes y conflictos de interÃ©s;
- preparar una decisiÃ³n informada.

Tono:
- claro;
- tranquilo;
- respetuoso;
- no paternalista;
- prÃ¡ctico;
- independiente;
- orientado a preguntas y criterios de decisiÃ³n.

Formato preferido:
- frases cortas;
- secciones claras;
- listas cuando ayuden;
- una prÃ³xima acciÃ³n concreta al final.
""",
    "configuracion_privacidad": """# ConfiguraciÃ³n de privacidad

## Umbral de revisiÃ³n manual

6

## Significado

Si el riesgo de confidencialidad estimado es igual o inferior a este nÃºmero, el sistema puede procesar automÃ¡ticamente el texto.

Si el riesgo es superior a este nÃºmero, el sistema debe detenerse y preguntar al cliente si quiere enviar el texto tal como estÃ¡ o reducir el riesgo antes de continuar.

Escala:
- 0 = sin riesgo apreciable.
- 10 = riesgo alto: datos personales, financieros o identificativos sensibles.
""",
    "historial_interacciones": """# Historial de interacciones

Este archivo guardarÃ¡ un resumen de las interacciones relevantes del cliente.

TodavÃ­a no hay interacciones registradas.
""",
    "privacidad_log": """# Log de privacidad

Este archivo registrarÃ¡ decisiones de confidencialidad: riesgo estimado, si se enviÃ³ el texto original o reducido, modelo usado y fecha.

TodavÃ­a no hay decisiones registradas.
""",
}


def ensure_client_files() -> None:
    """Create the active client folder and starter Markdown files if needed."""
    ACTIVE_CLIENT_DIR.mkdir(parents=True, exist_ok=True)

    for key, path in CLIENT_FILES.items():
        if not path.exists():
            path.write_text(INITIAL_CLIENT_FILES[key].strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------

def read_text_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def write_text_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def append_text_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(text.rstrip() + "\n")

def backup_client_file(path: Path) -> None:
    """
    Create a timestamped backup of a client Markdown file before overwriting it.
    """
    if not path.exists():
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backups_dir = path.parent / "backups"
    backups_dir.mkdir(parents=True, exist_ok=True)

    backup_path = backups_dir / f"{path.stem}_{timestamp}{path.suffix}"

    backup_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

def write_client_file_with_backup(path: Path, text: str) -> None:
    """
    Backup a client Markdown file, then overwrite it.
    """
    backup_client_file(path)
    write_text_file(path, text)

def load_prompt(*names: str) -> str:
    """Load one or more Markdown prompt files from the prompts folder."""
    parts: list[str] = []

    for name in names:
        path = PROMPTS_DIR / name
        if path.exists():
            content = path.read_text(encoding="utf-8").strip()
            if content:
                parts.append(content)

    return "\n\n---\n\n".join(parts)

def load_wealth_knowledge() -> str:
    """Load all Markdown files from Wealth_Knowledge."""
    if not WEALTH_KNOWLEDGE_DIR.exists():
        return ""

    parts: list[str] = []

    for path in sorted(WEALTH_KNOWLEDGE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8").strip()
        if content:
            parts.append(f"# Archivo fuente: {path.name}\n\n{content}")

    return "\n\n---\n\n".join(parts)


def load_client_context() -> dict[str, str]:
    """Load all live Markdown files for the active client."""
    ensure_client_files()
    return {key: read_text_file(path) for key, path in CLIENT_FILES.items()}

def read_privacy_threshold(default: int = 6) -> int:
    """
    Read the manual privacy review threshold from configuracion_privacidad.md.

    Expected format inside the file:

    ## Umbral de revisiÃ³n manual

    6

    If the file is missing or the number cannot be read, return the default.
    """
    text = read_text_file(CLIENT_FILES["configuracion_privacidad"])

    lines = text.splitlines()

    for index, line in enumerate(lines):
        if "Umbral de revisiÃ³n manual" in line:
            for following_line in lines[index + 1:]:
                clean_line = following_line.strip()

                if not clean_line:
                    continue

                try:
                    value = int(clean_line)
                    return max(0, min(10, value))
                except ValueError:
                    continue

    return default

def contains_any_marker(text: str, markers: list[str]) -> bool:
    """
    Check whether the text contains any marker as a whole word or phrase.

    This avoids false positives like:
    - "dependiente" inside "independiente"
    """
    lower_text = text.lower()

    for marker in markers:
        lower_marker = marker.lower()
        pattern = r"(?<!\w)" + re.escape(lower_marker) + r"(?!\w)"

        if re.search(pattern, lower_text):
            return True

    return False

def find_matching_markers(text: str, markers: list[str]) -> list[str]:
    """
    Return markers found as whole words or phrases.

    Avoids false positives like:
    - "dependiente" inside "independiente"
    """
    lower_text = text.lower()
    found: list[str] = []

    for marker in markers:
        lower_marker = marker.lower()
        pattern = r"(?<!\w)" + re.escape(lower_marker) + r"(?!\w)"

        if re.search(pattern, lower_text):
            found.append(marker)

    return found

def estimate_privacy_risk(text: str) -> tuple[int, list[str]]:
    """
    Estimate confidentiality risk from 0 to 10 using simple local rules.

    Returns:
    - risk score from 0 to 10
    - list of reasons
    """
    risk = 0
    reasons: list[str] = []

    # Amounts / financial figures
    money_markers = [
        "â‚¬", "eur", "euros", "kâ‚¬", "mâ‚¬", "millÃ³n", "millones"
    ]
    matched_money = find_matching_markers(text, money_markers)
    if matched_money:
        risk += 3
        reasons.append(
            "contiene importes o referencias financieras concretas "
            f"({', '.join(matched_money)})"
        )

    # Personal identifiers
    personal_markers = [
        "me llamo", "mi nombre", "dni", "nie", "pasaporte",
        "telÃ©fono", "email", "correo", "@", "direcciÃ³n", "calle"
    ]
    matched_personal = find_matching_markers(text, personal_markers)
    if matched_personal:
        risk += 4
        reasons.append(
            "puede contener datos identificativos personales "
            f"({', '.join(matched_personal)})"
        )

    # Financial institutions / accounts / advisors
    financial_markers = [
        "banco", "bank", "cuenta", "iban", "broker", "custodio",
        "asesor", "asesoramiento", "entidad", "plataforma",
        "sabadell", "caixabank", "bbva", "santander", "bankinter",
        "renta 4", "myinvestor", "indexa"
    ]
    matched_financial = find_matching_markers(text, financial_markers)
    if matched_financial:
        risk += 2
        reasons.append(
            "menciona entidades financieras, cuentas, plataformas o asesores "
            f"({', '.join(matched_financial)})"
        )

    # Wealth / transaction events
    wealth_markers = [
        "vendÃ­", "he vendido", "venta de mi empresa", "herencia",
        "relaciones", "jubilaciÃ³n", "jubilarme", "pensiÃ³n",
        "inversiÃ³n", "invertir", "cartera", "acciones", "fondos",
        "etf", "bonos"
    ]
    matched_wealth = find_matching_markers(text, wealth_markers)
    if matched_wealth:
        risk += 2
        reasons.append(
            "describe situaciÃ³n patrimonial o decisiones de inversiÃ³n "
            f"({', '.join(matched_wealth)})"
        )

    # Family context
    family_markers = [
        "hijo", "hija", "mujer", "marido", "divorcio",
        "dependiente", "discapacidad", "enfermedad"
    ]
    matched_family = find_matching_markers(text, family_markers)
    if matched_family:
        risk += 2
        reasons.append(
            "incluye contexto familiar o personal sensible "
            f"({', '.join(matched_family)})"
        )

    # Life-stage / planning context
    life_planning_markers = [
        "retiro"
    ]
    matched_life_planning = find_matching_markers(text, life_planning_markers)
    if matched_life_planning:
        risk += 1
        reasons.append(
            "incluye contexto de planificaciÃ³n vital o patrimonial "
            f"({', '.join(matched_life_planning)})"
        )

    # Long detailed messages tend to carry more context
    if len(text) > 500:
        risk += 1
        reasons.append("el mensaje es largo y puede contener contexto sensible acumulado")

    risk = max(0, min(10, risk))

    if not reasons:
        reasons.append("no se detectan datos sensibles evidentes")

    return risk, reasons

def reduce_privacy_risk_locally(text: str) -> str:
    """
    Create a rough lower-risk version of the user's text using simple local rules.

    This is only a placeholder. Later, Gemini can produce a better anonymized version.
    """
    reduced = text

    replacements = {
        "Caixabank": "un banco",
        "CaixaBank": "un banco",
        "Sabadell": "un banco",
        "BBVA": "un banco",
        "Santander": "un banco",
        "Bankinter": "un banco",
        "Renta 4": "una plataforma financiera",
        "MyInvestor": "una plataforma financiera",
        "Indexa": "una plataforma financiera",
        "Barcelona": "una ciudad espaÃ±ola",
        "Madrid": "una ciudad espaÃ±ola",
    }

    for original, replacement in replacements.items():
        reduced = reduced.replace(original, replacement)

    money_patterns = [
        "800.000 euros",
        "800.000 â‚¬",
        "800000 euros",
        "800000 â‚¬",
        "800k",
        "800 k",
    ]

    for pattern in money_patterns:
        reduced = reduced.replace(pattern, "un relaciones lÃ­quido significativo")

    return reduced

def privacy_bar(score: int) -> str:
    """
    Return a visual 0â€“10 privacy risk bar.
    """
    score = max(0, min(10, score))
    return "â–ˆ" * score + "â–‘" * (10 - score)

def save_wealth_log(user_input: str, ai_answer: str, usage: dict) -> None:
    """Save a trace of a model-generated answer."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"""
## {timestamp}

### Cliente activo

{ACTIVE_CLIENT_NAME}

### Entrada del usuario

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
    append_text_file(WEALTH_LOG_FILE, entry)

def process_with_orchestrator_placeholder(text_to_process: str, source: str) -> str:
    """
    Placeholder for the future Gemini orchestrator.

    For now, it only records the approved text in historial_interacciones.md.
    Later, this function will:
    - call Gemini;
    - update quien_soy.md;
    - update que_quiero.md;
    - update que_tengo_que_hacer.md;
    - generate the final client response;
    - save a full audit log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    append_text_file(
        CLIENT_FILES["historial_interacciones"],
        f"""
## {timestamp}

### Fuente

{source}

### Texto procesado

{text_to_process}

### Estado

Procesado por el orquestador placeholder. TodavÃ­a no se ha enviado a Gemini.

---
""",
    )

    return (
        "He procesado el texto con el orquestador placeholder.\n\n"
        "TodavÃ­a no he llamado a Gemini ni he actualizado los tres resÃºmenes vivos.\n\n"
        "Pero la tuberÃ­a ya funciona:\n"
        "mensaje â†’ privacidad â†’ aprobaciÃ³n â†’ procesamiento â†’ historial."
    )

def process_with_gemini_orchestrator(text_to_process: str, source: str) -> str:
    """
    First real Gemini orchestrator.

    It updates:
    - quien_soy.md
    - que_quiero.md
    - que_tengo_que_hacer.md

    And returns the client-facing answer.
    """
    ensure_client_files()

    client_context = load_client_context()
    wealth_knowledge = load_wealth_knowledge()

    system_prompt = """
Eres un copiloto patrimonial independiente para clientes espaÃ±oles.

Tu funciÃ³n NO es recomendar inversiones concretas.
Tu funciÃ³n NO es vender productos.
Tu funciÃ³n NO es decidir por el cliente.

Tu funciÃ³n es:
- ordenar la informaciÃ³n del cliente;
- clarificar quiÃ©n es;
- clarificar quÃ© quiere;
- identificar quÃ© tiene que hacer;
- explicar riesgos, costes, preguntas y criterios;
- ayudar al cliente a preparar mejores decisiones.

Debes escribir en castellano claro, sobrio, tranquilo y prÃ¡ctico.

No escribas como una carta formal bancaria.
No empieces con "Estimado cliente".
No uses tono comercial.
Habla de forma directa, humana e independiente.
Usa "usted" si el estilo del cliente no indica lo contrario, pero mantÃ©n un tono cercano y claro.

Reglas estrictas:
- No recomiendes productos concretos.
- No digas al cliente quÃ© inversiÃ³n debe elegir.
- No hagas market timing.
- No prometas rentabilidades.
- No sustituyas a un asesor financiero regulado.
- Si falta informaciÃ³n, formula preguntas.
- Si hay incertidumbre, dilo.
- MantÃ©n los archivos vivos limpios, Ãºtiles y editables.
- No termines con preguntas vagas como "Â¿Le parece bien si empezamos por ahÃ­?"
- Termina siempre con una prÃ³xima acciÃ³n concreta, pequeÃ±a y fÃ¡cil de responder.
- Si faltan muchos datos, pide solo el dato mÃ¡s importante ahora.
- No pidas tres bloques grandes de informaciÃ³n a la vez.

Debes devolver SOLO JSON vÃ¡lido.
No uses Markdown fuera del JSON.
No expliques nada fuera del JSON.
"""

    prompt = f"""
Tenemos un cliente patrimonial.

El cliente ha escrito este nuevo mensaje:

<<<MENSAJE_CLIENTE
{text_to_process}
MENSAJE_CLIENTE>>>

Fuente del mensaje:
{source}

Estos son los archivos vivos actuales del cliente.

<<<QUIEN_SOY_ACTUAL
{client_context["quien_soy"]}
QUIEN_SOY_ACTUAL>>>

<<<QUE_QUIERO_ACTUAL
{client_context["que_quiero"]}
QUE_QUIERO_ACTUAL>>>

<<<QUE_TENGO_QUE_HACER_ACTUAL
{client_context["que_tengo_que_hacer"]}
QUE_TENGO_QUE_HACER_ACTUAL>>>

<<<ESTILO_RESPUESTA
{client_context["estilo_respuesta"]}
ESTILO_RESPUESTA>>>

Este es el conocimiento patrimonial local disponible:

<<<WEALTH_KNOWLEDGE
{wealth_knowledge}
WEALTH_KNOWLEDGE>>>

Tarea:

1. Interpreta el nuevo mensaje del cliente.
2. Actualiza el contenido completo de quien_soy.md.
3. Actualiza el contenido completo de que_quiero.md.
4. Actualiza el contenido completo de que_tengo_que_hacer.md.
5. Escribe una respuesta Ãºtil para el cliente.
6. PropÃ³n una prÃ³xima acciÃ³n concreta, pequeÃ±a y fÃ¡cil de responder.
   Si faltan muchos datos, elige solo el dato mÃ¡s importante para avanzar.

La respuesta al cliente debe ser breve, clara y accionable. No debe parecer una carta comercial.
Debe terminar orientando al cliente hacia una sola acciÃ³n concreta.
Evita cerrar con preguntas vagas de permiso.

Devuelve SOLO este JSON:

{{
  "quien_soy": "contenido completo actualizado de quien_soy.md",
  "que_quiero": "contenido completo actualizado de que_quiero.md",
  "que_tengo_que_hacer": "contenido completo actualizado de que_tengo_que_hacer.md",
  "respuesta_cliente": "respuesta final para enviar al cliente por Telegram",
  "proxima_accion": "una prÃ³xima acciÃ³n concreta",
  "notas_auditoria": "resumen breve de quÃ© se ha actualizado y por quÃ©"
}}
"""

    try:
        raw_answer, usage = gemini_llm(prompt=prompt, system_prompt=system_prompt)

    except errors.ServerError as error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        append_text_file(
            WEALTH_LOG_FILE,
            f"""
## {timestamp}

### Error del orquestador Gemini

Gemini no estaba disponible temporalmente.

### Error

{error}

### Texto que se intentaba procesar

{text_to_process}

### Estado

No se han modificado los resÃºmenes vivos.

---
""",
        )

        return (
            "He intentado llamar al orquestador, pero Gemini estÃ¡ temporalmente saturado.\n\n"
            "No he modificado los resÃºmenes vivos.\n\n"
            "He guardado el error en el log. Puedes volver a enviar el mensaje en unos minutos."
        )

    except Exception as error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        append_text_file(
            WEALTH_LOG_FILE,
            f"""
## {timestamp}

### Error inesperado del orquestador

### Error

{error}

### Texto que se intentaba procesar

{text_to_process}

### Estado

No se han modificado los resÃºmenes vivos.

---
""",
        )

        return (
            "Ha ocurrido un error inesperado al llamar al orquestador.\n\n"
            "No he modificado los resÃºmenes vivos.\n\n"
            "He guardado el error en el log para depurarlo."
        )

    try:
        parsed = extract_json_from_text(raw_answer)

    except Exception as first_error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        append_text_file(
            WEALTH_LOG_FILE,
            f"""
## {timestamp}

### Aviso del orquestador Gemini

La primera respuesta no era JSON vÃ¡lido. Se intentarÃ¡ reparaciÃ³n automÃ¡tica.

### Error inicial

{first_error}

### Respuesta cruda inicial

{raw_answer}

---
""",
        )

        try:
            parsed = repair_json_with_gemini(raw_answer)

            append_text_file(
                WEALTH_LOG_FILE,
                f"""
## {timestamp}

### ReparaciÃ³n JSON

La reparaciÃ³n automÃ¡tica del JSON ha funcionado.

---
""",
            )

        except Exception as repair_error:
            append_text_file(
                WEALTH_LOG_FILE,
                f"""
## {timestamp}

### Error del orquestador Gemini

No se pudo parsear ni reparar la respuesta como JSON.

### Error inicial

{first_error}

### Error de reparaciÃ³n

{repair_error}

### Respuesta cruda

{raw_answer}

---
""",
            )

            return (
                "He llamado al orquestador, pero la respuesta no era JSON vÃ¡lido y no he podido repararla automÃ¡ticamente.\n\n"
                "No he modificado los resÃºmenes vivos.\n\n"
                "He guardado la respuesta cruda en el log para depurarlo."
            )

    required_keys = [
        "quien_soy",
        "que_quiero",
        "que_tengo_que_hacer",
        "respuesta_cliente",
        "proxima_accion",
        "notas_auditoria",
    ]

    missing_keys = [key for key in required_keys if key not in parsed]

    if missing_keys:
        return (
            "El orquestador respondiÃ³, pero faltan campos obligatorios:\n\n"
            + "\n".join(f"- {key}" for key in missing_keys)
            + "\n\nNo he modificado los resÃºmenes vivos."
        )

    write_client_file_with_backup(CLIENT_FILES["quien_soy"], parsed["quien_soy"])
    write_client_file_with_backup(CLIENT_FILES["que_quiero"], parsed["que_quiero"])
    write_client_file_with_backup(
        CLIENT_FILES["que_tengo_que_hacer"],
        parsed["que_tengo_que_hacer"],
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    append_text_file(
        CLIENT_FILES["historial_interacciones"],
        f"""
## {timestamp}

### Fuente

{source}

### Texto procesado

{text_to_process}

### Respuesta al cliente

{parsed["respuesta_cliente"]}

### PrÃ³xima acciÃ³n

{parsed["proxima_accion"]}

### Notas de auditorÃ­a

{parsed["notas_auditoria"]}

### Modelo

{usage.get("model", GEMINI_MODEL)}

### Tokens

- Input tokens: {usage.get("input_tokens", 0)}
- Output tokens: {usage.get("output_tokens", 0)}
- Total tokens: {usage.get("total_tokens", 0)}
- Estimated cost USD: {usage.get("estimated_cost_usd", 0):.6f}

---
""",
    )

    save_wealth_log(
        user_input=text_to_process,
        ai_answer=parsed["respuesta_cliente"],
        usage=usage,
    )

    return (
        f"{parsed['respuesta_cliente']}\n\n"
        f"PrÃ³xima acciÃ³n:\n{parsed['proxima_accion']}\n\n"
        "---\n"
        "ResÃºmenes vivos actualizados."
        + format_gemini_usage_note(usage)
    )

# ---------------------------------------------------------------------
# Gemini helper
# ---------------------------------------------------------------------

def gemini_llm(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """Send a prompt to Gemini and return answer text plus usage metadata."""
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

def extract_json_from_text(text: str) -> dict:
    """
    Extract JSON from a Gemini response.

    Gemini may return pure JSON, or JSON wrapped in ```json ... ```.
    This helper makes parsing a bit more robust.
    """
    cleaned = text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.removeprefix("```json").strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.removeprefix("```").strip()

    if cleaned.endswith("```"):
        cleaned = cleaned.removesuffix("```").strip()

    return json.loads(cleaned)

def repair_json_with_gemini(raw_text: str) -> dict:
    """
    Ask Gemini to repair an invalid JSON-like response into valid JSON.

    This is used only when the first JSON parse fails.
    """
    repair_system_prompt = """
Eres un reparador estricto de JSON.

Tu Ãºnica tarea es convertir el texto recibido en JSON vÃ¡lido.

Reglas:
- Devuelve SOLO JSON vÃ¡lido.
- No expliques nada.
- No uses Markdown.
- No uses ```json.
- Conserva exactamente estas claves si aparecen:
  - quien_soy
  - que_quiero
  - que_tengo_que_hacer
  - respuesta_cliente
  - proxima_accion
  - notas_auditoria
- Si falta alguna clave, crÃ©ala con un texto breve indicando que falta informaciÃ³n.
"""

    repair_prompt = f"""
Este texto deberÃ­a ser JSON, pero puede contener errores de formato.

Repara el texto y devuelve SOLO JSON vÃ¡lido.

Texto a reparar:

<<<RAW_TEXT
{raw_text}
RAW_TEXT>>>
"""

    repaired_answer, _usage = gemini_llm(
        prompt=repair_prompt,
        system_prompt=repair_system_prompt,
    )

    return extract_json_from_text(repaired_answer)

def format_gemini_usage_note(usage: dict) -> str:
    """Small cost note appended to Telegram answers during development."""
    return (
        "\n\n---\n"
        "EstimaciÃ³n de uso Gemini:\n"
        f"Modelo: {usage['model']}\n"
        f"Input tokens: {usage['input_tokens']}\n"
        f"Output tokens: {usage['output_tokens']}\n"
        f"Total tokens: {usage['total_tokens']}\n"
        f"Coste estimado: ${usage['estimated_cost_usd']:.6f}"
    )


async def send_long_message(update: Update, text: str, reply_markup=None, chunk_size: int = 3500) -> None:
    """Send long Telegram messages in safe chunks."""
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
# Telegram handlers
# ---------------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()
    await update.message.reply_text(
        (
            "Soy Copiloto Relaciones.\n\n"
            f"Cliente activo: {ACTIVE_CLIENT_NAME}\n\n"
            "De momento, los botones muestran los tres resÃºmenes vivos. "
            "En el siguiente paso activaremos la entrada libre con evaluaciÃ³n de confidencialidad."
        ),
        reply_markup=MAIN_KEYBOARD,
    )


async def show_quien_soy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()
    await send_long_message(update, read_text_file(CLIENT_FILES["quien_soy"]), reply_markup=MAIN_KEYBOARD)


async def show_que_quiero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()
    await send_long_message(update, read_text_file(CLIENT_FILES["que_quiero"]), reply_markup=MAIN_KEYBOARD)


async def show_que_tengo_que_hacer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()
    await send_long_message(update, read_text_file(CLIENT_FILES["que_tengo_que_hacer"]), reply_markup=MAIN_KEYBOARD)

async def show_privacy_threshold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()
    threshold = read_privacy_threshold()

    await update.message.reply_text(
        f"Umbral de revisiÃ³n manual actual: {threshold}/10",
        reply_markup=MAIN_KEYBOARD,
    )

async def test_privacy_risk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = " ".join(context.args).strip()

    if not text:
        await update.message.reply_text(
            "Uso: /riesgo texto a evaluar",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    score, reasons = estimate_privacy_risk(text)
    threshold = read_privacy_threshold()

    reasons_text = "\n".join(f"- {reason}" for reason in reasons)

    await update.message.reply_text(
        (
            f"Riesgo de confidencialidad: {score}/10\n"
            f"{privacy_bar(score)}\n\n"
            f"Umbral de revisiÃ³n manual: {threshold}/10\n\n"
            f"Motivos:\n{reasons_text}"
        ),
        reply_markup=MAIN_KEYBOARD,
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("pending_privacy_message", None)
    context.user_data.pop("pending_privacy_score", None)
    context.user_data.pop("pending_privacy_reasons", None)

    await update.message.reply_text(
        "Cancelado. He eliminado el mensaje pendiente.",
        reply_markup=MAIN_KEYBOARD,
    )

async def send_pending_privacy_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()

    pending_message = context.user_data.get("pending_privacy_message")
    score = context.user_data.get("pending_privacy_score")
    reasons = context.user_data.get("pending_privacy_reasons", [])

    if not pending_message:
        await update.message.reply_text(
            "No hay ningÃºn mensaje pendiente para enviar.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    threshold = read_privacy_threshold()
    reasons_text = "\n".join(f"- {reason}" for reason in reasons)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    append_text_file(
        CLIENT_FILES["privacidad_log"],
        f"""
## {timestamp}

### Mensaje recibido

{pending_message}

### Riesgo estimado

{score}/10

### Umbral

{threshold}/10

### DecisiÃ³n

El cliente ha aprobado continuar con el texto original pese a superar el umbral.

### Estado

TodavÃ­a no se ha enviado a la LLM externa en esta versiÃ³n.

### Motivos

{reasons_text}

---
""",
    )

    context.user_data.pop("pending_privacy_message", None)
    context.user_data.pop("pending_privacy_score", None)
    context.user_data.pop("pending_privacy_reasons", None)

    orchestrator_result = process_with_gemini_orchestrator(
        text_to_process=pending_message,
        source="Texto aprobado tras revisiÃ³n de privacidad",
    )

    await update.message.reply_text(
        (
            f"Texto aprobado para continuar.\n\n"
            f"Riesgo de confidencialidad: {score}/10\n"
            f"{privacy_bar(score)}\n\n"
            "He registrado la decisiÃ³n en el log de privacidad.\n\n"
            f"{orchestrator_result}"
        ),
        reply_markup=MAIN_KEYBOARD,
    )
    
async def reduce_pending_privacy_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()

    pending_message = context.user_data.get("pending_privacy_message")

    if not pending_message:
        await update.message.reply_text(
            "No hay ningÃºn mensaje pendiente para reducir.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    original_score = context.user_data.get("pending_privacy_score")
    original_reasons = context.user_data.get("pending_privacy_reasons", [])

    reduced_message = reduce_privacy_risk_locally(pending_message)
    reduced_score, reduced_reasons = estimate_privacy_risk(reduced_message)

    context.user_data["pending_privacy_message"] = reduced_message
    context.user_data["pending_privacy_score"] = reduced_score
    context.user_data["pending_privacy_reasons"] = reduced_reasons
    context.user_data["pending_privacy_original_message"] = pending_message
    context.user_data["pending_privacy_original_score"] = original_score
    context.user_data["pending_privacy_original_reasons"] = original_reasons

    threshold = read_privacy_threshold()

    original_reasons_text = "\n".join(f"- {reason}" for reason in original_reasons)
    reduced_reasons_text = "\n".join(f"- {reason}" for reason in reduced_reasons)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    append_text_file(
        CLIENT_FILES["privacidad_log"],
        f"""
## {timestamp}

### AcciÃ³n

ReducciÃ³n local de riesgo de confidencialidad.

### Texto original

{pending_message}

### Riesgo original

{original_score}/10

### Motivos originales

{original_reasons_text}

### Texto reducido

{reduced_message}

### Riesgo reducido

{reduced_score}/10

### Motivos reducidos

{reduced_reasons_text}

### Estado

TodavÃ­a no se ha enviado a la LLM externa en esta versiÃ³n.

---
""",
    )

    decision_keyboard = ReplyKeyboardMarkup(
        [
            ["Enviar la pregunta"],
            ["Cancelar"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        (
            "He creado una versiÃ³n con menor riesgo de confidencialidad.\n\n"
            f"Riesgo original: {original_score}/10\n"
            f"{privacy_bar(original_score)}\n\n"
            f"Riesgo reducido: {reduced_score}/10\n"
            f"{privacy_bar(reduced_score)}\n\n"
            f"VersiÃ³n reducida:\n\n"
            f"{reduced_message}\n\n"
            f"Umbral de revisiÃ³n manual: {threshold}/10\n\n"
            "Si te parece bien, pulsa â€œEnviar la preguntaâ€.\n"
            "Nota: en esta versiÃ³n, eso solo aprobarÃ¡ continuar con este texto reducido; todavÃ­a no se enviarÃ¡ a la LLM externa."
        ),
        reply_markup=decision_keyboard,
    )

async def handle_free_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()

    user_text = update.message.text.strip()
    score, reasons = estimate_privacy_risk(user_text)
    threshold = read_privacy_threshold()

    reasons_text = "\n".join(f"- {reason}" for reason in reasons)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    if score <= threshold:
        append_text_file(
            CLIENT_FILES["privacidad_log"],
            f"""
## {timestamp}

### Mensaje recibido

{user_text}

### Riesgo estimado

{score}/10

### Umbral

{threshold}/10

### DecisiÃ³n

Procesar automÃ¡ticamente en el siguiente paso.

### Motivos

{reasons_text}

---
""",
        )

        orchestrator_result = process_with_gemini_orchestrator(
            text_to_process=user_text,
            source="Texto procesado automÃ¡ticamente por estar dentro del umbral de privacidad",
        )

        await update.message.reply_text(
            (
                f"Riesgo de confidencialidad: {score}/10\n"
                f"{privacy_bar(score)}\n\n"
                f"Umbral de revisiÃ³n manual: {threshold}/10\n\n"
                f"Motivos:\n{reasons_text}\n\n"
                "Este mensaje estÃ¡ dentro del umbral configurado.\n\n"
                f"{orchestrator_result}"
            ),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    context.user_data["pending_privacy_message"] = user_text
    context.user_data["pending_privacy_score"] = score
    context.user_data["pending_privacy_reasons"] = reasons

    decision_keyboard = ReplyKeyboardMarkup(
        [
            ["Enviar la pregunta"],
            ["Reducir riesgo de confidencialidad"],
            ["Cancelar"],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        (
            f"Riesgo de confidencialidad: {score}/10\n"
            f"{privacy_bar(score)}\n\n"
            f"Umbral de revisiÃ³n manual: {threshold}/10\n\n"
            f"Motivos:\n{reasons_text}\n\n"
            "Este mensaje supera el umbral configurado.\n\n"
            "Puedes enviarlo tal como estÃ¡ o reducir el riesgo antes de enviarlo a una LLM externa."
        ),
        reply_markup=decision_keyboard,
    )


# ---------------------------------------------------------------------
# App
# ---------------------------------------------------------------------

def main() -> None:
    ensure_client_files()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(MessageHandler(filters.Regex(r"^Cancelar$"), cancel))
    app.add_handler(MessageHandler(filters.Regex(r"^Enviar la pregunta$"), send_pending_privacy_message))
    app.add_handler(MessageHandler(filters.Regex(r"^Reducir riesgo de confidencialidad$"), reduce_pending_privacy_message))

    app.add_handler(CommandHandler("privacidad", show_privacy_threshold))

    app.add_handler(CommandHandler("riesgo", test_privacy_risk))

    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ‘¤ Resumen de quiÃ©n soy yo$"), show_quien_soy))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸŽ¯ Resumen de quÃ© quiero$"), show_que_quiero))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ§­ Resumen de quÃ© tengo que hacer$"), show_que_tengo_que_hacer))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_free_text))

    app.run_polling()


if __name__ == "__main__":
    main()

