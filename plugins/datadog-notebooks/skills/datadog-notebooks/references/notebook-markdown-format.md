# Datadog notebooks from Markdown

Use this reference when writing Markdown that is intended to become a Datadog notebook.

The Datadog notebooks CLI creates and updates Datadog notebooks from `.md` files. Each Markdown file is parsed into notebook cells.

## Markdown format

A notebook Markdown file contains two kinds of content:

1. **Prose** — becomes Markdown cells
2. **Special fenced query blocks** — become Datadog notebook query cells

## Prose becomes Markdown cells

Any regular Markdown becomes a Markdown cell in the notebook:

- headings
- paragraphs
- lists
- links
- images

Standard fenced code blocks such as ```` ```python ```` or ```` ```json ```` are preserved inside the Markdown cell as normal Markdown content.

## `log-query` becomes a Log Stream cell

A fenced code block tagged `log-query` is parsed as JSON and becomes a Log Stream cell.

The JSON body must have:

- `query` — required

It may also include:

- `indexes`
- `columns`
- `time`

### Example with columns and relative time

```log-query
{
  "query": "service:web env:production",
  "indexes": ["main"],
  "columns": ["@backend", "@error", "@resp_type"],
  "time": "4h"
}
```

### Example with absolute time

```log-query
{
  "query": "service:web env:production",
  "time": {
    "start": "2026-02-20T00:00:00Z",
    "end": "2026-02-24T00:00:00Z"
  }
}
```

### `log-query` fields

| Field | Required | Description |
|---|---|---|
| `query` | Yes | Datadog log query string |
| `indexes` | No | List of log indexes to search |
| `columns` | No | List of columns to display |
| `time` | No | Relative span string such as `"4h"` or an absolute `{start,end}` object |

## `metric-query` becomes a Timeseries cell

A fenced code block tagged `metric-query` is parsed as JSON and becomes a Timeseries cell.

The JSON body must have either:

- `query` — single metric query
- `queries` — multiple metric queries in one graph

### Simple metric query

```metric-query
{
  "query": "avg:system.cpu.user{env:production}",
  "time": "4h"
}
```

### Metric query with title, aliases, and display type

```metric-query
{
  "query": "avg:system.cpu.user{env:production} by {host}",
  "title": "CPU Usage by Host",
  "aliases": {
    "avg:system.cpu.user{env:production} by {host}": "CPU"
  },
  "display_type": "area",
  "time": {
    "start": "2026-02-17T08:00:00Z",
    "end": "2026-02-26T08:00:00Z"
  }
}
```

### Multiple queries in one graph

```metric-query
{
  "queries": [
    "p50:service.latency{env:production}",
    "p95:service.latency{env:production}",
    "p99:service.latency{env:production}"
  ],
  "aliases": {
    "p50:service.latency{env:production}": "p50",
    "p95:service.latency{env:production}": "p95",
    "p99:service.latency{env:production}": "p99"
  },
  "title": "Latency Percentiles"
}
```

### Metric query with event overlays

```metric-query
{
  "query": "avg:system.cpu.user{env:production}",
  "events": [
    {"q": "source:statsig gate:my_flag"},
    {"q": "source:deploy env:production"}
  ]
}
```

### `metric-query` fields

| Field | Required | Description |
|---|---|---|
| `query` | Yes* | Datadog metric query string |
| `queries` | No | Array of metric query strings for multi-line graphs |
| `time` | No | Relative span string or absolute `{start,end}` object |
| `title` | No | Graph title |
| `aliases` | No | Map of query expression to legend name |
| `display_type` | No | `"line"`, `"bars"`, or `"area"` |
| `events` | No | Array of event overlay queries like `{"q": "..."}` |

\* `query` is not required when `queries` is used.

## `event-query` becomes an event-based Timeseries cell

A fenced code block tagged `event-query` is parsed as JSON and becomes a Timeseries cell backed by the formula-and-functions event query API.

### Simple count

```event-query
{
  "data_source": "events",
  "search": "source:deploy env:production",
  "compute": "count",
  "title": "Deploy Events"
}
```

### Aggregation with metric and grouping

```event-query
{
  "data_source": "events",
  "search": "source:deploy",
  "compute": "avg",
  "metric": "@duration",
  "group_by": [
    {
      "facet": "service",
      "limit": 10
    }
  ],
  "title": "Deploy Duration by Service",
  "display_type": "bars",
  "time": "4h"
}
```

### `event-query` fields

| Field | Required | Description |
|---|---|---|
| `data_source` | Yes | Source such as `events`, `logs`, `rum`, `spans`, `security_signals`, `audit`, `ci_tests`, `ci_pipelines` |
| `search` | Yes | Filter query string |
| `compute` | Yes | Aggregation such as `count`, `avg`, `sum`, `min`, `max`, `median`, `pc95`, `pc99`, `cardinality` |
| `metric` | No | Metric field for aggregations other than count |
| `group_by` | No | Array of grouping objects like `{"facet": "field", "limit": 10}` |
| `title` | No | Graph title |
| `display_type` | No | `"line"`, `"bars"`, or `"area"` |
| `time` | No | Relative span string or absolute `{start,end}` object |
| `events` | No | Event overlay queries |

## Template variables

Notebooks can include template variables such as `$env` or `$service`. Define them in a YAML frontmatter block at the very top of the Markdown file:

```yaml
---
variables:
  - name: env
    prefix: env
    default: production
  - name: service
    prefix: service
    default: "*"
---
```

The frontmatter block must be the first thing in the file, ignoring leading whitespace.

Only the `variables` key is recognized.

When reading a notebook back through the same workflow, template variables are emitted as frontmatter again, so the format round-trips cleanly.

### Template variable fields

| Field | Description |
|---|---|
| `name` | Variable name, used as `$name` in queries |
| `prefix` | Tag prefix such as `env` or `service` |
| `default` | Default dropdown value |

## Section links

You can write links like `[text](#heading-slug)` to create cross-references between sections.

These use GitHub-style heading slugs:

- lowercase
- hyphens for spaces and punctuation

Important: Datadog does not natively support `#slug` anchor navigation. A post-processing bookmarklet can convert these links into working `?cell_id=` URLs after notebook creation.

## Annotations

You can define graph annotations in an `## Annotations` section at the end of the notebook. Each line defines a point-in-time marker intended to appear on all timeseries graphs.

### Format

```text
## Annotations
- YYYY-MM-DD HH:MM UTC | color | Description text
```

### Example

```text
## Annotations
- 2026-02-05 13:00 UTC | red | Regression onset - latency spike begins
- 2026-02-06 09:00 UTC | gray | Deploy abc123 - cache layer update
- 2026-02-07 15:30 UTC | green | Recovery - metrics back to baseline
```

Available colors:

- `red`
- `yellow`
- `green`
- `blue`
- `purple`
- `pink`
- `orange`
- `gray`

## Bookmarklet note

A post-processing bookmarklet can perform two tasks after the notebook is created or updated:

1. resolve section links into working notebook cell URLs
2. create annotations from the `## Annotations` section

When authoring Markdown, keep this in mind:

- section links should target real headings
- annotation timestamps should line up with the notebook time range

If the workflow uses a local `dd-notebook-enhance.js` bookmarklet source, the typical generation flow is:

```sh
npx terser datadog/src/notebooks/dd-notebook-enhance.js --compress --mangle \
  | tr -d '\n' | sed 's/;$//' \
  | { echo -n 'javascript:void('; cat; echo -n ')'; } \
  | pbcopy
```

That bookmarklet is meant to be run in the browser after creating or updating the notebook.
