# eCoach AI Call Ladder Architecture

## Purpose

Reduce cost and latency while preserving answer quality.

The system should not use the strongest / slowest model by default.
It should first try a fast grounded answer using the right files, and escalate only when that answer is not good enough.

## Call 1: Fast router call

Always use a fast model.

Responsibilities:
- classify the user message;
- decide whether the orchestrator is needed;
- if no orchestrator is needed, provide a short direct response;
- select the client files needed;
- select the knowledge files needed;
- set the semantic depth of the case;
- detect possible memory updates;
- detect possible follow-up extraction.

If the message is simple, such as â€œHolaâ€, â€œGraciasâ€, or a basic help request:
- needs_orchestrator=false;
- return direct_response;
- stop.

If the message requires patrimonial/financial analysis:
- needs_orchestrator=true;
- select exactly the needed files, not more and not less.

## Call 2: Fast grounded answer call

Use a fast model with the selected client and knowledge files.

The answer call must return structured JSON with:

- respuesta_cliente;
- quality_self_check.

The quality_self_check must be binary, not medium-confidence.

Example:

{
  "respuesta_cliente": "...",
  "quality_self_check": {
    "good_enough": true,
    "needs_stronger_model": false,
    "reason": "The answer covers the relevant risks, uses the available numbers, compares against the correct baseline and gives a clear next action.",
    "known_limitations": [
      "Exact product payoff cannot be analyzed without ISIN/KID."
    ],
    "missing_information_needed": [
      "ISIN",
      "KID",
      "full cost disclosure"
    ]
  }
}

## Call 3: Strong escalation call

Use a stronger model only if Call 2 says:

- good_enough=false; or
- needs_stronger_model=true; or
- the Call 2 JSON is invalid and cannot be repaired; or
- the Call 2 answer is empty or technically broken.

The strong model receives:
- original user message;
- selected client files;
- selected knowledge files;
- Flash draft answer;
- Flash quality_self_check.

The strong model should improve/correct the answer, not unnecessarily expand it.

## Deterministic rules

Do not use deterministic financial-content rules such as:
- must mention coupon;
- must mention barrier;
- must mention issuer risk.

Those can be wrong depending on the product.

Use deterministic rules only for technical failures:
- invalid JSON;
- missing respuesta_cliente;
- empty answer;
- promised copy-paste message missing;
- timeout;
- Telegram send failure.

Semantic quality should be judged by the model through quality_self_check.

## Evaluation plan

For each product case, compare:

A. Ladder mode:
   router â†’ fast grounded answer â†’ strong model only if needed.

B. Pro-only mode:
   router â†’ strong model.

For each case, record:
- selected files;
- model(s) used;
- input tokens;
- output tokens;
- total cost;
- latency;
- final answer quality;
- whether escalation happened;
- whether escalation was useful;
- whether Flash falsely passed.

Main metric:
False pass rate must be very low.

If Flash often says good_enough=true but the answer is not good enough, tighten the self-check prompt or add escalation conditions.

If Flash answers are consistently good enough, keep Flash as default and use Pro rarely.

## Working principle

Playbooks carry expertise.
Fast models should be enough for many standard cases when the right playbooks are selected.
Strong models are reserved for genuinely difficult, ambiguous, high-stakes or failed-quality cases.

