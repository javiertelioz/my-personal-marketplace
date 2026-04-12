# SRE runbook guidance for Datadog notebooks

Use this reference to keep runbooks operational, short, and actionable.

## Recommended operating sequence

The healthiest adoption cycle is:

1. alert appears frequently
2. create a runbook-style notebook
3. embed metrics, logs, and actionable links
4. link the notebook from the relevant monitor
5. use it during real incidents
6. refine it after every incident

## Common SRE mistakes

### 1. Using the notebook like a static wiki

If the notebook has no metrics, queries, or actionable links, it is not taking advantage of Datadog.

### 2. Adding too many steps

A runbook for a frequent incident should usually be traversable in **3 to 7 minutes**.

### 3. Omitting escalation criteria

The on-call responder needs a clear point where investigation stops and escalation starts.

### 4. Not revising the runbook after a real incident

Every incident should improve the runbook:

- clarify confusing steps
- add stronger queries
- remove low-value checks
- capture better signals

### 5. Not linking the runbook to the monitor

If the runbook is not close to the alert, responders are less likely to use it.

## Monitor linkage guidance

When relevant, the output should instruct the user to:

- attach the runbook link to the related monitor
- include the runbook in monitor messages or supported operational assets
- keep the runbook URL stable so responders always land in the same place

## Minimum governance

Every reusable runbook should expose:

- runbook owner
- associated service
- responsible team
- last review date
- typical severity or supported use cases

## Good first target

If the team is starting from scratch, document only one painful recurring incident first, such as:

- high error rate
- provider timeout
- latency spike
- queue lag
