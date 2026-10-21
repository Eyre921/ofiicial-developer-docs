---
title: "Delete a backup"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/delete_backup
path: reference/api/2026-07/control-plane/delete_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml delete /backups/{backup_id}
Delete a backup.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

pc.backups.delete(backup_id="9947520e-d5a1-4418-a78d-9f464c9969da")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

await pc.backups.delete('9947520e-d5a1-4418-a78d-9f464c9969da');
```

```go Go theme={null}
package main

import (
    "context"
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

    err = pc.DeleteBackup(ctx, "9947520e-d5a1-4418-a78d-9f464c9969da")
    if err != nil {
        log.Fatalf("Failed to delete backup: %v", err)
    }

    fmt.Println("Backup deleted")
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
BACKUP_ID="9947520e-d5a1-4418-a78d-9f464c9969da"

curl -X DELETE "https://api.pinecone.io/backups/$BACKUP_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
```
