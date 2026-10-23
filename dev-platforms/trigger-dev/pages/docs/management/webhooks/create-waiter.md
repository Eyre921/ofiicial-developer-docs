---
title: "Create a webhook waiter"
source: https://trigger.dev/docs/management/webhooks/create-waiter
path: docs/management/webhooks/create-waiter
---

v3-openapi POST /api/v1/webhooks/endpoints/{endpointId}/waiters
Create a waiter on an endpoint. A waiter is a waitpoint that completes when a matching delivery arrives on the endpoint, so a run waiting on its id resumes with the verified event. It only matches deliveries that arrive after it was created. Omit `match` to get a waiter with its own `url`, for providers that take a webhook URL per request.
