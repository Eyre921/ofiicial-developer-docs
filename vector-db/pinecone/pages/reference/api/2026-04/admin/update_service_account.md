---
title: "Update a service account"
source: https://docs.pinecone.io/reference/api/2026-04/admin/update_service_account
path: reference/api/2026-04/admin/update_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml patch /admin/service-accounts/{service_account_id}
Update a service account's mutable metadata. Only `name` is supported as a mutable field; fields that are omitted are left unchanged.
Role bindings cannot be updated here; use the role binding endpoints to create or delete bindings.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="YOUR_SERVICE_ACCOUNT_ID"

  curl -X PATCH "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "ci-prod-renamed"
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "name": "ci-prod-renamed",
    "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
