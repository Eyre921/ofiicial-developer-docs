---
title: "P1 alert intake"
source: https://docs.fireworks.ai/field-eng/p1-alert-intake
path: field-eng/p1-alert-intake
---

How to get a new or materially changed P1 customer alert approved to page.

A new or materially changed P1 customer alert needs an intake file before it can page.
Only about 10% of alerts in `#customer-incidents-alerts` were ever acked, so each P1 now
has to justify waking someone.

## The process

<Steps>
  <Step title="Open your PR with the alert change" />

  <Step title="Add the intake file">
    Copy [`example.yaml.template`](https://github.com/fw-ai/fireworks/blob/main/terraform/gcp/fw-ai-cp-prod/alerts/intake/example.yaml.template) in the alerts `intake/` folder to `<alert-name>.yaml`.
  </Step>

  <Step title="Fill it in">
    Owner and customer, critical impact, signal, threshold and duration with rationale,
    evidence, expected pages per month, on-call action, runbook, review date. Push without
    the resource address or fingerprint if you don't have them. CI reports the exact
    values to paste.
  </Step>

  <Step title="CI validates the file">
    CI checks the intake file against your Terraform plan and fails if it is missing, incomplete, or inconsistent.
  </Step>

  <Step title="The review agent comments on your PR">
    It reads the diff and the planned alert, opens your evidence links, and flags arbitrary
    thresholds, low-sample conclusions, likely false positives, and runbooks with no action.
    It posts `RECOMMEND`, `DO NOT RECOMMEND`, or `INSUFFICIENT EVIDENCE` with citations.
    Advisory only. It cannot approve or merge.
  </Step>

  <Step title="A human approves the paging decision">
    Prefer the most recent customer on-call as reviewer.
  </Step>
</Steps>

The file stays in Git as the record of why the alert is allowed to page.

## When intake is required

Creating a new critical customer alert, promoting an alert to critical, or materially
changing an enrolled P1: its signal or query, threshold, duration, scope, severity,
routing, owner, or runbook.

Not required for P2 and P3 alerts, severity downgrades, or formatting-only edits. P1s
predating the process are reported as a notice, not a failure.

## What qualifies as P1

| Criterion | Definition | Examples |
| - | - | - |
| **SLA violation** | Customer production traffic is failing or breaching an agreed SLA at meaningful scale | 429s blocking production inference; majority of requests failing; majority of traffic over agreed latency |
| **Loss of service** | An active, agreed customer need is unmet, causing loss of service or a customer-side incident | Production deployment down and not serving; traffic in a forbidden region; high rate of 500s |

<Warning>
  If neither criterion applies, it is not a P1. Route it to the customer's Slack channel or
  a dashboard instead. P0 and P1 page a phone, P2 pings Slack, and P3 does not belong in
  `#customer-incidents-alerts` at all.
</Warning>

A past incident is not required. A first-occurrence risk qualifies when the failure mode is
credible, the impact would be critical, and the threshold is supported by testing, capacity
limits, or SLO modeling.

## Review criteria

Reviewers approve only when the impact meets one of the two criteria, the threshold follows
from the cited evidence, the expected page volume is reasonable for a phone page, routing
and ownership are correct, and the on-call has a documented immediate action. Approvals
should say so explicitly.

## After approval

Each intake carries a review date, and due alerts are reassessed against ack rate. A daily
DM lists the alerts that paged you with **Actionable** and **Not actionable** buttons.
Rating them is what drives alert cleanup. Raise problem alerts in `#amle-on-call-automation`.
