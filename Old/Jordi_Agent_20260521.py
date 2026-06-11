import os
from datetime import datetime
from pathlib import Path
from turtle import update

import ollama
from google import genai
from google.genai import types

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
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["ðŸ§  Ask", "ðŸ’¼ Wealth"],
        ["ðŸ‘¤ Client Profile", "ðŸ¦ Platform Options"],
        ["ðŸ“Š Portfolio Parser", "âœ… Suitability Checklist"],
        ["ðŸ“ Investment Memo"],
        ["ðŸ“¥ Inbox", "ðŸ“… Today"],
        ["âœï¸ Capture"],
    ],
    resize_keyboard=True,
    is_persistent=True,
)

ASKING, CAPTURING, WEALTH, CLIENT_PROFILE, PLATFORM_OPTIONS, PORTFOLIO_PARSER, SUITABILITY_CHECKLIST, INVESTMENT_MEMO = range(8)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Jordi Agent is alive. Choose an action:",
        reply_markup=MAIN_KEYBOARD,
    )

INBOX_FILE = Path("SecondBrain_inbox.md")
WEALTH_LOG_FILE = Path("Wealth_Logs.md")
PROMPTS_DIR = Path("prompts")
WEALTH_KNOWLEDGE_DIR = Path("Wealth_Knowledge")

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

def load_wealth_knowledge() -> str:
    """
    Load all Markdown files from the Wealth_Knowledge folder
    and combine them into one knowledge context.
    Simple v18 version: no search, no embeddings, no database.
    """
    if not WEALTH_KNOWLEDGE_DIR.exists():
        return ""

    parts = []

    for path in sorted(WEALTH_KNOWLEDGE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8").strip()

        if content:
            parts.append(
                f"# Source file: {path.name}\n\n{content}"
            )

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

def gemini_llm(prompt: str, system_prompt: str | None = None) -> tuple[str, dict]:
    """
    Send a prompt to Gemini and return:
    - answer text
    - usage/cost metadata
    """
    if gemini_client is None:
        raise RuntimeError("Gemini client is not configured. Check GEMINI_API_KEY in .env.")

    config = None
    if system_prompt:
        config = types.GenerateContentConfig(
            system_instruction=system_prompt
        )

    response = gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config,
    )

    usage = getattr(response, "usage_metadata", None)

    input_tokens = getattr(usage, "prompt_token_count", 0) if usage else 0
    output_tokens = getattr(usage, "candidates_token_count", 0) if usage else 0
    total_tokens = getattr(usage, "total_token_count", 0) if usage else 0

    # Adjust these prices to match the exact model you use.
    # Example: Gemini 3.1 Flash-Lite Preview standard pricing:
    input_price_per_1m = 0.1
    output_price_per_1m = 0.4

    estimated_cost_usd = (
        (input_tokens / 1_000_000) * input_price_per_1m
        + (output_tokens / 1_000_000) * output_price_per_1m
    )

    metadata = {
        "model": GEMINI_MODEL,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "estimated_cost_usd": estimated_cost_usd,
    }

    return response.text, metadata

