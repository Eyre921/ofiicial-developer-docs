---
title: "Create and organize pages — technical reference"
source: https://developers.notion.com/guides/mcp/tools-pages-reference
path: guides/mcp/tools-pages-reference
---

Find parameters and examples for creating, editing, moving, duplicating, and deleting Notion pages through MCP.

## Create pages

`notion-create-pages`

Creates one or more Notion pages with specified properties and content. Supports applying [database templates](/guides/data-apis/creating-pages-from-templates) to pre-populate new pages with content and property values. Each page can optionally have an icon (an emoji character, a custom emoji by name, a Notion icon identifier as returned by fetch such as "icons/pizza_blue", or an external image URL) and a cover image. Set `is_skill: true` to create a page as a [Notion Skill](/guides/mcp/notion-skills). If a parent is not specified, a private page will be created.

To save a [personal memory](/guides/mcp/tools-skills-agents-reference#read-save-and-update-memories), pass `parent: "memory"` and omit `creation_mode`. Notion creates the managed memory destination on the first save.

To create a top-level page in a teamspace, pass `parent: {"teamspace_id": "…"}` with an ID from `notion-get-teams`. All pages in the call share that parent. See [Teamspace root pages](/guides/mcp/tools-pages-reference#teamspace-root-pages) for permissions and an example.

Use `creation_mode: "draft"` when the user wants a durable page but has not named a destination. Draft mode creates a workspace-level private page and cannot be combined with `parent`. If the user names a private or shared destination, omit `creation_mode` and create the page under that parent.

The tool description recommends `allow_async: true` for most page creates. This is guidance to assistants, not a request default. See [Async page create and update](/guides/mcp/tools-pages-reference#async-page-create-and-update).

Markdown in `content` that is too large or too heavily formatted to parse in one call returns a `validation_error`, and the call creates no pages. All pages in one call share the same parse limit, so a call that creates several pages can reach it even when no single page would. With `allow_async: true`, the call still returns an `async_task`, and the task ends as `failed` with that error. Retrying the same call fails the same way. Create the pages with part of the content and add the rest with further calls, or split the content into child pages.

Each page in the result has a `properties` object with the values the page was saved with, under the keys the tool saved them to. Use those keys in later calls. A repaired key appears under its data-source key, and a date sent under its property name appears under its start key, such as `date:Due:start`. Keys the tool skips, such as `id` and `url`, and any key but `title` on a page outside a database, are left out. Signed file links appear as you sent them.

When the tool repairs a property before it writes a page, the page is still created and the result includes a `warnings` array. For example, a data source with a "URL" property stores it under the key `userDefined:URL`, so a `URL` property in the input is written under that key. Each warning has an `index`, which points to the page in the input `pages` array, plus a `code` and a `message`. Each message is at most 500 characters. A clean create has no `warnings` key. A property value that can't be written still fails the call with a `validation_error`.

```json theme={null}
{
  "pages": [
    {
      "id": "3f20509d-d76d-81a9-8a48-ebb7c86a786e",
      "url": "https://www.notion.so/3f20509dd76d81a98a48ebb7c86a786e",
      "properties": { "userDefined:URL": "https://example.com" }
    }
  ],
  "warnings": [
    {
      "index": 0,
      "code": "create_warning",
      "message": "Wrote property \"URL\" using its data-source key \"userDefined:URL\". Use \"userDefined:URL\" in future calls."
    }
  ]
}
```

## Update a page

`notion-update-page`

Update a Notion page's properties, content, icon, or cover. You can also [change whether a page is a Skill](/guides/mcp/notion-skills#change-whether-a-page-is-a-skill) or apply [database templates](/guides/data-apis/creating-pages-from-templates) to an existing page. Icon, cover, and `is_skill` can be set alongside any update command. To change only the icon or cover, use `update_properties` and omit `properties`.

> [!NOTE]
>
> The `update_content` command applies each search-and-replace operation whose `old_str` matches the page and skips the rest. Each skipped operation appears in `warnings` with code `no_match`, or `indentation_mismatch` when the text is on the page with different indentation. If an operation misses and no content-changing operation matches, the call returns a validation error naming the unmatched values and the page is left unchanged. If the connection can read the page, the error also asks you to fetch the page again and base the retry's `old_str` on its current text; an update that runs as an `async_task` fails with the plain no-match error instead. The error never includes page text. An operation whose `old_str` and `new_str` are identical doesn't change the page and doesn't count as a match. Each `old_str` must be a non-empty string that matches exactly one location, unless `replace_all_matches: true` is set for that operation.

When part of the input was changed or ignored, the result includes a `warnings` array. Examples are operations whose `old_str` matched nothing, lines dropped for incorrect indentation, text auto-corrected to match the page, and a property key repaired before the write, such as `URL` written as `userDefined:URL`. Each warning has a `code` and a `message`. Each message is at most 500 characters; a longer one is cut and ends with a note giving its original length, such as `… (truncated from 12000 characters)`. Markdown parser warnings also carry `category`, such as `unsupported_tag`, and `autofix`, which is `true` when the parser changed the content to apply it. A clean update has no `warnings` key. Read any warnings before you treat the edit as done.

```json theme={null}
{
  "page_id": "3f20509d-d76d-81a9-8a48-ebb7c86a786e",
  "warnings": [
    {
      "code": "update_warning",
      "message": "The following lines were dropped due to incorrect indentation: Dropped line"
    }
  ]
}
```

If the page is too large to load in full (about 20,000 records, most of them blocks) and the edit targets a block that wasn't loaded or would remove content that wasn't loaded, the call returns a `validation_error` and the page is left unchanged. Retrying the same call fails the same way. Content that wasn't loaded appears as `<unknown>` tags when you fetch the page, so edit only content outside those tags.

The tool description recommends `allow_async: true` for most page updates. This is guidance to assistants, not a request default. See [Async page create and update](/guides/mcp/tools-pages-reference#async-page-create-and-update).

## Move pages

`notion-move-pages`

Move one or more Notion pages or databases to a new parent. People can gain or lose access because moved items inherit access from the new parent.

## Duplicate a page

`notion-duplicate-page`

Duplicate a Notion page within your workspace. This action completes asynchronously.

## Delete pages

`notion-delete-pages`

Move up to 20 Notion pages to Trash. Database rows are pages. To move a whole database to Trash, use `notion-delete-databases`. Items in Trash can be restored with `notion-restore-pages` or from Trash in Notion. Locked pages can't be moved to Trash; unlock them in Notion first.

The call must set `user_confirmed: true`. Without it, nothing is moved to Trash, and the error lists the pages so the MCP client can confirm them with the user. The tool is marked destructive (`destructiveHint: true`), so MCP clients that honor tool annotations ask before running it. Requires the update content [capability](/reference/capabilities).

## Get async task status

`notion-get-async-task`

Retrieves the current status of an async task started by another tool, such as `notion-duplicate-page`, `notion-create-pages` with `allow_async: true`, or `notion-update-page` whenever it returns an `async_task`. Returns one of `queued`, `running`, `retrying`, `succeeded`, or `failed`. When a task has succeeded, the operation's result is included in the response; when it has failed, an error is included instead.

Poll this tool with the `task_id` from the originating tool's `async_task` response. Wait briefly between polls — the original response includes a suggested backoff.

## Teamspace root pages

`notion-create-pages` accepts `parent.teamspace_id` to create pages directly in a teamspace, alongside its other top-level pages. Get the ID from `notion-get-teams`; IDs with or without dashes are accepted. Pass only one parent ID per call.

Use a connection that acts as a Notion user. Bot-scoped workspace connections don't support this destination. The user must have permission to edit the teamspace's pages and add top-level pages. If the teamspace limits top-level page edits to owners, the user must be a teamspace owner. Listing a teamspace with `notion-get-teams` doesn't grant permission to create pages there.

New pages inherit the teamspace's permissions, so people with access to its pages can access the new pages. The teamspace must be active and belong to the connected workspace. Omit `creation_mode`: draft mode creates private pages and can't be combined with a teamspace parent.

For example, replace the sample ID with a teamspace ID returned by `notion-get-teams`:

```json theme={null}
{
  "tool": "notion-create-pages",
  "arguments": {
    "parent": { "teamspace_id": "195de922-1179-449f-ab80-75a27c979105" },
    "allow_async": true,
    "pages": [
      {
        "properties": { "title": "Project kickoff" },
        "content": "# Project kickoff\n\nGoals, owners, and next steps."
      }
    ]
  }
}
```

Teamspace root creation supports both synchronous and [async page creation](/guides/mcp/tools-pages-reference#async-page-create-and-update). When the tool returns an `async_task`, wait for it to succeed before using the new pages. This parent option is specific to Notion MCP; it isn't a parent option for the REST [Create a page](/reference/post-page) endpoint.

## Async page create and update

The `notion-create-pages` and `notion-update-page` tools support `allow_async: true` for page create and update work. Their tool descriptions recommend that assistants pass it for most page writes. This is guidance to assistants, not a schema or server default: omitting `allow_async` has the same meaning as before. The same validation, permissions, and write operation still apply.

The descriptions recommend `allow_async: false` when the next step needs the created or updated page right away. They also recommend retrying synchronously when an async attempt is rejected as too large to queue.

A request that is too large to queue returns a `validation_error` instead of an `async_task`. Either split it into smaller page writes or retry it with `allow_async: false`.

When a call returns an `async_task` handle, poll `notion-get-async-task` with the returned `async_task.id` passed as `task_id` until the task reaches `succeeded` or `failed`. Wait for `succeeded` before any step that depends on the write, such as linking to a new page or adding content to it.

> [!NOTE]
>
> A `succeeded` status covers the page write, not template application. When dependent work needs template output, follow the webhook flow in [Creating pages from templates](/guides/data-apis/creating-pages-from-templates#step-3-confirm-page-contents-are-ready). For direct checks, look for the expected content or properties and stop after a bounded number of retries.

When `allow_async` is omitted or `false`, `notion-create-pages` keeps its synchronous result shape. `notion-update-page` waits for a synchronous result when it can, but it can still return a pollable `async_task` if queued execution runs past the synchronous wait deadline, so handle both shapes.

```json theme={null}
{
  "tool": "notion-create-pages",
  "arguments": {
    "allow_async": true,
    "parent": { "page_id": "YOUR_PAGE_ID" },
    "pages": [
      {
        "properties": { "title": "Migration plan" },
        "content": "# Migration plan\n\nLarge markdown content..."
      }
    ]
  }
}
```

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "queued",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "mcp",
    "name": "create_pages"
  }
}
```

```json theme={null}
{
  "tool": "notion-update-page",
  "arguments": {
    "allow_async": true,
    "page_id": "YOUR_PAGE_ID",
    "command": "replace_content",
    "new_str": "# Updated plan\n\nLarge replacement markdown..."
  }
}
```

```json theme={null}
{
  "tool": "notion-get-async-task",
  "arguments": {
    "task_id": "task_abc123"
  }
}
```

If the task is still `queued`, `running`, or `retrying`, wait at least the suggested `poll_after_seconds` before polling again. A `succeeded` task includes the operation result. For `notion-create-pages` and `notion-update-page`, that result includes the same `warnings` array as a direct call. A `failed` task includes an error object that the assistant can summarize or use to retry with a corrected request.
