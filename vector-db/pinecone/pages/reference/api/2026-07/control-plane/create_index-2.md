---
title: "Create an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index
path: reference/api/2026-07/control-plane/create_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes
Create a Pinecone index. Define the schema for your index — dense vector, sparse vector, and full-text search fields, and string fields with integrated embedding — and, optionally, the deployment infrastructure (managed serverless or BYOC).

The index is a document index, read and written through the Documents API. To enable integrated embedding on a field, declare a `string` field with `embed` (dense) and/or `sparse_embed` (sparse): Pinecone embeds the field's text when documents are written and the query text when a search scores the field. BYOC indexes cannot declare `embed` or `sparse_embed`.

**The index schema cannot be modified after creation.** Field types, dimensions, metrics, embedding models, and text-analysis settings are permanent. Choose your schema carefully before creating an index.

To create an index from a backup, use [Create index from backup](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup).

For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index).

[Create a legacy integrated index](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_for_model) creates legacy integrated indexes, which require the legacy Records API.

The index initializes asynchronously. Before sending data plane requests, poll [Describe an index](/reference/api/2026-07/control-plane/describe_index) until `status.ready` is `true` (and, for `Dedicated` read capacity, until `read_capacity.status.state` is `"Ready"`). The response shows each `full_text_search` field's resolved analyzer settings (`language`, `stemming`, and `stop_words`), including any defaults applied at creation.

## Cloud regions

For managed (serverless) indexes, the `cloud` and `region` fields in `deployment` accept the following values:

| Cloud | Region | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| - | - | - | - |
| `aws` | `us-east-1` (Virginia) | Starter, Builder, Standard, Enterprise | General availability |
| `aws` | `us-west-2` (Oregon) | Builder, Standard, Enterprise | General availability |
| `aws` | `eu-west-1` (Ireland) | Builder, Standard, Enterprise | General availability |
| `aws` | `eu-central-1` (Frankfurt) | Builder, Standard, Enterprise | General availability |
| `aws` | `ap-southeast-1` (Singapore) | Builder, Standard, Enterprise | General availability |
| `gcp` | `us-central1` (Iowa) | Builder, Standard, Enterprise | General availability |
| `gcp` | `europe-west4` (Netherlands) | Builder, Standard, Enterprise | General availability |
| `azure` | `eastus2` (Virginia) | Builder, Standard, Enterprise | General availability |

The cloud and region can't be changed after a serverless index is created.

> [!NOTE]
>
> On the Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade to the Builder, Standard, or Enterprise plan](/admin/billing/upgrade-billing-plan).

For BYOC indexes, set `deployment.environment` to the environment ID provisioned for your account instead. See [Bring Your Own Cloud](/guides/production/bring-your-own-cloud) for details.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schema = (
    SchemaBuilder()
      .add_string_field(name="title", full_text_search={})
      .add_string_field(name="body", full_text_search={"language": "en", "stemming": True, "stop_words": True})
      .build()
)

index_model = pc.indexes.create(
    name="articles",
    schema=schema,
    read_capacity={"mode": "OnDemand"},
)

host = index_model.host
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const indexModel = await pc.indexes.create({
  name: 'articles',
  schema: {
    fields: {
      title: {
        type: 'string',
        fullTextSearch: {},
      },
      body: {
        type: 'string',
        fullTextSearch: {
          language: 'en',
          stemming: true,
          stopWords: true,
        },
      },
    },
  },
  readCapacity: {
    mode: 'OnDemand',
  },
});

