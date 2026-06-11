from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_chunk_callback_answers")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

old = '''    await query.message.reply_text(answer, reply_markup=reply_markup)'''

new = '''    await reply_message_text_in_chunks(
        query.message,
        answer,
    )

    if reply_markup is not None:
        await query.message.reply_text(
            "Siguiente paso:",
            reply_markup=reply_markup,
        )'''

count = text.count(old)

if count != 1:
    raise SystemExit(
        f"Expected exactly one final callback reply line, found {count}."
    )

text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")

print("Callback LLM answers will now be sent in Telegram-safe chunks.")
