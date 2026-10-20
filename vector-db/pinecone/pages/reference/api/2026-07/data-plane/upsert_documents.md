---
title: "Upsert documents"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/upsert_documents
path: reference/api/2026-07/data-plane/upsert_documents
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml post /namespaces/{namespace}/documents/upsert
Upsert documents into a namespace.

Each document must include an `_id` field and at least one field defined in the index schema; metadata fields may be provided alongside them. Any metadata field you provide that is not declared in the schema is stored on the document, returned via include_fields, and automatically indexed for filtering.

On a `string` field whose schema declares `embed` or `sparse_embed`, provide the text: Pinecone embeds it with the field's model and stores the resulting vectors, and the text itself unless the field sets `store_text: false`. A vector or any other non-string value on such a field is rejected. A field with `embed` must be present on every document; a field with only `sparse_embed` may be omitted. An index that embeds a field accepts at most 96 documents per request, the inference batch size.

Pinecone embeds the text on every request that carries it, so a retried upsert produces the same vectors and is embedded, and metered, again. If embedding fails, nothing in the request is written. When the request embeds text, the response's `usage.embed_total_tokens` reports the tokens it consumed.

Documents aren't deduplicated by `_id` within a request. Each entry is written, counted in `upserted_count`, billed in write units and, for embedded fields, embedded and counted in `embed_total_tokens`. The last entry with a given `_id` wins.

Upsert fully replaces any document with the same `_id`, so fields you omit are removed. To change specific fields, use [Update documents](/reference/api/2026-07/data-plane/update_documents). If any document fails schema validation, the whole request fails and nothing is written. The namespace is created on first upsert (use `__default__` if you don't need partitioning), and documents become searchable within about a minute.

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(name="articles")

NAMESPACE = "example-namespace"

docs = [
    {"_id": "doc1", "title": "Machine learning in 2024", "body": "Machine learning models are revolutionizing natural language processing", "category": "technology", "year": 2024},
    {"_id": "doc2", "title": "Vector databases", "body": "Vector databases enable fast similarity search across embeddings", "category": "technology", "year": 2023},
    {"_id": "doc3", "title": "Quantum computing", "body": "Quantum computers leverage superposition for faster computation", "category": "science", "year": 2024},
]

# For large ingests, index.documents.batch_upsert(...) splits documents into
# concurrent requests to this endpoint.
index.documents.upsert(
    namespace=NAMESPACE,
    documents=docs,
)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const index = pc.index({
  name: 'articles',
  namespace: 'example-namespace',
});

const result = await index.documents.upsert({
  documents: [
    {
      _id: 'doc1',
      title: 'Machine learning in 2024',
      body: 'Machine learning models are revolutionizing natural language processing',
      category: 'technology',
      year: 2024,
    },
    {
      _id: 'doc2',
      title: 'Vector databases',
      body: 'Vector databases enable fast similarity search across embeddings',
      category: 'technology',
      year: 2023,
    },
    {
      _id: 'doc3',
      title: 'Quantum computing',
      body: 'Quantum computers leverage superposition for faster computation',
      category: 'science',
      year: 2024,
    },
  ],
});

console.log(`Upserted ${result.upsertedCount} documents`);
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

    idx, err := pc.DescribeIndex(ctx, "articles")
    if err != nil {
        log.Fatalf("Failed to describe index: %v", err)
    }

    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
        Host:      idx.Host,
        Namespace: "example-namespace",
    })
    if err != nil {
        log.Fatalf("Failed to create IndexConnection: %v", err)
    }

    res, err := idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
        Documents: []pinecone.Document{
            {
                "_id":      "doc1",
                "title":    "Machine learning in 2024",
                "body":     "Machine learning models are revolutionizing natural language processing",
                "category": "technology",
                "year":     2024,
            },
            {
                "_id":      "doc2",
                "title":    "Vector databases",
                "body":     "Vector databases enable fast similarity search across embeddings",
                "category": "technology",
                "year":     2023,
            },
            {
                "_id":      "doc3",
                "title":    "Quantum computing",
                "body":     "Quantum computers leverage superposition for faster computation",
                "category": "science",
                "year":     2024,
            },
        },
    })
    if err != nil {
        log.Fatalf("Failed to upsert documents: %v", err)
    }
    fmt.Printf("Upserted %d documents\n", res.UpsertedCount)
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="articles-abc123.svc.us-east-1.pinecone.io"
curl "https://$INDEX_HOST/namespaces/__default__/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      {
        "_id": "doc1",
        "title": "Machine learning in 2024",
        "body": "Machine learning models are revolutionizing natural language processing",
        "category": "technology",
        "year": 2024
      },
      {
        "_id": "doc2",
        "title": "Vector databases",
        "body": "Vector databases enable fast similarity search across embeddings",
        "category": "technology",
        "year": 2023
      },
      {
        "_id": "doc3",
        "title": "Quantum computing",
        "body": "Quantum computers leverage superposition for faster computation",
        "category": "science",
        "year": 2024
      }
    ]
  }'
```
