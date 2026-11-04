---
title: "Semantic search"
source: https://docs.pinecone.io/guides/search/semantic-search
path: guides/search/semantic-search
---

Run semantic search in Pinecone over dense vectors in a document index, querying with text or with a dense vector you generate.

Semantic search finds the documents in an [index with dense vectors](/guides/indexes/indexing-overview#indexes-with-dense-vectors) that are most similar in meaning and context to a query. It's also called nearest neighbor search, similarity search, or vector search.

Semantic search uses [dense vectors](https://www.pinecone.io/learn/vector-embeddings/). Each number in a dense vector corresponds to a point in a multidimensional space. Vectors that are closer together in that space are semantically similar.

For a legacy vector index, see [Query vectors](/guides/legacy/vectors-api/query-vectors). For a legacy integrated index, see [Search with text](/guides/legacy/records-api/search-with-text).

## Search a document index

In a [document index](/guides/indexes/data-modeling#documents), you choose how to score each search with a clause in `score_by`. Use an `embed` clause to search with text, or a `dense_vector` clause to search with a dense vector you generate yourself.

### Search with text

To search with text, the `string` field must declare `embed`, which enables [integrated embedding](/guides/search/integrated-embedding). Pinecone embeds your query text with the field's model. For example, this searches the `chunk_text` field of an index whose schema declares `"chunk_text": {"type": "string", "embed": {}}` and returns the 2 documents most semantically related to "Disease prevention":

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

results = index.documents.search(
    namespace="example-namespace",
    top_k=2,
    score_by=[
        {"type": "embed", "fields": ["chunk_text"], "query": "Disease prevention"}
    ],
    include_fields=["chunk_text", "category"],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: "INDEX_HOST", namespace: "example-namespace" })

const results = await index.documents.search({
  topK: 2,
  scoreBy: [
    { type: 'embed', fields: ['chunk_text'], query: 'Disease prevention' },
  ],
  includeFields: ['chunk_text', 'category'],
})

console.log(results)
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func prettifyStruct(obj interface{}) string {
    bytes, _ := json.MarshalIndent(obj, "", "  ")
    return string(bytes)
}

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    // To get the unique host for an index,
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    query := "Disease prevention"
    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 2,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeEmbed, Fields: []string{"chunk_text"}, Query: &query},
        },
        IncludeFields: []string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "top_k": 2,
            "score_by": [
                {
                    "type": "embed",
                    "fields": ["chunk_text"],
                    "query": "Disease prevention"
                }
            ],
            "include_fields": ["chunk_text", "category"]
        }'
```

### Search with a dense vector

To search a `dense_vector` field, pass a `dense_vector` clause in `score_by` with the query's dense vector. Generate the query vector with the same embedding model you used at upsert. For example, this searches the `embedding` field of the [`articles-hybrid` schema](/guides/search/full-text-search#example-schemas), so the query vector must have 1536 dimensions:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Replace with your query embedding, which must match the index's dimension (1536 in this example)
query_vector = [0.1] * 1536

results = index.documents.search(
    namespace="articles",
    top_k=3,
    score_by=[
        {
            "type": "dense_vector",
            "fields": ["embedding"],
            "values": query_vector,
        }
    ],
    include_fields=["title"],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: "INDEX_HOST", namespace: "articles" })

// Replace with your query embedding, which must match the index's dimension (1536 in this example)
const queryVector = new Array(1536).fill(0.1)

const results = await index.documents.search({
  topK: 3,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: queryVector },
  ],
  includeFields: ['title'],
})

console.log(results)
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func prettifyStruct(obj interface{}) string {
    bytes, _ := json.MarshalIndent(obj, "", "  ")
    return string(bytes)
}

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    // To get the unique host for an index,
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "articles"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    // Replace with your query embedding, which must match the index's dimension (1536 in this example)
    queryVector := make([]float32, 1536)
    for i := range queryVector {
        queryVector[i] = 0.1
    }
    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 3,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
        },
        IncludeFields: []string{"title"},
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

# Stand-in built with jq. Replace with your query embedding, which must match the index's dimension (1536 in this example)
QUERY_VECTOR=$(jq -nc '[range(1536) | 0.1]')

curl "https://$INDEX_HOST/namespaces/articles/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "top_k": 3,
            "score_by": [
                {
                    "type": "dense_vector",
                    "fields": ["embedding"],
                    "values": '"$QUERY_VECTOR"'
                }
            ],
            "include_fields": ["title"]
        }'
```
