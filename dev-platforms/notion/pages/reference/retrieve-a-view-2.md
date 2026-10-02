---
title: "Retrieve a view"
source: https://developers.notion.com/reference/retrieve-a-view
path: reference/retrieve-a-view
---

get /v1/views/{view_id}
Retrieve a view by its ID.

For a successful request, the response is a [View](/reference/view) object.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the view doesn't exist, or if the connection doesn't have access.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
