---
title: "Pinecone model gallery"
source: https://docs.pinecone.io/models/overview
path: models/overview
---

Compare the embedding and reranking models you can use with Pinecone by type, company, modality, dimension, max tokens, and supported API.

Models

Compare the embedding and reranking models you can use with Pinecone.

[Request a model](https://www.pinecone.io/request-a-model/)

> [tab] Pinecone API key
>
> Embed and rerank with these models using only your Pinecone API key. Let Pinecone embed your text and rerank results as part of upserts and searches, or call a model directly to get vectors or scores. The Supported API column shows which options each model supports.
>
> | Model | Company | Type | Modality | Dimension | Max tokens | Processing location | Supported API | Actions |
> | - | - | - | - | - | - | - | - | - |
> | [llama-text-embed-v2](/models/llama-text-embed-v2) | NVIDIA | Embedding | Text | 1024, 2048, 768, 512, 384 | 2048 | `us` | Documents, Standalone embedding, Records | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=llama-text-embed-v2\&dimensions=1024\&metric=cosine\&with_model=llama-text-embed-v2) |
> | [multilingual-e5-large](/models/multilingual-e5-large) | Microsoft | Embedding | Text | 1024 | 507 | `us` | Documents, Standalone embedding, Records | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=multilingual-e5-large\&dimensions=1024\&metric=cosine\&with_model=multilingual-e5-large) |
> | [pinecone-sparse-english-v0](/models/pinecone-sparse-english-v0) | Pinecone | Embedding | Text | Sparse | 2048 | `us` | Documents, Standalone embedding, Records | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=pinecone-sparse-english-v0\&metric=dotproduct\&with_model=pinecone-sparse-english-v0) |
> | [cohere-rerank-4-fast](/models/cohere-rerank-4-fast) | Cohere | Reranking | Text | N/A | 4096 | `global` | Standalone reranking, Records | |
> | [bge-reranker-v2-m3](/models/bge-reranker-v2-m3) | BAAI | Reranking | Text | N/A | 1024 | `us` | Standalone reranking, Records | |
>
> In the Supported API column:
>
> * Documents: The [Documents API](/reference/api/2026-07/data-plane/upsert_documents), for document indexes with integrated embedding.
> * Standalone embedding: The standalone [`/embed`](/reference/api/2026-07/inference/generate-vectors) endpoint, which embeds text without an index.
> * Standalone reranking: The standalone [`/rerank`](/reference/api/2026-07/inference/rerank-results) endpoint, which reranks results without an index.
> * Records: The legacy [Records API](/reference/api/2026-07/data-plane/upsert_records), for legacy integrated indexes created with `create_index_for_model`.

