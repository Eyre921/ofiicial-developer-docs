---
title: "Delete comment"
source: https://developers.notion.com/reference/delete-a-comment
path: reference/delete-a-comment
---

delete /v1/comments/{comment_id}
Deletes a comment by its `comment_id`.

Returns a [comment object](/reference/comment-object) for the deleted comment.

A connection can only delete comments that it created. Attempting to delete a comment created by another user or connection will return a 404 error.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Reminder: Turn on connection comment capabilities**

  Connection capabilities for reading and inserting comments are off by default.

  This endpoint requires a connection to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code.

  For more information on connection capabilities, see the [capabilities guide](/reference/capabilities). To update your connection settings, visit the <a href={developerConnectionsUrl}>Developer portal</a>.
</Info>
