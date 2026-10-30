---
title: "Patch workspace"
source: https://docs.langchain.com/langsmith/smith-api/workspaces/patch-workspace
path: langsmith/smith-api/workspaces/patch-workspace
---

/langsmith/langsmith-platform-openapi.json patch /api/v1/workspaces/{workspace_id}
Rename a workspace in the current organization.

Requires the workspace settings manage permission. A name that is already taken returns 409.
