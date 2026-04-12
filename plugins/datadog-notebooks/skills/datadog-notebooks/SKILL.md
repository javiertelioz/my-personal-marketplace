---
name: datadog-notebooks
description: Design Datadog notebook runbooks as Markdown for service troubleshooting and incident response. Use when the user wants to create or improve a Datadog notebook runbook, turn incident knowledge into an investigation flow, or document how to diagnose and recover a service.
---

# Datadog Notebook Runbooks

Create **Datadog notebook runbooks in Markdown** for operational troubleshooting, incident response, and recurring service issues.

This skill is for authoring the **Markdown source** of a Datadog notebook runbook. It is optimized for responders who need a practical document with:

- clear trigger conditions
- the fastest useful triage steps
- metrics, logs, traces, and events to inspect
- safe mitigation options
- explicit escalation criteria
- follow-up and ownership

## What this skill does

- designs runbooks for recurring incident patterns such as high error rate, latency spikes, provider timeouts, and queue lag
- asks for the minimum context needed to make the runbook operational
- scans the codebase when available to infer service boundaries, dependencies, and likely failure domains
- produces the **actual notebook Markdown**
- uses reusable placeholders when real telemetry names are not confirmed
- keeps the output aligned with Datadog notebook authoring patterns

## What this skill does not do

- it does **not** assume live access to Datadog
- it does **not** invent confirmed metric names, monitor IDs, dashboards, or log fields
- it does **not** treat the runbook like a static wiki page
- it does **not** generate bloated incident flows when a short triage path is enough

## Bundled references

Use these references while writing the runbook:

- `references/notebooks-reference.md`
- `references/metrics-reference.md`
- `references/sre-runbook-guidance.md`
- `references/notebook-markdown-format.md`
- `references/notebook-markdown-rules.md`
- `references/notebook-markdown-example.md`
- `templates/runbook-template.md`

Use them as follows:

- use the **format** reference for special fenced blocks, frontmatter, links, and annotations
- use the **rules** reference for validation, time values, and warning conditions
- use the **example** reference for end-to-end notebook structure
- use the **metrics** reference for safe placeholder strategy and tag guidance
- use the **SRE guidance** reference to avoid operational anti-patterns
- use the **template** when the user wants a reusable runbook skeleton

## Required discovery

Before drafting the notebook, gather enough context to make it actionable:

1. **Service**
   - What service or system is this for?
   - What business capability does it support?
2. **Incident pattern**
   - What problem should the runbook solve?
   - Examples: high error rate, provider timeout, latency spike, queue lag
3. **Signals**
   - Which metrics, logs, traces, or events are already used?
   - Which alert or symptom should lead responders to this runbook?
4. **Scope**
   - production only, all envs, specific region, cluster, or tenant
5. **Mitigation authority**
   - What actions are allowed: restart, rollback, scale, fail over, feature flag change, queue drain, cache clear
6. **Escalation**
   - Who owns the system and when must the responder escalate?
7. **Monitor linkage**
   - Which monitors should point to this runbook?
8. **Governance**
   - Who owns the runbook?
   - When was it last reviewed?

If a repository is available, inspect it to infer:

- entrypoints and handlers
- workers and scheduled jobs
- queues, databases, caches, and external APIs
- health checks and diagnostics
- logging patterns, retries, circuit breakers, and timeouts

## Authoring approach

When generating the notebook:

1. Start with a **specific title** and narrow scope.
2. Keep the first triage pass short enough for a responder to traverse quickly.
3. Put the highest-value telemetry first.
4. Organize investigation steps by hypotheses when useful.
5. Include mitigation with validation after each action.
6. Add explicit escalation criteria.
7. Keep ownership, review date, and related monitors visible near the top.
8. Mark assumptions and unresolved telemetry as TODOs.

## Output requirements

Return:

1. proposed notebook title
2. short summary of the runbook purpose
3. the full notebook Markdown
4. unresolved placeholders that still need confirmation

## Output rules

- generate the **actual Markdown**, not commentary about Markdown
- prefer reusable placeholders such as `$service`, `$env`, `$region`, `$cluster`, and `$dependency`
- clearly distinguish confirmed facts from inferred context
- use `TODO:` markers for unconfirmed telemetry details
- follow the special Markdown block rules in `references/notebook-markdown-format.md`
- enforce the validation constraints in `references/notebook-markdown-rules.md`

## Operational quality bar

The runbook should help responders answer:

1. Is this the right runbook?
2. What should I check first?
3. Which signals confirm the issue?
4. What dependencies are likely involved?
5. What actions are safe to try?
6. How do I confirm recovery?
7. When do I escalate?
