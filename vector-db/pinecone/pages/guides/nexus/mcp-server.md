---
title: "MCP server"
source: https://docs.pinecone.io/guides/nexus/mcp-server
path: guides/nexus/mcp-server
---

Query your Pinecone Nexus contexts from any Model Context Protocol client, such as Claude Desktop, over Streamable HTTP.

The Nexus MCP server exposes three read-only tools, `list_contexts`, `query_context`, and `get_query`, over Streamable HTTP at your deployment's workspace host with the `/mcp` path.

## Prerequisites

* **A Pinecone API key** with access to your Nexus project. Create one in the [Pinecone console](https://app.pinecone.io/organizations/-/keys).
* **The MCP endpoint.** Your deployment's workspace host with the `/mcp` path (the base of `nexus_default_workspace_data_console_url` from the [install output](/guides/nexus/byoc/deploy)).
* **Node.js**, so the `mcp-remote` bridge can run through `npx`.

## Connect

Add this server config to your MCP client. Swap `YOUR_PINECONE_API_KEY` for your Pinecone API key. The server logs in with it per request, so every caller queries their own project. For clients that launch local stdio servers, the `mcp-remote` bridge connects them to the remote Streamable HTTP endpoint.

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

* `list_contexts`: list the contexts available to your project (each has a `slug`, and only curated contexts are queryable). Takes no arguments and returns an array of context objects, each shaped `{ slug, name, id, description, queryable, is_curating, is_optimizing, last_curated_at, last_optimized_at }`. `queryable` turns true once the context has been curated, `is_curating` and `is_optimizing` flag whether work is running now, and the two timestamps are ISO strings or `null`.
* `query_context`: submit a question scoped to one context. Args: `context` (slug), `question`. Runs in background mode and returns a `query_id` immediately without waiting for the answer. The return object is `{ query_id, status, model }`. Pass the `query_id` to `get_query` to fetch the result.
* `get_query`: poll the result of a submitted query. Args: `query_id`. Returns `{ query_id, answer, output_json, citations, model, status, error }`. `answer` is the grounded answer text, or `null` until it is ready. `output_json` holds structured output when the query requested a shape, otherwise `null`. `citations` is an array of source references and `error` is set only when the query failed. Keep polling until `status` is `completed`, `failed`, or `cancelled`.
