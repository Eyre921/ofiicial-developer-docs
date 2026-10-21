---
title: "Cancel an import"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/cancel_import
path: reference/api/2026-07/data-plane/cancel_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml delete /bulk/imports/{id}
Cancel an import operation if it is not yet finished. It has no effect if the operation is already finished.

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

index.cancel_import("101")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

await index.cancelImport('101');
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    err = idxConnection.CancelImport(ctx, "101")
    if err != nil {
        log.Fatalf("Failed to cancel import: %v", err)
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X DELETE "https://$INDEX_HOST/bulk/imports/101" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
