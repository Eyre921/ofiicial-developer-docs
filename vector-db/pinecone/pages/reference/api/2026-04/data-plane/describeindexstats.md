---
title: "Get index stats"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/describeindexstats
path: reference/api/2026-04/data-plane/describeindexstats
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /describe_index_stats
Return statistics about the contents of an index, including the vector count per namespace, the number of dimensions, and the index fullness.

Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.

<Note>
  Index fullness is also relevant for [dedicated read nodes](/guides/index-data/dedicated-read-nodes#index-fullness). The response includes `memoryFullness` and `storageFullness` alongside `indexFullness`, which summarizes overall capacity usage. For serverless on-demand indexes, all three values are typically `0` because storage and compute scale automatically. For dedicated indexes, monitor these values and [add shards](/guides/index-data/dedicated-read-nodes#add-or-remove-shards) before the index reaches capacity.
</Note>

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```jsonc curl theme={null}
  // EXAMPLE RESPONSE 1: Serverless index (on-demand)
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 10000
      }
    },
    "indexFullness": 0,
    "totalVectorCount": 10000,
    "dimension": 1024,
    "metric": "cosine",
    "vectorType": "dense",
    "memoryFullness": 0,
    "storageFullness": 0
  }

  // EXAMPLE RESPONSE 2: Serverless index (dedicated read nodes)
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 705000
      }
    },
    "indexFullness": 0.01,
    "totalVectorCount": 705000,
    "dimension": 1536,
    "metric": "cosine",
    "vectorType": "dense",
    "memoryFullness": 0.01,
    "storageFullness": 0.01
  }
  ```
</ResponseExample>
