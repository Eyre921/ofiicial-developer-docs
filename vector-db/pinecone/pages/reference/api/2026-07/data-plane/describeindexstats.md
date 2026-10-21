---
title: "Get index stats"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/describeindexstats
path: reference/api/2026-07/data-plane/describeindexstats
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /describe_index_stats
Return statistics about the contents of an index, including the vector count per namespace, the number of dimensions, and the index fullness.

Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.

> [!NOTE]
>
> Index fullness is also relevant for [dedicated read nodes](/guides/index-data/dedicated-read-nodes/concepts#index-fullness). The response includes `memoryFullness` and `storageFullness` alongside `indexFullness`, which summarizes overall capacity usage. For serverless on-demand indexes, all three values are typically `0` because storage and compute scale automatically. For dedicated indexes, these values indicate when the index needs more capacity. See [Scale your index](/guides/index-data/dedicated-read-nodes/scale).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

stats = index.describe_index_stats()
print(stats.total_vector_count)
for name, summary in stats.namespaces.items():
    print(name, summary.vector_count)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

const stats = await index.describeIndexStats();
console.log(stats.totalRecordCount);
for (const [name, summary] of Object.entries(stats.namespaces ?? {})) {
  console.log(name, summary.recordCount);
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
        Host: "INDEX_HOST",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    stats, err := idxConnection.DescribeIndexStats(ctx)
    if err != nil {
        log.Fatalf("Failed to describe index stats: %v", err)
    }
    fmt.Println(stats.TotalVectorCount)
    for name, summary := range stats.Namespaces {
        fmt.Println(name, summary.VectorCount)
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="YOUR_INDEX_HOST"

curl -X POST "https://$INDEX_HOST/describe_index_stats" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
