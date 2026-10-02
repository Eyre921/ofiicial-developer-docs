---
title: "List personal access tokens in a workspace"
source: https://developers.notion.com/reference/admin/list-personal-access-tokens
path: reference/admin/list-personal-access-tokens
---

openapi-adminApi.json GET /v1/spaces/{space_id}/personal_access_tokens
List active, expired, and revoked personal access tokens in a workspace.

The organization bot token must have the following scopes:

* `personal-access-token:read`

This endpoint returns personal access token (PAT) records, but never returns token values. Use the `id` from a result as the `bot_id` when you [revoke the token](/reference/admin/revoke-personal-access-token).

## Filter results

Use `status` to return active, expired, or revoked tokens. Use `creator_ids` to filter by the members who created the tokens, and use `search` to match a token name.

Use bracket encoding to filter by more than one status or creator:

```text theme={null}
?status[]=active&status[]=expired&creator_ids[]=aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa
```

To learn how PATs work and how members create them, see [Personal access tokens](/guides/get-started/personal-access-tokens).
