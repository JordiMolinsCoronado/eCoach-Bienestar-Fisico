# Copiloto Relaciones â€” Timeline and Next Steps

**Date:** 2026-05-25  
**Status:** v0.1 is close to code-freeze. The core engine works; the next major value is in testing through realistic client scenarios and improving the Markdown knowledge/configuration files.

---

## 1. Current state â€” what already works

The current version already has the first usable product spine:

- Telegram bot receives free-text client messages.
- The bot shows a temporary â€œPensandoâ€¦â€ message while processing.
- DeepSeek V4 Pro is the primary LLM provider.
- Gemini is available as fallback.
- Provider-neutral usage reporting works.
- Living client summaries are updated:
  - `quien_soy.md`
  - `que_quiero.md`
  - `que_tengo_que_hacer.md`
  - `estilo_respuesta.md`
  - `agent_config.md`
  - `agent_observations.md`
  - `historial_interacciones.md`
  - `proactivity_log.md`
- Agent observations are generated and stored.
- Follow-up triggers are created.
- Follow-up triggers can be viewed, sent, snoozed, completed, deleted, and logged.
- The scheduler works and Telegram notifications appear when the chat is not muted.
- Basic duplicate creation control works.
- Follow-up types are normalized into a fixed set.
- Simple reminder behavior is now acceptable: short answer, one clear next action, no over-helping.

The key conclusion: **the core programming is good enough to stop expanding features for now.**

---

## 2. What â€œno multi-client UI yetâ€ means

At the moment, the bot works with one active client folder at a time through `.env`:

```env
ACTIVE_CLIENT_NAME=Cliente1
```

That means the bot reads and writes files inside:

```text
ClientData/Cliente1/
```

A future multi-client UI would allow commands like:

```text
/client Elena
/client Carlos
/client Marta
```

or a dashboard where a user can select the active client without changing `.env` and restarting the bot.

This is **not necessary now**. For demos and testing, we can simply create different client folders and switch manually through `.env`:

```env
ACTIVE_CLIENT_NAME=Caso_1_PreJubilacion
ACTIVE_CLIENT_NAME=Caso_2_VentaEmpresa
ACTIVE_CLIENT_NAME=Caso_3_Herencia
```

Then restart the bot for each case.

---

## 3. Programming stop point

The next programming step is not another feature. The next step is to freeze the current code as a stable baseline.

Recommended file name:

```text
eCoach_Relaciones_v0_1.py
```

or:

```text
eCoach_Relaciones_20260525_stable.py
```

Also create a small `CHANGELOG.md` entry:

```text
v0.1 â€” 2026-05-25

Working:
- Telegram free text to orchestrator
- DeepSeek V4 Pro primary provider
- Gemini fallback provider
- living summaries
- agent observations
- follow-up creation
- follow-up commands
- scheduler
- Telegram notifications
- basic duplicate control
- provider-neutral usage note

Known limitations:
- no multi-client UI yet
- no document upload / PDF analysis yet
- privacy risk layer not active
- follow-up deduplication is simple, not semantic-perfect
- DeepSeek can be slower than Gemini
```

After this, avoid adding code unless a real bug appears.

---

## 4. New Phase 3 â€” scenario-based testing and demo creation

Instead of a dry technical test suite, the next testing phase should be based on fictional but realistic client scenarios, like characters in a book.

The goal is to create 2 or 3 recorded Telegram conversations that show a new client how to use the software.

Each demo should show:

1. The client writes naturally in Telegram.
2. Copiloto Relaciones understands the situation.
3. The bot updates:
   - `quien_soy.md`
   - `que_quiero.md`
   - `que_tengo_que_hacer.md`
4. The bot creates useful follow-ups when appropriate.
5. The user opens the summaries and sees a living client memory forming.
6. The viewer understands how they could use the system in their own life.

This is better than feature-checklist testing because it demonstrates the product through human stories.

---

## 5. Demo scenario structure

Each scenario should have:

- A fictional client name.
- Age and life situation.
- Financial context.
- Emotional state.
- Main goal.
- Main fear or confusion.
- A pending document, decision, meeting, or action.
- A short Telegram script.
- Expected summary evolution.
- Expected follow-up behavior.

The conversation should be short enough to record clearly: around 5 to 8 client messages.

After every few messages, show one or more of:

```text
/quien_soy or the â€œResumen de quiÃ©n soy yoâ€ button
/que_quiero or the â€œResumen de quÃ© quieroâ€ button
/que_tengo_que_hacer or the â€œResumen de quÃ© tengo que hacerâ€ button
/followups
/scheduler_status
```

The recording should make the viewer feel: â€œAh, now I understand how I would use this.â€

---

## 6. Suggested demo cases

### Case 1 â€” Pre-retirement bank proposal

**Name:** Elena  
**Age:** 61  
**Situation:** Close to retirement. Has savings, owns her home, and receives a bank proposal she does not fully understand.  
**Financial context:** Around â‚¬420,000 in savings.  
**Emotion:** Careful, cautious, afraid of making a bad irreversible decision.  
**Goal:** Preserve capital, generate some income, avoid bad products, decide calmly.  
**Immediate task:** Ask the bank for the full proposal with products, costs, liquidity, risk level, and tax consequences.

This is the best first demo because it is common, emotionally understandable, and strongly aligned with the softwareâ€™s value.

---

### Case 2 â€” Entrepreneur after selling a company

**Name:** Carlos  
**Age:** 52  
**Situation:** Has sold a business and suddenly has a large amount of liquidity. Banks and advisors are approaching him.  
**Financial context:** Significant liquidity after company sale; tax and investment uncertainty.  
**Emotion:** Overwhelmed, suspicious of banks, afraid of wasting the opportunity.  
**Goal:** Protect the capital, understand tax consequences, build a long-term plan, avoid being pushed into unsuitable products.  
**Immediate task:** Organize documents, clarify time horizon, identify tax constraints, and compare proposals.

