---
title: "API reference"
source: https://docs.pinecone.io/reference/api/introduction
path: reference/api/introduction
---

Pinecone API reference overview for Database, Inference, and Admin endpoints with supported SDKs including Python, Node.js, Java, and Go.

Pinecone's APIs let you interact programmatically with your Pinecone account.

> [!NOTE]
>
> [SDK versions](/reference/pinecone-sdks#sdk-versions) are pinned to specific API versions.

## Database

Use the Database API to store and query records in [Pinecone Database](/guides/get-started/quickstart).

The following Pinecone SDKs support the Database API:

> [card] [CLI](/reference/cli/overview)

> [card] [Python SDK](/reference/sdks/python/overview)

> [card] [Node.js SDK](/reference/sdks/node/overview)

> [card] [Java SDK](/reference/sdks/java/overview)

> [card] [Go SDK](/reference/sdks/go/overview)

## Inference

Use the Inference API to generate vector embeddings and rerank results using [embedding models](/guides/index-data/index-configuration#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone's infrastructure.

There are two ways to use the Inference API:

* As a standalone service, through the [Rerank documents](/reference/api/latest/inference/rerank-results) and [Generate vectors](/reference/api/latest/inference/generate-vectors) endpoints.
* As an integrated part of database operations, through the [Create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model), [Upsert text](/reference/api/latest/data-plane/upsert_records), and [Search with text](/reference/api/latest/data-plane/search_records) endpoints.

The following Pinecone SDKs support using the Inference API:

> [card] [Python SDK](/reference/sdks/python/overview)

> [card] [Node.js SDK](/reference/sdks/node/overview)

> [card] [Java SDK](/reference/sdks/java/overview)

> [card] [Go SDK](/reference/sdks/go/overview)
