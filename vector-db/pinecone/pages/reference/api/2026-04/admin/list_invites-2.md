---
title: "List invites"
source: https://docs.pinecone.io/reference/api/2026-04/admin/list_invites
path: reference/api/2026-04/admin/list_invites
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/invites
List invites in the caller's organization. Results are paginated. Returns pending and expired invites (processed and deleted invites are excluded); use `status` to distinguish pending from expired. See query parameters for cursor rules.
Role bindings are not included. Use `GET /admin/role-bindings` with `principal_type` and `principal_id` to list them.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/invites" \
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
        "id": "9c8e3528-b9c0-4358-84ce-84c28e91b566",
        "email": "newhire@acme.com",
        "status": "pending",
        "expires_at": "2026-05-21T03:00:00Z",
        "processed_at": null,
        "created_at": "2026-04-14T20:00:00Z"
      }
    ],
    "pagination": {
      "next": "eyJsYXN0X2lkIjoiOWM4ZTM1MjgifQ=="
    }
  }
  ```
</ResponseExample>
