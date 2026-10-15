---
title: "List webhook endpoints"
source: https://trigger.dev/docs/management/webhooks/list-endpoints
path: docs/management/webhooks/list-endpoints
---

v3-openapi GET /api/v1/webhooks/endpoints
**Private beta:** [request access](https://trigger.dev/webhooks-beta) to use webhooks.
List the hosted webhook endpoints in the environment, ordered by declared id. Each endpoint includes its webhook URL and whether its signing secret is set. The secret itself is never returned.
