---
title: "Create comment"
source: https://developers.notion.com/reference/create-a-comment
path: reference/create-a-comment
---

post /v1/comments
Creates a comment in a page, block or existing discussion thread.

Returns a [comment object](/reference/comment-object) for the created comment.

There are three locations where a new comment can be added with the public API:

1. A page
2. A block
3. An existing discussion thread

The request body will differ slightly depending on which type of comment is being added with this endpoint.

To add a new comment to a page or block, a `parent` object with a `page_id` or `block_id` must be provided in the body params.

To add a new comment to an existing discussion thread, a `discussion_id` string must be provided in the body params. (Inline comments to start a new discussion thread cannot be created via the public API.)

***Either* the `parent.page_id` , `parent.block_id` *or* `discussion_id` parameter must be provided — ONLY one can be specified**.

### Comment body format

The comment body can be provided in one of two formats:

* **`rich_text`**: An array of [rich text objects](/reference/rich-text) that represent the content of the comment.
* **`markdown`**: A Markdown string. Comment Markdown supports inline formatting only (bold, italic, strikethrough, inline code, links), inline equations, and mentions. Block-level Markdown such as fenced code blocks, headings, lists, tables, and blockquotes does not render as structured blocks in comments.

Exactly one of `rich_text` or `markdown` must be provided. Providing both or neither will return a validation error.

To see additional examples of creating a [page](/guides/data-apis/working-with-comments#adding-a-comment-to-a-page) or [discussion](/guides/data-apis/working-with-comments#responding-to-a-discussion-thread) comment and to learn more about comments in Notion, see the [Working with comments](/guides/data-apis/working-with-comments) guide.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Reminder: Turn on connection comment capabilities**

  Connection capabilities for reading and inserting comments are off by default.

  This endpoint requires a connection to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code.

  For more information on connection capabilities, see the [capabilities guide](/reference/capabilities). To update your connection settings, visit the <a href={developerConnectionsUrl}>Developer portal</a>.
</Info>
