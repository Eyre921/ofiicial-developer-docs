---
title: "Delete org personal access token"
source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-org-personal-access-token
path: langsmith/smith-api/orgs/delete-org-personal-access-token
---

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/personal-access-tokens/{pat_id}
Delete a personal access token, removing the record entirely.

Callers may always delete their own tokens; organization admins may delete
any member's.
