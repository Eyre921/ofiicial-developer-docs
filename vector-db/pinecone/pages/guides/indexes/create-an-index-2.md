---
title: "Create an index"
source: https://docs.pinecone.io/guides/indexes/create-an-index
path: guides/indexes/create-an-index
---

Create a Pinecone serverless index for full-text (BM25), semantic (dense vector), sparse-vector, or hybrid search with a document schema.

A Pinecone index lets you store and search your data. A document index stores JSON documents whose fields you declare in a schema at creation. It can combine dense vector, sparse vector, and full-text (`string`) fields in one document, so a single index serves [full-text search](/guides/search/full-text-search), [semantic search](/guides/search/semantic-search), and [sparse-vector search](/guides/search/sparse-vector-search).

To create a legacy vector index, see [Create a vector index](/guides/legacy/vectors-api/create-a-vector-index). To create a legacy integrated index, see [Create an integrated index](/guides/legacy/records-api/create-an-integrated-index).

> [!TIP]
>
> You can create an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless).

## Create a document index

An index with a document schema stores typed JSON documents. The schema declares how each ranking field is indexed: as a `string` field with `full_text_search` enabled for BM25 ranking, a `dense_vector` for ANN similarity, or a `sparse_vector`. A single index can mix all three ranking field types, and at query time you pick the ranking signal with `score_by`. Any other fields you upsert are stored as metadata, auto-indexed for filtering at upsert time.

> [!NOTE]
>
> Full-text search and integrated embedding are different features. A `string` field with `full_text_search` is indexed for BM25 keyword ranking and Lucene queries. It doesn't create vectors or call an embedding model. To have Pinecone turn a field's text into vectors, use [integrated embedding](/guides/search/integrated-embedding): declare `embed` or `sparse_embed` on a `string` field in a document index. The legacy `create_index_for_model` path does this too, creating a [legacy integrated index](/guides/legacy/records-api/create-an-integrated-index) served by the legacy Records API.

Indexes with document schemas use API version `2026-07`, supported through REST and the Python (v10 or later), Node.js (v9 or later), and Go (v7 or later) SDKs. For other languages, call the REST endpoint directly.

### Minimal: BM25 on a single text field

The example below creates an `articles` index whose `body` field is indexed for BM25 ranking. Other fields included at upsert time are stored on each document and auto-indexed for filtering as metadata.

```python Python theme={null}
import os
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schema = (
    SchemaBuilder()
      .add_string_field(name="body", full_text_search={})
      .build()
)

pc.indexes.create(name="articles", schema=schema)
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "articles",
    "deployment": {
      "deployment_type": "managed",
      "cloud": "aws",
      "region": "us-east-1"
    },
    "schema": {
      "fields": {
        "body": {
          "type": "string",
          "full_text_search": {}
        }
      }
    }
  }'
```

### Multi-field schema: BM25 + dense vector

A single index with a document schema can hold `string` fields with `full_text_search` and `dense_vector` ranking fields together, and the same schema can also include a `sparse_vector` field. A single search request ranks by one scoring type. Multi-field BM25 is supported: use multiple `text` clauses on different fields, or one `query_string` clause spanning fields. Any scoring method can be combined with metadata filters, including text-match filters (`$match_phrase`, `$match_all`, `$match_any`) on `string` fields with `full_text_search`.

```python Python theme={null}
import os
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schema = (
    SchemaBuilder()
      .add_string_field(name="title", full_text_search={})
      .add_string_field(name="body", full_text_search={})
      .add_dense_vector_field(name="embedding", dimension=1536, metric="cosine")
      .build()
)

pc.indexes.create(name="articles-multi", schema=schema)
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "articles-multi",
    "deployment": {
      "deployment_type": "managed",
      "cloud": "aws",
      "region": "us-east-1"
    },
    "schema": {
      "fields": {
        "title":    { "type": "string", "full_text_search": {} },
        "body":     { "type": "string", "full_text_search": {} },
        "embedding":{ "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
      }
    }
  }'
```

You can include additional fields (for example, `category` or `year`) at upsert time. All metadata fields are automatically indexed for filtering — they don't need to be declared in the schema. The schema is for ranking fields only. `string_list`, `float`, and `boolean` fields are always metadata, and a `string` field is metadata unless it sets `full_text_search`, `embed`, or `sparse_embed`. Declaring a metadata-only field in the schema is rejected at index creation. To index only the metadata fields you filter on, see [Configure metadata indexing](/guides/indexes/configure-metadata-indexing).

### Integrated embedding

On a document index, declare `embed` or `sparse_embed` on a `string` field. Pinecone then embeds its text on write and the query text at search time, so you upsert and search with plain text instead of vectors. See [Integrated embedding](/guides/search/integrated-embedding) for the schema, examples, and limits.

For the full schema reference (all field types, language and analyzer options, dedicated read capacity, and Python SDK examples), see [Full-text search](/guides/search/full-text-search).

> [!NOTE]
>
> You can't add, remove, or modify a document index's fields after you create it. To change a schema, [delete the index](/guides/indexes/manage-indexes#delete-an-index) and create a new one. To move an existing legacy vector index or legacy integrated index onto a document schema, [convert it](/guides/indexes/convert-an-index) instead of reloading your data.

## Create an index from a backup

You can create an index from a backup. For more details, see [Restore an index](/guides/indexes/restore-an-index).

## Wait for the index to be ready

A new index of any type can't accept data until its `status.ready` field is `true`. The Python SDK waits for this by default, and the Node.js SDK waits when you pass `waitUntilReady: true`. If you call the API directly, [describe the index](/guides/indexes/manage-indexes#describe-an-index) repeatedly until `status.ready` is `true`, then upsert.
