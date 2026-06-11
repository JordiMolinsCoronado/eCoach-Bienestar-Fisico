import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CODE_PATH = REPO_ROOT / "eCoach_Relaciones.py"
APPTEXTS_DIR = REPO_ROOT / "AppTexts"


def main() -> None:
    code = CODE_PATH.read_text(encoding="utf-8")

    # Find literal calls like:
    # load_required_app_text("some_file.md")
    required_files = sorted(
        set(
            re.findall(
                r'load_required_app_text\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
                code,
            )
        )
    )

    errors: list[str] = []

    if not required_files:
        errors.append("No load_required_app_text(...) references found. This may indicate a test bug.")

    for filename in required_files:
        path = APPTEXTS_DIR / filename

        if not path.exists():
            errors.append(f"Missing required AppTexts file: {filename}")
            continue

        if not path.is_file():
            errors.append(f"Required AppTexts path is not a file: {filename}")
            continue

        content = path.read_text(encoding="utf-8")

        if not content.strip():
            errors.append(f"Required AppTexts file is empty: {filename}")

    if errors:
        print("FILE INTEGRITY SMOKE TEST FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("FILE INTEGRITY SMOKE TEST PASSED")
    print(f"- Checked required AppTexts files: {len(required_files)}")


if __name__ == "__main__":
    main()

