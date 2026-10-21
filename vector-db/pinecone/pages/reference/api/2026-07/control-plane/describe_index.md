---
title: "Describe an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_index
path: reference/api/2026-07/control-plane/describe_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /indexes/{index_name}
Get a description of an index.

Returns detailed information about a specific index, including its schema, status, host URL, and read capacity. Poll this endpoint after calling [Create an index](/reference/api/2026-07/control-plane/create_index) until `status.ready: true` (and, for `Dedicated` read capacity, `read_capacity.status.state: "Ready"`) before performing data plane operations.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

index_model = pc.indexes.describe(name="articles")
print(index_model.status, index_model.schema)

host = index_model.host
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const indexModel = await pc.indexes.describe('articles');
console.log(indexModel.status, indexModel.schema);

const host = indexModel.host;
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
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

    idx, err := pc.DescribeIndex(ctx, "articles")
    if err != nil {
        log.Fatalf("Failed to describe index: %v", err)
    }
    schema, err := json.Marshal(idx.Schema)
    if err != nil {
        log.Fatalf("Failed to marshal schema: %v", err)
    }
    fmt.Println(idx.Status.State, string(schema))

    host := idx.Host
    fmt.Println(host)
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
curl "https://api.pinecone.io/indexes/articles" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
