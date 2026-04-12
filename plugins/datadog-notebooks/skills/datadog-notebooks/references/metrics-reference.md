# Datadog metrics reference

Sources:

- https://docs.datadoghq.com/api/latest/metrics/?code-lang=go
- https://docs.datadoghq.com/metrics/

Use this reference when proposing metric sections, placeholders, and query structure for a runbook.

## Key metric concepts to respect

Do not invent real metric names when the repository or user has not confirmed them. Instead:

- infer likely signal categories
- propose placeholder metric names
- clearly mark TODOs for confirmation

## Common metric categories for runbooks

Start from signal categories rather than fake names:

- throughput
- error rate
- latency p50 / p95 / p99
- saturation
- backlog / queue depth
- dependency health
- retries / timeouts
- resource pressure

## Tags and queryability

The Datadog metrics API documentation highlights that metrics are shaped by metric type and queryable tags. When drafting placeholders, prefer tag dimensions responders are likely to use:

- `service`
- `env`
- `region`
- `cluster`
- `team`
- `endpoint`
- `dependency`
- `queue`

## Safe guidance for placeholder metrics

When no canonical metric is known, prefer placeholders like:

- `TODO: confirm request latency metric`
- `TODO: confirm 5xx error rate metric`
- `TODO: confirm queue lag metric`

Avoid pretending a metric definitely exists unless it was:

- provided by the user
- found in code or telemetry definitions
- found in monitor configuration

## Query design guidance

- Favor a small number of high-value queries over graph overload.
- Keep the first section focused on confirmation and triage.
- Add comparison or decomposition only when it helps isolate the cause.
- If a signal likely depends on tags, call out the expected tag dimensions explicitly.
