---
title: "Perplexity with Cursor"
source: https://docs.perplexity.ai/docs/getting-started/integrations/cursor
path: docs/getting-started/integrations/cursor
---

Use Perplexity inside Cursor — call the API from project code with the official TypeScript SDK, use the OpenAI-compatible base URL, or wire up the hosted Perplexity Docs MCP for in-editor documentation lookup.

## Overview

[Cursor](https://cursor.com) is an AI-first code editor that can call any HTTP API from your project code and supports the Model Context Protocol (MCP) for in-editor tools. This guide covers three integration paths for Perplexity:

<CardGroup>
  <Card title="Official TypeScript SDK" icon="code">
    Call the Perplexity API directly from your project code while you build in Cursor. **Recommended.**
  </Card>

  <Card title="OpenAI-Compatible SDK" icon="plug">
    Reuse an existing OpenAI client by pointing `baseURL` at `https://api.perplexity.ai/v1`.
  </Card>

  <Card title="Cursor MCP" icon="book">
    Configure the hosted Perplexity Docs MCP in `.cursor/mcp.json` so Cursor can look up Perplexity docs while you code.
  </Card>
</CardGroup>

<Info>
  **Recommended path:** Use the official SDK (or the OpenAI-compatible SDK) from your application code, and add the Perplexity Docs MCP to Cursor for in-editor documentation lookup. Cursor's "custom OpenAI-compatible model" override pointed at Perplexity is **experimental** and tends to be less reliable than code-level integration or MCP — see [Custom Model Override (Experimental)](#custom-model-override-experimental).
</Info>

## Prerequisites

* Cursor installed ([cursor.com/download](https://cursor.com/download))
* Node.js 18+ for the TypeScript examples
* A Perplexity API key

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate a key from the Perplexity API Portal.
</Card>

## API Key Handling

Never hardcode your API key in source files or commit it to a repository. Store it in an environment variable and read it at runtime:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>

  <Tab title=".env (project-local)">
    Create a `.env` file in your project root and add it to `.gitignore`:

    ```bash theme={null}
    # .env
    PERPLEXITY_API_KEY=your_api_key_here
    ```

    Load it at startup (for example with [`dotenv`](https://www.npmjs.com/package/dotenv)):

    ```typescript theme={null}
    import "dotenv/config";
    ```
  </Tab>
</Tabs>

<Warning>
  Treat `PERPLEXITY_API_KEY` like a password. Don't paste it into chat, prompts, or shared files. If a key is exposed, [rotate it](https://console.perplexity.ai) immediately.
</Warning>

***

## Path 1: Official TypeScript SDK (Recommended)

Build your application in Cursor and call the Perplexity API from your code using the official SDK. This is the most reliable path and gives you full type safety, preset support, and access to every API feature.

### Install

```bash theme={null}
npm install @perplexity-ai/perplexity_ai
```

<Tip>
  `pnpm` and `yarn` work the same way: `pnpm add @perplexity-ai/perplexity_ai` / `yarn add @perplexity-ai/perplexity_ai`.
</Tip>

### Agent API with `pro-search`

The Agent API is the recommended surface for most applications. Use the `pro-search` preset for web-grounded responses with sensible defaults:

```typescript theme={null}
import Perplexity from "@perplexity-ai/perplexity_ai";

const client = new Perplexity(); // reads PERPLEXITY_API_KEY from the environment

const response = await client.responses.create({
  preset: "pro-search",
  input: "Summarize the latest changes to the Perplexity Agent API.",
});

console.log(`Model used: ${response.model}`);
console.log(response.output_text);
```

<Accordion title="Python equivalent">
  ```python theme={null}
  from perplexity import Perplexity

  client = Perplexity()  # reads PERPLEXITY_API_KEY from the environment

  response = client.responses.create(
      preset="pro-search",
      input="Summarize the latest changes to the Perplexity Agent API.",
  )

  print(f"Model used: {response.model}")
  print(response.output_text)
  ```
</Accordion>

### Add Web Search

Enable the `web_search` tool for explicit control over when search is used:

```typescript theme={null}
import Perplexity from "@perplexity-ai/perplexity_ai";

const client = new Perplexity();

const response = await client.responses.create({
  model: "openai/gpt-5.4",
  input: "What are the latest developments in AI inference hardware?",
  tools: [{ type: "web_search" }],
  instructions:
    "You have access to a web_search tool. Use it for questions about current events, news, or recent developments.",
});

if (response.status === "completed") {
  console.log(response.output_text);
}
```

<Tip>
  Cursor's AI chat can scaffold and edit these snippets for you. Open the chat with `Cmd+L` / `Ctrl+L`, paste in your goal, and ask Cursor to "use `@perplexity-ai/perplexity_ai` with the `pro-search` preset."
</Tip>

For more presets, tools, and configuration options see the [Agent API quickstart](/docs/agent-api/quickstart) and the [SDK overview](/docs/sdk/overview).

***

## Path 2: OpenAI-Compatible SDK

If you already have an OpenAI client in your project, you can reuse it by pointing the `baseURL` at `https://api.perplexity.ai/v1`. Perplexity accepts `POST /v1/responses` as an alias for the Agent API.

### Install

```bash theme={null}
npm install openai
```

### Use It

```typescript theme={null}
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.PERPLEXITY_API_KEY,
  baseURL: "https://api.perplexity.ai/v1",
});

const response = await client.responses.create({
  model: "openai/gpt-5.4",
  input: "Explain the key differences between REST and GraphQL APIs.",
});

console.log(response.output_text);
```

<Accordion title="Python equivalent">
  ```python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("PERPLEXITY_API_KEY"),
      base_url="https://api.perplexity.ai/v1",
  )

  response = client.responses.create(
      model="openai/gpt-5.4",
      input="Explain the key differences between REST and GraphQL APIs.",
  )

  print(response.output_text)
  ```
</Accordion>

<Info>
  Use `baseURL` (TypeScript) or `base_url` (Python) — both must include the `/v1` suffix. See the [OpenAI Compatibility guide](/docs/agent-api/openai-compatibility) for the full list of supported parameters and which Perplexity features are available through this path.
</Info>

***

## Path 3: Cursor MCP for Docs Lookup

Cursor supports the Model Context Protocol (MCP). The hosted **Perplexity Docs MCP** at `https://docs.perplexity.ai/mcp` lets Cursor search and read Perplexity's documentation directly from chat — useful for grounding code suggestions in canonical docs without context-switching to a browser.

### Project-Scoped Configuration

Add a `.cursor/mcp.json` file at the root of your project. This makes the server available only for that project:

```json theme={null}
{
  "mcpServers": {
    "perplexity-docs": {
      "url": "https://docs.perplexity.ai/mcp"
    }
  }
}
```

### Global Configuration

To make the server available across all projects, add the same entry to `~/.cursor/mcp.json`:

```json theme={null}
{
  "mcpServers": {
    "perplexity-docs": {
      "url": "https://docs.perplexity.ai/mcp"
    }
  }
}
```

<Steps>
  <Step title="Add the Configuration">
    Save the JSON above to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global).
  </Step>

  <Step title="Reload Cursor">
    Open **Cursor → Settings → MCP** and confirm `perplexity-docs` appears with a green/ready status. Restart Cursor if needed.
  </Step>

  <Step title="Use It from Chat">
    In Cursor chat, ask questions like *"Using the Perplexity docs MCP, show me how to enable `pro-search` in the Agent API."* Cursor will call the MCP server and ground its answer in current documentation.
  </Step>
</Steps>

<Tip>
  The Docs MCP is read-only and does not require an API key — it only serves Perplexity documentation. To give Cursor access to Perplexity **search and reasoning** tools (not just docs), install the [Perplexity MCP Server](/docs/getting-started/integrations/mcp-server), which uses `@perplexity-ai/mcp-server` and requires `PERPLEXITY_API_KEY`.
</Tip>

***

## Custom Model Override (Experimental)

Cursor lets you point its built-in model picker at an OpenAI-compatible base URL. While it is possible to set this to `https://api.perplexity.ai/v1` and use a Perplexity model name, this path has limitations:

* The Agent API surface (presets, structured tool calls, finance/people search) is not fully exercised by Cursor's internal prompting.
* Cursor's autocomplete and edit features are tuned to specific model behaviors and may not work well with substituted models.
* Streaming, tool use, and error handling can behave differently than in a code-level integration.

For these reasons, **we recommend calling Perplexity from your project code** (Path 1 or Path 2) and using the **Perplexity Docs MCP** (Path 3) for in-editor docs lookup. Reach for the custom model override only when you specifically want Cursor's chat UI to talk to a Perplexity model and are comfortable with the trade-offs.

***

## Next Steps

<CardGroup>
  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Presets, tools, and the full Agent API surface used by the examples above.
  </Card>

  <Card title="Perplexity SDK Overview" icon="code-circle" href="/docs/sdk/overview">
    Install, configure, and use the official Python and TypeScript SDKs.
  </Card>

  <Card title="OpenAI Compatibility" icon="plug" href="/docs/agent-api/openai-compatibility">
    Drop-in compatibility details, supported parameters, and migration tips.
  </Card>

  <Card title="Perplexity MCP Server" icon="server" href="/docs/getting-started/integrations/mcp-server">
    Add Perplexity search, ask, research, and reason tools to Cursor and other MCP clients.
  </Card>
</CardGroup>

<Info>
  Need help? Join the [Perplexity developer community](https://community.perplexity.ai) for support and discussion.
</Info>