async def gemini_ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args).strip()

    if not prompt:
        await update.message.reply_text("Use: /geminiask your question")
        return

    await update.message.reply_text("Thinking with Gemini...")

    try:
        answer, usage = gemini_llm(prompt)

        cost_note = (
            f"\n\n---\n"
            f"Gemini usage estimate:\n"
            f"Model: {usage['model']}\n"
            f"Input tokens: {usage['input_tokens']}\n"
            f"Output tokens: {usage['output_tokens']}\n"
            f"Total tokens: {usage['total_tokens']}\n"
            f"Estimated cost: ${usage['estimated_cost_usd']:.6f}"
        )

        await send_long_message(
            update,
            answer + cost_note,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Gemini error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

async def send_long_message(update: Update, text: str, reply_markup=None, chunk_size: int = 3500):
    """
    Send long Telegram messages in safe chunks.
    Telegram has a message length limit, so we split long answers.
    """
    if not text:
        await update.message.reply_text("Empty answer.", reply_markup=reply_markup)
        return

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    for index, chunk in enumerate(chunks):
        if index == len(chunks) - 1:
            await update.message.reply_text(chunk, reply_markup=reply_markup)
        else:
            await update.message.reply_text(chunk)

def save_wealth_log(user_input: str, ai_analysis: str):
    """
    Save each Wealth analysis to a Markdown log file
    for traceability and later review.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"""
## {timestamp}

### User input

{user_input}

### Model

{OLLAMA_MODEL}

### Prompt files

- base_rules.md
- wealth_policy.md
- client_profile_questions.md

### AI analysis

{ai_analysis}

---
"""

    with WEALTH_LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)

def format_gemini_usage_note(usage: dict) -> str:
    return (
        f"\n\n---\n"
        f"Gemini usage estimate:\n"
        f"Model: {usage['model']}\n"
        f"Input tokens: {usage['input_tokens']}\n"
        f"Output tokens: {usage['output_tokens']}\n"
        f"Total tokens: {usage['total_tokens']}\n"
        f"Estimated cost: ${usage['estimated_cost_usd']:.6f}"
    )

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
        answer, usage = gemini_llm(prompt)

        await send_long_message(
            update,
            answer + format_gemini_usage_note(usage),
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(f"Local LLM error: {e}")

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

async def wealth_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tell me the finance/portfolio case."
    )
    return WEALTH

async def client_profile_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tell me the client situation."
    )
    return CLIENT_PROFILE

async def platform_options_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tell me the client/platform situation."
    )
    return PLATFORM_OPTIONS

async def portfolio_parser_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Paste the portfolio description."
    )
    return PORTFOLIO_PARSER

async def suitability_checklist_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tell me the client situation for the pre-advice checklist."
    )
    return SUITABILITY_CHECKLIST

async def investment_memo_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tell me the product and client context for the investment memo."
    )
    return INVESTMENT_MEMO

async def wealth_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty wealth case. Try again.")
        return WEALTH

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        wealth_prompt = f"""
        Analyze this wealth-management case.

        Use exactly this structure:

        1. What the client seems to need
        2. What information is missing
        3. Questions to ask the client
        4. Possible options to compare
        5. Main risks or warnings
        6. Suggested next tiny action
        7. Reminder: this is not a recommendation

        Do not give investment recommendations.
        Do not say "I recommend", "you should buy", "you should sell", or "this is suitable".

        Local wealth knowledge:
        {wealth_knowledge}

        Client case:
        {prompt}
        """

        #answer = local_llm(wealth_prompt, system_prompt=system_prompt)
        answer, usage = gemini_llm(wealth_prompt, system_prompt=system_prompt)

        save_wealth_log(prompt, answer)

        await send_long_message(
            update,
            answer + format_gemini_usage_note(usage),
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Wealth mode error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def client_profile_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty client situation. Try again.")
        return CLIENT_PROFILE

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        profile_prompt = f"""
Generate a client profiling questionnaire for this finance/wealth-management case.

Use this structure:

1. Basic context
2. Investment objective
3. Time horizon
4. Liquidity needs
5. Financial situation
6. Capacity for loss
7. Willingness to take risk
8. Knowledge and experience
9. Existing portfolio
10. Preferences and constraints
11. Documents needed
12. Most urgent missing information
13. Suggested next tiny action
14. Reminder: this is not a recommendation

Do not recommend investments.
Only generate questions and missing-information checks.

Local wealth knowledge:
{wealth_knowledge}

Client situation:
{prompt}
"""

        answer = local_llm(profile_prompt, system_prompt=system_prompt)

        await send_long_message(
            update,
            answer,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Client Profile error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def platform_options_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty platform situation. Try again.")
        return PLATFORM_OPTIONS

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        platform_prompt = f"""
Compare platform or custody options for this finance/wealth-management case.

Use exactly this structure:

1. What operational problem the client seems to have
2. What information is missing
3. Platform categories to compare
4. Comparison criteria
5. Main operational risks or warnings
6. Questions to ask before choosing any platform
7. Suggested next tiny action
8. Reminder: this is not a recommendation

Platform categories may include:
- Traditional bank
- Private bank
- Online broker
- Fund platform
- Robo-advisor
- Indexed fund platform
- Money market / cash account route
- Treasury bills / short-term government debt route

Comparison criteria may include:
- Custody cost
- Trading cost
- Fund subscription/redemption cost
- Availability of clean share classes
- Availability of low-cost indexed funds
- Availability of ETFs
- Spanish tax reporting convenience
- Regulation / investor protection
- Minimum investment
- User experience
- Transfer friction
- Currency handling
- Operational risk

Do not recommend a specific platform.
Do not rank one platform as the final best choice.
Only explain categories, trade-offs, missing information, and questions to ask.

Local wealth knowledge:
{wealth_knowledge}

Client/platform situation:
{prompt}
"""

        answer = local_llm(platform_prompt, system_prompt=system_prompt)

        await send_long_message(
            update,
            answer,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Platform Options error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def portfolio_parser_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty portfolio description. Try again.")
        return PORTFOLIO_PARSER

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        portfolio_prompt = f"""
Analyze this simple portfolio description.

Use exactly this structure:

1. Allocation summary
2. Main concentration risks
3. Liquidity risks
4. Currency risks
5. Cost questions
6. Missing information
7. Questions before deciding anything
8. Suggested next tiny action
9. Reminder: this is not a recommendation

Rules:
- Do not recommend buying, selling, or holding anything.
- Do not optimize the portfolio.
- Do not say the portfolio is suitable.
- Do not propose final target weights.
- Only summarize, identify risks, identify missing data, and generate questions.
- If percentages do not add up to 100%, say so clearly.
- If asset classes are unclear, say what needs clarification.
- If currency exposure is unknown, say it is unknown.

Local wealth knowledge:
{wealth_knowledge}
Portfolio description:
{prompt}
"""

        answer = local_llm(portfolio_prompt, system_prompt=system_prompt)

        await send_long_message(
            update,
            answer,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Portfolio Parser error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def suitability_checklist_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty client situation. Try again.")
        return SUITABILITY_CHECKLIST

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        checklist_prompt = f"""
Generate a pre-advice suitability-style checklist for this finance/wealth-management case.

Important:
- Do not claim this is a formal legal suitability assessment.
- Do not recommend investments.
- Do not say any product is suitable.
- Only identify information to verify before a human advisor or client makes a decision.

Use exactly this structure:

1. Investment objective
2. Time horizon
3. Risk tolerance
4. Capacity for loss
5. Liquidity needs
6. Knowledge and experience
7. Existing exposure
8. Tax residence
9. ESG or sustainability preferences
10. Product restrictions
11. Documents needed
12. Red flags
13. Suggested next tiny action
14. Reminder: this is not a recommendation

Local wealth knowledge:
{wealth_knowledge}

Client situation:
{prompt}
"""

        answer = local_llm(checklist_prompt, system_prompt=system_prompt)

        await send_long_message(
            update,
            answer,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Suitability Checklist error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def investment_memo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty memo context. Try again.")
        return INVESTMENT_MEMO

    await update.message.reply_text("Thinking...")

    try:
        system_prompt = load_prompt(
            "base_rules.md",
            "wealth_policy.md",
            "client_profile_questions.md",
        )

        wealth_knowledge = load_wealth_knowledge()

        memo_prompt = f"""
Draft a non-final investment memo for this finance/wealth-management case.

Important:
- Do not recommend the product.
- Do not say the product is suitable.
- Do not say the client should buy, sell, or hold.
- The memo may support human reasoning only.
- A human advisor or client must make the final decision.
- If information is missing, say so clearly.

Use exactly this structure:

1. Product summary
2. Possible role in the portfolio
3. Possible fit factors
4. Possible not-fit factors
5. Main risks
6. Fees, liquidity, and operational questions
7. Suitability concerns to verify
8. Missing information
9. Human decision required
10. Suggested next tiny action
11. Reminder: this is not a recommendation

Local wealth knowledge:
{wealth_knowledge}
Product and client context:
{prompt}
"""

        answer = local_llm(memo_prompt, system_prompt=system_prompt)

        await send_long_message(
            update,
            answer,
            reply_markup=MAIN_KEYBOARD,
        )

    except Exception as e:
        await update.message.reply_text(
            f"Investment Memo error: {e}",
            reply_markup=MAIN_KEYBOARD,
        )

    return ConversationHandler.END

async def ask_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text.strip()

    if not prompt:
        await update.message.reply_text("Empty question. Try again.")
        return ASKING

    await update.message.reply_text("Thinking...")

    try:
        answer, usage = gemini_llm(prompt)

        await send_long_message(
            update,
            answer + format_gemini_usage_note(usage),
            reply_markup=MAIN_KEYBOARD,
        )

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
        MessageHandler(filters.Regex("^ðŸ’¼ Wealth$"), wealth_start),
        MessageHandler(filters.Regex("^ðŸ‘¤ Client Profile$"), client_profile_start),
        MessageHandler(filters.Regex("^ðŸ¦ Platform Options$"), platform_options_start),
        MessageHandler(filters.Regex("^ðŸ“Š Portfolio Parser$"), portfolio_parser_start),
        MessageHandler(filters.Regex("^âœ… Suitability Checklist$"), suitability_checklist_start),
        MessageHandler(filters.Regex("^ðŸ“ Investment Memo$"), investment_memo_start),
    ],
    states={
        ASKING: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, ask_message)
        ],
        CAPTURING: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, capture_message)
        ],
        WEALTH: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, wealth_message)
        ],
        CLIENT_PROFILE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, client_profile_message)
        ],
        PLATFORM_OPTIONS: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, platform_options_message)
        ],
        PORTFOLIO_PARSER: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, portfolio_parser_message)
        ],
        SUITABILITY_CHECKLIST: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, suitability_checklist_message)
        ],
        INVESTMENT_MEMO: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, investment_memo_message)
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

app.add_handler(CommandHandler("geminiask", gemini_ask))

app.add_handler(conversation_handler)

app.add_handler(MessageHandler(filters.Regex("^ðŸ“¥ Inbox$"), inbox))
app.add_handler(MessageHandler(filters.Regex("^ðŸ“… Today$"), today))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture))

app.run_polling()
