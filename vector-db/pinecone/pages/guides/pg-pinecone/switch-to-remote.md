---
title: "Switch from native to remote"
source: https://docs.pinecone.io/guides/pg-pinecone/switch-to-remote
path: guides/pg-pinecone/switch-to-remote
---

Switch a pg_pinecone table from the native engine to the remote engine, so Pinecone serves its vector search while Postgres keeps the rows.

When a table outgrows a single Postgres server, you can move its vector search to Pinecone by switching the table to the `remote` engine. Pinecone stores a copy of the vectors and answers the table's similarity queries, and Postgres keeps every row. Your queries don't change, and you can [switch back to native](#switch-back-to-native) at any time.

## Before you begin

* pg\_pinecone installed, as the [quickstart](/guides/pg-pinecone/quickstart) shows.
* A Pinecone API key stored in the database, which the `remote` engine needs even if you bring your own vectors. Store it with `SELECT pinecone.set_api_key('YOUR_API_KEY');`.
* A table with a `native` index. The examples use the `docs` table from the quickstart, so skip the quickstart's clean-up step if you want to follow along.

## Switch to the remote engine

The `remote` engine relies on a background worker that copies writes to Pinecone, and Postgres starts that worker only when the extension is preloaded.

### 1. Preload the extension

Add `pg_pinecone` to `shared_preload_libraries` in `postgresql.conf`. To find the file, run `SHOW config_file;` in `psql`. If the setting already lists other libraries, add `pg_pinecone` to the list:

```ini postgresql.conf theme={null}
shared_preload_libraries = 'pg_pinecone'
```

Then restart Postgres. For example, `sudo systemctl restart postgresql` on most Linux installs, or `brew services restart postgresql@17` with Homebrew on macOS.

### 2. Switch the engine

Reconnect and switch the table to the `remote` engine:

```sql SQL theme={null}
SELECT pinecone.set_engine('docs', 'remote');
```

This creates a serverless index in your Pinecone project and starts copying the table's vectors to it in the background. The index is created in `aws` `us-east-1` unless you set `pinecone.am_cloud` and `pinecone.am_region` first. While the copy runs, queries keep using the `native` index, so reads and writes aren't interrupted.

### 3. Wait for the copy to finish

Check progress with `pinecone.status()`:

```sql SQL theme={null}
SELECT table_name, mode, index_name, backlog FROM pinecone.status();
```

`mode` is `promoting` while the copy runs. When `mode` is `remote` and `backlog` is `0`, Pinecone is serving the table's queries. In version 0.10.0 and later, a table of a million rows takes up to about an hour to copy at the default settings.

### 4. Run the same query

Run the quickstart's query again, unchanged:

**Your own vectors**

```sql SQL theme={null}
SET enable_seqscan = off;

SELECT id, body
FROM docs
ORDER BY embedding <=> '[1, 0, 0]'
LIMIT 2;
```

**Pinecone embeddings**

```sql SQL theme={null}
SET enable_seqscan = off;

SELECT id, body
FROM docs
ORDER BY embedding <=> (SELECT pinecone.embed('What should I order for breakfast at a cafe?')::vector)
LIMIT 2;
```

Pinecone now serves the results. The new index also appears in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes) under the name `pinecone.status()` reports.

New writes to the table reach Pinecone within a few seconds, so a query run immediately after a write may not reflect it yet. See [Consistency with the remote engine](/guides/pg-pinecone/storage-engines#consistency-with-the-remote-engine) for details.

## Switch back to native

Switching back moves the table's search into Postgres again. Postgres still has every row, so nothing is copied back from Pinecone. The rebuild blocks queries and writes on the table while it runs, as [Switching engines](/guides/pg-pinecone/storage-engines#switching-engines) explains, so plan it for a quiet period.

### 1. Switch the engine back

```sql SQL theme={null}
SELECT pinecone.set_engine('docs', 'native');
```

pg\_pinecone rebuilds the `native` index from the table, then deletes the Pinecone index it created.

### 2. Check that the switch finished

```sql SQL theme={null}
SELECT table_name, mode FROM pinecone.status();
```

The table is back on `native` when it no longer appears in the results. The rebuild runs in the background, so the table can still show `remote` for a few seconds on a small table, or longer on a large one.

## Query the index from your application

The Pinecone index that the `remote` engine creates is a standard [Pinecone Database](/guides/get-started/overview) index, so your application can also query it directly with a [Pinecone SDK](/reference/sdks/python/overview). The table's records are in a namespace named after the table, such as `public.docs`, so pass that namespace in your query. Its record IDs are Postgres row locations in `block:offset` form, not your primary key values, so look up matching rows through Postgres. To move a workload off Postgres entirely, see [Migrate from pgvector](/guides/index-data/migrate-from-pgvector).
