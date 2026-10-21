---
title: "Search with a vector"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/query
path: reference/api/2026-07/data-plane/query
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /query
Search a namespace using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

For guidance, examples, and limits, see [Search](https://docs.pinecone.io/guides/search/search-overview).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

response = index.query(
    namespace="example-namespace",
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    filter={"genre": {"$eq": "documentary"}},
    top_k=3,
    include_values=True,
)
for match in response.matches:
    print(match.id, match.score, match.values)
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

const response = await index.query({
  vector: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  filter: {
    genre: { $eq: 'documentary' },
  },
  topK: 3,
  includeValues: true,
});
for (const match of response.matches) {
  console.log(match.id, match.score, match.values);
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

    filter, err := pinecone.NewMetadataFilter(map[string]interface{}{
        "genre": map[string]interface{}{
            "$eq": "documentary",
        },
    })
    if err != nil {
        log.Fatalf("Failed to create metadata filter: %v", err)
    }

    res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
        Vector:         []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
        TopK:           3,
        MetadataFilter: filter,
        IncludeValues:  true,
    })
    if err != nil {
        log.Fatalf("Failed to query vectors: %v", err)
    }
    for _, match := range res.Matches {
        fmt.Println(match.Vector.Id, match.Score, *match.Vector.Values)
    }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/query" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "namespace": "example-namespace",
    "vector": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    "filter": {"genre": {"$eq": "documentary"}},
    "topK": 3,
    "includeValues": true
  }'
```
