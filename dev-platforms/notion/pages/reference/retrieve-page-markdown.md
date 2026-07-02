---
title: "Retrieve a page as markdown"
source: https://developers.notion.com/reference/retrieve-page-markdown
path: reference/retrieve-page-markdown
---

get /v1/pages/{page_id}/markdown
Retrieve the content of a page rendered as enhanced markdown.

### Use cases

Use this endpoint to retrieve the full content of a Notion page as [enhanced markdown](/guides/data-apis/enhanced-markdown), instead of working with the [block-based API](/reference/get-block-children). This is especially useful for agentic systems and developer tools that work natively with markdown.

The endpoint also accepts non-navigable block IDs returned in `unknown_block_ids` from a previous truncated response. Pass these IDs to fetch additional subtrees of a large page.

### General behavior

Returns a `page_markdown` object containing the page content as an enhanced markdown string.

<Info>
  **Requirements**

  Your connection must have [read content capabilities](/reference/capabilities#content-capabilities) on the target page in order to call this endpoint. To update your connection's capabilities, navigate to the <a href={developerConnectionsUrl}>Developer portal</a>, select your connection, open the **Configuration** tab, and scroll to the Capabilities section.

  Attempting to call this endpoint without read content capabilities returns an HTTP response with a 403 status code.
</Info>

### Unknown blocks

Some blocks may appear as `<unknown url="..." alt="..."/>` tags in the markdown output. This happens when:

* **Truncation**: The page exceeds the record limit (approximately 20,000 blocks) and some blocks could not be loaded.
* **Permissions**: The page contains child pages or other content that is not shared with the connection.
* **Unsupported block types**: Certain block types (such as bookmarks, embeds, and link previews) are [not yet supported](/guides/data-apis/working-with-markdown-content#unsupported-block-types) in the markdown format.

When truncation or permissions cause unknown blocks, the `truncated` field is set to `true` and the `unknown_block_ids` array contains the affected block IDs.

You can attempt to fetch unloaded blocks by passing their IDs back to this same endpoint as the `page_id` path parameter. Blocks that are unknown due to permissions will return a 404 error since the connection does not have access.

<Note>
  The `unknown_block_ids` array does not distinguish between truncated and inaccessible blocks. Handle `object_not_found` errors gracefully when re-fetching unknown block IDs.
</Note>

For unsupported block types, use the [block-based API](/reference/retrieve-a-block) to retrieve the full structured data.

### Errors

Returns a 404 HTTP response if the page doesn't exist, or if the connection doesn't have access to the page.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
