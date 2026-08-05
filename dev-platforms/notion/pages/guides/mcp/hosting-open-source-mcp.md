---
title: "Hosting a local MCP server"
source: https://developers.notion.com/guides/mcp/hosting-open-source-mcp
path: guides/mcp/hosting-open-source-mcp
---

Learn how and when to use the open-source Notion MCP server.

<Warning>
  The open-source `notion-mcp-server` package is no longer actively maintained. We recommend the remote [Notion MCP](/guides/mcp/get-started-with-mcp) server for most clients. Issues and pull requests on the open-source repository are not actively monitored.
</Warning>

If you need to run your own MCP server, the [`notion-mcp-server` package](https://github.com/makenotion/notion-mcp-server) is available as an open-source implementation. This option may be suitable if you:

* Need bearer token authentication for fully automated workflows
* Already have an existing Notion connection you want to reuse
* Require access to the original JSON-based v1 APIs
* Prefer to manage infrastructure yourself

Compared to Notion's remote MCP, running the open-source server requires more technical setup, including provisioning your own Notion connection, managing API tokens, and handling deployment.

<Note>
  The remote Notion MCP server at `https://mcp.notion.com/mcp` requires no self-hosted infrastructure and receives current tools and updates.
</Note>

## Next steps

If you still want to self-host, explore the [GitHub repo](https://github.com/makenotion/notion-mcp-server) to get started.

For the recommended approach, see [Connecting to Notion MCP](/guides/mcp/get-started-with-mcp).
