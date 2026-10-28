---
title: "Create a collection"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_collection
path: reference/api/2026-07/control-plane/create_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /collections
Create a Pinecone collection.

Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

collection = pc.collections.create(name="example-collection", source="docs-example")
print(collection.name, collection.status)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const collection = await pc.collections.create({
  name: 'example-collection',
  source: 'docs-example',
});
console.log(collection.name, collection.status);
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

    collection, err := pc.CreateCollection(ctx, &pinecone.CreateCollectionRequest{
        Name:   "example-collection",
        Source: "docs-example",
    })
    if err != nil {
        log.Fatalf("Failed to create collection: %v", err)
    }
    fmt.Println(collection.Name, collection.Status)
}
```

```hcl Terraform theme={null}
# Requires Terraform provider v5.0.0 or later
# The source must be an existing pod-based index
resource "pinecone_collection" "example_collection" {
  name   = "example-collection"
  source = "docs-example"
}

output "example_collection_status" {
  value = pinecone_collection.example_collection.status
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -s "https://api.pinecone.io/collections" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "name": "example-collection",
        "source": "docs-example"
  }'
```
