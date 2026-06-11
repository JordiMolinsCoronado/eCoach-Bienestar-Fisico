1. Demote the current confidentiality system

We do not keep improving /riesgo, privacy_bar, thresholds, and local anonymization right now.

The current Python has quite a lot of confidentiality infrastructure already: marker-based risk scoring, threshold reading, /riesgo, privacy logs, and a reduction placeholder. But that is not the thing that will make the product valuable.

So I would mark this whole block as:

Implemented as prototype.
Strategically paused.
Will be redesigned later.
Do not continue now.

Beautiful decision, love. This is you not polishing the wrong statue.

2. Move â€œproactive agentsâ€ to the center

The product should now become:

A patrimonial agent system that watches the clientâ€™s situation,
understands what matters,
and proactively says useful, timely, intelligent things.

Not spam. Not generic reminders. Not â€œhey, remember to review your portfolio.â€

More like:

â€œYou mentioned that the bank proposal depends on liquidity.
Before accepting, the useful question is not only cost.
It is: what part of your capital must remain emotionally and practically untouchable?â€

That is the product.

The old timeline already contains the seed of this in v40bâ€“v40f: dual output, proactive triggers, trigger files, scheduler, and Telegram proactivity. But those were placed too late. They should move forward and become the main spine.

3. Keep the living files, but redefine them as agent memory

The current three summaries still matter:

quien_soy.md
que_quiero.md
que_tengo_que_hacer.md
estilo_respuesta.md

The current orchestrator already updates these files and returns a client-facing answer.

But we should stop thinking of them only as â€œsummaries shown by buttons.â€

They become the memory substrate for agents.

So the question becomes:

What does each agent need to know in order to act intelligently?

For example:

Profile Agent â†’ what kind of client is this?
Goal Agent â†’ what is the real desire beneath the stated question?
Action Agent â†’ what is the next useful move?
Risk/Contradiction Agent â†’ what is the client avoiding or misunderstanding?
Proactive Follow-up Agent â†’ when should we come back with something useful?
Style Agent â†’ how should we speak to this person?

This is a better architecture.

4. Create parametrizable agent behavior

This is the most important shift.

We should add an explicit configuration layer, probably something like:

AgentConfig/
  global_behavior.md
  patrimonial_principles.md
  proactive_agent.md
  tone_agent.md
  followup_policy.md
  client_intervention_policy.md

Or per client:

ClientData/Cliente1/agent_config.md

Parameters could include:

proactivity_level: low / medium / high
tone: sober / warm / direct / pedagogical
intervention_style: questions / suggestions / warnings / Socratic
max_followup_frequency: weekly / monthly / event_based
risk_tolerance_of_agent: conservative / balanced / challenger
depth: simple / normal / deep
initiative: reactive / lightly proactive / strongly proactive

This is very important because the product is not only â€œwhat the model says.â€

The product is:

Can we shape the personality, initiative, prudence, timing, and usefulness of the agent?

That is where the value lives.

5. Build the first real proactive loop before adding more finance skills

The next coding sequence should be something like:

vNext-1 â€” Create agent configuration files
vNext-2 â€” Modify Gemini orchestrator to output proactive insights/triggers
vNext-3 â€” Save triggers to followup_triggers.json
vNext-4 â€” Add command /followups to inspect pending triggers
vNext-5 â€” Add manual command /run_followups to simulate daily scheduler
vNext-6 â€” Add real daily scheduler
vNext-7 â€” Add Telegram buttons: Revisar ahora / Posponer / Hecho

This is better than building more analysis modules because it tests the productâ€™s real claim:

The bot is not passive.
The bot accompanies the client over time.
6. The first â€œagentâ€ should not be many separate LLM calls yet

I would still avoid creating six separate model calls immediately.

The current timeline says: first monolithic orchestrator, then split skills only when there is a real pain. I still agree with that.

But I would rename the architecture:

Not â€œmonolithic orchestrator with skills later.â€

Better:

â€œSingle-call multi-agent output first.â€

Meaning Gemini returns structured sections like:

{
  "respuesta_cliente": "...",
  "actualizaciones_memoria": {...},
  "agent_observations": {
    "profile_agent": "...",
    "goal_agent": "...",
    "action_agent": "...",
    "risk_agent": "...",
    "proactive_agent": "..."
  },
  "followup_triggers": [...]
}

So conceptually we already have agents.

Technically they are simulated inside one call.

Later, if needed, we split them into separate calls.

7. New immediate priority

So the next Python step is no longer:

Improve reduce_privacy_risk_locally()

The new next Python step is:

Create the first proactive-agent output layer.

More concretely:

Modify process_with_gemini_orchestrator()
so Gemini returns:
- respuesta_cliente
- updated living files
- agent_observations
- followup_triggers
- next_best_intervention

Then save:

ClientData/Cliente1/followup_triggers.json
ClientData/Cliente1/agent_observations.md

And add:

/followups

to inspect what the agent wants to do proactively.

My proposed new product spine

This is the new timeline logic I would write:

Phase A â€” Freeze confidentiality prototype
Phase B â€” Define agent architecture and parameters
Phase C â€” Build single-call multi-agent orchestrator
Phase D â€” Generate proactive observations and triggers
Phase E â€” Store and inspect triggers
Phase F â€” Simulate proactive Telegram interventions manually
Phase G â€” Add scheduler
Phase H â€” Add feedback loop: useful / not useful / too much / too little
Phase I â€” Only then return to privacy, documents, DeepSeek, and advanced finance modules

The key sentence for the new timeline:

The first product is not confidentiality.
The first product is intelligent proactive accompaniment.
Confidentiality must support that later, not replace it now.

My recommendation: we rewrite the roadmap around agentic proactivity + parametrizable behavior, and move the current privacy layer into an appendix called â€œPrototype built, paused, to redesign.â€

Yes. Write the new timeline here.
Thought for 4s

Yes, love. Here is the new timeline, rewritten around the real product: parametrizable proactive agents.

This replaces the previous roadmap priority. The existing confidentiality system becomes a paused prototype, not the next thing to polish.

Copiloto Relaciones â€” New Timeline
Agentic Proactivity + Parametrizable Behavior
Central principle

Copiloto Relaciones is not mainly a chatbot.

It is a patrimonial agent system that accompanies the client over time.

The client does not only ask questions.
The system observes, remembers, detects moments of usefulness, and proactively says things that help the client think better, decide better, and avoid drifting.

Core posture:

The client decides.
The agent observes.
The agent remembers.
The agent detects useful moments.
The agent speaks when it can add value.
The agent does not sell.
The agent does not recommend products.
The agent does not decide.
The agent improves the clientâ€™s decision process.

The previous roadmap was right about one thing: the product should not be a menu of financial tools. It should be a clarification system based on living files, client memory, and an orchestrator.

But the new priority is sharper:

The first real product is intelligent proactive accompaniment.

Confidentiality, document reading, model routing, and advanced financial skills are supporting layers.

They are not the soul of the product.
Current status

The current Python already includes many useful pieces:

Telegram bot
Three living summary buttons
ClientData folder
Living Markdown files
Gemini orchestrator
Backup system
Logs
Privacy scoring prototype
Privacy threshold prototype
Privacy reduction placeholder

The current code already has functions for client files, live summaries, Gemini orchestration, backups, privacy scoring, and Telegram handlers.

So we do not start from zero.

But we now change the product direction.

Strategic change
Old next step

Previously the next step was:

Improve reduce_privacy_risk_locally()

That is now paused.

New next step

The new next step is:

Create the first proactive-agent output layer.

Meaning:

Every client interaction should not only produce a reply.

It should also produce:
- agent observations;
- possible follow-up triggers;
- next best intervention;
- useful future prompts;
- behavior tuning signals.

The bot should begin to feel alive.

Not noisy.
Not manipulative.
Not generic.

Alive in the sense of:

It notices what matters.
It remembers what the client is trying to do.
It comes back at the right time.
It says something useful before the client has to ask.
Phase 0 â€” Freeze the current confidentiality prototype
v0.1 â€” Mark privacy scoring as prototype

