---
title: "Update a page's content as markdown"
source: https://developers.notion.com/reference/update-page-markdown
path: reference/update-page-markdown
---

patch /v1/pages/{page_id}/markdown
Insert or replace content in a page using markdown.

### Use cases

#### Updating content with search-and-replace (recommended)

Use the `update_content` command to make targeted edits using an array of search-and-replace operations. Each operation specifies an `old_str` to find and a `new_str` to replace it with. This is the recommended approach for making precise edits without rewriting the full page.

#### Replacing all page content (recommended)

Use the `replace_content` command to replace the entire page content with new markdown. Provide the full replacement content in `new_str`.

#### Inserting content (legacy)

Use the `insert_content` command to add new markdown content to a page. Provide `position: { "type": "start" }` to prepend, `position: { "type": "end" }` to explicitly append, or omit `position` to append to the end of the page. You can also provide an `after` selection to insert at a specific point; `after` uses an **ellipsis-based selection** format: `"start text...end text"`.

<Note>
  We recommend using `update_content` or `replace_content` instead. The `insert_content` command is still supported but may be deprecated in a future version.
</Note>

#### Replacing a content range (legacy)

Use the `replace_content_range` command to replace a matched range of existing content with new markdown. The `content_range` parameter uses the same ellipsis-based selection format as `after`.

<Note>
  We recommend using `update_content` instead. The `replace_content_range` command is still supported but may be deprecated in a future version.
</Note>

### General behavior

Returns a `page_markdown` object containing the full page content as markdown after the update, in the request's `markdown_version` syntax, including `truncated` and `unknown_block_ids` fields for large pages.

Set `allow_async: true` at the top level of the request body to receive an HTTP `202` response with an `async_task` object instead of waiting for the markdown update to finish in the original request. This is useful for high block-count markdown updates, especially `replace_content` requests and large batches of `update_content` operations.

Set `markdown_version: "v2"` at the top level of the request body to write and read [Notion-flavored Markdown](/guides/data-apis/notion-flavored-markdown) instead of enhanced markdown. This is an opt-in preview; `v1` is the default. A synchronous `v2` response can include a `warnings` array when the parser changed or ignored part of your content. Async updates (`allow_async: true`) don't return warnings. See [Markdown versions](/guides/data-apis/working-with-markdown-content#markdown-versions).

If `allow_async` is omitted or `false`, this endpoint keeps its existing synchronous response behavior. `allow_async` changes response behavior only; it does not change validation, permissions, or which operation runs. See [Retrieve an async task](/reference/retrieve-async-task) and [Working with markdown content](/guides/data-apis/working-with-markdown-content#running-large-markdown-writes-asynchronously) for polling examples.

<Info>
  **Requirements**

  Your connection must have [update content capabilities](/reference/capabilities#content-capabilities) on the target page in order to call this endpoint. To update your connection's capabilities, navigate to the <a href={developerConnectionsUrl}>Developer portal</a>, select your connection, open the **Configuration** tab, and scroll to the Capabilities section.

  Attempting to call this endpoint without update content capabilities returns an HTTP response with a 403 status code.
</Info>

<Tip>
  **Newlines in content**

  The `content` field expects markdown in the request's `markdown_version` syntax (enhanced markdown by default) with actual newline characters. In JSON, `\n` is the escape sequence for a newline — for example, `"## Heading\n\nParagraph"` creates a heading followed by a paragraph.

  When using cURL, wrap the `--data` body in **single quotes** (`'...'`) so that `\n` is passed through to the JSON parser. Avoid `$'...'` quoting, which converts `\n` into a literal newline and produces invalid JSON.

  Note that the interactive API explorer on this page does not support multiline input. To test with newlines, use cURL, an SDK, or any HTTP client that sends properly encoded JSON.
</Tip>

<Warning>
  **Protecting child pages and databases**

  By default, this endpoint refuses to delete child pages or databases. If an operation would remove them, a `validation_error` is returned listing the affected items. Set `allow_deleting_content` to `true` in the command body (`replace_content_range`, `update_content`, or `replace_content`) to permit deletion.
</Warning>

### Errors

| Error code | Condition |
| - | - |
| `validation_error` | The `content_range` or `after` selection does not match any content in the page, or an `old_str` in `update_content` is not found. |
| `validation_error` | Both `insert_content.after` and `insert_content.position` are provided. Use only one insertion target. |
| `validation_error` | The operation would delete child pages or databases and `allow_deleting_content` is not `true`. |
| `validation_error` | An `old_str` in `update_content` matches multiple locations and `replace_all_matches` is not `true`. |
| `validation_error` | An `old_str` in `update_content` is an empty string. |
| `validation_error` | The provided ID is a database or non-page block. |
| `validation_error` | The target page is a synced page. Synced pages cannot be updated. |
| `validation_error` | The page content after the edit is too large or too heavily formatted to process in one call. The limit counts the whole page, not the edit, so retrying the same request fails the same way. Move some content into child pages or reduce the page size. |
| `validation_error` | The page is too large to load in full (about 20,000 records, most of them blocks), and the edit targets a block that wasn't loaded or would remove content that wasn't loaded. Retrying the same request fails the same way. Content that wasn't loaded appears as `<unknown>` tags in the page's markdown, so edit only content outside those tags. `additional_data.limit_kind` is `page_record_count`. |
| `object_not_found` | The page does not exist or the connection does not have access to it. |

*Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
