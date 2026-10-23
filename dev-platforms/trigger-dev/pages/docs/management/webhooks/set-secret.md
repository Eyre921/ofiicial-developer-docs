---
title: "Set a webhook signing secret"
source: https://trigger.dev/docs/management/webhooks/set-secret
path: docs/management/webhooks/set-secret
---

v3-openapi PUT /api/v1/webhooks/endpoints/{endpointId}/secret
Store the signing secret or public key the provider issued for this endpoint, such as the `whsec_` secret Stripe returns when you create a webhook endpoint. It replaces the existing secret. Pass `previousSecretTtlSeconds` to keep accepting the old secret for a while, for example while the provider rolls its secret.