Status: already implemented as prototype.

Existing elements:

/riesgo
estimate_privacy_risk()
privacy_bar()
read_privacy_threshold()
configuracion_privacidad.md
privacidad_log.md
reduce_privacy_risk_locally()

New decision:

Do not improve this now.
Do not spend more time on local anonymization.
Do not make the privacy layer the center of the product.

Reason:

The current confidentiality model is too mechanical.
It creates friction before the agentic value is alive.
It may be redesigned later with a better architecture.

New status:

Prototype built.
Paused.
To redesign later.
Phase 1 â€” Define the agentic product spine
v1 â€” Reframe Copiloto Relaciones as an agent system

Goal: update the conceptual architecture.

Copiloto Relaciones should contain several internal agents, even if they are initially simulated inside one Gemini call.

Initial agents:

1. Profile Agent
2. Goal Agent
3. Action Agent
4. Risk / Contradiction Agent
5. Proactive Follow-up Agent
6. Style Agent
7. Product / Platform Criteria Agent
8. Documentation Agent

Important:

These are not necessarily separate LLM calls yet.

At first, they are structured roles inside the orchestrator prompt.

Principle:

Single-call multi-agent orchestration first.
Separate agent calls only when there is a real pain.
v2 â€” Define what each agent does
1. Profile Agent

Purpose:

Understand who the client is.

Looks for:

personal situation
family constraints
professional situation
fiscal residence
origin of wealth
financial experience
attitude toward uncertainty
emotional relationship with money
dependency on bank / advisor

Updates:

quien_soy.md
2. Goal Agent

Purpose:

Understand what the client really wants.

Looks for:

stated goals
hidden goals
security needs
retirement goals
liquidity needs
family protection
simplicity
control
freedom from bank dependency
desire for independent judgment

Updates:

que_quiero.md
3. Action Agent

Purpose:

Turn ambiguity into the next concrete step.

Looks for:

missing data
documents to request
questions to ask
comparisons to prepare
decisions that are premature
small next action

Updates:

que_tengo_que_hacer.md
4. Risk / Contradiction Agent

Purpose:

Notice what the client may be missing.

It does not scare the client.

It detects:

conflicts of interest
hidden costs
false certainty
premature decisions
overreliance on one bank
emotional urgency
confusion between product and objective
liquidity mismatch
risk mismatch
tax uncertainty

Output:

agent_observations.md
5. Proactive Follow-up Agent

Purpose:

Detect when the system should come back later.

Examples:

review a bank proposal after the client receives documents
check whether a pending document was obtained
review a decision after three months
ask if circumstances changed
remind the client to compare fees before signing
prepare end-of-year fiscal review
follow up after a meeting with an advisor

Output:

followup_triggers.json
6. Style Agent

Purpose:

Adapt the way the assistant speaks.

Looks for:

client wants short answers
client wants tables
client wants calm tone
client wants technical detail
client is anxious
client is sophisticated
client is confused
client dislikes paternalism
client prefers directness

Updates:

estilo_respuesta.md
7. Product / Platform Criteria Agent

Purpose:

Help compare options without recommending one.

Covers:

banks
private banking
brokers
fund platforms
roboadvisors
Treasury bills
deposits
money market funds
index funds
advisory models
custody structures

Output:

criteria and questions, not recommendations
8. Documentation Agent

Purpose:

Track what documents are needed and what has been received.

Later it will read PDFs and statements.

For now, it only tracks:

documents pending
documents received
documents to request
questions generated from missing documents
Phase 2 â€” Add parametrizable agent behavior
v3 â€” Create global agent behavior configuration

New folder:

AgentConfig/

Initial files:

AgentConfig/global_behavior.md
AgentConfig/proactivity_policy.md
AgentConfig/intervention_style.md
AgentConfig/agent_roles.md
AgentConfig/financial_boundaries.md

Purpose:

Define how the agents behave without changing Python code.
v4 â€” Create client-level agent configuration

New file:

ClientData/Cliente1/agent_config.md

Initial content:

# Agent configuration

