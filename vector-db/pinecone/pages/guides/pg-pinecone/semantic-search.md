---
title: "Search a table with semantic search"
source: https://docs.pinecone.io/guides/pg-pinecone/semantic-search
path: guides/pg-pinecone/semantic-search
---

Search a Postgres table by meaning in SQL, with a hosted embedding model or your own vectors, using a Pinecone index that pg_pinecone keeps in sync.

pg_pinecone can rank a Postgres table's rows by meaning with [semantic search](/guides/search/semantic-search), using a Pinecone index it keeps in sync with the table. Pinecone can embed one of the table's text columns with a hosted model, or you can store your own vectors in a vector column.

## Before you begin

* [pg_pinecone installed](/guides/pg-pinecone/quickstart).
* A Pinecone API key stored in the database. Store it with `SELECT pinecone.set_api_key('YOUR_API_KEY');`.
* `pg_pinecone` in `shared_preload_libraries`, followed by a Postgres restart. See [Preload the extension](/guides/pg-pinecone/switch-to-remote#preload-the-extension).
* A table with a single-column primary key, which becomes each document's ID. You must own the table.
* A Pinecone plan that includes the hosted model you use. For example, [`gemini-embedding-2`](/models/gemini-embedding-2) requires a Builder, Standard, or Enterprise plan.

## Search by meaning

### 1. Create a sample table

This guide uses a table of notes:

```sql SQL theme={null}
CREATE TABLE notes (
    id       bigint PRIMARY KEY,
    body     text,
    category text
);

INSERT INTO notes (id, body, category) VALUES
    (1, 'Semantic search finds documents by concept rather than by exact keyword matches.', 'search'),
    (2, 'Our office closes at 5 PM on Fridays.', 'admin'),
    (3, 'Vector embeddings capture the meaning of text so similar ideas land close together.', 'search'),
    (4, 'Remember to submit expense reports by the end of the month.', 'admin');
```

### 2. Embed a text column

Call `pinecone.track_docs()` and give one text column an `embed` option. Pinecone then embeds that column's text with a hosted model on every write and every query, using [integrated embedding](/guides/search/integrated-embedding):

```sql SQL theme={null}
SELECT pinecone.track_docs('notes',
    text_columns     => '{"body": {"language": "en", "embed": {"model": "gemini-embedding-2"}}}',
    metadata_columns => ARRAY['category']);
```

This creates a Pinecone index and copies the table's existing rows to it, then keeps it in sync. To check when the initial copy is done, see the [full-text search guide](/guides/pg-pinecone/full-text-search#wait-for-the-initial-copy).

### 3. Search the table

Search with `mode => 'embed'`. Pinecone embeds the query with the same model and ranks rows by similarity:

```sql SQL theme={null}
SELECT n.id, n.body, s.score
FROM pinecone.search_docs('notes', 'finding information by concept instead of exact words',
       mode => 'embed', k => 3) s
JOIN notes n ON n.id = s.id::bigint
ORDER BY s.rank;
```

The two notes about search rank first, though neither contains the words "finding information":

```text Output theme={null}
 id |                                        body                                         |   score
----+-------------------------------------------------------------------------------------+-----------
  1 | Semantic search finds documents by concept rather than by exact keyword matches.    | 0.8373871
  3 | Vector embeddings capture the meaning of text so similar ideas land close together. | 0.7104721
  4 | Remember to submit expense reports by the end of the month.                         | 0.5482254
```

Keep these points in mind:

* **Model settings**: pg_pinecone passes the `embed` object to Pinecone. `model` is required, and you can also set `dimension`, `metric`, `processing_location`, `write_parameters`, and `read_parameters`. Pinecone fills in defaults for anything you leave out.
* **Keyword and semantic search on one column**: The column keeps its full-text index, so `mode => 'text'` still ranks it with BM25. Semantic and BM25 scores use different scales. To rank by both, run two searches and merge the results by rank.
* **Filters**: `mode => 'embed'` works with `filter` and `must`, so you can rank by meaning within rows that match a metadata value or required text. For examples, see the [full-text search guide](/guides/pg-pinecone/full-text-search#filter-results).
* **One embedded column**: Only one text column can set `embed`, and you can't combine it with `vector_column`.
* **Empty text**: A row whose `embed` column is `NULL` or blank isn't indexed. If Pinecone already has a copy of that row, pg_pinecone deletes it.

## Combine text and vector search

If your table already stores embeddings, declare the column with `vector_column` instead of using `embed`. Then pass a query vector with `vector`, and name the column the text query must match with `field`. The text query narrows the results to rows that match it in that column, and the vector ranks what's left.

This example uses the `articles` table from [Search a table with full-text search](/guides/pg-pinecone/full-text-search), which declares `vector_column => 'embedding'`:

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

## Embed a field on an index directly

To embed a field on an index that isn't tied to a table, add the same `embed` object to the field in `pinecone.create_doc_index()`, then search it with an `embed` clause in `pinecone.search_doc_index()`:

```sql SQL theme={null}
SELECT pinecone.create_doc_index('faq-semantic',
  '{"fields": {"question": {"type": "string", "full_text_search": {"language": "en"},
                            "embed": {"model": "gemini-embedding-2"}}}}');

SELECT id, score
FROM pinecone.search_doc_index('faq-semantic',
  '{"type": "embed", "fields": ["question"], "query": "billing statements"}', k => 3);
```

To add documents with `pinecone.upsert_docs()` and delete the index with `pinecone.drop_doc_index()`, see the [full-text search guide](/guides/pg-pinecone/full-text-search#search-an-index-directly).
