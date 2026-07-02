---
title: "Pinecone Assistant architecture"
source: https://docs.pinecone.io/reference/architecture/assistant-architecture
path: reference/architecture/assistant-architecture
---

Pinecone Assistant architecture: This page describes the architecture for Pinecone Assistant.

This page describes the architecture for [Pinecone Assistant](/guides/assistant/overview).

## Overview

[Pinecone Assistant](/guides/assistant/overview) runs as a managed service on the Pinecone platform. It uses a combination of machine learning models and information retrieval techniques to provide responses that are informed by your documents. The assistant is designed to be easy to use, requiring minimal setup and no machine learning expertise.

Pinecone Assistant simplifies complex tasks like data chunking, vector search, embedding, and querying while ensuring privacy and security.

<img />

<img />

## Data ingestion

When a [document is uploaded](/guides/assistant/manage-files), the assistant processes the content by chunking it into smaller parts and generating [vector embeddings](https://www.pinecone.io/learn/vector-embeddings-for-developers/) for each chunk. These embeddings are stored in an [index](/guides/index-data/indexing-overview), making them ready for retrieval.

## Data retrieval

During a [chat](/guides/assistant/chat-with-assistant), the assistant processes the message to formulate relevant search queries, which are used to query the index and identify the most relevant chunks from the uploaded content.

## Response generation

After retrieving these chunks, the assistant performs a ranking step to determine which information is most relevant. This [context](/guides/assistant/context-snippets-overview), along with the chat history and [assistant instructions](/guides/assistant/manage-assistants#add-instructions-to-an-assistant), is then used by a large language model (LLM) to generate responses that are informed by your documents.