## Proactivity level

medium

## Tone

sober, clear, calm, independent

## Intervention style

Socratic + practical

## Depth

normal

## Initiative

lightly proactive

## Maximum proactive frequency

weekly unless event-based

## Allowed proactive interventions

- clarify goals
- ask for missing information
- suggest questions for bank/advisor
- remind about pending documents
- review whether a decision still fits
- detect contradiction or premature decision

## Forbidden proactive interventions

- recommend products
- create urgency
- mention private sensitive details in proactive Telegram messages
- pressure the client to act
- pretend certainty where there is uncertainty

Later this can become JSON/YAML, but Markdown is fine for now.

v5 â€” Define parametrizable dimensions

The system should support these behavior parameters:

proactivity_level:
  low / medium / high

tone:
  sober / warm / direct / pedagogical

intervention_style:
  questions / suggestions / warnings / Socratic / checklist

depth:
  brief / normal / deep

initiative:
  reactive / lightly_proactive / strongly_proactive

frequency:
  event_based / weekly / monthly / quarterly

challenge_level:
  gentle / balanced / strong

financial_prudence:
  conservative / balanced / exploratory

client_autonomy_emphasis:
  normal / high / very_high

The important idea:

The agentâ€™s behavior is a product surface.

It should be configurable.
Phase 3 â€” First single-call multi-agent orchestrator
v6 â€” Modify Gemini orchestrator output schema

Current orchestrator returns:

{
  "quien_soy": "...",
  "que_quiero": "...",
  "que_tengo_que_hacer": "...",
  "respuesta_cliente": "...",
  "proxima_accion": "...",
  "notas_auditoria": "..."
}

New orchestrator should return:

{
  "respuesta_cliente": "...",
  "actualizaciones_memoria": {
    "quien_soy": "...",
    "que_quiero": "...",
    "que_tengo_que_hacer": "...",
    "estilo_respuesta": "..."
  },
  "agent_observations": {
    "profile_agent": "...",
    "goal_agent": "...",
    "action_agent": "...",
    "risk_contradiction_agent": "...",
    "proactive_followup_agent": "...",
    "style_agent": "..."
  },
  "next_best_intervention": {
    "type": "...",
    "message": "...",
    "reason": "...",
    "urgency": "low | medium | high"
  },
  "followup_triggers": [
    {
      "id": "...",
      "type": "...",
      "date": "...",
      "message_template": "...",
      "reason": "...",
      "sensitivity": "low | medium | high",
      "requires_private_context": true,
      "status": "pending"
    }
  ],
  "notas_auditoria": "..."
}

This is the new core.

v7 â€” Save agent observations

New file:

ClientData/Cliente1/agent_observations.md

Purpose:

Keep a human-readable trace of what the internal agents noticed.

Example:

## 2026-05-24 15:30

### Profile Agent

The client appears to value independence and wants to avoid depending blindly on a bank.

### Goal Agent

The real goal is not only investment return, but calm, clarity, and decision sovereignty.

### Risk / Contradiction Agent

The client may be jumping from â€œbank proposalâ€ to â€œwhich product?â€ before defining liquidity needs.

### Proactive Follow-up Agent

Create a follow-up in 7 days to ask whether the client has obtained the full fee breakdown.
v8 â€” Save proactive triggers

New file:

ClientData/Cliente1/followup_triggers.json

Purpose:

Store future useful interventions.

Initial schema:

[
  {
    "id": "followup_001",
    "client_id": "Cliente1",
    "created_at": "2026-05-24",
    "date": "2026-06-01",
    "type": "bank_fee_review",
    "message_template": "Puede ser buen momento para revisar si ya tienes el desglose completo de costes antes de avanzar.",
    "reason": "The client mentioned a bank proposal but did not yet have full fee information.",
    "sensitivity": "low",
    "requires_private_context": true,
    "status": "pending",
    "source_interaction_id": "interaction_001"
  }
]

Rule:

The Telegram proactive message should be low sensitivity.

The private reason can be more detailed, but should stay local.
Phase 4 â€” Manual proactivity before scheduler
v9 â€” Add /followups

