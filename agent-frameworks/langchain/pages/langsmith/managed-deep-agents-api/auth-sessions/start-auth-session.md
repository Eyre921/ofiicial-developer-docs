---
title: "Start an authorization session"
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/auth-sessions/start-auth-session
path: langsmith/managed-deep-agents-api/auth-sessions/start-auth-session
---

/langsmith/managed-deep-agents-openapi.json post /auth-sessions
Start an OAuth authorization session for the caller. If the user is already authorized, the response can be completed immediately. Otherwise, the response includes a verification URL that the user must visit to complete authorization.
