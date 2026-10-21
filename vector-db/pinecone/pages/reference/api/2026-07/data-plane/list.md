---
title: "List record IDs"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/list
path: reference/api/2026-07/data-plane/list
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /vectors/list
List the IDs of records in a single namespace of a serverless index. An optional prefix can be passed to limit the results to IDs with a common prefix.

Returns up to 100 IDs at a time by default in sorted order (bitwise "C" collation). If the `limit` parameter is set, `list` returns up to that number of IDs instead. Whenever there are additional IDs to return, the response includes `pagination.next`, a token you pass as `paginationToken` to get the next batch of IDs. When the response has no `pagination`, there are no more IDs to return.

For guidance and examples, see [List record IDs](https://docs.pinecone.io/guides/manage-data/list-record-ids).

**Note:** `list` is supported only for serverless indexes.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

for page in index.list(prefix="doc1#", limit=3, namespace="example-namespace"):
    print([item.id for item in page.vectors])
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

let paginationToken;
do {
  const page = await index.listPaginated({
    prefix: 'doc1#',
    limit: 3,
    paginationToken,
  });
  for (const vector of page.vectors ?? []) {
    console.log(vector.id);
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      "INDEX_HOST",
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    prefix := "doc1#"
    limit := uint32(3)
    var paginationToken *string
    for {
        res, err := idxConnection.ListVectors(ctx, &pinecone.ListVectorsRequest{
            Prefix:          &prefix,
            Limit:           &limit,
            PaginationToken: paginationToken,
        })
        if err != nil {
            log.Fatalf("Failed to list vectors: %v", err)
        }
        for _, id := range res.VectorIds {
            fmt.Println(*id)
        }
        if res.NextPaginationToken == nil {
            break
        }
        paginationToken = res.NextPaginationToken
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&prefix=doc1%23&limit=3" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
