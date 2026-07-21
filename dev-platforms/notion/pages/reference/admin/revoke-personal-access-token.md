---
title: "Revoke a personal access token in a workspace"
source: https://developers.notion.com/reference/admin/revoke-personal-access-token
path: reference/admin/revoke-personal-access-token
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/personal_access_tokens/{bot_id}
Revoke a personal access token in a workspace.

The organization bot token must have the following scopes:

* `personal-access-token:write-high-impact`
