---
title: "Analytics and event logs"
source: https://docs.pinecone.io/guides/marketplace/analytics-and-event-logs
path: guides/marketplace/analytics-and-event-logs
---

Track end-user activity, refusal rates, feedback, and event logs in a Pinecone Marketplace deployment for analytics, auditing, and debugging.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Every deployment has a dashboard with analytics and an append-only event log. Use them to understand how end users are using the knowledge application and where it can be improved.

## Analytics

The analytics view shows:

* Active end users over time.
* Conversation and query volume.
* Refusal rate, broken down by `OUT_OF_SCOPE` and `BLOCKED` outcomes.
* Most-asked questions.
* Feedback ratings over time.
* Per-version traffic and quality trends.

Use analytics to spot patterns: a sudden spike in refusals usually means a content gap or a poorly scoped knowledge base; a drop in feedback ratings after a publish usually means a regression.

## Event log

The event log captures every meaningful action for a deployment. Events include:

| Category     | What it covers                                                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Lifecycle    | Deployment created, version building, publish started, publish completed, version active, version failed, rollback.                                                            |
| Chat         | Each query, the routing decision, the Knowledge Agent Toolkit (KAT) outcome (`CALL_KB`, `ASK_SLOT`, `BLOCKED`, `OUT_OF_SCOPE`), the knowledge bases queried, and the response. |
| Feedback     | Thumbs-up and thumbs-down ratings, with optional comments.                                                                                                                     |
| Sync         | Source sync runs, with success or failure and per-file detail.                                                                                                                 |
| Provisioning | Background provisioning steps for each publish.                                                                                                                                |

Events are append-only and timestamped. The dashboard supports filtering and searching by category, version, knowledge base, and outcome.

## Using analytics and events together

A typical investigation looks like this:

1. Notice an increase in refusals in analytics.
2. Filter the event log to recent `OUT_OF_SCOPE` outcomes.
3. Find common patterns in the refused questions.
4. Decide whether to add content, expand scope, or adjust manifests.
5. Edit the deployment, publish a new version, and watch the next round of analytics.

## Exporting and integrations

Analytics and events surface in the deployment dashboard. Programmatic access through the API is also available; see the [Reference](/reference/api/marketplace/events) tab.
