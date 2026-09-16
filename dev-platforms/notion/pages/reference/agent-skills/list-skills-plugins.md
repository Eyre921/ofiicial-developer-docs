---
title: "List plugins"
source: https://developers.notion.com/reference/agent-skills/list-skills-plugins
path: reference/agent-skills/list-skills-plugins
---

openapi.json GET /v1/ai/plugins
List the plugins available to your connection.

Returns the list of available plugins. To fetch an individual plugin from the list, call [Get plugin](/reference/agent-skills/get-plugin-directory).

The response includes plugins for skills shared with the connection. If you see fewer plugins than expected, check the connection's access to your skills databases.

Each unique value in a skills database's **Tags** property becomes a plugin. An untagged skill becomes a plugin containing only that skill.

For an overview of how to use the Agent Skills API, see the [guide overview](/guides/agent-skills/overview).

## Using version\_id

`version_id` is an opaque string. An unchanged value means the plugin's contents are unchanged so you can skip re-downloading its directory.

## Pagination

This endpoint uses [standard cursor pagination](/reference/intro#pagination). Follow `next_cursor` until `has_more` is `false`.

## Errors

| Status | Code                  | Cause                                                                               |
| :----- | :-------------------- | :---------------------------------------------------------------------------------- |
| 400    | `validation_error`    | `start_cursor` is malformed, out of range, or was issued for a different workspace. |
| 403    | `restricted_resource` | The token lacks the **Read content** capability.                                    |
