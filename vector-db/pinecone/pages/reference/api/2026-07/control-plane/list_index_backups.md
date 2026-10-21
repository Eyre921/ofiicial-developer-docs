---
title: "List backups for an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_index_backups
path: reference/api/2026-07/control-plane/list_index_backups
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /indexes/{index_name}/backups
When `include_deleted` is false (or omitted), `index_name` must resolve to an active index in the project. If no active index by that name exists—including the case where only deleted indexes have used the name—the API returns **404**, not an empty list.

When `include_deleted` is true, the API returns backups from every index in the project that has ever used this name (active and deleted). The `source_index_deleted_at` field is present only when the backup is from a deleted index. **404** is returned only when no index by that name has ever existed in the project (active or deleted).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

backups = pc.backups.list(index_name="docs-example")
print(backups)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const backups = await pc.backups.listByIndex('docs-example');
console.log(backups);
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

    indexName := "docs-example"

    backups, err := pc.ListBackups(ctx, &pinecone.ListBackupsParams{
        IndexName: &indexName,
    })
    if err != nil {
        log.Fatalf("Failed to list backups: %v", err)
    }

    out, err := json.MarshalIndent(backups, "", "  ")
    if err != nil {
        log.Fatalf("Failed to marshal response: %v", err)
    }
    fmt.Println(string(out))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_NAME="docs-example"

curl -X GET "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -H "accept: application/json"
```
