---
title: "Bring your own vectors"
source: https://docs.pinecone.io/guides/get-started/quickstart/bring-your-own-vectors
path: guides/get-started/quickstart/bring-your-own-vectors
---

Create an index with a dense-vector field, upsert embeddings you already have, and run semantic search.

If you already generate embeddings, store them directly. Create an index with a dense-vector field, upsert your vectors, and rank by similarity. Pinecone does no embedding on your behalf here.

## Prerequisites

* A Pinecone account and API key ([get one](https://app.pinecone.io)).
* **Python 3.10+**.
* The Pinecone Python SDK: `pip install --upgrade pinecone`.

## Upsert your vectors and search

<Steps>
  <Step title="Set your API key">
    Set your API key as an environment variable so the SDK can authenticate:

    ```bash theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```
  </Step>

  <Step title="Create an index with a dense-vector field">
    Set `dimension` to match your embedding model's output, and pick a distance `metric` (`cosine`, `dotproduct`, or `euclidean`). Only the vector field goes in the schema; other fields like `text` are stored on the documents (non-schema fields are stored as metadata, capped at 40 KB per document).

    ```python theme={null}
    import os, time
    from pinecone import Pinecone, SchemaBuilder

    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    schema = (
        SchemaBuilder()
          .add_dense_vector_field(name="embedding", dimension=1024, metric="cosine")
          .build()
    )
    if not pc.indexes.exists(name="byo-vectors"):
        pc.indexes.create(name="byo-vectors", schema=schema)

    while not pc.indexes.describe(name="byo-vectors").status.ready:
        time.sleep(2)

    index = pc.Index(name="byo-vectors")
    ```
  </Step>

  <Step title="Upsert your vectors">
    Each document carries its `embedding` (a list of floats matching the schema's `dimension`) plus any fields you want to store. Replace the truncated vectors below with your real embeddings.

    ```python theme={null}
    index.documents.upsert(
        namespace="__default__",
        documents=[
            # each `embedding` is a full list of 1024 floats (shown truncated)
            {"_id": "1", "embedding": [0.12, 0.04, ...], "text": "Refund requests must be submitted within 30 days."},
            {"_id": "2", "embedding": [0.08, 0.21, ...], "text": "Enterprise support responds within 4 hours."},
        ],
    )

    time.sleep(5)  # documents are indexed asynchronously, so wait a moment
    ```
  </Step>

  <Step title="Search by vector similarity">
    Embed your query with the **same model** you used for the documents, then rank by the dense-vector field (`embedding`).

    ```python theme={null}
    query_embedding = [0.10, 0.05, ...]  # embed your query text with the same model

    resp = index.documents.search(
        namespace="__default__",
        top_k=3,
        score_by=[{"type": "dense_vector", "fields": ["embedding"], "values": query_embedding}],
        include_fields=["*"],
    )

    for m in resp.matches:
        print(m._id, m._score, getattr(m, "text", ""))
    ```
  </Step>
</Steps>

## Next steps

<CardGroup>
  <Card title="Match keywords" icon="layer-group" href="/guides/search/full-text-search#schema-definition">
    Add a `full_text_search` field to your schema for keyword search, or combine it with your vectors for hybrid search.
  </Card>

  <Card title="Data modeling" icon="table" href="/guides/index-data/data-modeling">
    How to design a schema for your workload
  </Card>
</CardGroup>
