# Evaluating a skill

Use this reference when the skill is ready to test.

## Two kinds of evaluation

### 1. Output-quality evals

These test whether the skill produces good results for realistic tasks.

Store them in:

`evals/evals.json`

Each eval should include:

- `id`
- `prompt`
- `expected_output`
- optional `files`
- optional `assertions`

## Example eval structure

```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Create a runbook for the most common queue lag incident in payments.",
      "expected_output": "A runbook with triage, metrics, logs, mitigation, and escalation criteria.",
      "assertions": [
        "The output includes escalation criteria",
        "The output includes at least one metric section"
      ]
    }
  ]
}
```

### 2. Trigger-quality evals

These test whether the description causes the skill to activate when it should.

Store them in:

`evals/description-eval-queries.json`

Each query should include:

- `query`
- `should_trigger`

## Evaluation workflow

1. run the task **with** the skill
2. run the same task against a baseline
3. compare quality, correctness, and cost
4. add assertions where pass/fail can be checked objectively

## Good eval habits

- start with 2 to 3 realistic evals
- include near-misses for trigger testing
- vary phrasing and detail level
- include at least one edge case
- improve assertions after seeing the first results

## Scaffolding

Use:

```bash
python3 scripts/scaffold-evals.py --skill-path /path/to/skill
```

This writes starter eval files you can customize.
