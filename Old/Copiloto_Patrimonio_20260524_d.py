import os
import json

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

WEALTH_KNOWLEDGE_DIR = Path("Wealth_Knowledge")
AGENT_CONFIG_DIR = Path("AgentConfig")
INTERVENTION_PATTERNS_DIR = AGENT_CONFIG_DIR / "InterventionPatterns"
INITIAL_CLIENT_FILES_DIR = Path("InitialClientFiles")
APP_TEXTS_DIR = Path("AppTexts")

CLIENTS_DIR = Path("ClientData")
ACTIVE_CLIENT_NAME = os.getenv("ACTIVE_CLIENT_NAME", "Cliente1")
ACTIVE_CLIENT_DIR = CLIENTS_DIR / ACTIVE_CLIENT_NAME

CLIENT_FILES = {
    "quien_soy": ACTIVE_CLIENT_DIR / "quien_soy.md",
    "que_quiero": ACTIVE_CLIENT_DIR / "que_quiero.md",
    "que_tengo_que_hacer": ACTIVE_CLIENT_DIR / "que_tengo_que_hacer.md",
    "estilo_respuesta": ACTIVE_CLIENT_DIR / "estilo_respuesta.md",
    "agent_config": ACTIVE_CLIENT_DIR / "agent_config.md",
    "agent_observations": ACTIVE_CLIENT_DIR / "agent_observations.md",
    "historial_interacciones": ACTIVE_CLIENT_DIR / "historial_interacciones.md",
}

WEALTH_LOG_FILE = ACTIVE_CLIENT_DIR / "wealth_logs.md"
FOLLOWUP_TRIGGERS_FILE = ACTIVE_CLIENT_DIR / "followup_triggers.json"

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

def ensure_client_files() -> None:
    """Create the active client folder and starter Markdown files if needed."""
    ACTIVE_CLIENT_DIR.mkdir(parents=True, exist_ok=True)

    for key, path in CLIENT_FILES.items():
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

def ensure_followup_triggers_file() -> None:
    """Create followup_triggers.json if it does not exist."""
    FOLLOWUP_TRIGGERS_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not FOLLOWUP_TRIGGERS_FILE.exists():
        FOLLOWUP_TRIGGERS_FILE.write_text("[]\n", encoding="utf-8")


