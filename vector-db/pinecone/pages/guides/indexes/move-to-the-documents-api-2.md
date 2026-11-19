---
title: "Move to the Documents API"
source: https://docs.pinecone.io/guides/indexes/move-to-the-documents-api
path: guides/indexes/move-to-the-documents-api
---

Move your data from a legacy vector index or legacy integrated index to a document index, and update your code to call the Documents API.

An index stays on the API it was created with. An index on the legacy Vectors API or legacy Records API never moves to the [Documents API](/guides/get-started/documents-api) on its own, even after you upgrade your SDK, and requests sent to the wrong API are refused. To use the Documents API, put your data in a new document index and point your code at it. Your legacy indexes and the code that calls them keep working in the meantime.

## Move your data

To move a serverless or Bring Your Own Cloud (BYOC) index without reloading your data, [convert it](/guides/indexes/convert-an-index). Pinecone creates a new document index with the schema you choose and fills it from the source index's records, and the source index is left unchanged. Conversion is available on Standard and Enterprise plans.

If you can't convert your index, or you want to reshape your data on the way in, create a new index and load your data into it:

### 1. Upgrade your SDK

Upgrade to a `2026-07` SDK (Python v10 or later, Node.js v9 or later, or Go v7 or later), or use the REST API. The Java SDK doesn't support `2026-07` yet, so call the REST API from Java.

### 2. Create a document index

[Create a new index](/guides/indexes/create-an-index) with the [schema](/guides/indexes/data-modeling) you want. Add a `deployment` only if you need a specific deployment type, cloud, or region; otherwise it defaults to managed serverless.

### 3. Load your data

Load your data from its source with [upsert](/guides/data/upsert-data) or [import](/guides/data/import-data). Each record becomes a document: its ID goes in `_id`, its vector goes in your dense field, and its metadata keys become top-level fields.

### 4. Switch your application

Point your application at the new index's host, and switch its calls to their [Documents API equivalents](#documents-api-equivalents). Writes sent to the old index after you loaded your data aren't in the new one, so pause them or replay them.

### 5. Delete the old index

When you no longer need the old index, [delete it](/guides/indexes/manage-indexes#delete-an-index).

## Documents API equivalents

Each legacy call has a Documents API equivalent. In the Python SDK:

| Operation | Legacy vector index | Document index |
| - | - | - |
| Create | `pc.create_index(dimension=..., metric=..., vector_type=...)` | `pc.indexes.create(schema=...)` |
| Write | `index.upsert` | `index.documents.upsert` |
| Search | `index.query` with a vector | `index.documents.search` with a `dense_vector` clause in `score_by` |
| Fetch | `index.fetch` | `index.documents.fetch` |
| Update | `index.update` | `index.documents.update` |
| Delete | `index.delete` | `index.documents.delete` |
| List IDs | `index.list` | `index.documents.list` |

For a legacy integrated index, see [Integrated embedding](/guides/search/integrated-embedding) for the document index setup, which needs Python SDK `10.1.0` or later:

* `pc.create_index_for_model` becomes `pc.indexes.create` with a `string` field that declares `embed`.
* `index.upsert_records` becomes `index.documents.upsert`.
* `index.search` becomes `index.documents.search` with an `embed` clause in `score_by`.

Index-management calls like `describe_index` and `list_indexes` also return a new shape on API version `2026-07`:

* In the REST API, a `schema` object replaces the top-level `dimension`, `metric`, `vector_type`, and `spec`, so `dimension` and `metric` appear on the schema's dense-vector field. Update any code that calls the REST API directly.
* The SDKs return both the new fields and the older top-level ones, so SDK code that reads the top-level fields keeps working.

## FAQ

> [accordion] I use hybrid search (dense + sparse, legacy Vectors API). What happens?
>
> Your existing indexes that store both dense and sparse vectors keep working through the legacy Vectors API, with the same single combined query. On the Documents API, a schema can declare both a `dense_vector` and a `sparse_vector` field, so one index holds both, but a search ranks by one scoring type per request. There's no single combined dense + sparse query, so to combine results, run each search separately and fuse them client-side with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).

> [accordion] I use integrated embedding (the legacy Records API). Does anything change?
>
> Your existing indexes are unaffected, and the legacy Records API and `create_index_for_model` keep working. Document indexes support integrated embedding too: declare a `string` field with `embed` or `sparse_embed`, and Pinecone embeds its text for you. For new work, prefer that path. See [Integrated embedding](/guides/search/integrated-embedding).

> [accordion] Can I keep creating indexes on the legacy Vectors API?
>
> Yes. In the `2026-07` SDK, your existing `create_index(dimension=..., metric=..., vector_type=..., spec=...)` code works unchanged and still creates a legacy vector index, so you don't have to downgrade. If you call the REST API directly on `2026-07`, use a schema with the reserved `_values`/`_sparse_values` fields, or pin an earlier API version (`X-Pinecone-Api-Version: 2026-04`) to send the original request body. Indexes you create either way stay on the `/vectors/*` data plane.
