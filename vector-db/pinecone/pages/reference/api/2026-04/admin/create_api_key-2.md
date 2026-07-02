---
title: "Create an API key"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_api_key
path: reference/api/2026-04/admin/create_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/projects/{project_id}/api-keys
Create a new API key for a project. Developers can use the API key to authenticate requests to Pinecone's Data Plane and Control Plane APIs.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_PROJECT_ID="YOUR_PROJECT_ID"

  curl "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"name": "Example API Key",
  		"roles": ["ProjectEditor"]
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Example API key",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "roles": [
        "ProjectEditor"
      ]
    },
    "value": "string"
  }
  ```
</ResponseExample>
