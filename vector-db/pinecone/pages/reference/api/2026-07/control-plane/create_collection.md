---
title: "Create a collection"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_collection
path: reference/api/2026-07/control-plane/create_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /collections
Create a Pinecone collection.
Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/collections" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "name": "example-collection",
          "source": "docs-example"
    }'
  ```
</RequestExample>
