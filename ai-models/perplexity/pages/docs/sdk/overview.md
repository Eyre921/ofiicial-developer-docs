---
title: "Quickstart"
source: https://docs.perplexity.ai/docs/sdk/overview
path: docs/sdk/overview
---

Learn how to use the official Perplexity SDKs for Python and TypeScript to access the Perplexity APIs with type safety and async support.

## Overview

The official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications. Both SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.

Access four APIs: **Agent API** for third-party models with web search tools and presets, **Search** for ranked web search results, **Sonar** for web-grounded AI responses, and **Embeddings** for generating text embeddings.

## Available APIs

<CardGroup>
  <Card title="Agent API" icon="code-circle" href="/docs/agent-api/quickstart">
    Third-party models from OpenAI, Anthropic, Google, and more with presets and web search tools.
  </Card>

  <Card title="Search" icon="search" href="/docs/search/quickstart">
    Ranked web search results with filtering, multi-query support, and domain controls.
  </Card>

  <Card title="Sonar" icon="message" href="/docs/sonar/quickstart">
    AI responses with web-grounded knowledge, conversation context, and streaming support.
  </Card>

  <Card title="Embeddings" icon="cube" href="/docs/embeddings/quickstart">
    Generate high-quality text embeddings for semantic search and RAG.
  </Card>
</CardGroup>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

<Card title="Get your Perplexity API Key" icon="key" href="https://console.perplexity.ai">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

After generating the key, set it as an environment variable in your terminal:

<Tabs>
  <Tab title="Windows">
    ```bash theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>

  <Tab title="MacOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>
</Tabs>

### Using Environment Variables

You can use the environment variable directly:

<CodeGroup>
  ```python Python theme={null}
  import os
  from perplexity import Perplexity

  client = Perplexity() # Automatically uses PERPLEXITY_API_KEY
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
    apiKey: process.env['PERPLEXITY_API_KEY'], // This is the default and can be omitted
  });
  ```
</CodeGroup>

Or use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:

<CodeGroup>
  ```python Python theme={null}
  import os
  from dotenv import load_dotenv
  from perplexity import Perplexity

  load_dotenv()

  client = Perplexity() # Uses PERPLEXITY_API_KEY from .env file
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import dotenv from 'dotenv';

  dotenv.config();

  const client = new Perplexity(); // Uses PERPLEXITY_API_KEY from .env file
  ```
</CodeGroup>

<Tip>
  Now you're ready to start using the Perplexity APIs! Choose your API below for step-by-step usage guides.
</Tip>

<CardGroup>
  <Card title="Agent API" icon="code-circle" href="/docs/agent-api/quickstart">
    Get started with third-party models
  </Card>

  <Card title="Search" icon="search" href="/docs/search/quickstart">
    Get started with web search
  </Card>

  <Card title="Sonar" icon="message" href="/docs/sonar/quickstart">
    Get started with AI responses
  </Card>

  <Card title="Embeddings" icon="cube" href="/docs/embeddings/quickstart">
    Get started with text embeddings
  </Card>
</CardGroup>

## Resources

<CardGroup>
  <Card title="Python Package" icon="brand-python" href="https://pypi.org/project/perplexityai/">
    Install from PyPI with pip
  </Card>

  <Card title="Node.js and TypeScript Package" icon="brand-npm" href="https://www.npmjs.com/package/@perplexity-ai/perplexity_ai">
    Install from npm registry
  </Card>
</CardGroup>