> [tab] Bring your own vectors
>
> These models don't work with a Pinecone API key. Generate vectors with the company's API, or run an open-source model yourself, and upsert them to an index. To rerank, call the company's API with the results you query from Pinecone.
>
> | Model | Company | Type | Modality | Dimension | Max tokens | Actions |
> | - | - | - | - | - | - | - |
> | [gte-base](/models/gte-base) | Alibaba | Embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=gte-base\&dimensions=768\&metric=cosine) |
> | [gte-large](/models/gte-large) | Alibaba | Embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=gte-large\&dimensions=1024\&metric=cosine) |
> | [embed-english-light-v3.0](/models/cohere-embed-english-light-v3.0) | Cohere | Embedding | Text | 384 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-english-light-v3-0\&dimensions=384\&metric=cosine) |
> | [embed-english-v3.0](/models/cohere-embed-english-v3.0) | Cohere | Embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-english-v3-0\&dimensions=1024\&metric=cosine) |
> | [embed-multilingual-v3.0](/models/cohere-embed-multilingual-v3.0) | Cohere | Embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-multilingual-v3-0\&dimensions=1024\&metric=cosine) |
> | [all-MiniLM-L12-v2](/models/all-MiniLM-L12-v2) | HuggingFace | Embedding | Text | 384 | 256 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=all-minilm-l12-v2\&dimensions=384\&metric=cosine) |
> | [all-mpnet-base-v2](/models/all-mpnet-base-v2) | HuggingFace | Embedding | Text | 768 | 384 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=all-mpnet-base-v2\&dimensions=768\&metric=cosine) |
> | [instructor-large](/models/instructor-large) | HuggingFace | Embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=instructor-large\&dimensions=768\&metric=cosine) |
> | [instructor-xl](/models/instructor-xl) | HuggingFace | Embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=instructor-xl\&dimensions=768\&metric=cosine) |
> | [jina-clip-v2](/models/jina-clip-v2) | Jina AI | Embedding | Multimodal | 1024 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=jina-clip-v2\&dimensions=1024\&metric=cosine) |
> | [jina-embeddings-v4](/models/jina-embeddings-v4) | Jina AI | Embedding | Multimodal | 2048, 128, 256, 512, 1024 | 32768 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=jina-embeddings-v4\&dimensions=2048\&metric=cosine) |
> | [CLIP-ViT-B-32-laion2B-s34B-b79K](/models/CLIP-ViT-B-32-laion2B-s34B-b79K) | Laion | Embedding | Multimodal | 512 | 77 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=clip-vit-b-32-laion2b-s34b-b79k\&dimensions=512\&metric=cosine) |
> | [e5-base-v2](/models/e5-base-v2) | Microsoft | Embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=e5-base-v2\&dimensions=768\&metric=cosine) |
> | [e5-large-v2](/models/e5-large-v2) | Microsoft | Embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=e5-large-v2\&dimensions=1024\&metric=cosine) |
> | [mistral-embed](/models/mistral-embed) | Mistral AI | Embedding | Text | 1024 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=mistral-embed\&dimensions=1024\&metric=cosine) |
> | [CLIP](/models/clip) | OpenAI | Embedding | Multimodal | 512, 768 | 77 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=clip\&dimensions=512\&metric=cosine) |
> | [text-embedding-ada-002](/models/text-embedding-ada-002) | OpenAI | Embedding | Text | 1536 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=text-embedding-ada-002\&dimensions=1536\&metric=cosine) |
> | [rerank-2](/models/rerank-2) | Voyage AI | Reranking | Text | N/A | 16000 | |
> | [rerank-2-lite](/models/rerank-2-lite) | Voyage AI | Reranking | Text | N/A | 8000 | |
> | [voyage-2](/models/voyage-02) | Voyage AI | Embedding | Text | 1024 | 4000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-2\&dimensions=1024\&metric=cosine) |
> | [voyage-3](/models/voyage-3) | Voyage AI | Embedding | Text | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3\&dimensions=1024\&metric=cosine) |
> | [voyage-3-large](/models/voyage-3-large) | Voyage AI | Embedding | Text | 1024, 256, 512, 2048 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3-large\&dimensions=1024\&metric=cosine) |
> | [voyage-3-lite](/models/voyage-3-lite) | Voyage AI | Embedding | Text | 512 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3-lite\&dimensions=512\&metric=cosine) |
> | [voyage-code-2](/models/voyage-code-2) | Voyage AI | Embedding | Text | 1536 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-code-2\&dimensions=1536\&metric=cosine) |
> | [voyage-code-3](/models/voyage-code-3) | Voyage AI | Embedding | Text | 1024, 256, 512, 2048 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-code-3\&dimensions=1024\&metric=cosine) |
> | [voyage-finance-2](/models/voyage-finance-2) | Voyage AI | Embedding | Text | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-finance-2\&dimensions=1024\&metric=cosine) |
> | [voyage-large-2](/models/voyage-large-2) | Voyage AI | Embedding | Text | 1536 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-large-2\&dimensions=1536\&metric=cosine) |
> | [voyage-law-2](/models/voyage-law-2) | Voyage AI | Embedding | Text | 1024 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-law-2\&dimensions=1024\&metric=cosine) |
> | [voyage-multimodal-3](/models/voyage-multimodal-3) | Voyage AI | Embedding | Multimodal | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-multimodal-3\&dimensions=1024\&metric=cosine) |
