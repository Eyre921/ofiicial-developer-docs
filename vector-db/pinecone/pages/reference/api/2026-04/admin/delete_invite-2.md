---
title: "Delete an invite"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_invite
path: reference/api/2026-04/admin/delete_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/invites/{invite_id}
Delete a pending or expired invite and its role bindings, revoking the acceptance link. Returns `202`; the invite is then no longer returned by get requests (returns `404`).
Deleting an already-accepted (processed) invite returns `409`; the underlying user is unaffected. To remove an accepted user, use `DELETE /admin/users/{user_id}` instead. Deleting an invite that does not exist in your organization returns `404`.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="YOUR_INVITE_ID"

  curl -X DELETE "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
