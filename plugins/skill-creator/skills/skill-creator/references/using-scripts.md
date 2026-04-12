# Using scripts

Use this reference before adding anything under `scripts/`.

## When scripts help

Add a script when the task is fragile, repetitive, or easier to verify with deterministic code.

Good reasons:

- validation
- parsing
- scaffolding files
- mechanical transformations

Bad reasons:

- hiding a vague workflow the skill should explain directly
- dumping general-purpose application code into the skill

## Script design rules

- keep each script single-purpose
- make the interface non-interactive
- accept inputs through flags or positional arguments
- provide `--help`
- print success details to stdout
- print actionable failures to stderr
- exit non-zero on failure

## Referencing scripts

Use relative paths from the skill root:

- `scripts/validate-skill.py`
- `scripts/scaffold-evals.py`

## Versioned one-off tools

If a one-off command is enough, prefer clear, versioned tooling rather than long ad hoc shell pipelines.

Examples:

- `npx package@version`
- `uv run script.py`
- `go run module@version`

## Use scripts sparingly

If the agent can follow the logic reliably from short instructions, do not force everything into a script.

Scripts are for deterministic help, not for replacing the core skill logic.
