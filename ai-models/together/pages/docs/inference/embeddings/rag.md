---
title: "Retrieval-augmented generation"
source: https://docs.together.ai/docs/inference/embeddings/rag
path: docs/inference/embeddings/rag
---

Build a retrieval-augmented generation pipeline with Together embeddings, rerank, and chat completions.

Retrieval-augmented generation (RAG) grounds a language model's answer in your own documents. At a high level, you embed a corpus of text into vectors, store those vectors, retrieve the closest matches to a user's query, and pass the retrieved text into a chat completion as context. The model answers from your data instead of guessing.

Together AI exposes the three primitives a RAG pipeline needs (embeddings, rerank, and chat completions) behind a single API and SDK. The walkthrough below builds an end-to-end example you can run as-is, then points to deeper material on each piece, common vector store integrations, and existing RAG cookbooks in the [Guides](/docs/guides) tab.

## End-to-end example

The script below builds a tiny RAG pipeline with no external dependencies beyond the Together SDK. It embeds a small corpus, stores the vectors in memory, retrieves the top matches by cosine similarity, and passes them into a chat completion as context.

```python Python theme={null}
import math
from together import Together

client = Together()

EMBEDDING_MODEL = "intfloat/multilingual-e5-large-instruct"
CHAT_MODEL = "MiniMaxAI/MiniMax-M3"

# A tiny corpus. In a real app, load from your data source and chunk first.
corpus = [
    "Photosynthesis converts sunlight, water, and carbon dioxide into glucose and oxygen, primarily in the chloroplasts of plant leaves.",
    "Mitochondria generate ATP through cellular respiration and are often called the powerhouse of the cell.",
    "Plate tectonics explains the slow movement of Earth's lithospheric plates and accounts for earthquakes and volcanoes.",
    "The water cycle moves water between oceans, atmosphere, and land through evaporation, condensation, and precipitation.",
    "Natural selection favors organisms whose inherited traits improve their chance of surviving and reproducing.",
    "Neural networks are layered computations of weighted sums and nonlinear activations, loosely inspired by biological neurons.",
]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na and nb else 0.0


# 1. Embed the corpus once.
doc_embeddings = client.embeddings.create(
    model=EMBEDDING_MODEL, input=corpus
).data
index = list(zip(corpus, [d.embedding for d in doc_embeddings]))


def rag(query: str, top_k: int = 3) -> str:
    # 2. Embed the query.
    q_emb = (
        client.embeddings.create(model=EMBEDDING_MODEL, input=query)
        .data[0]
        .embedding
    )

    # 3. Retrieve top_k by cosine similarity.
    ranked = sorted(index, key=lambda d: cosine(q_emb, d[1]), reverse=True)
    context = "\n\n".join(text for text, _ in ranked[:top_k])

    # 4. Generate an answer grounded in the retrieved context.
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the question using only the context below. "
                    "If the context is insufficient, say so.\n\n"
                    f"Context:\n{context}"
                ),
            },
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content


print(rag("How do plants make their food?"))
```

This is the smallest pipeline that's still recognizably RAG. Real systems chunk longer documents to fit the embedding model's context limit (514 tokens for `intfloat/multilingual-e5-large-instruct`), persist vectors in a database, and add a reranking stage to improve precision before generation.

### Add a rerank stage

A reranker is a second-stage model that re-scores the top results from your vector search using the query and document together. Rerank improves precision when the top of your similarity ranking is noisy or when you only have room for a few documents in the prompt. See the [Rerank guide](/docs/inference/embeddings/rerank) for details.

