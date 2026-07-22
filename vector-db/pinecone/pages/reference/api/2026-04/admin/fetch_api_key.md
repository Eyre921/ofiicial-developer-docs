---
title: "Get API key details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_api_key
path: reference/api/2026-04/admin/fetch_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/api-keys/{api_key_id}
Get an API key's details, excluding its secret.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_API_KEY_ID="3fa85f64-5717-4562-b3fc-2c963f66afa6"

  curl -X GET "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      -H "accept: application/json" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "roles": [
      "ProjectEditor"
    ]
  }
  ```
</ResponseExample>
