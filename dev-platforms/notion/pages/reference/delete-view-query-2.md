---
title: "Delete a view query"
source: https://developers.notion.com/reference/delete-view-query
path: reference/delete-view-query
---

delete /v1/views/{view_id}/queries/{query_id}
Delete a cached view query.

Deletes a cached view query. This is idempotent — it returns success even if the query doesn't exist or has already expired.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
