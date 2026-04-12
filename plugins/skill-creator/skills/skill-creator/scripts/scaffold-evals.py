#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


def read_skill_name(skill_path: Path) -> str:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return skill_path.name
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return skill_path.name
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return skill_path.name


def write_json(path: Path, payload: object, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold eval files for an Agent Skills-style skill.")
    parser.add_argument("--skill-path", required=True, help="Path to the skill directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing eval files.")
    args = parser.parse_args()

    skill_path = Path(args.skill_path).expanduser().resolve()
    if not skill_path.exists() or not skill_path.is_dir():
        print(f"ERROR: Skill path does not exist or is not a directory: {skill_path}", file=sys.stderr)
        return 1

    skill_name = read_skill_name(skill_path)
    evals_dir = skill_path / "evals"

    evals_payload = {
        "skill_name": skill_name,
        "evals": [
            {
                "id": 1,
                "prompt": "Replace this with a realistic task that should be solved well by the skill.",
                "expected_output": "Describe the expected result in human-readable form.",
                "assertions": [
                    "Replace this with a concrete pass/fail assertion."
                ]
            }
        ]
    }
    description_queries_payload = [
        {
            "query": "Replace this with a prompt that should trigger the skill.",
            "should_trigger": True
        },
        {
            "query": "Replace this with a near-miss prompt that should not trigger the skill.",
            "should_trigger": False
        }
    ]

    write_json(evals_dir / "evals.json", evals_payload, force=args.force)
    write_json(
        evals_dir / "description-eval-queries.json",
        description_queries_payload,
        force=args.force,
    )

    print(f"Created eval scaffolding for {skill_name} in {evals_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
