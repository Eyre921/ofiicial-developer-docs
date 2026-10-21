---
title: "Delete records"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/delete
path: reference/api/2026-07/data-plane/delete
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/delete
Delete records by id or by metadata from a single namespace.

For guidance and examples, see [Delete data](https://docs.pinecone.io/guides/manage-data/delete-data).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

index.delete(ids=["id-1", "id-2"], namespace="example-namespace")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({
  host: 'INDEX_HOST',
  namespace: 'example-namespace',
});

await index.deleteMany({
  ids: ['id-1', 'id-2'],
});
```

```go Go theme={null}
package main

import (
    "context"
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

    // To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      "INDEX_HOST",
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    err = idxConnection.DeleteVectorsById(ctx, []string{"id-1", "id-2"})
    if err != nil {
        log.Fatalf("Failed to delete vectors: %v", err)
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/vectors/delete" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "ids": [
      "id-1", 
      "id-2"
    ],
    "namespace": "example-namespace"
  }
'
```