const host = indexModel.host;
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

    language := "en"
    stemming := true
    stopWords := true

    idx, err := pc.CreateIndex(ctx, &pinecone.CreateIndexRequest{
        Name: "articles",
        Schema: pinecone.IndexSchema{
            Fields: map[string]pinecone.IndexSchemaField{
                "title": {
                    String: &pinecone.StringField{
                        FullTextSearch: &pinecone.FullTextSearchConfig{},
                    },
                },
                "body": {
                    String: &pinecone.StringField{
                        FullTextSearch: &pinecone.FullTextSearchConfig{
                            Language:  &language,
                            Stemming:  &stemming,
                            StopWords: &stopWords,
                        },
                    },
                },
            },
        },
        ReadCapacity: &pinecone.ReadCapacityParams{
            OnDemand: &pinecone.ReadCapacityOnDemandConfig{},
        },
    })
    if err != nil {
        log.Fatalf("Failed to create index: %v", err)
    }

    host := idx.Host
    fmt.Println(host)
}
```

```hcl Terraform theme={null}
# Requires Terraform provider v5.0.0 or later
resource "pinecone_index" "articles" {
  name = "articles"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      title = { string = { full_text_search = {} } }
      body  = { string = { full_text_search = { language = "en", stemming = true, stop_words = true } } }
    }
  }
  read_capacity = {
    on_demand = {}
  }
  deletion_protection = "disabled"
}

output "articles_host" {
  value = pinecone_index.articles.host
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

# EXAMPLE REQUEST 1: On-demand read capacity (default)
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "articles",
    "deployment": {
      "deployment_type": "managed",
      "cloud": "aws",
      "region": "us-east-1"
    },
    "schema": {
      "fields": {
        "title": {
          "type": "string",
          "full_text_search": {}
        },
        "body": {
          "type": "string",
          "full_text_search": {}
        }
      }
    },
    "read_capacity": { "mode": "OnDemand" },
    "deletion_protection": "disabled"
  }'

# EXAMPLE REQUEST 2: Dedicated read capacity
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "articles-dedicated",
    "deployment": {
      "deployment_type": "managed",
      "cloud": "aws",
      "region": "us-east-1"
    },
    "schema": {
      "fields": {
        "content": {
          "type": "string",
          "full_text_search": {}
        }
      }
    },
    "read_capacity": {
      "mode": "Dedicated",
      "dedicated": {
        "node_type": "b1",
        "scaling": "Manual",
        "manual": { "shards": 1, "replicas": 1 }
      }
    },
    "deletion_protection": "disabled"
  }'

# EXAMPLE REQUEST 3: Multi-field schema (text + dense + sparse ranking fields)
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "articles-multifield",
    "deployment": {
      "deployment_type": "managed",
      "cloud": "aws",
      "region": "us-east-1"
    },
    "schema": {
      "fields": {
        "title":     { "type": "string",        "full_text_search": {} },
        "body":      { "type": "string",        "full_text_search": { "language": "en", "stemming": true, "stop_words": true } },
        "embedding": { "type": "dense_vector",  "dimension": 1536, "metric": "cosine" },
        "sparse_embedding": { "type": "sparse_vector" }
      }
    }
  }'

# EXAMPLE REQUEST 4: Bring-your-own-cloud (BYOC) deployment.
# BYOC indexes support on-demand and dedicated read capacity. This example uses dedicated.
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "byoc-index",
    "deployment": {
      "deployment_type": "byoc",
      "environment": "aws-us-east-1-b921.byoc"
    },
    "read_capacity": {
      "mode": "Dedicated",
      "dedicated": {
        "node_type": "b1",
        "scaling": "Manual",
        "manual": { "shards": 1, "replicas": 1 }
      }
    },
    "schema": {
      "fields": {
        "embedding": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
      }
    }
  }'

# EXAMPLE REQUEST 5: BYOC deployment with on-demand read capacity.
# The index runs on the shared on-demand pool in your BYOC cluster, so no shards or replicas are set.
curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "byoc-on-demand-index",
    "deployment": {
      "deployment_type": "byoc",
      "environment": "aws-us-east-1-b921.byoc"
    },
    "read_capacity": {
      "mode": "OnDemand"
    },
    "schema": {
      "fields": {
        "embedding": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
      }
    }
  }'
```