<Note>
  Rerank models like `mixedbread-ai/mxbai-rerank-large-v2` are only available on [dedicated endpoints](https://api.together.ai/endpoints/configure). Spin one up before running the snippet below, then point `RERANK_MODEL` at it.
</Note>

To slot reranking in, retrieve more candidates from the vector store than you plan to use, rerank them, and pass the top reranked documents into the chat completion.

```python Python theme={null}
RERANK_MODEL = (
    "mixedbread-ai/mxbai-rerank-large-v2"  # requires dedicated endpoint
)


def rag_with_rerank(query: str, retrieve_k: int = 20, top_n: int = 3) -> str:
    q_emb = (
        client.embeddings.create(model=EMBEDDING_MODEL, input=query)
        .data[0]
        .embedding
    )

    # 1. Over-retrieve from the vector store.
    candidates = sorted(
        index, key=lambda d: cosine(q_emb, d[1]), reverse=True
    )[:retrieve_k]
    candidate_texts = [text for text, _ in candidates]

    # 2. Rerank the candidates with a Together reranker.
    reranked = client.rerank.create(
        model=RERANK_MODEL,
        query=query,
        documents=candidate_texts,
        top_n=top_n,
    )
    context = "\n\n".join(candidate_texts[r.index] for r in reranked.results)

    # 3. Generate the final answer.
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": f"Answer using only the context below.\n\nContext:\n{context}",
            },
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content
```

The same pattern (over-retrieve, rerank, generate) is what production RAG systems use, regardless of which vector store sits underneath.

## Vector store integrations

The in-memory store above is fine for a few hundred documents. For larger corpora, persist your vectors in a dedicated vector database. Together embeddings work with any store that accepts raw float vectors.

### Pinecone

Pinecone is a managed vector database with a serverless tier. Embed with Together, then upsert and query through the Pinecone client.

```python Python theme={null}
from pinecone import Pinecone, ServerlessSpec
from together import Together

pc = Pinecone(api_key="<PINECONE_API_KEY>", source_tag="TOGETHER_AI")
client = Together()

pc.create_index(
    name="together-rag",
    dimension=1024,  # match your embedding model's output dimension
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-west-2"),
)
index = pc.Index("together-rag")

texts = ["Our solar system orbits the Milky Way at about 515,000 mph."]
embeddings = client.embeddings.create(
    model="intfloat/multilingual-e5-large-instruct", input=texts
).data

index.upsert(
    vectors=[
        {
            "id": f"doc_{i}",
            "values": e.embedding,
            "metadata": {"text": texts[i]},
        }
        for i, e in enumerate(embeddings)
    ]
)
```

For Pinecone-specific guidance on indexing, namespaces, and metadata filtering, see the [Pinecone documentation](https://docs.pinecone.io/).

### MongoDB Atlas Vector Search

MongoDB Atlas adds vector search on top of a regular Mongo collection. Store the embedding alongside the document and define a vector index on the embedding field.

```python Python theme={null}
from pymongo import MongoClient
from together import Together

mongo = MongoClient("<MONGODB_ATLAS_URI>")
collection = mongo["rag_db"]["documents"]
client = Together()

text = "Our solar system orbits the Milky Way at about 515,000 mph."
embedding = (
    client.embeddings.create(
        model="intfloat/multilingual-e5-large-instruct", input=text
    )
    .data[0]
    .embedding
)

collection.insert_one({"text": text, "embedding": embedding})
```

Once your Atlas vector index is configured, query with `$vectorSearch` in an aggregation pipeline. The full walkthrough is in the [MongoDB + Together AI tutorial](https://www.together.ai/blog/rag-tutorial-mongodb).

### Pixeltable

Pixeltable is a declarative table for unstructured data. It can call Together embeddings as a column expression, so chunking, embedding, and indexing all live in your table definition.

```python Python theme={null}
import pixeltable as pxt
from pixeltable.functions.together import embeddings

docs = pxt.create_table("rag.documents", {"text": pxt.String})
docs.add_computed_column(
    embedding=embeddings(
        input=docs.text, model="intfloat/multilingual-e5-large-instruct"
    )
)
docs.add_embedding_index(
    "text",
    string_embed=embeddings.using(
        model="intfloat/multilingual-e5-large-instruct"
    ),
)
```

For more, see the [Pixeltable + Together docs](https://docs.pixeltable.com/sdk/latest/together).

### Other frameworks

Together is also a first-class provider in the major LLM application frameworks:

* LangChain: [`langchain-together`](https://python.langchain.com/docs/integrations/providers/together/) ships `TogetherEmbeddings` and a `ChatTogether` model. See the [LangChain + Together RAG tutorial](https://www.together.ai/blog/rag-tutorial-langchain).
* LlamaIndex: [`TogetherEmbedding`](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/together/) and [`TogetherLLM`](https://docs.llamaindex.ai/en/stable/examples/llm/together/) plug straight into a `VectorStoreIndex`. See the [LlamaIndex + Together RAG tutorial](https://www.together.ai/blog/rag-tutorial-llamaindex).

## Beyond the basics

Once your pipeline is working, the next questions are usually about chunking strategy, retrieval quality, and evaluation. Start here:

* [Embeddings](/docs/inference/embeddings/embeddings). Available models, batch shapes, and the `client.embeddings.create` reference.
* [Rerank](/docs/inference/embeddings/rerank). When to add a reranker, supported models, and JSON-rank-fields mode.
* [Quickstart: RAG](/docs/quickstart-retrieval-augmented-generation-rag). End-to-end Paul Graham essay example with chunking, embedding, retrieval, rerank, and generation.
* [Building a RAG workflow](/docs/building-a-rag-workflow). Longer guide that walks through document loading, chunking, and prompt construction.
* [How to implement contextual RAG from Anthropic](/docs/how-to-implement-contextual-rag-from-anthropic). Apply Anthropic's contextual retrieval technique using Together embeddings and rerank.
* [How to improve search with rerankers](/docs/how-to-improve-search-with-rerankers). Side-by-side comparison of vector search alone versus vector search plus rerank.

For working notebooks, browse the [together-cookbook](https://github.com/togethercomputer/together-cookbook) repo on GitHub.
