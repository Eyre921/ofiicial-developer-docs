---
title: "Pinecone documentation"
source: https://docs.pinecone.io/guides/get-started/overview
path: guides/get-started/overview
---

Pinecone is the leading vector database for building accurate and performant AI applications at scale in production.

<CardGroup>
  <Card title="Database quickstart" icon="database" href="/guides/get-started/quickstart">
    Set up a fully managed vector database for high-performance semantic search
  </Card>

  <Card title="Assistant quickstart" icon="comments" href="/guides/assistant/quickstart/sdk-quickstart">
    Create an AI assistant that answers complex questions about your proprietary data
  </Card>

  <Card title="Marketplace quickstart" icon="store" href="/guides/marketplace/quickstart">
    Publish a no-code knowledge application from a vertical template (public preview)
  </Card>
</CardGroup>

## Workflows

<Tabs>
  <Tab title="Integrated embedding">
    Use integrated embedding to upsert and search with text and have Pinecone generate vectors automatically.

    <Steps>
      <Step title="Create an index">
        [Create an index](/guides/index-data/create-an-index) that matches your retrieval needs: an [index with a document schema](/guides/get-started/concepts#document) for [full-text search](/guides/search/full-text-search) on FTS-enabled `string` fields (BM25 ranking, with `dense_vector` and `sparse_vector` fields available in the same schema); an [index with dense vectors](/guides/index-data/create-an-index#create-a-dense-index) integrated with a [hosted embedding model](/guides/index-data/create-an-index#embedding-models) for [semantic search](/guides/search/semantic-search); or an [index with sparse vectors](/guides/index-data/create-an-index#create-an-index-for-sparse-vectors) for [sparse-vector lexical search](/guides/search/lexical-search) with a custom encoder.
      </Step>

      <Step title="Prepare data">
        [Prepare](/guides/index-data/data-modeling) your data for efficient ingestion, retrieval, and management in Pinecone.
      </Step>

      <Step title="Upsert text">
        [Upsert](/guides/index-data/upsert-data) your source text and have Pinecone convert the text to vectors automatically. For full-text search, [upsert typed documents](/guides/index-data/upsert-data#upsert-documents) and Pinecone indexes each field according to the schema. [Use namespaces to partition data](/guides/index-data/indexing-overview#namespaces) for faster queries and multitenant isolation between customers.
      </Step>

      <Step title="Search with text">
        [Search](/guides/search/search-overview) the index with a query text. Again, Pinecone uses the index's integrated model to convert the text to a vector automatically.
      </Step>

      <Step title="Improve relevance">
        [Filter by metadata](/guides/search/filter-by-metadata) to limit the scope of your search, [rerank results](/guides/search/rerank-results) to increase search accuracy, or use [full-text search](/guides/search/full-text-search) for precise keyword and phrase matching alongside semantic ranking on the same index.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Bring your own vectors">
    If you use an external embedding model to generate vectors, you can upsert and search with vectors directly.

    <Steps>
      <Step title="Generate vectors">
        Use an external embedding model to convert data into dense or sparse vectors.
      </Step>

      <Step title="Create an index">
        [Create an index](/guides/index-data/create-an-index) that matches the characteristics of your embedding model. Dense vectors enable [semantic search](/guides/search/semantic-search); sparse vectors enable [sparse-vector lexical search](/guides/search/lexical-search) with a custom encoder; or an [index with a document schema](/guides/get-started/concepts#document) lets you store dense and sparse vectors alongside BM25-indexed `string` fields (declared with `full_text_search`) under one schema, with auto-indexed filterable metadata on every document.
      </Step>

      <Step title="Prepare data">
        [Prepare](/guides/index-data/data-modeling) your data for efficient ingestion, retrieval, and management in Pinecone.
      </Step>

      <Step title="Ingest vectors">
        [Load your vectors](/guides/index-data/data-ingestion-overview) and metadata into your index using Pinecone's import or upsert feature. [Use namespaces to partition data](/guides/index-data/indexing-overview#namespaces) for faster queries and multitenant isolation between customers.
      </Step>

      <Step title="Search with a vector">
        Use an external embedding model to convert a query text to a vector and [search](/guides/search/search-overview) the index with the vector.
      </Step>

      <Step title="Improve relevance">
        [Filter by metadata](/guides/search/filter-by-metadata) to limit the scope of your search, [rerank results](/guides/search/rerank-results) to increase search accuracy, or add an [index with a document schema](/guides/get-started/concepts#document) for [full-text search](/guides/search/full-text-search) (or [sparse-vector lexical search](/guides/search/lexical-search) with a custom encoder) to capture precise keyword matches.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Start building

<CardGroup>
  <Card title="IDEs & CLIs" icon="wand-magic-sparkles" href="/guides/get-started/ai-coding-tools">
    Use Pinecone with agentic IDEs and CLIs like Claude Code, Gemini CLI, and Cursor.
  </Card>

  <Card title="CLI" icon="terminal" href="/reference/cli/quickstart">
    Command-line tool for managing Pinecone infrastructure and data.
  </Card>

  <Card title="API Reference" icon="code-simple" href="/reference">
    Comprehensive details about the Pinecone APIs, SDKs, utilities, and architecture.
  </Card>

  <Card title="Integrated Inference" icon="cubes" href="/guides/index-data/indexing-overview#integrated-embedding">
    Simplify vector search with integrated embedding and reranking.
  </Card>

  <Card title="Examples" icon="grid-round" href="/examples">
    Hands-on notebooks and sample apps with common AI patterns and tools.
  </Card>

  <Card title="Integrations" icon="link-simple" href="/integrations/overview">
    Pinecone's growing number of third-party integrations.
  </Card>

  <Card title="Troubleshooting" icon="bug" href="/troubleshooting/contact-support">
    Resolve common Pinecone issues with our troubleshooting guide.
  </Card>

  <Card title="Releases" icon="party-horn" href="/release-notes">
    News about features and changes in Pinecone and related tools.
  </Card>
</CardGroup>
