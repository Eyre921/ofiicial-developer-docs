---
title: "Adopt the Documents API"
source: https://docs.pinecone.io/guides/index-data/adopt-the-documents-api
path: guides/index-data/adopt-the-documents-api
---

Learn what changes in API version 2026-07, whether your existing code is affected, and how to move to schema-based indexes.

API version `2026-07` introduces the [Documents API](/guides/search/full-text-search), a new way to create and query indexes that can hold dense vectors, sparse vectors, and full-text fields in a single index. This page explains what changes, whether your existing code is affected, and how to adopt schema-based indexes.

## What's changing

API version `2026-07` adds a schema-based way to create and query indexes, alongside the existing [Vectors API](/guides/search/semantic-search).

To create a document index, use `pc.indexes.create` (or `POST /indexes` in the REST API) with a `schema`:

* A `schema` declares each of your index's fields and its type, so one index can hold dense-vector, sparse-vector, and full-text fields together.
* A `deployment` sets the deployment type, cloud, and region. It's optional and defaults to managed serverless. Read capacity is configured separately, with a top-level `read_capacity`.

At the API level, `POST /indexes` on `2026-07` is schema-only: the top-level `dimension`, `metric`, `vector_type`, and `spec` of earlier versions are replaced by the `schema`. Existing indexes are unaffected, and the SDK keeps the old create-index call working (see below).

## Two kinds of indexes on `2026-07`

`2026-07` gives you two kinds of index. A vector index is the classic index you already use: dense and sparse vectors, read and written through the Vectors API. A document index is new — its schema can hold dense-vector, sparse-vector, and full-text fields in one index, read and written through the Documents API.

|                     | Vector index                                                              | Document index (new)                                                  |
| ------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Create with         | `pc.create_index(dimension=..., metric=..., vector_type=...)` (unchanged) | `pc.indexes.create(schema=...)`                                       |
| Read and write with | `index.upsert`, `index.query`, `index.fetch`                              | `index.documents.*` (`upsert`, `search`, `fetch`, `update`, `delete`) |
| Full-text search    | Not available                                                             | Declare full-text fields in the schema                                |

In the SDK, your existing `pc.create_index(dimension=..., metric=..., vector_type=...)` code is unchanged and still creates a vector index; the SDK maps it to a schema for you. To create a document index, call `pc.indexes.create` with a `schema`. A request uses one or the other, not both.

## What this means for your existing code

An index's data plane is fixed when the index is created, not by the API version or SDK you call it with.

* An index created before `2026-07` uses the Vectors API for its entire life, even after you upgrade your SDK. Indexes that use integrated embedding use the Records API instead.
* An index created on `2026-07` or later with a schema uses the Documents API.

So your existing code keeps working, whether or not you upgrade the SDK. Upgrading doesn't move an index you created before `2026-07` onto the Documents API, or change how you query and upsert to it, and `create_index` in the `2026-07` SDK still accepts the old parameters.

<Note>
  If you call the REST API directly on `2026-07`, `POST /indexes` is schema-based. To create a classic vector index, use a schema with only the reserved `_values` (dense) and/or `_sparse_values` (sparse) fields, which replace the old top-level `dimension`, `metric`, and `vector_type`. To keep sending the original request body instead, pin an earlier API version (`2026-04`).
</Note>

Upgrading the SDK does change the control plane. Beyond `create_index`, index-management calls like `describe_index` and `list_indexes` return the new model shape: the top-level `dimension`, `metric`, and `vector_type` are replaced by a `schema` object, so `dimension` now appears inside the schema's dense-vector field. Update any code that reads those top-level fields when you upgrade.

Each index supports exactly one data plane. A request sent to the wrong data-plane API is refused, and the error guides you to the correct API.

## Adopt schema-based indexes

You can't convert an existing index to a schema-based one. To use a schema (and full-text search), create a new index with the schema you want and ingest your data into it.

1. Upgrade to the `2026-07` Python SDK (v10 or later), or use the REST API. Node.js and other SDKs for the Documents API are coming soon.
2. [Create a new index](/guides/index-data/create-an-index) with the [schema](/guides/index-data/data-modeling) you want. Add a `deployment` only if you need a specific deployment type, cloud, or region; otherwise it defaults to managed serverless.
3. Ingest your data into it.

## FAQ

<AccordionGroup>
  <Accordion title="I use hybrid search (dense + sparse, Vectors API). What happens?">
    Your existing hybrid indexes keep working through the Vectors API, with the same single combined query. On the Documents API, a schema can declare both a `dense_vector` and a `sparse_vector` field, so one index holds both, but a search ranks by one scoring type per request. There's no single combined dense + sparse query, so to combine results, run each search separately and fuse them client-side with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).
  </Accordion>

  <Accordion title="I use integrated embedding (the Records API). Does anything change?">
    No. The Records API and `create_index_for_model` are unaffected, so your integrated-embedding indexes keep working exactly as they do today. Integrated embedding isn't available on schema-based (document) indexes; keep creating integrated-inference indexes the way you do now.
  </Accordion>

  <Accordion title="Can I keep creating indexes on the old Vectors API?">
    Yes. In the `2026-07` SDK, your existing `create_index(dimension=..., metric=..., vector_type=..., spec=...)` code works unchanged and still creates a vector index, so you don't have to downgrade. If you call the REST API directly on `2026-07`, use a schema with the reserved `_values`/`_sparse_values` fields, or pin an earlier API version (`X-Pinecone-Api-Version: 2026-04`) to send the original request body. Indexes you create either way stay on the `/vectors/*` data plane.
  </Accordion>

  <Accordion title="I'm on 2026-01.alpha. What changed for me?">
    `2026-01.alpha` is now a mirror of `2026-07`. If you were already using a schema and the Documents API, nothing changes.
  </Accordion>
</AccordionGroup>
