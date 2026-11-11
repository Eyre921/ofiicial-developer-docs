---
title: "Work together in Notion — technical reference"
source: https://developers.notion.com/guides/mcp/tools-comments-reference
path: guides/mcp/tools-comments-reference
---

Find parameters and permissions for Notion MCP comments, discussions, suggested edits, page history, and restoring pages.

## Add a comment

`notion-create-comment`

Add a comment to a page or specific content. Supports page-level comments,
block-level comments (via content selection), and replies to existing discussions.

## Get comments

`notion-get-comments`

Lists all comments and discussions on a page. Can include block-level and
inline discussions, resolved threads, and full comment content. Comments the
connected user wrote are marked `by-you="true"`.

Pending suggested edits are listed with `kind="suggested_edit"`. Pass their `discussion://` URL to `notion-get-suggested-edit`. The response's `suggested_edits_status` is `included` when pending suggestions are in the list, `upgrade_required` when the workspace isn't on a Business or Enterprise plan, and `not_enabled` when the connection doesn't support them. Use it to tell an empty result apart from one that couldn't include suggestions.

## Edit and react to comments

These tools change existing comments and discussions. Get comment and discussion IDs from `notion-get-comments` or `notion-create-comment`. Comment IDs work with or without dashes.

* `notion-update-comment` replaces the text of a comment the user wrote. Pass `comment_id` and the full new text as inline markdown in `markdown`. The new text replaces the whole comment. Block-level markdown, such as lists and headings, isn't supported.
* `notion-delete-comment` deletes a comment the user wrote. If it's the last comment in its discussion, the discussion is removed too.
* `notion-set-discussion-resolved` resolves a discussion with `resolved: true` or reopens it with `resolved: false`. Pass `discussion_id`, either a `discussion://` URL from `notion-get-comments` or the `discussion_id` from `notion-create-comment`.
* `notion-set-comment-reaction` adds (`reacted: true`) or removes (`reacted: false`) the user's reaction on a comment. Pass one standard Unicode emoji in `emoji`. Setting the same state twice changes nothing.

> [!NOTE]
>
> Requires a Business or Enterprise plan. On other plans the tools return an upgrade prompt.

Users can edit and delete only their own comments. The tool descriptions tell assistants to fix a comment with `notion-update-comment` instead of deleting it and posting a new one, and to resolve a discussion only when a person asks.

## Suggest edits

These tools propose changes to a page that a person accepts or rejects in Notion. A suggestion doesn't change the page until someone accepts it. `notion-fetch` shows only accepted content, so pending suggestions don't appear in fetched page text.

* `notion-create-suggested-edit` proposes one change. Pass the page as `page_id`, the exact text to change as `old_text`, and the proposed Notion-flavored Markdown as `new_text`. Copy `old_text` from `notion-fetch` output. It must appear exactly once on the page. `mode` defaults to `replace`, and an empty `new_text` suggests a deletion. With `insert_before` or `insert_after`, `old_text` is an anchor that stays as it is, and `new_text` is only the inserted content. A suggestion can span blocks and change text, formatting, mentions, equations, and tables, or add, remove, or replace blocks. To suggest a change to a page title or a database title or text property, pass its name as `property_name` and use `replace`. You can't insert into an empty page. The response has a `suggested_edit_url` and `status: "pending"`.
* `notion-get-suggested-edit` reads one pending suggestion. Pass its `suggested_edit_url`. The response has a Markdown before-and-after `diff` and the `allowed_actions` the user can take, `accept`, `reject`, or both.
* `notion-resolve-suggested-edit` accepts or rejects one pending suggestion. Pass `suggested_edit_url` and `action`. Accepting applies the change to the page. Rejecting discards it. The tool is marked destructive (`destructiveHint: true`), so MCP clients that honor tool annotations ask before running it.

In Notion, each suggestion appears on the page as a suggested edit with its own discussion thread. You can pass a single-line inline Markdown `comment` to start that thread.

> [!NOTE]
>
> Requires a Business or Enterprise plan. On other plans the tools return an upgrade prompt.

Creating a suggestion needs comment access to the page. Accepting needs edit access to the page. Users can reject their own suggestions with comment access, and anyone's suggestions with edit access. Creating and resolving need the insert comments [capability](/reference/capabilities), and reading needs the read comments capability. Accepting also needs the update content capability.

One suggestion can't overlap another pending suggestion. To change a pending suggestion, reject it, then create a new one. If someone edits the text a suggestion covers, the suggestion becomes stale. A stale suggestion can't be read or accepted, but it can still be rejected. Errors return an HTTP 400 `validation_error` with `additional_data.tool_error_code` set to a code such as `suggested_edit_no_match`, `suggested_edit_multiple_matches`, `suggested_edit_conflict`, or `suggested_edit_stale`.

## Restore pages

`notion-restore-pages`

Restore up to 20 Notion pages or databases from Trash to where they were before they were deleted. Restoring an item that is already out of Trash succeeds and changes nothing. Requires the update content [capability](/reference/capabilities).

If a page's parent is still in Trash, the call returns an error that asks you to restore the parent first. Pages at the top level of a workspace, such as top-level private pages, can't be restored through Notion MCP yet. Restore them from Trash in Notion.

## View a past version

`notion-view-version`

Reads a page or database as it looked at a past time. Pass the page and an ISO 8601 `time`. A page returns its properties and Markdown content. A database returns its data sources, views, and rows. Requires edit access to the page, and can only read as far back as the workspace's plan keeps version history.

## Get version changes

`notion-get-version-changes`

Lists what changed in a page or database between two times and who made each change, including edits from Notion AI, Custom Agents, and MCP clients. The range defaults to the last 24 hours. Requires edit access to the page, and can only read as far back as the workspace's plan keeps version history.

## Restore a past version

`notion-restore-version`

Restores a page or database to how it looked at a past time. This undoes every edit made after that time, including other people's, and removes comments added after it. Subpages and database row pages keep their content, so restore each one on its own. Databases inside a page stay as they are unless you set `include_inline_databases: true`.

Call it first without `user_confirmed`. Nothing changes, and the response says what the restore would undo. Show that to the user, and only after they agree, call again with `user_confirmed: true`. The restore then runs in the background.

Requires edit access to the page and the update content [capability](/reference/capabilities). It can only go back as far as the workspace's plan keeps version history.
