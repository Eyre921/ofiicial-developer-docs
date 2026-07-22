---
title: "List role bindings"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_role_bindings
path: reference/api/2026-04/admin/list_role_bindings
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/role-bindings
List role bindings in the caller's organization, optionally filtered by principal, resource, and role.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/role-bindings?principal_type=user&principal_id=e2e92523-85dc-4142-b8c2-e681be8b78df" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "5a86ed21-daf1-448d-a9ca-f92a0fd839d3",
        "principal_type": "user",
        "principal_id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
        "resource_type": "organization",
        "resource_id": "-ExampleOrgId0000000",
        "role": "OrgMember",
        "created_at": "2026-04-10T15:23:00Z"
      }
    ],
    "pagination": {
      "next": "eyJsYXN0X2lkIjoiNWE4NmVkMjEifQ=="
    }
  }
  ```
</ResponseExample>
