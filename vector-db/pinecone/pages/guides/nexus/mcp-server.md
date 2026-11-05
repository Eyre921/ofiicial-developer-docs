---
title: "Connect an MCP client to Pinecone Nexus"
source: https://docs.pinecone.io/guides/nexus/mcp-server
path: guides/nexus/mcp-server
---

Query your Pinecone Nexus contexts from any MCP client, such as Claude Desktop, over Streamable HTTP.

The Nexus Model Context Protocol (MCP) server lets any MCP client query your Nexus contexts over Streamable HTTP. It serves three read-only tools: `list_contexts`, `query_context`, and `get_query`.

## Prerequisites

* A Pinecone API key with access to your Nexus project. Create one in the [Pinecone console](https://app.pinecone.io/organizations/-/keys).
* The MCP endpoint, your deployment's workspace host with the `/mcp` path (the base of `nexus_default_workspace_data_console_url` from the [install output](/guides/nexus/byoc/deploy)).
* Node.js, so the `mcp-remote` bridge can run through `npx`.

## Add the server config

Add the config below to your MCP client, replacing `YOUR_WORKSPACE_HOST` and `YOUR_PINECONE_API_KEY` with your own values. The server authenticates each request with the key you pass, so every caller queries their own project. The `mcp-remote` bridge lets clients that only launch local stdio servers reach the remote HTTP endpoint.

```json theme={null}
{
  "mcpServers": {
    "nexus": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://YOUR_WORKSPACE_HOST/mcp",
        "--header", "X-Pinecone-Api-Key:YOUR_PINECONE_API_KEY",
        "--transport", "http-only"
      ]
    }
  }
}
```

## Tools

* `list_contexts`: List the contexts available to your project (each has a `slug`). Takes no arguments and returns an array of context objects, each shaped `{ slug, name, id, description, queryable, is_curating, is_optimizing, last_curated_at, last_optimized_at }`. `queryable` turns true once the context has been optimized, `is_curating` and `is_optimizing` flag whether work is running now, and the two timestamps are ISO strings or `null`.
* `query_context`: Submit a question scoped to one context. Args: `context` (slug), `question`. Runs in background mode and returns a `query_id` immediately without waiting for the answer. The return object is `{ query_id, status, model }`. Pass the `query_id` to `get_query` to fetch the result.
* `get_query`: Poll the result of a submitted query. Args: `query_id`. Returns `{ query_id, answer, output_json, citations, model, status, error }`. `answer` is the grounded answer text, or `null` until it's ready. `output_json` holds structured output when the query requested a shape, otherwise `null`. `citations` is an array of source references and `error` is set only when the query failed. Keep polling until `status` is `completed`, `failed`, or `cancelled`.
