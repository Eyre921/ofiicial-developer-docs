---
title: "Fetch records by metadata"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/fetch_by_metadata
path: reference/api/2026-07/data-plane/fetch_by_metadata
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/fetch_by_metadata
Look up and return records by metadata from a single namespace. The returned records include the vector data and metadata.

For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

response = index.fetch_by_metadata(
    namespace="__default__",
    filter={"genre": {"$eq": "Action/Adventure"}},
    limit=2,
)
for vector_id, vector in response.vectors.items():
    print(vector_id, vector.metadata)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({
  host: 'INDEX_HOST',
  namespace: '__default__',
});

const response = await index.fetchByMetadata({
  filter: {
    genre: { $eq: 'Action/Adventure' },
  },
  limit: 2,
});
for (const [id, record] of Object.entries(response.records)) {
  console.log(id, record.metadata);
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
        Namespace: "__default__",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    filter, err := pinecone.NewMetadataFilter(map[string]interface{}{
        "genre": map[string]interface{}{
            "$eq": "Action/Adventure",
        },
    })
    if err != nil {
        log.Fatalf("Failed to create metadata filter: %v", err)
    }

    limit := uint32(2)
    res, err := idxConnection.FetchVectorsByMetadata(ctx, &pinecone.FetchVectorsByMetadataRequest{
        Filter: filter,
        Limit:  &limit,
    })
    if err != nil {
        log.Fatalf("Failed to fetch vectors by metadata: %v", err)
    }
    for id, vector := range res.Vectors {
        fmt.Println(id, vector.Metadata.AsMap())
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "namespace": "__default__",
    "filter": {"genre": {"$eq": "Action/Adventure"}},
    "limit": 2
  }'
```
