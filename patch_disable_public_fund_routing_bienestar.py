from pathlib import Path
import shutil

path = Path("eCoach_Bienestar_Fisico.py")
text = path.read_text(encoding="utf-8")

backup = path.with_suffix(".py.before_disable_public_fund_routing")
shutil.copy2(path, backup)
print(f"Backup created: {backup}")


def replace_between(
    source: str,
    start_marker: str,
    end_marker: str,
    replacement: str,
) -> str:
    start = source.find(start_marker)

    if start == -1:
        raise SystemExit(f"Could not find start marker: {start_marker}")

    end = source.find(end_marker, start)

    if end == -1:
        raise SystemExit(f"Could not find end marker: {end_marker}")

    return (
        source[:start]
        + replacement.rstrip()
        + "\n\n"
        + source[end:]
    )


# ------------------------------------------------------------
# 1. Disable Patrimonio public-enrichment intent detection.
# ------------------------------------------------------------

text = replace_between(
    text,
    "def is_public_enrichment_intent(text: str) -> bool:",
    "def save_last_portfolio_isins_for_public_enrichment(",
    '''
def is_public_enrichment_intent(text: str) -> bool:
    """
    Disabled in eCoach Bienestar Físico.

    Health messages must never be interpreted as requests to enrich
    investment funds, KIDs, TERs, OCFs or ISINs.
    """
    return False
''',
)

print("Disabled public-fund intent detection.")


# ------------------------------------------------------------
# 2. Neutralize any separately registered fund-message handler.
# ------------------------------------------------------------

text = replace_between(
    text,
    "async def handle_public_enrichment_command(update, context):",
    "def build_private_bank_data_request_message(",
    '''
async def handle_public_enrichment_command(update, context):
    """
    Compatibility guard for inherited Patrimonio registrations.

    If an old handler sends a Bienestar Físico message here, forward it
    to the normal health free-text flow instead of producing a funds reply.
    """
    await handle_free_text(update, context)
''',
)

print("Converted inherited public-enrichment handler into health forwarding.")


path.write_text(text, encoding="utf-8")
print("Patch completed successfully.")
