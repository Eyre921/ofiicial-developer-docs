---
title: "Describe a backup"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_backup
path: reference/api/2026-07/control-plane/describe_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /backups/{backup_id}
Get a description of a backup.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="8c85e612-ed1c-4f97-9f8c-8194e07bcf71"

  curl -X GET "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -H "accept: application/json"
  ```
</RequestExample>
