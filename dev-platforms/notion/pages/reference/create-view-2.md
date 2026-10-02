---
title: "Create a view"
source: https://developers.notion.com/reference/create-view
path: reference/create-view
---

post /v1/views
Create a new view on a database or add a widget view to a dashboard.

For a successful request, the response is a [View](/reference/view) object.

Provide exactly one of the following to specify where the view is created:

* `database_id` — create a view directly on an existing database.
* `view_id` — add a widget view inside an existing dashboard view.
* `create_database` — create a new linked database block on a page and add the view to it.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have insert content and update content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the database or view doesn't exist, or if the connection doesn't have access.

Returns a 400 HTTP response if more than one of `database_id`, `view_id`, or `create_database` is provided, or if none is provided.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
