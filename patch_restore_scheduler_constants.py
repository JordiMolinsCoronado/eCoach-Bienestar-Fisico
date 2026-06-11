from pathlib import Path

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

hour_definition = 'PROACTIVE_SCHEDULER_HOUR = int(os.getenv("PROACTIVE_SCHEDULER_HOUR", "9"))'
minute_definition = 'PROACTIVE_SCHEDULER_MINUTE = int(os.getenv("PROACTIVE_SCHEDULER_MINUTE", "0"))'

# Insert definitions near the other environment configuration.
if hour_definition not in text or minute_definition not in text:
    anchors = [
        'LLM_MAX_OUTPUT_TOKENS = int(os.getenv("LLM_MAX_OUTPUT_TOKENS", "5000"))',
        'TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]',
    ]

    anchor = next((item for item in anchors if item in text), None)

    if anchor is None:
        raise SystemExit("Could not find configuration anchor.")

    addition = (
        anchor
        + "\n\n"
        + hour_definition
        + "\n"
        + minute_definition
    )

    text = text.replace(anchor, addition, 1)
    print("Inserted scheduler constant definitions.")
else:
    print("Scheduler constant definitions already present.")

# Fix malformed f-string.
bad = (
    'f"- Hora diaria date-only: '
    '{PROACTIVE_SCHEDULER_HOUR:02d}:PROACTIVE_SCHEDULER_MINUTE:02d} '
    '{APP_TIMEZONE}",'
)

good = (
    'f"- Hora diaria date-only: '
    '{PROACTIVE_SCHEDULER_HOUR:02d}:'
    '{PROACTIVE_SCHEDULER_MINUTE:02d} '
    '{APP_TIMEZONE}",'
)

if bad in text:
    text = text.replace(bad, good, 1)
    print("Fixed malformed scheduler display string.")
else:
    print("Malformed scheduler display string not found; inspect line manually if needed.")

path.write_text(text, encoding="utf-8")
print("Patch complete.")
