---
name: skill-creator
description: Create new agent skills that follow the Agent Skills specification and use progressive disclosure well. Use when creating a new skill, restructuring an existing skill, improving a skill description for better triggering, adding scripts or references, or scaffolding evals and validation for a skill package. Do not use for general README writing, non-agentic library code, or unrelated plugin documentation.
---

# Skill Creator

Create **Agent Skills-compatible skill packages** that are structured, discoverable, and easy to validate.

This skill is designed for:

- creating a new skill from scratch
- upgrading a loose prompt into a reusable skill
- improving a skill description so it triggers more reliably
- deciding what belongs in `SKILL.md` versus `references/`, `scripts/`, or `assets/`
- validating a skill before publishing it
- scaffolding eval files so the skill can be tested

## What this skill does

- creates a spec-aligned skill directory
- keeps `SKILL.md` concise and operational
- pushes detailed material into focused reference files
- suggests when to use scripts for deterministic tasks
- validates the finished skill with local checks and `skills-ref` when available
- scaffolds eval files for output-quality and trigger-quality testing

## What this skill does not do

- it does **not** write README files or general repository docs
- it does **not** create broad multi-purpose documentation bundles with unclear scope
- it does **not** assume `skills-ref` is already installed
- it does **not** approve vague descriptions that fail to say when the skill should or should not trigger

## Start here

Read `references/start-here.md` first.

Then choose the smallest set of references needed for the current task:

- read `references/skill-specification.md` to check the required file layout and frontmatter rules
- read `references/writing-a-good-skill.md` when drafting or restructuring `SKILL.md`
- read `references/writing-a-good-description.md` when tuning the description for discoverability
- read `references/using-scripts.md` before adding anything under `scripts/`
- read `references/validating-a-skill.md` before final validation
- read `references/evaluating-a-skill.md` before creating `evals/evals.json`
- read `references/checklist.md` for the final audit

## Required input

Before creating or revising a skill, gather:

1. the intended skill name
2. the user task or workflow the skill should handle
3. the boundaries of what is in scope and out of scope
4. any fragile or deterministic steps that should be scripted
5. whether the skill needs templates, references, or evals

When working in this marketplace, place the finished skill under:

`plugins/<plugin-name>/skills/<skill-name>/`

## Workflow

### 1. Define the skill clearly

- choose a kebab-case skill name that matches the directory name
- write a short description that says **when to use the skill**
- identify negative triggers so the description also says when **not** to use it

### 2. Create the minimum valid structure

Create:

- `SKILL.md`
- `references/` only if detailed material is needed
- `scripts/` only if a deterministic helper is needed
- `assets/` only if reusable templates or static files are needed
- `evals/` when the skill should be benchmarked or compared

Use `assets/skill-template.md` as the starting point for the new `SKILL.md`.

### 3. Keep `SKILL.md` lean

- put the activation logic and workflow in `SKILL.md`
- move heavy details to one-level-deep files in `references/`
- keep file references relative and explicit
- tell the agent **when** to read each reference instead of listing a folder with no routing guidance

### 4. Add scripts only for fragile work

If the skill needs deterministic help for validation, parsing, scaffolding, or formatting:

- add a small CLI in `scripts/`
- make it non-interactive
- provide `--help`
- emit success information to stdout
- emit failures to stderr with actionable messages

### 5. Validate the result

Run:

```bash
python3 scripts/validate-skill.py /path/to/skill
```

If `skills-ref` is installed, the script will also call:

```bash
skills-ref validate /path/to/skill
```

Fix all structural and metadata problems before treating the skill as finished.

### 6. Scaffold evals

Run:

```bash
python3 scripts/scaffold-evals.py --skill-path /path/to/skill
```

This creates starter files for:

- `evals/evals.json`
- `evals/description-eval-queries.json`

Then customize them for the specific skill.

## Output requirements

When asked to create a skill, return:

1. the proposed skill name
2. the final directory structure
3. the complete `SKILL.md`
4. any references, scripts, assets, and eval files
5. unresolved assumptions, if any

## Final quality bar

A finished skill should:

1. match the Agent Skills specification
2. have a description that is likely to trigger at the right time
3. use progressive disclosure instead of bloated instructions
4. validate cleanly
5. include eval scaffolding when the skill is important enough to benchmark
