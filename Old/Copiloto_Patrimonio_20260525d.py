import os
import json

from contextvars import ContextVar
from datetime import datetime, date, time
from zoneinfo import ZoneInfo
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types, errors
from openai import OpenAI
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

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_INPUT_PRICE_PER_1M = float(os.getenv("DEEPSEEK_INPUT_PRICE_PER_1M", "0.435"))
DEEPSEEK_OUTPUT_PRICE_PER_1M = float(os.getenv("DEEPSEEK_OUTPUT_PRICE_PER_1M", "0.87"))

SHOW_USAGE_NOTE = os.getenv(
    "SHOW_USAGE_NOTE",
    os.getenv("SHOW_GEMINI_USAGE_NOTE", "true"),
).lower() == "true"

LLM_PROVIDER_ORDER = [
    provider.strip().lower()
    for provider in os.getenv("LLM_PROVIDER_ORDER", "deepseek,gemini").split(",")
    if provider.strip()
]

WEALTH_KNOWLEDGE_DIR = Path("Wealth_Knowledge")
AGENT_CONFIG_DIR = Path("AgentConfig")
INTERVENTION_PATTERNS_DIR = AGENT_CONFIG_DIR / "InterventionPatterns"
INITIAL_CLIENT_FILES_DIR = Path("InitialClientFiles")
APP_TEXTS_DIR = Path("AppTexts")

CLIENTS_DIR = Path("ClientData")
DEFAULT_CLIENT_NAME = os.getenv("ACTIVE_CLIENT_NAME", "Cliente1")

CURRENT_CLIENT_NAME: ContextVar[str] = ContextVar(
    "CURRENT_CLIENT_NAME",
    default=DEFAULT_CLIENT_NAME,
)


def current_client_name() -> str:
    """Return the client currently active in this async context."""
    return CURRENT_CLIENT_NAME.get()


def set_current_client_name(client_name: str) -> None:
    """Set the client currently active in this async context."""
    CURRENT_CLIENT_NAME.set(client_name)


def active_client_dir() -> Path:
    """Return the active client's folder."""
    return CLIENTS_DIR / current_client_name()


def client_files() -> dict[str, Path]:
    """Return live Markdown file paths for the active client."""
    active_dir = active_client_dir()

    return {
        "quien_soy": active_dir / "quien_soy.md",
        "que_quiero": active_dir / "que_quiero.md",
        "que_tengo_que_hacer": active_dir / "que_tengo_que_hacer.md",
        "estilo_respuesta": active_dir / "estilo_respuesta.md",
        "agent_config": active_dir / "agent_config.md",
        "agent_observations": active_dir / "agent_observations.md",
        "proactivity_log": active_dir / "proactivity_log.md",
        "historial_interacciones": active_dir / "historial_interacciones.md",
    }


def wealth_log_file() -> Path:
    return active_client_dir() / "wealth_logs.md"


def followup_triggers_file() -> Path:
    return active_client_dir() / "followup_triggers.json"


def app_state_file() -> Path:
    return active_client_dir() / "app_state.json"


def client_name_from_update(update: Update) -> str:
    """Map one Telegram chat to one isolated client folder."""
    if update.effective_chat is None:
        return DEFAULT_CLIENT_NAME

    return f"telegram_{update.effective_chat.id}"


def activate_client_from_update(update: Update) -> None:
    """Activate the correct client folder for this Telegram update."""
    set_current_client_name(client_name_from_update(update))


def iter_telegram_client_names() -> list[str]:
    """Return all Telegram-based client folder names."""
    if not CLIENTS_DIR.exists():
        return []

    return sorted(
        path.name
        for path in CLIENTS_DIR.iterdir()
        if path.is_dir() and path.name.startswith("telegram_")
    )


APP_TIMEZONE = os.getenv("APP_TIMEZONE", "Europe/Madrid")
PROACTIVE_SCHEDULER_HOUR = int(os.getenv("PROACTIVE_SCHEDULER_HOUR", "10"))
PROACTIVE_SCHEDULER_MINUTE = int(os.getenv("PROACTIVE_SCHEDULER_MINUTE", "40"))

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

deepseek_client = (
    OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
    )
    if DEEPSEEK_API_KEY
    else None
)

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

def ensure_client_files() -> None:
    """Create the active client folder and starter Markdown files if needed."""
    active_client_dir().mkdir(parents=True, exist_ok=True)

    for key, path in client_files().items():
        if path.exists():
            continue

        template_path = INITIAL_CLIENT_FILES_DIR / f"{key}.md"

        if template_path.exists():
            content = template_path.read_text(encoding="utf-8").strip()
        else:
            content = f"# {key}\n\nPendiente."

        path.write_text(content + "\n", encoding="utf-8")

# ---------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------

def now_app() -> datetime:
    """Current datetime in the app timezone."""
    return datetime.now(ZoneInfo(APP_TIMEZONE))


def today_app() -> date:
    """Current date in the app timezone."""
    return now_app().date()


def format_app_datetime() -> str:
    """Standard timestamp in the app timezone."""
    return now_app().strftime("%Y-%m-%d %H:%M:%S")


def format_app_minute() -> str:
    """Standard minute-level timestamp in the app timezone."""
    return now_app().strftime("%Y-%m-%d %H:%M")


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

def load_app_state() -> dict:
    """Load small persistent app state, such as the Telegram chat ID."""
    path = app_state_file()

    if not path.exists():
        return {}

    try:
        content = path.read_text(encoding="utf-8").strip()

        if not content:
            return {}

        data = json.loads(content)

        if isinstance(data, dict):
            return data

        return {}

    except json.JSONDecodeError:
        return {}


def save_app_state(state: dict) -> None:
    """Save small persistent app state."""
    path = app_state_file()
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def remember_chat_id(update: Update) -> None:
    """Remember the current Telegram chat ID so scheduled jobs can send proactive messages."""
    if update.effective_chat is None:
        return

    state = load_app_state()
    state["telegram_chat_id"] = update.effective_chat.id
    state["telegram_chat_id_updated_at"] = format_app_datetime()
    save_app_state(state)


