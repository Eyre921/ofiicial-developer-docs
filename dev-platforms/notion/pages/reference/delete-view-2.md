---
title: "Delete a view"
source: https://developers.notion.com/reference/delete-view
path: reference/delete-view
---

delete /v1/views/{view_id}
Delete a view from a database.

Deletes the specified view. The last remaining view on a database cannot be deleted — delete the database instead.

For dashboard views, deleting the dashboard also archives all of its widget views.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have update content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the view doesn't exist, or if the connection doesn't have access.

Returns a 400 HTTP response if the view is the last view on the database.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
