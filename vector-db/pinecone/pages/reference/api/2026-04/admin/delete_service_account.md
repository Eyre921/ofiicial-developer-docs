---
title: "Delete a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_service_account
path: reference/api/2026-04/admin/delete_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/service-accounts/{service_account_id}
Delete a service account and its role bindings. Returns `202`; the service account is then no longer returned by get requests (returns `404`).
OAuth tokens minted by the service account are revoked within a few seconds.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="YOUR_SERVICE_ACCOUNT_ID"

  curl -X DELETE "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
