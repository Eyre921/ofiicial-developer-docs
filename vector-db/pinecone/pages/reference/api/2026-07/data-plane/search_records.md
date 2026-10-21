---
title: "Search with text (legacy Records API)"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/search_records
path: reference/api/2026-07/data-plane/search_records
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /records/namespaces/{namespace}/search
Search a namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query. 

This operation is part of the legacy Records API, which legacy integrated indexes require. For new work, create a document index with a `string` field that uses integrated embedding (`embed` or `sparse_embed`), and search it with the Documents API's `search_documents` operation and an `embed` or `sparse_embed` scoring method.

Searching with text (`inputs`) is supported only for [legacy integrated indexes](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding); for any other index a text query is rejected with `400`, and it is not available on BYOC indexes; reranking (`rerank`) is likewise unavailable on BYOC indexes. Searching with a query vector (`vector`) or a record ID (`id`) works on any index served by the vectors API.

For guidance and examples, see [Search](https://docs.pinecone.io/guides/search/search-overview).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

# Search with a query text and rerank the results
# Supported only for indexes with integrated embedding
search_with_text = index.search(
    namespace="example-namespace",
    inputs={"text": "Disease prevention"},
    top_k=4,
    fields=["category", "chunk_text"],
    rerank={
        "model": "bge-reranker-v2-m3",
        "top_n": 2,
        "rank_fields": ["chunk_text"],
    },
)
for hit in search_with_text.result.hits:
    print(hit.id, hit.score, hit.fields)

# Search with a query vector and rerank the results
search_with_vector = index.search(
    namespace="example-namespace",
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    top_k=4,
    fields=["category", "chunk_text"],
    rerank={
        "query": "Disease prevention",
        "model": "bge-reranker-v2-m3",
        "top_n": 2,
        "rank_fields": ["chunk_text"],
    },
)
for hit in search_with_vector.result.hits:
    print(hit.id, hit.score, hit.fields)

# Search with a record ID and rerank the results
search_with_id = index.search(
    namespace="example-namespace",
    id="rec1",
    top_k=4,
    fields=["category", "chunk_text"],
    rerank={
        "query": "Disease prevention",
        "model": "bge-reranker-v2-m3",
        "top_n": 2,
        "rank_fields": ["chunk_text"],
    },
)
for hit in search_with_id.result.hits:
    print(hit.id, hit.score, hit.fields)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

// To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({
  host: 'INDEX_HOST',
  namespace: 'example-namespace',
});

// Search with a query text and rerank the results
// Supported only for indexes with integrated embedding
const searchWithText = await index.searchRecords({
  query: {
    inputs: { text: 'Disease prevention' },
    topK: 4,
  },
  fields: ['category', 'chunk_text'],
  rerank: {
    model: 'bge-reranker-v2-m3',
    topN: 2,
    rankFields: ['chunk_text'],
  },
});
console.log(searchWithText.result.hits);

// Search with a query vector and rerank the results
const searchWithVector = await index.searchRecords({
  query: {
    vector: {
      values: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    },
    topK: 4,
  },
  fields: ['category', 'chunk_text'],
  rerank: {
    query: 'Disease prevention',
    model: 'bge-reranker-v2-m3',
    topN: 2,
    rankFields: ['chunk_text'],
  },
});
console.log(searchWithVector.result.hits);

// Search with a record ID and rerank the results
const searchWithId = await index.searchRecords({
  query: {
    id: 'rec1',
    topK: 4,
  },
  fields: ['category', 'chunk_text'],
  rerank: {
    query: 'Disease prevention',
    model: 'bge-reranker-v2-m3',
    topN: 2,
    rankFields: ['chunk_text'],
  },
});
console.log(searchWithId.result.hits);
```

```go Go theme={null}
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: os.Getenv("PINECONE_API_KEY"),
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    // To get the host for an index, see https://docs.pinecone.io/guides/manage-data/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      "INDEX_HOST",
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    fields := []string{"category", "chunk_text"}
    rerankQuery := "Disease prevention"
    topN := int32(2)

    // Search with a query text and rerank the results
    // Supported only for indexes with integrated embedding
    searchWithText, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
            TopK: 4,
        },
        Fields: &fields,
        Rerank: &pinecone.SearchRecordsRerank{
            Model:      "bge-reranker-v2-m3",
            TopN:       &topN,
            RankFields: []string{"chunk_text"},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search with text: %v", err)
    }
    for _, hit := range searchWithText.Result.Hits {
        fmt.Println(hit.Id, hit.Score, hit.Fields["category"])
    }

    // Search with a query vector and rerank the results
    searchWithVector, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            Vector: &pinecone.SearchRecordsVector{
                Values: &[]float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
            },
            TopK: 4,
        },
        Fields: &fields,
        Rerank: &pinecone.SearchRecordsRerank{
            Query:      &rerankQuery,
            Model:      "bge-reranker-v2-m3",
            TopN:       &topN,
            RankFields: []string{"chunk_text"},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search with vector: %v", err)
    }
    for _, hit := range searchWithVector.Result.Hits {
        fmt.Println(hit.Id, hit.Score, hit.Fields["category"])
    }

    // Search with a record ID and rerank the results
    recordId := "rec1"
    searchWithId, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            Id:   &recordId,
            TopK: 4,
        },
        Fields: &fields,
        Rerank: &pinecone.SearchRecordsRerank{
            Query:      &rerankQuery,
            Model:      "bge-reranker-v2-m3",
            TopN:       &topN,
            RankFields: []string{"chunk_text"},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search with ID: %v", err)
    }
    for _, hit := range searchWithId.Result.Hits {
        fmt.Println(hit.Id, hit.Score, hit.Fields["category"])
    }
}
```

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
