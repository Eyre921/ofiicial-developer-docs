---
title: "Update a record"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/update
path: reference/api/2026-07/data-plane/update
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /vectors/update
Update records in a namespace, either by ID or with a metadata filter. By ID, you can change a single record's vector values, its metadata, or both. A filter updates metadata only, and applies to every record that matches.

If a vector value is included, it will overwrite the previous value. If `set_metadata` is included, only the specified metadata fields are modified, and if a specified metadata field does not exist, it is added.

For guidance and examples, see [Update data](https://docs.pinecone.io/guides/manage-data/update-data).

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
