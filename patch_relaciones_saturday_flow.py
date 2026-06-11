from pathlib import Path
import re

path = Path("eCoach_Relaciones.py")
text = path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------
# 1) Make initial discovery reply show relationship path buttons
# ---------------------------------------------------------------------

text = text.replace(
    "    await update.message.reply_text(answer, reply_markup=MAIN_KEYBOARD)\n",
    "    await update.message.reply_text(answer, reply_markup=alternatives_path_keyboard())\n",
    1,
)

# ---------------------------------------------------------------------
# 2) Add relationship initial-message detector into handle_free_text
# ---------------------------------------------------------------------

if "def detect_relationship_initial_message" not in text:
    marker = "\nasync def handle_free_text"
    if marker not in text:
        raise SystemExit("Could not find handle_free_text marker.")

    helper = r'''
def detect_relationship_initial_message(user_text: str) -> bool:
    text = user_text.lower()

    relationship_markers = [
        "hombre que me gusta",
        "psicóloga",
        "psicologa",
        "no persiga",
        "no perseguir",
        "entre citas",
        "ambiguo",
        "desaparece",
        "se me olvida todo",
        "cuando me activo",
        "relación romántica",
        "relacion romantica",
    ]

    hits = sum(1 for marker in relationship_markers if marker in text)
    return hits >= 2

'''
    text = text.replace(marker, "\n" + helper + marker, 1)


insert_after = '    user_text = update.message.text.strip()\n'
relationship_branch = '''
    if detect_relationship_initial_message(user_text):
        await reply_initial_discovery_with_llm(update, user_text)
        return

'''

if relationship_branch.strip() not in text:
    if insert_after not in text:
        raise SystemExit("Could not find user_text assignment in handle_free_text.")
    text = text.replace(insert_after, insert_after + relationship_branch, 1)


# ---------------------------------------------------------------------
# 3) Override relationship keyboards and handlers before main()
# ---------------------------------------------------------------------

override_marker = "\ndef main() -> None:"
if override_marker not in text:
    raise SystemExit("Could not find main() marker.")

