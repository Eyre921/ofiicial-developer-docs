---
title: "Twelve Labs"
source: https://docs.pinecone.io/integrations/twelve-labs
path: integrations/twelve-labs
---

Connect Pinecone and Twelve Labs to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

[Twelve Labs](https://twelvelabs.io) is an AI company that provides state-of-the-art video understanding capabilities through its easy-to-use APIs. Our newly released product is the Embed API, which enables developers to create high-quality multimodal embeddings that capture the rich context and interactions between different modalities in videos, such as visual expressions, body language, spoken words, and overall context.

By integrating Twelve Labs' Embed API with Pinecone's vector database, developers can efficiently store, index, and retrieve these multimodal embeddings at scale. This integration empowers developers to build cutting-edge AI applications that leverage video data, such as video search, recommendation systems, content moderation, and more. Developers can seamlessly generate embeddings using Twelve Labs' API and store them in Pinecone for fast and accurate similarity search and retrieval.

The integration of Twelve Labs and Pinecone offers developers a powerful toolkit to process and understand video content in a more human-like manner. By combining Twelve Labs' video-native approach with Pinecone's purpose-built vector search capabilities, developers can unlock new possibilities and build innovative applications across various industries, including media and entertainment, e-commerce, education, and beyond.

<PrimarySecondaryCTA />

## Setup guide

To integrate Twelve Labs' Embed API with Pinecone:

1. Sign up for a [Twelve Labs](https://twelvelabs.io) and obtain your API key.
2. Install the [Twelve Labs Python client library](https://github.com/twelvelabs-io/twelvelabs-python).
3. Sign up for a [Pinecone account](https://app.pinecone.io/) and [create an index](/guides/index-data/create-an-index).
4. Install the [Pinecone client library](/reference/pinecone-sdks).
5. Use the [Twelve Labs Embed API](https://docs.twelvelabs.io/docs/create-embeddings) to generate multimodal embeddings for your videos.
6. Connect to your Pinecone index and [upsert the embeddings](/guides/index-data/upsert-data).
7. [Query the Pinecone index](/guides/search/search-overview) to retrieve similar videos based on embeddings.

For more detailed information and code examples, please see the [Twelve Labs documentation](https://docs.twelvelabs.io).