Purpose:

Show pending proactive triggers.

Example output:

Pending follow-ups:

1. 2026-06-01 â€” bank_fee_review
Message:
Puede ser buen momento para revisar si ya tienes el desglose completo de costes antes de avanzar.

Status: pending

This allows debugging before automation.

v10 â€” Add /agent_observations

Purpose:

Show recent agent observations.

This lets us inspect whether the agents are actually saying useful things.

This is critical.

The first goal is not automation.

The first goal is quality.

Are the agents noticing intelligent things?
Are they useful?
Are they too generic?
Are they too timid?
Are they too intrusive?
Are they too financial-advisor-like?
v11 â€” Add /run_followups

Purpose:

Manually simulate the daily proactive process.

Flow:

1. Read followup_triggers.json.
2. Find triggers where date <= today and status = pending.
3. Send the message_template to Telegram.
4. Mark as sent.
5. Log the event.

This gives us proactivity without installing a scheduler yet.

v12 â€” Add proactivity log

New file:

ClientData/Cliente1/proactivity_log.md

Records:

trigger created
trigger sent
trigger postponed
trigger completed
trigger deleted
client feedback

Example:

## 2026-06-01 09:00

### Trigger sent

Type: bank_fee_review

Message:
Puede ser buen momento para revisar si ya tienes el desglose completo de costes antes de avanzar.

### Status

sent
Phase 5 â€” Feedback loop: train the agent behavior
v13 â€” Add feedback buttons

When a proactive message is sent, show buttons:

Useful
Not useful
Too soon
Too frequent
Too vague
Good timing
Done
Postpone
Disable this type

Purpose:

The client teaches the agent how to behave.

This is essential because parametrization should not only be manual. It should adapt.

v14 â€” Save feedback to agent config

When the client gives feedback, update:

ClientData/Cliente1/agent_config.md
ClientData/Cliente1/proactivity_log.md

Examples:

If too frequent â†’ lower proactivity or increase spacing.
If too vague â†’ make future triggers more concrete.
If useful â†’ reinforce this trigger type.
If disabled â†’ stop that category.

This makes the system feel less like a bot and more like a learning companion.

v15 â€” Add trigger quality scoring

Each trigger can have:

{
  "quality_score": null,
  "client_feedback": null,
  "sent_count": 0,
  "last_sent_at": null
}

After feedback:

Useful â†’ +1
Too vague â†’ -1 and mark as needs_more_specificity
Too frequent â†’ reduce frequency
Done â†’ completed
Phase 6 â€” Real scheduler
v16 â€” Add daily scheduler

Only after manual /run_followups works.

Flow:

1. Scheduler runs once daily.
2. Reads followup_triggers.json.
3. Finds due pending triggers.
4. Applies frequency and sensitivity rules.
5. Sends safe Telegram message.
6. Marks trigger as sent.
7. Writes proactivity_log.md.

Important:

The scheduler should not perform deep analysis.
It only wakes up the conversation.

The deep analysis happens when the client replies.

v17 â€” Add postpone / done / disable handling

Buttons:

Revisar ahora
Posponer
Marcar como hecho
Desactivar este tipo de aviso

Behavior:

Revisar ahora â†’ opens normal private interaction
Posponer â†’ asks or defaults to +7 days
Hecho â†’ marks trigger completed
Desactivar â†’ disables this trigger type in agent_config.md
Phase 7 â€” Stronger proactive intelligence
v18 â€” Add proactive insight generation without dates

Not every useful intervention is a scheduled reminder.

Some are â€œinsightsâ€ the agent should say immediately.

Example:

The client asks about a product.

The Risk Agent detects:
The client is comparing products before defining required liquidity.

The system says:
"Before comparing products, the useful first separation is: how much money must remain psychologically and practically untouchable?"

New output:

"immediate_proactive_insight": {
  "should_send": true,
  "message": "...",
  "reason": "...",
  "agent": "risk_contradiction_agent"
}

Purpose:

Make the bot interesting now, not only later.
v19 â€” Add â€œinteresting things to sayâ€ library