def load_followup_triggers() -> list[dict]:
    """Load proactive follow-up triggers from JSON."""
    ensure_followup_triggers_file()

    try:
        content = FOLLOWUP_TRIGGERS_FILE.read_text(encoding="utf-8").strip()

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
    FOLLOWUP_TRIGGERS_FILE.parent.mkdir(parents=True, exist_ok=True)

    FOLLOWUP_TRIGGERS_FILE.write_text(
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

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

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

    append_text_file(CLIENT_FILES["agent_observations"], entry)

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
    return read_text_file(CLIENT_FILES["agent_config"])

def load_client_context() -> dict[str, str]:
    """Load all live Markdown files for the active client."""
    ensure_client_files()
    return {key: read_text_file(path) for key, path in CLIENT_FILES.items()}

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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    template = load_required_app_text("wealth_log_entry.md")

    entry = render_template(
        template,
        {
            "timestamp": timestamp,
            "active_client_name": ACTIVE_CLIENT_NAME,
            "user_input": user_input,
            "model": str(usage.get("model", GEMINI_MODEL)),
            "input_tokens": str(usage.get("input_tokens", 0)),
            "output_tokens": str(usage.get("output_tokens", 0)),
            "total_tokens": str(usage.get("total_tokens", 0)),
            "estimated_cost_usd": f"{usage.get('estimated_cost_usd', 0):.6f}",
            "ai_answer": ai_answer,
        },
    )

    append_text_file(WEALTH_LOG_FILE, entry)

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

    current_date = datetime.now().strftime("%Y-%m-%d")

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
        },
    )

    try:
        raw_answer, usage = gemini_llm(prompt=prompt, system_prompt=system_prompt)

    except errors.ServerError as error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        log_entry = render_template(
            load_required_app_text("orchestrator_server_error_log.md"),
            {
                "timestamp": timestamp,
                "error": str(error),
                "text_to_process": text_to_process,
            },
        )

        append_text_file(WEALTH_LOG_FILE, log_entry)

        return load_required_app_text("orchestrator_server_error_reply.md")

    except Exception as error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        log_entry = render_template(
            load_required_app_text("orchestrator_unexpected_error_log.md"),
            {
                "timestamp": timestamp,
                "error": str(error),
                "text_to_process": text_to_process,
            },
        )

        append_text_file(WEALTH_LOG_FILE, log_entry)

        return load_required_app_text("orchestrator_unexpected_error_reply.md")

    try:
        parsed = extract_json_from_text(raw_answer)

    except Exception as first_error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        warning_log_entry = render_template(
            load_required_app_text("orchestrator_json_parse_warning_log.md"),
            {
                "timestamp": timestamp,
                "first_error": str(first_error),
                "raw_answer": raw_answer,
            },
        )

        append_text_file(WEALTH_LOG_FILE, warning_log_entry)

        try:
            parsed = repair_json_with_gemini(raw_answer)

            success_log_entry = render_template(
                load_required_app_text("orchestrator_json_repair_success_log.md"),
                {
                    "timestamp": timestamp,
                },
            )

            append_text_file(WEALTH_LOG_FILE, success_log_entry)

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

            append_text_file(WEALTH_LOG_FILE, failure_log_entry)

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

    write_client_file_with_backup(CLIENT_FILES["quien_soy"], parsed["quien_soy"])
    write_client_file_with_backup(CLIENT_FILES["que_quiero"], parsed["que_quiero"])
    write_client_file_with_backup(
        CLIENT_FILES["que_tengo_que_hacer"],
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

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        normalized_triggers: list[dict] = []

        for index, trigger in enumerate(new_followup_triggers, start=1):
            if not isinstance(trigger, dict):
                continue

            normalized_trigger = {
                "id": str(trigger.get("id") or f"followup_{id_timestamp}_{index}"),
                "client_id": ACTIVE_CLIENT_NAME,
                "created_at": str(trigger.get("created_at") or timestamp),
                "date": str(trigger.get("date") or ""),
                "type": str(trigger.get("type") or "general_followup"),
                "message_template": str(trigger.get("message_template") or ""),
                "reason": str(trigger.get("reason") or ""),
                "sensitivity": str(trigger.get("sensitivity") or "low"),
                "requires_private_context": bool(trigger.get("requires_private_context", True)),
                "status": str(trigger.get("status") or "pending").lower(),
                "source": source,
            }

            if normalized_trigger["message_template"]:
                normalized_triggers.append(normalized_trigger)

        if normalized_triggers:
            save_followup_triggers(existing_triggers + normalized_triggers)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

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
        CLIENT_FILES["historial_interacciones"],
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
            "gemini_usage_note": format_gemini_usage_note(usage),
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

    repaired_answer, _usage = gemini_llm(
        prompt=repair_prompt,
        system_prompt=repair_system_prompt,
    )

    return extract_json_from_text(repaired_answer)

def format_gemini_usage_note(usage: dict) -> str:
    """Small cost note appended to Telegram answers during development."""
    template = load_required_app_text("gemini_usage_note.md")

    return render_template(
        template,
        {
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
    ensure_client_files()

    template = load_required_app_text("start_message.md")

    message = render_template(
        template,
        {
            "active_client_name": ACTIVE_CLIENT_NAME,
        },
    )

    await update.message.reply_text(
        message,
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

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()

    message = load_required_app_text("cancel_message.md")

    await update.message.reply_text(
        message,
        reply_markup=MAIN_KEYBOARD,
    )

async def handle_free_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()

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
    ensure_followup_triggers_file()

    triggers = load_followup_triggers()

    pending = [
        trigger for trigger in triggers
        if trigger.get("status", "pending") == "pending"
    ]

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

async def show_agent_observations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ensure_client_files()

    observations = read_text_file(CLIENT_FILES["agent_observations"])

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
    ensure_client_files()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("followups", show_followups))
    app.add_handler(CommandHandler("agent_observations", show_agent_observations))

    app.add_handler(MessageHandler(filters.Regex(r"^Cancelar$"), cancel))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ‘¤ Resumen de quiÃ©n soy yo$"), show_quien_soy))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸŽ¯ Resumen de quÃ© quiero$"), show_que_quiero))
    app.add_handler(MessageHandler(filters.Regex(r"^ðŸ§­ Resumen de quÃ© tengo que hacer$"), show_que_tengo_que_hacer))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_free_text))

    app.run_polling()


if __name__ == "__main__":
    main()

