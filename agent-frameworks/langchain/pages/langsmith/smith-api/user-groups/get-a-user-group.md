---
title: "Get a user group"
source: https://docs.langchain.com/langsmith/smith-api/user-groups/get-a-user-group
path: langsmith/smith-api/user-groups/get-a-user-group
---

/langsmith/langsmith-platform-openapi.json get /api/v1/platform/orgs/current/user-groups/{user_group_id}
Gets one user group in the organization.
An organization scoped user group needs organization:user-groups:read.
A workspace scoped user group needs workspaces:user-groups:read in its workspace.
