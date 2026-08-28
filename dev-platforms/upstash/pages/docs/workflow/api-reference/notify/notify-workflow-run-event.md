---
title: "Notify Workflow Run Event"
source: https://upstash.com/docs/workflow/api-reference/notify/notify-workflow-run-event
path: docs/workflow/api-reference/notify/notify-workflow-run-event
---

/workflow/openapi.yaml post /v2/notify/{workflowRunId}/{eventId}
Notify an event to a specific workflow run's waiters.

This endpoint sends an event notification to waiters within a specific workflow run.
Unlike the general notify endpoint, this uses a "safe notify" mechanism that guarantees
delivery even if no waiter is currently active.

**Safe Notify Behavior:**
- If a waiter is currently active, it receives the notification immediately
- If no waiter is active, the notification is saved in the database
- When a waiter becomes active later, it will consume the saved notification
- This ensures events are never lost due to timing issues
