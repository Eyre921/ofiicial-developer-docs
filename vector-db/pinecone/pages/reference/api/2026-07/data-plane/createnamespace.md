---
title: "Create a namespace"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/createnamespace
path: reference/api/2026-07/data-plane/createnamespace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces
Create a namespace in a serverless index.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

namespace = index.create_namespace(
    name="example-namespace",
    schema={
        "fields": {
            "document_id": {"filterable": True},
            "document_title": {"filterable": True},
            "chunk_number": {"filterable": True},
            "document_url": {"filterable": True},
            "created_at": {"filterable": True},
        }
    },
)
print(namespace)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

const namespace = await index.createNamespace({
  name: 'example-namespace',
  schema: {
    fields: {
      document_id: { filterable: true },
      document_title: { filterable: true },
      chunk_number: { filterable: true },
      document_url: { filterable: true },
      created_at: { filterable: true },
    },
  },
});
console.log(namespace);
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

    namespace, err := idxConnection.CreateNamespace(ctx, &pinecone.CreateNamespaceParams{
        Name: "example-namespace",
        Schema: &pinecone.MetadataSchema{
            Fields: map[string]pinecone.MetadataSchemaField{
                "document_id":    {Filterable: true},
                "document_title": {Filterable: true},
                "chunk_number":   {Filterable: true},
                "document_url":   {Filterable: true},
                "created_at":     {Filterable: true},
            },
        },
    })
    if err != nil {
        log.Fatalf("Failed to create namespace: %v", err)
    }
    fmt.Println(namespace.Name, namespace.RecordCount)
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "name": "example-namespace",
        "schema": {
		  "fields": { 
            "document_id": {"filterable": true},
            "document_title": {"filterable": true},
            "chunk_number": {"filterable": true},
            "document_url": {"filterable": true},
            "created_at": {"filterable": true}
          }
        }
      }'
```
