---
title: "Update a record"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/update
path: reference/api/2026-07/data-plane/update
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/update
Update records by ID or by metadata in a namespace. Updating by ID changes the vector and/or metadata of a single record. Updating by metadata changes metadata across multiple records using a metadata filter.
If a vector value is included, it will overwrite the previous value. If `set_metadata` is included, only the specified metadata fields are modified, and if a specified metadata field does not exist, it is added.
For guidance and examples, see [Update data](https://docs.pinecone.io/guides/manage-data/update-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "id": "id-3",
          "values": [4.0, 2.0],
          "setMetadata": {"type": "comedy"},
          "namespace": "example-namespace"
        }'
  ```
</RequestExample>
