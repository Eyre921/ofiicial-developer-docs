---
title: "Switch from pgvector to native"
source: https://docs.pinecone.io/guides/pg-pinecone/switch-from-pgvector
path: guides/pg-pinecone/switch-from-pgvector
---

Replace a table's pgvector index with a pg_pinecone native index without changing your queries, and switch back to pgvector if you need to.

A table with a pgvector index, such as an [HNSW index](https://github.com/pgvector/pgvector#hnsw), is on the `pgvector` engine. You can switch it to `native`, which runs the search engine Pinecone uses at scale inside Postgres. Your queries and data stay the same, and you can [switch back to pgvector](#switch-back-to-pgvector) at any time.

## Before you begin

* pg\_pinecone installed and created in the database, as steps 1 and 2 of the [quickstart](/guides/pg-pinecone/quickstart) show.
* A table with a `vector` column and a pgvector index on that column created with `CREATE INDEX`. If `pinecone.create_index()` built the pgvector index instead, skip this guide and switch it with one call: `SELECT pinecone.set_engine('your_table', 'native');`.
* A single-column primary key, if you plan to [switch to `remote`](/guides/pg-pinecone/switch-to-remote) later. A `native` index doesn't need one.

## Replace the index

### 1. Create a native index

Create a `native` index on the table's `vector` column. The pgvector index keeps serving queries while the `native` index builds:

```sql SQL theme={null}
SELECT pinecone.create_index('your_table', 'embedding', engine => 'native');
```

`pinecone.create_index()` uses cosine distance by default. If your pgvector index uses a different distance, pass the matching `metric`: `'l2'` for `vector_l2_ops`, or `'ip'` for `vector_ip_ops`.

If your queries filter on one column, such as a tenant ID, add it as a filter column with `filter_column => 'tenant_id'`. See [Filter column](/guides/pg-pinecone/storage-engines#filter-column).

### 2. Drop the pgvector index

```sql SQL theme={null}
DROP INDEX your_hnsw_index;
```

Your queries now use the `native` index.

### 3. Check which index serves queries

Run `EXPLAIN` on a similarity query. This one uses a row's own vector as the query:

```sql SQL theme={null}
EXPLAIN (COSTS OFF)
SELECT id FROM your_table
ORDER BY embedding <=> (SELECT embedding FROM your_table LIMIT 1)
LIMIT 10;
```

The plan includes `Index Scan using your_table_embedding_pinecone_idx`. `pinecone.create_index()` names the index `<table>_<column>_pinecone_idx`. On a small table, Postgres may choose to read every row instead of using any index, because that's cheaper.

## Switch back to pgvector

If the table uses the `remote` engine, [switch it back to `native`](/guides/pg-pinecone/switch-to-remote#switch-back-to-native) first.

### 1. Drop the native index

```sql SQL theme={null}
DROP INDEX your_table_embedding_pinecone_idx;
```

Until the pgvector index exists, queries on the table read every row.

### 2. Create the pgvector index

```sql SQL theme={null}
CREATE INDEX your_hnsw_index ON your_table USING hnsw (embedding vector_cosine_ops);
```

Postgres builds the index from the vectors already in the table.