relationship_overrides = r'''
# ---------------------------------------------------------------------
# eCoach Relaciones — Saturday demo relationship flow overrides
# ---------------------------------------------------------------------

def alternatives_path_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Gestionarlo sola",
                    callback_data=SELF_MANAGED_PATH_CALLBACK,
                )
            ],
            [
                InlineKeyboardButton(
                    "Delegar el juicio",
                    callback_data=DELEGATED_PATH_CALLBACK,
                )
            ],
            [
                InlineKeyboardButton(
                    "Agencia relacional guiada",
                    callback_data=GUIDED_PATH_CALLBACK,
                )
            ],
        ]
    )


def design_mi_plan_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Diseña Mi Plan",
                    callback_data=DESIGN_MI_PLAN_CALLBACK,
                )
            ]
        ]
    )


def create_mi_plan_followup_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Crear seguimiento — mañana 10:00",
                    callback_data=CREATE_MI_PLAN_FOLLOWUP_CALLBACK,
                )
            ]
        ]
    )


async def handle_self_managed_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Camino elegido: gestionarlo sola.

Meaning:
- The user tries to solve the romantic ambiguity alone.
- She may read about attachment, watch dating advice, ask friends, analyze messages, write and delete texts, wait, block, doubt.
- Pros: independence and learning.
- Cons: overanalysis, activation, impulsivity, confusion between limits and punishment, possible self-abandonment.

Finality:
Explain this path warmly and without shaming.
Make clear it can teach things, but when the nervous system is activated it can become chaotic.
Invite her to consider Agencia relacional guiada.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the answer after the user chooses the self-managed relationship path.",
        facts=facts,
        reply_markup=alternatives_path_keyboard(),
    )


async def handle_delegated_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Camino elegido: delegar el juicio.

Meaning:
- The user asks friends, rigid dating rules, therapy, the man, or eCoach to decide for her.
- She wants someone to say: write, wait, block, continue, leave.
- Pros: short-term relief.
- Cons: loss of internal authority, dependence, disconnection from values, relief without maturity.

Finality:
Explain this path warmly and without shaming.
Make clear that eCoach will not become another dependency.
Invite her to consider Agencia relacional guiada.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the answer after the user chooses delegated judgement in relationship context.",
        facts=facts,
        reply_markup=alternatives_path_keyboard(),
    )


async def handle_guided_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Camino elegido: agencia relacional guiada.

Core idea:
- No persecución ansiosa.
- No juicio delegado.
- Agencia relacional guiada.

Boundary:
- eCoach does not replace the psychologist.
- The psychologist keeps therapeutic authority.
- The user keeps the decision.
- eCoach helps between sessions.

What eCoach helps with:
- pause;
- regulate;
- separate facts from stories;
- remember values;
- prepare messages;
- practice boundaries;
- observe consistency;
- prepare material for therapy.

The user does not say: eCoach decides for me.
The user says: eCoach helps me not lose myself while I decide.

Finality:
Explain the guided path clearly and end by offering to create Mi Plan.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the answer after the user chooses Agencia relacional guiada.",
        facts=facts,
        reply_markup=design_mi_plan_keyboard(),
    )


async def handle_design_mi_plan_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Mi Plan for Laura.

Situation:
- Laura is seeing a man she likes.
- When they are together, connection seems good.
- Between dates, there is ambiguity.
- Sometimes he writes warmly.
- Sometimes he disappears.
- Sometimes he proposes vague plans.
- Her psychologist has advised her not to pursue and to observe coherence.
- When Laura gets activated, she forgets that guidance.

Mi Plan structure:

1. Current relational question:
¿Esta conexión se está volviendo mutua y clara, o vivo de esperanza intermitente?

2. Separate facts from stories.

Facts:
- He is warm when they are together.
- He sometimes writes with affection.
- He sometimes disappears.
- He sometimes proposes vague plans.
- He says he wants to see her but does not always concretize.

Stories:
- I did something wrong.
- I am too intense.
- If I ask for clarity, I will lose him.
- I must adapt to his rhythm.
- I should become colder.
- I should block him.

3. Relational values:
- clarity;
- warmth;
- reciprocity;
- not pursuing;
- not punishing;
- not self-abandoning;
- expressing a need calmly;
- observing facts, not fantasies.

4. Boundary experiment:
Me gusta verte y lo paso bien contigo.
A la vez, los planes muy vagos no me van bien.
Si te apetece vernos, prefiero concretar día y hora.

The boundary experiment is not an ultimatum, not a punishment, not a game.
It is a clear, warm, self-respecting experiment.

5. Observe the response:
- Does he become clearer?
- Does he respect the boundary?
- Does he move toward her with facts?
- Does he punish clarity?
- Does the relationship make her more herself or less herself?

6. Prepare therapy:
Before the next psychology session, eCoach can summarize:
- what happened;
- what she felt;
- what she thought;
- what she did;
- where she abandoned herself;
- where she held herself;
- what to bring to therapy.

Follow-up:
- Suggested follow-up: mañana a las 10:00.
- Purpose: review activation, facts vs stories, values, and next clear step.

Finality:
Write Mi Plan warmly and practically.
End by making the follow-up feel like the next clear step.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write Mi Plan for Laura in eCoach Relaciones.",
        facts=facts,
        reply_markup=create_mi_plan_followup_keyboard(),
    )


async def handle_create_mi_plan_followup_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Follow-up created.

Date:
- mañana

Time:
- 10:00

Topic:
- revisar activación, hechos vs historias, valores relacionales y siguiente paso claro.

In the follow-up, eCoach will review:
- whether Laura became activated;
- whether she paused before acting;
- whether she separated facts from stories;
- whether she acted from values;
- whether she needs to prepare something for her psychologist.

Tone:
- warm;
- non-punitive;
- high goodwill;
- no shame.

Example tone:
Eso fue activación, no fracaso.
Vamos a mirarlo con calma:
¿qué quería hacer el miedo, y qué elegiría tu yo más sereno ahora?

Finality:
Confirm the follow-up has been created and explain what will happen.
"""

    thinking_message = await query.message.reply_text("Pensando...")

    try:
        followup_text = await asyncio.to_thread(
            generate_skill_client_reply,
            "manage_relationship_pattern",
            "Write the relationship follow-up creation confirmation.",
            facts,
        )
    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        await query.message.reply_text(f"No he podido crear el seguimiento: {error}")
        return

    try:
        await thinking_message.delete()
    except Exception:
        pass

    try:
        client_dir = active_client_dir()
        followups_dir = client_dir / "followups"
        followups_dir.mkdir(parents=True, exist_ok=True)
        followup_file = followups_dir / "relaciones_laura_followup_manana_10-00.md"
        followup_file.write_text(followup_text, encoding="utf-8")
    except Exception:
        pass

    await query.message.reply_text(followup_text)

'''

# Remove previous relationship overrides if re-running this patch
start = text.find("# ---------------------------------------------------------------------\n# eCoach Relaciones — Saturday demo relationship flow overrides")
if start != -1:
    end = text.find("\ndef main() -> None:", start)
    if end == -1:
        raise SystemExit("Could not find end of previous relationship overrides.")
    text = text[:start] + text[end:]

text = text.replace(override_marker, "\n" + relationship_overrides + override_marker, 1)

path.write_text(text, encoding="utf-8")
print("Patched eCoach Relaciones Saturday demo flow.")
