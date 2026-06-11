#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [ "${1:-}" = "" ]; then
  echo "Usage:"
  echo "  bash scripts/restore_runtime.sh runtime_backups/backup_YYYYMMDD_HHMMSS"
  echo
  echo "Available backups:"
  ls -1 runtime_backups 2>/dev/null || true
  exit 1
fi

BACKUP_DIR="$1"

if [ ! -d "$BACKUP_DIR" ]; then
  echo "ERROR: backup folder not found: $BACKUP_DIR"
  exit 1
fi

echo "== eCoach runtime restore =="
echo "Backup folder: $BACKUP_DIR"
echo

echo "Safety check before restore..."
bash scripts/deploy_check.sh
echo

RESTORE_SNAPSHOT="runtime_backups/pre_restore_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RESTORE_SNAPSHOT"

if [ -d "ClientData" ]; then
  cp -a ClientData "$RESTORE_SNAPSHOT/"
  echo "OK: current ClientData backed up to $RESTORE_SNAPSHOT"
fi

if [ -f ".env" ]; then
  cp -a .env "$RESTORE_SNAPSHOT/.env"
  echo "OK: current .env backed up to $RESTORE_SNAPSHOT"
fi

if [ -d "$BACKUP_DIR/ClientData" ]; then
  rm -rf ClientData
  cp -a "$BACKUP_DIR/ClientData" ./ClientData
  echo "OK: restored ClientData/"
else
  echo "WARN: backup has no ClientData/"
fi

if [ -f "$BACKUP_DIR/.env" ]; then
  cp -a "$BACKUP_DIR/.env" ./.env
  echo "OK: restored .env"
else
  echo "WARN: backup has no .env"
fi

echo
echo "Restore complete."
echo "Previous runtime state was saved to:"
echo "$RESTORE_SNAPSHOT"
echo
echo "Recommended next command:"
echo "  bash scripts/deploy_check.sh && sudo systemctl restart patrimonio-copiloto"

