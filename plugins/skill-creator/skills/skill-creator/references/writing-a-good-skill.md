# Writing a good skill

Use this reference when drafting or restructuring the main instructions.

## Start from real expertise

A good skill captures domain-specific guidance that the agent would not reliably infer on its own.

Focus on:

- project conventions
- fragile workflows
- common gotchas
- repeated reviewer feedback
- known failure patterns

## Keep the scope coherent

A skill should cover one clear unit of work.

Good examples:

- create a Datadog notebook runbook
- review a threat model with STRIDE-A
- create an Agent Skills-compliant skill package

Bad examples:

- do all engineering documentation
- create any artifact related to software delivery

## Keep `SKILL.md` focused

Use `SKILL.md` for:

- when to use the skill
- when not to use it
- the main workflow
- explicit routing to references and scripts

Move large details out of `SKILL.md` when they are:

- schemas
- long examples
- extensive checklists
- rule tables
- troubleshooting branches

## Prefer procedures over declarations

Teach the agent how to approach the task, not just what a finished artifact should vaguely look like.

Prefer:

1. gather the required inputs
2. choose the right template
3. validate the structure
4. produce the output

Over:

- “make it good”
- “follow best practices”
- “be clear and professional”

## Add only what the agent lacks

Avoid padding the skill with generic explanations the agent already knows.

High-value content includes:

- naming rules
- exact file locations
- non-obvious edge cases
- required validation steps
- project-specific terminology

## Good reference routing

A strong skill does not just mention `references/`.

It says exactly when to read each file, such as:

- read `references/error-codes.md` if the API returns a non-200 status
- read `references/template-rules.md` before writing the final Markdown

That routing is part of the skill quality.
