from pathlib import Path
import ast
import re

path = Path("eCoach_Relaciones.py")
source = path.read_text(encoding="utf-8")
tree = ast.parse(source)

print("\n=== DIRECT USER-FACING STRING REPLIES ===\n")

interesting_calls = {
    "reply_text",
    "send_message",
    "edit_text",
    "answer",
}

results = []

for node in ast.walk(tree):
    if not isinstance(node, ast.Call):
        continue

    func_name = None

    if isinstance(node.func, ast.Attribute):
        func_name = node.func.attr
    elif isinstance(node.func, ast.Name):
        func_name = node.func.id

    if func_name not in interesting_calls:
        continue

    if not node.args:
        continue

    first_arg = node.args[0]

    if isinstance(first_arg, ast.Constant) and isinstance(first_arg.value, str):
        text = first_arg.value.strip()
        if text:
            results.append((node.lineno, func_name, text))

    elif isinstance(first_arg, ast.JoinedStr):
        results.append(
            (node.lineno, func_name, "<f-string / dynamically constructed>")
        )

for lineno, func_name, text in sorted(results):
    compact = re.sub(r"\s+", " ", text)
    if len(compact) > 220:
        compact = compact[:217] + "..."
    print(f"{lineno}: {func_name}: {compact}")


print("\n=== FUNCTIONS THAT APPEAR TO GENERATE LLM ANSWERS ===\n")

for pattern in [
    r"generate_skill_client_reply",
    r"generate_initial_discovery_reply",
    r"reply_initial_discovery_with_llm",
    r"answer_callback_with_skill",
    r"answer_message_with_skill",
    r"llm_generate_for_route",
]:
    matches = [m.start() for m in re.finditer(pattern, source)]
    print(f"{pattern}: {len(matches)} occurrence(s)")


print("\n=== POTENTIALLY HARDCODED LONG TEXT BLOCKS ===\n")

for node in ast.walk(tree):
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        value = node.value if isinstance(node, ast.Assign) else node.value

        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            content = value.value.strip()

            if len(content) >= 250:
                line = getattr(node, "lineno", "?")
                preview = re.sub(r"\s+", " ", content)[:200]
                print(f"{line}: {preview}...")


print("\n=== DUPLICATE FUNCTION DEFINITIONS ===\n")

definitions = {}

for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        definitions.setdefault(node.name, []).append(node.lineno)

for name, lines in sorted(definitions.items()):
    if len(lines) > 1:
        print(f"{name}: {lines}")
