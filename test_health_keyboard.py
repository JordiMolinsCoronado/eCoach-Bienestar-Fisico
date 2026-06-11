import os

os.environ.setdefault("TELEGRAM_BOT_TOKEN", "LOCAL_TEST_TOKEN")

import eCoach_Bienestar_Fisico as app

keyboard = app.health_document_analysis_keyboard()

print(keyboard.to_dict())
