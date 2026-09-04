---
title: "Full-text search overview"
source: https://docs.pinecone.io/guides/search/full-text-search
path: guides/search/full-text-search
---

Upsert and search typed JSON documents in Pinecone with BM25 scoring, Lucene query syntax, dense and sparse vector ranking, and metadata filters.

<Tip>
  You can also use the Pinecone console to create indexes with document schemas, upsert documents, search documents, and fetch or delete documents by ID.
</Tip>

Full-text search ranks documents by keyword and phrase relevance using **BM25** scoring, with optional **Lucene** query syntax. Because an index with a document schema can also declare dense and sparse vector fields, the same index can rank by semantic or sparse-vector similarity, so one index can cover keyword and semantic search.

## When to use it

Reach for full-text search when exact words, phrases, names, codes, or identifiers matter, not just semantic similarity. For semantic-only or vector-only workloads, an [index with dense vectors](/guides/core-concepts/key-terms#index-with-dense-vectors) (the Vectors API) is simpler. See [Search overview](/guides/search/search-overview) to choose the right approach.

<Note>
  Full-text search requires [API version](/reference/api/versioning) `2026-07`: send `X-Pinecone-Api-Version: 2026-07` on REST requests, or use the `2026-07` Python SDK (v10 or later).
</Note>

## Capabilities

What full-text search does and doesn't match:

| Capability                      | Status                                                                                                                                                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fuzzy matching (typo tolerance) | Supported in `query_string` queries only ([query syntax](/guides/search/full-text-search/query-syntax))                                                                                                                    |
| Stemming                        | Supported, opt-in per field at index creation ([stemming](/guides/search/full-text-search/text-processing#stemming))                                                                                                       |
| Stop-word removal               | Supported, opt-in per field at index creation ([tokens & analyzers](/guides/search/full-text-search/text-processing#tokens-and-analyzers))                                                                                 |
| Substring / n-gram matching     | Supported, opt-in per field at index creation. Can't be combined with stemming or stop words on the same field ([n-grams](/guides/search/full-text-search/text-processing#substring-search-with-n-grams))                  |
| Synonym expansion               | Not supported. A search for `car` won't match a document containing only `automobile`. Use [semantic search](/guides/search/semantic-search) or [hybrid search](/guides/search/hybrid-search) for synonyms or paraphrases. |

## How it works

Pinecone's Documents API stores typed fields you declare in a schema. End to end, the flow is short: create an index with a [schema](#schema-definition) that declares your ranking fields, upsert your data as JSON documents, then search by choosing one ranking signal per search request with `score_by`. The [end-to-end example](#end-to-end-example) below stitches all three steps into one runnable script.

1. You upsert data as JSON **documents**.
2. You declare how each field should be indexed via a **schema**, as a `string` field with `full_text_search` enabled (BM25 scoring), a `dense_vector` field, or a `sparse_vector` field. The schema is for ranking fields only; metadata fields are not declared.
3. Pinecone indexes each field's content according to the type of the field declared in the schema. Any other fields on the upserted documents are automatically stored and indexed for filtering, no schema declaration required.

For the field types you can declare, see [Schema field types](#schema-field-types). Filterable metadata is not part of the schema. Any field you upsert that is not declared in the schema is stored on the document, returned via `include_fields`, and automatically indexed for filtering, see [Metadata fields](#metadata-fields).

Every search ranks by one scoring type. The `score_by` clause selects the scoring method for the request:

* `text`, BM25 token matching over one or more FTS-enabled `string` fields.
* `query_string`, Lucene query syntax across one or more FTS-enabled `string` fields, including cross-field boolean queries.
* `dense_vector`, vector similarity against a `dense_vector` field.
* `sparse_vector`, sparse-vector similarity against a `sparse_vector` field.

The same index can support all four when the schema declares the corresponding fields, but a given request commits to one scoring type. To narrow the candidates a vector ranking sees, combine the `score_by` with a metadata filter, including the text-match operators `$match_phrase`, `$match_all`, and `$match_any` on FTS-enabled `string` fields, plus the standard logical and comparison operators (`$and`, `$or`, `$not`, `$exists`, etc.). The filter narrows what's eligible; the `score_by` ranks what remains. This is the most common hybrid pattern.

For example, on an index whose schema declares both a `dense_vector` field (`review_embedding`) and an FTS-enabled `string` field (`review_text`), this single request runs semantic search across the corpus but only over documents whose `review_text` contains the exact phrase "beautifully written":

```python Python theme={null}
index.documents.search(
    namespace="reviews",
    top_k=5,
    score_by=[
        {
            "type": "dense_vector",
            "fields": ["review_embedding"],
            "values": query_embedding,
        }
    ],
    filter={"review_text": {"$match_phrase": "beautifully written"}},
)
```

The dense ranking still controls the order of results; the text-match filter just narrows what's eligible to be ranked.

## End-to-end example

A complete run from index creation through search. Copy this into a single file, set `PINECONE_API_KEY`, and run.

<Tip>
  For a runnable version, see this [Google Colab notebook](https://colab.research.google.com/drive/1lsPeNLCJ2ucbYthHYs9WpybW4nAfB8tG), which upserts and searches a sample Wikipedia dataset.
</Tip>

```python Python theme={null}
import os
import time
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# 1. Create an index. Setting `full_text_search` on a `string` field enables BM25.
schema = (
    SchemaBuilder()
      .add_string_field(name="title", full_text_search={"language": "en"})
      .add_string_field(name="body", full_text_search={"language": "en"})
      .build()
)
pc.indexes.create(name="articles-quickstart", schema=schema)

# Wait for the index to be ready before upserting (no timeout — add a loop cap in production).
while not pc.indexes.describe(name="articles-quickstart").status.ready:
    time.sleep(2)

index = pc.Index(name="articles-quickstart")

# 2. Upsert documents. Fields declared in the schema (`title`, `body`) are
#    BM25-indexed; any extra fields (`category`, `year`) are stored on the
#    document and auto-indexed for filtering as metadata.
index.documents.upsert(
    namespace="example-namespace",
    documents=[
        {
            "_id": "doc1",
            "title": "Machine learning in 2024",
            "body": "Machine learning models are revolutionizing natural language processing",
            "category": "technology",
            "year": 2024,
        },
        {
            "_id": "doc2",
            "title": "Vector databases",
            "body": "Vector databases enable fast similarity search across embeddings",
            "category": "technology",
            "year": 2023,
        },
        {
            "_id": "doc3",
            "title": "Quantum computing",
            "body": "Quantum computers leverage superposition for faster computation",
            "category": "science",
            "year": 2024,
        },
    ],
)

# 3. Search with BM25 ranking on `body`, narrowed by a metadata filter and a
#    phrase-match text filter on the FTS field. The relevance score comes back
#    as `_score` (not `score`).
response = index.documents.search(
    namespace="example-namespace",
    top_k=5,
    score_by=[
        {
            "type": "text",
            "fields": ["body"],
            "query": "machine learning",
        }
    ],
    filter={
        "year": {"$gte": 2024},
        "body": {"$match_phrase": "natural language"},
    },
    include_fields=["title", "body", "category", "year"],
)

for match in response.matches:
    print(match._id, match._score, getattr(match, "title", ""))
```

What each piece does:

* **`SchemaBuilder().add_string_field(..., full_text_search={"language": "en"})`** declares a BM25-indexed text field. Without `full_text_search`, the `string` field would be rejected at index creation — schemas only declare ranking fields.
* **`index.documents.upsert(...)`** writes plain JSON documents. Schema fields are validated; non-schema fields (`category`, `year` here) are stored and auto-indexed for filtering. For large datasets, use [Import](/guides/index-data/import-data) instead.
* **`score_by=[{"type": "text", ...}]`** picks BM25 as the scoring type. One scoring type per request; combine scoring with text matching via `filter` rather than mixing scoring methods.
* **`filter`** narrows candidates *before* ranking. Standard operators (`$eq`, `$gte`, etc.) apply to any metadata field; the text-match operators (`$match_phrase`, `$match_all`, `$match_any`) only apply to FTS-enabled `string` fields.
* **`_score`** is the system-owned relevance score. A user metadata field named `score` would be returned alongside, untouched.

## Filters vs. scoring

Filters are deterministic — each document either matches or it doesn't — and they apply before scoring. Scoring methods (`text`/BM25, `query_string`/Lucene, `dense_vector`, `sparse_vector`) order whatever remains after filtering, and only the top `top_k` hits are returned (max 10,000).

When you're combining text matching with vector ranking, start with the hard yes/no constraints as filters (including the text-match operators `$match_phrase`, `$match_all`, `$match_any` on FTS-enabled `string` fields), then pick a `score_by` method to rank whatever remains. Use BM25 (`score_by` `text` or `query_string`) when keyword and phrase ranking *order* matters, not just inclusion.

## Schema definition

The schema is required at [index creation](/guides/index-data/create-an-index) and declares the fields that drive ranking or vector search. Filterable metadata is not declared in the schema: any field you upsert that isn't in the schema is automatically stored and indexed for filtering.

### Schema field types

| Type            | Purpose                                                                                                             | Key options                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `dense_vector`  | ANN similarity search                                                                                               | `dimension` (required), `metric` (`cosine`, `dotproduct`, `euclidean`)                 |
| `sparse_vector` | Sparse-vector similarity search with values from a custom sparse encoder                                            | None                                                                                   |
| `string` (text) | Full-text search. Set `full_text_search` to enable BM25, for example, `{ "language": "en" }`, or `{}` for defaults. | `language`, `stemming`, `stop_words`, `ngram` (all optional, under `full_text_search`) |

<Note>
  Schemas can only declare ranking fields. Declaring a metadata-only field (a `string` field without `full_text_search`, or a `string_list`, `float`, or `boolean` field) is rejected at index creation with a 400 error. Metadata fields are auto-indexed at upsert time. See [Metadata fields](#metadata-fields).
</Note>

Field names must be unique, non-empty strings, and must not start with `_` or `$`. The `_` prefix is reserved for system-managed fields (for example, `_id`, `_score`); `$` is reserved for filter operators. Field names are also limited to 64 bytes. Every document has a required `_id` field, which carries its unique identifier. A user metadata field named `score` is allowed, and match scores are returned as `_score` to avoid collisions.

<Note>
  Indexes with document schemas do not support integrated inference fields such as `semantic_text`. To use dense or sparse vector ranking in an index with a document schema, declare a `dense_vector` or `sparse_vector` field and provide vector values at upsert time.
</Note>

<Note>
  A `string` field with `full_text_search` isn't metadata and doesn't count toward the 40 KB metadata limit for documents. Use these FTS-enabled `string` fields for searchable chunk text. Indexes with document schemas do not support combining integrated inference fields, such as `semantic_text` fields, with full-text-search fields. To combine semantic ranking with full-text search, declare a `dense_vector` field alongside one or more FTS-enabled `string` fields and provide dense vector values when you upsert documents.
</Note>

### Example schemas

A text-only schema. The minimal `{}` config enables FTS with all defaults; sub-fields like `language`, `stemming`, and `stop_words` are optional overrides:

```json theme={null}
{
  "name": "articles",
  "deployment": {
    "deployment_type": "managed",
    "cloud": "aws",
    "region": "us-east-1"
  },
  "schema": {
    "fields": {
      "title": {
        "type": "string",
        "full_text_search": { "language": "en" }
      },
      "body": {
        "type": "string",
        "description": "The main body text of the article",
        "full_text_search": {
          "language": "en",
          "stemming": true,
          "stop_words": true
        }
      }
    }
  }
}
```

<Note>
  Including `full_text_search`, even an empty object `{}`, is what turns full-text search on for a `string` field. Without it, the field is rejected at index creation, because schemas only declare ranking fields.
</Note>

A multi-field schema with text, dense, and sparse vectors:

```json theme={null}
{
  "name": "articles-hybrid",
  "deployment": {
    "deployment_type": "managed",
    "cloud": "aws",
    "region": "us-east-1"
  },
  "schema": {
    "fields": {
      "title": {
        "type": "string",
        "full_text_search": { "language": "en" }
      },
      "body": {
        "type": "string",
        "full_text_search": { "language": "en" }
      },
      "embedding": {
        "type": "dense_vector",
        "dimension": 1536,
        "metric": "cosine"
      },
      "sparse_embedding": {
        "type": "sparse_vector"
      }
    }
  }
}
```

Documents upserted into either schema can carry additional fields, for example, `category` (string), `tags` (array of strings), `year` (number), or `in_stock` (boolean). These fields are stored on the document, returned via `include_fields`, and automatically indexed for filtering. They do not need to be declared in the schema.

### Metadata fields

Metadata fields are **not declared in the schema**. Any field you include on an upserted document that is not declared in the schema is treated as metadata: it is stored on the document, returned via `include_fields`, and automatically indexed for filtering with the standard operators (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`, `$exists`, `$and`, `$or`, `$not`).

Metadata field types are inferred from the values you upsert: strings, numbers (stored as floating point), booleans, and arrays of strings are all supported. You can mix metadata field types across documents in the same index.

<Warning>
  Schema migration is not yet supported. Once an index is created, you cannot add, remove, or modify fields. Plan your schema carefully.
</Warning>

## Schema validation

Documents are validated against the index schema on upsert. If any document is invalid, the entire upsert fails and nothing is written. For the validation rules, see [Schema validation](/guides/index-data/data-modeling#schema-validation).

## Filter operators

Filters are applied *before* the search runs, so the search only considers documents that match. On document indexes, a filter can use the comparison and set operators (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`, `$exists`), the logical operators `$and`, `$or`, and `$not`, and the [text-match operators](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) on FTS-enabled `string` fields. Multiple fields at the top level of a `filter` object combine with implicit AND. For operator details and examples, see [Filter by metadata](/guides/search/filter-by-metadata).

## Search examples

These examples combine `score_by` scoring with `filter` narrowing on a document index.

### Token matching with a filter

```bash theme={null}
curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
  -H "Api-Key: {{YOUR_API_KEY}}" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "include_fields": ["title", "body", "category", "year"],
    "filter": {
      "category": { "$eq": "technology" },
      "year": { "$gte": 2024 }
    },
    "score_by": [{
      "type": "text",
      "fields": ["body"],
      "query": "machine learning"
    }],
    "top_k": 10
  }'
```

### Cross-field boolean query (query\_string)

```bash theme={null}
curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
  -H "Api-Key: {{YOUR_API_KEY}}" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "include_fields": ["title", "body"],
    "score_by": [{
      "type": "query_string",
      "query": "title:(quantum) OR body:(machine learning)"
    }],
    "top_k": 10
  }'
```

### Dense ranking with a phrase-match filter

```bash theme={null}
curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
  -H "Api-Key: {{YOUR_API_KEY}}" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "include_fields": ["title", "body"],
    "filter": { "body": { "$match_phrase": "machine learning" } },
    "score_by": [{
      "type": "dense_vector",
      "fields": ["embedding"],
      "values": [0.12, 0.34, 0.56]
    }],
    "top_k": 10
  }'
```

### BM25 ranking with a text-match filter

```bash theme={null}
curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
  -H "Api-Key: {{YOUR_API_KEY}}" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "include_fields": ["body", "category", "year"],
    "filter": {
      "$and": [
        { "body": { "$match_all": "federal reserve" } },
        { "category": { "$eq": "finance" } }
      ]
    },
    "score_by": [{
      "type": "text",
      "fields": ["body"],
      "query": "monetary policy impact"
    }],
    "top_k": 10
  }'
```

This restricts the candidate set to finance articles whose `body` contains both "federal" and "reserve", then ranks those candidates by BM25 score against "monetary policy impact".

### Phrase filter with negation

```bash theme={null}
curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
  -H "Api-Key: {{YOUR_API_KEY}}" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "include_fields": ["body", "category"],
    "filter": {
      "$and": [
        { "body": { "$match_phrase": "large language model" } },
        { "body": { "$not": { "$match_any": "spam advertisement" } } }
      ]
    },
    "score_by": [{
      "type": "text",
      "fields": ["body"],
      "query": "recent advances in generative AI"
    }],
    "top_k": 10
  }'
```

This requires the exact phrase "large language model" and excludes documents containing "spam" or "advertisement".

For the full request and response schema, see [Search documents](/reference/api/latest/data-plane/search_documents).

## Troubleshooting

<AccordionGroup>
  <Accordion title="Document not appearing in search results">
    * Check indexing latency: new documents may take up to 1 minute to become searchable; schemas with multiple indexed fields may take slightly longer.
    * Verify the upsert response shows the expected `upserted_count`.
    * Confirm you're searching the same namespace where you upserted.
    * With `type: "text"`, multi-word queries use **token OR** matching — documents need not contain the full phrase. Try a single-term query first to confirm the document is searchable.
    * If using filters, ensure the document's field values match your filter conditions. Metadata fields are auto-indexed at upsert time, so any field present on a document can be filtered on; filtering on a field that no document contains returns no results.
  </Accordion>

  <Accordion title="Unexpected search results">
    * **`type: "text"` uses OR across terms.** `machine learning` matches documents that contain "machine", "learning", or both (BM25 ranking). For an **exact phrase**, use `type: "query_string"` with `body:("machine learning")` or a `$match_phrase` filter.
    * **`type: "query_string"` defaults to OR for unquoted terms.** `body:(machine learning)` matches documents containing either term. Use `AND` or `+` for required terms.
    * Operators like `AND`, `OR`, `NOT`, `*`, `~`, and `^` only work with `type: "query_string"`. With `type: "text"`, they are treated as literal words.
  </Accordion>

  <Accordion title="Query syntax errors">
    Query syntax errors only apply to `type: "query_string"`. With `type: "text"`, any input is valid as a literal string to be tokenized.

    * Unmatched quotes (`"machine learning`): Close all quotes.
    * Empty query: Provide at least one search term.
    * Invalid boolean syntax (`AND machine`): Operators need terms on both sides.
    * Unbalanced parentheses: Match all opening and closing parens.
    * Unknown field name: Field names in the query must match text-searchable fields in the schema.
  </Accordion>

  <Accordion title="API errors">
    * `401 Unauthorized`: Check the `Api-Key` header.
    * `400 Bad Request`: Check JSON syntax and required fields. Examples: `fields` array with more than one element for `dense_vector`/`sparse_vector`; missing mutually-exclusive field for Fetch/Delete.
    * `404 Not Found`: Verify the index name and host URL.
    * Missing API version: Add `X-Pinecone-Api-Version: 2026-07`.
  </Accordion>

  <Accordion title="Upsert errors">
    * Type mismatch: Ensure values match declared schema types.
    * Invalid `_id`: Every document must have a non-empty `_id` string.
    * Reserved names: Field names cannot start with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators), and must be at most 64 bytes.
  </Accordion>

  <Accordion title="Slow search performance">
    * Reduce query complexity: Boolean operators and large phrase slop are more expensive than simple term queries.
    * Simplify filters: Filters are applied before scoring, so broad filters increase the search space.
    * For cost-sensitive workloads, use `read_capacity.mode: "Dedicated"` to get predictable latency.
  </Accordion>

  <Accordion title="Common request-shape pitfalls">
    When a request is rejected with a 4xx that doesn't seem to match your intent, the cause is usually one of these:

    * **Sparse-vector `score_by` clauses use `sparse_values`, not `values`.** The `values` key is for `dense_vector`. A sparse clause needs the full object: `"sparse_values": { "indices": [...], "values": [...] }`.

    * **Every `score_by` clause must include `type`.** It's the discriminator that selects the scoring method (`text`, `query_string`, `dense_vector`, `sparse_vector`). Omitting it returns a 400.

    * **Every document must have a non-empty `_id` string.** There is no default; the upsert request fails if any document in the batch is missing `_id` or has an empty value.

    * **Wait for `status.ready: true` before searching.** A newly created index can briefly return empty results. For `Dedicated` read capacity, also wait for `read_capacity.status.state: "Ready"`.

    * **The match-score response field is `_score`, not `score`.** A user metadata field named `score` is allowed and is returned alongside the system-owned `_score`.

    * **Namespace is part of the URL path.** Use `__default__` (the literal string) if you don't need partitioning. An empty path segment is rejected.

    * **`dense_vector` queries use `values`, not `query`.** Only `text` and `query_string` clauses use `query` (a string). `dense_vector` and `sparse_vector` use `values` (a float array) and `sparse_values` (an `{indices, values}` object) respectively.
  </Accordion>
</AccordionGroup>

## Requirements and limitations

* All requests require `X-Pinecone-Api-Version: 2026-07`.
* The REST API, Python SDK (`pinecone`), and Pinecone console are the supported entry points.
* **Endpoint compatibility**: indexes with document schemas use the `/namespaces/{namespace}/documents/*` endpoints; dense, sparse, and integrated-inference indexes continue to use `/vectors/*` (and `/records/*` for integrated inference). The two endpoint families are index-type-specific and don't cross over.
* Supported deployment modes: managed (serverless) with `read_capacity.mode` of `OnDemand` or `Dedicated`.
* Changing an index from dedicated read capacity back to on-demand read capacity is not supported. To move from dedicated read capacity to on-demand, create a new on-demand index and reingest your data.
* Schemas declare ranking fields only: text fields (`string` with `full_text_search`), `dense_vector`, and `sparse_vector`. Text-only, text + dense vector, and combined dense + sparse + text schemas are all supported in a single index. Metadata-only field declarations (`string` without `full_text_search`, `string_list`, `float`, `boolean`) are rejected at index creation; metadata is auto-indexed at upsert time.
* **Schema and document limits**: a schema can contain up to 100 `full_text_search` string fields; each `full_text_search` string field can be up to 100 KB and 10,000 tokens; tokens can be up to 256 bytes before analyzer truncation; each document can be up to 2 MB; each upsert request can contain up to 1000 documents and 2 MB.
* **Metadata size**: metadata fields on a document (everything outside FTS-enabled `string` fields) are limited to 40 KB per document in total. This limit does not apply to `full_text_search` text fields.
* **Vector-field cardinality**: a schema can declare up to 100 `string` fields with `full_text_search` enabled, but at most one `dense_vector` field and at most one `sparse_vector` field per index.
* **Field-name policy**: schema and metadata field names must not start with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators), and are limited to 64 bytes.
* The match-score response field is `_score` (renamed from `score` so that user metadata named `score` can coexist with the system-owned match score in the flat response payload).
* **A single search request ranks by one scoring type.** Multi-field BM25 is supported: name several fields in one `text` clause, or pass multiple `text` clauses, which the server combines into one ranking; a `query_string` clause can also target several fields. Every contributing field weighs equally in `2026-07`; there is no per-field weight parameter. To combine BM25 ranking with `dense_vector` or `sparse_vector` ranking, restrict the dense (or sparse) search with a text-match filter (`$match_phrase`, `$match_all`, `$match_any`) on the full-text field, or run separate searches and merge the results client-side.
* Newly upserted documents are indexed asynchronously and may not be searchable immediately.
* **Partial updates**: `POST /namespaces/{namespace}/documents/upsert` replaces the entire document for a given `_id`. For field-level changes, use `POST /namespaces/{namespace}/documents/update`, which patches only the fields you specify (removing others with `_remove_fields`) per ID, or applies the same patch in bulk to every document matching a metadata `filter` (with `set_fields` / `remove_fields`), leaving unmentioned fields unchanged.
* **Schemas are fixed at index creation.** Adding, removing, or retyping fields after creation is not yet supported. Existing indexes created before `2026-07` cannot be backfilled with a schema. To use FTS, dense + FTS, or any Documents API query in `2026-07`, create a new index with the desired schema and reindex documents.
* **Metadata is auto-indexed**: any field on an upserted document that is not declared in the schema is automatically indexed for filtering. The schema declares only ranking fields (FTS-enabled `string`, `dense_vector`, `sparse_vector`); declaring metadata-only fields (`string` without `full_text_search`, `string_list`, `float`, `boolean`) is rejected at index creation. Track metadata field names and types in your application. Pinecone infers the type from the values you upsert.
* **Bulk import** from object storage is supported for indexes with document schemas via JSONL files, see [Prepare document-schema files (JSONL)](/guides/index-data/import-data#prepare-document-schema-files-jsonl). Semantic-text (auto-embedded) fields are not yet supported in schemas.
* **Maximum results per query**: `top_k` is capped at **10,000**. Full-text search is optimized for ranked retrieval rather than aggregation- or count-style queries.
* Indexes cannot be created in CMEK-enabled projects.
* Backup and restore are not yet supported.
* **`describe_index_stats`** is not yet supported on indexes with document schemas.
* [Fuzzy matching](/guides/search/full-text-search/query-syntax) (`term~`, `term~N`) is available only in `query_string` scoring, not in `type: "text"` or in `$match_*` filters.
* Single-term prefix wildcards (`auto*`) are not supported; use phrase prefix (`"word auto"*`) instead, or configure a field for [substring search](/guides/search/full-text-search/text-processing#substring-search-with-n-grams).

## Pricing

Reads and writes on indexes with document schemas are metered using the same [read units (RUs)](/guides/manage-cost/understanding-cost#read-units) and [write units (WUs)](/guides/manage-cost/understanding-cost#write-units) model as vector indexes.
