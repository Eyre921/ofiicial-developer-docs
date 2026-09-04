---
title: "Update comment"
source: https://developers.notion.com/reference/update-a-comment
path: reference/update-a-comment
---

patch /v1/comments/{comment_id}
Updates a comment by its `comment_id`.

Returns a [comment object](/reference/comment-object) for the updated comment.

A connection can only update comments that it created. Attempting to update a comment created by another user or connection will return a 404 error.

### Comment body format

The comment body can be provided in one of two formats:

* **`rich_text`**: An array of [rich text objects](/reference/rich-text) that represent the updated content of the comment.
* **`markdown`**: A Markdown string. Supports inline formatting (bold, italic, strikethrough, inline code, links), inline equations, and mentions.

Exactly one of `rich_text` or `markdown` must be provided. Providing both or neither will return a validation error.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Reminder: Turn on connection comment capabilities**

  Connection capabilities for reading and inserting comments are off by default.

  This endpoint requires a connection to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code.

  For more information on connection capabilities, see the [capabilities guide](/reference/capabilities). To update your connection settings, visit the <a href={developerConnectionsUrl}>Developer portal</a>.
</Info>
