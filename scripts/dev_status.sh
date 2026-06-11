#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_BIN="${PYTHON_BIN:-/opt/patrimonio-copiloto/.venv/bin/python}"
CLIENT_NAME="${CLIENT_NAME:-telegram_7960326623}"

echo "== eCoach Dev Status =="
echo

echo "== Git =="
git branch --show-current || true
git --no-pager log -1 --oneline || true
echo

echo "== Git status =="
git status --short || true
echo

echo "== Service status =="
systemctl is-active patrimonio-copiloto || true
systemctl status patrimonio-copiloto --no-pager -l | head -n 20 || true
echo

echo "== Scheduler config =="
"$PYTHON_BIN" - <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

import eCoach_Patrimonio as bot

print(f"APP_TIMEZONE={bot.APP_TIMEZONE}")
print(f"PROACTIVE_SCHEDULER_HOUR={bot.PROACTIVE_SCHEDULER_HOUR}")
print(f"PROACTIVE_SCHEDULER_MINUTE={bot.PROACTIVE_SCHEDULER_MINUTE}")
PY
echo

echo "== Follow-up files =="
"$PYTHON_BIN" - <<'PY'
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

import eCoach_Patrimonio as bot

client_name = os.environ.get("CLIENT_NAME", "telegram_7960326623")
bot.set_current_client_name(client_name)

active_path = bot.followup_triggers_file()
archive_path = bot.followup_archive_file()
buffer_path = bot.session_buffer_file()

def load_list(path: Path) -> list:
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return []
    try:
        data = json.loads(content)
        return data if isinstance(data, list) else []
    except Exception:
        return []

active = load_list(active_path)
archive = load_list(archive_path)
pending = [item for item in active if str(item.get("status", "pending")).lower() == "pending"]
timed = [item for item in pending if str(item.get("time", "")).strip()]
date_only = [item for item in pending if not str(item.get("time", "")).strip()]

print(f"client={client_name}")
print(f"active_followups={len(active)}")
print(f"pending_followups={len(pending)}")
print(f"pending_date_only={len(date_only)}")
print(f"pending_timed={len(timed)}")
print(f"archived_followups={len(archive)}")
print(f"session_buffer_exists={buffer_path.exists()}")
print(f"session_buffer_size={buffer_path.stat().st_size if buffer_path.exists() else 0}")
PY
echo

echo "== Deploy check =="
bash scripts/deploy_check.sh

