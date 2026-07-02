---
title: "Complete a waitpoint token via HTTP callback"
source: https://trigger.dev/docs/management/waitpoints/complete-callback
path: docs/management/waitpoints/complete-callback
---

v3-openapi POST /api/v1/waitpoints/tokens/{waitpointId}/callback/{callbackHash}
Completes a waitpoint token using the pre-signed callback URL returned in the `url` field when the token was created. No API key is required — the `callbackHash` in the URL acts as the authentication token.

This is designed to be given directly to external services (e.g. as a webhook URL) so they can unblock a waiting run without needing access to your API key. The entire request body is passed as the output data to the waiting run.

If the token is already completed, this is a no-op and returns `success: true`.
