---
title: "Describe a collection"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_collection
path: reference/api/2026-07/control-plane/describe_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /collections/{collection_name}
Get a description of a collection.

Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

collection = pc.collections.describe(name="example-collection")
print(collection.name, collection.status, collection.dimension, collection.vector_count)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const collection = await pc.collections.describe('example-collection');
console.log(collection.name, collection.status, collection.dimension, collection.vectorCount);
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

    collection, err := pc.DescribeCollection(ctx, "example-collection")
    if err != nil {
        log.Fatalf("Failed to describe collection: %v", err)
    }
    fmt.Println(collection.Name, collection.Status, collection.Dimension, collection.VectorCount)
}
```

```hcl Terraform theme={null}
# Requires Terraform provider v5.0.0 or later
data "pinecone_collection" "example_collection" {
  name = "example-collection"
}

output "example_collection" {
  value = {
    status       = data.pinecone_collection.example_collection.status
    dimension    = data.pinecone_collection.example_collection.dimension
    vector_count = data.pinecone_collection.example_collection.vector_count
  }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/collections/example-collection" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
```
