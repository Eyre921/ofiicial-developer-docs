---
title: "Delete an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/delete_index
path: reference/api/2026-07/control-plane/delete_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml delete /indexes/{index_name}
Delete an existing index.

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X DELETE "https://api.pinecone.io/indexes/docs-example" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
