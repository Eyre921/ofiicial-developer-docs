---
title: "Get tools"
source: https://docs.langchain.com/langsmith/smith-api/mcp/get-tools
path: langsmith/smith-api/mcp/get-tools
---

/langsmith/langsmith-platform-openapi.json get /api/v1/mcp/tools
Return MCP tools — from cache if fresh, otherwise by fetching from remote.

On cache miss, tries manifest fetch first (fast), then falls back to full
MCP handshake. Caches the result before returning.

Pass force_refresh=true to bypass the cache and always fetch from the
remote server (the result is still cached via upsert for future requests).

The ls_user_id query parameter allows service-key callers (which don't carry
ls_user_id in auth) to specify the user for per-user OAuth cache lookups.
