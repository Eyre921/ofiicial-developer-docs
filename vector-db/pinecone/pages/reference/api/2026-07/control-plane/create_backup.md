---
title: "Create a backup of an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_backup
path: reference/api/2026-07/control-plane/create_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes/{index_name}/backups
Create a backup of an index.

The backup records the schema of the index it is taken from and reports it as `schema`. An index created from the backup with [Create index from backup](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup) inherits that schema.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

backup = pc.backups.create(
    index_name="docs-example",
    name="example-backup",
    description="Monthly backup of production index",
)
print(backup)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const backup = await pc.backups.create('docs-example', {
  name: 'example-backup',
  description: 'Monthly backup of production index',
});
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

    backupName := "example-backup"
    backupDesc := "Monthly backup of production index"

    backup, err := pc.CreateBackup(ctx, &pinecone.CreateBackupParams{
        IndexName:   "docs-example",
        Name:        &backupName,
        Description: &backupDesc,
    })
    if err != nil {
        log.Fatalf("Failed to create backup: %v", err)
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
INDEX_NAME="docs-example"

curl "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "example-backup", 
      "description": "Monthly backup of production index"
      }'
```
