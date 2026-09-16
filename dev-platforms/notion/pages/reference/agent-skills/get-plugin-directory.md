---
title: "Get plugin"
source: https://developers.notion.com/reference/agent-skills/get-plugin-directory
path: reference/agent-skills/get-plugin-directory
---

openapi.json GET /v1/ai/plugins/{id}
Download a plugin directory containing skills and supporting files.

Pass in an `id` from [List plugins](/reference/agent-skills/list-skills-plugins).

Returns a signed URL to a gzipped tar archive of a plugin directory following the [Agent Plugins](https://agent-plugins.org) standard.

Currently plugins returned by Notion only contain skills and no MCP resources or extensions, but this may change in the future. You should treat the entire folder returned by the API as a standard-compliant plugin.

For an overview of how to use the Agent Skills API, see the [guide overview](/guides/agent-skills/overview).

## Plugin size limits

A plugin directory includes at most 100 skills; when a plugin has more, the most recently updated ones are included.

## Errors

| Status | Code                  | Cause                                                                             |
| :----- | :-------------------- | :-------------------------------------------------------------------------------- |
| 404    | `directory_not_found` | No plugin with that ID is shared with the connection, or the ID no longer exists. |
| 403    | `restricted_resource` | The token lacks the **Read content** capability.                                  |
