---
title: "API reference"
source: https://docs.pinecone.io/reference/api/introduction
path: reference/api/introduction
---

Pinecone REST API: Pinecone's APIs let you interact programmatically with your Pinecone account.

Pinecone's APIs let you interact programmatically with your Pinecone account.

<Note>
  [SDK versions](/reference/pinecone-sdks#sdk-versions) are pinned to specific API versions.
</Note>

## Database

Use the Database API to store and query records in [Pinecone Database](/guides/get-started/quickstart).

The following Pinecone SDKs support the Database API:

<CardGroup>
  <Card title="CLI" icon="terminal" href="/reference/cli/overview" />

  <Card title="Python SDK" icon="python" href="/reference/sdks/python/overview" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/sdks/node/overview" />

  <Card title="Java SDK" icon="java" href="/reference/sdks/java/overview" />

  <Card title="Go SDK" icon="golang" href="/reference/sdks/go/overview" />
</CardGroup>

## Inference

Use the Inference API to generate vector embeddings and rerank results using [embedding models](/guides/index-data/create-an-index#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone's infrastructure.

There are two ways to use the Inference API:

* As a standalone service, through the [Rerank documents](/reference/api/latest/inference/rerank) and [Generate vectors](/reference/api/latest/inference/generate-embeddings) endpoints.
* As an integrated part of database operations, through the [Create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model), [Upsert text](/reference/api/latest/data-plane/upsert_records), and [Search with text](/reference/api/latest/data-plane/search_records) endpoints.

The following Pinecone SDKs support using the Inference API:

<CardGroup>
  <Card title="Python SDK" icon="python" href="/reference/sdks/python/overview" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/sdks/node/overview" />

  <Card title="Java SDK" icon="java" href="/reference/sdks/java/overview" />

  <Card title="Go SDK" icon="golang" href="/reference/sdks/go/overview" />
</CardGroup>
