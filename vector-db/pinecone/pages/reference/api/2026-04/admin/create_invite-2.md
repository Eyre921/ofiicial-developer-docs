---
title: "Invite a user to the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_invite
path: reference/api/2026-04/admin/create_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/invites
Invite a user to the organization by email and grant their initial role bindings.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/invites" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
    -d '{
      "email": "newhire@acme.com",
      "role_bindings": [
        {
          "resource_type": "organization",
          "role": "OrgMember"
        },
        {
          "resource_type": "project",
          "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
          "role": "ProjectMember"
        }
      ]
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9c8e3528-b9c0-4358-84ce-84c28e91b566",
    "email": "newhire@acme.com",
    "status": "pending",
    "expires_at": "2026-05-21T03:00:00Z",
    "processed_at": null,
    "created_at": "2026-04-14T20:00:00Z"
  }
  ```
</ResponseExample>
