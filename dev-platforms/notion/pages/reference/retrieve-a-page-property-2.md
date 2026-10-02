---
title: "Retrieve a page property item"
source: https://developers.notion.com/reference/retrieve-a-page-property
path: reference/retrieve-a-page-property
---

get /v1/pages/{page_id}/properties/{property_id}

Retrieves one property on a page. The response is a [property item or paginated list](/reference/property-item-object), depending on the type.

Get the property ID from [Retrieve a page](/reference/retrieve-a-page) or [Retrieve a data source](/reference/retrieve-a-data-source). Pass URL-encoded IDs as returned by the API.

## Property item objects

### Simple properties

Most types return one `property_item` object. This includes `status`, `select`, `files`, and `multi_select`. See [Response shape by type](/reference/property-item-object#response-shape-by-type).

### Paginated properties

`title`, `rich_text`, `people`, and `relation` return a paginated list. Use this endpoint when a page response omits references. Continue with `next_cursor` until `has_more` is `false`. The next URL is nested at `property_item.next_url`.

See [Pagination fields and examples](/reference/property-item-object#paginated-values) or [Read every item in a page property](/guides/data-apis/read-page-property-values).

### Rollup properties

Rollups return a list with calculation metadata at `property_item.rollup`. Read every page before using a calculated result. See [Rollup response rules and limits](/reference/property-item-object#rollup).

### Errors

The connection needs [read content capabilities](/reference/capabilities). Missing capabilities return `403`. A missing page or property, or missing access to the page, returns `404`.

Requests can also fail with a [validation or rate-limit error](/reference/status-codes#error-codes). See [Request limits](/reference/request-limits).
