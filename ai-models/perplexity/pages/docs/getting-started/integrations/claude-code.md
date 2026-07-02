---
title: "Perplexity with Claude Code"
source: https://docs.perplexity.ai/docs/getting-started/integrations/claude-code
path: docs/getting-started/integrations/claude-code
---

Use Perplexity inside Claude Code — call the API from project code with the official TypeScript SDK, use the OpenAI-compatible base URL, or wire up the hosted Perplexity Docs MCP for in-editor documentation lookup.

## Overview

[Claude Code](https://docs.claude.com/en/docs/claude-code) is Anthropic's agentic coding tool that lives in your terminal, IDE, and CI. It can edit files, run commands, and call Model Context Protocol (MCP) servers as part of its workflow. This guide covers three integration paths for Perplexity:

<CardGroup>
  <Card title="Official TypeScript SDK" icon="code">
    Let Claude Code write and run application code that calls the Perplexity API directly. **Recommended.**
  </Card>

  <Card title="OpenAI-Compatible SDK" icon="plug">
    Reuse an existing OpenAI client by pointing `baseURL` at `https://api.perplexity.ai/v1`.
  </Card>

  <Card title="Claude Code MCP" icon="book">
    Register the hosted Perplexity Docs MCP with `claude mcp add` so Claude Code can look up Perplexity docs while you work.
  </Card>
</CardGroup>

<Info>
  **Recommended path:** Have Claude Code build features against your project code using the official SDK (or the OpenAI-compatible SDK), and register the Perplexity Docs MCP for in-editor documentation lookup. Claude Code does **not** officially support swapping its underlying model for the Perplexity API — see [Replacing Claude Code's model (not recommended)](#replacing-claude-codes-model-not-recommended).
</Info>

## Prerequisites

* Claude Code installed — see the [Claude Code quickstart](https://docs.claude.com/en/docs/claude-code/quickstart)
* Node.js 18+ for the TypeScript examples
* A Perplexity API key

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate a key from the Perplexity API Portal.
</Card>

## API key handling

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
  Treat `PERPLEXITY_API_KEY` like a password. Don't paste it into prompts, share it with Claude Code, or commit it to source control. If a key is exposed, [rotate it](https://console.perplexity.ai) immediately.
</Warning>

***

## Path 1: Official TypeScript SDK (recommended)

Have Claude Code scaffold and edit code that calls the Perplexity API using the official SDK. This is the most reliable path and gives you full type safety, preset support, and access to every API feature.

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

### Add web search

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
  Ask Claude Code to scaffold these calls for you — for example, *"Add a `summarize.ts` script that uses `@perplexity-ai/perplexity_ai` with the `pro-search` preset and reads `PERPLEXITY_API_KEY` from the environment."* Claude Code will edit the file, install the package, and run it.
</Tip>

For more presets, tools, and configuration options see the [Agent API quickstart](/docs/agent-api/quickstart) and the [SDK overview](/docs/sdk/overview).

***

## Path 2: OpenAI-compatible SDK

If your project already uses an OpenAI client, you can reuse it by pointing the `baseURL` at `https://api.perplexity.ai/v1`. Perplexity accepts `POST /v1/responses` as an alias for the Agent API.

### Install

```bash theme={null}
npm install openai
```

### Use it

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

## Path 3: Claude Code MCP for docs lookup

Claude Code supports the Model Context Protocol (MCP). The hosted **Perplexity Docs MCP** at `https://docs.perplexity.ai/mcp` lets Claude Code search and read Perplexity's documentation directly — useful for grounding code suggestions in canonical docs without context-switching to a browser.

### Add the server

Claude Code can register a remote MCP server over HTTP using the `claude mcp add` command with the `--transport http` flag:

<Tabs>
  <Tab title="Project scope">
    Add the server only for the current project (writes to `.mcp.json` in your repo root):

    ```bash theme={null}
    claude mcp add --transport http --scope project perplexity-docs https://docs.perplexity.ai/mcp
    ```
  </Tab>

  <Tab title="User scope">
    Add the server for all projects on this machine:

    ```bash theme={null}
    claude mcp add --transport http --scope user perplexity-docs https://docs.perplexity.ai/mcp
    ```
  </Tab>
</Tabs>

<Tip>
  If you'd rather not run the CLI, you can also edit the project's `.mcp.json` directly:

  ```json theme={null}
  {
    "mcpServers": {
      "perplexity-docs": {
        "type": "http",
        "url": "https://docs.perplexity.ai/mcp"
      }
    }
  }
  ```

  Claude Code reads `.mcp.json` at the repo root for project-scoped servers. Refer to the [Claude Code MCP documentation](https://docs.claude.com/en/docs/claude-code/mcp) for the canonical schema and any newer transport options.
</Tip>

### Verify and use

<Steps>
  <Step title="Confirm the server is registered">
    Run `claude mcp list` and check that `perplexity-docs` appears in the output.
  </Step>

  <Step title="Restart Claude Code">
    Quit and relaunch Claude Code (or run `/mcp` from inside a session) so the new server is loaded.
  </Step>

  <Step title="Use it from a prompt">
    Ask Claude Code something like *"Using the Perplexity docs MCP, show me how to enable `pro-search` in the Agent API."* Claude Code will call the MCP server and ground its answer in current documentation.
  </Step>
</Steps>

<Info>
  The Docs MCP is read-only and does not require an API key — it only serves Perplexity documentation. To give Claude Code access to Perplexity **search and reasoning** tools (not just docs), install the [Perplexity MCP Server](/docs/getting-started/integrations/mcp-server), which uses `@perplexity-ai/mcp-server` and requires `PERPLEXITY_API_KEY`.
</Info>

***

## Replacing Claude Code's model (not recommended)

Claude Code is designed to run on Anthropic's Claude models, and the agent's tool use, prompting, and editing behavior are tuned to those models. Pointing the Claude Code CLI at the Perplexity API as an alternative model provider is **not an officially supported configuration**.

Instead:

* **Use Perplexity from your project code** (Path 1 or Path 2). Claude Code will happily write, edit, and run code that calls Perplexity for web-grounded answers, research, and search.
* **Add the Perplexity Docs MCP** (Path 3) so Claude Code can look up Perplexity documentation in-session.

This combination gives you Claude Code's editing and orchestration strengths alongside Perplexity's search-grounded responses, without depending on undocumented model-override behavior.

***

## Next steps

<CardGroup>
  <Card title="Agent API quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Presets, tools, and the full Agent API surface used by the examples above.
  </Card>

  <Card title="Perplexity SDK overview" icon="code-circle" href="/docs/sdk/overview">
    Install, configure, and use the official Python and TypeScript SDKs.
  </Card>

  <Card title="OpenAI compatibility" icon="plug" href="/docs/agent-api/openai-compatibility">
    Drop-in compatibility details, supported parameters, and migration tips.
  </Card>

  <Card title="Perplexity MCP Server" icon="server" href="/docs/getting-started/integrations/mcp-server">
    Add Perplexity search, ask, research, and reason tools to Claude Code and other MCP clients.
  </Card>
</CardGroup>

<Info>
  Need help? Join the [Perplexity developer community](https://community.perplexity.ai) for support and discussion.
</Info>
