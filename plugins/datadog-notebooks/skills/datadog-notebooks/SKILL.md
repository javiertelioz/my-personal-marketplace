---
name: datadog-notebooks
description: Design Datadog notebook runbooks as Markdown for service troubleshooting and incident response. Use when the user wants to create or improve a Datadog notebook runbook, turn incident knowledge into an investigation flow, or document how to diagnose and recover a service.
---

# Datadog Notebook Runbooks

Design **Datadog notebook runbooks** that improve how responders investigate, mitigate, and validate issues in a service.

This skill does **not** assume direct access to Datadog. Instead, it builds the notebook from:

- user-provided service context
- known alerts and metrics
- codebase scanning for runtime and dependency clues
- recurring failure modes and remediation steps

The final output is **Markdown for the runbook notebook**, ready to be reviewed or later imported into the user’s Datadog notebook workflow.

## Core objective

Produce a notebook that helps engineers answer, in order:

1. **Is this the right runbook?**
2. **What should I check first?**
3. **What telemetry confirms the problem?**
4. **What dependencies might be involved?**
5. **What actions are safe to try?**
6. **How do I know the service recovered?**
7. **When do I escalate?**

## Important constraints

- Do **not** assume live Datadog access
- Do **not** invent real metric names, monitors, dashboards, or log fields unless clearly marked as placeholders
- You **may** scan the project to infer:
  - service boundaries
  - entrypoints
  - dependencies
  - background jobs
  - queues
  - databases
  - caches
  - external APIs
  - health checks
  - likely failure domains
- If critical telemetry details are missing, ask for them instead of guessing

## Required discovery

Before generating the notebook, collect enough context to make the runbook operational.

Ask about:

1. **Service and business function**
   - What service is this for?
   - What user journey or business capability does it support?
2. **Common problem pattern**
   - What issue is this runbook meant to solve?
   - Examples: latency spike, elevated 5xx, queue backlog, timeouts, deploy regression, dependency outage
3. **Signals**
   - Which metrics, logs, traces, or events do responders already use?
   - Which alerts or SLO symptoms trigger this runbook?
4. **Environment and scope**
   - prod only, all envs, region-specific, cluster-specific, tenant-specific
5. **Mitigation authority**
   - What actions are allowed? restart, rollback, scale up, fail over, feature flag toggle, drain queue, clear cache
6. **Escalation**
   - Who owns the service and who must be paged if mitigation fails?

If a repository is available, scan it to enrich the notebook with architectural context.

## Codebase scanning goals

When code is available, inspect the project to infer:

- application entrypoints and handlers
- scheduled jobs and workers
- database and cache usage
- downstream services and third-party integrations
- message queues and async pipelines
- feature flags and config surfaces
- health endpoints, readiness, liveness, and diagnostics
- logging conventions and error markers
- retry logic, circuit breakers, and timeout behavior

Use this to improve the runbook structure, but keep inferred details labeled as inferred if not confirmed by the user.

## Recommended notebook structure

Default to this structure unless the user asks for something different:

### 1. Title

Make it operational and specific.

Examples:

- `Checkout API - Elevated 5xx Runbook`
- `Payments Worker - Queue Backlog Investigation`
- `Auth Service - Latency Spike Triage`

### 2. Purpose and scope

- what this runbook covers
- when it should be used
- when it should not be used

### 3. Service context

- service summary
- critical dependencies
- blast radius
- owner team

### 4. Entry conditions

- alert names or symptoms
- thresholds or patterns
- prerequisite context to gather before acting

### 5. Template variables

Prefer reusable placeholders such as:

- `$env`
- `$service`
- `$region`
- `$cluster`
- `$team`
- `$dependency`

### 6. Triage views

Start with a small set of high-value telemetry:

- availability / error rate
- latency
- traffic / throughput
- saturation or backlog
- deploy or incident markers

### 7. Investigation flow

Organize by hypotheses:

- recent deploy regression
- dependency degradation
- database pressure
- cache failure
- queue congestion
- resource exhaustion
- bad config or feature flag

### 8. Mitigation options

For each mitigation:

- when to try it
- risk level
- exact validation after applying it

### 9. Validation

- what healthy looks like
- which signals must return to normal
- how long to observe

### 10. Escalation

- when to escalate
- to whom
- what evidence to include

### 11. Follow-up

- known gaps
- permanent fix ideas
- post-incident notes

## Markdown output format

Generate **Markdown**, not prose about Markdown.

The notebook content can mix:

- regular Markdown narrative and checklists
- notebook-oriented query blocks for logs, metrics, and events

### Prose sections

Use regular Markdown for:

- instructions
- checklists
- warnings
- rollback steps
- validation criteria
- escalation rules

### Log query block

Use this when you know or can safely propose a log stream query shape:

````markdown
```log-query
{
  "query": "service:$service env:$env status:error",
  "indexes": ["main"],
  "columns": ["service", "host", "@http.status_code", "@error.message"],
  "time": "4h"
}
```
````

### Metric query block

Use this for graphs the operator should look at first:

````markdown
```metric-query
{
  "query": "avg:service.request.latency{service:$service,env:$env}",
  "title": "Request Latency",
  "display_type": "line",
  "time": "4h",
  "events": [{"q": "source:deploy service:$service env:$env"}]
}
```
````

Use `queries` when multiple related signals belong in one graph.

### Event query block

Use this for deploy markers, incidents, or event-derived signals:

````markdown
```event-query
{
  "data_source": "events",
  "search": "source:deploy service:$service env:$env",
  "compute": "count",
  "title": "Deploy Events"
}
```
````

## Notebook UX guidance from Datadog

Design the notebook so it works well inside Datadog:

- use headings so the notebook gets a table of contents
- use concise sections instead of long paragraphs
- use numbered steps for procedures
- use checklists for mitigation and validation
- use tables for owners, thresholds, and escalation paths
- prefer a shared global time window for investigation coherence
- use template variables to avoid cloning notebooks per service or env
- structure the notebook so version history remains meaningful over time
- favor runbook-type notebooks with team tagging and service ownership clearly visible

## Output rules

When creating the notebook:

- generate the **actual notebook markdown**
- include placeholders only when necessary
- mark assumptions explicitly
- clearly separate:
  - confirmed facts
  - inferred architecture context
  - placeholder telemetry that needs user confirmation

If information is incomplete, still produce a useful draft, but annotate missing items with:

- `TODO: confirm metric name`
- `TODO: confirm monitor threshold`
- `TODO: confirm owner/escalation`

## Preferred response shape

Return:

1. Proposed notebook title
2. Short summary of what the runbook is for
3. The notebook markdown
4. A short list of unresolved telemetry placeholders, if any

## Anti-patterns

Avoid notebooks that are:

- generic and non-actionable
- only descriptive, with no investigation flow
- tied to one hardcoded env when reuse is expected
- missing validation after mitigation
- missing escalation criteria
- overloaded with low-value graphs before the primary signals
