---
title: "Notify Event"
source: https://upstash.com/docs/workflow/api-reference/notify/notify-event
path: docs/workflow/api-reference/notify/notify-event
---

/workflow/openapi.yaml post /v2/notify/{eventId}
Notify an event to all waiters listening for that event ID.

This endpoint broadcasts an event to all active waiters that are waiting for the specified event.
Each waiting workflow step receives the event data and continues execution.

**Important:** This is an "unsafe notify" operation - if there are no active waiters when the
notification is sent, the event is lost and will not be delivered later. For guaranteed delivery
within a specific workflow run, use the `/v2/notify/{workflowRunId}/{eventId}` endpoint instead.
