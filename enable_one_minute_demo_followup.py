from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_demo_one_minute_followup")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")

old_schedule = '''    tomorrow = today_app() + timedelta(days=1)
    followup_date = tomorrow.strftime("%Y-%m-%d")
    followup_time = "08:00"'''

new_schedule = '''    demo_followup_at = now_app() + timedelta(minutes=1)
    followup_date = demo_followup_at.strftime("%Y-%m-%d")
    followup_time = demo_followup_at.strftime("%H:%M")'''

if old_schedule in text:
    text = text.replace(old_schedule, new_schedule, 1)
    print("Changed schedule to one minute.")
elif new_schedule in text:
    print("One-minute schedule already active.")
else:
    raise SystemExit("Could not find the follow-up schedule block.")

text = text.replace(
    '"Crear seguimiento — mañana 08:00"',
    '"Activar seguimiento de demo — en 1 minuto"',
)

text = text.replace(
    '"Listo, Laura. He creado un seguimiento para mañana a las 08:00.\\n\\n"',
    '"Listo, Laura. Para esta demostración, haré el seguimiento dentro de aproximadamente un minuto.\\n\\n"',
)

path.write_text(text, encoding="utf-8")

print("One-minute demo follow-up enabled.")
