---
title: "List users in the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_users
path: reference/api/2026-04/admin/list_users
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/users
List users who are members of the caller's organization. Results are paginated.
Optional filters:
- `email` — case-insensitive match on the user's email address.
Pagination tokens apply to the full query, including `email`. See query parameters for cursor rules.
Role bindings are not included. Use `GET /admin/role-bindings` with `principal_type` and `principal_id` to list them.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/users" \
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
        "id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
        "email": "alice@example.com",
        "name": "Alice Example",
        "created_at": "2026-04-10T15:23:00Z",
        "updated_at": "2026-04-12T09:11:00Z"
      }
    ],
    "pagination": {
      "next": "eyJsYXN0X2lkIjoiZTJlOTI1MjMifQ=="
    }
  }
  ```
</ResponseExample>
