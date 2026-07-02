---
title: "Get sandbox access decision"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-sandbox-access-decision
path: langsmith/smith-api/sandboxes/get-sandbox-access-decision
---

/langsmith/langsmith-platform-openapi.json get /auth/sandbox-access
Combines authn + per-sandbox authz for runtime access. Returns the caller's PublicAuthInfo on allow (HTTP 200) or a 403 with the deny reason on deny.
