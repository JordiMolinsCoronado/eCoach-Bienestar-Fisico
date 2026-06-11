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

count = text.count(old_schedule)

if count != 1:
    raise SystemExit(
        f"Expected exactly one tomorrow-at-08:00 schedule block, found {count}."
    )

text = text.replace(
    old_schedule,
    new_schedule,
    1,
)

old_button = '''"Crear seguimiento — mañana 08:00"'''
new_button = '''"Activar seguimiento de demo — en 1 minuto"'''

if old_button in text:
    text = text.replace(
        old_button,
        new_button,
        1,
    )
    print("Changed follow-up button text.")
else:
    print("Original button text not found; schedule will still be changed.")


old_confirmation = '''"Listo, Laura. He creado un seguimiento para mañana a las 08:00.\\n\\n"'''

new_confirmation = '''"Listo, Laura. Para esta demostración, haré el seguimiento dentro de aproximadamente un minuto.\\n\\n"'''

if old_confirmation in text:
    text = text.replace(
        old_confirmation,
        new_confirmation,
        1,
    )
    print("Changed confirmation message.")
else:
    print("Original confirmation text not found; inspect it if necessary.")


old_plan_ending = '''- say eCoach can check in the following morning;'''
new_plan_ending = '''- say that, for this demonstration, eCoach can check in in approximately one minute;'''

if old_plan_ending in text:
    text = text.replace(
        old_plan_ending,
        new_plan_ending,
        1,
    )


path.write_text(text, encoding="utf-8")

print("Demo follow-up will now be scheduled one minute after the button is clicked.")
