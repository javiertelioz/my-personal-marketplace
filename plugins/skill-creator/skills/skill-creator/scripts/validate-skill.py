#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DISALLOWED_ROOT_FILES = {"README.md", "CHANGELOG.md", "INSTALLATION.md", "INSTALLATION_GUIDE.md"}


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md is missing opening YAML frontmatter.")

    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        raise ValueError("SKILL.md is missing closing YAML frontmatter.")

    data: dict[str, str] = {}
    for line in lines[1:end_index]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def find_nested_files(base: Path) -> list[str]:
    if not base.exists() or not base.is_dir():
        return []
    nested = []
    for path in base.rglob("*"):
        if path.is_file() and path.parent != base:
            nested.append(path.relative_to(base).as_posix())
    return sorted(nested)


def validate_local(skill_path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not skill_path.exists():
        return [f"Skill path does not exist: {skill_path}"], warnings
    if not skill_path.is_dir():
        return [f"Skill path is not a directory: {skill_path}"], warnings

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return [f"Missing required file: {skill_md}"], warnings

    try:
        frontmatter = read_frontmatter(skill_md)
    except ValueError as exc:
        return [str(exc)], warnings

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    parent_name = skill_path.name

    if not name:
        errors.append("Frontmatter is missing required field: name")
    elif not (1 <= len(name) <= 64):
        errors.append(f"Skill name must be 1-64 characters; got {len(name)}.")
    elif not NAME_RE.match(name):
        errors.append("Skill name must use lowercase letters, numbers, and single hyphens only.")
    elif name != parent_name:
        errors.append(f"Skill name '{name}' does not match directory name '{parent_name}'.")

    if not description:
        errors.append("Frontmatter is missing required field: description")
    elif len(description) > 1024:
        errors.append(f"Description must be 1024 characters or fewer; got {len(description)}.")
    else:
        lowered = description.lower()
        if "use when" not in lowered:
            warnings.append("Description should include 'Use when ...' guidance.")
        if "do not use" not in lowered and "don't use" not in lowered:
            warnings.append("Description should include a negative trigger such as 'Do not use ...'.")

    line_count = len(skill_md.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        warnings.append(f"SKILL.md is {line_count} lines; consider moving detail into references/.")

    for filename in DISALLOWED_ROOT_FILES:
        if (skill_path / filename).exists():
            warnings.append(f"Human-facing root file found: {filename}")

    for dirname in ("references", "scripts", "assets"):
        nested = find_nested_files(skill_path / dirname)
        if nested:
            warnings.append(
                f"{dirname}/ contains nested files or directories deeper than one level: {', '.join(nested)}"
            )

    skill_text = skill_md.read_text(encoding="utf-8")
    if "\\" in skill_text and re.search(r"(references|scripts|assets)\\", skill_text):
        warnings.append("Use forward slashes in file references inside SKILL.md.")

    return errors, warnings


def run_skills_ref(skill_path: Path, require: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    executable = shutil.which("skills-ref")
    if executable is None:
        message = "skills-ref not found on PATH; skipped external validation."
        if require:
            errors.append(message)
        else:
            warnings.append(message)
        return errors, warnings

    result = subprocess.run(
        [executable, "validate", os.fspath(skill_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)
    if result.returncode != 0:
        errors.append("skills-ref validation failed.")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Agent Skills-style skill directory.")
    parser.add_argument("skill_path", help="Path to the skill directory to validate.")
    parser.add_argument(
        "--require-skills-ref",
        action="store_true",
        help="Fail if the external skills-ref executable is not available.",
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path).expanduser().resolve()
    errors, warnings = validate_local(skill_path)
    ext_errors, ext_warnings = run_skills_ref(skill_path, require=args.require_skills_ref)
    errors.extend(ext_errors)
    warnings.extend(ext_warnings)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validation passed for {skill_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
