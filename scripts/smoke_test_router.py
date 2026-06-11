import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import eCoach_Relaciones as bot


CLIENT_NAME = "telegram_7960326623"


def assert_condition(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> None:
    bot.set_current_client_name(CLIENT_NAME)
    bot.ensure_client_files()

    tests = [
        {
            "name": "smalltalk",
            "input": "Hola",
            "expected_route": "smalltalk",
            "needs_orchestrator": False,
        },
        {
            "name": "memory fact",
            "input": "Tengo 51 aÃ±os y vivo en Barcelona.",
            "expected_routes": {"memory_update", "simple_response"},
            "needs_orchestrator": False,
            "expects_should_update_memory": True,
        },
        {
            "name": "explicit followup",
            "input": "RecuÃ©rdame maÃ±ana revisar la respuesta del banco.",
            "expected_route": "followup_management",
            "needs_orchestrator": False,
            "expects_followup_triggers": True,
        },
        {
            "name": "ambiguous future event",
            "input": "El banco me contestarÃ¡ maÃ±ana sobre la simulaciÃ³n.",
            "expected_route": "simple_response",
            "needs_orchestrator": False,
            "expects_no_followup_triggers": True,
        },
    ]

    errors: list[str] = []

    for test in tests:
        decision = bot.route_user_message(test["input"])

        route = decision.get("route")
        needs_orchestrator = decision.get("needs_orchestrator")
        followup_triggers = decision.get("followup_triggers", [])
        direct_response = str(decision.get("direct_response", "") or "")

        expected_route = test.get("expected_route")
        expected_routes = test.get("expected_routes")

        if expected_routes is not None:
            assert_condition(
                route in expected_routes,
                f"{test['name']}: expected route in {expected_routes}, got {route}. Decision: {decision}",
                errors,
            )
        else:
            assert_condition(
                route == expected_route,
                f"{test['name']}: expected route {expected_route}, got {route}. Decision: {decision}",
                errors,
            )

        assert_condition(
            needs_orchestrator == test["needs_orchestrator"],
            f"{test['name']}: expected needs_orchestrator={test['needs_orchestrator']}, got {needs_orchestrator}. Decision: {decision}",
            errors,
        )

        if test.get("expects_should_update_memory"):
            assert_condition(
                decision.get("should_update_memory") is True,
                f"{test['name']}: expected should_update_memory=True. Decision: {decision}",
                errors,
            )

        if test.get("expects_followup_triggers"):
            assert_condition(
                isinstance(followup_triggers, list) and len(followup_triggers) >= 1,
                f"{test['name']}: expected at least one followup_trigger. Decision: {decision}",
                errors,
            )

        if test.get("expects_no_followup_triggers"):
            assert_condition(
                not followup_triggers,
                f"{test['name']}: expected no followup_triggers. Decision: {decision}",
                errors,
            )

            assert_condition(
                "recuerde" in direct_response.lower()
                or "recordatorio" in direct_response.lower()
                or "recuÃ©rdame" in direct_response.lower()
                or "quieres que" in direct_response.lower(),
                f"{test['name']}: expected direct response to ask about reminder. Response: {direct_response}",
                errors,
            )

        print(f"OK: {test['name']} â†’ route={route}, needs_orchestrator={needs_orchestrator}")

    if errors:
        print("")
        print("ROUTER SMOKE TEST FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("")
    print("ROUTER SMOKE TEST PASSED")


if __name__ == "__main__":
    main()

