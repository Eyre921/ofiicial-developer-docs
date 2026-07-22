---
title: "Remove a user from the organization"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_user
path: reference/api/2026-04/admin/delete_user
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/users/{user_id}
Remove a user from the organization and revoke their role bindings; their Pinecone account is not deleted.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_USER_ID="YOUR_USER_ID"

  curl -X DELETE "https://api.pinecone.io/admin/users/$PINECONE_USER_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
