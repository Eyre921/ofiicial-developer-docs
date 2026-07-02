---
title: "List API keys"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/list_api_keys
path: reference/api/2026-04/admin-assistant/list_api_keys
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/projects/{project_id}/api-keys
List all API keys in a project.

<RequestExample>
  ```bash curl theme={null}
  curl -X GET "https://api.pinecone.io/admin/projects" \
      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "roles": [
          "ProjectEditor"
        ]
      }
    ]
  }
  ```
</ResponseExample>
