---
title: "Generate a webhook signing secret"
source: https://trigger.dev/docs/management/webhooks/generate-secret
path: docs/management/webhooks/generate-secret
---

v3-openapi POST /api/v1/webhooks/endpoints/{endpointId}/rotate-secret
**Private beta:** [request access](https://trigger.dev/webhooks-beta) to use webhooks.
Generate a new signing secret for the endpoint, store it, and return it once. Use this for providers where you choose the secret, such as GitHub. It replaces any existing secret, so deliveries fail verification until the provider uses the new one. Endpoints whose source verifies with a public key refuse this; set the provider's key with the set secret endpoint instead.
