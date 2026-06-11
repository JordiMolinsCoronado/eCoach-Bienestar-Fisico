from pathlib import Path

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

disable_patterns = [
    "analyze_uploaded_documents_callback_handler",
    "handle_compare_current_portfolio_button",
    "handle_define_concrete_alternative_button",
    "handle_prepare_provisional_alternative_button",
    "handle_define_initial_alternative_button",
    "handle_search_providers_button",
    "handle_build_same_risk_lower_cost_portfolio_button",
    "handle_review_before_execute_button",
    "handle_provider_selected_button",
    "handle_missing_data_checklist_button",
    "handle_keep_similar_risk_button",
    "handle_reduce_risk_button",
    "handle_public_enrichment_command",
    "PUBLIC_ENRICHMENT_RE",
    "PROVIDER_INDEXA_CALLBACK",
    "PROVIDER_INBESTME_CALLBACK",
    "COMPARE_CURRENT_PORTFOLIO_CALLBACK",
    "DEFINE_CONCRETE_ALTERNATIVE_CALLBACK",
    "PREPARE_PROVISIONAL_ALTERNATIVE_CALLBACK",
    "DEFINE_INITIAL_ALTERNATIVE_CALLBACK",
    "SEARCH_PROVIDERS_CALLBACK",
    "REVIEW_BEFORE_EXECUTE_CALLBACK",
    "MISSING_DATA_CHECKLIST_CALLBACK",
    "KEEP_SIMILAR_RISK_CALLBACK",
    "REDUCE_RISK_CALLBACK",
]

new_lines = []
for line in text.splitlines():
    stripped = line.strip()

    if stripped.startswith("app.add_handler(") and any(pattern in line for pattern in disable_patterns):
        if "Disabled in eCoach Relaciones demo" not in line:
            new_lines.append("    # Disabled in eCoach Relaciones demo: " + stripped)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

text = "\n".join(new_lines) + "\n"
path.write_text(text, encoding="utf-8")

print("Disabled remaining Patrimonio-specific active handlers.")
