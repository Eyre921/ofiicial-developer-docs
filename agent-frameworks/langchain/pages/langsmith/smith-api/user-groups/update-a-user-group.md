---
title: "Update a user group"
source: https://docs.langchain.com/langsmith/smith-api/user-groups/update-a-user-group
path: langsmith/smith-api/user-groups/update-a-user-group
---

/langsmith/langsmith-platform-openapi.json patch /api/v1/platform/orgs/current/user-groups/{user_group_id}
Renames an organization-wide user group or changes its description or IdP group mapping.
Omitted fields are left unchanged, and a null description or idp_group_name clears
it. idp_sync_enabled needs an IdP group. A workspace scoped user group returns 400: its
workspace grant creates and deletes it. Needs organization:user-groups:manage.
