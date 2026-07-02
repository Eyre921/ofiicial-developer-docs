---
title: "Upsert records"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/upsert
path: reference/api/2026-04/data-plane/upsert
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /vectors/upsert
Upsert records into a namespace. If a new value is upserted for an existing record ID, it will overwrite the previous value.

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
      "vectors": [
        {
          "id": "vec1",
          "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
          "metadata": {"genre": "comedy", "year": 2020}
        },
        {
          "id": "vec2",
          "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
          "metadata": {"genre": "documentary", "year": 2019}
        }
      ],
      "namespace": "example-namespace"
    }'
  ```
</RequestExample>

<ResponseExample />

```
```
