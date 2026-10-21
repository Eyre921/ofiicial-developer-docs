---
title: "List indexes"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_indexes
path: reference/api/2026-07/control-plane/list_indexes
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /indexes
List all indexes in a project.

Returns all indexes in the project, including their current status and configuration. Each item in the response has the same shape as the response from [Describe an index](/reference/api/2026-07/control-plane/describe_index).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

for index_model in pc.indexes.list():
    print(index_model.name, index_model.host, index_model.status.state)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const { indexes = [] } = await pc.indexes.list();
for (const indexModel of indexes) {
  console.log(indexModel.name, indexModel.host, indexModel.status.state);
}
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

    idxs, err := pc.ListIndexes(ctx)
    if err != nil {
        log.Fatalf("Failed to list indexes: %v", err)
    }
    for _, idx := range idxs {
        fmt.Println(idx.Name, idx.Host, idx.Status.State)
    }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
