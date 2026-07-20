---
title: "Get user details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_user
path: reference/api/2026-04/admin/fetch_user
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/users/{user_id}
Get a user by ID. Returns `404` if the user is not in your organization.
Role bindings are not included. Use `GET /admin/role-bindings` with `principal_type` and `principal_id` to list them.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_USER_ID="e2e92523-85dc-4142-b8c2-e681be8b78df"

  curl -X GET "https://api.pinecone.io/admin/users/$PINECONE_USER_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "e2e92523-85dc-4142-b8c2-e681be8b78df",
    "email": "alice@example.com",
    "name": "Alice Example",
    "created_at": "2026-04-10T15:23:00Z",
    "updated_at": "2026-04-12T09:11:00Z"
  }
  ```
</ResponseExample>
