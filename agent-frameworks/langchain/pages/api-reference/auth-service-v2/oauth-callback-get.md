---
title: "Oauth Callback Get"
source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback-get
path: api-reference/auth-service-v2/oauth-callback-get
---

https://api.host.langchain.com/openapi.json get /v2/auth/callback/{provider_id}
Handle OAuth callback redirect from OAuth providers.

Processes the OAuth token exchange, then redirects to the frontend callback
page for a consistent UI experience.
