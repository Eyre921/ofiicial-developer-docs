---
title: "Update an MCP server"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/update-mcp-server
path: langsmith/managed-deep-agents-api/mcp-servers/update-mcp-server
---

/langsmith/managed-deep-agents-openapi.json patch /mcp-servers/{mcp_server_id}
Update an MCP server's URL, credential headers, or auth configuration. Passing `headers` replaces the entire stored header array — partial diffs are not supported. Use this endpoint to rotate credentials.
