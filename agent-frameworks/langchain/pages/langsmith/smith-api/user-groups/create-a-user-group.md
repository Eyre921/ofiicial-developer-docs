---
title: "Create a user group"
source: https://docs.langchain.com/langsmith/smith-api/user-groups/create-a-user-group
path: langsmith/smith-api/user-groups/create-a-user-group
---

/langsmith/langsmith-platform-openapi.json post /api/v1/platform/orgs/current/user-groups
Creates an organization-wide user group. Needs organization:user-groups:manage. Workspace scoped
user groups are not created here: granting an organization-wide user group access to a
workspace creates its workspace scoped user group there, so workspace_id and
parent_user_group_id return 400.
