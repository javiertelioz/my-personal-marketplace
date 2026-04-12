# Validating a skill

Use this reference once the skill structure is in place.

## Validation goals

A validation pass should confirm:

- the skill directory exists
- `SKILL.md` exists
- frontmatter contains `name` and `description`
- the skill name matches the directory name
- naming rules are respected
- the description length is acceptable
- the directory layout is sane
- the skill does not contain obvious anti-patterns like README files or nested reference trees

## Local wrapper script

Run:

```bash
python3 scripts/validate-skill.py /path/to/skill
```

What it does:

1. performs built-in structural checks
2. warns about common authoring mistakes
3. calls `skills-ref validate` if the executable is available

## Optional strict mode

If `skills-ref` is required in your workflow, run:

```bash
python3 scripts/validate-skill.py --require-skills-ref /path/to/skill
```

This fails if the external validator is not installed.

## Common failures

### Name mismatch

- frontmatter `name` does not match the parent directory
- invalid characters
- consecutive hyphens

### Description issues

- too vague
- too long
- missing usage context

### Structure issues

- missing `SKILL.md`
- nested files under `references/`, `scripts/`, or `assets/`
- human-facing docs like `README.md` added to the skill root

## When validation passes

Move on to:

- `evaluating-a-skill.md` for output and trigger evals
- `checklist.md` for the final audit
