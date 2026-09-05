---
title: "Create an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index
path: reference/api/2026-07/control-plane/create_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes
Create a Pinecone index. Define the schema for your index — dense vector, sparse vector, and full-text search fields — and, optionally, the deployment infrastructure (managed serverless or BYOC). To create an index with an integrated embedding model, use [Create an index with integrated embedding](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_for_model). If `deployment` is omitted, the index is deployed as a managed (serverless) index on `aws` in `us-east-1`.
**The index schema cannot be modified after creation.** Field types, dimensions, metrics, and text-analysis settings are permanent. Choose your schema carefully before creating an index.
To create an index from a backup, use [Create index from backup](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup).
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index).


Creates a new schema-defined index. The schema declares each field and its type — dense vector, sparse vector, or [full-text search](/guides/search/full-text-search). The index initializes asynchronously; poll [`GET /indexes/{index_name}`](/reference/api/2026-07/control-plane/describe_index) until `status.ready: true` (and, for `Dedicated` read capacity, `read_capacity.status.state: "Ready"`) before performing data plane operations.

<Note>
  To create a classic vector index (read and written through the Vectors API), use the reserved `_values` (dense) and/or `_sparse_values` (sparse) schema fields. These replace the top-level `dimension`, `metric`, and `vector_type` of earlier API versions, and are REST-only for now.
</Note>

<Note>
  Document schemas do not support `semantic_text` fields. To combine semantic ranking with full-text search, declare a `dense_vector` field and provide vector values when you upsert documents. For integrated embedding indexes that use the Records API, see [Create an index](/guides/index-data/create-an-index).
</Note>

## Cloud regions

For managed (serverless) indexes, the `cloud` and `region` fields in `deployment` accept the following values:

| Cloud   | Region                       | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| ------- | ---------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| `aws`   | `us-east-1` (Virginia)       | Starter, Builder, Standard, Enterprise              | General availability                                      |
| `aws`   | `us-west-2` (Oregon)         | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `eu-west-1` (Ireland)        | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `eu-central-1` (Frankfurt)   | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `ap-southeast-1` (Singapore) | Builder, Standard, Enterprise                       | General availability                                      |
| `gcp`   | `us-central1` (Iowa)         | Builder, Standard, Enterprise                       | General availability                                      |
| `gcp`   | `europe-west4` (Netherlands) | Builder, Standard, Enterprise                       | General availability                                      |
| `azure` | `eastus2` (Virginia)         | Builder, Standard, Enterprise                       | General availability                                      |

The cloud and region cannot be changed after a serverless index is created.

<Note>
  On the Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade to the Builder, Standard, or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

For BYOC indexes, set `deployment.environment` to the environment ID provisioned for your account instead. See [Bring Your Own Cloud](/guides/production/bring-your-own-cloud) for details.

<RequestExample>
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

  # EXAMPLE REQUEST 4: Classic vector index — reserved `_values` field, served by the Vectors API.
  curl "https://api.pinecone.io/indexes" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "classic-index",
      "schema": {
        "fields": {
          "_values": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
        }
      }
    }'

  # EXAMPLE REQUEST 5: Bring-your-own-cloud (BYOC) deployment.
  # BYOC indexes require Dedicated read capacity — OnDemand is rejected.
  curl "https://api.pinecone.io/indexes" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "byoc-index",
      "deployment": {
        "deployment_type": "byoc",
        "environment": "aws-us-east-1-b921"
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
  ```
</RequestExample>

<Note>
  Responses show each `full_text_search` field's resolved analyzer config: `language`, `stemming`, and `stop_words` reflect your request settings or the defaults applied at index creation.
</Note>
