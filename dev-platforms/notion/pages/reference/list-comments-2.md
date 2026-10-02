---
title: "List comments"
source: https://developers.notion.com/reference/list-comments
path: reference/list-comments
---

get /v1/comments
Retrieves a list of un-resolved [Comment objects](/reference/comment-object) from a page or block.

See [Pagination](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Reminder: Turn on connection comment capabilities**

  Connection capabilities for reading and inserting comments are off by default.

  This endpoint requires a connection to have read comment capabilities. Attempting to call this endpoint without read comment capabilities will return an HTTP response with a 403 status code.

  For more information on connection capabilities, see the [capabilities guide](/reference/capabilities). To update your connection settings, visit the <a href={developerConnectionsUrl}>Developer portal</a>.
</Info>
