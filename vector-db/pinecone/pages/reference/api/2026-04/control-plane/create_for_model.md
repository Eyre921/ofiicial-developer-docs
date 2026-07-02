---
title: "Create an index with integrated embedding"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/create_for_model
path: reference/api/2026-04/control-plane/create_for_model
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml post /indexes/create-for-model
Create an index with integrated embedding.
With this type of index, you provide source text, and  Pinecone uses a [hosted embedding model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models)  to convert the text automatically during [upsert](https://docs.pinecone.io/reference/api/2026-04/data-plane/upsert_records)  and [search](https://docs.pinecone.io/reference/api/2026-04/data-plane/search_records).  
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/indexes/create-for-model \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "name": "integrated-dense-curl",
          "cloud": "aws",
          "region": "us-east-1",
          "embed": {
            "model": "llama-text-embed-v2",
            "metric": "cosine",
            "field_map": {
              "text": "chunk_text"
            },
            "write_parameters": {
              "input_type": "passage",
              "truncate": "END"
            },
            "read_parameters": {
              "input_type": "query",
              "truncate": "END"
            }
          }
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "9dabb7cb-ec0a-4e2e-b79e-c7c997e592ce",
    "name": "integrated-dense-curl",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": false,
      "state": "Initializing"
    },
    "host": "integrated-dense-curl-govk0nt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws"
      }
    },
    "deletion_protection": "disabled",
    "tags": null,
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "chunk_text"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "input_type": "query",
        "truncate": "END"
      }
    }
  }
  ```
</ResponseExample>
