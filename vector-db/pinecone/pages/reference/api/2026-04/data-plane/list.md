---
title: "List record IDs"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/list
path: reference/api/2026-04/data-plane/list
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml get /vectors/list
List the IDs of records in a single namespace of a serverless index. An optional prefix can be passed to limit the results to IDs with a common prefix.

Returns up to 100 IDs at a time by default in sorted order (bitwise "C" collation). If the `limit` parameter is set, `list` returns up to that number of IDs instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of IDs. When the response does not include a `pagination_token`, there are no more IDs to return.

For guidance and examples, see [List record IDs](https://docs.pinecone.io/guides/manage-data/list-record-ids).

**Note:** `list` is supported only for serverless indexes.

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&prefix=doc1#&limit=3" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "vectors": [
      { "id": "doc1#chunk1" },
      { "id": "doc1#chunk2" },
      { "id": "doc1#chunk3" }
    ],
    "pagination": {
      "next": "c2Vjb25kY2FsbA=="
    },
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</ResponseExample>
