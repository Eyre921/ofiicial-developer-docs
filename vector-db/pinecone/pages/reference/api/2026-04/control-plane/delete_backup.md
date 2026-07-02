---
title: "Delete a backup"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/delete_backup
path: reference/api/2026-04/control-plane/delete_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml delete /backups/{backup_id}
Delete a backup.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="9947520e-d5a1-4418-a78d-9f464c9969da"

  curl -X DELETE "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample />
