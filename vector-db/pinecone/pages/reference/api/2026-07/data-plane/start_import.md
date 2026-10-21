---
title: "Start import"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/start_import
path: reference/api/2026-07/data-plane/start_import
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /bulk/imports
Start an asynchronous import of vectors from object storage into an index.

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

response = index.start_import(
    uri="s3://BUCKET_NAME/PATH/TO/DIR",
    error_mode="continue",
    integration_id="a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
)
print(response.id)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();
// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

const response = await index.startImport({
  uri: 's3://BUCKET_NAME/PATH/TO/DIR',
  errorMode: 'continue',
  integration: 'a12b3d4c-47d2-492c-a97a-dd98c8dbefde',
});
console.log(response.id);
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

    integrationId := "a12b3d4c-47d2-492c-a97a-dd98c8dbefde"
    errorMode := string(pinecone.ImportErrorModeContinue)
    res, err := idxConnection.StartImport(ctx, "s3://BUCKET_NAME/PATH/TO/DIR", &integrationId, &errorMode)
    if err != nil {
        log.Fatalf("Failed to start import: %v", err)
    }
    fmt.Println(res.Id)
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/bulk/imports" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H 'X-Pinecone-Api-Version: 2026-07' \
  -d '{
        "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
        "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
        "errorMode": {
            "onError": "continue"
            }
        }'
```
