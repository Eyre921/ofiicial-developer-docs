---
title: "Contextualized Embeddings"
source: https://docs.perplexity.ai/docs/embeddings/contextualized-embeddings
path: docs/embeddings/contextualized-embeddings
---

Generate document-aware embeddings for chunks that share context, improving retrieval quality for document-based applications.

## Overview

Contextualized embeddings generate embeddings for document chunks that share context awareness. Unlike standard embeddings where each text is embedded independently, contextualized embeddings understand that chunks belong to the same document and incorporate that relationship.

<Info>
  Use contextualized embeddings when embedding chunks from the same document (e.g., paragraphs, sections). Use [standard embeddings](/docs/embeddings/quickstart) for independent texts like search queries or standalone sentences.
</Info>

## Models

|             Model            | Dimensions | Context | MRL | Quantization | Price (\$/1M tokens) |
| :--------------------------: | :--------: | :-----: | :-: | :----------: | :------------------: |
| `pplx-embed-context-v1-0.6b` |    1024    |   32K   | Yes |  INT8/BINARY |        \$0.008       |
|  `pplx-embed-context-v1-4b`  |    2560    |   32K   | Yes |  INT8/BINARY |        \$0.05        |

All models use mean pooling and require no instruction prefix.

## Basic Usage

Pass documents as nested arrays where each inner array represents chunks from a single document:

