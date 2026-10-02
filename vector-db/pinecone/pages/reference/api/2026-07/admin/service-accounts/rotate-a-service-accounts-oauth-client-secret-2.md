---
title: "Rotate a service account's OAuth client secret"
source: https://docs.pinecone.io/reference/api/2026-07/admin/service-accounts/rotate-a-service-accounts-oauth-client-secret
path: reference/api/2026-07/admin/service-accounts/rotate-a-service-accounts-oauth-client-secret
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/admin_2026-07.oas.yaml post /admin/service-accounts/{service_account_id}/rotate-secret
Rotate a service account's OAuth client secret; the previous secret and its tokens are revoked within seconds and the new secret is returned only once.
