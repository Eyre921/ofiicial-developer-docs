---
title: "Fetch records"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/fetch
path: reference/api/2026-07/data-plane/fetch
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /vectors/fetch
Look up and return records by ID from a single namespace. The returned records include the vector data and/or metadata.

For on-demand indexes, since vector values are retrieved from object storage, fetch operations may have increased latency. If you only need metadata or IDs, consider using the query operation with `includeValues` set to `false` instead.

For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

response = index.fetch(ids=["id-1", "id-2"], namespace="example-namespace")
for vector_id, vector in response.vectors.items():
    print(vector_id, vector.values)
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

const response = await index.fetch({
  ids: ['id-1', 'id-2'],
});
for (const [id, record] of Object.entries(response.records)) {
  console.log(id, record.values);
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

    // To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      "INDEX_HOST",
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    res, err := idxConnection.FetchVectors(ctx, []string{"id-1", "id-2"})
    if err != nil {
        log.Fatalf("Failed to fetch vectors: %v", err)
    }
    for id, vector := range res.Vectors {
        fmt.Println(id, *vector.Values)
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/vectors/fetch?ids=id-1&ids=id-2&namespace=example-namespace" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
