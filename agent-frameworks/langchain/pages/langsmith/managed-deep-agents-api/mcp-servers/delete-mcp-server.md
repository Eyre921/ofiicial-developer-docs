---
title: "Delete an MCP server"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/delete-mcp-server
path: langsmith/managed-deep-agents-api/mcp-servers/delete-mcp-server
---

/langsmith/managed-deep-agents-openapi.json delete /mcp-servers/{mcp_server_id}
Delete an MCP server. The call is idempotent: deleting a non-existent server returns `204`. After deletion, agents whose tools reference this server's URL will no longer have the stored headers attached at invocation time.
