# Notebook Markdown rules and validation

Use this reference for validation, constraints, and warning conditions when writing Datadog notebook Markdown.

## Cell parsing rules

- Empty or whitespace-only Markdown between special blocks is dropped.
- Leading and trailing blank lines in Markdown cells are trimmed.
- Regular code fences such as ```` ```python ```` or ```` ```json ```` are treated as normal Markdown.
- A `log-query`, `metric-query`, or `event-query` block inside another fenced block is **not** treated as special.

## Error conditions

These should be treated as errors:

- unterminated `log-query`, `metric-query`, or `event-query` blocks
- invalid JSON inside special blocks
- missing required fields:
  - `query` for `log-query`
  - `query` or `queries` for `metric-query`
  - `data_source`, `search`, and `compute` for `event-query`

Special query blocks only count when they are real top-level fenced blocks. A `log-query`, `metric-query`, or `event-query` block embedded inside another fenced code block is not special syntax.

## Section link validation

Links such as `[text](#slug)` must reference a heading that actually exists in the document.

Warn if a link target does not match any heading slug.

## Template variable consistency

If a template variable defines a prefix such as:

```yaml
- name: env
  prefix: env
```

then queries should not hardcode a conflicting value such as:

```text
env:staging
```

If a query hardcodes a value for a declared variable prefix, treat it as a warning or a failure depending on workflow strictness.

In stricter workflows, this warning can be promoted to a failure unless the user explicitly acknowledges it.

## Time span values

The notebook global time span can be set separately, and individual query cells can override it with a `time` field.

Supported relative values commonly include:

| Value | Meaning |
|---|---|
| `1m` | Past 1 minute |
| `5m` | Past 5 minutes |
| `10m` | Past 10 minutes |
| `15m` | Past 15 minutes |
| `30m` | Past 30 minutes |
| `1h` | Past 1 hour |
| `4h` | Past 4 hours |
| `1d` | Past 1 day |
| `2d` | Past 2 days |
| `1w` | Past 1 week |

Absolute time is also allowed through:

```json
{
  "start": "2026-02-20T00:00:00Z",
  "end": "2026-02-24T00:00:00Z"
}
```

## Annotation guidance

Annotations are only useful when their timestamps fall within the visible time range of the related graphs.

When authoring an `## Annotations` section:

- keep timestamps aligned with notebook time windows
- keep descriptions short and operationally meaningful
- prefer incident, deploy, and recovery markers

## Practical authoring guardrails

- Prefer a small number of high-value graphs over dashboard sprawl.
- Keep frequent-incident runbooks short enough to traverse quickly.
- Put escalation criteria in plain sight.
- Keep monitor linkage visible so responders can reach the runbook from the alert.
- Use TODO markers instead of inventing telemetry.