<Warning>
  **Chunk ordering:** Chunks within each document must be sent in the order they appear in the source document. The model uses sequential context to generate document-aware embeddings, so maintaining the original order is essential for optimal results.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.contextualized_embeddings.create(
      input=[
          # Document 1: Three chunks
          [
              "Curiosity begins in childhood with endless questions about the world.",
              "As we grow, curiosity drives us to explore new ideas and challenge assumptions.",
              "Scientific breakthroughs often start with a simple curious question."
          ],
          # Document 2: Two chunks
          [
              "The Curiosity rover explores Mars, searching for signs of ancient life.",
              "Each discovery on Mars sparks new questions about our place in the universe."
          ]
      ],
      model="pplx-embed-context-v1-4b"
  )

  for doc in response.data:
      for chunk in doc.data:
          print(f"Doc {doc.index}, Chunk {chunk.index}: {chunk.embedding}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.contextualizedEmbeddings.create({
      input: [
          // Document 1: Three chunks
          [
              "Curiosity begins in childhood with endless questions about the world.",
              "As we grow, curiosity drives us to explore new ideas and challenge assumptions.",
              "Scientific breakthroughs often start with a simple curious question."
          ],
          // Document 2: Two chunks
          [
              "The Curiosity rover explores Mars, searching for signs of ancient life.",
              "Each discovery on Mars sparks new questions about our place in the universe."
          ]
      ],
      model: "pplx-embed-context-v1-4b"
  });

  for (const doc of response.data!) {
      for (const chunk of doc.data!) {
          console.log(`Doc ${doc.index}, Chunk ${chunk.index}: ${chunk.embedding!}`);
      }
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/v1/contextualizedembeddings' \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "input": [
        [
          "Curiosity begins in childhood with endless questions about the world.",
          "As we grow, curiosity drives us to explore new ideas and challenge assumptions.",
          "Scientific breakthroughs often start with a simple curious question."
        ],
        [
          "The Curiosity rover explores Mars, searching for signs of ancient life.",
          "Each discovery on Mars sparks new questions about our place in the universe."
        ]
      ],
      "model": "pplx-embed-context-v1-4b"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "object": "list",
    "data": [
      {
        "object": "list",
        "index": 0,
        "data": [
          { "object": "embedding", "index": 0, "embedding": "/* base64-encoded signed int8 values */" },
          { "object": "embedding", "index": 1, "embedding": "/* base64-encoded signed int8 values */" },
          { "object": "embedding", "index": 2, "embedding": "/* base64-encoded signed int8 values */" }
        ]
      },
      {
        "object": "list",
        "index": 1,
        "data": [
          { "object": "embedding", "index": 0, "embedding": "/* base64-encoded signed int8 values */" },
          { "object": "embedding", "index": 1, "embedding": "/* base64-encoded signed int8 values */" }
        ]
      }
    ],
    "model": "pplx-embed-context-v1-4b",
    "usage": {
      "prompt_tokens": 72,
      "total_tokens": 72
    }
  }
  ```
</Accordion>

## Parameters

| Parameter         | Type                   | Required |    Default    | Description                                                                                               |
| ----------------- | ---------------------- | :------: | :-----------: | --------------------------------------------------------------------------------------------------------- |
| `input`           | array\[array\[string]] |    Yes   |       -       | Nested array: each inner array contains chunks from one document. Max 512 documents, 16,000 total chunks. |
| `model`           | string                 |    Yes   |       -       | Model identifier: `pplx-embed-context-v1-0.6b` or `pplx-embed-context-v1-4b`                              |
| `dimensions`      | integer                |    No    |      Full     | Matryoshka dimension (128-1024 for 0.6b, 128-2560 for 4b)                                                 |
| `encoding_format` | string                 |    No    | `base64_int8` | Output encoding: `base64_int8` (signed int8) or `base64_binary` (packed bits)                             |

<Warning>
  **Input limits:** Total tokens per document must not exceed 32K. Total chunks across all documents must not exceed 16,000. All chunks in a single request must not exceed 120,000 tokens combined. Empty strings are not allowed.
</Warning>

## Golden Chunk Retrieval Example

Build a chunk retrieval system where chunks from the same document share context:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import numpy as np
  from perplexity import Perplexity

  client = Perplexity()

  def decode_embedding(b64_string):
      """Decode a base64-encoded int8 embedding."""
      return np.frombuffer(base64.b64decode(b64_string), dtype=np.int8).astype(np.float32)

  def cosine_similarity(a, b):
      return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

  # Your documents, each split into chunks
  documents = [
      {
          "title": "Machine Learning Guide",
          "chunks": [
              "Machine learning is a subset of AI that enables systems to learn.",
              "Supervised learning uses labeled data for training models.",
              "Unsupervised learning finds patterns in unlabeled data."
          ]
      },
      {
          "title": "Deep Learning Fundamentals",
          "chunks": [
              "Deep learning uses neural networks with multiple layers.",
              "Convolutional networks excel at image processing tasks.",
              "Transformers revolutionized natural language processing."
          ]
      }
  ]

  # 1. Embed all document chunks with context awareness
  doc_chunks = [doc["chunks"] for doc in documents]
  doc_response = client.contextualized_embeddings.create(
      input=doc_chunks,
      model="pplx-embed-context-v1-4b"
  )

  # Build index
  chunk_index = []
  for doc_obj in doc_response.data:
      for chunk_obj in doc_obj.data:
          chunk_index.append({
              "doc_idx": doc_obj.index,
              "chunk_idx": chunk_obj.index,
              "embedding": decode_embedding(chunk_obj.embedding),
              "text": documents[doc_obj.index]["chunks"][chunk_obj.index],
              "doc_title": documents[doc_obj.index]["title"]
          })

  # 2. Embed the query using the same contextualized model
  # Wrap each query as a single-element inner list: [[query1], [query2]]
  query = "How do neural networks process images?"
  query_response = client.contextualized_embeddings.create(
      input=[[query]],
      model="pplx-embed-context-v1-4b"
  )
  query_embedding = decode_embedding(query_response.data[0].data[0].embedding)

  # 3. Find most relevant chunks
  results = []
  for item in chunk_index:
      score = cosine_similarity(query_embedding, item["embedding"])
      results.append({**item, "score": score})

  results = sorted(results, key=lambda x: x["score"], reverse=True)

  print(f"Query: {query}\n")
  print("Top results:")
  for r in results[:3]:
      print(f"  [{r['doc_title']}] {r['score']:.4f}: {r['text'][:60]}...")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  function decodeEmbedding(b64String: string): Int8Array {
      const buffer = Buffer.from(b64String, 'base64');
      return new Int8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
  }

  function cosineSimilarity(a: Int8Array, b: Int8Array): number {
      let dotProduct = 0, normA = 0, normB = 0;
      for (let i = 0; i < a.length; i++) {
          dotProduct += a[i] * b[i];
          normA += a[i] * a[i];
          normB += b[i] * b[i];
      }
      return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
  }

  // Your documents, each split into chunks
  const documents = [
      {
          title: "Machine Learning Guide",
          chunks: [
              "Machine learning is a subset of AI that enables systems to learn.",
              "Supervised learning uses labeled data for training models.",
              "Unsupervised learning finds patterns in unlabeled data."
          ]
      },
      {
          title: "Deep Learning Fundamentals",
          chunks: [
              "Deep learning uses neural networks with multiple layers.",
              "Convolutional networks excel at image processing tasks.",
              "Transformers revolutionized natural language processing."
          ]
      }
  ];

  // 1. Embed all document chunks with context awareness
  const docChunks = documents.map(doc => doc.chunks);
  const docResponse = await client.contextualizedEmbeddings.create({
      input: docChunks,
      model: "pplx-embed-context-v1-4b"
  });

  // Build index
  const chunkIndex = docResponse.data!.flatMap(docObj =>
      docObj.data!.map(chunkObj => ({
          docIdx: docObj.index,
          chunkIdx: chunkObj.index,
          embedding: decodeEmbedding(chunkObj.embedding!),
          text: documents[docObj.index as number].chunks[chunkObj.index as number],
          docTitle: documents[docObj.index as number].title
      }))
  );

  // 2. Embed the query using the same contextualized model
  // Wrap each query as a single-element inner list: [[query1], [query2]]
  const query = "How do neural networks process images?";
  const queryResponse = await client.contextualizedEmbeddings.create({
      input: [[query]],
      model: "pplx-embed-context-v1-4b"
  });
  const queryEmbedding = decodeEmbedding(queryResponse.data![0].data![0].embedding!);

  // 3. Find most relevant chunks
  const results = chunkIndex
      .map(item => ({
          ...item,
          score: cosineSimilarity(queryEmbedding, item.embedding)
      }))
      .sort((a, b) => b.score - a.score);

  console.log(`Query: ${query}\n`);
  console.log("Top results:");
  for (const r of results.slice(0, 3)) {
      console.log(`  [${r.docTitle}] ${r.score.toFixed(4)}: ${r.text.slice(0, 60)}...`);
  }
  ```
</CodeGroup>

## When to Use Contextualized vs Standard

| Use Case                  | Recommendation            |
| ------------------------- | ------------------------- |
| Independent sentences     | Standard embeddings       |
| FAQ entries               | Standard embeddings       |
| General-purpose retrieval | Standard embeddings       |
| Document paragraphs       | Contextualized embeddings |
| PDF sections              | Contextualized embeddings |
| Article chunks            | Contextualized embeddings |
| Code file segments        | Contextualized embeddings |

<Tip>
  **Rule of thumb:** If chunks come from the same source document and their meaning depends on surrounding context, use contextualized embeddings. If each text stands alone, use standard embeddings. When using contextualized embeddings, embed queries with the same contextualized model by wrapping each query as a single-element inner list (e.g., `[[query]]`).
</Tip>

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/embeddings/quickstart">
    Get started with standard embeddings.
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/embeddings/best-practices">
    Batch processing, caching, and RAG patterns.
  </Card>
</CardGroup>
