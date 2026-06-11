# eCoach Relaciones â€” Architecture Map

## Purpose

eCoach Relaciones is a Telegram-based patrimonial copilot.

It helps the user:

- Ask financial/patrimonial questions.
- Maintain a Second Brain.
- Create and receive follow-ups.
- Consolidate session memory.
- Receive proactive reminders.

---

## Main systems

The bot has five core systems:

1. Router
2. Orchestrator
3. Second Brain memory
4. Follow-up engine
5. Smoke tests / deploy checks

---

## 1. Router

The router is the fast first LLM call.

Its job is to decide what kind of message the user sent.

Main routes:

- smalltalk
- simple_response
- memory_update
- followup_management
- deeper patrimonial/orchestrator route

Important behavior:

- Simple greetings are answered directly.
- Stable memory facts are acknowledged but not saved immediately.
- Explicit follow-up requests are saved immediately.
- Ambiguous future events ask before saving.
- Deeper financial questions go to the orchestrator.

Examples:

    Hola
    â†’ smalltalk

    Tengo 51 aÃ±os y vivo en Barcelona.
    â†’ should_update_memory = true

    RecuÃ©rdame maÃ±ana revisar la respuesta del banco.
    â†’ followup_management

    El banco me contestarÃ¡ maÃ±ana.
    â†’ simple_response, ask if user wants a reminder

---

## 2. Orchestrator

The orchestrator is used for deeper patrimonial analysis.

It receives:

- User message.
- Selected client memory files.
- Selected knowledge files.
- Pending follow-ups context.
- Agent configuration.

It generates the main financial answer.

The router decides whether the orchestrator is needed.

---

## 3. Second Brain memory

Stable facts and goals are not written immediately.

They are collected in:

    session_buffer.md

The user clicks:

    ðŸ’¾ Guardar sesiÃ³n

Then the bot:

1. Summarizes the session.
2. Proposes updates to:
   - quien_soy.md
   - que_quiero.md
   - que_tengo_que_hacer.md
3. Waits for user confirmation.
4. Saves only after confirmation.

Important rule:

Operational follow-ups should not be stored as Second Brain memory.

---

## 4. Follow-up engine

Follow-ups are operational, so explicit requests are saved immediately.

Active follow-ups live in:

    followup_triggers.json

Archived follow-ups live in:

    followup_archive.json

There are two follow-up types.

### Date-only follow-ups

Example:

    {
      "date": "2026-06-04",
      "time": ""
    }

These are sent by the daily scheduler.

Default scheduler:

    08:00 Europe/Madrid

### Timed follow-ups

Example:

    {
      "date": "2026-06-04",
      "time": "17:30"
    }

These are checked by the timed scheduler every minute.

### Archive behavior

When a follow-up is:

- sent
- completed
- deleted

it is moved out of:

    followup_triggers.json

and into:

    followup_archive.json

This keeps active follow-ups clean.

---

## 5. Telegram commands

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

Memory:

    ðŸ’¾ Guardar sesiÃ³n

---

## 6. Schedulers

There are two schedulers.

### Daily date-only scheduler

Registered with:

    app.job_queue.run_daily(...)

Purpose:

- Sends pending follow-ups with a date and no time.
- Runs once per day.

### Timed scheduler

Registered with:

    app.job_queue.run_repeating(...)

Purpose:

- Sends pending follow-ups with date + time.
- Runs every minute.

---

## 7. Smoke tests

The deploy check runs several safety tests:

    bash scripts/deploy_check.sh

Current checks:

1. Python compile check.
2. Follow-up smoke test.
3. Router smoke test.
4. Session memory smoke test.
5. File integrity smoke test.

These protect:

- Follow-up saving.
- Date-only delivery.
- Timed delivery.
- Archive movement.
- Router classification.
- Session memory consolidation.
- Required AppTexts files.

---

## 8. Runtime state versus source code

Do not commit runtime state:

- .env
- ClientData/
- logs
- session buffers
- followup runtime JSON files

Commit source code, prompts, docs, and test scripts.

---

## 9. Current product boundary

Follow-ups:

- explicit reminder request â†’ save immediately
- ambiguous future event â†’ ask first
- sent/completed/deleted â†’ archive

Memory:

- durable facts/goals â†’ session buffer
- save only after ðŸ’¾ Guardar sesiÃ³n + confirmation

Analysis:

- deeper financial question â†’ orchestrator

