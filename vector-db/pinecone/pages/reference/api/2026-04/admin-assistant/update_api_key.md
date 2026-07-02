---
title: "Update an API key"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/update_api_key
path: reference/api/2026-04/admin-assistant/update_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml patch /admin/api-keys/{api_key_id}
Update the name and roles of an API key.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_API_KEY_ID="YOUR_API_KEY_ID"

  curl -X PATCH "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "New API key name",
  		"roles": ["ProjectEditor"]
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "New API key name",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "roles": [
        "ProjectEditor"
      ]
    },
    "value": "string"
  }
  ```
</ResponseExample>
