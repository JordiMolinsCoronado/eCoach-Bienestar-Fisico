# eCoach Memory, Follow-up and Proactivity Architecture

## Purpose

eCoach should not become an endless collection of one-off use cases.

The system should be built from reusable layers:

1. General eCoach answer principles.
2. A finite set of domain playbooks.
3. User memory files.
4. Third-party action packaging.
5. Follow-up tracking.
6. Proactive reminders.
7. Evaluation/testing.

The goal is to make eCoach useful over time: it should understand the client, remember what matters, help update that memory safely, track open loops, and proactively remind the client what to do.

---

# 1. Finite playbook universe

Playbooks should represent reusable financial forces, not every possible question.

A new user question should usually be handled by combining existing playbooks.

Example:

"He heredado dinero y mi hermano me pide un prÃ©stamo"
=
- inheritance_liquidity_event_playbook.md
- family_friend_loan_playbook.md
- default_investment_stance.md

The router should think in terms of active dimensions:

- sudden liquidity;
- mortgage/debt;
- income interruption;
- liquidity buffer;
- bank product;
- investment product;
- real estate;
- family/friend pressure;
- startup/private investment;
- tax/legal bottleneck;
- retirement;
- long-term portfolio policy;
- self-directed investing;
- follow-up/action tracking.

## Core playbook families

### A. Liquidity and safety
- cash_parking_playbook.md
- emergency_fund_liquidity_buffer_playbook.md
- severance_income_interruption_playbook.md
- inheritance_liquidity_event_playbook.md
- debt_vs_liquidity_playbook.md

### B. Housing and mortgage
- mortgage_amortization_vs_investing_playbook.md
- mortgage_fixed_variable_mixed_playbook.md
- real_estate_investment_playbook.md
- primary_home_buy_sell_playbook.md

### C. Bank and investment products
- structured_products_playbook.md
- unit_linked_playbook.md
- pension_plans_playbook.md
- funds_of_funds_playbook.md
- managed_portfolios_playbook.md
- individual_bonds_playbook.md
- private_markets_playbook.md
- cash_parking_playbook.md
- self_directed_rto_playbook.md

### D. Relationship-money risk
- family_friend_loan_playbook.md
- startup_friend_investment_playbook.md
- couple_money_boundaries_playbook.md
- guarantees_avales_cosigning_playbook.md

### E. Life planning
- retirement_planning_playbook.md
- children_family_support_playbook.md
- investment_policy.md
- tax_legal_bottleneck_playbook.md

Do not create a new playbook if an existing combination covers the case well.

Create a new playbook only when:
- a recurring financial force is not represented;
- answers repeatedly miss important concepts;
- the case requires a distinct due-diligence checklist or action pattern.

---

# 2. Router philosophy

The router should select modules, not memorize exact cases.

It should identify:
- what type of decision this is;
- what risks are active;
- what documents/context are needed;
- what user memory is relevant;
- whether the question can be answered directly.

The router should avoid overloading context.

High-quality routing means:
- select what is needed;
- avoid broad files unless truly needed;
- combine multiple playbooks if the user's situation genuinely combines several forces;
- if uncertain, choose a lean safe fallback rather than everything.

Router failure must never trigger full context.

Fallback should be:
- client_files: ["estilo_respuesta"]
- knowledge_files: ["default_investment_stance.md"]
- no memory update
- no follow-up extraction unless the user explicitly requested one

---

# 3. User memory files

User memory should be editable, structured and trustworthy.

The four core files are:

- quien_soy.md
- que_quiero.md
- que_tengo_que_hacer.md
- estilo_respuesta.md

They should not become random logs. They should be stable profiles.

## 3.1 quien_soy.md template

# QuiÃ©n soy

## Identidad y contexto personal
- Nombre:
- Edad aproximada:
- Residencia fiscal:
- Familia / personas dependientes:
- SituaciÃ³n familiar relevante:

## Trabajo e ingresos
- SituaciÃ³n laboral:
- Estabilidad de ingresos:
- Fuentes de ingresos:
- Ingresos recurrentes aproximados:
- Riesgos de ingresos:

## Relaciones actual
- Liquidez:
- Vivienda / hipoteca:
- Inversiones:
- Deudas:
- Seguros:
- Pensiones:
- Otros activos:

## Perfil de riesgo real
- Tolerancia a pÃ©rdidas:
- Tolerancia a iliquidez:
- Experiencia inversora:
- Productos que entiende:
- Productos que no entiende:
- Reacciones emocionales tÃ­picas:

## Restricciones importantes
- Fiscalidad:
- Familia:
- Salud:
- Horizonte temporal:
- Obligaciones futuras:
- Temas pendientes:

## Ãšltima actualizaciÃ³n relevante
- Fecha:
- QuÃ© cambiÃ³:

---

## 3.2 que_quiero.md template

