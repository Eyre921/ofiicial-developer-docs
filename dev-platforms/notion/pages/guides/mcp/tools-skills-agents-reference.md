---
title: "Reuse instructions and delegate work — technical reference"
source: https://developers.notion.com/guides/mcp/tools-skills-agents-reference
path: guides/mcp/tools-skills-agents-reference
---

Find parameters for importing and enabling Notion Skills, searching memories, and starting and managing Custom Agent sessions.

## Convert a page to a skill

`notion-convert-page-to-skill`

Marks a Notion page as a [Notion Skill](/guides/mcp/notion-skills) without changing its content. Pass the page's full Notion URL. The page must be in the connected workspace, and you must have permission to edit it.

## Download a Notion Skill

`notion-download-skill`

Downloads a complete [Notion Skill](/guides/mcp/notion-skills#download-a-complete-skill). Pass the Skill page's `id`. The response contains `id`, `version_id`, and a signed `url` for a `tar.gz` archive with `SKILL.md` and supporting files and folders. The URL expires after one hour. For a Skill without supporting files, the response has `markdown`, the full `SKILL.md` text with its frontmatter, instead of `url`. Unavailable in eval mode and workspace-owned MCP connections.

## Upload a Notion Skill

`notion-upload-skill`

Imports an [Agent Skills standard](https://agentskills.io/home) directory into an existing page in a Skills database. Uploading takes three steps:

1. Call the tool with `action: "prepare"`, the target `page_id`, and the exact `content_length` and `checksum_crc32` of the `tar.gz` archive. `checksum_crc32` is the archive's big-endian CRC32 encoded as Base64, such as `AAAAAA==`, not as hex or an integer.
2. Send the raw archive bytes in a `PUT` request to the returned `upload_url`, with every header in `upload_headers`.
3. Call the tool with `action: "complete"`, the same `page_id`, and the returned `upload_token`.

The archive must contain `SKILL.md` with `name` and `description` in its YAML frontmatter, either at the root or in one folder named after the Skill. Other frontmatter fields are ignored. Completing the upload replaces the page's title, Description, body, and Files. `SKILL.md` becomes the page content, and the other files and folders are added to Files with their nested paths. Folders from earlier uploads aren't deleted. To upload a new Skill, create a page in a Skills database first.

Archives are limited to 20 MiB compressed, 25 MiB expanded, and 1,000 files and folders. `SKILL.md` can be at most 200,000 UTF-8 bytes. Other limits apply to folder depth and to path and file extension lengths. An upload that breaks any limit is rejected with a `validation_error`. Paths must be unique without regard to case. Links and special files are rejected. Upload URLs and tokens expire after ten minutes. Uploading never runs the Skill's instructions or scripts. Requires the read content, insert content, and update content [capabilities](/reference/capabilities). Unavailable in eval mode.

## Manage enabled Skills

`notion-get-enabled-skills` lists the Notion Skills the user has enabled for MCP clients. It takes no arguments. Each entry has the Skill page's `id`, a `name`, and a `description` of when to use it when one exists. Fetch a Skill's `id` to read it. The list holds at most 30 Skills and has no cursor, so a user with more enabled Skills doesn't see all of them. Long names and descriptions are shortened.

`notion-update-enabled-skills` enables or disables Skills by page URL. Pass up to 50 URLs in `add_skill_urls` or `remove_skill_urls`. `surfaces` picks which settings change: `mcp`, `notion_ai`, or both. It defaults to both. The tool changes only the current user's settings.

Both tools are available only to connections a user authorized with OAuth.

## Search personal memories

`notion-memory-search`

Searches the memories that the user's connected agents saved in earlier sessions, such as context, preferences, corrections, and decisions. Pass words or a short phrase as `query`, up to 500 characters. `limit` defaults to 10 and can be at most 50. Each result has an `id`, `title`, `url`, and `snippet`.

The tool returns the best matches, not every memory. See [Personal memories](/guides/mcp/tools-skills-agents#personal-memories) for an overview and user controls.

Memory tools require a user-backed connection with memories enabled for both the user and workspace. When either setting is off, Notion MCP hides memory search and its guidance, and memory operations are blocked. A client may need to refresh its connection to update its tool list.

### Read, save, and update memories

Existing page tools handle saving and editing memories:

| Operation | Tool and behavior |
| - | - |
| Read the memory destination | `notion-fetch` with `id: "memory"` returns the connected user's About page and Memories database in the current workspace, without creating them. |
| Save a memory | `notion-create-pages` with `parent: "memory"` creates an entry in the managed Memories database. Omit `creation_mode` and set `Type` to `Profile`, `Preference`, `Work`, `People`, or `Notes`. |
| Correct a memory | Fetch the memory page, then use `notion-update-page` to edit its content or properties. Update the About page too if its summary is affected. |
| List, count, or filter memories | Fetch `id: "memory"` to get the data source and schema, then use `notion-query-data-sources`. Query access follows that tool's plan limits. |

The `notion://docs/memory` MCP resource gives agents detailed guidance for saving, recalling, and forgetting memories. Read it once before the first memory search or save in a conversation. Clients that can't read resources can pass the resource URI to `notion-fetch`.

## Work with Custom Agent sessions

Use `notion-search-agents` to find a Custom Agent by name or description,
or to browse the user's favorite agents and the workspace's newest agents.
It returns the Custom Agent URL needed to start a session. Then use these
tools to find sessions, start a session, send follow-up messages, wait for
a reply, stop a run, and read session events:

* `notion-query-sessions`
* `notion-search-sessions`
* `notion-spawn-session`
* `notion-get-session-status`
* `notion-wait-session`
* `notion-stop-session`
* `notion-send-message-to-session`
* `notion-list-session-events`
* `notion-read-session-event`

Search results include up to 20 matches. Each title is limited to 150
characters, and each matching text span is limited to 300 characters.

`notion-search-sessions` returns no matches and a `warning` when the
workspace's search index is missing or not ready. Use
`notion-query-sessions` to list sessions while search is unavailable.

`notion-query-sessions` can return an empty page with a cursor. The same is
true for `notion-search-agents` when it is called without a `query`. Keep
following the cursor until the response stops returning one. A
`notion-search-agents` call with a `query` returns one page without a cursor.

Session tools return a `session_url` in the form
`session://<spaceId>/<sessionId>`. Pass it back unchanged. The tools also
accept the shorthand `session://<sessionId>` and `thread://<sessionId>`,
which resolve in the connected workspace. A full URL whose workspace ID
differs from the connected workspace returns HTTP 400 `validation_error`.
Malformed URLs and URLs for a resource other than a session also return
HTTP 400 `validation_error`. A valid session URL in the connected workspace
returns HTTP 404 `object_not_found` if the session is missing, inaccessible,
or unsupported.

`notion-send-message-to-session` returns a conflict error when the session
already has a run in progress. Wait for that run to finish with
`notion-wait-session`, then send the message.

> [!NOTE]
>
> Plan eligibility and tool discovery are separate. When Notion MCP advertises
> these tools, calling them requires Notion AI access and access to Custom
> Agents. Without that access, calls return a prompt with a recovery link. When
> a direct upgrade is available, `current_tool_access` reports the tools as
> `upgrade_required` with an `upgrade_url`. When Notion routes the user through
> a plan landing page instead, it reports them as `plan_required` with a
> `landing_page_url` and `landing_page_action`. If the workspace has a billing
> restriction, such as an unpaid invoice, calls return a permission error that
> asks a workspace owner to manage billing, and `current_tool_access` reports
> the tools as `not_enabled`.
>
> A connection that lacks the "View sessions and interact with agents"
> capability does not advertise these tools or include them in
> `current_tool_access`. Disconnect and reconnect Notion, or enable the
> capability in the integration's settings and re-authorize.
