---
title: "List imports"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/list_imports
path: reference/api/2026-07/data-plane/list_imports
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /bulk/imports
List all recent and ongoing import operations.

By default, `list_imports` returns up to 100 imports per page. If the `limit` parameter is set, `list` returns up to that number of imports instead. Whenever there are additional IDs to return, the response includes `pagination.next`, a token you pass as `paginationToken` to get the next batch of imports. When the response has no `pagination`, there are no more imports to return.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

> [!NOTE]
>
> This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

for import_op in index.list_imports(limit=10):
    print(import_op.id, import_op.status)
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
  const page = await index.listImports(10, paginationToken);
  for (const importOp of page.data ?? []) {
    console.log(importOp.id, importOp.status);
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

    limit := int32(10)
    var paginationToken *string
    for {
        res, err := idxConnection.ListImports(ctx, &pinecone.ListImportsRequest{
            Limit:           &limit,
            PaginationToken: paginationToken,
        })
        if err != nil {
            log.Fatalf("Failed to list imports: %v", err)
        }
        for _, importOp := range res.Imports {
            fmt.Println(importOp.Id, importOp.Status)
        }
        if res.NextPaginationToken == nil {
            break
        }
        paginationToken = res.NextPaginationToken
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken=Tm90aGluZyB0byBzZWUgaGVyZQo" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'X-Pinecone-Api-Version: 2026-07'
```
