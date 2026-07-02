---
title: "Query a data source"
source: https://developers.notion.com/reference/query-a-data-source
path: reference/query-a-data-source
---

post /v1/data_sources/{data_source_id}/query

### Overview

Gets a list of [pages](/reference/page) contained in the data source, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

<Info>
  **Databases, data sources, and wikis**

  [Wiki](https://www.notion.so/help/wikis-and-verified-pages) data sources can contain either pages or databases as children. In all other cases, the children can only be pages.

  For wikis, instead of directly returning any [database](/reference/database) results, this API returns all [data sources](/reference/data-source) that are children of *that* database. Surfacing the data source instead of the direct database child helps make it easier to craft your next API request (for example, retrieving the data source or listing its children.)

  Another tip for wikis is to use the `result_type` filter of `"page"` or `"data_source"` if you're only looking for query results that are one of those two types instead of both.
</Info>

### Filtering

[**Filters**](/reference/filter-data-source-entries) are similar to the [filters provided in the Notion UI](https://www.notion.so/help/views-filters-and-sorts) where the set of filters and filter groups chained by "And" in the UI is equivalent to having each filter in the array of the compound `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.
Filters operate on data source properties and can be combined. If no filter is provided, non-archived pages in the data source are returned with pagination.

<Frame>
  <img />
</Frame>

```json Filter object expandable theme={null}
{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    },
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
  	}
  ]
}
```

In addition to chained filters, data sources can be queried with single filters.

```json JSON theme={null}
{
    "property": "Done",
    "checkbox": {
        "equals": true
   }
}
```

### Archived pages

By default, this endpoint returns non-archived pages. To query archived pages instead, set the top-level `is_archived` body parameter to `true`:

```json theme={null}
{
  "is_archived": true
}
```

Set `is_archived` to `false`, or omit it, to query non-archived pages. The archive selector is applied before property filters and sorts, so filters only match rows in the selected archive partition.

`is_archived` is separate from `in_trash`. Page objects include `is_archived` to indicate whether a page is archived, while `in_trash` indicates trash status and is used by page/block/data source update APIs. `in_trash` is not a supported query body parameter for this endpoint.

### Sorting

[**Sorts**](/reference/sort-data-source-entries) are similar to the [sorts provided in the Notion UI](https://notion.so/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#0eb303043b1742468e5aff2f3f670505). Sorts operate on database properties or page timestamps and can be combined. The order of the sorts in the request matter, with earlier sorts taking precedence over later ones.

Notion doesn't guarantee any particular sort order when no sort parameters are provided.

### Pagination limit

This endpoint supports paginating through up to **10,000 results** per query. If a data source contains more matching entries than this limit, pagination stops at the 10,000th result: `has_more` becomes `false`, and every response page served from the capped result includes a `request_status` marking the result as incomplete:

```json theme={null}
{
  "request_status": {
    "type": "incomplete",
    "incomplete_reason": "query_result_limit_reached"
  }
}
```

Check `request_status.type === "incomplete"` on every response page to know whether a query was cut off. Any page with that status means the whole query result was capped. The limit is per query (a query is defined by its filter and sort), not per data source.

For connections that need to process all pages in a large data source, we recommend:

* Reading every row past the limit by partitioning the query into `created_time` windows. See [Query large data sources](/guides/data-apis/query-large-data-sources) for the technique and a [runnable cookbook example](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/query-large-data-sources).
* Using [filters](/reference/filter-data-source-entries) to narrow the result set (e.g. filter by `last_edited_time` to fetch only recently changed pages).
* Setting up [connection webhooks](/reference/webhooks) for incremental sync instead of polling the full data source on a schedule.

<Warning>
  **Incremental sync via webhooks**

  If your connection polls this endpoint on a recurring schedule to detect changes, consider switching to [connection webhooks](/reference/webhooks) instead. Webhooks notify your connection of changes in real time, eliminating the need to paginate through the entire data source. This is faster, more efficient, and avoids hitting the pagination limit.
</Warning>

### Recommendations for performance

Use the `filter_properties` query parameter to filter only the properties of the data source schema you need from the response items. For example:

```bash theme={null}
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title
```

Multiple filter properties can be provided by chaining the `filter_properties` query param. For example:

```bash theme={null}
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title&filter_properties[]=status
```

This parameter accepts property IDs or property names. Property IDs can be determined with the [Retrieve a data source](/reference/retrieve-a-data-source) endpoint.

If you are using the [Notion JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` endpoint expects an array of strings. For example:

```typescript TypeScript theme={null}
notion.dataSources.query({
	data_source_id: id,
	filter_properties: ["title", "status"]
})
```

Using `filter_properties` can make a significant improvement to the speed of the API and size of the JSON objects in the results, especially for databases with lots of properties, some of which might be rollups, relations, or formulas. If you need additional properties from each returned page, you can make subsequent calls to the [Retrieve page property item](/changelog/retrieve-page-property-values) or [Retrieve a page](/reference/retrieve-a-page) APIs.

If you're still running into long query times with this API, other tips include:

* Using more specific filter conditions to reduce the result set, e.g. a more specific title query or a shorter time window.
* Dividing large data sources (ones with more than several dozen thousand pages) into multiple; e.g. splitting a "tasks" database into "Tasks" and "Bugs".
* Pruning data source schemas to remove any complex formulas, rollups, two-way relations, or other properties that are no longer in use.
* Setting up [connection webhooks](/reference/webhooks) to reduce the need for polling this API by instead automatically notifying your system of incremental workspace events.

For more information, visit our [help center article on optimizing database load times](https://www.notion.com/help/optimize-database-load-times-and-performance).

### Other important details and tips

<Info>
  **Permissions**

  Before a connection can query a data source, its parent database must be shared with the connection. Attempting to query a data source in a database that has not been shared will return an HTTP response with a 404 status code.

  To share a database with a connection, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the connection from the dropdown list.
</Info>

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

<Info>
  **To display the page titles of related pages rather than just the ID:**

  1. Add a rollup property to the data source which uses a formula to get the related page's title. This works well if you have access to [update](/reference/update-a-data-source) the data source's schema.
  2. Otherwise, [retrieve the individual related pages](/reference/retrieve-a-page) using each page ID.
</Info>

<Warning>
  **Formula and rollup limitations**

  * If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
  * Rollups and formulas that depend on multiple layers of relations may not return correct results.
  * Notion recommends individually [retrieving each page property item](/reference/retrieve-a-page-property) to get the most accurate result.
</Warning>

### Errors

Returns a 404 HTTP response if the data source doesn't exist, or if the connection doesn't have access to the data source.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

Returns a 503 HTTP response if the data source query is temporarily unavailable due to backend datastore timeouts. The response body includes an `additional_data` object with retry guidance:

```json 503 response example theme={null}
{
  "object": "error",
  "status": 503,
  "code": "service_unavailable",
  "message": "Public API data source query is temporarily unavailable due to backend datastore timeouts. Retry with exponential backoff; if retries continue to fail, reduce page_size or narrow filters/sorts.",
  "additional_data": {
    "endpoint_name": "public_queryDataSource",
    "notion_error_name": "PgPoolWaitConnectionTimeout",
    "retry_guidance": [
      "Use exponential backoff with jitter",
      "Reduce page_size",
      "Narrow query filters/sorts"
    ]
  }
}
```

<Danger>
  **Note**: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
</Danger>
