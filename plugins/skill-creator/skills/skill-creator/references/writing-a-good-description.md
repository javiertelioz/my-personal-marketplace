# Writing a good description

Use this reference when tuning the frontmatter `description` for discoverability.

## What the description must do

The description is the main trigger surface for the skill.

It should explain:

- what the skill helps with
- when the agent should use it
- when the agent should avoid it

## Useful description pattern

Use wording like:

`Create X. Use when the user wants to Y or Z. Do not use for A or B.`

This works better than a vague summary.

## Description guidelines

- focus on user intent, not internal implementation
- mention multiple natural trigger situations
- include negative triggers for nearby tasks the skill should avoid
- keep it concise
- stay under 1024 characters

## Good example

`Create new agent skills that follow the Agent Skills specification. Use when creating a new skill, restructuring an existing skill, improving a skill description, adding references or scripts, or scaffolding evals and validation. Do not use for README writing, general plugin documentation, or unrelated code generation.`

## Weak example

`Helps with skills.`

It is too short, too vague, and does not say when to use it.

## Trigger eval queries

Test the description with realistic prompts:

- some should trigger
- some should not trigger
- many should be near-misses

Examples of **should trigger** prompts:

- “Create a new reusable skill for generating incident runbooks.”
- “Can you turn this repeated workflow into a proper Agent Skills package?”
- “Help me improve this skill description so it activates more reliably.”

Examples of **should not trigger** prompts:

- “Write a README for this repo.”
- “Create a Python library for parsing CSV files.”
- “Document our deployment process in Confluence style.”

## Train and validation split

Do not optimize the description against one static set of prompts only.

Split the prompt set into:

- train
- validation

Then improve the description on train and confirm it still generalizes on validation.
