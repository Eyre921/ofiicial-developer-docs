---
title: "Remove an MCP server"
source: https://docs.langchain.com/langsmith/tool-gateway-api/adding-tools/remove-an-mcp-server
path: langsmith/tool-gateway-api/adding-tools/remove-an-mcp-server
---

/langsmith/tool-gateway-openapi.json delete /v1/managed-tools/servers/{id}
Deletes an MCP server and its credential setup; shared OAuth connections are kept. Requires mcp-servers:delete for a workspace server. Call as yourself. Only the user who registered a personal server can delete it.
