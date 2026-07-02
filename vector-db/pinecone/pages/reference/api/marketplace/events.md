---
title: "Events and analytics"
source: https://docs.pinecone.io/reference/api/marketplace/events
path: reference/api/marketplace/events
---

Read deployment events and analytics counters from Pinecone Marketplace.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Events and Analytics API lets you stream the deployment event log and read analytics counters programmatically.

## Operations

| Operation     | Description                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------- |
| List events   | Return events for a deployment, with filters by category, version, knowledge base, and outcome. |
| Stream events | Subscribe to new events as they occur.                                                          |
| Get analytics | Return counters such as conversation volume, refusal rate, and feedback summary for a window.   |

For the operator-facing guides, see [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
