---
title: "Complete a waitpoint token"
source: https://trigger.dev/docs/management/waitpoints/complete
path: docs/management/waitpoints/complete
---

v3-openapi POST /api/v1/waitpoints/tokens/{waitpointId}/complete
Completes a waitpoint token, unblocking any run that is waiting for it via `wait.forToken()`. An optional `data` payload can be passed and will be returned to the waiting run. If the token is already completed, this is a no-op and returns `success: true`.

This endpoint accepts both secret API keys and short-lived JWTs (public access tokens), making it safe to call from frontend clients.
