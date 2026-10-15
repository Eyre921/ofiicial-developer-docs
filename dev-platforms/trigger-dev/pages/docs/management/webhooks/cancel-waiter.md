---
title: "Cancel a webhook waiter"
source: https://trigger.dev/docs/management/webhooks/cancel-waiter
path: docs/management/webhooks/cancel-waiter
---

v3-openapi POST /api/v1/webhooks/waiters/{waiterId}/cancel
**Private beta:** [request access](https://trigger.dev/webhooks-beta) to use webhooks.
Cancel a waiter. It stops matching deliveries, frees its slot toward the endpoint's limit, and fails the run's wait. If a delivery already claimed the waiter, the cancel is too late: the response has `cancelled: false` with `reason: "too_late"`, and the run resumes with that delivery's event.
