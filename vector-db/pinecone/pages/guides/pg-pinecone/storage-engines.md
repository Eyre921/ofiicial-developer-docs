---
title: "pg_pinecone storage engines"
source: https://docs.pinecone.io/guides/pg-pinecone/storage-engines
path: guides/pg-pinecone/storage-engines
---

Learn how pg_pinecone's pgvector, native, and remote storage engines work, when to use each, and how to switch between them.

pg\_pinecone searches a table's vector column with one of three engines: `pgvector` or `native` inside Postgres, or `remote` on Pinecone. The engine is a setting on the table's one pg\_pinecone index, so you switch engines per table. Your queries are the same on all three, so you can change engines without touching application code:

```sql SQL theme={null}
SELECT id, body FROM docs ORDER BY embedding <=> $1 LIMIT 10;
```

## The engines

| Engine | What it is | Where vectors are searched | Needs a Pinecone account |
| - | - | - | - |
| `pgvector` | pgvector's own index, such as HNSW. | In Postgres | No |
| `native` | The search engine Pinecone uses at scale, running inside Postgres. This is the default. | In Postgres | No |
| `remote` | A Pinecone Database index, kept in sync with your table. | In Pinecone | Yes |

If you create an index without choosing an engine, you get `native`. A pgvector index that a table already has stays in place until you replace it.

A `native` index built on fewer than 10,000 rows compares each query with every row. That's exact, but it slows down as the table grows, so create the index after you load your data, or rebuild it with `REINDEX` once the table is larger.

Postgres stays the system of record with every engine. Your rows, including the vector column, live in Postgres, and the engine only decides which index answers similarity queries.

## When to use each engine

* **`pgvector`**: A table that already has a pgvector index and doesn't filter its searches. You can keep that index and add pg\_pinecone without changing anything.
* **`native`**: Filtered search, especially when the rows that match a filter are clustered, such as per-tenant data queried with `WHERE tenant_id = $1`. The `native` engine scans by cluster, so it keeps finding matches where a graph index like pgvector's [HNSW](https://github.com/pgvector/pgvector#hnsw) can miss them. It runs without an account or network access.
* **`remote`**: A table that has outgrown a single Postgres server. Pinecone stores and searches the vectors, and Postgres keeps the rest of the row.

## Switching engines

You switch a table between `native` and `remote` with one call to `pinecone.set_engine()`, in either direction:

* **To `remote`**: pg\_pinecone creates a Pinecone index and copies the table's vectors to it in the background. Queries keep using the `native` index until the copy finishes, and new writes go to both, so reads and writes are never interrupted. In version 0.10.0 and later, a table of a million rows takes up to about an hour to copy at the default settings.
* **To `native`**: pg\_pinecone queues a rebuild of the `native` index and keeps serving queries from Pinecone until the rebuild starts. The rebuild blocks reads that use the index, and writes to the table, until it finishes. That usually takes seconds to a few minutes, depending on table size. After the rebuild, pg\_pinecone deletes the Pinecone index it created.

To switch a pgvector index you created with `CREATE INDEX` to `native`, create the `native` index with `pinecone.create_index()`, then drop the pgvector index. A pgvector index that `pinecone.create_index()` built switches with one call, `pinecone.set_engine('your_table', 'native')`. To switch from `native` back to `pgvector`, drop the `native` index and create the pgvector index again.

Every switch can be reversed, and none of them loses data. Postgres keeps every row, including the vector column, on every engine, so switching back rebuilds an index from the table.

[Switch from pgvector to native](/guides/pg-pinecone/switch-from-pgvector) and [Switch from native to remote](/guides/pg-pinecone/switch-to-remote) walk through each switch.

## Filtered and multi-tenant tables

An index can cover one extra column besides the vector, either as a filter column or as a partition column. Both apply to queries that include `WHERE column = value`.

### Filter column

A filter column narrows the search inside the index instead of after it. Set it with `filter_column` when you create a `native` or `remote` index:

```sql SQL theme={null}
SELECT pinecone.create_index('docs', 'embedding', engine => 'native', filter_column => 'tenant_id');

SELECT id, body FROM docs
WHERE tenant_id = $1
ORDER BY embedding <=> $2
LIMIT 10;
```

* **On `native`**: The engine applies the filter while it scans.
* **On `remote`**: pg\_pinecone stores the column as Pinecone metadata and sends `WHERE tenant_id = $1` to Pinecone as a [metadata filter](/guides/search/filter-by-metadata). A filtered `native` index keeps its filter column when you switch it to `remote`.
* **Other conditions**: Only `=` on the filter column is applied inside the index. Any other condition, such as a range or a second column, is applied to each batch the index returns, so a selective one can leave fewer rows than `LIMIT`. On `native`, the scan keeps going until the query has enough rows, because `pinecone.iterative_scan` defaults to `auto`. On `remote`, the scan asks Pinecone for more rows, up to 10,000, and returns an error if that's still not enough. To return the rows found instead, run `SET pinecone.iterative_scan = 'relaxed_order'`. Rows after the first batch arrive in batch order, so re-sort them if exact order matters. On the `pgvector` engine, use pgvector's own [`hnsw.iterative_scan`](https://github.com/pgvector/pgvector#iterative-index-scans) instead.

The filter column must be a `smallint`, `integer`, `bigint`, `text`, or `varchar` column.

### Partition column

A partition column gives each value its own Pinecone [namespace](/guides/index-data/indexing-overview#namespaces), so each tenant's vectors are stored and searched separately. It applies to the `remote` engine:

```sql SQL theme={null}
SELECT pinecone.create_index('docs', 'embedding', engine => 'remote', partition_column => 'tenant_id');
```

* **Namespaces**: Each value maps to a namespace named `<schema>.<table>:<value>`, such as `public.docs:42`.
* **Queries**: Every query must include `WHERE tenant_id = <value>`, and it searches only that tenant's namespace. A query without it returns an error instead of searching across tenants.
* **Removing a tenant**: `pinecone.delete_partition('docs', 42)` deletes that tenant's namespace. Its rows stay in the table.
* **Limits**: The column must be `NOT NULL`. Pinecone limits the number of namespaces per index by plan, and pg\_pinecone warns when a table has more than 1,000 distinct values.

You can also set `partition_column` when you switch a filtered `native` index to `remote` with `pinecone.set_engine()`.

## Consistency with the remote engine

When a table uses the `remote` engine, each committed write is queued in Postgres and copied to Pinecone by a background worker, usually within a few seconds. Under heavy write load, the queue can fall behind, and new rows can take minutes to become searchable.

* **No read-your-writes**: A query run right after a write may not reflect it yet.
* **Rolled-back writes never reach Pinecone**: Only committed changes are queued.
* **Postgres keeps working if Pinecone is unreachable**: Writes still commit in Postgres, and the queue holds them and retries while Pinecone is unavailable.
* **Searches aren't retried**: If Pinecone rejects a search because of a rate limit or a server error, the query fails immediately. Retry with backoff in your application, or spread tenants across namespaces with a [partition column](#partition-column).

`pinecone.status()` lists each table that syncs to Pinecone, with its `mode` and how many writes are still queued (`backlog`). Tables on `native` don't appear. A table whose pgvector index `pinecone.create_index()` built appears with `mode` `local`. The [operator runbook](https://github.com/pinecone-io/pg_pinecone/blob/main/docs/runbook.md) covers monitoring the queue and handling writes that Pinecone rejects.
