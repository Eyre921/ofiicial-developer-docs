---
title: "List collections"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_collections
path: reference/api/2026-07/control-plane/list_collections
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /collections
List all collections in a project.

Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

for collection in pc.collections.list():
    print(collection.name, collection.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const { collections = [] } = await pc.collections.list();
for (const collection of collections) {
  console.log(collection.name, collection.status);
}
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

    collections, err := pc.ListCollections(ctx)
    if err != nil {
        log.Fatalf("Failed to list collections: %v", err)
    }
    for _, collection := range collections {
        fmt.Println(collection.Name, collection.Status)
    }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/collections" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
