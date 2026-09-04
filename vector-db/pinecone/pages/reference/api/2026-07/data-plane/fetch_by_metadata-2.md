---
title: "Fetch records by metadata"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/fetch_by_metadata
path: reference/api/2026-07/data-plane/fetch_by_metadata
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/fetch_by_metadata
Look up and return records by metadata from a single namespace. The returned records include the vector data and metadata.
For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "namespace": "__default__",
      "filter": {"genre": {"$eq": "Action/Adventure"}},
      "limit": 2
    }'
  ```
</RequestExample>
