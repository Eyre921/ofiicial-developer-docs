---
title: "Best Practices"
source: https://docs.perplexity.ai/docs/embeddings/best-practices
path: docs/embeddings/best-practices
---

Optimize your embeddings workflow with batch processing, caching, RAG patterns, and performance tips.

## Overview

This guide covers best practices for getting the most out of Perplexity's Embeddings API, including dimension reduction, batch processing, RAG patterns, and error handling.

## Matryoshka Dimension Reduction

Perplexity embeddings support Matryoshka representation learning, allowing you to reduce embedding dimensions while maintaining quality. This enables faster similarity search and reduced storage costs.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Full dimensions (2560 for 4b model)
  full_response = client.embeddings.create(
      input=["Your text here"],
      model="pplx-embed-v1-4b"
  )
  print(f"Full: {full_response.data[0].embedding}")  # 2560-dim base64 string

  # Reduced dimensions - faster search, smaller storage
  reduced_response = client.embeddings.create(
      input=["Your text here"],
      model="pplx-embed-v1-4b",
      dimensions=512
  )
  print(f"Reduced: {reduced_response.data[0].embedding}")  # 512-dim base64 string
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Full dimensions (2560 for 4b model)
  const fullResponse = await client.embeddings.create({
      input: ["Your text here"],
      model: "pplx-embed-v1-4b"
  });
  console.log(`Full: ${fullResponse.data![0].embedding}`);

  // Reduced dimensions - faster search, smaller storage
  const reducedResponse = await client.embeddings.create({
      input: ["Your text here"],
      model: "pplx-embed-v1-4b",
      dimensions: 512
  });
  console.log(`Reduced: ${reducedResponse.data![0].embedding}`);
  ```
</CodeGroup>

<Note>
  **Trade-off:** Lower dimensions = faster search + less storage, but slightly lower quality. Start with full dimensions and reduce if needed.
</Note>

## Encoding Formats

Control precision and size of embedding outputs:

| Format          | Description                                                 |     Decoded Size     | Similarity Metric | Use Case                                      |
| --------------- | ----------------------------------------------------------- | :------------------: | :---------------: | --------------------------------------------- |
| `base64_int8`   | Base64-encoded signed int8 (-128 to 127)                    |   dimensions bytes   | Cosine similarity | Default, good balance of quality and size     |
| `base64_binary` | Base64-encoded packed bits (1 bit per dimension, LSB first) | dimensions / 8 bytes |  Hamming distance | Maximum compression for large-scale retrieval |

<CodeGroup>
  ```python Python theme={null}
  import base64
  import numpy as np

  # Decode base64_int8 (default)
  response = client.embeddings.create(
      input=["Your text"],
      model="pplx-embed-v1-4b"
  )
  int8_embedding = np.frombuffer(
      base64.b64decode(response.data[0].embedding), dtype=np.int8
  )

  # Binary embeddings for large-scale retrieval systems
  response = client.embeddings.create(
      input=["Your text"],
      model="pplx-embed-v1-4b",
      encoding_format="base64_binary"
  )
  binary_bytes = np.frombuffer(
      base64.b64decode(response.data[0].embedding), dtype=np.uint8
  )
  # Unpack bits: each byte contains 8 dimensions (LSB first)
  binary_embedding = np.unpackbits(binary_bytes, bitorder="little")
  ```

  ```typescript TypeScript theme={null}
  // Decode base64_int8 (default)
  const response = await client.embeddings.create({
      input: ["Your text"],
      model: "pplx-embed-v1-4b"
  });
  const buffer = Buffer.from(response.data![0].embedding, 'base64');
  const int8Embedding = new Int8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);

  // Binary embeddings for large-scale retrieval systems
  const binaryResponse = await client.embeddings.create({
      input: ["Your text"],
      model: "pplx-embed-v1-4b",
      encoding_format: "base64_binary"
  });
  const binaryBuffer = Buffer.from(binaryResponse.data![0].embedding, 'base64');
  // Each byte contains 8 dimensions as packed bits (LSB first)
  ```
</CodeGroup>

<Tip>
  `base64_int8` produces the same quality as bfloat16 with significantly reduced storage. Use `base64_binary` for extreme compression in large-scale systems.
</Tip>

## Similarity Metrics

Perplexity embedding models produce **unnormalized** embeddings. Choosing the correct similarity metric is critical for accurate retrieval.

<Warning>
  `pplx-embed-v1` and `pplx-embed-context-v1` natively produce unnormalized int8-quantized embeddings. You **must** compare them via cosine similarity. Using inner product or L2 distance directly will produce incorrect results because most embedding models are pre-normalized, but Perplexity embeddings are not.
</Warning>

### int8 Embeddings (`base64_int8`)

Compare using **cosine similarity**. If your vector database does not support cosine similarity natively, convert the embeddings to float32 and L2-normalize them before storing:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import numpy as np

  def decode_and_normalize(b64_string):
      """Decode and L2-normalize for vector DBs that only support inner product."""
      embedding = np.frombuffer(base64.b64decode(b64_string), dtype=np.int8).astype(np.float32)
      norm = np.linalg.norm(embedding)
      if norm > 0:
          embedding = embedding / norm
      return embedding

  # After normalization, cosine similarity == inner product
  ```

  ```typescript TypeScript theme={null}
  function decodeAndNormalize(b64String: string): Float32Array {
      const buffer = Buffer.from(b64String, 'base64');
      const int8 = new Int8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
      const float32 = new Float32Array(int8.length);

      // Convert to float32
      let norm = 0;
      for (let i = 0; i < int8.length; i++) {
          float32[i] = int8[i];
          norm += float32[i] * float32[i];
      }

      // L2-normalize so inner product == cosine similarity
      norm = Math.sqrt(norm);
      if (norm > 0) {
          for (let i = 0; i < float32.length; i++) {
              float32[i] /= norm;
          }
      }
      return float32;
  }
  ```
