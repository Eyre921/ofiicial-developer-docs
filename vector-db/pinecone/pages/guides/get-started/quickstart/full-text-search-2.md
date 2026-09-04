---
title: "Try full-text search"
source: https://docs.pinecone.io/guides/get-started/quickstart/full-text-search
path: guides/get-started/quickstart/full-text-search
---

Create an index, load documents, and run your first full-text (keyword) search in about five minutes.

Full-text search matches exact terms: IDs, SKUs, error codes, and phrases. Create an index, load a few documents, and run a keyword (BM25) search in about five minutes.

## Prerequisites

* A Pinecone account and API key ([get one](https://app.pinecone.io)).
* **Python 3.10+**.
* The Pinecone Python SDK: `pip install --upgrade pinecone`.

## Create an index and search

<Steps>
  <Step title="Set your API key">
    Set your API key as an environment variable so the SDK can authenticate:

    ```bash theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```
  </Step>

  <Step title="Create an index">
    Define a schema with a full-text (BM25) field, then create the index. Only search fields belong in the schema; filterable metadata like `category` goes in the documents and is indexed automatically.

    ```python theme={null}
    import os, time
    from pinecone import Pinecone, SchemaBuilder

    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    schema = (
        SchemaBuilder()
          .add_string_field(name="text", full_text_search={"language": "en"})
          .build()
    )
    if not pc.indexes.exists(name="quickstart"):
        pc.indexes.create(name="quickstart", schema=schema)

    while not pc.indexes.describe(name="quickstart").status.ready:
        time.sleep(2)

    index = pc.Index(name="quickstart")
    ```
  </Step>

  <Step title="Load sample documents">
    Each document is a JSON object with a required `_id`, the `text` field from your schema (indexed for full-text search), and any metadata you want to attach. Here, `category` is metadata: it's not declared in the schema, but Pinecone indexes it automatically so you can filter on it.

    These five short strings are just samples. Real documents can carry many metadata fields (up to 40 KB per document), plus dense- or sparse-vector fields if your schema declares them, and you can upsert up to 1,000 per request.

    ```python theme={null}
    index.documents.upsert(
        namespace="__default__",
        documents=[
            {"_id": "1", "text": "SKU KB-1024: wireless mechanical keyboard, USB-C, brown switches", "category": "product"},
            {"_id": "2", "text": "SKU MON-4200: 27-inch 4K monitor, HDMI and USB-C", "category": "product"},
            {"_id": "3", "text": "Order 88231 shipped on 2026-08-20 via express courier", "category": "order"},
            {"_id": "4", "text": "Error E1042: connection timeout after 30 seconds", "category": "log"},
            {"_id": "5", "text": "Ticket 5567 resolved: replaced faulty power adapter", "category": "support"},
        ],
    )

    time.sleep(5)  # documents are indexed asynchronously, so wait a moment
    ```
  </Step>

  <Step title="Run a full-text search">
    Search the index by choosing a scoring type with `score_by`. Here, `type: "text"` scores documents by BM25 keyword relevance on the `text` field, so an exact identifier like `E1042` surfaces the record that contains it.

    ```python theme={null}
    resp = index.documents.search(
        namespace="__default__",
        top_k=3,
        score_by=[{"type": "text", "fields": ["text"], "query": "E1042"}],
        include_fields=["*"],
    )

    for m in resp.matches:
        print(m._id, m._score, getattr(m, "text", ""))
    ```

    To narrow results, add a `filter` such as `{"category": {"$eq": "product"}}`. For exact phrase matching, use a `query_string` search instead (see the [query syntax reference](/guides/search/full-text-search/query-syntax)).
  </Step>
</Steps>

## Use your own data

Swap the sample documents for your own: keep the same `documents.upsert()` call and replace the `text` and metadata with your content. Each document needs a unique `_id` and the `text` field from your schema, plus any metadata fields you want to filter on.

```python theme={null}
index.documents.upsert(
    namespace="__default__",
    documents=[
        {"_id": "doc-1", "text": "Your first document...", "category": "your-category"},
        # ...your documents
    ],
)
```

For large sets, use [Bulk import](/guides/index-data/import-data) instead of upserting one request at a time.

## Next steps

<CardGroup>
  <Card title="Rank by meaning" icon="layer-group" href="/guides/search/full-text-search#schema-definition">
    Add a `dense_vector` field to your schema for semantic search, or combine it with text for hybrid search.
  </Card>

  <Card title="Ingest your own files" icon="database" href="/guides/get-started/quickstart/ingest-files">
    Embed your own files with Pinecone Inference and search by meaning
  </Card>

  <Card title="Bring your own vectors" icon="cube" href="/guides/get-started/quickstart/bring-your-own-vectors">
    Upsert embeddings you already have directly.
  </Card>
</CardGroup>

For the full reference (query syntax, filters, analyzers, and bulk import), see the [Full-text search guide](/guides/search/full-text-search).
