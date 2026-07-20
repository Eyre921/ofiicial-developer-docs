---
title: "Invite a user to the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/create_invite
path: reference/api/2026-04/admin/create_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/invites
Invite a user to join the organization. Sends an email with an acceptance link.
Grant roles with `role_bindings`. Include at least one `organization`-scoped binding that grants organization membership (`OrgOwner`, `OrgManager`, `OrgBillingAdmin`, or `OrgMember`; omit `resource_id`); add `project`-scoped bindings (with a `resource_id`) to grant project roles. Bindings are not returned in the response.
If a pending or expired invite already exists for the email, returns `409` with the existing invite's ID in the error message. Use `POST /admin/invites/{invite_id}/resend` to resend the email, and the role-bindings endpoints to change the invite's bindings.
If the email already belongs to a member of the organization, returns `409` (see shared conflict response). Manage that user's roles with the role-bindings endpoints instead.
An invite's bindings are first-class role bindings: they appear in `GET /admin/role-bindings` with `principal_type=invite` and `principal_id` equal to the invite ID, and can be added or removed with the role-bindings endpoints.


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
