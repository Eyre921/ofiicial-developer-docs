---
title: "Create an index from a backup"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/create_index_from_backup
path: reference/api/2026-04/control-plane/create_index_from_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml post /backups/{backup_id}/create-index
Create an index from a backup. For serverless backups, you can optionally set `read_capacity` so the restored index is created with dedicated read nodes (DRN) instead of defaulting to on-demand capacity.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -H 'Content-Type: application/json' \
    -d '{
          "name": "restored-index",
          "tags": {
            "tag0": "val0",
            "tag1": "val1"
          },
          "deletion_protection": "enabled"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```
</ResponseExample>