# QuÃ© quiero

## Objetivos principales
- Seguridad financiera:
- Vivienda:
- JubilaciÃ³n:
- Hijos/familia:
- Independencia financiera:
- Ayuda a familiares:
- Otros:

## Prioridades actuales
- Corto plazo:
- Medio plazo:
- Largo plazo:

## Criterios de buena decisiÃ³n
- Liquidez mÃ­nima:
- Riesgo aceptable:
- Simplicidad:
- Control:
- Rentabilidad esperada:
- Paz mental:
- Flexibilidad:

## Miedos o tensiones
- Miedo a perder:
- Miedo a equivocarme:
- PresiÃ³n externa:
- Culpa:
- Conflictos familiares:
- Ansiedad por deuda:
- Ansiedad por oportunidad perdida:

## Preferencias de decisiÃ³n
- Prefiere:
- Evita:
- Necesita ver antes de decidir:

## Ãšltima actualizaciÃ³n relevante
- Fecha:
- QuÃ© cambiÃ³:

---

## 3.3 que_tengo_que_hacer.md template

# QuÃ© tengo que hacer

## PrÃ³xima acciÃ³n activa
- AcciÃ³n:
- Tercero implicado:
- Mensaje enviado / pendiente:
- Fecha objetivo:
- Estado:

## Pendientes financieros abiertos
- Banco:
- Gestor / notario / fiscal:
- Hipoteca:
- Inversiones:
- Seguros:
- Familia / prÃ©stamos:
- Trabajo / ingresos:
- Otros:

## Follow-ups abiertos
- ID:
- Tema:
- QuiÃ©n debe responder:
- QuÃ© espero:
- Fecha para recordar:
- Estado:

## Decisiones pendientes
- Tema:
- QuÃ© falta para decidir:
- Riesgo de decidir demasiado pronto:
- PrÃ³xima revisiÃ³n:

## Decisiones aparcadas
- Tema:
- Por quÃ© se aparca:
- CuÃ¡ndo revisar:

## Ãšltima actualizaciÃ³n relevante
- Fecha:
- QuÃ© cambiÃ³:

---

## 3.4 estilo_respuesta.md template

# Estilo de respuesta

## Tono
- Claro:
- Protector:
- No paternalista:
- Sobrio:
- Con calma:
- Con cÃ¡lculo:

## Formato
- Prefiere bullets:
- Prefiere tablas:
- Longitud ideal:
- Nivel tÃ©cnico:
- Idioma:

## Reglas de utilidad
- Hacer cÃ¡lculos visibles cuando haya nÃºmeros.
- Dar mensaje copiable si hay tercero implicado.
- Una prÃ³xima acciÃ³n concreta.
- No dejar tareas vagas.
- Explicar riesgos sin asustar.
- No sobre-recomendar.

## Evitar
- Jerga bancaria innecesaria:
- Respuestas largas sin acciÃ³n:
- Preguntas vagas:
- Exceso de legalismo:
- Tono comercial:

## Ãšltima actualizaciÃ³n relevante
- Fecha:
- QuÃ© cambiÃ³:

---

# 4. Memory update consent flow

eCoach should not silently mutate user memory in a way that feels spooky or unsafe.

When the user gives information that is useful long term, eCoach should propose saving it.

Example:

"He detectado un dato Ãºtil para tu memoria patrimonial:

- Tienes una hipoteca variable de 160.000â‚¬.
- Tus gastos familiares son unos 2.500â‚¬/mes.

Â¿Quieres que lo guarde en tu resumen de 'QuiÃ©n soy'?"

Options:
- Guardar
- Editar antes
- No guardar

## Save-worthy information

Save only information likely to matter again:
- income;
- employment situation;
- family obligations;
- dependents;
- mortgage;
- debt;
- liquidity;
- investments;
- recurring expenses;
- tax/legal constraints;
- risk tolerance;
- investment experience;
- emotional decision patterns;
- current open tasks;
- preferred response style.

## Not save-worthy by default

Do not save:
- hypothetical test cases;
- fake development examples;
- one-off numbers from simulations;
- product examples not belonging to the user;
- sensitive personal details unless clearly relevant and consented.

## Test mode protection

Development/test scenarios must not be saved as real user memory unless explicitly confirmed.

Possible rule:
If client was reset recently or message appears to be a test case, eCoach should not update memory silently.

Better future implementation:
- TEST_MODE=true for development users;
- in test mode, memory updates are logged but not applied unless user confirms.

---

# 5. Telegram memory buttons

The buttons should become a memory interface.

Current buttons:
- Resumen de quiÃ©n soy yo
- Resumen de quÃ© quiero
- Resumen de quÃ© tengo que hacer

When clicked, eCoach should:
1. Show current file content.
2. Offer actions:
   - AÃ±adir dato
   - Corregir dato
   - Borrar dato
   - Reorganizar resumen
   - Volver
3. User replies naturally.
4. eCoach proposes exact patch.
5. User confirms.
6. File is updated.
7. Backup is created.

## Example flow

User clicks:
"Resumen de quiÃ©n soy yo"

Bot shows:
current quien_soy.md

Bot asks:
"Â¿Quieres aÃ±adir, corregir o borrar algo?"

User:
"AÃ±ade que mis gastos familiares son 2.500â‚¬/mes."

Bot:
"Propongo aÃ±adir en Trabajo e ingresos / Relaciones actual:
- Gastos familiares recurrentes aproximados: 2.500â‚¬/mes.

Â¿Confirmas?"

Buttons:
- Confirmar
- Editar
- Cancelar

---

# 6. Follow-up object schema

Follow-ups should be structured objects, not vague notes.

Example:

{
  "id": "fup_20260603_001",
  "client_id": "telegram_7960326623",
  "title": "Revisar respuesta del banco sobre amortizaciÃ³n",
  "third_party": "banco",
  "waiting_for": "SimulaciÃ³n amortizando 25.000â‚¬ reduciendo plazo y reduciendo cuota",
  "created_at": "2026-06-03",
  "due_at": "2026-06-05",
  "status": "open",
  "priority": "normal",
  "source_message": "...",
  "next_prompt": "Â¿Te respondiÃ³ el banco sobre la simulaciÃ³n de amortizaciÃ³n?"
}

## Follow-up fields

Required:
- id
- title
- third_party or internal_task
- waiting_for
- created_at
- due_at
- status
- next_prompt

Optional:
- priority
- notes
- related_memory_file
- related_case_type
- last_reminded_at
- snoozed_until

## Follow-up statuses

- open
- waiting
- snoozed
- done
- cancelled

---

# 7. Follow-up creation flow

When eCoach gives a third-party message, it should often propose a follow-up:

"Â¿Quieres que te lo recuerde maÃ±ana si no has recibido respuesta?"

But it should not overdo it.

Follow-up should be proposed when:
- user needs third-party response;
- decision depends on that response;
- delay is likely;
- forgetting would create risk.

Follow-up should not be proposed for every trivial message.

## Commands/buttons

- /followups
- Ver follow-ups
- Marcar hecho
- Posponer
- Borrar
- AÃ±adir manualmente
- Recordarme maÃ±ana
- Recordarme en una semana

---

# 8. Morning proactivity

Morning message should help the client act.

Example:

"Buenos dÃ­as. Tienes 2 temas abiertos:

1. Gestor/notario: confirmar impuestos y gastos pendientes de la herencia.
2. Banco: esperar simulaciÃ³n de amortizaciÃ³n de hipoteca.

El bloqueo principal es el gestor/notario, porque sin saber el dinero neto no conviene decidir sobre hipoteca o inversiÃ³n.

PrÃ³xima acciÃ³n: enviar o reenviar el mensaje al gestor."

## Morning message logic

Each morning:
1. Load open follow-ups.
2. Load que_tengo_que_hacer.md.
3. Identify highest-priority blocker.
4. Send one short message.
5. Avoid overwhelming list.
6. Include one action.

## Proactivity levels

- off
- light: only explicit reminders
- normal: morning summary + due follow-ups
- strong: proactive prioritization and suggested next action

Client should be able to choose.

---

# 9. Quality rules that belong in orchestrator, not playbooks

These are universal:

## Arithmetic before homework
If the user gives numbers, calculate what can already be calculated before asking for more data.

## Third-party action packaging
If the next action involves a third party, provide exact wording/questions.

## One next action
Final next action should normally be one concrete action.

## No vague homework
Do not say "ask the bank" or "check with advisor" without packaging the action.

## Burden of proof
Complex/expensive/illiquid/opaque products must justify themselves.

## Client safety first
Emergency fund, family obligations and core stability come before optional investments.

## Do not overclaim
Calculations must be clearly approximate when based on assumptions.

---

# 10. Implementation order

Recommended next implementation steps:

1. Create official initial memory templates in InitialClientFiles.
2. Add memory display/edit flows for Telegram buttons.
3. Add conservative memory-update proposal flow.
4. Add TEST_MODE or memory-update confirmation protection.
5. Improve follow-up schema/storage.
6. Add follow-up buttons/commands.
7. Add morning proactive message logic.
8. Build evaluation battery:
   - ladder mode;
   - pro-only mode;
   - compare answer quality, latency, cost and false-pass rate.

---

# 11. Current development principle

Do not keep adding playbooks endlessly.

Only add a playbook when:
- a reusable financial force is missing;
- repeated failures show the current modules cannot handle it;
- the new playbook will cover many future cases.

Prefer improving:
- router dimensions;
- orchestrator universal rules;
- memory templates;
- follow-up/proactivity logic;
- evaluation.

