---
title: "Update a project"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/update_project
path: reference/api/2026-04/admin-assistant/update_project
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml patch /admin/projects/{project_id}
Update a project's name, maximum number of Pods, or customer-managed encryption key (CMEK).


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="YOUR_PROJECT_ID"

  curl -X PATCH "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
      "name": "updated-example-project"
      }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "updated-example-project",
    "max_pods": 0,
    "force_encryption_with_cmek": false,
    "organization_id": "string",
    "created_at": "2025-03-17T00:42:31.912Z"
  }
  ```
</ResponseExample>
