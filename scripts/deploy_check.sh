#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_BIN="${PYTHON_BIN:-/opt/patrimonio-copiloto/.venv/bin/python}"

echo "== eCoach deploy check =="
echo

echo "1/5 Python compile check..."
"$PYTHON_BIN" -m py_compile eCoach_Patrimonio.py
echo "OK: Python compile passed."
echo

echo "2/5 Follow-up smoke test..."
"$PYTHON_BIN" scripts/smoke_test_followups.py
echo "OK: Follow-up smoke test passed."
echo

echo "3/5 Router smoke test..."
"$PYTHON_BIN" scripts/smoke_test_router.py
echo "OK: Router smoke test passed."
echo

echo "4/5 Session memory smoke test..."
"$PYTHON_BIN" scripts/smoke_test_session_memory.py
echo "OK: Session memory smoke test passed."
echo

echo "5/5 File integrity smoke test..."
"$PYTHON_BIN" scripts/smoke_test_file_integrity.py
echo "OK: File integrity smoke test passed."
echo

echo "READY TO RESTART"

