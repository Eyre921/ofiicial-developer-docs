---
title: "Retrieve a page property item"
source: https://developers.notion.com/reference/retrieve-a-page-property
path: reference/retrieve-a-page-property
---

get /v1/pages/{page_id}/properties/{property_id}

Retrieves a `property_item` object for a given `page_id` and `property_id`. Depending on the property type, the object returned will either be a value or a [paginated](/reference/pagination) list of property item values. See [Property item objects](/reference/property-item-object) for specifics.

To obtain `property_id`s, use the [Retrieve a database](/reference/retrieve-a-database) endpoint.

In cases where a property item has more than 25 references, this endpoint should be used, rather than [Retrieve a page](/reference/retrieve-a-page). ([Retrieve a page](/reference/retrieve-a-page) will not return a complete list when the list exceeds 25 references.)

## Property Item Objects

For more detailed information refer to the [Property item object documentation](/reference/property-item-object)

### Simple Properties

Each individual `property_item` properties will have a `type` and under the the key with the value for `type`, an object that identifies the property value, documented under [Page property values](/reference/page-property-values).

### Paginated Properties

Property types that return a paginated list of property item objects are:

* `title`
* `rich_text`
* `relation`
* `people`

Look for the `next_url` value in the response object for these property items to view paginated results. Refer to [paginated page properties](/reference/page-property-values#paginated-page-properties) for a full description of the response object for these properties.

Refer to the [pagination reference](/reference/intro#pagination) for details on how to iterate through a results list.

### Rollup Properties

<Check>
  Learn more about rollup properties on the [Page properties page](/reference/page-property-values#rollup) or in Notion’s [Help Center](https://www.notion.so/help/relations-and-rollups).
</Check>

For regular "Show original" rollups, the endpoint returns a flattened list of all the property items in the rollup.

For rollups with an aggregation, the API returns a [rollup property value](/reference/page#rollup-property-values) under the `rollup` key and the list of relations.

In order to avoid timeouts, if the rollup has a with a large number of aggregations or properties the endpoint returns a `next_cursor` value that is used to determinate the aggregation value *so far* for the subset of relations that have been paginated through.

Once `has_more` is `false`, then the final rollup value is returned. Refer to the [Pagination documentation](/reference/pagination) for more information on pagination in the Notion API.

Computing the values of following aggregations are *not* supported. Instead the endpoint returns a list of `property_item` objects for the rollup:

* `show_unique` (Show unique values)
* `unique` (Count unique values)
* `median`(Median)

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the page or property doesn't exist, or if the connection doesn't have access to the page.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