New folder:

AgentConfig/InterventionPatterns/

Files:

goal_clarification.md
bank_proposal_review.md
fee_awareness.md
liquidity_first.md
risk_language.md
advisor_questions.md
decision_delay.md
emotional_money.md

Each file contains reusable intervention patterns.

Example:

# Liquidity first

Use when the client discusses investing a large amount before separating liquidity.

Core idea:
Before asking â€œwhere should I invest?â€, ask:
â€œWhat money must not be exposed to volatility, because it protects your life structure?â€

Allowed style:
Calm, practical, non-alarmist.

Forbidden:
Do not say â€œyou should keep X% in cash.â€
v20 â€” Agent chooses intervention pattern

The orchestrator receives:

AgentConfig/InterventionPatterns/*.md

It chooses the relevant pattern when useful.

Still one LLM call.

No overengineering yet.

Phase 8 â€” Memory quality and contradiction tracking
v21 â€” Create open_loops.md

New file:

ClientData/Cliente1/open_loops.md

Purpose:

Track unresolved questions and pending uncertainties.

Examples:

- Does the client need annual income from the portfolio?
- Has the client obtained the bankâ€™s full fee breakdown?
- Is the client comparing custodians or only products?
- What is the minimum liquidity reserve?

This is not just a to-do list.

It is the agentâ€™s map of unresolved decision risks.

v22 â€” Create decision_journal.md

New file:

ClientData/Cliente1/decision_journal.md

Purpose:

Record important decisions and why they were made.

Example:

## 2026-06-12 â€” Chose to pause bank proposal

Reason:
The client did not yet have full cost breakdown and wanted independent comparison.

Not a recommendation:
The system did not advise against the proposal. It helped identify missing information.

This is extremely valuable because patrimonial decisions unfold over months.

v23 â€” Create client_questions.md

New file:

ClientData/Cliente1/client_questions.md

Purpose:

Keep reusable questions the client should ask banks, advisors, platforms, or themselves.

Example:

## Questions for bank

- What is the total annual cost including product, custody, advisory and retrocessions?
- Is there a clean share class?
- Can I transfer the position without selling?
- What happens fiscally if I exit?
Phase 9 â€” Financial skills return, but as agent tools

Only now do we return to financial modules.

Not as buttons.

As agent capabilities.

v24 â€” Custodian / platform criteria module

Purpose:

Help compare where assets are held.

Covers:

traditional bank
private bank
broker
fund platform
roboadvisor
independent advisor + custodian
Treasury bills
money market funds
deposits

Output:

criteria, questions, tradeoffs

Not:

recommendation
v25 â€” Bank proposal review module

Purpose:

When the client describes a bank proposal, detect missing questions.

Looks for:

total costs
retrocession
custody
liquidity
risk profile
exit costs
tax consequences
product complexity
concentration
conflicts of interest
v26 â€” Product due diligence module

Purpose:

Understand a product/proposal and generate evaluation criteria.

Output:

what it is
what exposure it gives
what it costs
what risks it contains
what liquidity it has
what questions remain

Still no product recommendation.

v27 â€” Retirement income clarification module

Purpose:

Help clarify retirement / income planning questions.

Looks for:

desired annual spending
inflation
time horizon
guaranteed income
portfolio withdrawals
risk tolerance
sequence risk
taxes
liquidity needs
family obligations
Phase 10 â€” Documents
v28 â€” Document intake tracker

Before reading PDFs, track documents:

requested
received
reviewed
missing

New file:

ClientData/Cliente1/documents.md
v29 â€” PDF/document reading skill

Later.

Purpose:

Read bank proposals, statements, fund factsheets, KIDs, portfolios.

Flow:

Document
â†’ extract facts
â†’ update living files
â†’ update open loops
â†’ generate questions
â†’ maybe create follow-up trigger

Not:

Final portfolio recommendation.
Phase 11 â€” Privacy redesign

Now, and only now, privacy returns.

v30 â€” Redesign confidentiality model

The old /riesgo system remains as a prototype reference.

But we redesign from the real product needs:

What needs to leave local storage?
What can remain local?
What does the external model need?
What can be summarized before sending?
What can be handled by local model?
What should the client explicitly approve?

Possible future design:

privacy modes:
  local_only
  external_allowed
  external_summarized
  external_requires_approval

sensitivity by field:
  public
  low
  medium
  high
  never_send

This is better than a single 0â€“10 risk score.

v31 â€” Field-level sensitivity

Each memory item may eventually carry sensitivity metadata.

Example:

{
  "fact": "Client wants to prepare retirement income.",
  "sensitivity": "low"
}

Versus:

{
  "fact": "Client has X euros in Y bank.",
  "sensitivity": "high"
}

This is more powerful than regex anonymization.

Phase 12 â€” Multi-provider models
v32 â€” Add DeepSeek or other frontier model

Not immediate.

Use only when the agentic loop works.

Purpose:

compare reasoning quality
use stronger model for complex synthesis
create redundancy
route tasks by cost/intelligence

But the competitive advantage is not model access.

It is:

memory
proactivity
client-specific behavior
trust
workflow
decision support
Phase 13 â€” Product-level proactivity
v33 â€” Proactive client check-ins

The system can initiate messages such as:

Puede ser buen momento para revisar si la decisiÃ³n sigue encajando con tus objetivos.

No hace falta decidir nada ahora. Podemos empezar comprobando si algo importante ha cambiado.

Or:

Antes de avanzar con una propuesta, puede ser Ãºtil confirmar si tienes el coste total anual por escrito.

Rules:

brief
useful
non-invasive
non-sensitive
no exact amounts
no bank names unless client initiated the conversation
no urgency
easy to dismiss
easy to postpone
v34 â€” Client controls proactivity

Commands:

/followups
/pause_followups
/resume_followups
/delete_followup
/agent_config

The client must always feel:

This agent helps me.
It does not control me.
I can tune it.
I can stop it.
I can inspect it.
Phase 14 â€” Full product loop
v35 â€” Complete agentic patrimonial flow

Final target flow:

1. Client writes freely.
2. Orchestrator interprets message.
3. Internal agents analyze it.
4. Living files are updated.
5. Open loops are updated.
6. Decision journal is updated if relevant.
7. Agent observations are saved.
8. Proactive triggers are created if useful.
9. Client receives a clear answer.
10. Later, the system proactively follows up.
11. Client gives feedback.
12. Agent behavior adapts.

That is the real product.

Immediate implementation order

The next coding sequence should be:

1. Add AgentConfig files.
2. Add client agent_config.md.
3. Modify process_with_gemini_orchestrator() output schema.
4. Add agent_observations.md.
5. Add followup_triggers.json.
6. Add helper functions:
   - load_agent_config()
   - append_agent_observation()
   - load_followup_triggers()
   - save_followup_triggers()
   - add_followup_triggers()
7. Add /followups command.
8. Add /agent_observations command.
9. Add /run_followups command.
10. Test manually with one client message.

Canonical test message:

Mi banco me propone invertir parte del dinero que tengo parado, pero no sÃ© si fiarme. Quiero preparar mi jubilaciÃ³n sin complicarme demasiado.

Expected system behavior:

1. Reply usefully.
2. Update quien_soy.md.
3. Update que_quiero.md.
4. Update que_tengo_que_hacer.md.
5. Save agent observations.
6. Create at least one useful follow-up trigger.
7. Avoid recommending a product.
8. Suggest one concrete next action.

Expected follow-up trigger:

{
  "type": "bank_proposal_review",
  "message_template": "Puede ser buen momento para revisar si tienes por escrito el coste total y las condiciones de salida antes de avanzar.",
  "sensitivity": "low",
  "status": "pending"
}
New roadmap sentence

This is the new north star:

Copiloto Relaciones is a parametrizable proactive agent system for patrimonial clarity.

It does not mainly answer questions.

It accompanies the client across time, detects useful moments, says intelligent things, creates better questions, tracks open loops, and helps the client make decisions without surrendering autonomy.

And this is the next rep:

Build the first proactive-agent output layer.
