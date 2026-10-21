---
title: "Update a record"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/update
path: reference/api/2026-07/data-plane/update
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/update
Update records in a namespace, either by ID or with a metadata filter. By ID, you can change a single record's vector values, its metadata, or both. A filter updates metadata only, and applies to every record that matches.

If a vector value is included, it will overwrite the previous value. If `set_metadata` is included, only the specified metadata fields are modified, and if a specified metadata field does not exist, it is added.

For guidance and examples, see [Update data](https://docs.pinecone.io/guides/manage-data/update-data).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

index.update(
    id="id-3",
    values=[4.0, 2.0],
    set_metadata={"type": "comedy"},
    namespace="example-namespace",
)
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

await index.update({
  id: 'id-3',
  values: [4.0, 2.0],
  metadata: { type: 'comedy' },
});
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      "INDEX_HOST",
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    metadata, err := pinecone.NewMetadata(map[string]interface{}{
        "type": "comedy",
    })
    if err != nil {
        log.Fatalf("Failed to create metadata: %v", err)
    }

    err = idxConnection.UpdateVector(ctx, &pinecone.UpdateVectorRequest{
        Id:       "id-3",
        Values:   []float32{4.0, 2.0},
        Metadata: metadata,
    })
    if err != nil {
        log.Fatalf("Failed to update vector: %v", err)
    }
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/vectors/update" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "id": "id-3",
        "values": [4.0, 2.0],
        "setMetadata": {"type": "comedy"},
        "namespace": "example-namespace"
      }'
```
