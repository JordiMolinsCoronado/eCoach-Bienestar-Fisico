import json
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import eCoach_Relaciones as bot


TEST_CLIENT = "telegram_smoke_test_session_memory"


def fail(message: str) -> None:
    print("SESSION MEMORY SMOKE TEST FAILED")
    print(f"- {message}")
    raise SystemExit(1)


def main() -> None:
    bot.set_current_client_name(TEST_CLIENT)

    client_dir = bot.active_client_dir()

    if client_dir.exists():
        shutil.rmtree(client_dir)

    bot.ensure_client_files()
    bot.ensure_followup_triggers_file()

    files = bot.client_files()

    files["quien_soy"].write_text(
        "- Resto de datos pendientes.\n",
        encoding="utf-8",
    )

    files["que_quiero"].write_text(
        "- Resto de objetivos pendientes.\n",
        encoding="utf-8",
    )

    files["que_tengo_que_hacer"].write_text(
        "- Resto de tareas pendientes.\n",
        encoding="utf-8",
    )

    bot.append_session_buffer(
        user_text="Tengo 61 aÃ±os y vivo en Manresa.",
        assistant_answer="Entendido. Lo tendremos en cuenta durante esta conversaciÃ³n.",
    )

    buffer_content = bot.session_buffer_file().read_text(encoding="utf-8")

    if "Tengo 61 aÃ±os" not in buffer_content:
        fail("The stable fact was not written to session_buffer.md.")

    data = bot.generate_session_consolidation()

    if not isinstance(data, dict):
        fail("generate_session_consolidation did not return a dict.")

    updates = data.get("quien_soy_updates", [])

    if not updates:
        fail(f"No quien_soy_updates returned. Data: {data}")

    updates_text = "\n".join(str(item) for item in updates)

    if "61" not in updates_text or "Manresa" not in updates_text:
        fail(f"quien_soy_updates do not include age/residence. Updates: {updates}")

    old_content = files["quien_soy"].read_text(encoding="utf-8")

    new_content = bot.apply_session_updates_to_memory_file(
        target_key="quien_soy",
        old_content=old_content,
        updates=updates,
    )

    if "Consolidaciones de sesiÃ³n" in new_content:
        fail("apply_session_updates_to_memory_file returned forbidden 'Consolidaciones de sesiÃ³n'.")

    if "61" not in new_content or "Manresa" not in new_content:
        fail(f"Updated quien_soy content does not include expected fact. Content: {new_content}")

    # Clean test client folder after validation.
    if client_dir.exists():
        shutil.rmtree(client_dir)

    print("SESSION MEMORY SMOKE TEST PASSED")
    print(f"- Updates: {updates}")
    print("- No forbidden Consolidaciones de sesiÃ³n section.")
    print("- Test client cleaned.")


if __name__ == "__main__":
    main()

