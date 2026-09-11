---
title: "Create an index from a backup"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup
path: reference/api/2026-07/control-plane/create_index_from_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /backups/{backup_id}/create-index
Create an index from a backup.
The restored index inherits the schema of the index the backup was taken from, including its full-text search fields and its integrated embedding configuration, and the request cannot override it. A backup that carries no `schema` restores an index whose fields are derived from the source index's dimension, metric, and vector type, and reported under the reserved `_values` / `_sparse_values` names.
For serverless backups, you can optionally set `read_capacity` so the restored index is created with dedicated read nodes (DRN) instead of defaulting to on-demand capacity.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
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
