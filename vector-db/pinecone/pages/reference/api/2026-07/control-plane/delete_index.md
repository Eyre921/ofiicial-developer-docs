---
title: "Delete an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/delete_index
path: reference/api/2026-07/control-plane/delete_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml delete /indexes/{index_name}
Delete an existing index.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

pc.indexes.delete(name="docs-example")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

await pc.indexes.delete('docs-example');
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

    err = pc.DeleteIndex(ctx, "docs-example")
    if err != nil {
        log.Fatalf("Failed to delete index: %v", err)
    }
    fmt.Println("Deleted index docs-example")
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X DELETE "https://api.pinecone.io/indexes/docs-example" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
