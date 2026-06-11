import os
from datetime import datetime
from pathlib import Path

import ollama

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

load_dotenv()

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4:e4b-it-q4_K_M")

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["ðŸ§  Ask", "ðŸ’¼ Wealth"],
        ["ðŸ“¥ Inbox", "ðŸ“… Today"],
        ["âœï¸ Capture"],
    ],
    resize_keyboard=True,
    is_persistent=True,
)

ASKING, CAPTURING = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Jordi Agent is alive. Choose an action:",
        reply_markup=MAIN_KEYBOARD,
    )

INBOX_FILE = Path("SecondBrain_inbox.md")
PROMPTS_DIR = Path("prompts")

def load_prompt(*names: str) -> str:
    """
    Load one or more Markdown prompt files from the prompts folder
    and combine them into a single system prompt.
    """
    parts = []

    for name in names:
        path = PROMPTS_DIR / name

        if not path.exists():
            raise FileNotFoundError(f"Prompt file not found: {path}")

        parts.append(path.read_text(encoding="utf-8"))

    return "\n\n---\n\n".join(parts)


def local_llm(prompt: str, system_prompt: str | None = None) -> str:
    """
    Send a prompt to the local Ollama model and return the answer.
    """
    if system_prompt is None:
        system_prompt = (
            "You are Jordi Agent, a concise local assistant. "
            "Answer clearly and practically. "
            "Use English by default. "
            "When the user asks about tasks, suggest one tiny concrete next action."
        )

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return response["message"]["content"]

async def capture(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"\n- [{timestamp}] {user_message}\n"

    with INBOX_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)

    await update.message.reply_text("Captured. One less hidden bomb.")

async def inbox(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not INBOX_FILE.exists():
        await update.message.reply_text("Inbox is empty.")
        return

    lines = INBOX_FILE.read_text(encoding="utf-8").strip().splitlines()
    recent = lines[-10:]

    if not recent:
        await update.message.reply_text("Inbox is empty.")
        return

    await update.message.reply_text("Recent captures:\n" + "\n".join(recent))

async def wealth_placeholder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Wealth mode is connected as a button. The real wealth flow comes next.",
        reply_markup=MAIN_KEYBOARD,
    )

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not INBOX_FILE.exists():
        await update.message.reply_text("No captures today.")
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    lines = INBOX_FILE.read_text(encoding="utf-8").strip().splitlines()

    today_lines = [line for line in lines if f"[{today_str}" in line]

    if not today_lines:
        await update.message.reply_text("No captures today.")
        return

    await update.message.reply_text("Todayâ€™s captures:\n" + "\n".join(today_lines[-20:]))

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args).strip()

    if not prompt:
        await update.message.reply_text("Use: /ask your question")
        return

    await update.message.reply_text("Thinking...")

    try:
        answer = local_llm(prompt)
        await update.message.reply_text(answer[:3500])

    except Exception as e:
        await update.message.reply_text(f"Local LLM error: {e}")

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ðŸ“¥ Inbox":
        await inbox(update, context)
        return

    if text == "ðŸ“… Today":
        await today(update, context)
        return

    if text == "ðŸ§  Ask":
        await update.message.reply_text(
            "Send your question like this:\n/ask What is the next tiny action?",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    if text == "âœï¸ Capture":
        await update.message.reply_text(
            "Just send me the task or thought. I will capture it.",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    await capture(update, context)

async def ask_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "What do you want to ask Jordi Agent?"
    )
    return ASKING


async def capture_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "What should I capture?"
    )
    return CAPTURING

async def ask_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty question. Try again.")
        return ASKING

    await update.message.reply_text("Thinking...")

    try:
        answer = local_llm(prompt)
        await update.message.reply_text(answer[:3500], reply_markup=MAIN_KEYBOARD)

    except Exception as e:
        await update.message.reply_text(
            f"Local LLM error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def capture_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()

    if not user_message:
        await update.message.reply_text("Empty capture. Try again.")
        return CAPTURING

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n- [{timestamp}] {user_message}\n"

    with INBOX_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)

    await update.message.reply_text(
        "Captured. One less hidden bomb.",
        reply_markup=MAIN_KEYBOARD,
    )

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Cancelled.",
        reply_markup=MAIN_KEYBOARD,
    )
    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex("^ðŸ§  Ask$"), ask_start),
        MessageHandler(filters.Regex("^âœï¸ Capture$"), capture_start),
    ],
    states={
        ASKING: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, ask_message)
        ],
        CAPTURING: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, capture_message)
        ],
    },
    fallbacks=[
        CommandHandler("cancel", cancel)
    ],
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("inbox", inbox))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("cancel", cancel))

app.add_handler(conversation_handler)

app.add_handler(MessageHandler(filters.Regex("^ðŸ’¼ Wealth$"), wealth_placeholder))
app.add_handler(MessageHandler(filters.Regex("^ðŸ“¥ Inbox$"), inbox))
app.add_handler(MessageHandler(filters.Regex("^ðŸ“… Today$"), today))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture))

app.run_polling()
