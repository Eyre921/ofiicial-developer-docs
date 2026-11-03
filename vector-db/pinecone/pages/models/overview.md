---
title: "Model gallery"
source: https://docs.pinecone.io/models/overview
path: models/overview
---

Compare the embedding and reranking models you can use with Pinecone by type, company, input, dimension, max tokens, and supported API.

# Model gallery

Embedding and reranking models you can use with your Pinecone API key, plus models you run yourself and bring as vectors.

[Request a model](https://www.pinecone.io/request-a-model/)

> [tab] Pinecone API key
>
> | Model | Company | Type | Input | Dimension | Max tokens | [Processing location](/guides/index-data/processing-locations) | Supported API | Minimum plan | Status | Actions |
> | - | - | - | - | - | - | - | - | - | - | - |
> | [gemini-embedding-2](/models/gemini-embedding-2) | Google | Dense embedding | Text | 128 to 3072 (default: 3072) | 8192 | `global` | Documents | Builder | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=gemini-embedding-2\&dimensions=3072\&metric=cosine\&with_model=gemini-embedding-2) |
> | [text-embedding-3-large](/models/text-embedding-3-large) | OpenAI | Dense embedding | Text | 1 to 3072 (default: 3072) | 8192 | `global` or `us` | Documents | Starter | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=text-embedding-3-large\&dimensions=3072\&metric=cosine\&with_model=text-embedding-3-large) |
> | [text-embedding-3-small](/models/text-embedding-3-small) | OpenAI | Dense embedding | Text | 1 to 1536 (default: 1536) | 8192 | `global` or `us` | Documents | Starter | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=text-embedding-3-small\&dimensions=1536\&metric=cosine\&with_model=text-embedding-3-small) |
> | [llama-text-embed-v2](/models/llama-text-embed-v2) | NVIDIA | Dense embedding | Text | 2048, 1024, 768, 512, 384 (default: 1024) | 2048 | `us` | Documents, Standalone embedding, Records | Starter | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=llama-text-embed-v2\&dimensions=1024\&metric=cosine\&with_model=llama-text-embed-v2) |
> | [multilingual-e5-large](/models/multilingual-e5-large) | Microsoft | Dense embedding | Text | 1024 | 507 | `us` | Documents, Standalone embedding, Records | Starter | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=multilingual-e5-large\&dimensions=1024\&metric=cosine\&with_model=multilingual-e5-large) |
> | [pinecone-sparse-english-v0](/models/pinecone-sparse-english-v0) | Pinecone | Sparse embedding | Text | Sparse | 2048 | `us` | Documents, Standalone embedding, Records | Starter | | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=pinecone-sparse-english-v0\&metric=dotproduct\&with_model=pinecone-sparse-english-v0) |
> | [cohere-rerank-4-fast](/models/cohere-rerank-4-fast) | Cohere | Reranking | Text | N/A | 4096 | `global` | Standalone reranking, Records | Standard | | |
> | [bge-reranker-v2-m3](/models/bge-reranker-v2-m3) | BAAI | Reranking | Text | N/A | 1024 | `us` | Standalone reranking, Records | Starter | | |
> | [pinecone-rerank-v0](/models/pinecone-rerank-v0) | Pinecone | Reranking | Text | N/A | 512 | `us` | Standalone reranking, Records | Starter | Deprecated | |
>
> Documents: The [Documents API](/reference/api/2026-07/data-plane/upsert_documents), for document indexes with integrated embedding.
>
> Standalone embedding: The standalone [`/embed`](/reference/api/2026-07/inference/generate-vectors) endpoint, which embeds text without an index.
>
> Standalone reranking: The standalone [`/rerank`](/reference/api/2026-07/inference/rerank-results) endpoint, which reranks results without an index.
>
> Records: The legacy [Records API](/reference/api/2026-07/data-plane/upsert_records), for legacy integrated indexes created with `create_index_for_model`.