This case demonstrates Copiloto Relaciones as a protection system against complexity and sales pressure.

---

### Case 3 â€” Inheritance and family complexity

**Name:** Marta  
**Age:** 47  
**Situation:** Receives or expects an inheritance, with siblings/family tension and unclear paperwork.  
**Financial context:** Inherited assets may include cash, property, or funds.  
**Emotion:** Confused, emotionally loaded, worried about signing something without understanding.  
**Goal:** Understand what she owns, what she must decide, what documents matter, and what professional help is needed.  
**Immediate task:** List documents, deadlines, family stakeholders, and decisions that must not be rushed.

This case demonstrates the bot as a calm memory and action system during emotionally charged financial events.

---

## 7. Recording format for each demo

For each scenario:

1. Set a clean active client folder in `.env`:

```env
ACTIVE_CLIENT_NAME=Caso_1_PreJubilacion
```

2. Restart the bot.

3. Send `/start`.

4. Paste or type the scenario messages in Telegram slowly.

5. After key moments, show the summaries:

```text
Resumen de quiÃ©n soy yo
Resumen de quÃ© quiero
Resumen de quÃ© tengo que hacer
```

6. Show `/followups` if the scenario creates a reminder.

7. End the video with the visible transformation:

```text
A vague financial worry becomes structured identity, goals, next actions, and follow-ups.
```

---

## 8. The Markdown files are the secret sauce

After code freeze, most improvement should happen in the `.md` files, not in Python.

Priority order:

### 1. `AgentConfig/`

Defines the personality and judgment of the copilot.

It should answer:

- What kind of wealth copilot is this?
- How proactive should it be?
- How cautious should it be?
- How does it avoid sounding like a bank salesperson?
- How does it protect the client from confusion, pressure, and vague advice?
- How does it handle uncertainty?
- How does it ask for missing information?

Desired character:

```text
calm, prudent, protective, document-oriented, anti-confusion, action-focused, non-salesy
```

---

### 2. `Wealth_Knowledge/`

This is where the domain expertise lives.

First files to create or improve:

```text
investment_proposal_review.md
bank_conflict_of_interest.md
investment_costs.md
risk_profile.md
liquidity_and_time_horizon.md
questions_to_ask_bank.md
spanish_tax_context_basic.md
```

The most important first file:

```text
Wealth_Knowledge/investment_proposal_review.md
```

It should teach the bot to ask for and analyze:

- Product name
- Product wrapper
- Fees and commissions
- Entry and exit costs
- Ongoing costs
- Liquidity
- Risk level
- Currency exposure
- Tax consequences
- Conflicts of interest
- Alternatives
- Questions to ask before signing

---

### 3. `InitialClientFiles/`

These are the empty starting memories for a new client.

They should be structured enough to guide the model but not so full that they pollute the first conversation.

Important files:

```text
quien_soy.md
que_quiero.md
que_tengo_que_hacer.md
estilo_respuesta.md
agent_config.md
agent_observations.md
proactivity_log.md
historial_interacciones.md
```

Suggested structure:

`quien_soy.md`:

- Personal profile
- Family context
- Financial situation known so far
- Preferences
- Constraints
- Unknowns

`que_quiero.md`:

- Goals
- Fears
- Time horizon
- Desired lifestyle
- Priorities
- Non-negotiables

`que_tengo_que_hacer.md`:

- Pending documents
- Pending decisions
- Next actions
- Follow-ups
- Questions to clarify

---

### 4. `AppTexts/orchestrator_user_prompt.md`

Already strong, but it may become too long or overfit to reminders.

Later it should be simplified into clear sections:

1. Role
2. Input context
3. Living-summary update rules
4. Client response rules
5. Follow-up rules
6. JSON schema

Do not overwork it now unless testing reveals a clear problem.

---

### 5. `estilo_respuesta.md`

This file controls the client-facing tone.

Desired style:

- Short
- Clear
- Protective
- Not salesy
- Not paternalistic
- No vague offers
- No over-explaining
- One concrete next action
- Calm when the client is anxious
- Precise when the client is confused

This may be more important than adding more Python code.

---

## 9. New testing philosophy

From now on, testing should answer:

```text
Does the client understand himself better after using the bot?
Does the client know what to do next?
Does the bot reduce confusion instead of adding noise?
Does the bot create useful memory without becoming verbose?
Does the bot feel like a calm patrimonial copilot, not a generic chatbot?
```

This is more important than testing endless technical edge cases.

---

## 10. When programming is finished for v0.1

Programming is finished for v0.1 when this sentence is true:

```text
The bot reliably captures user intent, updates memory, creates useful follow-ups, and does not spam.
```

Current status: this is basically true.

So the next real work is:

1. Freeze the code.
2. Create 2â€“3 demo scenarios.
3. Record Telegram conversations.
4. Improve `.md` files based on what feels generic, weak, or unclear.
5. Only return to Python if the demos reveal a real functional bug.

---

## 11. Immediate next action

Create **Case 1: Elena â€” Pre-retirement bank proposal**.

Deliverables:

1. Scenario description.
2. Telegram script with 5â€“8 client messages.
3. Expected evolution of:
   - `quien_soy.md`
   - `que_quiero.md`
   - `que_tengo_que_hacer.md`
4. Expected follow-up behavior.
5. Recording checklist.

This is the next meaningful step because it moves the project from engineering into product demonstration.

---

## 12. Stop condition for today

A good stopping point is:

```text
The code has been frozen as v0.1, and the timeline/roadmap file has been saved.
```

After that, the next session should begin with the first fictional client scenario, not more code.


