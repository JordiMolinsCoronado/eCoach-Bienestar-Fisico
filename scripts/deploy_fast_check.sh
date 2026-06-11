#!/usr/bin/env bash
set -euo pipefail

echo "== eCoach FAST deploy check =="

echo
echo "1/2 Python compile check..."
.venv/bin/python -m py_compile eCoach_Patrimonio.py
echo "OK: Python compile passed."

echo
echo "2/2 File integrity smoke test..."
.venv/bin/python scripts/smoke_test_file_integrity.py
echo "OK: File integrity smoke test passed."

echo
echo "FAST READY TO RESTART"

