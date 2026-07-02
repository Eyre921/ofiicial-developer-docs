---
title: "Oauth Callback"
source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback
path: api-reference/auth-service-v2/oauth-callback
---

https://api.host.langchain.com/openapi.json post /v2/auth/callback/{provider_id}
Finalize an OAuth flow.

Claims the auth request, verifies the caller, exchanges the code, and saves the token.
Used by both the frontend bridge and the headless flow (where a customer-owned service
forwards the code/state, optionally proxied through smith-go). In all cases the auth
request is user-initiated and the caller presents the end user's own credentials, so
the authenticated user must match the user who initiated the flow.
