---
title: "Delete a collection"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/delete_collection
path: reference/api/2026-04/control-plane/delete_collection
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml delete /collections/{collection_name}
Delete an existing collection.
Serverless indexes do not support collections.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X DELETE "https://api.pinecone.io/collections/example-collection" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample />
