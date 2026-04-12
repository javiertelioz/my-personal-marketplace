# Example Datadog notebook Markdown

Use this example as a reference for overall shape, special query blocks, and Markdown-to-cell flow.

## Example Markdown file

````markdown
---
variables:
  - name: env
    prefix: env
    default: production
  - name: service
    prefix: service
    default: auth
---

# Production Error Investigation

We have seen a spike in 5xx errors from the auth service.

## CPU usage during the incident

```metric-query
{"query": "avg:system.cpu.user{service:$service,env:$env}", "time": "4h"}
```

## Auth service errors

```log-query
{"query": "service:$service status:error env:$env"}
```

Errors appear clustered around 2pm UTC. Check the downstream database path next.

## Database timeouts

```log-query
{"query": "service:postgres-proxy @duration:>5000 env:$env", "indexes": ["main"], "time": "1d"}
```

## Next steps

- Check recent deploys to the auth service
- Review connection pool settings
````

## Resulting notebook cells

This Markdown produces six notebook cells:

1. Markdown cell for the title and introductory paragraph
2. Timeseries cell for `avg:system.cpu.user{service:$service,env:$env}`
3. Log Stream cell for `service:$service status:error env:$env`
4. Markdown cell for the analysis paragraph and the `Database timeouts` heading
5. Log Stream cell for `service:postgres-proxy @duration:>5000 env:$env`
6. Markdown cell for the `Next steps` checklist

## Why this example is useful

It demonstrates:

- YAML frontmatter for template variables
- normal prose mixed with query cells
- relative cell time overrides
- a short investigation narrative
- a practical notebook progression from symptom to dependency check
