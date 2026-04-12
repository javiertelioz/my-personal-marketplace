# Skill specification

Use this reference to make sure the skill structure and metadata follow the Agent Skills specification.

## Minimum structure

A skill directory must contain at least:

```text
skill-name/
├── SKILL.md
├── scripts/      # optional
├── references/   # optional
├── assets/       # optional
└── evals/        # optional, but recommended when benchmarking matters
```

## `SKILL.md` requirements

`SKILL.md` must contain:

1. YAML frontmatter
2. Markdown body

Required frontmatter fields:

- `name`
- `description`

Optional fields:

- `license`
- `compatibility`
- `metadata`
- `allowed-tools`

## `name` rules

The `name` field must:

- be 1 to 64 characters
- use lowercase letters, numbers, and single hyphens only
- not start or end with a hyphen
- not contain consecutive hyphens
- match the parent directory name exactly

## `description` rules

The `description` field must:

- be non-empty
- stay under 1024 characters
- describe what the skill does and when to use it
- include task signals that help the agent activate it correctly

## Progressive disclosure

Keep `SKILL.md` short enough that it remains useful when loaded into context.

Good pattern:

- `SKILL.md` contains activation guidance and the main workflow
- `references/` contains detailed rules and examples
- `scripts/` contains deterministic helpers
- `assets/` contains templates and static resources

## File references

Use relative paths from the skill root, for example:

- `references/api-rules.md`
- `scripts/validate.sh`
- `assets/template.json`

Keep references flat and easy to follow. Avoid deep nested chains.

## Marketplace placement

Inside this repository, a skill should live under:

```text
plugins/<plugin-name>/skills/<skill-name>/SKILL.md
```

The plugin manifest then points to that `SKILL.md` entrypoint.
