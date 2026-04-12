# Datadog notebooks reference

Source:

- https://docs.datadoghq.com/notebooks/

Use this reference to keep notebook drafts aligned with how Datadog notebooks actually work.

## What notebooks are good for

Datadog notebooks are collaborative rich-text documents that can combine live telemetry with operational narrative. They are suitable for:

- investigations
- postmortems
- runbooks
- service documentation

## Content a notebook can contain

Design notebook Markdown so it can map naturally to these Datadog elements:

- headers and automatic table of contents
- bullet lists, numbered lists, and checklists
- Markdown cells
- code blocks
- graphs and widgets
- images
- block quotes and callouts
- tables
- comments and collaborative review

## Reusable notebook features

Prefer these features when drafting reusable runbooks:

- template variables such as `$service`, `$env`, `$region`, `$cluster`
- global notebook time for coherent investigations
- local graph time only when a view needs an intentionally different scope
- notebook tags like `Runbook`, `Investigation`, `Documentation`
- team tags for ownership and discoverability

## Practical authoring guidance

- Keep headings specific so the table of contents is useful.
- Use concise sections instead of long narrative blocks.
- Put the highest-value graphs and queries first.
- Use checklists for mitigation and closure.
- Keep owner, scope, and escalation visible near the top.
- Prefer notebooks that can be reused and updated over one-off static documents.

## Template strategy

Datadog provides a template gallery and supports custom templates. For repeated operational patterns, write the runbook so it can become a reusable template rather than a one-off incident note.
