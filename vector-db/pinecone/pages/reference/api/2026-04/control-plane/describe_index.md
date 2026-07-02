---
title: "Describe an index"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/describe_index
path: reference/api/2026-04/control-plane/describe_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /indexes/{index_name}
Get a description of an index.

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" 
  ```
</RequestExample>

<ResponseExample>
  ```jsonc curl theme={null}
  // EXAMPLE RESPONSE 1: Serverless index (on-demand)
  {
    "name": "example-serverless-ondemand-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-serverless-ondemand-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "OnDemand",
          "status": {
            "state": "Ready",
            "current_shards": null,
            "current_replicas": null
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag1": "value1",
      "tag2": "value2"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "END"
      },
      "vector_type": "dense"
    }
  }

  // EXAMPLE RESPONSE 2: Serverless index (dedicated)
  {
    "name": "example-serverless-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-serverless-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0",
      "tag1": "value1"
    }
  }
  ```
</ResponseExample>
