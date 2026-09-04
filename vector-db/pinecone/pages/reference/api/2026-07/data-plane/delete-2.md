---
title: "Delete records"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/delete
path: reference/api/2026-07/data-plane/delete
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/delete
Delete records by id or by metadata from a single namespace.

For guidance and examples, see [Delete data](https://docs.pinecone.io/guides/manage-data/delete-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "ids": [
        "id-1", 
        "id-2"
      ],
      "namespace": "example-namespace"
    }
  '
  ```
</RequestExample>
