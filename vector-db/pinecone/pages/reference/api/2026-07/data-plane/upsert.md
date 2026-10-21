---
title: "Upsert records"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/upsert
path: reference/api/2026-07/data-plane/upsert
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/upsert
Upsert records into a namespace. If a new value is upserted for an existing record ID, it will overwrite the previous value.

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

> [!TIP]
>
> To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

response = index.upsert(
    vectors=[
        {
            "id": "vec1",
            "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            "metadata": {"genre": "comedy", "year": 2020},
        },
        {
            "id": "vec2",
            "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            "metadata": {"genre": "documentary", "year": 2019},
        },
    ],
    namespace="example-namespace",
)
print(response.upserted_count)
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

await index.upsert({
  records: [
    {
      id: 'vec1',
      values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
      metadata: { genre: 'comedy', year: 2020 },
    },
    {
      id: 'vec2',
      values: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
      metadata: { genre: 'documentary', year: 2019 },
    },
  ],
});
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

    metadata1, err := pinecone.NewMetadata(map[string]interface{}{
        "genre": "comedy",
        "year":  2020,
    })
    if err != nil {
        log.Fatalf("Failed to create metadata: %v", err)
    }

    metadata2, err := pinecone.NewMetadata(map[string]interface{}{
        "genre": "documentary",
        "year":  2019,
    })
    if err != nil {
        log.Fatalf("Failed to create metadata: %v", err)
    }

    vectors := []*pinecone.Vector{
        {
            Id:       "vec1",
            Values:   &[]float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
            Metadata: metadata1,
        },
        {
            Id:       "vec2",
            Values:   &[]float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
            Metadata: metadata2,
        },
    }

    count, err := idxConnection.UpsertVectors(ctx, vectors)
    if err != nil {
        log.Fatalf("Failed to upsert vectors: %v", err)
    }
    fmt.Printf("Upserted %d vectors\n", count)
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/vectors/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "vectors": [
      {
        "id": "vec1",
        "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        "metadata": {"genre": "comedy", "year": 2020}
      },
      {
        "id": "vec2",
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        "metadata": {"genre": "documentary", "year": 2019}
      }
    ],
    "namespace": "example-namespace"
  }'
```
