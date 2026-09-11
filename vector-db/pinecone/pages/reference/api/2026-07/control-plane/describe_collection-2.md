---
title: "Describe a collection"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_collection
path: reference/api/2026-07/control-plane/describe_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml get /collections/{collection_name}
Get a description of a collection.
Collections are supported only for pod-based indexes. Pod-based indexes cannot be created with API version `2026-07`, so this operation applies to pod-based indexes created with an earlier API version.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/collections/tiny-collection" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
