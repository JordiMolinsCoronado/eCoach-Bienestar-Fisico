from pathlib import Path
import ast

source_path = Path("eCoach_Bienestar_Fisico.py")
source = source_path.read_text(encoding="utf-8-sig")
tree = ast.parse(source)

target_name = "detect_physical_wellbeing_initial_message"

function_node = next(
    (
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == target_name
    ),
    None,
)

if function_node is None:
    raise SystemExit(f"Could not find {target_name}")

module = ast.Module(body=[function_node], type_ignores=[])
ast.fix_missing_locations(module)

namespace = {}
exec(compile(module, str(source_path), "exec"), namespace)

detector = namespace[target_name]

message = """
Me llamo Laura, tengo 48 años y vivo en Barcelona.

He ido al médico porque quiero perder peso.
Tengo el colesterol y el azúcar un poco elevados.
La visita duró quince minutos y no tengo un plan concreto.
Tengo la analítica y una prueba genética. ¿Puedo subirlas?
"""

print("Detected:", detector(message))
