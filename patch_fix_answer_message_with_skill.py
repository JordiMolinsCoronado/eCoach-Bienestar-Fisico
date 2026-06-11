from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# Remove any broken helper if it was previously inserted
broken_re = r'\nasync def answer_message_with_skill\(.*?\):.*?(?=\nasync def |\ndef |\n# ---------------------------------------------------------------------)'
text, removed = re.subn(broken_re, "", text, flags=re.S)
print("Removed old answer_message_with_skill:", removed)

m = re.search(
    r'\nasync def answer_callback_with_skill\(.*?\):.*?(?=\nasync def |\ndef |\n# ---------------------------------------------------------------------)',
    text,
    flags=re.S,
)

if not m:
    raise SystemExit("Could not find answer_callback_with_skill.")

new_helper = r'''
async def answer_message_with_skill(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    skill_name: str,
    task: str,
    facts: str,
    reply_markup=None,
) -> None:
    thinking_message = await update.message.reply_text("Pensando...")

    try:
        answer = await asyncio.to_thread(
            generate_skill_client_reply,
            skill_name,
            task,
            facts,
        )
    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        await update.message.reply_text(
            f"No he podido aplicar el plan en tiempo real: {error}",
            reply_markup=MAIN_KEYBOARD,
        )
        return

    try:
        await thinking_message.delete()
    except Exception:
        pass

    await update.message.reply_text(answer, reply_markup=reply_markup)
'''

text = text[:m.end()] + "\n\n" + new_helper.strip() + "\n" + text[m.end():]

path.write_text(text, encoding="utf-8")
print("Inserted correct answer_message_with_skill helper.")
