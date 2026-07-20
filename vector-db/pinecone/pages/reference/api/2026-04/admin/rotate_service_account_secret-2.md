---
title: "Rotate a service account's OAuth client secret"
source: https://docs.pinecone.io/reference/api/2026-04/admin/rotate_service_account_secret
path: reference/api/2026-04/admin/rotate_service_account_secret
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/service-accounts/{service_account_id}/rotate-secret
Rotate the OAuth `client_secret` for a service account. The previous secret and tokens minted from it are revoked within a few seconds. The new secret is returned only in this response.
Repeating the request may rotate again and invalidate the previous new secret.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_SERVICE_ACCOUNT_ID="f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c"

  curl -X POST "https://api.pinecone.io/admin/service-accounts/$PINECONE_SERVICE_ACCOUNT_ID/rotate-secret" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "service_account": {
      "id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
      "name": "My Service Account",
      "client_id": "l3Ow0CmFyc4jOONcwiKUCRqQKN0tiCAn",
      "created_at": "2026-04-10T15:23:00Z",
      "updated_at": "2026-04-10T15:23:00Z"
    },
    "client_secret": "8p-kkC23XOWvkCosKq-BOn3G74qp__rBcDMxc82iB4gfzRvuhSCRBKM7C5Q7TAzj"
  }
  ```
</ResponseExample>
