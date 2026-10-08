---
title: "Pinecone Assistant"
source: https://docs.pinecone.io/guides/assistant/overview
path: guides/assistant/overview
---

Pinecone Assistant is a managed service for building production-grade RAG chat and agent applications grounded in your data.

Pinecone Assistant answers questions about your proprietary data. You upload files to an assistant, then chat with it or retrieve context snippets, and get back answers grounded in your data.

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/guides/assistant/quickstart/sdk-quickstart">
    Create an assistant, upload a file, and chat with it
  </Card>

  <Card title="Files" icon="file" href="/guides/assistant/files-overview">
    Supported file types, metadata, and how files are processed
  </Card>

  <Card title="Chat with an assistant" icon="comments" href="/guides/assistant/chat-with-assistant">
    Ask questions and get grounded answers with citations
  </Card>

  <Card title="Context snippets" icon="scissors" href="/guides/assistant/context-snippets-overview">
    Retrieve relevant context to use with your own LLM or agent
  </Card>

  <Card title="Pricing and limits" icon="tag" href="/guides/assistant/pricing-and-limits">
    Costs for ingestion, chat, and storage, plus plan limits
  </Card>

  <Card title="MCP server" icon="server" href="/guides/assistant/mcp-server">
    Connect AI agents to your assistant through its MCP server
  </Card>
</CardGroup>

## What you can do

With Pinecone Assistant, you can:

* Prototype and deploy an AI assistant without building your own retrieval pipeline.
* Get context-aware answers about your proprietary data without training an LLM.
* Get answers grounded in your data, with references to the files each answer draws from.

## SDK support

You can use the [Assistant API](/reference/api/assistant/introduction) directly, through the [Pinecone Python SDK](/reference/sdks/python/overview), or through the [Pinecone Node.js SDK](/reference/sdks/node/overview).

## Workflow

These steps outline the Pinecone Assistant workflow, which you can follow in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant) or with the [Pinecone API](/reference/api/assistant/introduction):

1. [Create an assistant](/guides/assistant/create-assistant) to answer questions about your documents.
2. [Upload documents](/guides/assistant/upload-files) to your assistant. Your assistant manages chunking, embedding, and storage for you.
3. [Chat with your assistant](/guides/assistant/chat-with-assistant) and receive responses as a JSON object or as a text stream. For each chat, your assistant queries a large language model (LLM) with context from your documents, so the LLM's responses are grounded in them.
4. [Evaluate the assistant's responses](/guides/assistant/evaluation-overview) for correctness and completeness.
5. [Add instructions](/guides/assistant/manage-assistants#add-instructions-to-an-assistant) to tailor your assistant's behavior and responses to specific use cases or requirements. [Filter chat by file metadata](/guides/assistant/chat-with-assistant#filter-chat-with-metadata) to reduce latency and improve the accuracy of responses.
6. [Retrieve context snippets](/guides/assistant/retrieve-context-snippets) to understand what relevant data snippets Pinecone Assistant is using to generate responses. You can use the retrieved snippets with your own LLM, RAG application, or agentic workflow.

To try these steps with the Python or Node.js SDK, see the [SDK quickstart](/guides/assistant/quickstart/sdk-quickstart). To learn how Pinecone Assistant processes files and generates answers, see [Assistant architecture](/reference/architecture/assistant-architecture).

## Resources

<CardGroup>
  <Card title="API reference" icon="code-simple" href="/reference/api/assistant/introduction">
    Details about the Assistant API and its SDK support
  </Card>

  <Card title="Examples" icon="grid-round" href="/examples/assistant">
    Sample apps and notebooks built with Pinecone Assistant
  </Card>

  <Card title="Changelog" icon="party-horn" href="/release-notes">
    What's new in Pinecone
  </Card>
</CardGroup>

## Other Pinecone products

<CardGroup>
  <Card title="Pinecone Database" icon="database" href="/guides/get-started/overview">
    The retrieval foundation, bringing full-text and semantic search with metadata filtering into one managed database
  </Card>

  <Card title="Pinecone Nexus" icon="brain-circuit" href="/guides/nexus/overview">
    The knowledge engine for agents, serving grounded, cited answers in one call
  </Card>
</CardGroup>
