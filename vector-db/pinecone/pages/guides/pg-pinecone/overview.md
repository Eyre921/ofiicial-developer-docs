---
title: "pg_pinecone"
source: https://docs.pinecone.io/guides/pg-pinecone/overview
path: guides/pg-pinecone/overview
---

pg_pinecone is an open-source PostgreSQL extension that runs the search engine Pinecone uses at scale inside Postgres, or on an index in Pinecone's cloud.

pg\_pinecone is an open-source PostgreSQL extension, licensed under [Apache 2.0](https://github.com/pinecone-io/pg_pinecone/blob/main/LICENSE), that brings Pinecone's vector search into the Postgres database you already run. It runs on PostgreSQL 17 and 18 servers you manage yourself, because installing it needs superuser access. The `remote` engine and full-text search also need a server setting.

> **[Quickstart](/guides/pg-pinecone/quickstart)**
>
> Install the extension and search a table with a native index.

> **[Storage engines](/guides/pg-pinecone/storage-engines)**
>
> The pgvector, native, and remote engines, and when to use each.

> **[Switch from pgvector to native](/guides/pg-pinecone/switch-from-pgvector)**
>
> Replace a table's pgvector index with a native index.

> **[Switch from native to remote](/guides/pg-pinecone/switch-to-remote)**
>
> Switch a table to the remote engine when it outgrows one server.

## How it works

pg\_pinecone has three engines for a table's vector search:

* **`pgvector`**: Uses pgvector's own index, the same one you'd run without pg\_pinecone.
* **`native`**: The default. Runs the search engine Pinecone uses at scale, inside your Postgres database. It doesn't call Pinecone.
* **`remote`**: Runs the search on an index in Pinecone's cloud instead, for a table that outgrows one server.

Your tables and queries stay the same on every engine, and you switch a table between `native` and `remote` with one SQL call. Every switch can be reversed. Postgres keeps every row on every engine, including `remote`, so switching back rebuilds an index from data already in your database.

### Architecture

![An application sends pgvector SQL to Postgres, which keeps the rows and their vector column. pg\_pinecone searches them with the native engine (the default), the pgvector engine, or the remote engine, which syncs to a Pinecone serverless index and returns the results.](https://mintcdn.com/pinecone/qIfhVY6y5p5rJ02f/images/pg-pinecone/pg-pinecone-overview-light.svg?fit=max\&auto=format\&n=qIfhVY6y5p5rJ02f\&q=85\&s=a925c57ae6c04da11de0bda31fb8041a)

The diagram names these index types:

* **HNSW** (Hierarchical Navigable Small World): A graph index in pgvector. Each vector links to its nearest neighbors, and a search follows those links toward the query.
* **IVFFlat**: A clustered index in pgvector. It groups vectors into lists and compares the query with the full vectors in the lists nearest to it.
* **IVF + RaBitQ**: How the `native` engine searches. IVF (inverted file) groups vectors into clusters the same way, and RaBitQ stores each vector as a short binary code, so the index is small and quick to scan. The closest matches are then rechecked against the full vectors.

## Features

* **Filtered search**: With a [filter column](/guides/pg-pinecone/storage-engines#filter-column), the `native` engine applies a filter, such as a tenant ID, during the search, so filtered queries return a full set of results. It runs in your database without an account or network access.
* **Scale**: The `remote` engine moves a table's vector search to a Pinecone index, and Postgres keeps the rows.
* **Unchanged queries**: A pgvector query like `ORDER BY embedding <=> $1` works the same on every engine.
* **Tenant isolation**: With the `remote` engine, each tenant can have its own Pinecone namespace, so a query searches only that tenant's data.
* **Full-text search**: pg\_pinecone keeps a Pinecone index for full-text search in sync with a table's text columns, and you run BM25, vector, or hybrid searches on it from SQL.
* **SQL functions**: You can generate embeddings and rerank results in SQL. See the [SQL reference](https://github.com/pinecone-io/pg_pinecone/blob/main/docs/reference.md).

## Choose your path

* **New to vector search**: The [quickstart](/guides/pg-pinecone/quickstart) creates a table with embeddings and searches it with a `native` index.
* **Already using pgvector**: [Switch from pgvector to native](/guides/pg-pinecone/switch-from-pgvector).
* **Outgrowing one server**: [Switch from native to remote](/guides/pg-pinecone/switch-to-remote), so Pinecone serves the table's vector search.
* **Leaving Postgres**: [Migrate from pgvector](/guides/index-data/migrate-from-pgvector) moves your data into Pinecone Database.
