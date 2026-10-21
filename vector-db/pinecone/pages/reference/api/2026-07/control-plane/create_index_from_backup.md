---
title: "Create an index from a backup"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup
path: reference/api/2026-07/control-plane/create_index_from_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /backups/{backup_id}/create-index
Create an index from a backup.

The restored index inherits the schema of the index the backup was taken from, including its full-text search fields and its embedding configuration (`embed` / `sparse_embed` fields, or the `semantic_text` field of a legacy integrated index created via create-for-model), and the request cannot override it. A backup that carries no `schema` restores an index whose fields are derived from the source index's dimension, metric, and vector type, and reported under the reserved `_values` / `_sparse_values` names.

For serverless backups, you can optionally set `read_capacity` so the restored index is created with dedicated read nodes (DRN) instead of defaulting to on-demand capacity.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

response = pc.create_index_from_backup(
    backup_id="a65ff585-d987-4da5-a622-72e19a6ed5f4",
    name="restored-index",
    tags={
        "tag0": "val0",
        "tag1": "val1",
    },
    deletion_protection="enabled",
    timeout=-1,  # Return the restore job ID without waiting for the index
)
print(response)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const response = await pc.backups.createIndex(
  'a65ff585-d987-4da5-a622-72e19a6ed5f4',
  {
    name: 'restored-index',
    tags: {
      tag0: 'val0',
      tag1: 'val1',
    },
    deletionProtection: 'enabled',
  },
);
console.log(response);
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "os"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: os.Getenv("PINECONE_API_KEY"),
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    deletionProtection := pinecone.DeletionProtectionEnabled
    tags := pinecone.IndexTags{
        "tag0": "val0",
        "tag1": "val1",
    }

    response, err := pc.CreateIndexFromBackup(ctx, &pinecone.CreateIndexFromBackupParams{
        BackupId:           "a65ff585-d987-4da5-a622-72e19a6ed5f4",
        Name:               "restored-index",
        Tags:               &tags,
        DeletionProtection: &deletionProtection,
    })
    if err != nil {
        log.Fatalf("Failed to create index from backup: %v", err)
    }

    out, err := json.MarshalIndent(response, "", "  ")
    if err != nil {
        log.Fatalf("Failed to marshal response: %v", err)
    }
    fmt.Println(string(out))
}
```

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
