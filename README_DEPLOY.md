# eCoach Relaciones â€” Deploy Checklist

## Golden rule

Before restarting the bot after code changes, run:

    cd /opt/relaciones-copiloto
    bash scripts/deploy_check.sh

Only restart if it ends with:

    READY TO RESTART

Then restart:

    sudo systemctl restart relaciones-copiloto
    sleep 2
    sudo systemctl status relaciones-copiloto --no-pager -l

Expected:

    Active: active (running)

---

## One-command safe restart

    cd /opt/relaciones-copiloto

    bash scripts/deploy_check.sh && sudo systemctl restart relaciones-copiloto && sleep 2 && sudo systemctl status relaciones-copiloto --no-pager -l

---

## Runtime backup and restore

Before risky changes, back up runtime state:

    cd /opt/relaciones-copiloto

    bash scripts/backup_runtime.sh

This backs up:

- ClientData/
- .env

into:

    runtime_backups/backup_YYYYMMDD_HHMMSS

To restore a previous runtime backup:

    cd /opt/relaciones-copiloto

    bash scripts/restore_runtime.sh runtime_backups/backup_YYYYMMDD_HHMMSS

After restoring, run:

    bash scripts/deploy_check.sh

    sudo systemctl restart relaciones-copiloto

Runtime backups are not committed to Git.

---

## Dev status

To inspect the current project state:

    cd /opt/relaciones-copiloto

    bash scripts/dev_status.sh

This shows:

- Git branch and latest commit.
- Git status.
- systemd service status.
- scheduler config.
- active and archived follow-up counts.
- session buffer status.
- deploy check result.

---

## What deploy_check does

`bash scripts/deploy_check.sh` currently runs:

1. Python compile check.
2. Follow-up smoke test.
3. Router smoke test.
4. Session memory smoke test.
5. File integrity smoke test.

This protects the main product paths:

- Explicit follow-ups.
- Date-only follow-ups.
- Timed follow-ups.
- Follow-up archive.
- Router classification.
- Session-based Second Brain memory.
- Required `AppTexts/*.md` files.

---

## Sync one or more files from VPS to laptop

On VPS, create a bundle:

    cd /opt/relaciones-copiloto

    tar -czf /tmp/ecoach_sync_bundle.tgz \
      path/to/file1 \
      path/to/file2

On laptop PowerShell:

    cd "C:\SecondBrain\OneDrive - Jordi Molins Coronado\RAM_Jordi\Prevengen\Prototipos\eCoach_Relaciones"

    scp -F "C:\SecondBrain\OneDrive - Jordi Molins Coronado\RAM_Jordi\Prevengen\Prototipos\.ssh\config" prevengen-server-fsn1-01:/tmp/ecoach_sync_bundle.tgz ecoach_sync_bundle.tgz

    tar -xzf ecoach_sync_bundle.tgz

    Remove-Item ecoach_sync_bundle.tgz

Then commit and push from laptop:

    git status
    git --no-pager diff

    git add path/to/file1 path/to/file2

    git commit -m "Commit message"

    git push

If Git says nothing to commit:

    git push

---

## Align VPS from GitHub

After pushing from laptop:

    cd /opt/relaciones-copiloto

    git fetch origin
    git reset --hard origin/main

    bash scripts/deploy_check.sh

    sudo systemctl restart relaciones-copiloto

    sleep 2

    sudo systemctl status relaciones-copiloto --no-pager -l

---

## Do not commit runtime state

Do not commit:

- `.env`
- `ClientData/`
- logs
- session buffers
- follow-up runtime JSON files

Runtime files are production state, not source code.

---

## Useful Telegram commands

General:

    /start
    /menu
    /help
    /version
    /diagnostics

Follow-ups:

    /followup_help
    /followups
    /due_followups
    /all_followups
    /followup_archive
    /followup_archive_stats
    /followup_cleanup
    /scheduler_status
    /run_followups

---

## Current follow-up architecture

Explicit follow-up request:

    RecuÃ©rdame maÃ±ana revisar la respuesta del banco.

is saved immediately.

Ambiguous future event:

    El banco me contestarÃ¡ maÃ±ana.

asks before saving.

Date-only follow-up:

    {
      "date": "2026-06-04",
      "time": ""
    }

is sent by the daily scheduler.

Timed follow-up:

    {
      "date": "2026-06-04",
      "time": "17:30"
    }

is sent by the timed scheduler.

Sent/completed/deleted follow-ups are moved from:

    followup_triggers.json

to:

    followup_archive.json

---

## Current memory architecture

Stable facts and goals are not saved immediately.

They are collected in:

    session_buffer.md

Then the user clicks:

    ðŸ’¾ Guardar sesiÃ³n

The bot proposes Second Brain updates.

Only after confirmation are these saved into:

    quien_soy.md
    que_quiero.md
    que_tengo_que_hacer.md

