---
title: "Full-text search"
source: https://docs.pinecone.io/guides/search/full-text-search
path: guides/search/full-text-search
---

Upsert and search typed JSON documents in Pinecone with BM25 scoring, Lucene query syntax, dense and sparse vector ranking, and metadata filters.

<Note>
  Full-text search is in [public preview](#public-preview). APIs may continue to evolve before general availability.
</Note>

<Tip>
  You can also use the Pinecone console to create indexes with document schemas, upsert documents, search documents, and fetch or delete documents by ID.
</Tip>

Full-text search ranks documents by keyword and phrase relevance using **BM25** scoring, with optional **Lucene** query syntax. Because an index with a document schema can also declare dense and sparse vector fields, the same index can rank by semantic or sparse-vector similarity, so one index can cover keyword and semantic search.

**When to use it.** Reach for full-text search when exact words, phrases, names, codes, or identifiers matter, not just semantic similarity. For semantic-only or vector-only workloads, an [index with dense vectors](/guides/get-started/concepts#index-with-dense-vectors) (the vector API) is simpler; see [Search overview](/guides/search/search-overview) to choose the right approach.

### Capabilities

What full-text search does and doesn't match:

| Capability                      | Status                                                                                                                                                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fuzzy matching (typo tolerance) | Supported in `query_string` queries only ([query syntax](#query-syntax-reference))                                                                                                                                         |
| Stemming                        | Supported, opt-in per field at index creation ([stemming](#stemming))                                                                                                                                                      |
| Stop-word removal               | Supported, opt-in per field at index creation ([tokens & analyzers](#tokens-and-analyzers))                                                                                                                                |
| Substring / n-gram matching     | Supported, opt-in per field at index creation. Can't be combined with stemming or stop words on the same field ([n-grams](#substring-search-with-n-grams))                                                                 |
| Synonym expansion               | Not supported. A search for `car` won't match a document containing only `automobile`. Use [semantic search](/guides/search/semantic-search) or [hybrid search](/guides/search/hybrid-search) for synonyms or paraphrases. |

**The path, end to end.** Create an index with a [schema](#schema-definition) that declares your ranking fields, upsert your data as JSON documents, then search by choosing one ranking signal per search request with `score_by`. The [end-to-end example](#end-to-end-example) below stitches all three steps into one runnable script, and the sections after it cover each operation in detail.

Pinecone's document API stores typed fields you declare in a schema. How it works:

1. You upsert data as JSON **documents**.
2. You declare how each field should be indexed via a **schema** — as a `string` field with `full_text_search` enabled (BM25 scoring), a `dense_vector` field, or a `sparse_vector` field. The schema is for ranking fields only; metadata fields are not declared.
3. Pinecone indexes each field's content according to the type of the field declared in the schema. Any other fields on the upserted documents are automatically stored and indexed for filtering — no schema declaration required.

Supported schema field types:

* **Text fields** (`type: "string"` with a `full_text_search` config object — for example, `{ "language": "en" }`; `{}` is also valid and uses the same defaults) — indexed for BM25 ranking and Lucene queries.
* **Dense vector fields** (`type: "dense_vector"`) — indexed for ANN similarity search.
* **Sparse vector fields** (`type: "sparse_vector"`) — indexed for sparse vector similarity search.

Filterable metadata is not part of the schema. Any field you upsert that is not declared in the schema is stored on the document, returned via `include_fields`, and automatically indexed for filtering — see [Metadata fields](#metadata-fields).

**Every search picks exactly one ranking signal.** The `score_by` clause selects the scoring method for the request:

* `text` — BM25 token matching on a single FTS-enabled `string` field.
* `query_string` — Lucene query syntax across one or more FTS-enabled `string` fields, including cross-field boolean queries.
* `dense_vector` — vector similarity against a `dense_vector` field.
* `sparse_vector` — sparse-vector similarity against a `sparse_vector` field.

The same index can support all four when the schema declares the corresponding fields, but a given request commits to one. To narrow the candidates a vector ranking sees, combine the `score_by` with a metadata filter — including the text-match operators `$match_phrase`, `$match_all`, and `$match_any` on FTS-enabled `string` fields, plus the standard logical and comparison operators (`$and`, `$or`, `$not`, `$exists`, etc.). The filter narrows what's eligible; the `score_by` ranks what remains. This is the most common hybrid pattern.

For example, on an index whose schema declares both a `dense_vector` field (`review_embedding`) and an FTS-enabled `string` field (`review_text`), this single request runs semantic search across the corpus but only over documents whose `review_text` contains the exact phrase "beautifully written":

```python Python theme={null}
index.documents.search(
    namespace="reviews",
    top_k=5,
    score_by=[
        {
            "type": "dense_vector",
            "field": "review_embedding",
            "values": query_embedding,
        }
    ],
    filter={"review_text": {"$match_phrase": "beautifully written"}},
)
```

The dense ranking still controls the order of results; the text-match filter just narrows what's eligible to be ranked.

### End-to-end example

A complete run from index creation through search. Copy this into a single file, set `PINECONE_API_KEY`, and run.

```python Python theme={null}
import os
import time
from pinecone import Pinecone
from pinecone.preview import SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# 1. Create an index. Setting `full_text_search` on a `string` field enables BM25.
schema = (
    SchemaBuilder()
      .add_string_field(name="title", full_text_search={"language": "en"})
      .add_string_field(name="body", full_text_search={"language": "en"})
      .build()
)
pc.preview.indexes.create(name="articles-quickstart", schema=schema)

# Wait for the index to be ready before upserting (no timeout — add a loop cap in production).
while not pc.preview.indexes.describe(name="articles-quickstart").status.ready:
    time.sleep(2)

index = pc.preview.index(name="articles-quickstart")

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
            "field": "body",
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
* **`index.documents.upsert(...)`** writes plain JSON documents. Schema fields are validated; non-schema fields (`category`, `year` here) are stored and auto-indexed for filtering.
* **`score_by=[{"type": "text", ...}]`** picks BM25 as the ranking method. One ranking method per request; combine ranking with text matching via `filter` rather than mixing score methods.
* **`filter`** narrows candidates *before* ranking. Standard operators (`$eq`, `$gte`, etc.) apply to any metadata field; the text-match operators (`$match_phrase`, `$match_all`, `$match_any`) only apply to FTS-enabled `string` fields.
* **`_score`** is the system-owned relevance score. A user metadata field named `score` would be returned alongside, untouched.

The Python SDK reference further down covers every operation individually; the example above stitches the most common path into one runnable script.

### Filters vs. scoring

Filters are deterministic — each document either matches or it doesn't — and they apply before scoring. Scoring methods (`text`/BM25, `query_string`/Lucene, `dense_vector`, `sparse_vector`) order whatever remains after filtering, and only the top `top_k` hits are returned (max 10,000).

When you're combining text matching with vector ranking, start with the hard yes/no constraints as filters (including the text-match operators `$match_phrase`, `$match_all`, `$match_any` on FTS-enabled `string` fields), then pick a `score_by` method to rank whatever remains. Use BM25 (`score_by` `text` or `query_string`) when keyword and phrase ranking *order* matters, not just inclusion.

<Note>
  An index with a document schema can store both `dense_vector` and `sparse_vector` fields, plus one or more `string` fields with `full_text_search` enabled. A single search request scores results with one ranking method at a time: dense vector, sparse vector, BM25 text, or Lucene query syntax. You can still combine vector ranking with full-text keyword matching in one request by using a text-match filter, such as `$match_phrase`, `$match_all`, or `$match_any`. The vector search ranks the matching documents; the full-text filter narrows the set of documents to search.
</Note>

## Schema definition

The schema is required at index creation and declares the fields that drive ranking or vector search. Filterable metadata is not declared in the schema — any field you upsert that is not declared in the schema is automatically stored and indexed for filtering.

**Schema field types:**

| Type            | Purpose                                                                                                              | Key options                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `dense_vector`  | ANN similarity search                                                                                                | `dimension` (required), `metric` (`cosine`, `dotproduct`, `euclidean`)                 |
| `sparse_vector` | Sparse-vector similarity search with values from a custom sparse encoder                                             | —                                                                                      |
| `string` (text) | Full-text search. Set `full_text_search` to enable BM25 — for example, `{ "language": "en" }`, or `{}` for defaults. | `language`, `stemming`, `stop_words`, `ngram` (all optional, under `full_text_search`) |

<Note>
  Schemas can only declare ranking fields. Declaring a metadata-only field (a `string` field without `full_text_search`, or a `string_list`, `float`, or `boolean` field) is rejected at index creation with a 400 error. Metadata fields are auto-indexed at upsert time. See [Metadata fields](#metadata-fields).
</Note>

**Reserved names.** Field names must be unique, non-empty strings, and **must not start with `_` or `$`**. The `_` prefix is reserved for system-managed fields (for example, `_id`, `_score`); `$` is reserved for filter operators. Field names are also limited to **64 bytes**. Every document has a required `_id` field, which carries its unique identifier. A user metadata field named `score` is allowed — match scores are returned as `_score` to avoid collisions.

<Note>
  In public preview, indexes with document schemas do not support integrated inference fields such as `semantic_text`. To use dense or sparse vector ranking in an index with a document schema, declare a `dense_vector` or `sparse_vector` field and provide vector values at upsert time.
</Note>

<Note>
  A `string` field with `full_text_search` is not metadata and does not count toward the 40 KB metadata limit for records. Use these FTS-enabled `string` fields for searchable chunk text. In public preview, indexes with document schemas do not support combining integrated inference fields, such as `semantic_text` fields, with full-text-search fields. To combine semantic ranking with full-text search, declare a `dense_vector` field alongside one or more FTS-enabled `string` fields and provide dense vector values when you upsert documents.
</Note>

**Example: text-only schema** (minimal `{}` enables FTS with all defaults; sub-fields like `language`, `stemming`, and `stop_words` are optional overrides)

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

**Example: text + dense + sparse vector (multi-field) schema**

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

Documents upserted into either schema can carry additional fields — for example, `category` (string), `tags` (array of strings), `year` (number), or `in_stock` (boolean). These fields are stored on the document, returned via `include_fields`, and automatically indexed for filtering. They do not need to be declared in the schema.

### Metadata fields

Metadata fields are **not declared in the schema**. Any field you include on an upserted document that is not declared in the schema is treated as metadata: it is stored on the document, returned via `include_fields`, and automatically indexed for filtering with the standard operators (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`, `$exists`, `$and`, `$or`, `$not`).

Metadata field types are inferred from the values you upsert: strings, numbers (stored as floating point), booleans, and arrays of strings are all supported. You can mix metadata field types across documents in the same index.

<Warning>
  Schema migration is not yet supported. Once an index is created, you cannot add, remove, or modify fields. Plan your schema carefully.
</Warning>

## API and SDK reference

Full-text search uses API version `2026-01.alpha`. All requests require the header `X-Pinecone-Api-Version: 2026-01.alpha`.

The endpoints below are split into control-plane operations (project-scoped, authenticated against `api.pinecone.io`) and data-plane operations (index-scoped, authenticated against the per-index `INDEX_HOST.svc.<region>.pinecone.io` host returned by `DescribeIndex`). The preview SDK reflects the same split: `pc.preview.*` for control-plane FTS operations and `pc.preview.index(...).documents.*` for data-plane document operations.

### Control plane operations

Control plane operations manage indexes and their configuration.

<AccordionGroup>
  <Accordion title="Create index (POST /indexes)">
    Creates a new index with the provided schema. The index initializes asynchronously; poll the describe endpoint to know when it's ready for data operations.

    **Example request — on-demand read capacity (default)**

    ```bash theme={null}
    curl -X POST "https://api.pinecone.io/indexes" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
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
              "full_text_search": { "language": "en" }
            }
          }
        },
        "read_capacity": { "mode": "OnDemand" },
        "deletion_protection": "disabled"
      }'
    ```

    **Example request — dedicated read capacity**

    ```bash theme={null}
    curl -X POST "https://api.pinecone.io/indexes" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "name": "articles-dedicated",
        "deployment": {
          "deployment_type": "managed",
          "cloud": "aws",
          "region": "us-east-1"
        },
        "schema": {
          "fields": {
            "content": {
              "type": "string",
              "full_text_search": { "language": "en" }
            }
          }
        },
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": { "shards": 1, "replicas": 1 }
          }
        },
        "deletion_protection": "disabled"
      }'
    ```

    Request parameters:

    * `name` (string, optional) - Unique index name (lowercase alphanumeric and hyphens, 1-45 characters). Auto-generated if omitted.
    * `deployment` (object, optional) - Deployment configuration. Defaults to `managed` on AWS `us-east-1` if omitted.
      * `deployment_type` (string) - `"managed"` for serverless, `"pod"` for pod-based, `"byoc"` for bring-your-own-cloud.
      * For `managed`: `cloud` (`"aws"` | `"gcp"` | `"azure"`), `region` (e.g., `"us-east-1"`).
    * `schema` (object, required) - Schema definition. See [Schema definition](#schema-definition) for all supported field types. Each field in `schema.fields` uses the `type` discriminator to select its configuration:

      * `dense_vector`: `dimension` (required), `metric` (required, one of `cosine`, `dotproduct`, `euclidean`).
      * `sparse_vector`: no additional options.
      * `string` (text): `full_text_search: { ... }` (object); optional sub-fields `language`, `stemming`, `stop_words`, and `ngram` (`{ min_gram, max_gram, prefix_only }`, for [substring search](#substring-search-with-n-grams)).
      * Any field may also include an optional `description` (string) — free-text documentation of what the field contains. It's stored on the schema and returned by describe-index, and is especially useful for agentic workflows where an LLM inspects the schema to decide how to query the index.

      Metadata-only fields (`string` without `full_text_search`, `string_list`, `float`, `boolean`) are not allowed in the schema and are rejected at index creation. Metadata fields are auto-indexed for filtering at upsert time — see [Metadata fields](#metadata-fields).
    * `read_capacity` (object, optional) - Read capacity for serverless (managed) indexes:
      * `mode: "OnDemand"` — default; auto-scaled shared read capacity.
      * `mode: "Dedicated"` — provisioned read nodes. Requires a `dedicated` block with `node_type`, `scaling`, and (for `Manual` scaling) `manual: { shards, replicas }`.
    * `deletion_protection` (string, optional) - `"enabled"` or `"disabled"` (default: `"disabled"`).
    * `tags` (object, optional) - Key-value tags for the index.

    **Schema constraints:**

    * Field names must be unique within the schema.
    * Field names must contain only alphanumeric characters and underscores, must not start with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators), and must be at most 64 bytes.
    * The schema must contain at least one field.

    **Example response**

    **Status:** 201 Created

    ```json theme={null}
    {
      "id": "e51ea4e1-2dda-4607-94dc-9054b1fa8492",
      "name": "articles",
      "host": "articles-jweaq8m.svc.aped-4627-b74a.pinecone.io",
      "status": {
        "ready": false,
        "state": "Initializing"
      },
      "deployment": {
        "deployment_type": "managed",
        "cloud": "aws",
        "region": "us-east-1",
        "environment": "aped-4627-b74a"
      },
      "schema": {
        "version": "v1",
        "fields": {
          "title": {
            "type": "string",
            "description": null,
            "full_text_search": {
              "language": "en",
              "stemming": false,
              "stop_words": false,
              "lowercase": true,
              "max_token_length": 40
            }
          },
          "body": {
            "type": "string",
            "description": null,
            "full_text_search": {
              "language": "en",
              "stemming": false,
              "stop_words": false,
              "lowercase": true,
              "max_token_length": 40
            }
          }
        }
      },
      "read_capacity": {
        "mode": "OnDemand",
        "status": { "state": "Ready" }
      },
      "tags": null,
      "deletion_protection": "disabled"
    }
    ```

    The response shows fields with **server-applied defaults**. Each FTS-enabled field's `full_text_search` block returns the full resolved analyzer config: the settable subset (`language`, `stemming`, `stop_words`) reflects what was passed at index creation (or its default when omitted), and `lowercase` and `max_token_length` are server-applied defaults that aren't settable from the request. All fields include `description` (`null` if not supplied at creation).

    Wait for `status.ready: true` before performing data plane operations. For `Dedicated` read capacity, also wait for `read_capacity.status.state: "Ready"`.

    Response fields:

    * `id` (string) — Unique index ID.
    * `name` (string) — Index name.
    * `host` (string) — Per-index host URL for data-plane operations (`INDEX_HOST.svc.<region>.pinecone.io`).
    * `status` (object) — Provisioning status.
      * `ready` (boolean) — Whether the index is ready for data-plane operations.
      * `state` (string) — Current state, e.g., `"Initializing"`, `"Ready"`.
    * `deployment` (object) — Resolved deployment configuration.
      * `deployment_type` (string) — e.g., `"managed"`.
      * `cloud` (string) — Cloud provider.
      * `region` (string) — Region code.
      * `environment` (string) — Environment identifier assigned by the system.
    * `schema` (object) — Resolved schema with server-applied defaults.
      * `version` (string) — Schema version, e.g., `"v1"`.
      * `fields` (object) — Map of field name → resolved field definition. See note above on `full_text_search` server-applied defaults.
    * `read_capacity` (object) — Resolved read capacity configuration.
      * `mode` (string) — `"OnDemand"` or `"Dedicated"`.
      * `dedicated` (object, present when `mode: "Dedicated"`) — Dedicated read-node configuration: `node_type`, `scaling`, and (for `Manual` scaling) `manual.{ shards, replicas }`.
      * `status` (object) — Read-capacity provisioning status.
        * `state` (string) — e.g., `"Migrating"`, `"Ready"`.
        * `current_shards` (integer or null, `Dedicated` only) — Current number of provisioned shards.
        * `current_replicas` (integer or null, `Dedicated` only) — Current number of provisioned replicas.
    * `tags` (object or null) — Key-value tags, or `null` if none.
    * `deletion_protection` (string) — `"enabled"` or `"disabled"`.
  </Accordion>

  <Accordion title="List indexes (GET /indexes)">
    Returns all indexes in the project, including their current status and configuration.

    ```bash theme={null}
    curl -X GET "https://api.pinecone.io/indexes" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha"
    ```

    **Status:** 200 OK. Returns an array of index objects, each with the same structure as the create-index response.
  </Accordion>

  <Accordion title="Describe index (GET /indexes/{index_name})">
    Returns detailed information about a specific index, including its schema, status, and host URL.

    ```bash theme={null}
    curl -X GET "https://api.pinecone.io/indexes/articles" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha"
    ```

    **Status:** 200 OK. Returns the same structure as the create-index response.
  </Accordion>

  <Accordion title="Update index (PATCH /indexes/{index_name})">
    Updates index configuration. Currently, only `deletion_protection` can be updated.

    ```bash theme={null}
    curl -X PATCH "https://api.pinecone.io/indexes/articles" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{ "deletion_protection": "enabled" }'
    ```

    **Status:** 200 OK. Returns the updated index configuration.
  </Accordion>

  <Accordion title="Delete index (DELETE /indexes/{index_name})">
    Permanently deletes an index and all its data. If `deletion_protection` is enabled, you must first disable it using the update endpoint.

    ```bash theme={null}
    curl -X DELETE "https://api.pinecone.io/indexes/articles" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha"
    ```

    **Status:** 202 Accepted (empty body).
  </Accordion>
</AccordionGroup>

### Data plane operations

<Note>
  Data plane operations include a namespace in the URL path. Namespaces partition documents within an index: they're auto-created on first upsert and completely isolated from each other. Use `"__default__"` if you don't need partitioning. If your documents are in another namespace, search, fetch, and delete requests must target that namespace.
</Note>

<AccordionGroup>
  <Accordion title="Upsert documents (POST /namespaces/{namespace}/documents/upsert)">
    Inserts or updates documents. If a document with the same `_id` exists, it is completely replaced. Documents are indexed asynchronously and may not be searchable immediately after upsert.

    **Example request**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/upsert" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
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

    Path parameters:

    * `namespace` (string, required) - Namespace name (use `"__default__"` if not using namespaces).

    Body parameters:

    * `documents` (array, required, 1-1000 items) - Array of documents to upsert. Each document is an object with:
      * `_id` (string, required) - Unique document ID. If a document with this `_id` already exists, it is replaced entirely. If multiple documents in the same batch share an `_id`, only the last one is stored.
      * Fields matching your schema. Additional fields are stored on the document and auto-indexed for filtering as metadata. Names starting with `_` or `$` are rejected.

    Limits:

    * Each upsert request can contain up to 1000 documents and must be no larger than 2 MB.
    * Each document can be no larger than 2 MB.
    * Each `full_text_search` string field can be no larger than 100 KB and can contain up to 10,000 tokens.
    * Each token can be no larger than 256 bytes before analyzer truncation.
    * Metadata fields on a document (everything outside FTS-enabled `string` fields) are limited to 40 KB per document in total. This metadata limit does not apply to `full_text_search` text fields.

    **Example response**

    **Status:** 202 Accepted

    ```json theme={null}
    {
      "upserted_count": 3
    }
    ```

    Response fields:

    * `upserted_count` (integer) - Number of documents accepted for upsert.

    #### Schema validation

    Each item in the `documents` array is validated against your index schema. If any item fails validation, **the entire request fails** and nothing is upserted.

    | Scenario                                                             | Result                                                            |
    | -------------------------------------------------------------------- | ----------------------------------------------------------------- |
    | Field value doesn't match declared type (for schema-declared fields) | **Error** — request fails                                         |
    | Document or request exceeds a size or count limit                    | **Error** — request fails                                         |
    | Field not in schema                                                  | Stored on the document and auto-indexed for filtering as metadata |
    | Field name starts with `_` or `$`                                    | **Error** — request fails                                         |
    | Schema field missing from item                                       | OK — schema fields are optional unless stated otherwise           |
    | Document missing `_id`                                               | **Error** — request fails                                         |
  </Accordion>

  <Accordion title="Search documents (POST /namespaces/{namespace}/documents/search)">
    Searches documents using any one of four scoring methods: BM25 token matching (`text`), Lucene query syntax (`query_string`), dense vector similarity (`dense_vector`), or sparse vector similarity (`sparse_vector`). Optionally filter by field values before scoring.

    <Tip>
      To populate an initial view before a user enters a query, use `query_string` with `query: "*"`. This returns `top_k` documents in an arbitrary order; it is not relevance-ranked keyword search.
    </Tip>

    **Example request**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "include_fields": ["title", "body", "category", "year"],
        "score_by": [{
          "type": "text",
          "field": "body",
          "query": "machine learning"
        }],
        "top_k": 10
      }'
    ```

    Path parameters:

    * `namespace` (string, required) - Namespace name (use `"__default__"` if not using namespaces).

    Body parameters:

    * `include_fields` (array, optional) - List of field names to return in results. Defaults to `[]` if omitted (or `null`); each match then returns only `_id` and `_score` with no stored fields. Use `["*"]` to return all stored fields (including fields not declared in the schema). User metadata fields named `score` are returned alongside the system-owned `_score` match score.
    * `score_by` (array, required) - Array of scoring methods. A single search request ranks by one scoring type. Multi-field BM25 is supported: pass several `text` clauses (one per field) or use a single `query_string` clause whose query targets multiple fields, and every contributing field weighs equally; there is no per-clause weight parameter. To combine BM25 ranking with `dense_vector` or `sparse_vector` ranking, restrict the dense (or sparse) search with a text-match filter on the lexical field (`$match_phrase`, `$match_all`, `$match_any`) or run separate searches and merge results client-side. Each item must be one of:
      * **`type: "text"`** — BM25 token matching on a single text field. Multi-word queries use OR-style matching (case-insensitive). Phrase constraints are not supported here; use `query_string` with quoted terms for exact-phrase ranking.
        * `field` (string, required) — Name of a text-searchable field.
        * `query` (string, required) — One or more words to search for.
      * **`type: "query_string"`** — Lucene query syntax. Supports boolean operators, phrase prefix matching, boosting, fuzzy matching (`term~`, `term~N`), and cross-field queries.

        * `query` (string, required) — A Lucene query string (see [query syntax reference](#query-syntax-reference)). Target a specific field with Lucene field qualifiers directly in the query string: `notes:friendship`, or combine fields with boolean operators: `title:(alpha) OR body:(beta)`. The query runs against all text-searchable fields in the index when no field qualifier is specified.

        <Warning>
          `query_string` does not accept a `field` or `fields` parameter. Passing either returns a `400` error. Use Lucene field qualifiers in the query string itself to target specific fields: `fieldname:value` or `fieldname:(multi word value)`.
        </Warning>
      * **`type: "dense_vector"`** — Dense vector similarity ranking. Requires a `dense_vector` field in the schema.
        * `field` (string, required) — Name of the dense-vector field to score against.
        * `values` (array of floats, required) — Query vector.
      * **`type: "sparse_vector"`** — Sparse vector similarity ranking. Requires a `sparse_vector` field in the schema.
        * `field` (string, required) — Name of the sparse-vector field to score against.
        * `sparse_values` (object, required) — `{ "indices": [...], "values": [...] }`.
    * `top_k` (integer, required) - Number of results to return (1-10000).
    * `filter` (object, optional) - Filter conditions applied before scoring. Filter on any metadata field on your documents (auto-indexed at upsert time) or use the text match operators (`$match_phrase`, `$match_all`, `$match_any`) on FTS-enabled `string` fields. Supports the filter operators below.

    **Search limits:**

    | Limit                        | Value  | Description                                                                    |
    | ---------------------------- | ------ | ------------------------------------------------------------------------------ |
    | Max `score_by` clauses       | 100    | Maximum number of clauses in the `score_by` array                              |
    | Max total `score_by` payload | 100 KB | Maximum encoded size of all `score_by` clauses combined                        |
    | Max per-clause query size    | 10 KB  | Maximum size of the `query` string in a single `text` or `query_string` clause |

    #### Filter operators

    Filters are applied *before* the search runs. The search only considers documents that match the filter.

    | Operator        | Example                                                                 | Description                                                                                          |
    | --------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `$eq`           | `{"category": {"$eq": "tech"}}`                                         | Equals                                                                                               |
    | `$ne`           | `{"category": {"$ne": "tech"}}`                                         | Not equals                                                                                           |
    | `$gt`           | `{"year": {"$gt": 2023}}`                                               | Greater than                                                                                         |
    | `$gte`          | `{"year": {"$gte": 2023}}`                                              | Greater than or equal                                                                                |
    | `$lt`           | `{"year": {"$lt": 2025}}`                                               | Less than                                                                                            |
    | `$lte`          | `{"year": {"$lte": 2025}}`                                              | Less than or equal                                                                                   |
    | `$in`           | `{"category": {"$in": ["a", "b"]}}`                                     | In list                                                                                              |
    | `$nin`          | `{"category": {"$nin": ["a", "b"]}}`                                    | Not in list                                                                                          |
    | `$exists`       | `{"category": {"$exists": true}}`                                       | Field has a value (`true`) or is absent (`false`).                                                   |
    | `$match_phrase` | `{"body": {"$match_phrase": "machine learning"}}`                       | Exact phrase match (contiguous tokens) on a text-searchable field. Compose with any `score_by` type. |
    | `$match_all`    | `{"body": {"$match_all": "machine learning"}}`                          | All tokens present, in any order, on a text-searchable field.                                        |
    | `$match_any`    | `{"body": {"$match_any": "AI robotics"}}`                               | At least one token present, on a text-searchable field.                                              |
    | `$and`          | `{"$and": [{"category": {"$eq": "tech"}}, {"year": {"$gte": 2024}}]}`   | Logical AND of the listed clauses.                                                                   |
    | `$or`           | `{"$or": [{"category": {"$eq": "tech"}}, {"category": {"$eq": "ai"}}]}` | Logical OR of the listed clauses.                                                                    |
    | `$not`          | `{"$not": {"category": {"$eq": "archive"}}}`                            | Negation of the wrapped clause.                                                                      |

    By default, multiple fields at the top level of a `filter` object are combined with implicit AND semantics. Use `$and`, `$or`, and `$not` to build explicit compound conditions (they can nest).

    The text match operators (`$match_phrase`, `$match_all`, `$match_any`) share a few rules:

    * **Where they apply.** Fields declared with a `full_text_search` config object.
    * **Tokenization.** They reuse the field's configured tokenizer and stemmer — a token that matches in BM25 scoring will match in a text match filter.
    * **Value limit.** Each operator accepts at most **128 tokens** in its value.
    * **Lucene-style operators.** Phrase slop (`"phrase"~N`), term boosting (`^N`), and phrase prefix (`"phrase pre"*`) are not parsed — values are literal text and match semantics come from the operator name. To use those operators, score with `query_string`.
    * **Composition.** They compose freely with metadata operators under `$and`, `$or`, and `$not` at any nesting level:

    ```json theme={null}
    {
      "$and": [
        { "body": { "$match_all": "federal reserve" } },
        { "category": { "$eq": "finance" } },
        { "year": { "$gte": 2024 } }
      ]
    }
    ```

    <Warning>
      Filters, including text match operators (`$match_phrase`, `$match_all`, `$match_any`), are only valid on `POST /namespaces/{namespace}/documents/search`. The `POST /namespaces/{namespace}/documents/fetch` endpoint is **ID-only**, and `POST /namespaces/{namespace}/documents/delete` accepts only `ids` or `delete_all`. To act on documents matching a metadata expression, search to retrieve matching IDs (capped at `top_k`, max 10,000 per request), then fetch or delete by ID. To remove all documents in a namespace in one call, use `delete_all` instead.
    </Warning>

    #### More examples

    **Token matching with filter:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "include_fields": ["title", "body", "category", "year"],
        "filter": {
          "category": { "$eq": "technology" },
          "year": { "$gte": 2024 }
        },
        "score_by": [{
          "type": "text",
          "field": "body",
          "query": "machine learning"
        }],
        "top_k": 10
      }'
    ```

    **Cross-field boolean query with `query_string`:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "include_fields": ["title", "body"],
        "score_by": [{
          "type": "query_string",
          "query": "title:(quantum) OR body:(machine learning)"
        }],
        "top_k": 10
      }'
    ```

    **Dense vector ranking with a phrase-match filter:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "include_fields": ["title", "body"],
        "filter": { "body": { "$match_phrase": "machine learning" } },
        "score_by": [{
          "type": "dense_vector",
          "field": "embedding",
          "values": [0.12, 0.34, 0.56]
        }],
        "top_k": 10
      }'
    ```

    **Sparse vector ranking:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "include_fields": ["title", "body"],
        "score_by": [{
          "type": "sparse_vector",
          "field": "sparse_embedding",
          "sparse_values": {
            "indices": [12, 287, 4096],
            "values": [0.41, 0.33, 0.18]
          }
        }],
        "top_k": 10
      }'
    ```

    **Text match filter with BM25 ranking:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
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
          "field": "body",
          "query": "monetary policy impact"
        }],
        "top_k": 10
      }'
    ```

    This restricts the candidate set to finance articles whose `body` contains both "federal" and "reserve", then ranks those candidates by BM25 score against "monetary policy impact".

    **Phrase filter with negation:**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/search" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
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
          "field": "body",
          "query": "recent advances in generative AI"
        }],
        "top_k": 10
      }'
    ```

    This requires the exact phrase "large language model" and excludes documents containing "spam" or "advertisement".

    **Example response**

    **Status:** 200 OK

    ```json theme={null}
    {
      "matches": [
        {
          "_id": "doc1",
          "_score": 0.8234,
          "title": "Machine learning in 2024",
          "body": "Machine learning models are revolutionizing natural language processing",
          "category": "technology",
          "year": 2024
        }
      ],
      "namespace": "__default__",
      "usage": { "read_units": 1 }
    }
    ```

    Response fields:

    * `matches` (array) - Ranked matches, most relevant first.
      * `_id` (string) - Document ID.
      * `_score` (float) - Relevance score (higher is better). The leading underscore prevents collision with user-defined metadata fields named `score`.
      * Plus any fields requested via `include_fields`.
    * `namespace` (string) - Namespace searched.
    * `usage` (object) - `read_units` consumed.
  </Accordion>

  <Accordion title="Fetch documents (POST /namespaces/{namespace}/documents/fetch)">
    Fetches documents by ID. Fetch is **ID-only** — the endpoint does not accept a `filter` parameter. To retrieve documents matching a metadata expression, use `POST /namespaces/{namespace}/documents/search` with a `filter` instead.

    **Example request — fetch by ids**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/fetch" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{
        "ids": ["doc1", "doc2"],
        "include_fields": ["title", "body", "category"]
      }'
    ```

    Body parameters:

    * `ids` (array of strings, required, 1-1000 items) - Document IDs to fetch. Must contain at least one ID; an empty array returns a 400 error.
    * `include_fields` (array of strings, optional) - Field names to include. If omitted, all fields are returned.

    **Example response**

    **Status:** 200 OK

    ```json theme={null}
    {
      "documents": {
        "doc1": {
          "_id": "doc1",
          "title": "Machine learning in 2024",
          "body": "Machine learning models are revolutionizing natural language processing",
          "category": "technology"
        },
        "doc2": {
          "_id": "doc2",
          "title": "Vector databases",
          "body": "Vector databases enable fast similarity search across embeddings",
          "category": "technology"
        }
      },
      "namespace": "__default__",
      "usage": { "read_units": 2 }
    }
    ```

    Response fields:

    * `documents` (object) - Map of document ID to the returned fields (including `_id`).
    * `namespace` (string) - Namespace fetched from.
    * `usage` (object) - `read_units` consumed.
  </Accordion>

  <Accordion title="Delete documents (POST /namespaces/{namespace}/documents/delete)">
    Deletes documents from a namespace. You must specify exactly one of `ids` or `delete_all`. Delete does not accept a `filter` parameter — to delete documents matching a metadata expression, fetch their IDs via `POST /namespaces/{namespace}/documents/search` first, then pass them to delete.

    **Example request — delete by ids**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/delete" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{ "ids": ["doc1", "doc2"] }'
    ```

    **Example request — delete all in namespace**

    ```bash theme={null}
    curl -X POST "https://articles-abc123.svc.us-east-1.pinecone.io/namespaces/__default__/documents/delete" \
      -H "Api-Key: {{YOUR_API_KEY}}" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-01.alpha" \
      -d '{ "delete_all": true }'
    ```

    Body parameters (specify exactly one):

    * `ids` (array of strings, 1-1000 items) - Document IDs to delete.
    * `delete_all` (boolean) - If `true`, delete all documents in the namespace.

    **Example response**

    **Status:** 202 Accepted

    ```json theme={null}
    {}
    ```
  </Accordion>
</AccordionGroup>

## Python SDK

<Tip>
  For a runnable end-to-end example, see this [Google Colab notebook](https://colab.research.google.com/drive/1lsPeNLCJ2ucbYthHYs9WpybW4nAfB8tG), which demonstrates upserting and searching a sample Wikipedia dataset.
</Tip>

### Installation

Full-text search is available in the standard `pinecone` Python SDK under the `pc.preview.*` namespace, which gates the alpha API surface. Make sure you have a recent version of the SDK installed.

```sh theme={null}
pip install --upgrade pinecone
```

<Note>
  FTS endpoints are accessed via `pc.preview.*` for control-plane operations and `pc.preview.index(...).documents.*` for data-plane document operations. The `preview` namespace makes the alpha status explicit and isolates FTS APIs from the GA `pc.indexes.*` and `pc.index(...)` namespaces used by the vector API.
</Note>

### Control plane

<AccordionGroup>
  <Accordion title="Instantiate the client">
    ```python theme={null}
    import os
    from pinecone import Pinecone

    pc = Pinecone(
      api_key=os.environ.get('PINECONE_API_KEY')
    )
    ```
  </Accordion>

  <Accordion title="Create index (on-demand read capacity)">
    ```python theme={null}
    from pinecone.preview import SchemaBuilder

    schema = (
        SchemaBuilder()
          .add_string_field(name="title", full_text_search={"language": "en"})
          .add_string_field(name="body", full_text_search={"language": "en", "stemming": True})
          .build()
    )

    index_model = pc.preview.indexes.create(
        name="articles",
        schema=schema,
        read_capacity={"mode": "OnDemand"},
    )

    host = index_model.host
    ```
  </Accordion>

  <Accordion title="Create index (dedicated read capacity)">
    ```python theme={null}
    from pinecone.preview import SchemaBuilder

    schema = (
        SchemaBuilder()
          .add_string_field(name="content", full_text_search={"language": "en"})
          .build()
    )

    index_model = pc.preview.indexes.create(
        name="articles-dedicated",
        schema=schema,
        read_capacity={
            "mode": "Dedicated",
            "dedicated": {
                "node_type": "b1",
                "scaling": "Manual",
                "manual": {"shards": 1, "replicas": 1},
            },
        },
    )
    ```
  </Accordion>

  <Accordion title="Describe index">
    ```python theme={null}
    index_model = pc.preview.indexes.describe(name="articles")
    print(index_model.status, index_model.schema)
    ```
  </Accordion>

  <Accordion title="List indexes">
    ```python theme={null}
    for idx in pc.preview.indexes.list():
        print(idx.name, idx.status)
    ```
  </Accordion>

  <Accordion title="Check whether an index exists">
    ```python theme={null}
    if pc.preview.indexes.exists(name="articles"):
        index_model = pc.preview.indexes.describe(name="articles")
    ```
  </Accordion>

  <Accordion title="Update index configuration">
    ```python theme={null}
    pc.preview.indexes.configure(
        name="articles",
        deletion_protection="enabled",
        tags={"env": "prod"},
    )
    ```

    Use `configure` to update mutable settings on an existing index (for example, deletion protection or index tags). Schema changes are not supported in public preview.
  </Accordion>

  <Accordion title="Delete index">
    ```python theme={null}
    pc.preview.indexes.delete(name="articles")
    ```
  </Accordion>
</AccordionGroup>

### Data plane

<AccordionGroup>
  <Accordion title="Build a data plane client">
    ```python theme={null}
    index = pc.preview.index(name="articles")
    ```
  </Accordion>

  <Accordion title="Upsert documents">
    ```python theme={null}
    NAMESPACE = 'example-namespace'

    docs = [
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
    ]

    # batch_upsert splits docs into parallel requests — use it for large sets.
    # For small batches (≤1000 docs), index.documents.upsert(namespace=..., documents=...) is simpler.
    index.documents.batch_upsert(
        namespace=NAMESPACE,
        documents=docs,
        batch_size=50,
        max_concurrency=4,
        show_progress=True,
    )
    ```
  </Accordion>

  <Accordion title="Search — token match (type: text)">
    ```python theme={null}
    NAMESPACE = 'example-namespace'

    response = index.documents.search(
        namespace=NAMESPACE,
        top_k=10,
        score_by=[
            {
                "type": "text",
                "field": "body",
                "query": "machine learning",
            }
        ],
        include_fields=["title", "body", "category", "year"],
    )
    for match in response.matches:
        print(match._id, match._score, getattr(match, "title", ""))
    ```
  </Accordion>

  <Accordion title="Search — Lucene query string (type: query_string)">
    ```python theme={null}
    NAMESPACE = 'example-namespace'

    response = index.documents.search(
        namespace=NAMESPACE,
        top_k=10,
        score_by=[
            {
                "type": "query_string",
                "query": "title:(quantum) OR body:(machine learning)",
            }
        ],
        include_fields=["title", "body"],
    )
    ```
  </Accordion>

  <Accordion title="Search — dense vector ranking with phrase-match filter">
    ```python theme={null}
    NAMESPACE = 'example-namespace'
    query_vector = [0.12, 0.34, ...]  # replace with your actual query vector

    response = index.documents.search(
        namespace=NAMESPACE,
        top_k=10,
        score_by=[
            {
                "type": "dense_vector",
                "field": "embedding",
                "values": query_vector,
            }
        ],
        filter={"body": {"$match_phrase": "machine learning"}},
        include_fields=["title", "body"],
    )
    ```
  </Accordion>

  <Accordion title="Fetch documents">
    ```python theme={null}
    NAMESPACE = 'example-namespace'

    response = index.documents.fetch(
        namespace=NAMESPACE,
        ids=["doc1", "doc2"],
        include_fields=["title", "body", "category"],
    )
    for doc_id, doc in response.documents.items():
        print(doc_id, getattr(doc, "title", ""))
    ```
  </Accordion>

  <Accordion title="Delete documents">
    ```python theme={null}
    NAMESPACE = 'example-namespace'

    index.documents.delete(namespace=NAMESPACE, ids=["doc1", "doc2"])

    index.documents.delete(namespace=NAMESPACE, delete_all=True)
    ```

    Delete is **ID-only** (or `delete_all`) — it does not accept a `filter`. To delete documents matching a metadata expression, search first to get IDs, then pass them to `delete`.
  </Accordion>
</AccordionGroup>

## Bulk import

Bulk import loads large numbers of documents into an index from object storage (Amazon S3, Google Cloud Storage, or Azure Blob Storage) in a single asynchronous job. It is the most efficient way to populate an index with many documents at once. For small or ongoing writes, use [`documents.upsert`](#data-plane-operations) instead.

For indexes with document schemas, import files are [JSON Lines](https://jsonlines.org/) (`.jsonl`), optionally gzip-compressed (`.jsonl.gz`). This is the equivalent of the Parquet-based [Import records](/guides/index-data/import-data) flow used by indexes without a schema definition: the `start_import`, `describe_import`, `list_imports`, and `cancel_import` operations are identical, and Pinecone selects the file format automatically from the index type.

<Note>
  Bulk import is supported for indexes with document schemas in which every field is caller-supplied — full-text `string`, `dense_vector`, `sparse_vector`, and auto-indexed metadata. Semantic-text (auto-embedded) fields are not yet supported in schema.
</Note>

### File format

Each line of a `.jsonl` (or `.jsonl.gz`) file is one JSON document, identical in shape to a document you would pass to [`documents.upsert`](#data-plane-operations). Import validates every document through the same code path as a live upsert, so any document that upserts cleanly imports cleanly.

For example, consider an index whose schema declares one full-text field and one dense vector field:

```json theme={null}
{
  "schema": {
    "fields": {
      "body": {
        "type": "string",
        "full_text_search": { "language": "en" }
      },
      "embedding": {
        "type": "dense_vector",
        "dimension": 3,
        "metric": "cosine"
      }
    }
  }
}
```

Each line supplies `_id`, the schema-declared fields, and any additional fields you want stored as filterable metadata (`category` and `year` here):

```jsonl theme={null}
{"_id": "doc1", "body": "Machine learning models are revolutionizing natural language processing", "embedding": [0.12, 0.34, 0.56], "category": "technology", "year": 2024}
{"_id": "doc2", "body": "Vector databases enable fast similarity search across embeddings", "embedding": [0.91, 0.05, 0.44], "category": "technology", "year": 2023}
```

Each document follows these rules:

* `_id` is required in every document: a non-empty string, unique within the namespace.
* Searchable fields declared in the schema are encoded by type:
  * A `dense_vector` field (`embedding` above) is a JSON array of floats whose length equals the schema's declared `dimension`. When the schema declares a dense vector field, every document must include it.
  * A `sparse_vector` field is an object `{"indices": [...], "values": [...]}`.
  * A full-text `string` field (`body` above) is a JSON string.
* Any other field (`category` and `year` above) is stored on the document and [auto-indexed as filterable metadata](#metadata-fields): a string, number, boolean, or array of strings. An array of numbers in an undeclared field is rejected rather than stored as metadata.
* Field names must not start with `_` (reserved for system fields like `_id`) or `$` (reserved for filter operators).

The same per-document size limits as [upsert](#data-plane-operations) apply.

### Directory layout

Lay files out by namespace, exactly as for [Parquet imports](/guides/index-data/import-data#3-prepare-your-data): under a common dataset prefix in your bucket or container, create one subdirectory per namespace and place that namespace's `.jsonl` / `.jsonl.gz` files inside it.

```
<BUCKET_OR_CONTAINER_NAME>/
└── <DATASET_PREFIX>/
    ├── namespace1/
    │   ├── 0.jsonl
    │   └── 1.jsonl.gz
    └── namespace2/
        └── 0.jsonl
```

* Each namespace must **not already exist** in the index — imports only create new namespaces.
* A namespace subdirectory can mix plain `.jsonl` and gzip-compressed `.jsonl.gz` files.

### Prepare a file

Generate a schema-conformant `.jsonl` (or `.jsonl.gz`) file from your documents, then upload it to a namespace subdirectory in object storage.

```python Python theme={null}
import gzip
import json

documents = [
    {
        "_id": "doc1",
        "body": "Machine learning models are revolutionizing natural language processing",
        "embedding": [0.12, 0.34, 0.56],   # must match the schema dimension
        "category": "technology",
        "year": 2024,
    },
    {
        "_id": "doc2",
        "body": "Vector databases enable fast similarity search across embeddings",
        "embedding": [0.91, 0.05, 0.44],
        "category": "technology",
        "year": 2023,
    },
]

# Plain JSONL: one compact JSON document per line.
with open("0.jsonl", "w") as f:
    for doc in documents:
        f.write(json.dumps(doc) + "\n")

# Or gzip-compressed (.jsonl.gz) to cut storage and transfer.
with gzip.open("0.jsonl.gz", "wt") as f:
    for doc in documents:
        f.write(json.dumps(doc) + "\n")
```

Upload the file to the relevant namespace subdirectory in your bucket or container, e.g. `<DATASET_PREFIX>/namespace1/0.jsonl`.

#### Convert Parquet files to JSONL

If your data is already stored as Parquet in the [vector import format](/guides/index-data/import-data#3-prepare-your-data) (`id`, `values`, `sparse_values`, `metadata` columns), convert each file to JSONL for the document schema. Map `id` to `_id`, the vector columns to your schema's field names, and spread the `metadata` JSON string into top-level fields:

```python Python theme={null}
import gzip
import json

import pyarrow.parquet as pq

# Your schema's field names
DENSE_FIELD = "embedding"          # dense_vector field
SPARSE_FIELD = "sparse_embedding"  # sparse_vector field

table = pq.read_table("0.parquet")

with gzip.open("0.jsonl.gz", "wt") as f:
    for row in table.to_pylist():
        doc = {"_id": row["id"]}
        if row.get("values") is not None:
            doc[DENSE_FIELD] = row["values"]
        if row.get("sparse_values") is not None:
            doc[SPARSE_FIELD] = {
                "indices": row["sparse_values"]["indices"],
                "values": row["sparse_values"]["values"],
            }
        if row.get("metadata"):
            # Metadata keys become top-level fields. Keys that match a
            # schema-declared field (e.g. a full-text "body" field) are
            # validated against the schema; the rest are auto-indexed metadata.
            doc.update(json.loads(row["metadata"]))
        f.write(json.dumps(doc) + "\n")
```

### Start an import

To import from a secure data source, you first need a [storage integration](/guides/operations/integrations/manage-storage-integrations) that gives Pinecone access to your object storage. An integration is not required for public data sources.

Start the import against the index host with the [`start_import`](/reference/api/latest/data-plane/start_import) operation (`POST /bulk/imports`) — the same endpoint, parameters, and behavior as for [Parquet imports](/guides/index-data/import-data#4-import-records-into-an-index). Pinecone detects from the index's document schema that the files are JSONL. For `uri`, specify the bucket or container in your storage provider's URI format, plus the dataset prefix — not a path to a single file or a namespace subdirectory.

<Note>
  Bulk import is not yet supported in any Pinecone SDK. Use the REST API to start and manage imports.
</Note>

```bash curl theme={null}
# To get the unique host for an index, see
# https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/bulk/imports" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-01.alpha" \
  -d '{
    "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
    "uri": "STORAGE_URI/DATASET_PREFIX",
    "errorMode": { "onError": "continue" }
  }'
```

The response contains an `id` you can use to track the import with the [`describe_import`](/reference/api/latest/data-plane/describe_import) operation:

```json Response theme={null}
{
  "id": "1"
}
```

Imported documents are indexed asynchronously and may not be searchable immediately after the import reports complete.

### Track and manage an import

The [`describe_import`](/reference/api/latest/data-plane/describe_import), [`list_imports`](/reference/api/latest/data-plane/list_imports), and [`cancel_import`](/reference/api/latest/data-plane/cancel_import) operations behave the same for document and vector indexes. See [Import records](/guides/index-data/import-data#5-track-import-progress) for the full request and response shapes and troubleshooting.

```bash curl theme={null}
curl -X GET "https://$INDEX_HOST/bulk/imports/1" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-01.alpha"
```

Per-document errors identify the file name, row number, and document `_id`. With `errorMode.onError` set to `continue`, invalid documents are skipped and the rest import — use `records_imported` to see how many loaded; with `abort`, the import stops on the first invalid document.

A namespace subdirectory that contains no `.jsonl` / `.jsonl.gz` files is skipped — no namespace is created for it. An import that finds no importable files anywhere under the dataset prefix fails.

### Import limits

Document imports share the [import limits](/guides/index-data/import-data#import-limits): up to 10,000 namespaces and 100,000 files per import, up to 10 GB per file, and — for on-demand indexes — up to 1 TB total input data per import.

For `.jsonl.gz` files, size limits are checked against an estimated uncompressed size of 10× the compressed file size, so plan for roughly 1 GB per compressed file.

## Tokens and analyzers

The word "token" appears in every scoring method, but it means different things in each. Knowing what counts as a token in your chosen method is essential to writing queries that match what you expect.

### FTS tokens (`type: "text"`, `type: "query_string"`, and `$match_*` filters)

When you declare a field with `full_text_search: { ... }`, Pinecone runs the field's text through an **analyzer pipeline** at index time and at query time. Both `type: "text"` and `type: "query_string"` use the same pipeline, and the text-match filter operators ([`$match_phrase`, `$match_all`, `$match_any`](#filters-vs-scoring)) reuse it as well — so a token that scores in BM25 will match in a filter on the same field.

The pipeline (in order):

1. **Split** the text on whitespace and punctuation. Hyphenated words become multiple tokens (`state-of-the-art` → `state`, `of`, `the`, `art`).
2. **Lowercase** every token. Lowercasing is server-applied and cannot be overridden.
3. **Stem** each token to its root form, if [`stemming`](#stemming) is enabled on the field. The stemmer is selected by the field's [`language`](#language) setting (`models` → `model`, `running` → `run`).
4. **Drop stop words** (common words like `the`, `and`), if `stop_words: true` is set on the field. Not all languages have built-in stop word lists; see the [Language](#language) table for details.
5. **Cap** each token at 40 characters. This cap is server-applied and cannot be overridden.

For example, with the `english` analyzer, `stemming: true`, and `stop_words: false`, the input `"State-of-the-Art Models"` becomes the tokens `state`, `of`, `the`, `art`, `model`. Those are the tokens BM25 scores against, and the tokens a `$match_phrase: "art models"` filter will look for.

Fields configured for [substring search](#substring-search-with-n-grams) replace this whole-token pipeline with character n-gram tokenization, so a token is further split into overlapping character sequences.

### Dense-vector tokens (`type: "dense_vector"`)

Dense embedding models have their own internal tokenizer — usually a subword scheme like BPE, WordPiece, or SentencePiece — that breaks text into pieces the model was trained on. Those tokens are **private to the model**. You never query them directly: a dense search compares the full embedding of a query against the full embedding of a document. The same string can therefore behave very differently in `type: "text"` (which sees the FTS analyzer tokens above) and `type: "dense_vector"` (which sees a single high-dimensional vector). The `$match_*` filter operators do not apply to dense-vector fields.

### Sparse-vector tokens (`type: "sparse_vector"`)

Sparse encoders also tokenize internally, and the tokenization depends on the encoder. Pinecone's hosted [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) produces learned per-token weights and **expands to related terms** that don't appear in the source text. Encoder tokens are not interchangeable with FTS analyzer tokens, and `$match_*` filters do not apply to sparse-vector fields.

### Practical implication

If your application stores the same source text in an FTS-enabled `string` field and also encodes it into a `dense_vector` or `sparse_vector` field, the three representations are tokenized **independently**: the FTS analyzer for the `string` field, and each model's internal tokenizer for the vector fields. Identical query strings will therefore retrieve different documents under different `score_by` types, and `$match_*` filters can only narrow on the FTS-analyzer tokens of FTS-enabled `string` fields.

## Query syntax reference

Full-text search supports two text-based query types with different capabilities:

| Feature                 | `type: "text"`                                                             | `type: "query_string"`                                 |
| ----------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Purpose**             | Simple token search on one field                                           | Lucene query syntax                                    |
| **`fields` parameter**  | Required (exactly one field)                                               | Optional (restricts to listed text-searchable fields)  |
| **Multi-word behavior** | Token match, OR across terms (BM25)                                        | OR by default; use `AND`, quotes, etc. for other logic |
| **Boolean operators**   | Not supported (treated as words)                                           | `AND`, `OR`, `NOT`, `+`, `-`                           |
| **Phrase prefix**       | Not supported                                                              | `"phrase pre"*` (last term as prefix)                  |
| **Phrase matching**     | Not supported in `score_by` (use `query_string` or `$match_phrase` filter) | Wrap in quotes: `"exact phrase"`                       |
| **Phrase slop**         | Not supported                                                              | `"phrase"~N`                                           |
| **Boosting**            | Not supported                                                              | `term^N`                                               |
| **Regex**               | Not supported                                                              | `field:/pattern.*/`                                    |
| **Fuzzy matching**      | Not supported                                                              | `term~`, `term~N` (typo tolerance)                     |
| **Stemming**            | Supported ([when enabled](#stemming))                                      | Supported ([when enabled](#stemming))                  |
| **Case sensitivity**    | Case-insensitive                                                           | Case-insensitive                                       |

### Token matching (`type: "text"`)

With `type: "text"`, the query string is run through the field's analyzer pipeline (see [Tokens and analyzers](#tokens-and-analyzers)) and each resulting term contributes to the BM25 score. Multiple terms use **OR** semantics: documents can match if they contain **any** of the terms; documents that match more terms or stronger term statistics typically rank higher. Matching is case-insensitive. Exact **phrase** constraints (adjacent words in order) belong in `type: "query_string"` using quotes, or in a `$match_phrase` filter.

| Query              | Matches                                                               | Does not match                         |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------- |
| `machine learning` | "**Machine** learning is great" (has "machine")                       | "Vector databases only" (neither term) |
| `machine learning` | "We use **learning** and **machine**" (both terms present, any order) | "Vector databases only" (neither term) |
| `machine`          | "**Machine** learning is great"                                       | "Vector databases only" (no "machine") |

**Key behaviors:**

* **Single term** (`machine`): Matches documents containing that term. Case-insensitive.
* **Multiple terms** (`machine learning`): Each term is searched independently with OR-style matching and combined BM25 scoring — not as a single adjacent phrase.
* **No operator support**: Characters like `AND`, `OR`, `NOT`, `*`, `~`, `^`, `+`, `-`, and quotes are treated as literal text.

### Lucene query syntax (`type: "query_string"`)

With `type: "query_string"`, you write Lucene query syntax, with operator support. Field names are embedded in the query itself (e.g., `content:(term)`) and can combine multiple fields with boolean operators.

| Operator       | Syntax                     | Example                             | Description                                                 |
| -------------- | -------------------------- | ----------------------------------- | ----------------------------------------------------------- |
| Term           | `field:(word)`             | `body:(computers)`                  | Match documents containing term                             |
| Multiple terms | `field:(a b)`              | `body:(machine learning)`           | OR by default — matches either term                         |
| Phrase         | `field:("words")`          | `body:("machine learning")`         | Exact phrase match (adjacent, in order)                     |
| AND            | `AND`                      | `body:(a AND b)`                    | Both terms required                                         |
| OR             | `OR`                       | `body:(a OR b)`                     | Either term matches (same as default)                       |
| NOT            | `NOT`                      | `body:(a NOT b)`                    | Exclude second term                                         |
| Required       | `+term`                    | `body:(+database search)`           | Term must be present                                        |
| Excluded       | `-term`                    | `body:(database -deprecated)`       | Term must not be present                                    |
| Grouping       | `(expr)`                   | `body:((a OR b) AND c)`             | Control precedence                                          |
| Phrase slop    | `"phrase"~N`               | `body:("fast search"~2)`            | Allow up to N words between phrase terms                    |
| Boost          | `term^N`                   | `body:(machine^3 learning)`         | Multiply term's relevance score by N                        |
| Phrase prefix  | `"phrase pre"*`            | `body:("james w"*)`                 | Last term in phrase matched as prefix                       |
| Regex          | `field:/pattern.*/`        | `body:/comput.*/`                   | Match documents by regular expression on a field            |
| Fuzzy          | `term~` or `term~N`        | `body:(compxter~1)`                 | Match terms within edit distance N (0–2) for typo tolerance |
| Cross-field    | `fieldA:(…) OR fieldB:(…)` | `title:(quantum) OR body:(machine)` | Combine clauses across text-searchable fields               |

<AccordionGroup>
  <Accordion title="Terms and default OR behavior">
    A **term** is a single word. Multiple space-separated terms use **OR logic** by default.

    ```
    body:(machine learning)
    ```

    Matches documents containing "machine" OR "learning" (or both). Documents with both terms rank higher.
  </Accordion>

  <Accordion title="Phrases">
    Wrap multiple words in quotes to match them as an exact sequence.

    ```
    body:("machine learning")
    ```

    Matches only documents containing the exact phrase "machine learning" with the words adjacent. That is different from `type: "text"` with `query: "machine learning"`, which uses **token OR** matching on the field. For phrase matching as a **filter** (e.g., composed with dense-vector ranking), use `{"body": {"$match_phrase": "machine learning"}}` in the `filter` block.

    *Phrase terms are matched against the field's analyzed tokens. If [stemming](#stemming) is enabled on the field, the phrase terms stem too — e.g., `"running fast"` matches `running fast` and `runs fast`.*
  </Accordion>

  <Accordion title="Boolean operators (AND, OR, NOT)">
    Use `AND`, `OR`, and `NOT` for explicit boolean logic.

    ```
    body:(machine AND learning)        # Both terms required (any order)
    body:(machine OR learning)         # Either term (same as default)
    body:(machine NOT learning)        # "machine" but not "learning"
    ```

    **Precedence:** AND binds tighter than OR. Use parentheses to control order:

    ```
    body:((database OR storage) AND distributed)
    ```
  </Accordion>

  <Accordion title="Required and excluded terms (+, -)">
    Use `+` to require a term and `-` to exclude a term.

    ```
    body:(+database distributed)       # MUST contain "database", "distributed" optional
    body:(database -deprecated)        # Contains "database", must NOT contain "deprecated"
    body:(+vector +search -legacy)     # MUST have "vector" AND "search", must NOT have "legacy"
    ```
  </Accordion>

  <Accordion title="Phrase proximity (slop)">
    Allow words in a phrase to appear within N positions of each other.

    ```
    body:("machine learning"~3)
    ```

    Matches "machine learning", "machine deep learning", or "machine-assisted learning" (words within 3 positions).

    *The phrase terms are matched against analyzed tokens, so [stemming](#stemming) (when enabled on the field) applies here too.*
  </Accordion>

  <Accordion title="Term boosting">
    Increase the importance of specific terms in ranking using `^N`.

    ```
    body:(machine^3 learning)          # "machine" weighted 3x more than "learning"
    body:("neural network"^2 deep)     # Phrase boosted 2x
    ```

    Documents with boosted terms rank higher when those terms appear.
  </Accordion>

  <Accordion title="Phrase prefix">
    Append `*` to a quoted phrase to treat the last term as a prefix. The phrase must contain at least two terms.

    ```
    body:("james w"*)                  # Matches "james webb", "james watson", "james wilde"
    body:("machine lea"*)              # Matches "machine learning", "machine learns"
    ```

    Both the literal terms and the prefix are matched against the field's analyzed tokens. If [stemming](#stemming) is enabled on the field, stemming applies to the completed terms in the phrase, while the final prefix is expanded against analyzed tokens.

    Phrase prefix is optimized for autocomplete-style queries where the final word prefix is reasonably specific. To keep latency low, Pinecone expands the final prefix to the first 50 matching terms in lexicographic order. For example, `"new yor"*` can match `new york`, but `"new yo"*` might not if `york` is not among the first 50 expanded terms for `yo`.
  </Accordion>

  <Accordion title="Regex">
    Wrap a pattern in forward slashes to match documents by regular expression on a field.

    ```
    body:/comput.*/
    ```

    Matches documents whose `body` field contains a token matching the regex `comput.*` (e.g., "computer", "computing", "computation"). Regex patterns are matched against individual analyzed tokens, not the raw field text.

    ```
    body:/machin[ei].*/
    ```

    Matches tokens like "machine" or "machene". Standard Lucene regex syntax is supported.

    Regex is only available with `type: "query_string"`. It is not supported with `type: "text"`.
  </Accordion>

  <Accordion title="Fuzzy matching (typo tolerance)">
    Append `~` to a bare term to match indexed terms within a small edit distance, so a misspelled query term still matches the intended word.

    ```
    body:(compxter~1)                  # Matches "computer" (1 edit away)
    body:(machine~ learning~)          # Auto distance per term, based on term length
    title:(pinecone~2)                 # Explicit distance 2
    ```

    * **`term~`** — automatic distance based on the term's length: terms shorter than 4 characters must match exactly, terms of 4–7 characters allow 1 edit, and terms of 8 or more characters allow 2 edits.
    * **`term~N`** — fixed edit distance `N`, where `N` is `0`, `1`, or `2`. `~0` is an exact match. A distance greater than 2 is a query error (`400`).

    An "edit" is an inserted, deleted, or substituted character (plain Levenshtein distance). Swapping two adjacent characters counts as 2 edits. Matching is case-insensitive, as with all text queries.

    Fuzzy matches are scored as a constant; exact matches still contribute their full BM25 score, so an exact hit ranks above a fuzzy hit for the same term. Fuzzy composes with the rest of the query syntax — boolean operators, required/excluded terms, boosts, field qualifiers, and metadata filters.

    <Note>
      The `~` operator is fuzzy only when it follows a **bare term**. After a quoted phrase, `~N` keeps its [phrase slop](#query-syntax-reference) meaning — for example, `body:("machine learning"~2)` is slop, while `body:(learning~2)` is fuzzy. There is no fuzzy phrase matching.
    </Note>

    <Note>
      On [stemmed](#stemming) fields, fuzzy matching runs against the stemmed terms and is best-effort: a typo that changes how a word stems may not match. Fuzzy matching is most effective on fields without stemming (the default). Fuzzy is available only with `type: "query_string"`; with `type: "text"`, `~` is treated as a literal character.
    </Note>
  </Accordion>

  <Accordion title="Cross-field queries">
    `query_string` can target multiple fields in the same expression. Use Lucene field qualifiers (`field:(clause)`) directly in the query string; omit them to run against all text-searchable fields:

    ```
    title:(quantum) OR body:(machine learning)
    ```

    Matches documents whose `title` contains "quantum", documents whose `body` contains "machine" or "learning", or both — with BM25 scoring combining across fields.
  </Accordion>
</AccordionGroup>

## Stemming

Stemming reduces words to their root form so that morphological variants match each other. For example, with stemming enabled, a query for "run" also matches documents containing "running" or "runs".

Stemming is **opt-in** and disabled by default. To enable it, set `stemming: true` on a text-searchable field when creating the index. The stemming algorithm is determined by the field's [`language`](#language) setting.

**Example: enabling stemming with French**

```json theme={null}
{
  "schema": {
    "fields": {
      "body": {
        "type": "string",
        "full_text_search": {
          "stemming": true,
          "language": "french"
        }
      }
    }
  }
}
```

Stemming applies to both `type: "text"` and `type: "query_string"` queries on the field.

<Note>
  Stemming is set at index creation and cannot be changed afterward.
</Note>

## Language

The `language` parameter controls tokenization and stemming behavior for a text-searchable field. It determines how text is analyzed during indexing and search: how words are split into tokens and, when [stemming](#stemming) is enabled, which language-specific rules are used to reduce words to their root forms.

The default language is `"en"` (English). You can specify a language using either its short code or full name (e.g., `"fr"` or `"french"`).

**Supported languages:**

| Code | Full name    | Stop words |
| ---- | ------------ | ---------- |
| `ar` | `arabic`     | No         |
| `da` | `danish`     | Yes        |
| `de` | `german`     | Yes        |
| `el` | `greek`      | No         |
| `en` | `english`    | Yes        |
| `es` | `spanish`    | Yes        |
| `fi` | `finnish`    | Yes        |
| `fr` | `french`     | Yes        |
| `hu` | `hungarian`  | Yes        |
| `it` | `italian`    | Yes        |
| `nl` | `dutch`      | Yes        |
| `no` | `norwegian`  | Yes        |
| `pt` | `portuguese` | Yes        |
| `ro` | `romanian`   | No         |
| `ru` | `russian`    | Yes        |
| `sv` | `swedish`    | Yes        |
| `ta` | `tamil`      | No         |
| `tr` | `turkish`    | No         |

<Note>
  Language is set at index creation and cannot be changed afterward.
</Note>

## Substring search with n-grams

By default, full-text search matches whole tokens: a query for `comp` does not match a document containing `computer`. To match substrings (for example, to find `computer` from `comp`, `mput`, or `uter`), configure a text field for **character n-gram** tokenization.

With n-gram tokenization, each token is broken into overlapping character sequences (n-grams) at index time, and query text is broken the same way at search time, so a substring of an indexed word matches. This is useful for partial-word matching, autocomplete, and searching identifiers or codes where users type only a fragment.

To enable it, set an `ngram` object on a text field's `full_text_search` config at index creation:

```json theme={null}
{
  "schema": {
    "fields": {
      "product_name": {
        "type": "string",
        "full_text_search": {
          "ngram": {
            "min_gram": 3,
            "max_gram": 4,
            "prefix_only": false
          }
        }
      }
    }
  }
}
```

`ngram` parameters:

| Parameter     | Type    | Required             | Description                                                                                                                                                                                                         |
| ------------- | ------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `min_gram`    | integer | Yes                  | Shortest n-gram to generate. Must be at least `1`.                                                                                                                                                                  |
| `max_gram`    | integer | Yes                  | Longest n-gram to generate. Must be at least `min_gram` and at most `10`.                                                                                                                                           |
| `prefix_only` | boolean | No (default `false`) | When `true`, generate only n-grams anchored to the start of each token (edge n-grams). Use this for prefix and autocomplete matching. When `false`, generate n-grams at every position for full substring matching. |

For example, with `min_gram: 3`, `max_gram: 4`, and `prefix_only: false`, the token `search` is indexed as `sea`, `ear`, `arc`, `rch`, `sear`, `earc`, `arch`. A shorter or longer window changes the tradeoff: smaller n-grams match more loosely and grow the index more; larger n-grams are more precise but require longer matching substrings.

**Querying an n-gram field.** No special query syntax is needed. Once a field is configured for n-grams, ordinary `type: "text"` and `query_string` queries against it match on substrings automatically, because the query text is tokenized into the same n-grams as the indexed text:

```python Python theme={null}
response = index.documents.search(
    namespace="example-namespace",
    top_k=10,
    score_by=[
        {
            "type": "text",
            "field": "product_name",
            "query": "sear",
        }
    ],
    include_fields=["product_name"],
)
```

<Note>
  N-gram tokenization cannot be combined with [`stemming`](#stemming) or `stop_words` on the same field — an index-creation request that sets `ngram` alongside either is rejected with a `400` error. Tokens are always lowercased. Because every position emits a token for each gram length, an n-gram field is larger on disk than a plain text field; keep `min_gram`/`max_gram` as narrow as your matching needs allow.
</Note>

<Note>
  N-gram configuration is set at index creation and cannot be changed afterward.
</Note>

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
    * `400 Bad Request`: Check JSON syntax and required fields. Examples: `fields` array with more than one element for `text`/`dense_vector`/`sparse_vector`; missing mutually-exclusive field for Fetch/Delete.
    * `404 Not Found`: Verify the index name and host URL.
    * Missing API version: Add `X-Pinecone-Api-Version: 2026-01.alpha`.
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

## Public preview

Full-text search is in public preview under API version `2026-01.alpha`. The feature is ready for production evaluation; APIs may continue to evolve before general availability.

**Requirements & limitations**

* All requests require `X-Pinecone-Api-Version: 2026-01.alpha`.
* The REST API, Python SDK (`pinecone`, `pc.preview.*` namespace for FTS control plane), and Pinecone console are the supported entry points for public preview.
* **Endpoint compatibility**: indexes with document schemas use the `/namespaces/{namespace}/documents/*` endpoints; dense, sparse, and integrated-inference indexes continue to use `/vectors/*` (and `/records/*` for integrated inference). The two endpoint families are index-type-specific and don't cross over.
* Supported deployment modes: managed (serverless) with `read_capacity.mode` of `OnDemand` or `Dedicated`.
* Changing an index from dedicated read capacity back to on-demand read capacity is not supported. To move from dedicated read capacity to on-demand, create a new on-demand index and reingest your data.
* Schemas declare ranking fields only: text fields (`string` with `full_text_search`), `dense_vector`, and `sparse_vector`. Text-only, text + dense vector, and combined dense + sparse + text schemas are all supported in a single index. Metadata-only field declarations (`string` without `full_text_search`, `string_list`, `float`, `boolean`) are rejected at index creation; metadata is auto-indexed at upsert time.
* **Schema and document limits**: a schema can contain up to 100 `full_text_search` string fields; each `full_text_search` string field can be up to 100 KB and 10,000 tokens; tokens can be up to 256 bytes before analyzer truncation; each document can be up to 2 MB; each upsert request can contain up to 1000 documents and 2 MB.
* **Metadata size**: metadata fields on a document (everything outside FTS-enabled `string` fields) are limited to 40 KB per document in total. This limit does not apply to `full_text_search` text fields.
* **Vector-field cardinality**: a schema can declare up to 100 `string` fields with `full_text_search` enabled, but at most one `dense_vector` field and at most one `sparse_vector` field per index.
* **Field-name policy**: schema and metadata field names must not start with `_` (reserved for system-managed fields like `_id` and `_score`) or `$` (reserved for filter operators), and are limited to 64 bytes.
* The match-score response field is `_score` (renamed from `score` so that user metadata named `score` can coexist with the system-owned match score in the flat response payload).
* **A single search request ranks by one scoring type.** Multi-field BM25 is supported: pass multiple `text` clauses (one per field) or a single `query_string` clause that targets several fields — every contributing field weighs equally in `2026-01.alpha`; there is no per-clause weight parameter. To combine BM25 ranking with `dense_vector` or `sparse_vector` ranking, restrict the dense (or sparse) search with a text-match filter (`$match_phrase`, `$match_all`, `$match_any`) on the lexical field, or run separate searches and merge the results client-side.
* Newly upserted documents are indexed asynchronously and may not be searchable immediately.
* **No partial / per-field updates**: `POST /namespaces/{namespace}/documents/upsert` always replaces the entire document for a given `_id`. There is no `PATCH` endpoint and no field-level merge in `2026-01.alpha`. To update a single field, fetch the document by ID (`POST /namespaces/{namespace}/documents/fetch`), modify the field client-side, and upsert the full document back under the same `_id`. Field-level merge is on the roadmap for a post-public-preview release.
* **Schemas are fixed at index creation.** Adding, removing, or retyping fields after creation is not yet supported. Existing pre-public-preview indexes cannot be backfilled with a schema — to use FTS, dense + FTS, or any document API query in `2026-01.alpha`, create a new index with the desired schema and reindex documents.
* **Metadata is auto-indexed**: any field on an upserted document that is not declared in the schema is automatically indexed for filtering. The schema declares only ranking fields (FTS-enabled `string`, `dense_vector`, `sparse_vector`); declaring metadata-only fields (`string` without `full_text_search`, `string_list`, `float`, `boolean`) is rejected at index creation. Track metadata field names and types in your application — Pinecone infers the type from the values you upsert.
* **Bulk import** from object storage is supported for indexes with document schemas via JSONL files — see [Bulk import](#bulk-import). Semantic-text (auto-embedded) fields are not yet supported in schemas.
* **Maximum results per query**: `top_k` is capped at **10,000**. Full-text search is optimized for ranked retrieval; for aggregation- or count-style queries (e.g., "how many documents contain term X"), faceting is on the roadmap for a future release.
* Indexes cannot be created in CMEK-enabled projects.
* Backup and restore are not yet supported.
* **`describe_index_stats`** is not yet supported on indexes with document schemas.
* [Fuzzy matching](#query-syntax-reference) (`term~`, `term~N`) is available only in `query_string` scoring, not in `type: "text"` or in `$match_*` filters.
* Single-term prefix wildcards (`auto*`) are not supported; use phrase prefix (`"word auto"*`) instead, or configure a field for [substring search](#substring-search-with-n-grams).

## Pricing

Reads and writes on indexes with document schemas are metered using the same [read units (RUs)](/guides/manage-cost/understanding-cost#read-units) and [write units (WUs)](/guides/manage-cost/understanding-cost#write-units) model as vector indexes. List pricing for public preview will be announced before general availability.

## Next steps

* **[Create an index](/guides/index-data/create-an-index)**: create an index with a document schema that declares your ranking fields.
* **[Model your data](/guides/index-data/data-modeling#schema-patterns)**: schema-pattern recipes for keyword-only, multi-field, dense + FTS, and multi-signal indexes.
* **[Choose a search approach](/guides/search/search-overview)**: compare full-text, semantic, sparse-vector, and hybrid search.
* **[Hybrid search](/guides/search/hybrid-search)**: combine keyword and vector ranking, including when to use a document schema versus the vector API.
* **[Filter by metadata](/guides/search/filter-by-metadata)**: narrow the candidate set before ranking.
* **[Understanding cost](/guides/manage-cost/understanding-cost)**: how read units and write units are metered.
