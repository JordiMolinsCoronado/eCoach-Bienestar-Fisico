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


# ---------------------------------------------------------------------
# 1) Guided path: give Mi Plan, but DO NOT show follow-up inline button yet.
# ---------------------------------------------------------------------

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

Do NOT offer to create a follow-up yet.
Do NOT show a follow-up button yet.
The follow-up comes only after a real activation has been processed.

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
        reply_markup=None,
    )
'''

text = replace_last_async_def(text, "handle_guided_path_button", guided_handler)


# ---------------------------------------------------------------------
# 2) Add deterministic real-time activation handler.
#    This prevents the message from going to the old Patrimonio router.
# ---------------------------------------------------------------------

activation_handler = r'''
async def handle_real_time_relationship_activation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activate_client_from_update(update)
    ensure_client_files()

    user_text = update.message.text or ""

    facts = f"""The user is writing during a REAL relational activation.

This is not a hypothetical case created by eCoach.
The user has come to eCoach before replying, exactly as Mi Plan instructed.

User message:
{user_text}

Context from Mi Plan:
- Laura likes this man.
- When they are together, things feel good.
- Between dates, ambiguity activates her.
- Her psychologist told her not to pursue and to observe coherence.
- eCoach must help between therapy sessions without replacing the psychologist.

Task:
Apply Mi Plan in real time.

The answer should include:

1. Pause:
- This is activation, not failure.
- Do not answer in the first wave.
- Take 30 seconds.
- The goal is not to suppress emotion, but to avoid letting activation write the message.

2. Facts vs stories:
Use the user's actual message.
Facts may include:
- he wrote late;
- he used warm language or emoji;
- he used vague wording;
- he did not concretize day/time;
- Laura feels urgency to answer.

Stories may include:
- I am not important;
- I am too intense;
- I must accept vagueness;
- I must become cold;
- I will lose him if I ask clearly.

3. Values:
- clarity;
- warmth;
- reciprocity;
- not pursuing;
- not punishing;
- not self-abandoning.

4. Possible replies:
Give 3 options:
A. warm and clear;
B. short and calm;
C. more direct.

Recommended version should be warm-clear, close to:
"Me apetece verte. Para mí mañana funciona mejor si lo concretamos con algo de margen. Si te va bien, dime día/hora y lo organizamos."

Do not make it manipulative.
Do not make it cold.
Do not make it needy.
Do not decide for Laura.
Say she can choose the version that feels most aligned.

5. Observe consistency:
After sending a clear warm message, the task is not obsessive monitoring.
The task is to observe whether he brings more clarity or keeps ambiguity.

6. Material for psychologist:
Suggest saving:
- trigger;
- body reaction;
- facts;
- story;
- action chosen;
- how she felt after choosing from values.

7. End by offering the follow-up:
Say we can create tomorrow's 10:00 follow-up to review what happened.

Tone:
- Practical.
- Warm.
- Product-like.
- Not patrimonial.
- Not financial.
- Not generic.
- No sentence saying "soy guía patrimonial-financiero".
"""

    await answer_message_with_skill(
        update=update,
        context=context,
        skill_name="manage_relationship_pattern",
        task="Apply Mi Plan in real time to this relationship activation.",
        facts=facts,
        reply_markup=create_mi_plan_followup_keyboard(),
    )
'''

# Insert before main() if not already present
if "async def handle_real_time_relationship_activation" not in text:
    marker = "\ndef main() -> None:"
    if marker not in text:
        raise SystemExit("Could not find main() marker.")
    text = text.replace(marker, "\n" + activation_handler.strip() + "\n" + marker, 1)
    print("Inserted handle_real_time_relationship_activation.")
else:
    text = replace_last_async_def(text, "handle_real_time_relationship_activation", activation_handler)
    print("Replaced existing handle_real_time_relationship_activation.")


# ---------------------------------------------------------------------
# 3) Register activation handler BEFORE generic handle_free_text.
# ---------------------------------------------------------------------

activation_registration = '''
    app.add_handler(MessageHandler(
        filters.Regex(r"(?i)(me acaba de escribir|me estoy activando|estoy activada|quiero contestar ya|contestarle ya|hacerme la fría|hacerme la fria|son las 23:40|quizá nos vemos|quiza nos vemos)") & ~filters.COMMAND,
        client_locked_handler(handle_real_time_relationship_activation),
    ))
'''

if "handle_real_time_relationship_activation" in text and "me acaba de escribir|me estoy activando" not in text:
    # Insert before the first generic free text handler.
    generic_patterns = [
        r'\n\s*app\.add_handler\(MessageHandler\(filters\.TEXT\s*&\s*~filters\.COMMAND,\s*client_locked_handler\(handle_free_text\)\)\)',
        r'\n\s*app\.add_handler\(MessageHandler\(filters\.TEXT\s*&\s*~filters\.COMMAND,\s*handle_free_text\)\)',
    ]

    inserted = False
    for pat in generic_patterns:
        m = re.search(pat, text)
        if m:
            text = text[:m.start()] + "\n" + activation_registration.rstrip() + text[m.start():]
            inserted = True
            break

    if not inserted:
        raise SystemExit("Could not find generic handle_free_text registration to insert before.")

    print("Registered activation handler before generic free-text handler.")
else:
    print("Activation handler registration appears to exist already.")


# ---------------------------------------------------------------------
# 4) Strengthen skill: activation must never fall to patrimonial router.
# ---------------------------------------------------------------------

skill_path = Path("skills/manage_relationship_pattern.md")
skill = skill_path.read_text(encoding="utf-8")

addition = """
## Real-time activation routing

When the user writes something like:
- "Me acaba de escribir..."
- "Me estoy activando..."
- "Quiero contestar ya..."
- "No sé si pedir claridad o hacerme fría..."
- "Son las 23:40..."

This is a real-time relationship activation.

Do not answer as a financial/patrimonial coach.
Do not say this is outside scope.
Do not redirect to finances.

Apply Mi Plan in real time:
1. pause;
2. facts vs stories;
3. values;
4. possible warm-clear replies;
5. observe consistency;
6. material for psychologist;
7. offer follow-up.

The user is not asking for generic relationship advice.
The user is asking for agency at the moment of activation.
"""

if "## Real-time activation routing" not in skill:
    skill = skill.rstrip() + "\n\n" + addition.strip() + "\n"
    skill_path.write_text(skill, encoding="utf-8")
    print("Updated skill with activation routing rule.")
else:
    print("Skill already has activation routing rule.")


path.write_text(text, encoding="utf-8")
print("Patched real-time activation routing and removed early follow-up button.")