def get_remembered_chat_id() -> int | None:
    """Return the remembered Telegram chat ID, if available."""
    state = load_app_state()

    chat_id = state.get("telegram_chat_id")

    if chat_id is None:
        return None

    try:
        return int(chat_id)
    except (TypeError, ValueError):
        return None
    
def backup_client_file(path: Path) -> None:
    """
    Create a timestamped backup of a client Markdown file before overwriting it.
    """
    if not path.exists():
        return

    timestamp = now_app().strftime("%Y%m%d_%H%M%S")

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

def ensure_followup_triggers_file() -> None:
    """Create followup_triggers.json if it does not exist."""
    path = followup_triggers_file()
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text("[]\n", encoding="utf-8")


def get_pending_followup_triggers() -> list[dict]:
    """Return pending follow-up triggers."""
    triggers = load_followup_triggers()

    return [
        trigger for trigger in triggers
        if str(trigger.get("status", "pending")).lower() == "pending"
    ]


def format_pending_followups_for_prompt() -> str:
    """Return a compact summary of pending follow-ups for the orchestrator prompt."""
    pending = get_pending_followup_triggers()

    if not pending:
        return "No hay follow-ups pendientes."

    lines: list[str] = []

    for index, trigger in enumerate(pending, start=1):
        lines.append(
            "\n".join(
                [
                    f"{index}.",
                    f"- id: {trigger.get('id', '')}",
                    f"- date: {trigger.get('date', '')}",
                    f"- type: {trigger.get('type', '')}",
                    f"- message_template: {trigger.get('message_template', '')}",
                    f"- reason: {trigger.get('reason', '')}",
                    f"- status: {trigger.get('status', '')}",
                ]
            )
        )

    return "\n\n".join(lines)