</CodeGroup>

### Binary Embeddings (`base64_binary`)

Compare using **Hamming distance**. Binary embeddings encode each dimension as a single bit, so the natural distance metric is the number of differing bits between two vectors.

```python theme={null}
import numpy as np

def hamming_distance(a: np.ndarray, b: np.ndarray) -> int:
    """Hamming distance between two binary vectors (as uint8 packed bits)."""
    return np.unpackbits(np.bitwise_xor(a, b)).sum()
```

<Note>
  Most vector databases (Pinecone, Weaviate, Qdrant, Milvus) support cosine similarity as a distance metric. Verify your database's configuration before indexing embeddings.
</Note>

## RAG Pattern

Combine embeddings with Perplexity's Agentic Research API for retrieval-augmented generation:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import numpy as np
  from perplexity import Perplexity

  client = Perplexity()

  def decode_embedding(b64_string):
      return np.frombuffer(base64.b64decode(b64_string), dtype=np.int8).astype(np.float32)

  def cosine_similarity(a, b):
      return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

  # 1. Your knowledge base (embed once, store in vector DB)
  knowledge_base = [
      "Perplexity API provides web-grounded AI responses",
      "The Embeddings API supports Matryoshka dimension reduction",
      "Contextualized embeddings share context across document chunks"
  ]

  kb_response = client.embeddings.create(input=knowledge_base, model="pplx-embed-v1-4b")
  kb_embeddings = [decode_embedding(emb.embedding) for emb in kb_response.data]

  # 2. User query
  user_query = "How do I reduce embedding dimensions?"

  # 3. Find relevant context
  query_response = client.embeddings.create(input=[user_query], model="pplx-embed-v1-4b")
  query_embedding = decode_embedding(query_response.data[0].embedding)

  scores = [(i, cosine_similarity(query_embedding, emb)) for i, emb in enumerate(kb_embeddings)]
  top_docs = sorted(scores, key=lambda x: x[1], reverse=True)[:2]
  context = "\n".join([knowledge_base[i] for i, _ in top_docs])

  # 4. Generate answer with context
  response = client.responses.create(
      model="openai/gpt-5.5",
      input=f"Answer using this context:\n\n{context}\n\nQuestion: {user_query}"
  )

  print(response.output[0].content[0].text)
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

  // 1. Your knowledge base
  const knowledgeBase = [
      "Perplexity API provides web-grounded AI responses",
      "The Embeddings API supports Matryoshka dimension reduction",
      "Contextualized embeddings share context across document chunks"
  ];

  const kbResponse = await client.embeddings.create({
      input: knowledgeBase,
      model: "pplx-embed-v1-4b"
  });
  const kbEmbeddings = kbResponse.data!.map(emb => decodeEmbedding(emb.embedding!));

  // 2. User query
  const userQuery = "How do I reduce embedding dimensions?";

  // 3. Find relevant context
  const queryResponse = await client.embeddings.create({
      input: [userQuery],
      model: "pplx-embed-v1-4b"
  });
  const queryEmbedding = decodeEmbedding(queryResponse.data![0].embedding!);

  const scores = kbEmbeddings.map((emb, i) => ({
      index: i,
      score: cosineSimilarity(queryEmbedding, emb)
  }));
  const topDocs = scores.sort((a, b) => b.score - a.score).slice(0, 2);
  const context = topDocs.map(d => knowledgeBase[d.index]).join("\n");

  // 4. Generate answer with context
  const response = await client.responses.create({
      model: "openai/gpt-5.5",
      input: `Answer using this context:\n\n${context}\n\nQuestion: ${userQuery}`
  });

  console.log((response.output[0] as any).content[0].text);
  ```
</CodeGroup>

## Batch Processing

Process large datasets efficiently with async batching:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity

  async def batch_embed(texts: list[str], batch_size: int = 100):
      async with AsyncPerplexity() as client:
          results = []
          for i in range(0, len(texts), batch_size):
              batch = texts[i:i + batch_size]
              response = await client.embeddings.create(
                  input=batch,
                  model="pplx-embed-v1-4b"
              )
              results.extend(response.data)
              print(f"Processed {min(i + batch_size, len(texts))}/{len(texts)}")
          return results

  # Usage
  texts = ["Document " + str(i) for i in range(1000)]
  embeddings = asyncio.run(batch_embed(texts))
  print(f"Generated {len(embeddings)} embeddings")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function batchEmbed(texts: string[], batchSize: number = 100) {
      const client = new Perplexity();
      const results: any[] = [];

      for (let i = 0; i < texts.length; i += batchSize) {
          const batch = texts.slice(i, i + batchSize);
          const response = await client.embeddings.create({
              input: batch,
              model: "pplx-embed-v1-4b"
          });
          results.push(...(response.data ?? []));
          console.log(`Processed ${Math.min(i + batchSize, texts.length)}/${texts.length}`);
      }

      return results;
  }

  // Usage
  const texts = Array.from({ length: 1000 }, (_, i) => `Document ${i}`);
  const embeddings = await batchEmbed(texts);
  console.log(`Generated ${embeddings.length} embeddings`);
  ```
