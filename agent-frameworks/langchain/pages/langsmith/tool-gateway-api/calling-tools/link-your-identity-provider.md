---
title: "Link your identity provider"
source: https://docs.langchain.com/langsmith/tool-gateway-api/calling-tools/link-your-identity-provider
path: langsmith/tool-gateway-api/calling-tools/link-your-identity-provider
---

/langsmith/tool-gateway-openapi.json put /v1/managed-tools/oidc-connection
Links an enabled identity provider in this workspace so its access tokens can authenticate MCP calls, replacing any current link. Requires workspaces:integrations:manage. Call as yourself.
