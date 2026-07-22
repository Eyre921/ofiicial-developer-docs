---
title: "Delete a role binding"
source: https://docs.pinecone.io/reference/api/2026-04/admin/delete_role_binding
path: reference/api/2026-04/admin/delete_role_binding
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/role-bindings/{role_binding_id}
Delete a role binding; permissions are revoked when the deletion completes.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_ROLE_BINDING_ID="YOUR_ROLE_BINDING_ID"

  curl -X DELETE "https://api.pinecone.io/admin/role-bindings/$PINECONE_ROLE_BINDING_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
