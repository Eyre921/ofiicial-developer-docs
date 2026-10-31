---
title: "Search by title"
source: https://developers.notion.com/reference/post-search
path: reference/post-search
---

post /v1/search
Find pages and data sources by title.

Search returns [pages](/reference/page) and [data sources](/reference/data-source) that the connection can access. Omit `query` to search without a title filter. Search excludes duplicate linked databases. See [search limitations](/reference/search-optimizations-and-limitations#limitations) before using the results as an inventory.

To limit the request to pages or data sources, use the `filter` parameter with `property: "object"` and a `value` of `"page"` or `"data_source"`.

To list content in the trash, set `filter.in_trash` to `true`. You can combine `in_trash` with the object filter or use it by itself.

Results use [cursor-based pagination](/reference/pagination). To filter rows in one data source, use [Query a data source](/reference/query-a-data-source).

### Return fewer page properties

Use the `filter_properties` query parameter to return only the page properties you need. It works the same way as on [Query a data source](/reference/query-a-data-source#recommendations-for-performance), with two differences. Search results come from many data sources, so if a name or ID doesn't exist on a page, search skips it for that page instead of returning an error. Data source results always include their full property schema.

```bash theme={null}
curl -X POST 'https://api.notion.com/v1/search?filter_properties=title&filter_properties=Status' \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{"query": "Roadmap", "filter": {"property": "object", "value": "page"}}'
```

### Errors

See [status codes](/reference/status-codes#error-codes) for error responses.
