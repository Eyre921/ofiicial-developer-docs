---
title: "Describe a backup"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_backup
path: reference/api/2026-07/control-plane/describe_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /backups/{backup_id}
Get a description of a backup.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

backup = pc.backups.describe(backup_id="8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
print(backup)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const backup = await pc.backups.describe('8c85e612-ed1c-4f97-9f8c-8194e07bcf71');
console.log(backup);
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

    backup, err := pc.DescribeBackup(ctx, "8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
    if err != nil {
        log.Fatalf("Failed to describe backup: %v", err)
    }

    out, err := json.MarshalIndent(backup, "", "  ")
    if err != nil {
        log.Fatalf("Failed to marshal response: %v", err)
    }
    fmt.Println(string(out))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
BACKUP_ID="8c85e612-ed1c-4f97-9f8c-8194e07bcf71"

curl -X GET "https://api.pinecone.io/backups/$BACKUP_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -H "accept: application/json"
```
