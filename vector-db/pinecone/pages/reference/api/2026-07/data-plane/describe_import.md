---
title: "Describe an import"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/describe_import
path: reference/api/2026-07/data-plane/describe_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /bulk/imports/{id}
Return details of a specific import operation.

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

import_op = index.describe_import("101")
print(import_op.status, import_op.percent_complete, import_op.records_imported)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

const importOp = await index.describeImport('101');
console.log(importOp.status, importOp.percentComplete, importOp.recordsImported);
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

    importOp, err := idxConnection.DescribeImport(ctx, "101")
    if err != nil {
        log.Fatalf("Failed to describe import: %v", err)
    }
    fmt.Println(importOp.Status, importOp.PercentComplete, importOp.RecordsImported)
}
```

```bash curl theme={null}
# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X GET "https://$INDEX_HOST/bulk/imports/101" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'X-Pinecone-Api-Version: 2026-07'
```
