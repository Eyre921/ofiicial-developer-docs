---
title: "Create a view query"
source: https://developers.notion.com/reference/create-view-query
path: reference/create-view-query
---

post /v1/views/{view_id}/queries
Execute a view's query and return the first page of results.

Executes the view's filter and sort configuration against its data source, caches the full result set, and returns the first page of page references along with a `query_id` for [paginating through results](/reference/get-view-query-results).

Cached results expire after 15 minutes. Use the `expires_at` field to check when the cache will be invalidated.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Pagination limit

This endpoint caches up to **10,000 results** per query. If the view's filter and sort configuration matches more rows than this limit, the cache will be truncated and the response will include:

```json theme={null}
{
  "request_status": {
    "type": "incomplete",
    "incomplete_reason": "query_result_limit_reached"
  }
}
```

When `request_status.type` is `"incomplete"`, the `total_count` reflects only the truncated cache size (not the full matching row count), and subsequent [paginated requests](/reference/get-view-query-results) will stop once the cache is exhausted.

To work around this limit:

* Narrow the view's filter and sort configuration via [Update a view](/reference/update-a-view) (for example, filter by `last_edited_time` to only include recently changed rows).
* Set up [connection webhooks](/reference/webhooks) to detect changes in real time instead of polling this endpoint.

<Warning>
  **Incremental sync via webhooks**

  If your connection runs this endpoint on a recurring schedule to detect changes, consider switching to [connection webhooks](/reference/webhooks) for incremental sync. Webhooks notify your connection when rows change, removing the need to re-query the view and avoiding the pagination depth limit entirely.
</Warning>

### Errors

Returns a 404 HTTP response if the view doesn't exist, or if the connection doesn't have access.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
