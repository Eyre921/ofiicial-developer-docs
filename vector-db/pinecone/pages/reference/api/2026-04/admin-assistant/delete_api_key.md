---
title: "Delete an API key"
source: https://docs.pinecone.io/reference/api/2026-04/admin-assistant/delete_api_key
path: reference/api/2026-04/admin-assistant/delete_api_key
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/admin_2026-04.oas.yaml delete /admin/api-keys/{api_key_id}
Delete an API key from a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_API_KEY_ID="YOUR_KEY_ID"

  curl -X DELETE "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
  	-H "X-Pinecone-Api-Version: 2026-04" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```
</RequestExample>
