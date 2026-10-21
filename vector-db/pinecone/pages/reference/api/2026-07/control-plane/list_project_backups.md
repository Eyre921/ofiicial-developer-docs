---
title: "List backups for all indexes in a project"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_project_backups
path: reference/api/2026-07/control-plane/list_project_backups
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /backups
List all backups for a project.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

backups = pc.backups.list()
print(backups)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const backups = await pc.backups.list();
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

    backups, err := pc.ListBackups(ctx, nil)
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

curl -X GET "https://api.pinecone.io/backups" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -H "accept: application/json"
```
