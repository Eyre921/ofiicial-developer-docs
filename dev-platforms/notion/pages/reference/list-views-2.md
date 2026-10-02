---
title: "List views"
source: https://developers.notion.com/reference/list-views
path: reference/list-views
---

get /v1/views
List all views in a database.

Returns a paginated list of [View](/reference/view) references for the specified database.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the database doesn't exist, or if the connection doesn't have access.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
