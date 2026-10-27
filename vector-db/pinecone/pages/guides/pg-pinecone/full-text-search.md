---
title: "Search a table with full-text search"
source: https://docs.pinecone.io/guides/pg-pinecone/full-text-search
path: guides/pg-pinecone/full-text-search
---

Use pg_pinecone to keep a Pinecone index for full-text search in sync with a Postgres table, then run BM25, filtered, and hybrid searches in SQL.

pg\_pinecone can keep a Pinecone index for [full-text search](/guides/search/full-text-search) in sync with a Postgres table's text columns. You declare the searchable columns once and search them with SQL, and Postgres stays the system of record.

## Before you begin

* pg\_pinecone installed, as the [quickstart](/guides/pg-pinecone/quickstart) shows.
* A Pinecone API key stored in the database. Store it with `SELECT pinecone.set_api_key('YOUR_API_KEY');`.
* `pg_pinecone` in `shared_preload_libraries`, followed by a Postgres restart. See [Preload the extension](/guides/pg-pinecone/switch-to-remote#preload-the-extension).
* A table with a single-column primary key, which becomes each document's ID. You must own the table.

## Search a table

### 1. Create a sample table

This guide uses a table of help-center articles. The embeddings are only needed to [combine text and vector search](#combine-text-and-vector-search):

```sql SQL theme={null}
CREATE TABLE articles (
    id        bigint PRIMARY KEY,
    title     text,
    body      text,
    category  text,
    embedding vector(1024)
);

WITH input(id, title, body, category) AS (
    VALUES
        (1, 'Reset your password', 'Open Settings, choose Security, and select Reset password. A reset link arrives by email within a few minutes.', 'account'),
        (2, 'Enable two-factor authentication', 'Two-factor authentication adds a one-time code from an authenticator app to every sign-in.', 'account'),
        (3, 'Export your data', 'Go to Settings and choose Export to download every project as a CSV file.', 'data'),
        (4, 'Fix error E-1042 during import', 'Error E-1042 means the CSV file has a header row that does not match the table columns.', 'data'),
        (5, 'Change your billing plan', 'Upgrade or downgrade your plan from the Billing page. Changes take effect at the next invoice.', 'billing'),
        (6, 'Download past invoices', 'Every invoice is available as a PDF on the Billing page under Invoice history.', 'billing')
)
INSERT INTO articles (id, title, body, category, embedding)
SELECT i.id, i.title, i.body, i.category, e.embedding::vector
FROM input i
JOIN pinecone.embed_batch((SELECT array_agg(title || '. ' || body ORDER BY id) FROM input)) e
  ON e.ordinal = i.id;
```

### 2. Declare the searchable columns

Call `pinecone.track_docs()` with the text columns to index. `metadata_columns` lists columns you want to filter on, and `vector_column` is optional. `text_columns` takes a JSON list, and `metadata_columns` takes a Postgres array:

```sql SQL theme={null}
SELECT pinecone.track_docs(
    'articles',
    text_columns     => '["title", "body"]',
    metadata_columns => ARRAY['category'],
    vector_column    => 'embedding'
);
```

This creates a Pinecone index and queues the table's existing rows to be copied to it. Only the declared columns leave Postgres. From then on, pg\_pinecone copies every committed insert, update, and delete in the background.

A list of column names uses English text analysis with stemming and stop words. To set options per column, pass an object instead. For example, on a table with a `sku` column, turn off stemming and stop words so identifiers match exactly:

```sql SQL theme={null}
text_columns => '{"title": {"language": "en"}, "sku": {"stemming": false, "stop_words": false}}'
```

### 3. Wait for the initial copy

Check progress with `pinecone.status()`:

```sql SQL theme={null}
SELECT table_name, docs_backfill_done, docs_backfill_total, docs_queue_state
FROM pinecone.status();
```

The copy is finished when `docs_backfill_done` equals `docs_backfill_total`. `pinecone.flush_docs('articles')` waits until everything committed so far has been delivered, then returns `true`. It returns `false` if delivery doesn't finish within 30 seconds. Pinecone then takes up to about a minute to index delivered documents and make them searchable.

### 4. Search the table

`pinecone.search_docs()` returns each match's ID, score, and rank. Join back to the table for the rest of the row:

```sql SQL theme={null}
SELECT a.id, a.title, s.score
FROM pinecone.search_docs('articles', 'download invoice pdf', k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

```text Output theme={null}
 id |          title           |   score
----+--------------------------+-----------
  6 | Download past invoices   |  6.580365
  3 | Export your data         | 1.6908139
  5 | Change your billing plan | 1.0116261
```

Pinecone ranks results with BM25. Because the join reads the table with your own privileges, it respects row-level security and drops any row deleted since the last sync.

## Filter results

Use `filter` to restrict results by metadata columns, and `must` to require text in a column:

```sql SQL theme={null}
-- Only articles in the account category
SELECT a.id, a.title
FROM pinecone.search_docs('articles', 'settings',
       filter => '{"category": {"$eq": "account"}}', k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;

-- Only articles whose body contains the exact error code
SELECT a.id, a.title
FROM pinecone.search_docs('articles', 'import error',
       must => '{"body": {"$match_phrase": "E-1042"}}', k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

`must` accepts `$match_phrase`, `$match_all`, and `$match_any`. For the operators `filter` accepts, see [Filter operators](/guides/search/full-text-search#filter-operators).

To write the whole query in [Lucene syntax](/guides/search/full-text-search/query-syntax), set `mode => 'query_string'`:

```sql SQL theme={null}
SELECT a.id, a.title
FROM pinecone.search_docs('articles', 'title:(password OR invoices) -body:email',
       mode => 'query_string', k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

## Combine text and vector search

If you declared a `vector_column`, pass a query vector with `vector`, and name the column the text query must match with `field`. The text query narrows the results to rows that match it in that column, and the vector ranks what's left:

```sql SQL theme={null}
SELECT a.id, a.title
FROM pinecone.search_docs('articles', 'billing', field => 'body',
       vector => pinecone.embed('how do I get a receipt for my payment'), k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

```text Output theme={null}
 id |          title
----+--------------------------
  6 | Download past invoices
  5 | Change your billing plan
```

## Search one tenant

To keep each tenant's documents in their own Pinecone [namespace](/guides/index-data/indexing-overview#namespaces), pass a tenant column as `partition_column` when you call `pinecone.track_docs()`. Then name the tenant with `partition` on every search. This example uses a `tickets` table with a `tenant_id` column:

```sql SQL theme={null}
SELECT pinecone.track_docs('tickets',
    text_columns     => '["title", "body"]',
    partition_column => 'tenant_id');

SELECT s.id, s.score
FROM pinecone.search_docs('tickets', 'invoice pdf', partition => 42, k => 10) s;
```

A search covers exactly one tenant, and BM25 scores are calculated within that tenant's documents. A search without `partition` returns an error. With [`engine => 'local'`](#search-without-pinecone), `partition` becomes a condition on the column instead. `pinecone.delete_partition('tickets', 42)` deletes one tenant's documents from Pinecone, and its rows stay in the table.

The partition column must be `NOT NULL`. Pinecone limits the number of namespaces per index by plan, and pg\_pinecone warns when a table has more than 1,000 distinct values.

## Highlight matches

`pinecone.headline()` marks the query terms in a column's text, using the language you declared for that column:

```sql SQL theme={null}
SELECT a.id, pinecone.headline('articles', 'body', a.body, 'download invoice pdf') AS snippet
FROM pinecone.search_docs('articles', 'download invoice pdf', k => 2) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

```text Output theme={null}
 id |                                               snippet
----+-----------------------------------------------------------------------------------------------------
  6 | Every <b>invoice</b> is available as a <b>PDF</b> on the Billing page under <b>Invoice</b> history.
  3 | Go to Settings and choose Export to <b>download</b> every project as a CSV file.
```

## Search without Pinecone

Set `engine => 'local'` to answer the same call with Postgres's built-in full-text search instead of Pinecone:

```sql SQL theme={null}
SELECT a.id, a.title, s.score
FROM pinecone.search_docs('articles', 'download invoice', engine => 'local', k => 3) s
JOIN articles a ON a.id = s.id::bigint
ORDER BY s.rank;
```

The local engine reflects writes immediately. It also works on tables you haven't declared with `track_docs()` if you name a column with `field`. It ranks results with Postgres's `ts_rank_cd` instead of BM25 and requires every query word to match, so it can return fewer results than the remote engine, in a different order. It doesn't support `filter`, `must`, `vector`, or `mode => 'query_string'`, and it doesn't create an index, so add a [GIN index](https://www.postgresql.org/docs/current/textsearch-indexes.html) on large tables.

## Manage a tracked table

Once a table is tracked, pg\_pinecone keeps its Pinecone index in sync on its own. These functions handle the cases that need your attention:

* **Retry rejected documents**: If Pinecone rejects a document, pg\_pinecone sets it aside without stopping the rest of the table. `pinecone.failed_docs('articles')` lists rejected documents and why, and `pinecone.retry_failed_docs('articles')` queues them again.
* **Re-send every row**: `pinecone.backfill_docs('articles', clear => true)` copies the whole table again, for example after restoring a database backup.
* **Change a declared column**: Stop tracking the table before you drop, rename, or change the type of a declared column.
* **Stop tracking**: `pinecone.untrack_docs('articles', drop_index => true)` stops syncing and deletes the Pinecone index.

## Search an index directly

To work with a Pinecone index for full-text search that isn't tied to a table, use `pinecone.create_doc_index()`, `pinecone.upsert_docs()`, and `pinecone.search_doc_index()`:

```sql SQL theme={null}
SELECT pinecone.create_doc_index('faq',
  '{"fields": {"question": {"type": "string", "full_text_search": {"language": "en"}}}}');

SELECT pinecone.upsert_docs('faq',
  '[{"_id": "q1", "question": "How do I cancel my subscription?"},
    {"_id": "q2", "question": "Where can I find my invoices?"}]');

SELECT id, score
FROM pinecone.search_doc_index('faq',
  '{"type": "text", "fields": ["question"], "query": "invoices"}', k => 3);
```

Upserted documents become searchable shortly after Pinecone indexes them, so a search run immediately after an upsert may return nothing. The schema and query use the same JSON as the [Documents API](/guides/search/full-text-search).

To delete the index when you're done:

```sql SQL theme={null}
SELECT pinecone.drop_doc_index('faq');
```
