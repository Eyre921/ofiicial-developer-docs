---
title: "List namespaces"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/listnamespaces
path: reference/api/2026-07/data-plane/listnamespaces
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /namespaces
List all namespaces in a serverless index.

Up to 100 namespaces are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of namespaces are returned instead. Whenever there are additional namespaces to return, the response includes `pagination.next`, a token you pass as `paginationToken` to get the next batch of namespaces. When the response has no `pagination`, there are no more namespaces to return.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

for page in index.list_namespaces():
    for namespace in page.namespaces:
        print(namespace.name, namespace.record_count)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

let paginationToken;
do {
  const page = await index.listNamespaces({ paginationToken });
  for (const namespace of page.namespaces ?? []) {
    console.log(namespace.name, namespace.recordCount);
  }
  paginationToken = page.pagination?.next;
} while (paginationToken);
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    var paginationToken *string
    for {
        res, err := idxConnection.ListNamespaces(ctx, &pinecone.ListNamespacesParams{
            PaginationToken: paginationToken,
        })
        if err != nil {
            log.Fatalf("Failed to list namespaces: %v", err)
        }
        for _, namespace := range res.Namespaces {
            fmt.Println(namespace.Name, namespace.RecordCount)
        }
        if res.Pagination == nil || res.Pagination.Next == "" {
            break
        }
        paginationToken = &res.Pagination.Next
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
```
