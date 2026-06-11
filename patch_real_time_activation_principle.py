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


# 1) Guided path gives Mi Plan directly and invites Laura to write during a real activation.
guided_handler = r'''
async def handle_guided_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """The user has chosen: Agencia relacional guiada.

Write ONE combined answer. Do not ask whether she wants Mi Plan. She chose guided agency, so give her the plan directly.

Context:
- Laura is seeing a man she likes.
- When they are together, everything seems good.
- Between dates there is ambiguity.
- Sometimes he writes warmly.
- Sometimes he disappears.
- Sometimes he proposes vague plans.
- Her psychologist has told her not to pursue and to observe coherence.
- When Laura gets activated, she forgets the guidance.

Core product idea:
The value is not that eCoach invents a hypothetical scenario.
The value is that Laura writes to eCoach when the real activation happens, before replying to him.
Then eCoach applies Mi Plan in real time.

Core idea:
- No persecución ansiosa.
- No juicio delegado.
- Agencia relacional guiada.

Boundary:
- eCoach does not replace the psychologist.
- The psychologist keeps therapeutic authority.
- Laura keeps the decision.
- eCoach helps between sessions, especially when the pattern activates.

The answer should include:

1. Very short explanation of agencia relacional guiada:
- Laura decides.
- eCoach helps her not lose herself when activated.
- eCoach helps her practice between sessions.

2. Mi Plan:
- Current relational question:
  ¿Esta conexión se está volviendo mutua y clara, o vivo de esperanza intermitente?

- Facts vs stories:
  Facts:
  - When they are together, connection feels good.
  - Sometimes he writes warmly.
  - Sometimes he disappears.
  - Sometimes he proposes vague plans.
  - He says he wants to see her but does not always concretize.

  Stories:
  - I did something wrong.
  - I am too intense.
  - If I ask for clarity, I will lose him.
  - I must adapt to his rhythm.
  - I should become colder.
  - I should block him.

- Values:
  clarity, warmth, reciprocity, not pursuing, not punishing, not self-abandoning, expressing a need calmly, observing facts not fantasies.

- Boundary experiment:
  Me gusta verte y lo paso bien contigo.
  A la vez, los planes muy vagos no me van bien.
  Si te apetece vernos, prefiero concretar día y hora.

- Observe response:
  Does he become clearer?
  Does he respect the boundary?
  Does he move toward her with facts?
  Does he punish clarity?
  Does the relationship make her more herself or less herself?

- Therapy preparation:
  what happened, what she felt, what she thought, what she did, where she abandoned herself, where she held herself, what to bring to therapy.

3. End with a real-time instruction:
Tell Laura:
When the real activation happens, write here before replying.
She can write something imperfect like:
"Me acaba de escribir esto: 'Quizá nos vemos mañana, te digo algo 😘'. Me estoy activando y quiero contestar ya."

Then eCoach will apply Mi Plan in real time:
pause, facts vs stories, values, possible reply, observe consistency, therapy material.

Tone:
- Clear.
- Warm.
- Compact.
- Not too therapeutic.
- No "Con calidez".
- No repeated intro.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the combined Agencia relacional guiada + Mi Plan answer and invite real-time activation use.",
        facts=facts,
        reply_markup=create_mi_plan_followup_keyboard(),
    )
'''

text = replace_last_async_def(text, "handle_guided_path_button", guided_handler)


# 2) If old "Practicar caso real" handler still exists, make it redirect conceptually, not invent a case.
redirect_handler = r'''
async def handle_design_mi_plan_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    message = """La práctica real ocurre cuando aparezca la activación de verdad.

Cuando recibas un mensaje ambiguo, notes ansiedad y tengas impulso de responder rápido, escríbeme antes de contestar.

Puedes escribir algo tan simple como:

“Me acaba de escribir esto: ‘Quizá nos vemos mañana, te digo algo 😘’. Me estoy activando y quiero contestar ya.”

Entonces aplicaremos tu Mi Plan en tiempo real:
- pausa;
- hechos vs historias;
- valores;
- posible respuesta;
- observación de consistencia;
- material para tu psicóloga."""

    await query.message.reply_text(
        message,
        reply_markup=MAIN_KEYBOARD,
    )
'''

text = replace_last_async_def(text, "handle_design_mi_plan_button", redirect_handler)


# 3) Strengthen skill: real activation must be user-provided, not generated.
skill_path = Path("skills/manage_relationship_pattern.md")
skill = skill_path.read_text(encoding="utf-8")

addition = """
## Real-time activation principle

Do not invent a fake activation case as if eCoach were simulating the user's life.

The core product moment is:
- the user experiences a real activation;
- the user writes to eCoach before reacting;
- eCoach applies Mi Plan in real time.

Example user message:
"Son las 23:40. Me acaba de escribir: 'Quizá nos vemos mañana, te digo algo 😘'. Me estoy activando y quiero contestar ya."

When the user writes a real activation message, apply Mi Plan immediately:
1. pause;
2. separate facts from stories;
3. recall values;
4. offer possible clear replies;
5. help observe consistency without obsessive monitoring;
6. prepare material for the psychologist.

Never frame this as eCoach generating a hypothetical scenario.
Frame it as eCoach supporting the user inside the real moment.
"""

if "## Real-time activation principle" not in skill:
    skill = skill.rstrip() + "\n\n" + addition.strip() + "\n"
    skill_path.write_text(skill, encoding="utf-8")
    print("Updated manage_relationship_pattern.md with real-time activation principle.")
else:
    print("Skill already contains real-time activation principle.")

path.write_text(text, encoding="utf-8")
print("Patched guided flow: real activation is user-provided, not generated.")
