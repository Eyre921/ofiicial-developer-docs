---
title: "Get skill"
source: https://developers.notion.com/reference/agent-skills/get-skill-directory
path: reference/agent-skills/get-skill-directory
---

openapi.json GET /v1/ai/skills/{id}
Download a skill directory containing its instructions and supporting files.

Returns a signed URL to a gzipped tar archive containing one skill directory. Pass the Notion page ID of a skill that is shared with the connection.

The archive has one top-level directory containing `SKILL.md` and any files or folders attached through the skill's **Files** property. It does not include a `plugin.json` file or a `skills/` wrapper directory.

For an overview of how to use the Agent Skills API, see the [guide overview](/guides/agent-skills/overview).

## Errors

| Status | Code                  | Cause                                                                            |
| :----- | :-------------------- | :------------------------------------------------------------------------------- |
| 400    | `validation_error`    | The supplied skill ID is malformed.                                              |
| 404    | `directory_not_found` | No skill with that ID is shared with the connection, or the ID no longer exists. |
| 403    | `restricted_resource` | The token lacks the **Read content** capability.                                 |
