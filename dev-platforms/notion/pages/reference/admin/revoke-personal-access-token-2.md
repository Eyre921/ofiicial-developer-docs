---
title: "Revoke a personal access token in a workspace"
source: https://developers.notion.com/reference/admin/revoke-personal-access-token
path: reference/admin/revoke-personal-access-token
---

openapi-adminApi.json DELETE /v1/spaces/{space_id}/personal_access_tokens/{bot_id}
Permanently revoke a personal access token in a workspace.

The organization bot token must have the following scopes:

* `personal-access-token:write-high-impact`

Use [List personal access tokens](/reference/admin/list-personal-access-tokens) to get the token's `id`, then pass it as `bot_id`.

After revocation, the token can no longer authenticate API requests or access Notion Workers. Repeating the request leaves the token revoked and returns an empty response.

The workspace must belong to the organization that owns the organization bot token. The endpoint returns the same not-found response when the workspace or PAT does not exist, is outside the organization, or does not match the request.
