---
name: my-skill
description: Create a reusable skill for a specific workflow. Use when the user wants help with that workflow across repeated tasks. Do not use for unrelated documentation or general code generation.
---

# My Skill

State the purpose in one sentence.

## What this skill does

- explain the supported workflow
- state the primary output
- mention any deterministic helpers or templates

## What this skill does not do

- list nearby tasks that should not trigger the skill

## Required input

List the minimum inputs needed before producing the result.

## Workflow

1. gather the required context
2. read any necessary files under `references/`
3. use `assets/` templates if needed
4. run scripts only for deterministic work
5. produce the final output

## Output requirements

State exactly what the skill should return.
