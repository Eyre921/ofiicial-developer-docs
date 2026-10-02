---
title: "Fetch records"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/fetch
path: reference/api/2026-07/data-plane/fetch
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /vectors/fetch
Look up and return records by ID from a single namespace. The returned records include the vector data and/or metadata.
For on-demand indexes, since vector values are retrieved from object storage, fetch operations may have increased latency. If you only need metadata or IDs, consider using the query operation with `includeValues` set to `false` instead.
For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/fetch?ids=id-1&ids=id-2&namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
