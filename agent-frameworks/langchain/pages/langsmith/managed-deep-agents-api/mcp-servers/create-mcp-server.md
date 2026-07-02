---
title: "Register an MCP server"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/create-mcp-server
path: langsmith/managed-deep-agents-api/mcp-servers/create-mcp-server
---

/langsmith/managed-deep-agents-openapi.json post /mcp-servers
Register an MCP server in the caller's workspace. Static-header servers can include credential headers. OAuth servers should set `auth_type=oauth` and `oauth_mode=per_user_dynamic_client`, then register an OAuth provider and start an auth session before use.
