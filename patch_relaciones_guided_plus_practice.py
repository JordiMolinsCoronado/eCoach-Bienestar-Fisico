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
# 1) Change button after guided path: no longer "Diseña Mi Plan"
#    It now moves into a real activation practice.
# ---------------------------------------------------------------------

design_keyboard_re = r'def design_mi_plan_keyboard\(\) -> InlineKeyboardMarkup:\n.*?\n(?=def |\nasync def |\n# ---------------------------------------------------------------------)'
design_keyboard_new = r'''def design_mi_plan_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Practicar caso real — mensaje 23:40",
                    callback_data=DESIGN_MI_PLAN_CALLBACK,
                )
            ]
        ]
    )

'''

text, count = re.subn(design_keyboard_re, design_keyboard_new, text, count=1, flags=re.S)
print("design_mi_plan_keyboard replacements:", count)


# ---------------------------------------------------------------------
# 2) Guided path now includes Mi Plan directly.
# ---------------------------------------------------------------------

guided_handler = r'''
async def handle_guided_path_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """The user has chosen: Agencia relacional guiada.

Write ONE combined answer. Do not split into "guided path" and "Mi Plan".
Do not ask if she wants Mi Plan. She chose guided agency, so give her the plan directly.

Context:
- Laura is seeing a man she likes.
- When they are together, everything seems good.
- Between dates there is ambiguity.
- Sometimes he writes warmly.
- Sometimes he disappears.
- Sometimes he proposes vague plans.
- Her psychologist has told her not to pursue and to observe coherence.
- When Laura gets activated, she forgets the guidance.

Core idea:
- No persecución ansiosa.
- No juicio delegado.
- Agencia relacional guiada.

Boundary:
- eCoach does not replace the psychologist.
- The psychologist keeps therapeutic authority.
- Laura keeps the decision.
- eCoach helps between sessions.

The answer should include:

1. Very short explanation of agencia relacional guiada:
- Laura decides.
- eCoach helps her not lose herself when activated.
- eCoach helps her practice between sessions.

2. Mi Plan, without long duplication:
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

3. End by saying:
Now we practice the real moment: an ambiguous message at 23:40, when activation appears.
Invite her to press the practice button.

Tone:
- Clear.
- Warm.
- Compact.
- Not too therapeutic.
- No "Con calidez".
- No "juntas" too often.
- No repeated intro.
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the combined Agencia relacional guiada + Mi Plan answer.",
        facts=facts,
        reply_markup=design_mi_plan_keyboard(),
    )
'''

text = replace_last_async_def(text, "handle_guided_path_button", guided_handler)


# ---------------------------------------------------------------------
# 3) The former Mi Plan button now becomes a real activation practice.
# ---------------------------------------------------------------------

practice_handler = r'''
async def handle_design_mi_plan_button(update, context):
    query = update.callback_query
    await query.answer()
    await clear_clicked_inline_keyboard(query)

    facts = """Real-world activation practice.

Scenario:
It is 23:40.
Laura is already tired and emotionally open.
The man she likes sends this message:

"Quizá nos vemos mañana, te digo algo 😘"

Laura feels activation.
She wants to answer immediately.
Her body reads ambiguity as danger.
She thinks:
- Maybe he likes me.
- Maybe I am just an option.
- If I ask for clarity, I will lose him.
- If I say nothing, I betray myself.
- If I answer coldly, maybe I recover power.

Task:
Write an eCoach response that helps Laura practice agency in this exact moment.

The response should include:

1. Pause:
- This is activation, not failure.
- Do not answer in the first wave.
- Take 30 seconds.

2. Facts vs stories:
Facts:
- He wrote at 23:40.
- He used a warm emoji.
- He said "quizá".
- He did not concretize day/time.
- He left the plan open.

Stories:
- I am not important.
- I am too intense.
- I must accept vagueness.
- I must punish him with coldness.
- I will lose him if I ask clearly.

3. Values:
- clarity;
- warmth;
- reciprocity;
- not pursuing;
- not punishing;
- not self-abandoning.

4. Response options:
Give 3 possible messages:
A. warm and clear;
B. short and calm;
C. more direct.

The best recommended version should be something like:
"Me apetece verte. Para mí mañana funciona mejor si lo concretamos con algo de margen. Si te va bien, dime día/hora y lo organizamos."

Do not make it manipulative.
Do not make it cold.
Do not make it needy.
Do not make eCoach decide for her.
Say she chooses the version that feels most aligned.

5. Observe consistency:
After she sends a clear warm message, the task is not to monitor obsessively.
The task is to observe whether he brings more clarity or keeps ambiguity.

6. Material for psychologist:
Suggest saving:
- trigger;
- body reaction;
- facts;
- story;
- action chosen;
- how she felt after choosing from values.

7. End with:
If she wants, create tomorrow's follow-up at 10:00 to review what happened.

Tone:
- Practical.
- Warm but not sentimental.
- Product-like.
- Avoid "terapia AI".
- Avoid "te espero con alta disposición".
"""

    await answer_callback_with_skill(
        query=query,
        skill_name="manage_relationship_pattern",
        task="Write the real-world 23:40 activation practice.",
        facts=facts,
        reply_markup=create_mi_plan_followup_keyboard(),
    )
'''

text = replace_last_async_def(text, "handle_design_mi_plan_button", practice_handler)


# ---------------------------------------------------------------------
# 4) Strengthen the skill so it knows this new demo flow.
# ---------------------------------------------------------------------

skill_path = Path("skills/manage_relationship_pattern.md")
skill = skill_path.read_text(encoding="utf-8")

addition = """
## Saturday demo flow refinement

When the user chooses Agencia relacional guiada:
- Do not ask whether she wants Mi Plan.
- Give the guided-agency explanation and Mi Plan together.
- Avoid duplicating the same ideas twice.
- Keep it compact and structured.
- End by moving to a real-world activation practice.

The key product moment is not the abstract plan.
The key product moment is helping the user in a real activation:
example: 23:40, he writes a warm but vague message.

In activation practice, always help with:
1. pause;
2. facts vs stories;
3. values;
4. possible clear messages;
5. observing consistency;
6. material to bring to the psychologist.

Avoid:
- sounding like a therapist replacing therapy;
- saying “juntas” too often;
- sentimental endings like “con calidez”;
- manipulative dating tactics;
- cold punitive replies;
- telling the user what the man thinks.
"""

if "## Saturday demo flow refinement" not in skill:
    skill = skill.rstrip() + "\n\n" + addition.strip() + "\n"
    skill_path.write_text(skill, encoding="utf-8")
    print("Updated manage_relationship_pattern.md")
else:
    print("Skill already contained Saturday demo refinement.")

path.write_text(text, encoding="utf-8")
print("Patched guided path to include Mi Plan and converted Mi Plan button into 23:40 activation practice.")