</CodeGroup>

## Error Handling

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      response = client.embeddings.create(
          input=["Your text"],
          model="pplx-embed-v1-4b"
      )
  except perplexity.BadRequestError as e:
      print(f"Invalid request: {e}")
  except perplexity.RateLimitError:
      print("Rate limited, please retry later")
  except perplexity.APIStatusError as e:
      print(f"API error: {e.status_code}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const response = await client.embeddings.create({
          input: ["Your text"],
          model: "pplx-embed-v1-4b"
      });
  } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
          console.error("Invalid request:", error.message);
      } else if (error instanceof Perplexity.RateLimitError) {
          console.error("Rate limited, please retry later");
      } else if (error instanceof Perplexity.APIError) {
          console.error(`API error: ${error.status}`);
      }
  }
  ```
</CodeGroup>

## Tips

<Steps>
  <Step title="Batch requests">
    Send up to 512 texts per request to maximize throughput and reduce API calls.
  </Step>

  <Step title="Match models">
    Always use the same embedding model for both queries and documents to ensure consistent similarity scores.
  </Step>

  <Step title="Use cosine similarity">
    Perplexity embeddings are unnormalized. Always use cosine similarity for `base64_int8` and Hamming distance for `base64_binary`. If your vector DB only supports inner product, L2-normalize the embeddings before storing.
  </Step>

  <Step title="Cache embeddings">
    Store computed embeddings in a vector database. Never recompute embeddings for the same text.
  </Step>

  <Step title="Use Matryoshka wisely">
    Start with full dimensions for best quality. Reduce dimensions only if you need faster search or smaller storage.
  </Step>

  <Step title="Binary for scale">
    Use `base64_binary` encoding format for large-scale retrieval systems where storage and speed are critical.
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/embeddings/quickstart">
    Get started with basic embeddings functionality.
  </Card>

  <Card title="Contextualized Embeddings" icon="file-lines" href="/docs/embeddings/contextualized-embeddings">
    Document-aware embeddings for chunks with shared context.
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/embeddings-post">
    Complete Embeddings API documentation.
  </Card>

  <Card title="SDK Guide" icon="code" href="/docs/sdk/overview">
    Perplexity SDK features and best practices.
  </Card>
</CardGroup>
