---
title: "Upload a skill"
source: https://developers.notion.com/reference/agent-skills/upload-skill
path: reference/agent-skills/upload-skill
---

POST /v1/ai/skills/{id}/upload
Upload a skill directory archive to a skill page in one request.

Imports a skill directory into an existing page in a Skills database. Pass the page ID in the path, and send a gzipped tar archive of the directory under the `file` key of a `multipart/form-data` body. The archive can be up to 20 MiB.

> [!NOTE]
>
> Like [Send a file upload](/reference/upload-file), this endpoint takes multipart form data instead of JSON. Include a `boundary` in the `Content-Type` header.

The archive must contain `SKILL.md` with `name` and `description` frontmatter, either at the root or in one directory named after the skill. Uploading replaces the page's title, **Description**, content, and **Files**. Each file and folder next to `SKILL.md` becomes a file or folder in **Files**.

The response includes the updated page ID and `version_id`. It matches the `version_id` from [Get a skill](/reference/agent-skills/get-skill-directory) until the skill changes again, so you can tell whether a later download returns what you uploaded.

To import a new skill, create a page in a Skills database first.

## Errors

| Status | Code | Cause |
| :- | :- | :- |
| 400 | `validation_error` | The ID is malformed, `file` is missing or not sent as form data, the archive is invalid, or the page is not in a Skills database. |
| 403 | `restricted_resource` | The token lacks the **Read content**, **Insert content**, or **Update content** capability. |
| 404 | `object_not_found` | No page with that ID is shared with the connection. |
