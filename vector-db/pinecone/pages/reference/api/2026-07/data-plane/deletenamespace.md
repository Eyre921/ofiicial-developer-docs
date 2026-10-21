---
title: "Delete a namespace"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/deletenamespace
path: reference/api/2026-07/data-plane/deletenamespace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml delete /namespaces/{namespace}
Delete a namespace from a serverless index. Deleting a namespace is irreversible; all data in the namespace is permanently deleted.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

index.delete_namespace(name="example-namespace")
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

await index.deleteNamespace('example-namespace');
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

    err = idxConnection.DeleteNamespace(ctx, "example-namespace")
    if err != nil {
        log.Fatalf("Failed to delete namespace: %v", err)
    }
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="YOUR_INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE" # To target the default namespace, use "__default__".

curl -X DELETE "https://$INDEX_HOST/namespaces/$NAMESPACE" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
```
