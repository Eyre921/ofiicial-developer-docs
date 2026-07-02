---
title: "Search with text"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/search_records
path: reference/api/2026-04/data-plane/search_records
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /records/namespaces/{namespace}/search
Search a namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query. 

Searching with text is supported only for indexes with [integrated embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding). Searching with a query vector or record ID is supported for all indexes. 

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
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a query vector and rerank the results
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "query": {
              "vector": {
                  "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
              },
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a record ID and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "query": {
              "id": "rec1",
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.004433765076100826,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec4",
                  "_score": 0.0029121784027665854,
                  "fields": {
                      "category": "endocrine system",
                      "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6,
          "rerank_units": 1
      }
  }
  ```
</ResponseExample>
