# [Runbook] <Incident Name>

## Objective
Describe the incident pattern this runbook covers and what outcome it helps accelerate.

## Service / Owner
- Service:
- Team:
- Runbook owner:
- Last review:
- Typical severity:

## When to use it
- Related monitors:
- Symptoms:
- Triggering alerts:
- When not to use it:

## Impact
- Technical:
- Business:

## Initial validation
- [ ] Confirm incident scope
- [ ] Check for a recent deploy
- [ ] Validate external dependency health
- [ ] Review primary metrics
- [ ] Review recent logs

## Suggested variables
- `$service`
- `$env`
- `$region`
- `$cluster`
- `$dependency`

## Metrics to review
- Throughput
- Error rate
- Latency p95/p99
- Saturation
- Dependency metrics

```metric-query
{
  "query": "TODO: confirm primary metric {service:$service,env:$env}",
  "title": "Primary incident signal",
  "display_type": "line",
  "time": "4h"
}
```

## Logs to review

### Query 1

```log-query
{
  "query": "service:$service env:$env status:error",
  "indexes": ["main"],
  "time": "4h"
}
```

### Query 2

```log-query
{
  "query": "service:$service env:$env @http.status_code:[500 TO 599]",
  "indexes": ["main"],
  "time": "4h"
}
```

## Traces / APM
- Most affected endpoint:
- Slowest operation:
- Dependent service with the highest error volume:

## Investigation hypotheses
1. Recent deploy or configuration change
2. External dependency degradation
3. Resource saturation
4. Queue or backlog abnormality
5. Functional error or regression

## Mitigation
1. Possible mitigation:
   - When to apply it:
   - Risk:
   - Post-action validation:
2. Possible mitigation:
   - When to apply it:
   - Risk:
   - Post-action validation:

## Escalation

Escalate if:

- there is no improvement after the expected mitigation
- the impact exceeds the tolerated severity
- the likely cause belongs to another team or provider
- the on-call lacks permissions or the ability to act

## Closure criteria
- [ ] Error rate returns to baseline
- [ ] Latency normalizes
- [ ] No critical backlog remains
- [ ] Communication is sent
- [ ] Evidence is captured

## Follow-up
- Preventive action 1
- Preventive action 2
- New query or metric to add
- Unnecessary step to remove

## Minimum governance
- Associated service:
- Responsible team:
- Use cases:
- Last review date:
- Next review:
