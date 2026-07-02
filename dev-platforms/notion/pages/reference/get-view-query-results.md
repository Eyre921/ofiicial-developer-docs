---
title: "Get view query results"
source: https://developers.notion.com/reference/get-view-query-results
path: reference/get-view-query-results
---

get /v1/views/{view_id}/queries/{query_id}
Paginate through cached view query results.

Returns a page of results from a previously [created view query](/reference/create-view-query). Use `start_cursor` and `page_size` to paginate through the cached result set.

Cached results expire after 15 minutes from the time the query was created. If the cache has expired, this endpoint returns a 404.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Truncated queries

If the underlying [view query](/reference/create-view-query) matched more rows than the server-side pagination limit, the response will include a `request_status` field:

```json theme={null}
{
  "object": "list",
  "type": "page",
  "results": [...],
  "next_cursor": null,
  "has_more": false,
  "request_status": {
    "type": "incomplete",
    "incomplete_reason": "query_result_limit_reached"
  }
}
```

The `request_status` field is surfaced on every page of paginated results for a truncated query, so your connection can detect it regardless of which page it is on. When this field is present, there are additional rows matching the view's configuration that are not returned.

See [Create a view query](/reference/create-view-query) for guidance on working around the pagination limit (narrower view filters, [connection webhooks](/reference/webhooks)).

### Errors

Returns a 404 HTTP response if the query doesn't exist, has expired, or the `view_id` doesn't match.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
