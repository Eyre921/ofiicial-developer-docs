---
title: "List projects"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/list_projects
path: reference/api/2026-04/admin-assistant/list_projects
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/projects
List all projects in an organization.

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
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "example-project",
        "max_pods": 0,
        "force_encryption_with_cmek": true,
        "organization_id": "<string>",
        "created_at": "2023-11-07T05:31:56Z"
      }
    ]
  }
  ```
</ResponseExample>
