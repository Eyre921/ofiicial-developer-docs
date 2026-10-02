---
title: "Update a view"
source: https://developers.notion.com/reference/update-a-view
path: reference/update-a-view
---

patch /v1/views/{view_id}
Update a view's name, filter, sorts, or configuration.

For a successful request, the response is the updated [View](/reference/view) object.

All body parameters are optional. Only the provided fields are updated; omitted fields are left unchanged. To clear a field, pass `null`.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have update content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the view doesn't exist, or if the connection doesn't have access.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
