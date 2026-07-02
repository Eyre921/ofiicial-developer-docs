---
title: "List indexes"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_indexes
path: reference/api/2026-04/control-plane/list_indexes
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /indexes
List all indexes in a project.

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "indexes": [
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
      },
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
      },
      {
        "name": "example-pod-index",
        "vector_type": "dense",
        "metric": "cosine",
        "dimension": 768,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "example-pod-index-bhnyigt.svc.us-east-1-aws.pinecone.io",
        "spec": {
          "pod": {
            "replicas": 1,
            "shards": 1,
            "pods": 1,
            "pod_type": "s1.x1",
            "environment": "us-east-1-aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": null
      }
    ]
  }
  ```
</ResponseExample>
