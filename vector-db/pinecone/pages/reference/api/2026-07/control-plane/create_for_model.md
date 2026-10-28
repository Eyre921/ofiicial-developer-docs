---
title: "Create a legacy integrated index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_for_model
path: reference/api/2026-07/control-plane/create_for_model
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes/create-for-model
Create a legacy integrated index. Legacy integrated indexes created via create-for-model require the legacy Records API.

For new work, create a document index with [Create an index](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index), declaring `embed` or `sparse_embed` on a `string` field to enable integrated embedding on it, and read and write the index through the Documents API. Document indexes support integrated embedding alongside full-text search on the same field, and scoring with `score_by`.

With this type of index, you provide source text, and Pinecone uses a [hosted embedding model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to convert the text automatically during [upsert](https://docs.pinecone.io/reference/api/2026-07/data-plane/upsert_records) and [search](https://docs.pinecone.io/reference/api/2026-07/data-plane/search_records).

The response is this version's index model, with the embedding configuration surfaced as a `semantic_text` field in the index `schema`, named after the `field_map` text entry. Read and write the index through the legacy Records API.

For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

index_model = pc.indexes.create_for_model(
    name="docs-example",
    cloud="aws",
    region="us-east-1",
    embed={
        "model": "multilingual-e5-large",
        "field_map": {"text": "chunk_text"},
    },
)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const indexModel = await pc.indexes.createForModel({
  name: 'docs-example',
  cloud: 'aws',
  region: 'us-east-1',
  embed: {
    model: 'multilingual-e5-large',
    fieldMap: { text: 'chunk_text' },
  },
});
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

    idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
        Name:   "docs-example",
        Cloud:  pinecone.CloudAWS,
        Region: "us-east-1",
        Embed: pinecone.CreateIndexForModelEmbed{
            Model:    "multilingual-e5-large",
            FieldMap: map[string]interface{}{"text": "chunk_text"},
        },
    })
    if err != nil {
        log.Fatalf("Failed to create index: %v", err)
    }
    fmt.Println(idx.Name, idx.Host)
}
```

```hcl Terraform theme={null}
# Requires Terraform provider v5.0.0 or later
# Creates a legacy integrated index. For new indexes, declare integrated embedding
# on a string field of a document index instead (provider v5.1.0 or later).
resource "pinecone_index" "docs_example" {
  name = "docs-example"
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  embed = {
    model = "multilingual-e5-large"
    field_map = {
      text = "chunk_text"
    }
  }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/indexes/create-for-model" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "docs-example",
    "cloud": "aws",
    "region": "us-east-1",
    "embed": {
      "model": "multilingual-e5-large",
      "field_map": {"text": "chunk_text"}
    }
  }'
```
