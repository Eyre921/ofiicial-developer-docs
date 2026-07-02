---
title: "Create a collection"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/create_collection
path: reference/api/2026-04/control-plane/create_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml post /collections
Create a Pinecone collection.
  
Serverless indexes do not support collections.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/collections" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "name": "example-collection",
          "source": "docs-example"
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "name": "example-collection",
      "status": "Initializing",
      "environment": "us-east-1-aws",
      "dimension": 1536
  }
  ```
</ResponseExample>
