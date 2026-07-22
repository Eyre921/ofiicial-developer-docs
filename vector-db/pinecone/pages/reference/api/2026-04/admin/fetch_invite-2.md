---
title: "Get invite details"
source: https://docs.pinecone.io/reference/api/2026-04/admin/fetch_invite
path: reference/api/2026-04/admin/fetch_invite
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml get /admin/invites/{invite_id}
Get an invite in the caller's organization by ID.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_INVITE_ID="9c8e3528-b9c0-4358-84ce-84c28e91b566"

  curl -X GET "https://api.pinecone.io/admin/invites/$PINECONE_INVITE_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-H "accept: application/json" \
  	-H "X-Pinecone-Api-Version: 2026-04"
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
