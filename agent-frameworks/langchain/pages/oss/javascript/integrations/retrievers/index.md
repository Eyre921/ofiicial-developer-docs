---
title: "Retriever integrations"
source: https://docs.langchain.com/oss/javascript/integrations/retrievers/index
path: oss/javascript/integrations/retrievers/index
---

Integrate with retrievers using LangChain JavaScript.

A [retriever](/oss/javascript/deepagents/retrieval) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.

Retrievers accept a string query as input and return a list of `Document` objects.

For specifics on how to use retrievers, see the [relevant how-to guides here](/oss/javascript/deepagents/retrieval).

Note that all [vector stores](/oss/javascript/integrations/vectorstores) can be [cast to retrievers](/oss/javascript/deepagents/retrieval).
Refer to the vector store [integration docs](/oss/javascript/integrations/vectorstores/) for available vector store retrievers.

## All retrievers

<Columns>
  <Card title="Alchemyst AI Retriever" icon="link" href="/oss/javascript/integrations/retrievers/alchemystai-retriever" />

  <Card title="Knowledge Bases for Amazon Bedrock" icon="link" href="/oss/javascript/integrations/retrievers/bedrock-knowledge-bases" />

  <Card title="Exa" icon="link" href="/oss/javascript/integrations/retrievers/exa" />

  <Card title="HyDE Retriever" icon="link" href="/oss/javascript/integrations/retrievers/hyde" />

  <Card title="Amazon Kendra Retriever" icon="link" href="/oss/javascript/integrations/retrievers/kendra-retriever" />

  <Card title="SourceyRetriever" icon="link" href="/oss/javascript/integrations/retrievers/sourcey" />

  <Card title="Time-Weighted Retriever" icon="link" href="/oss/javascript/integrations/retrievers/time-weighted-retriever" />
</Columns>

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
