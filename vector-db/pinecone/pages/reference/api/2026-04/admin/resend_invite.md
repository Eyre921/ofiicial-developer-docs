---
title: "Resend an invite email"
source: https://docs.pinecone.io/reference/api/2026-04/admin/resend_invite
path: reference/api/2026-04/admin/resend_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml post /admin/invites/{invite_id}/resend
Resend the invite email and extend `expires_at` by 7 days.
Resending an expired invite is allowed: it extends `expires_at` by 7 days from now, returning the invite to `pending`.
Resending an already-accepted (processed) invite returns `409` (see shared conflict response).
Limited to 100 invite emails per hour per organization. Returns `429` when exceeded.
Repeat requests may send another email and extend expiry again.
Role bindings are not included. Use `GET /admin/role-bindings` with `principal_type` and `principal_id` to list them.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="9c8e3528-b9c0-4358-84ce-84c28e91b566"

  curl -X POST "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID/resend" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9c8e3528-b9c0-4358-84ce-84c28e91b566",
    "email": "newhire@acme.com",
    "status": "pending",
    "expires_at": "2026-05-28T20:14:00Z",
    "processed_at": null,
    "created_at": "2026-04-14T20:00:00Z"
  }
  ```
</ResponseExample>
