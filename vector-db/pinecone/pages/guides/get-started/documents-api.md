---
title: "Pinecone Documents API"
source: https://docs.pinecone.io/guides/get-started/documents-api
path: guides/get-started/documents-api
---

The Pinecone Documents API stores text, vectors, and metadata in one schema-defined index and serves full-text, semantic, and sparse-vector search from it.

The Documents API is how you read and write data in Pinecone Database. It's built for agents and search apps that need to find an exact identifier as reliably as a concept. An embedding model can't reliably tell one SKU, error code, or order number from a similar one, so a vector search on its own can return the wrong result without raising an error. One document index serves both keyword (full-text) search and semantic search, so you don't need a separate keyword engine to keep in sync with your vectors.

You don't have to generate embeddings yourself. When a text field declares `embed`, Pinecone embeds the text when you upsert it and embeds your query when you search. You can also bring your own dense or sparse vectors.

## Index schema

Each document is a JSON object with fields you name, such as `title` or `category`. The index schema, set when you create the index, declares which fields are searchable and how:

| Field | Declared as | Searched with |
| - | - | - |
| Text, such as a title or body | `string` with `full_text_search` | Full-text search, with BM25 ranking, Lucene query syntax (boolean operators, phrases, boosting, and fuzzy matching), and exact-term filters |
| Text you want Pinecone to embed | `string` with `embed` or `sparse_embed` | Semantic or sparse-vector search on vectors Pinecone generates |
| Vectors you bring | `dense_vector` or `sparse_vector` | Semantic or sparse-vector search |
| Anything else, such as a category or year | Not declared | Metadata filters |

A schema can declare several text fields, such as a title and a body, each with its own [text processing](/guides/search/full-text-search/text-processing) settings for language, stemming, stop words, or n-grams. One `string` field can also declare both `full_text_search` and `embed`, so the same text is searchable by keyword and by meaning. To design the fields for your own data, see [Data modeling](/guides/indexes/data-modeling).

## Search a document index

Each search request ranks results by the clauses in `score_by`, and an optional `filter` narrows the candidates first. You can run these types of search:

* [Full-text search](/guides/search/full-text-search) ranks by keyword relevance (BM25) with a `text` or `query_string` clause.
* [Semantic search with integrated embedding](/guides/search/integrated-embedding) ranks by meaning with an `embed` clause, and Pinecone embeds your query.
* [Semantic search with your own vectors](/guides/search/semantic-search) ranks by meaning with a `dense_vector` clause.
* [Sparse-vector search](/guides/search/sparse-vector-search) ranks by term weights with a `sparse_embed` or `sparse_vector` clause.
* [Semantic search filtered by text](/guides/search/filter-by-metadata#text-match-filters) ranks by meaning but keeps only documents whose full-text fields contain exact terms or phrases, using `$match_all`, `$match_any`, or `$match_phrase` in the `filter`.
* [Hybrid search](/guides/search/hybrid-search) runs a full-text search and a semantic search and merges the results with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).

Full-text clauses can be combined in one request, but a vector or embedding clause must be the only one. Any search can also [filter on metadata](/guides/search/filter-by-metadata), such as `{"category": {"$eq": "accessories"}}`.

In this example, the first search is a full-text search for an exact model number. The second is a semantic search with integrated embedding, filtered to accessories whose title contains that number:

```python Python expandable theme={null}
import os
import time
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schema = (
    SchemaBuilder()
      .add_string_field(name="title", full_text_search={"language": "en"})
      .add_string_field(name="description", full_text_search={"language": "en"}, embed={"model": "llama-text-embed-v2"})
      .build()
)
pc.indexes.create(name="product-catalog", schema=schema)
index = pc.index(name="product-catalog")

index.documents.upsert(
    namespace="catalog",
    documents=[
        {"_id": "1", "title": "KB-1024 wireless mechanical keyboard", "description": "Compact keyboard with brown switches and USB-C charging.", "category": "keyboards"},
        {"_id": "2", "title": "KB-1024 replacement keycaps", "description": "Soft-touch keycaps that fit the KB-1024 and quiet each keystroke.", "category": "accessories"},
        {"_id": "3", "title": "MS-300 silent mouse", "description": "A quiet mouse with soft clicks for shared offices.", "category": "accessories"},
    ],
)
time.sleep(10)  # documents are indexed asynchronously

# Full-text search: rank by exact terms (BM25)
results = index.documents.search(
    namespace="catalog",
    top_k=3,
    score_by=[{"type": "text", "fields": ["title"], "query": "KB-1024"}],
    include_fields=["title"],
)
for match in results.matches:
    print(match._id, match.title)

# Semantic search filtered by text: rank by meaning, keep only documents that contain an exact term, and filter on metadata
results = index.documents.search(
    namespace="catalog",
    top_k=3,
    score_by=[{"type": "embed", "fields": ["description"], "query": "make my typing quieter"}],
    filter={"$and": [{"title": {"$match_all": "KB-1024"}}, {"category": {"$eq": "accessories"}}]},
    include_fields=["title"],
)
for match in results.matches:
    print(match._id, match.title)
```

The first search returns both KB-1024 products. The second returns only the keycaps. The keyboard isn't an accessory, and the mouse's title doesn't contain KB-1024.

For when to use each approach, see [Search overview](/guides/search/search-overview).

## Legacy indexes

Indexes created before the Documents API keep working on the API they were created with:

| Index | Created with | API | Learn more |
| - | - | - | - |
| Legacy vector index | `create_index` with `dimension` and `metric` | Legacy Vectors API | [Create a legacy vector index](/guides/legacy/vectors-api/create-a-vector-index) |
| Legacy integrated index | `create_index_for_model` | Legacy Records API | [Create a legacy integrated index](/guides/legacy/records-api/create-an-integrated-index) |

To move a legacy index to the Documents API, including converting it without reloading your data, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).
