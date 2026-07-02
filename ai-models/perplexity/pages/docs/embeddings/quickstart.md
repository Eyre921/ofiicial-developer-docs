---
title: "Embeddings API"
source: https://docs.perplexity.ai/docs/embeddings/quickstart
path: docs/embeddings/quickstart
---

Generate high-quality text embeddings for semantic search, RAG, and machine learning applications.

## Overview

Perplexity's Embeddings API generates high-quality text embeddings for semantic search and retrieval. Choose between **standard embeddings** for independent texts or **contextualized embeddings** for document chunks that share context.

<Info>
  We recommend using our [official SDKs](/docs/sdk/overview) for a more convenient and type-safe way to interact with the Embeddings API.
</Info>

<Card title="Pricing" icon="receipt" href="/docs/getting-started/pricing">
  Pay-as-you-go pricing for all APIs. No subscription required.
</Card>

## Available Models

|             Model            | Dimensions | Context | MRL | Quantization | Price (\$/1M tokens) |
| :--------------------------: | :--------: | :-----: | :-: | :----------: | :------------------: |
|     `pplx-embed-v1-0.6b`     |    1024    |   32K   | Yes |  INT8/BINARY |        \$0.004       |
|      `pplx-embed-v1-4b`      |    2560    |   32K   | Yes |  INT8/BINARY |        \$0.03        |
| `pplx-embed-context-v1-0.6b` |    1024    |   32K   | Yes |  INT8/BINARY |        \$0.008       |
|  `pplx-embed-context-v1-4b`  |    2560    |   32K   | Yes |  INT8/BINARY |        \$0.05        |

All models use mean pooling and require no instruction prefix—you can embed text directly without prompt engineering.

<Warning>
  Perplexity embeddings are **unnormalized**. Always compare `base64_int8` embeddings via **cosine similarity** (not inner product or L2 distance). Compare `base64_binary` embeddings via **Hamming distance**. See [Best Practices](/docs/embeddings/best-practices) for details and normalization helpers.
</Warning>

<Tip>
  **When to use which:**

  * **Standard embeddings** (`pplx-embed-v1-*`) - Independent texts, search queries, single sentences
  * **Contextualized embeddings** (`pplx-embed-context-v1-*`) - Document chunks that benefit from shared context (e.g., paragraphs from the same article)
</Tip>

## Installation

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

## Next Steps

<CardGroup>
  <Card title="Standard Embeddings" icon="cube" href="/docs/embeddings/standard-embeddings">
    Embed independent texts, queries, and sentences.
  </Card>

  <Card title="Contextualized Embeddings" icon="file-lines" href="/docs/embeddings/contextualized-embeddings">
    Document-aware embeddings for chunks that share context.
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/embeddings/best-practices">
    Batch processing, caching, RAG patterns, and performance optimization.
  </Card>

  <Card title="Model Cards" icon="link" href="https://huggingface.co/perplexity-ai">
    See the model cards on HuggingFace.
  </Card>
</CardGroup>
