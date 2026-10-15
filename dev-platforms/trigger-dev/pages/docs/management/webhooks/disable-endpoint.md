---
title: "Disable a webhook endpoint"
source: https://trigger.dev/docs/management/webhooks/disable-endpoint
path: docs/management/webhooks/disable-endpoint
---

v3-openapi POST /api/v1/webhooks/endpoints/{endpointId}/disable
**Private beta:** [request access](https://trigger.dev/webhooks-beta) to use webhooks.
Pause an endpoint. Its status becomes `inactive` and its URL responds with `404` until you enable it, so providers see failed deliveries and retry on their own schedule. Returns the updated endpoint.
