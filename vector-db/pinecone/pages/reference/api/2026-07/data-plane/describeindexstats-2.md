---
title: "Get index stats"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/describeindexstats
path: reference/api/2026-07/data-plane/describeindexstats
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /describe_index_stats
Return statistics about the contents of an index, including the vector count per namespace, the number of dimensions, and the index fullness.

Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.

<Note>
  Index fullness is also relevant for [dedicated read nodes](/guides/index-data/dedicated-read-nodes#index-fullness). The response includes `memoryFullness` and `storageFullness` alongside `indexFullness`, which summarizes overall capacity usage. For serverless on-demand indexes, all three values are typically `0` because storage and compute scale automatically. For dedicated indexes, these values indicate when the index needs more capacity. See [Scale your index](/guides/index-data/dedicated-read-nodes#scale-your-index).
</Note>

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
