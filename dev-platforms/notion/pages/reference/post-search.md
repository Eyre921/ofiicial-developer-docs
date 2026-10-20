---
title: "Search by title"
source: https://developers.notion.com/reference/post-search
path: reference/post-search
---

post /v1/search
Searches all parent or child pages and data_sources that have been shared with a connection.

Returns all [pages](/reference/page) or [data\_sources](/reference/data-source) , excluding duplicated linked databases, that have titles that include the `query` param. If no `query` param is provided, then the response contains all pages or data\_sources that have been shared with the connection. The results adhere to any limitations related to an [connection’s capabilities](/reference/capabilities).

To limit the request to pages or data sources, use the `filter` parameter with `property: "object"` and a `value` of `"page"` or `"data_source"`.

To list content in the trash, set `filter.in_trash` to `true`. You can combine `in_trash` with the object filter or use it by itself.

### Return fewer page properties

Use the `filter_properties` query parameter to return only the page properties you need. It works the same way as on [Query a data source](/reference/query-a-data-source#recommendations-for-performance), with two differences. Search results come from many data sources, so if a name or ID doesn't exist on a page, search skips it for that page instead of returning an error. Data source results always include their full property schema.

```bash theme={null}
curl -X POST 'https://api.notion.com/v1/search?filter_properties=title&filter_properties=Status' \
  -H 'Authorization: Bearer ntn_...' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{"query": "Roadmap", "filter": {"property": "object", "value": "page"}}'
```

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

> [!NOTE]
>
> The Search endpoint supports pagination. To learn more about working with [paginated](/reference/intro#pagination) responses, see the pagination section of the Notion API Introduction.

> [!WARNING]
>
> To search a specific data\_source — not all sources shared with the connection — use the [Query a data\_source](/reference/query-a-data-source) endpoint instead.
