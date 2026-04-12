# Skill creation checklist

Use this checklist before publishing or committing a skill.

## Metadata and discovery

- [ ] The `name` matches the parent directory.
- [ ] The `name` uses lowercase letters, numbers, and single hyphens only.
- [ ] The `description` is under 1024 characters.
- [ ] The `description` clearly says when to use the skill.
- [ ] The `description` also says when not to use the skill.

## Structure

- [ ] `SKILL.md` exists.
- [ ] `references/`, `scripts/`, and `assets/` are used only when needed.
- [ ] Files inside `references/`, `scripts/`, and `assets/` are one level deep.
- [ ] No `README.md`, `CHANGELOG.md`, or similar human-facing docs were added to the skill root.

## Instruction quality

- [ ] `SKILL.md` contains the main workflow.
- [ ] `SKILL.md` routes to specific references when needed.
- [ ] The instructions are procedural and not vague.
- [ ] The skill avoids unnecessary context bloat.

## Scripts

- [ ] Scripts are small, deterministic CLIs.
- [ ] Scripts support `--help`.
- [ ] Scripts use stdout for success and stderr for failure.

## Validation and evals

- [ ] `python3 scripts/validate-skill.py /path/to/skill` passes.
- [ ] `skills-ref validate /path/to/skill` passes when available.
- [ ] `evals/evals.json` exists if the skill should be benchmarked.
- [ ] `evals/description-eval-queries.json` exists if description triggering matters.
