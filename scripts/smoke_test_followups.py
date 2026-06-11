import asyncio
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import eCoach_Relaciones as bot


CLIENT_NAME = "telegram_7960326623"
DATE_ONLY_ID = "smoke_test_date_only_followup"
TIMED_ID = "smoke_test_timed_followup"


def read_json(path: Path) -> list[dict]:
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return []
    return json.loads(content)


def write_json(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def remove_test_items(path: Path, ids: set[str]) -> None:
    data = read_json(path)
    data = [item for item in data if item.get("id") not in ids]
    write_json(path, data)


async def main() -> None:
    bot.set_current_client_name(CLIENT_NAME)
    bot.ensure_client_files()
    bot.ensure_followup_triggers_file()

    active_path = bot.followup_triggers_file()
    archive_path = bot.followup_archive_file()

    test_ids = {DATE_ONLY_ID, TIMED_ID}

    # Clean previous smoke-test leftovers.
    remove_test_items(active_path, test_ids)
    remove_test_items(archive_path, test_ids)

    now = bot.now_app()
    now_text = now.strftime("%Y-%m-%d %H:%M:%S")

    active = read_json(active_path)

    active.append(
        {
            "id": DATE_ONLY_ID,
            "client_id": CLIENT_NAME,
            "created_at": now_text,
            "date": bot.today_app().strftime("%Y-%m-%d"),
            "time": "",
            "type": "general_checkin",
            "message_template": "SMOKE TEST: date-only follow-up.",
            "reason": "Smoke test date-only follow-up.",
            "sensitivity": "low",
            "requires_private_context": True,
            "status": "pending",
            "source": "smoke_test",
        }
    )

    timed_target = now - timedelta(minutes=1)

    active.append(
        {
            "id": TIMED_ID,
            "client_id": CLIENT_NAME,
            "created_at": now_text,
            "date": timed_target.strftime("%Y-%m-%d"),
            "time": timed_target.strftime("%H:%M"),
            "type": "general_checkin",
            "message_template": "SMOKE TEST: timed follow-up.",
            "reason": "Smoke test timed follow-up.",
            "sensitivity": "low",
            "requires_private_context": True,
            "status": "pending",
            "source": "smoke_test",
        }
    )

    write_json(active_path, active)

    sent_messages: list[str] = []

    async def capture_message(text: str) -> None:
        sent_messages.append(text)

    date_result = await bot.send_due_followups(
        reply_text_func=capture_message,
        notes="Smoke test date-only sender.",
    )

    timed_result = await bot.send_due_timed_followups(
        reply_text_func=capture_message,
        notes="Smoke test timed sender.",
    )

    active_after = read_json(active_path)
    archive_after = read_json(archive_path)

    active_ids = {item.get("id") for item in active_after}
    archive_by_id = {item.get("id"): item for item in archive_after}

    errors: list[str] = []

    if date_result.get("sent_count") != 1:
        errors.append(f"Expected date-only sent_count=1, got {date_result.get('sent_count')}.")

    if timed_result.get("sent_count") != 1:
        errors.append(f"Expected timed sent_count=1, got {timed_result.get('sent_count')}.")

    if DATE_ONLY_ID in active_ids:
        errors.append("Date-only smoke test follow-up still active.")

    if TIMED_ID in active_ids:
        errors.append("Timed smoke test follow-up still active.")

    date_archived = archive_by_id.get(DATE_ONLY_ID)
    timed_archived = archive_by_id.get(TIMED_ID)

    if not date_archived:
        errors.append("Date-only smoke test follow-up not found in archive.")
    elif date_archived.get("archive_reason") != "sent":
        errors.append(f"Date-only archive_reason should be 'sent', got {date_archived.get('archive_reason')}.")

    if not timed_archived:
        errors.append("Timed smoke test follow-up not found in archive.")
    elif timed_archived.get("archive_reason") != "timed_sent":
        errors.append(f"Timed archive_reason should be 'timed_sent', got {timed_archived.get('archive_reason')}.")

    expected_messages = {
        "SMOKE TEST: date-only follow-up.",
        "SMOKE TEST: timed follow-up.",
    }

    if set(sent_messages) != expected_messages:
        errors.append(f"Unexpected captured messages: {sent_messages}")

    # Clean smoke-test archive entries after validation, so runtime files stay clean.
    remove_test_items(active_path, test_ids)
    remove_test_items(archive_path, test_ids)

    if errors:
        print("FOLLOW-UP SMOKE TEST FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("FOLLOW-UP SMOKE TEST PASSED")
    print(f"- Date-only result: {date_result}")
    print(f"- Timed result: {timed_result}")
    print(f"- Captured messages: {sent_messages}")
    print("- Active and archive smoke-test entries cleaned.")


if __name__ == "__main__":
    asyncio.run(main())

