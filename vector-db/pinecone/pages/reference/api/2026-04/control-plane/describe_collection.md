---
title: "Describe a collection"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/describe_collection
path: reference/api/2026-04/control-plane/describe_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml get /collections/{collection_name}
Get a description of a collection.
Serverless indexes do not support collections.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/collections/tiny-collection" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "name": "example-collection",
      "status": "Ready",
      "environment": "us-east-1-aws",
      "size": 3075398,
      "vector_count": 99,
      "dimension": 1536
  }
  ```
</ResponseExample>
