---
title: "Search with text"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/search_records
path: reference/api/2026-07/data-plane/search_records
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /records/namespaces/{namespace}/search
Search a namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query. 

Searching with text (`inputs`) is supported only for indexes with [integrated embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding); for any other index a text query is rejected with `400`, and it is not available on BYOC indexes; reranking (`rerank`) is likewise unavailable on BYOC indexes. Searching with a query vector (`vector`) or a record ID (`id`) works on any index served by the vectors API.

For guidance and examples, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```shell curl theme={null}
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Search with a query text and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 4
          },
          "fields": ["category", "chunk_text"],
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'

  # Search with a query vector and rerank the results
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "query": {
              "vector": {
                  "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
              },
              "top_k": 4
          },
          "fields": ["category", "chunk_text"],
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'

  # Search with a record ID and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "query": {
              "id": "rec1",
              "top_k": 4
          },
          "fields": ["category", "chunk_text"],
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'
  ```
</RequestExample>
