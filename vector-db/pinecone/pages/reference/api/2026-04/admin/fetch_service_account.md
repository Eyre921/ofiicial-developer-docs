---
title: "Get service account details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_service_account
path: reference/api/2026-04/admin/fetch_service_account
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/service-accounts/{service_account_id}
Get a service account by ID; the client secret is returned only from create and rotate-secret requests.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c"

  curl -X GET "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "name": "My Service Account",
    "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
