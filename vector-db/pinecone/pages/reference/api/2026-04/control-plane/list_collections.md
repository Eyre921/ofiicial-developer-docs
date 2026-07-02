---
title: "List collections"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_collections
path: reference/api/2026-04/control-plane/list_collections
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /collections
List all collections in a project.
Serverless indexes do not support collections.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/collections" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "collections": [
          {
              "name": "example-collection1",
              "status": "Ready",
              "environment": "us-east-1-aws",
              "size": 3081918,
              "vector_count": 99,
              "dimension": 3
          },
          {
              "name": "example-collection1",
              "status": "Ready",
              "environment": "us-east-1-aws",
              "size": 160087040000000,
              "vector_count": 10000000,
              "dimension": 1536
          }
      ]
  }
  ```
</ResponseExample>
