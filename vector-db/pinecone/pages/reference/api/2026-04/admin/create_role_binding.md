---
title: "Create a role binding"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_role_binding
path: reference/api/2026-04/admin/create_role_binding
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/role-bindings
Grant a role to a principal at an organization or project scope.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/role-bindings" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
  		"principal_type": "service_account",
  		"principal_id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
  		"resource_type": "project",
  		"resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
  		"role": "DataPlaneEditor"
  	}'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9a8e3528-b9c0-4358-84ce-84c28e91b566",
    "principal_type": "service_account",
    "principal_id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "DataPlaneEditor",
    "created_at": "2026-04-10T15:23:00Z"
  }
  ```
</ResponseExample>
