# Agent roles

The system contains several internal agents.

At this stage, these agents are not separate LLM calls.
They are structured roles inside one orchestrator call.

## Profile Agent

Understands who the client is.

Looks for:
- personal situation;
- family constraints;
- professional situation;
- fiscal residence;
- origin of wealth;
- financial experience;
- attitude toward uncertainty;
- emotional relationship with money;
- dependency on bank or advisor.

Updates:
- quien_soy.md

## Goal Agent

Understands what the client really wants.

Looks for:
- stated goals;
- hidden goals;
- security needs;
- retirement goals;
- liquidity needs;
- family protection;
- simplicity;
- control;
- freedom from bank dependency;
- desire for independent judgment.

Updates:
- que_quiero.md

## Action Agent

Turns ambiguity into a concrete next step.

Looks for:
- missing data;
- documents to request;
- questions to ask;
- comparisons to prepare;
- decisions that are premature;
- small next action.

Updates:
- que_tengo_que_hacer.md

## Risk / Contradiction Agent

Notices what the client may be missing.

Looks for:
- conflicts of interest;
- hidden costs;
- false certainty;
- premature decisions;
- overreliance on one bank;
- emotional urgency;
- confusion between product and objective;
- liquidity mismatch;
- risk mismatch;
- tax uncertainty.

Outputs:
- agent observations;
- useful warnings;
- better questions.

## Proactive Follow-up Agent

Detects when the system should come back later.

Looks for:
- pending documents;
- upcoming meetings;
- decisions that should be reviewed;
- cost information still missing;
- proposals that need comparison;
- moments where the client may drift.

Outputs:
- followup triggers.

## Style Agent

Adapts how the assistant speaks.

Looks for:
- client wants short answers;
- client wants tables;
- client wants calm tone;
- client wants technical detail;
- client is anxious;
- client is sophisticated;
- client is confused;
- client dislikes paternalism;
- client prefers directness.

Updates:
- estilo_respuesta.md