> [tab] Bring your own vectors
>
> \| Model | Company | Type | Input | Dimension | Max tokens | Actions |
> \|---|---|---|---|---|---|---|---|
> \| [gte-base](/models/gte-base) | Alibaba | Dense embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=gte-base\&dimensions=768\&metric=cosine) |
> \| [gte-large](/models/gte-large) | Alibaba | Dense embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=gte-large\&dimensions=1024\&metric=cosine) |
> \| [embed-english-light-v3.0](/models/cohere-embed-english-light-v3.0) | Cohere | Dense embedding | Text | 384 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-english-light-v3-0\&dimensions=384\&metric=cosine) |
> \| [embed-english-v3.0](/models/cohere-embed-english-v3.0) | Cohere | Dense embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-english-v3-0\&dimensions=1024\&metric=cosine) |
> \| [embed-multilingual-v3.0](/models/cohere-embed-multilingual-v3.0) | Cohere | Dense embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=embed-multilingual-v3-0\&dimensions=1024\&metric=cosine) |
> \| [all-MiniLM-L12-v2](/models/all-MiniLM-L12-v2) | HuggingFace | Dense embedding | Text | 384 | 256 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=all-minilm-l12-v2\&dimensions=384\&metric=cosine) |
> \| [all-mpnet-base-v2](/models/all-mpnet-base-v2) | HuggingFace | Dense embedding | Text | 768 | 384 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=all-mpnet-base-v2\&dimensions=768\&metric=cosine) |
> \| [instructor-large](/models/instructor-large) | HuggingFace | Dense embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=instructor-large\&dimensions=768\&metric=cosine) |
> \| [instructor-xl](/models/instructor-xl) | HuggingFace | Dense embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=instructor-xl\&dimensions=768\&metric=cosine) |
> \| [jina-clip-v2](/models/jina-clip-v2) | Jina AI | Dense embedding | Text, image | 1024 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=jina-clip-v2\&dimensions=1024\&metric=cosine) |
> \| [jina-embeddings-v4](/models/jina-embeddings-v4) | Jina AI | Dense embedding | Text, image | 2048, 128, 256, 512, 1024 | 32768 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=jina-embeddings-v4\&dimensions=2048\&metric=cosine) |
> \| [CLIP-ViT-B-32-laion2B-s34B-b79K](/models/CLIP-ViT-B-32-laion2B-s34B-b79K) | Laion | Dense embedding | Text, image | 512 | 77 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=clip-vit-b-32-laion2b-s34b-b79k\&dimensions=512\&metric=cosine) |
> \| [e5-base-v2](/models/e5-base-v2) | Microsoft | Dense embedding | Text | 768 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=e5-base-v2\&dimensions=768\&metric=cosine) |
> \| [e5-large-v2](/models/e5-large-v2) | Microsoft | Dense embedding | Text | 1024 | 512 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=e5-large-v2\&dimensions=1024\&metric=cosine) |
> \| [mistral-embed](/models/mistral-embed) | Mistral AI | Dense embedding | Text | 1024 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=mistral-embed\&dimensions=1024\&metric=cosine) |
> \| [CLIP](/models/clip) | OpenAI | Dense embedding | Text, image | 512, 768 | 77 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=clip\&dimensions=512\&metric=cosine) |
> \| [text-embedding-ada-002](/models/text-embedding-ada-002) | OpenAI | Dense embedding | Text | 1536 | 8192 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=text-embedding-ada-002\&dimensions=1536\&metric=cosine) |
> \| [rerank-2](/models/rerank-2) | Voyage AI | Reranking | Text | N/A | 16000 |  |
> \| [rerank-2-lite](/models/rerank-2-lite) | Voyage AI | Reranking | Text | N/A | 8000 |  |
> \| [voyage-2](/models/voyage-02) | Voyage AI | Dense embedding | Text | 1024 | 4000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-2\&dimensions=1024\&metric=cosine) |
> \| [voyage-3](/models/voyage-3) | Voyage AI | Dense embedding | Text | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3\&dimensions=1024\&metric=cosine) |
> \| [voyage-3-large](/models/voyage-3-large) | Voyage AI | Dense embedding | Text | 1024, 256, 512, 2048 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3-large\&dimensions=1024\&metric=cosine) |
> \| [voyage-3-lite](/models/voyage-3-lite) | Voyage AI | Dense embedding | Text | 512 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-3-lite\&dimensions=512\&metric=cosine) |
> \| [voyage-code-2](/models/voyage-code-2) | Voyage AI | Dense embedding | Text | 1536 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-code-2\&dimensions=1536\&metric=cosine) |
> \| [voyage-code-3](/models/voyage-code-3) | Voyage AI | Dense embedding | Text | 1024, 256, 512, 2048 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-code-3\&dimensions=1024\&metric=cosine) |
> \| [voyage-finance-2](/models/voyage-finance-2) | Voyage AI | Dense embedding | Text | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-finance-2\&dimensions=1024\&metric=cosine) |
> \| [voyage-large-2](/models/voyage-large-2) | Voyage AI | Dense embedding | Text | 1536 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-large-2\&dimensions=1536\&metric=cosine) |
> \| [voyage-law-2](/models/voyage-law-2) | Voyage AI | Dense embedding | Text | 1024 | 16000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-law-2\&dimensions=1024\&metric=cosine) |
> \| [voyage-multimodal-3](/models/voyage-multimodal-3) | Voyage AI | Dense embedding | Text, image | 1024 | 32000 | [Create index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless?name=voyage-multimodal-3\&dimensions=1024\&metric=cosine) |
