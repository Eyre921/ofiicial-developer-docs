---
title: "Twelve Labs"
source: https://docs.pinecone.io/integrations/twelve-labs
path: integrations/twelve-labs
---

Store Twelve Labs multimodal video embeddings in Pinecone to power video search, recommendations, and content moderation with fast similarity retrieval.

[Twelve Labs](https://twelvelabs.io) is an AI company that provides video understanding capabilities through its APIs. Its Embed API lets developers create multimodal embeddings that capture the context and interactions between different modalities in videos, such as visual expressions, body language, spoken words, and overall context.

By integrating Twelve Labs' Embed API with Pinecone Database, developers can store, index, and retrieve these multimodal embeddings at scale. This integration lets developers build AI applications that use video data, such as video search, recommendation systems, and content moderation. Developers generate embeddings using Twelve Labs' API and store them in Pinecone for fast, accurate similarity search and retrieval.

Together, Twelve Labs and Pinecone let developers process and understand video content in a more human-like manner. By combining Twelve Labs' video-native approach with Pinecone's purpose-built vector search, developers can build applications across industries, including media and entertainment, e-commerce, and education.

<PrimarySecondaryCTA />

## Setup guide

1. Sign up for a [Twelve Labs account](https://twelvelabs.io) and get your API key.
2. Install the [Twelve Labs Python client library](https://github.com/twelvelabs-io/twelvelabs-python).
3. Sign up for a [Pinecone account](https://app.pinecone.io/) and [create an index](/guides/index-data/create-an-index).
4. Install the [Pinecone client library](/reference/pinecone-sdks).
5. Use the [Twelve Labs Embed API](https://docs.twelvelabs.io/docs/create-embeddings) to generate multimodal embeddings for your videos.
6. Connect to your Pinecone index and [upsert the embeddings](/guides/index-data/upsert-data).
7. [Query the Pinecone index](/guides/search/search-overview) to retrieve similar videos based on embeddings.

For more information and code examples, see the [Twelve Labs documentation](https://docs.twelvelabs.io).
