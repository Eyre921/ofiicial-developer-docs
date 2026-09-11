---
title: "Ingest your own files"
source: https://docs.pinecone.io/guides/get-started/quickstart/ingest-files
path: guides/get-started/quickstart/ingest-files
---

Turn a folder of documents into a searchable index: extract text, chunk it, embed the chunks, and upsert.

Make a folder of raw documents searchable. The flow is: extract text, chunk it, embed the chunks, upsert, then search. Your coding agent can run this end to end (see the [Quickstart hub](/guides/get-started/quickstart)), or follow the steps.

<Note>
  This path uses [Pinecone Inference](/guides/core-concepts/key-terms#pinecone-inference), Pinecone's hosted embedding service, to turn your text into vectors. If you already generate your own embeddings, skip this and go to [Bring your own vectors](/guides/get-started/quickstart/bring-your-own-vectors) instead.
</Note>

## Prerequisites

* A Pinecone account and API key ([get one](https://app.pinecone.io)).
* **Python 3.10+**.
* The Pinecone Python SDK: `pip install --upgrade pinecone`.

## Ingest your own files and search

<Steps>
  <Step title="Set your API key">
    Set your API key as an environment variable so the SDK can authenticate:

    ```bash theme={null}
    export PINECONE_API_KEY="YOUR_API_KEY"
    ```
  </Step>

  <Step title="Extract text from your files">
    Convert each file (PDF, DOCX, HTML, and so on) to plain text using a parser of your choice. This step happens outside Pinecone. The result should be a list of records, each with an `id` and `text`, like the `docs` list below. It runs as-is, so you can complete the quickstart first and swap in your own extracted text after.

    <Note>
      If you're embedding images instead of text, skip this step and the chunking step. Embed your images directly with a multimodal embedding model, then upsert the resulting vectors following [Bring your own vectors](/guides/get-started/quickstart/bring-your-own-vectors).
    </Note>

    ```python theme={null}
    docs = [
        {"id": "handbook-1", "text": "Refund requests must be submitted within 30 days of purchase."},
        {"id": "handbook-2", "text": "Enterprise customers get support with a 4-hour response time."},
        # ...extracted from your files
    ]
    ```
  </Step>

  <Step title="Chunk the text">
    Split your text into smaller pieces so each fits your embedding model's input limit. The function below is a simple length-based split you can run as-is. For smarter approaches (by sentence, token, or document structure), see [chunking strategies](https://www.pinecone.io/learn/chunking-strategies/).

    ```python theme={null}
    def chunk(text, size=500):
        return [text[i:i + size] for i in range(0, len(text), size)]

    chunks = [
        {"id": f"{d['id']}#{i}", "text": part}
        for d in docs
        for i, part in enumerate(chunk(d["text"]))
    ]
    ```
  </Step>

  <Step title="Create an index with a dense-vector field">
    Set `dimension` to match your embedding model. `llama-text-embed-v2` outputs 1024 dimensions. Only the vector field goes in the schema; other fields are stored on the documents (non-schema fields are stored as metadata, capped at 40 KB per document).

    ```python theme={null}
    import os, time
    from pinecone import Pinecone, SchemaBuilder

    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    schema = (
        SchemaBuilder()
          .add_dense_vector_field(name="embedding", dimension=1024, metric="cosine")
          .build()
    )
    if not pc.indexes.exists(name="my-files"):
        pc.indexes.create(name="my-files", schema=schema)

    while not pc.indexes.describe(name="my-files").status.ready:
        time.sleep(2)

    index = pc.Index(name="my-files")
    ```
  </Step>

  <Step title="Embed the chunks and upsert">
    Use [Pinecone Inference](/guides/core-concepts/key-terms#pinecone-inference) to embed the chunks (in batches of 96, this model's per-call limit), then `upsert` the vectors alongside the text. For a large dataset, use `batch_upsert` or [Import](/guides/index-data/import-data) instead.

    ```python theme={null}
    # llama-text-embed-v2 accepts up to 96 inputs per call, so embed in batches.
    embeddings = []
    for i in range(0, len(chunks), 96):
        resp = pc.inference.embed(
            model="llama-text-embed-v2",
            inputs=[c["text"] for c in chunks[i:i + 96]],
            parameters={"input_type": "passage"},
        )
        embeddings.extend(resp)

    index.documents.upsert(
        namespace="__default__",
        documents=[
            {"_id": c["id"], "embedding": e['values'], "text": c["text"]}
            for c, e in zip(chunks, embeddings)
        ],
    )

    time.sleep(5)  # documents are indexed asynchronously, so wait a moment
    ```
  </Step>

  <Step title="Search your documents">
    To search, embed the query with the same model you used for the documents, then rank documents by vector similarity.

    ```python theme={null}
    q = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=["what is the refund policy?"],
        parameters={"input_type": "query"},
    )

    resp = index.documents.search(
        namespace="__default__",
        top_k=3,
        score_by=[{"type": "dense_vector", "fields": ["embedding"], "values": q[0]['values']}],
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

  <Card title="Bulk import" icon="database" href="/guides/index-data/import-data">
    Load large document sets efficiently
  </Card>
</CardGroup>
