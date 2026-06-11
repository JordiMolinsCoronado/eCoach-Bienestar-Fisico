from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

def replace_last_async_def(source: str, name: str, new_code: str) -> str:
    pattern = rf'\nasync def {name}\(.*?\):.*?(?=\nasync def |\ndef |\n# ---------------------------------------------------------------------|\ndef main\(\) -> None:|\Z)'
    matches = list(re.finditer(pattern, source, flags=re.S))
    if not matches:
        raise SystemExit(f"Could not find async function: {name}")
    m = matches[-1]
    return source[:m.start()] + "\n" + new_code.rstrip() + "\n" + source[m.end():]

guided_handler = r'''
async def handle_guided_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """The user has chosen: Agencia relacional guiada.

Write a SHORT answer. Do not dump a full long Mi Plan document.
The purpose is to establish the operating protocol, not to explain everything.

Context:
- Laura is seeing a man she likes.
- When they are together, everything seems good.
- Between dates there is ambiguity.
- Her psychologist told her not to pursue and to observe coherence.
- When Laura gets activated, she forgets the guidance.

Core product idea:
The psychologist provides the therapeutic method.
eCoach helps Laura apply that method between sessions, at the moment anxiety appears.
Then eCoach helps Laura return to the psychologist with concrete data about what happened.

Boundaries:
- eCoach does not replace the psychologist.
- eCoach does not decide for Laura.
- eCoach does not tell Laura what the man thinks.
- eCoach helps her pause and choose from values.

The answer must be compact and include:

1. "Has elegido agencia relacional guiada."
2. Laura decides; psychologist remains therapeutic reference.
3. eCoach helps between sessions when activation appears.
4. A very short Mi Plan as protocol:
   - pause before replying;
   - separate facts from stories;
   - remember values: clarity, warmth, reciprocity;
   - choose a reply that does not pursue, punish, or self-abandon;
   - observe what happens and bring concrete data to the psychologist.
5. Tell Laura to write here before answering when the real activation happens.
6. Give this simple example:
   "Me acaba de escribir. Me estoy activando y quiero contestar ya."
7. Say that then eCoach will apply the plan in real time:
   pause, facts vs stories, values, possible replies, observation of coherence, therapy material.

Important:
- Maximum about 180-230 words.
- No long numbered plan with six sections.
- No full boundary message yet.
- No detailed facts/stories list yet.
- Those details come later, when Laura writes during real activation.
- No follow-up button yet.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write a short guided-agency protocol after the user chooses Agencia relacional guiada.",
        facts=facts,
        reply_markup=None,
    )
'''

text = replace_last_async_def(text, "handle_guided_path_button", guided_handler)

path.write_text(text, encoding="utf-8")
print("Patched guided path to produce a short protocol, not a long Mi Plan document.")