def parse_followup_date(date_text: str) -> date | None:
    """Parse a follow-up date in YYYY-MM-DD format."""
    if not date_text:
        return None

    try:
        return datetime.strptime(date_text.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_snooze_date(date_text: str) -> date | None:
    """Parse simple snooze expressions into a date."""
    text = date_text.lower().strip()
    today = today_app()

    if text in {"hoy", "today"}:
        return today

    if text in {"maÃ±ana", "manana", "tomorrow"}:
        return date.fromordinal(today.toordinal() + 1)

    if text in {"semana", "una_semana", "1_semana", "next_week"}:
        return date.fromordinal(today.toordinal() + 7)

    if text in {"mes", "un_mes", "1_mes", "next_month"}:
        return date.fromordinal(today.toordinal() + 30)

    parsed = parse_followup_date(text)

    if parsed is not None:
        return parsed

    return None


def normalize_followup_text(text: str) -> str:
    """Normalize follow-up text for simple duplicate detection."""
    return " ".join(text.lower().strip().split())


def normalize_followup_type(raw_type: str, message_template: str = "", reason: str = "") -> str:
    """Normalize model-generated follow-up types into a fixed allowed list."""
    text = normalize_followup_text(
        " ".join(
            [
                raw_type,
                message_template,
                reason,
            ]
        )
    )

    allowed_types = {
        "document_expected",
        "document_review",
        "client_action_reminder",
        "decision_deadline",
        "meeting_preparation",
        "advisor_followup",
        "general_checkin",
    }

    raw_type_clean = raw_type.strip().lower()

    if raw_type_clean in allowed_types:
        return raw_type_clean

    action_words = [
        "accion",
        "acciÃ³n",
        "recordatorio_accion",
        "action",
        "reminder",
        "recordatorio",
        "contactar",
        "llamar",
        "escribir",
        "hacer",
    ]

    document_expected_words = [
        "document_pending",
        "pending_document",
        "document_delivery",
        "espera_documento",
        "propuesta",
        "documento",
        "documentacion",
        "documentaciÃ³n",
        "recibir",
    ]

    document_review_words = [
        "review",
        "revision",
        "revisiÃ³n",
        "analizar",
        "revisar",
        "comparar",
    ]

    meeting_words = [
        "meeting",
        "reunion",
        "reuniÃ³n",
        "cita",
    ]

    deadline_words = [
        "deadline",
        "fecha limite",
        "fecha lÃ­mite",
        "decidir antes",
        "vencimiento",
    ]

    advisor_words = [
        "asesor",
        "advisor",
        "gestor",
        "tercero",
    ]

    if any(word in text for word in deadline_words):
        return "decision_deadline"

    if any(word in text for word in meeting_words):
        return "meeting_preparation"

    if any(word in text for word in document_review_words):
        return "document_review"

    if any(word in text for word in document_expected_words):
        return "document_expected"

    if any(word in text for word in advisor_words):
        return "advisor_followup"

    if any(word in text for word in action_words):
        return "client_action_reminder"

    return "general_checkin"


def followup_text_blob(trigger: dict) -> str:
    """Combine follow-up fields into one normalized text blob."""
    return normalize_followup_text(
        " ".join(
            [
                str(trigger.get("type", "")),
                str(trigger.get("message_template", "")),
                str(trigger.get("reason", "")),
            ]
        )
    )


def canonical_followup_topic(trigger: dict) -> str:
    """Return a rough semantic topic for deduplication."""
    text = followup_text_blob(trigger)

    bank_proposal_keywords = [
        "banco",
        "propuesta",
        "costes",
        "costos",
        "productos",
        "condiciones",
        "inversiÃ³n",
        "inversion",
        "documento",
        "documentaciÃ³n",
        "documentacion",
    ]

    if any(keyword in text for keyword in bank_proposal_keywords):
        return "bank_proposal_review"

    return str(trigger.get("type", "")).strip().lower()


def is_similar_pending_followup(new_trigger: dict, existing_triggers: list[dict]) -> bool:
    """
    Return True if a similar pending follow-up already exists.

    Rules:
    - same date;
    - same canonical topic;
    - pending only.
    """
    new_date = str(new_trigger.get("date", "")).strip()
    new_topic = canonical_followup_topic(new_trigger)
    new_message = normalize_followup_text(str(new_trigger.get("message_template", "")))

    for existing in existing_triggers:
        existing_status = str(existing.get("status", "pending")).lower()

        if existing_status != "pending":
            continue

        existing_date = str(existing.get("date", "")).strip()

        if not existing_date or existing_date != new_date:
            continue

        existing_topic = canonical_followup_topic(existing)

        if existing_topic and new_topic and existing_topic == new_topic:
            return True

        existing_message = normalize_followup_text(str(existing.get("message_template", "")))

        if existing_message and new_message:
            shared_words = set(existing_message.split()) & set(new_message.split())
            all_words = set(existing_message.split()) | set(new_message.split())

            if all_words:
                similarity = len(shared_words) / len(all_words)

                if similarity >= 0.50:
                    return True

    return False


def infer_followup_date_from_user_text(user_text: str, current_date_text: str) -> str | None:
    """
    Infer obvious follow-up dates locally from the user's message.

    This protects the system when the LLM misunderstands simple date expressions
    like "hoy" or "maÃ±ana".
    """
    text = user_text.lower().strip()

    try:
        current = datetime.strptime(current_date_text, "%Y-%m-%d").date()
    except ValueError:
        return None

    if "hoy" in text:
        return current.strftime("%Y-%m-%d")

    if "maÃ±ana" in text:
        return (current.fromordinal(current.toordinal() + 1)).strftime("%Y-%m-%d")

    if "la semana que viene" in text:
        return (current.fromordinal(current.toordinal() + 7)).strftime("%Y-%m-%d")

    if "en unos dÃ­as" in text or "en unos dias" in text:
        return (current.fromordinal(current.toordinal() + 3)).strftime("%Y-%m-%d")

    if "el mes que viene" in text:
        return (current.fromordinal(current.toordinal() + 14)).strftime("%Y-%m-%d")

    return None
    

def load_followup_triggers() -> list[dict]:
    """Load proactive follow-up triggers from JSON."""
    ensure_followup_triggers_file()

    try:
        content = followup_triggers_file().read_text(encoding="utf-8").strip()

        if not content:
            return []

        data = json.loads(content)

        if isinstance(data, list):
            return data

        return []

    except json.JSONDecodeError:
        return []


def save_followup_triggers(triggers: list[dict]) -> None:
    """Save proactive follow-up triggers to JSON."""
    path = followup_triggers_file()
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(triggers, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    

def append_agent_observation(
    source: str,
    user_input: str,
    observations: dict[str, str],
) -> None:
    """Append internal agent observations to agent_observations.md."""
    ensure_client_files()

    timestamp = format_app_minute()

    sections: list[str] = []

    for agent_name, observation in observations.items():
        if not observation:
            continue

        clean_agent_name = agent_name.replace("_", " ").title()

        sections.append(
            f"### {clean_agent_name}\n\n{observation.strip()}"
        )

    if not sections:
        return

    template = load_required_app_text("agent_observation_entry.md")

    entry = render_template(
        template,
        {
            "timestamp": timestamp,
            "source": source,
            "user_input": user_input,
            "agent_sections": "\n\n".join(sections),
        },
    )

    append_text_file(client_files()["agent_observations"], entry)

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

def load_agent_config_files() -> str:
    """Load global agent configuration Markdown files."""
    if not AGENT_CONFIG_DIR.exists():
        return ""

    parts: list[str] = []

    for path in sorted(AGENT_CONFIG_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8").strip()
        if content:
            parts.append(f"# Agent config file: {path.name}\n\n{content}")

    return "\n\n---\n\n".join(parts)

def load_client_agent_config() -> str:
    """Load the active client's agent behavior configuration."""
    ensure_client_files()
    return read_text_file(client_files()["agent_config"])

def load_client_context() -> dict[str, str]:
    """Load all live Markdown files for the active client."""
    ensure_client_files()
    return {key: read_text_file(path) for key, path in client_files().items()}

def load_app_text(name: str) -> str:
    """Load an app text template from AppTexts."""
    path = APP_TEXTS_DIR / name

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8").strip()

def load_required_app_text(name: str) -> str:
    """Load an app text template and fail clearly if it is missing."""
    text = load_app_text(name)

    if text:
        return text

    fallback = load_app_text("missing_app_text_error.md")

    if fallback:
        message = render_template(
            fallback,
            {
                "filename": str(APP_TEXTS_DIR / name),
            },
        )
    else:
        message = f"Error de configuraciÃ³n: falta {APP_TEXTS_DIR / name}"

    raise RuntimeError(message)

def render_template(template: str, values: dict[str, str]) -> str:
    """Very simple {{placeholder}} replacement."""
    rendered = template

    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)

    return rendered

def save_wealth_log(user_input: str, ai_answer: str, usage: dict) -> None:
    """Save a trace of a model-generated answer."""
    timestamp = format_app_minute()

    template = load_required_app_text("wealth_log_entry.md")

    entry = render_template(
        template,
        {
            "timestamp": timestamp,
            "active_client_name": current_client_name(),
            "user_input": user_input,
            "model": str(usage.get("model", GEMINI_MODEL)),
            "input_tokens": str(usage.get("input_tokens", 0)),
            "output_tokens": str(usage.get("output_tokens", 0)),
            "total_tokens": str(usage.get("total_tokens", 0)),
            "estimated_cost_usd": f"{usage.get('estimated_cost_usd', 0):.6f}",
            "ai_answer": ai_answer,
        },
    )

    append_text_file(wealth_log_file(), entry)

def process_with_gemini_orchestrator(text_to_process: str, source: str) -> str:
    """
    Gemini orchestrator.

    It updates:
    - quien_soy.md
    - que_quiero.md
    - que_tengo_que_hacer.md

    It also saves:
    - agent observations
    - follow-up triggers

    And returns the client-facing answer.
    """
    ensure_client_files()

    client_context = load_client_context()
    wealth_knowledge = load_wealth_knowledge()
    global_agent_config = load_agent_config_files()
    client_agent_config = load_client_agent_config()

    pending_followups_context = format_pending_followups_for_prompt()

    current_date = today_app().strftime("%Y-%m-%d")

    system_prompt = load_required_app_text("orchestrator_system_prompt.md")
    prompt_template = load_required_app_text("orchestrator_user_prompt.md")

    prompt = render_template(
        prompt_template,
        {
            "text_to_process": text_to_process,
            "source": source,
            "current_date": current_date,
            "quien_soy": client_context["quien_soy"],
            "que_quiero": client_context["que_quiero"],
            "que_tengo_que_hacer": client_context["que_tengo_que_hacer"],
            "estilo_respuesta": client_context["estilo_respuesta"],
            "agent_config": client_agent_config,
            "global_agent_config": global_agent_config,
            "wealth_knowledge": wealth_knowledge,
            "pending_followups": pending_followups_context,
        },
    )

    try:
        raw_answer, usage = llm_generate(prompt=prompt, system_prompt=system_prompt)

    except errors.ServerError as error:
        timestamp = format_app_minute()

        log_entry = render_template(
            load_required_app_text("orchestrator_server_error_log.md"),
            {
                "timestamp": timestamp,
                "error": str(error),
                "text_to_process": text_to_process,
            },
        )

        append_text_file(wealth_log_file(), log_entry)

        return load_required_app_text("orchestrator_server_error_reply.md")

    except Exception as error:
        timestamp = format_app_minute()

        log_entry = render_template(
            load_required_app_text("orchestrator_unexpected_error_log.md"),
            {
                "timestamp": timestamp,
                "error": str(error),
                "text_to_process": text_to_process,
            },
        )

        append_text_file(wealth_log_file(), log_entry)

        return load_required_app_text("orchestrator_unexpected_error_reply.md")

    try:
        parsed = extract_json_from_text(raw_answer)

    except Exception as first_error:
        timestamp = format_app_minute()

        warning_log_entry = render_template(
            load_required_app_text("orchestrator_json_parse_warning_log.md"),
            {
                "timestamp": timestamp,
                "first_error": str(first_error),
                "raw_answer": raw_answer,
            },
        )

        append_text_file(wealth_log_file(), warning_log_entry)

        try:
            parsed = repair_json_with_gemini(raw_answer)

            success_log_entry = render_template(
                load_required_app_text("orchestrator_json_repair_success_log.md"),
                {
                    "timestamp": timestamp,
                },
            )

            append_text_file(wealth_log_file(), success_log_entry)

        except Exception as repair_error:
            failure_log_entry = render_template(
                load_required_app_text("orchestrator_json_failure_log.md"),
                {
                    "timestamp": timestamp,
                    "first_error": str(first_error),
                    "repair_error": str(repair_error),
                    "raw_answer": raw_answer,
                },
            )

            append_text_file(wealth_log_file(), failure_log_entry)

            return load_required_app_text("orchestrator_json_failure_reply.md")

    required_keys = [
        "quien_soy",
        "que_quiero",
        "que_tengo_que_hacer",
        "respuesta_cliente",
        "proxima_accion",
        "agent_observations",
        "followup_triggers",
        "notas_auditoria",
    ]

    missing_keys = [key for key in required_keys if key not in parsed]

    if missing_keys:
        missing_keys_text = "\n".join(f"- {key}" for key in missing_keys)

        return render_template(
            load_required_app_text("orchestrator_missing_keys_reply.md"),
            {
                "missing_keys": missing_keys_text,
            },
        )

    write_client_file_with_backup(client_files()["quien_soy"], parsed["quien_soy"])
    write_client_file_with_backup(client_files()["que_quiero"], parsed["que_quiero"])
    write_client_file_with_backup(
        client_files()["que_tengo_que_hacer"],
        parsed["que_tengo_que_hacer"],
    )

    agent_observations = parsed.get("agent_observations", {})

    if isinstance(agent_observations, dict):
        append_agent_observation(
            source=source,
            user_input=text_to_process,
            observations=agent_observations,
        )

    new_followup_triggers = parsed.get("followup_triggers", [])

    if isinstance(new_followup_triggers, list) and new_followup_triggers:
        existing_triggers = load_followup_triggers()

        timestamp = format_app_datetime()
        id_timestamp = now_app().strftime("%Y%m%d_%H%M%S")

        normalized_triggers: list[dict] = []

        date_override = infer_followup_date_from_user_text(
            user_text=text_to_process,
            current_date_text=current_date,
        )
        
        for index, trigger in enumerate(new_followup_triggers, start=1):
            if not isinstance(trigger, dict):
                continue

            normalized_trigger = {
                "id": f"followup_{id_timestamp}_{index}",
                "client_id": current_client_name(),
                "created_at": str(trigger.get("created_at") or timestamp),
                "date": str(date_override or trigger.get("date") or ""),
                "type": normalize_followup_type(
                    raw_type=str(trigger.get("type") or "general_checkin"),
                    message_template=str(trigger.get("message_template") or ""),
                    reason=str(trigger.get("reason") or ""),
                ),
                "message_template": str(trigger.get("message_template") or ""),
                "reason": str(trigger.get("reason") or ""),
                "sensitivity": str(trigger.get("sensitivity") or "low"),
                "requires_private_context": bool(trigger.get("requires_private_context", True)),
                "status": str(trigger.get("status") or "pending").lower(),
                "source": source,
            }

            if normalized_trigger["message_template"]:
                if is_similar_pending_followup(normalized_trigger, existing_triggers + normalized_triggers):
                    append_proactivity_log(
                        event_type="followup_duplicate_skipped",
                        trigger=normalized_trigger,
                        notes="Skipped because a similar pending follow-up already exists.",
                    )
                    continue
                
                normalized_triggers.append(normalized_trigger)

        if normalized_triggers:
            save_followup_triggers(existing_triggers + normalized_triggers)

            for trigger in normalized_triggers:
                append_proactivity_log(
                    event_type="followup_created",
                    trigger=trigger,
                    notes="Created by Gemini orchestrator from client interaction.",
                )

    timestamp = format_app_minute()

    historial_template = load_required_app_text("historial_interaction_entry.md")

    historial_entry = render_template(
        historial_template,
        {
            "timestamp": timestamp,
            "source": source,
            "text_to_process": text_to_process,
            "respuesta_cliente": parsed["respuesta_cliente"],
            "proxima_accion": parsed["proxima_accion"],
            "notas_auditoria": parsed["notas_auditoria"],
            "model": str(usage.get("model", GEMINI_MODEL)),
            "input_tokens": str(usage.get("input_tokens", 0)),
            "output_tokens": str(usage.get("output_tokens", 0)),
            "total_tokens": str(usage.get("total_tokens", 0)),
            "estimated_cost_usd": f"{usage.get('estimated_cost_usd', 0):.6f}",
        },
    )

    append_text_file(
        client_files()["historial_interacciones"],
        historial_entry,
    )

    save_wealth_log(
        user_input=text_to_process,
        ai_answer=parsed["respuesta_cliente"],
        usage=usage,
    )

    final_reply_template = load_required_app_text("orchestrator_final_reply.md")

    return render_template(
        final_reply_template,
        {
            "respuesta_cliente": parsed["respuesta_cliente"],
            "proxima_accion": parsed["proxima_accion"],
            "gemini_usage_note": format_usage_note(usage),
        },
    )

# ---------------------------------------------------------------------
# Gemini helper
# ---------------------------------------------------------------------

def gemini_llm(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """Send a prompt to Gemini and return answer text plus usage metadata."""
    if gemini_client is None:
        raise RuntimeError(load_required_app_text("gemini_not_configured_error.md"))

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

def deepseek_llm(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """Send a prompt to DeepSeek and return answer text plus usage metadata."""
    if deepseek_client is None:
        raise RuntimeError("DeepSeek API key is not configured.")

    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    response = deepseek_client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=messages,
        temperature=0,
    )

    answer = response.choices[0].message.content or ""

    usage = getattr(response, "usage", None)

    input_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
    output_tokens = getattr(usage, "completion_tokens", 0) if usage else 0
    total_tokens = getattr(usage, "total_tokens", input_tokens + output_tokens) if usage else 0

    estimated_cost_usd = (
        (input_tokens / 1_000_000) * DEEPSEEK_INPUT_PRICE_PER_1M
        + (output_tokens / 1_000_000) * DEEPSEEK_OUTPUT_PRICE_PER_1M
    )

    metadata = {
        "provider": "deepseek",
        "model": DEEPSEEK_MODEL,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "estimated_cost_usd": estimated_cost_usd,
    }

    return answer, metadata


def llm_generate(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """
    Generate with the configured provider order.

    Default:
    LLM_PROVIDER_ORDER=deepseek,gemini
    """
    last_error: Exception | None = None

    for provider in LLM_PROVIDER_ORDER:
        try:
            if provider == "deepseek":
                return deepseek_llm(prompt=prompt, system_prompt=system_prompt)

            if provider == "gemini":
                raw_answer, usage = gemini_llm(prompt=prompt, system_prompt=system_prompt)
                usage["provider"] = "gemini"
                return raw_answer, usage

            raise RuntimeError(f"Unknown LLM provider: {provider}")

        except Exception as error:
            last_error = error

            append_text_file(
                wealth_log_file(),
                "\n".join(
                    [
                        f"## {format_app_minute()}",
                        "",
                        "### LLM provider failed",
                        "",
                        f"Provider: {provider}",
                        "",
                        f"Error: {str(error)}",
                        "",
                        "---",
                        "",
                    ]
                ),
            )

            continue

    raise RuntimeError(f"All LLM providers failed. Last error: {last_error}")


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
    repair_system_prompt = load_required_app_text("json_repair_system_prompt.md")
    repair_prompt_template = load_required_app_text("json_repair_user_prompt.md")

    repair_prompt = render_template(
        repair_prompt_template,
        {
            "raw_text": raw_text,
        },
    )

    repaired_answer, _usage = llm_generate(
        prompt=repair_prompt,
        system_prompt=repair_system_prompt,
    )

    return extract_json_from_text(repaired_answer)

def format_usage_note(usage: dict) -> str:
    """Small cost note appended to Telegram answers during development."""
    if not SHOW_USAGE_NOTE:
        return ""

    template = load_required_app_text("usage_note.md")

    return render_template(
        template,
        {
            "provider": str(usage.get("provider", "unknown")),
            "model": str(usage.get("model", GEMINI_MODEL)),
            "input_tokens": str(usage.get("input_tokens", 0)),
            "output_tokens": str(usage.get("output_tokens", 0)),
            "total_tokens": str(usage.get("total_tokens", 0)),
            "estimated_cost_usd": f"{usage.get('estimated_cost_usd', 0):.6f}",
        },
    )

async def send_long_message(
    update: Update,
    text: str,
    reply_markup=None,
    chunk_size: int = 3500,
) -> None:
    """Send long Telegram messages in safe chunks."""
    if not text:
        empty_response_message = load_required_app_text("empty_response_message.md")

        await update.message.reply_text(
            empty_response_message,
            reply_markup=reply_markup,
        )
        return

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    for index, chunk in enumerate(chunks):
        if index == len(chunks) - 1:
            await update.message.reply_text(
                chunk,
                reply_markup=reply_markup,
            )
        else:
            await update.message.reply_text(chunk)

# ---------------------------------------------------------------------
# Telegram handlers
# ---------------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()

    remember_chat_id(update)

    template = load_required_app_text("start_message.md")

    message = render_template(
        template,
        {
            "active_client_name": current_client_name(),
        },
    )

    await update.message.reply_text(
        message,
        reply_markup=MAIN_KEYBOARD,
    )


async def show_quien_soy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()
    await send_long_message(update, read_text_file(client_files()["quien_soy"]), reply_markup=MAIN_KEYBOARD)


async def show_que_quiero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()
    await send_long_message(update, read_text_file(client_files()["que_quiero"]), reply_markup=MAIN_KEYBOARD)


async def show_que_tengo_que_hacer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()
    await send_long_message(update, read_text_file(client_files()["que_tengo_que_hacer"]), reply_markup=MAIN_KEYBOARD)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    context.user_data.clear()

    message = load_required_app_text("cancel_message.md")

    await update.message.reply_text(
        message,
        reply_markup=MAIN_KEYBOARD,
    )

async def handle_free_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()

    remember_chat_id(update)

    user_text = update.message.text.strip()

    thinking_text = load_required_app_text("thinking_message.md")

    thinking_message = await update.message.reply_text(
        thinking_text,
        reply_markup=MAIN_KEYBOARD,
    )

    try:
        source_label = load_required_app_text("free_text_source_label.md")

        orchestrator_result = process_with_gemini_orchestrator(
            text_to_process=user_text,
            source=source_label,
        )

    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        error_template = load_required_app_text("processing_error_message.md")

        error_message = render_template(
            error_template,
            {
                "error": str(error),
            },
        )

        await update.message.reply_text(
            error_message,
            reply_markup=MAIN_KEYBOARD,
        )
        return

    try:
        await thinking_message.delete()
    except Exception:
        pass

    await send_long_message(
        update,
        orchestrator_result,
        reply_markup=MAIN_KEYBOARD,
    )

async def show_followups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    pending = get_pending_followup_triggers()

    if not pending:
        await update.message.reply_text(
            load_required_app_text("followups_empty_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    header = load_required_app_text("followups_list_header.md")
    item_template = load_required_app_text("followups_item_template.md")

    default_date = load_required_app_text("followups_default_date.md")
    default_type = load_required_app_text("followups_default_type.md")
    default_message = load_required_app_text("followups_default_message.md")
    default_status = load_required_app_text("followups_default_status.md")

    items: list[str] = []

    for index, trigger in enumerate(pending, start=1):
        item = render_template(
            item_template,
            {
                "index": str(index),
                "date": str(trigger.get("date", default_date)),
                "type": str(trigger.get("type", default_type)),
                "message_template": str(trigger.get("message_template", default_message)),
                "status": str(trigger.get("status", default_status)),
            },
        )

        items.append(item)

    await send_long_message(
        update,
        header + "\n\n" + "\n\n".join(items),
        reply_markup=MAIN_KEYBOARD,
    )

async def show_due_followups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    triggers = load_followup_triggers()
    today = today_app()

    due: list[dict] = []

    for trigger in triggers:
        status = str(trigger.get("status", "pending")).lower()

        if status != "pending":
            continue

        trigger_date = parse_followup_date(str(trigger.get("date", "")))

        if trigger_date is None:
            continue

        if trigger_date <= today:
            due.append(trigger)

    if not due:
        await update.message.reply_text(
            "No hay follow-ups vencidos para enviar ahora.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    header = "Follow-ups vencidos:"
    item_template = load_required_app_text("followups_item_template.md")

    default_date = load_required_app_text("followups_default_date.md")
    default_type = load_required_app_text("followups_default_type.md")
    default_message = load_required_app_text("followups_default_message.md")
    default_status = load_required_app_text("followups_default_status.md")

    items: list[str] = []

    for index, trigger in enumerate(due, start=1):
        item = render_template(
            item_template,
            {
                "index": str(index),
                "date": str(trigger.get("date", default_date)),
                "type": str(trigger.get("type", default_type)),
                "message_template": str(trigger.get("message_template", default_message)),
                "status": str(trigger.get("status", default_status)),
            },
        )

        items.append(item)

    await send_long_message(
        update,
        header + "\n\n" + "\n\n".join(items),
        reply_markup=MAIN_KEYBOARD,
    )


async def scheduler_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    triggers = load_followup_triggers()
    today = today_app()
    chat_id = get_remembered_chat_id()

    pending_count = 0
    due_count = 0
    invalid_date_count = 0

    for trigger in triggers:
        status = str(trigger.get("status", "pending")).lower()

        if status != "pending":
            continue

        pending_count += 1

        trigger_date = parse_followup_date(str(trigger.get("date", "")))

        if trigger_date is None:
            invalid_date_count += 1
            continue

        if trigger_date <= today:
            due_count += 1

    chat_status = "sÃ­" if chat_id is not None else "no"

    message = "\n".join(
        [
            "Estado del scheduler:",
            "",
            f"- Scheduler activo: sÃ­",
            f"- Hora diaria: {PROACTIVE_SCHEDULER_HOUR:02d}:{PROACTIVE_SCHEDULER_MINUTE:02d} {APP_TIMEZONE}",
            f"- Chat ID recordado: {chat_status}",
            f"- Follow-ups pendientes: {pending_count}",
            f"- Follow-ups vencidos: {due_count}",
            f"- Follow-ups con fecha invÃ¡lida: {invalid_date_count}",
        ]
    )

    await update.message.reply_text(
        message,
        reply_markup=MAIN_KEYBOARD,
    )


async def show_all_followups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    triggers = load_followup_triggers()

    if not triggers:
        await update.message.reply_text(
            load_required_app_text("all_followups_empty_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    header = load_required_app_text("all_followups_list_header.md")
    item_template = load_required_app_text("all_followups_item_template.md")

    default_date = load_required_app_text("followups_default_date.md")
    default_type = load_required_app_text("followups_default_type.md")
    default_message = load_required_app_text("followups_default_message.md")
    default_status = load_required_app_text("followups_default_status.md")
    default_sent_at = load_required_app_text("all_followups_default_sent_at.md")

    items: list[str] = []

    for index, trigger in enumerate(triggers, start=1):
        item = render_template(
            item_template,
            {
                "index": str(index),
                "date": str(trigger.get("date", default_date)),
                "type": str(trigger.get("type", default_type)),
                "status": str(trigger.get("status", default_status)),
                "message_template": str(trigger.get("message_template", default_message)),
                "created_at": str(trigger.get("created_at", "")),
                "sent_at": str(trigger.get("sent_at", default_sent_at)),
                "reason": str(trigger.get("reason", "")),
            },
        )

        items.append(item)

    await send_long_message(
        update,
        header + "\n\n" + "\n\n".join(items),
        reply_markup=MAIN_KEYBOARD,
    )

async def mark_followup_done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    if not context.args:
        usage_template = load_required_app_text("followup_command_usage_message.md")
        message = render_template(
            usage_template,
            {
                "command": "/followup_done",
            },
        )

        await update.message.reply_text(
            message,
            reply_markup=MAIN_KEYBOARD,
        )
        return

    try:
        selected_index = int(context.args[0])
    except ValueError:
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    triggers = load_followup_triggers()

    pending_positions = [
        index for index, trigger in enumerate(triggers)
        if str(trigger.get("status", "pending")).lower() == "pending"
    ]

    if selected_index < 1 or selected_index > len(pending_positions):
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    trigger_position = pending_positions[selected_index - 1]

    completed_trigger = triggers[trigger_position]
    completed_trigger["status"] = "completed"
    completed_trigger["completed_at"] = format_app_datetime()

    append_proactivity_log(
        event_type="followup_completed",
        trigger=completed_trigger,
        notes="Marked completed manually via /followup_done.",
    )

    save_followup_triggers(triggers)

    await update.message.reply_text(
        load_required_app_text("followup_done_success_message.md"),
        reply_markup=MAIN_KEYBOARD,
    )

async def delete_followup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    if not context.args:
        usage_template = load_required_app_text("followup_command_usage_message.md")
        message = render_template(
            usage_template,
            {
                "command": "/delete_followup",
            },
        )

        await update.message.reply_text(
            message,
            reply_markup=MAIN_KEYBOARD,
        )
        return

    try:
        selected_index = int(context.args[0])
    except ValueError:
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    triggers = load_followup_triggers()

    pending_positions = [
        index for index, trigger in enumerate(triggers)
        if str(trigger.get("status", "pending")).lower() == "pending"
    ]

    if selected_index < 1 or selected_index > len(pending_positions):
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    trigger_position = pending_positions[selected_index - 1]
    deleted_trigger = triggers[trigger_position]

    append_proactivity_log(
        event_type="followup_deleted",
        trigger=deleted_trigger,
        notes="Deleted manually via /delete_followup.",
    )

    del triggers[trigger_position]

    save_followup_triggers(triggers)

    await update.message.reply_text(
        load_required_app_text("followup_delete_success_message.md"),
        reply_markup=MAIN_KEYBOARD,
    )

async def snooze_followup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_followup_triggers_file()

    if len(context.args) < 2:
        await update.message.reply_text(
            "Uso: /followup_snooze 1 maÃ±ana | /followup_snooze 1 semana | /followup_snooze 1 YYYY-MM-DD",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    try:
        selected_index = int(context.args[0])
    except ValueError:
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    new_date = parse_snooze_date(" ".join(context.args[1:]))

    if new_date is None:
        await update.message.reply_text(
            "No he entendido la nueva fecha. Use: maÃ±ana, semana, mes o YYYY-MM-DD.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    triggers = load_followup_triggers()

    pending_positions = [
        index for index, trigger in enumerate(triggers)
        if str(trigger.get("status", "pending")).lower() == "pending"
    ]

    if selected_index < 1 or selected_index > len(pending_positions):
        await update.message.reply_text(
            load_required_app_text("followup_invalid_index_message.md"),
            reply_markup=MAIN_KEYBOARD,
        )
        return

    trigger_position = pending_positions[selected_index - 1]
    snoozed_trigger = triggers[trigger_position]

    old_date = str(snoozed_trigger.get("date", ""))
    new_date_text = new_date.strftime("%Y-%m-%d")

    snoozed_trigger["date"] = new_date_text
    snoozed_trigger["status"] = "pending"
    snoozed_trigger["snoozed_at"] = format_app_datetime()
    snoozed_trigger["previous_date"] = old_date

    append_proactivity_log(
        event_type="followup_snoozed",
        trigger=snoozed_trigger,
        notes=f"Snoozed manually via /followup_snooze from {old_date} to {new_date_text}.",
    )

    save_followup_triggers(triggers)

    await update.message.reply_text(
        f"Follow-up pospuesto a {new_date_text}.",
        reply_markup=MAIN_KEYBOARD,
    )


async def send_due_followups(reply_text_func, notes: str) -> dict:
    """
    Send all pending follow-ups whose date is today or earlier.

    This is reusable:
    - /run_followups can call it manually.
    - a future automatic scheduler can call it daily.
    """
    ensure_followup_triggers_file()

    triggers = load_followup_triggers()
    today = today_app()

    sent_count = 0
    has_invalid_dates = False

    for trigger in triggers:
        status = str(trigger.get("status", "pending")).lower()

        if status != "pending":
            continue

        trigger_date = parse_followup_date(str(trigger.get("date", "")))

        if trigger_date is None:
            has_invalid_dates = True
            continue

        if trigger_date > today:
            continue

        message_template = str(trigger.get("message_template", "")).strip()

        if not message_template:
            continue

        await reply_text_func(message_template)

        trigger["status"] = "sent"
        trigger["sent_at"] = format_app_datetime()

        append_proactivity_log(
            event_type="followup_sent",
            trigger=trigger,
            notes=notes,
        )

        sent_count += 1

    save_followup_triggers(triggers)

    return {
        "sent_count": sent_count,
        "has_invalid_dates": has_invalid_dates,
    }


async def run_followups(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    async def reply_text(text: str) -> None:
        await update.message.reply_text(
            text,
            reply_markup=MAIN_KEYBOARD,
        )
    
    activate_client_from_update(update)

    result = await send_due_followups(
        reply_text_func=reply_text,
        notes="Sent manually via /run_followups.",
    )

    sent_count = result["sent_count"]
    has_invalid_dates = result["has_invalid_dates"]

    if sent_count == 0:
        message = load_required_app_text("run_followups_no_due_message.md")

        if has_invalid_dates:
            message += "\n\n" + load_required_app_text("run_followups_invalid_date_message.md")

        await update.message.reply_text(
            message,
            reply_markup=MAIN_KEYBOARD,
        )
        return

    summary_template = load_required_app_text("run_followups_sent_summary.md")

    summary_message = render_template(
        summary_template,
        {
            "count": str(sent_count),
        },
    )

    await update.message.reply_text(
        summary_message,
        reply_markup=MAIN_KEYBOARD,
    )


async def scheduled_run_followups(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Daily automatic follow-up check for all Telegram client folders."""
    client_names = iter_telegram_client_names()

    try:
        if not client_names:
            set_current_client_name(DEFAULT_CLIENT_NAME)

            append_text_file(
                wealth_log_file(),
                "\n".join(
                    [
                        f"## {format_app_minute()}",
                        "",
                        "### Scheduler",
                        "",
                        "No Telegram client folders found. Automatic follow-ups were not sent.",
                        "",
                        "---",
                        "",
                    ]
                ),
            )
            return

        for client_name in client_names:
            set_current_client_name(client_name)
            ensure_client_files()
            ensure_followup_triggers_file()

            chat_id = get_remembered_chat_id()

            if chat_id is None:
                append_text_file(
                    wealth_log_file(),
                    "\n".join(
                        [
                            f"## {format_app_minute()}",
                            "",
                            "### Scheduler",
                            "",
                            "No Telegram chat ID remembered for this client. Automatic follow-ups were not sent.",
                            f"Client: {client_name}",
                            "",
                            "---",
                            "",
                        ]
                    ),
                )
                continue

            async def send_text(text: str, target_chat_id: int = chat_id) -> None:
                await context.bot.send_message(
                    chat_id=target_chat_id,
                    text=text,
                    reply_markup=MAIN_KEYBOARD,
                )

            result = await send_due_followups(
                reply_text_func=send_text,
                notes="Sent automatically by daily scheduler.",
            )

            append_text_file(
                wealth_log_file(),
                "\n".join(
                    [
                        f"## {format_app_minute()}",
                        "",
                        "### Scheduler",
                        "",
                        "Automatic follow-up check completed for client.",
                        f"Client: {client_name}",
                        f"Sent count: {result['sent_count']}",
                        f"Invalid dates present: {result['has_invalid_dates']}",
                        "",
                        "---",
                        "",
                    ]
                ),
            )

    finally:
        set_current_client_name(DEFAULT_CLIENT_NAME)


def append_proactivity_log(
    event_type: str,
    trigger: dict,
    notes: str = "",
) -> None:
    """Append a proactive-agent event to proactivity_log.md."""
    ensure_client_files()

    timestamp = format_app_datetime()

    template = load_required_app_text("proactivity_log_entry.md")

    entry = render_template(
        template,
        {
            "timestamp": timestamp,
            "event_type": event_type,
            "followup_id": str(trigger.get("id", "")),
            "followup_type": str(trigger.get("type", "")),
            "followup_date": str(trigger.get("date", "")),
            "status": str(trigger.get("status", "")),
            "message_template": str(trigger.get("message_template", "")),
            "notes": notes,
        },
    )

    append_text_file(client_files()["proactivity_log"], entry)

async def show_proactivity_log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()

    log_text = read_text_file(client_files()["proactivity_log"])

    if not log_text:
        log_text = load_required_app_text("proactivity_log_empty_message.md")

    await send_long_message(
        update,
        log_text,
        reply_markup=MAIN_KEYBOARD,
    )

async def show_agent_observations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()

    observations = read_text_file(client_files()["agent_observations"])

    if not observations:
        observations = load_required_app_text("agent_observations_empty_message.md")

    await send_long_message(
        update,
        observations,
        reply_markup=MAIN_KEYBOARD,
    )

# ---------------------------------------------------------------------
# App
# ---------------------------------------------------------------------

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    if app.job_queue is None:
        raise RuntimeError(
            "JobQueue is not available. Install it with: pip install \"python-telegram-bot[job-queue]\""
        )
    
    app.job_queue.run_daily(
        scheduled_run_followups,
        time=time(
            hour=PROACTIVE_SCHEDULER_HOUR,
            minute=PROACTIVE_SCHEDULER_MINUTE,
            tzinfo=ZoneInfo(APP_TIMEZONE),
        ),
        name="daily_followup_scheduler",
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("followups", show_followups))
    app.add_handler(CommandHandler("due_followups", show_due_followups))
    app.add_handler(CommandHandler("scheduler_status", scheduler_status))
    app.add_handler(CommandHandler("all_followups", show_all_followups))
    app.add_handler(CommandHandler("proactivity_log", show_proactivity_log))
    app.add_handler(CommandHandler("followup_done", mark_followup_done))
    app.add_handler(CommandHandler("delete_followup", delete_followup))
    app.add_handler(CommandHandler("followup_snooze", snooze_followup))
    app.add_handler(CommandHandler("run_followups", run_followups))
    app.add_handler(CommandHandler("agent_observations", show_agent_observations))

    app.add_handler(MessageHandler(filters.Regex(r"^Cancelar$"), cancel))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ‘¤ Resumen de quiÃ©n soy yo$"), show_quien_soy))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸŽ¯ Resumen de quÃ© quiero$"), show_que_quiero))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ§­ Resumen de quÃ© tengo que hacer$"), show_que_tengo_que_hacer))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_free_text))

    app.run_polling()


if __name__ == "__main__":
    main()

