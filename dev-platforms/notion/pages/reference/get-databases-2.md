---
title: "Get databases"
source: https://developers.notion.com/reference/get-databases
path: reference/get-databases
---

get /v1/databases

<Danger>
  **Deprecated as of version 2025-09-03**

  This endpoint is deprecated and is only available on API version "2021-08-16" and earlier. Use the [Search API](/reference/post-search) instead. This endpoint will only return explicitly shared databases, while search will also return child pages. This endpoint's results cannot be filtered, while search can be used to match on page title.
</Danger>

List all [Databases](/reference/database) shared with the authenticated connection. The response may contain fewer than `page_size` of results.

<Info>
  **Database access**

  Connections can only access databases a user has shared with the connection.
</Info>

See [Pagination](/reference/pagination) for details about how to use a cursor to iterate through the list.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
