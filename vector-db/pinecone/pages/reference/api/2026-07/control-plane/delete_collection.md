---
title: "Delete a collection"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/delete_collection
path: reference/api/2026-07/control-plane/delete_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml delete /collections/{collection_name}
Delete an existing collection.

Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

pc.collections.delete(name="example-collection")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

await pc.collections.delete('example-collection');
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

    err = pc.DeleteCollection(ctx, "example-collection")
    if err != nil {
        log.Fatalf("Failed to delete collection: %v", err)
    }
    fmt.Println("Deleted collection example-collection")
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X DELETE "https://api.pinecone.io/collections/example-collection" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
