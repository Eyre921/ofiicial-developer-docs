---
title: "Retrieve a page"
source: https://developers.notion.com/reference/retrieve-a-page
path: reference/retrieve-a-page
---

get /v1/pages/{page_id}

<Warning>
  **This endpoint will not accurately return properties that exceed 25 references**

  Do **not** use this endpoint if a page property includes more than 25 references to receive the full list of references. Instead, use the [Retrieve a page property endpoint](/reference/retrieve-a-page-property) for the specific property to get its complete reference list.
</Warning>

Retrieves a [Page object](/reference/page) using the ID specified.

Responses contains page **properties**, not page content. To fetch page content, use the [Retrieve block children](/reference/get-block-children) endpoint.

Page properties are limited to up to **25 references** per page property. To retrieve data related to properties that have more than 25 references, use the [Retrieve a page property](/reference/retrieve-a-page-property#rollup-properties) endpoint. (See [Limits](/reference/retrieve-a-page#limits) below for additional information.)

### Parent objects: Pages vs. databases

If a page’s [Parent object](/reference/parent-object) is a database, then the property values will conform to the [database property schema](/reference/property-object).

If a page object is not part of a database, then the only property value available for that page is its `title`.

### Limits

The endpoint returns a maximum of 25 page or person references per [page property](/reference/page-property-values). If a page property includes more than 25 references, then the 26th reference and beyond might be returned as `Untitled`, `Anonymous`, or not be returned at all.

This limit affects the following properties:

* [`people`](/reference/page-property-values#people): response object can’t be guaranteed to return more than 25 people.
* [`relation`](/reference/page-property-values#relation): the `has_more` value of the `relation` in the response object is `true` if a `relation` contains more than 25 related pages. Otherwise, `has_more` is false.
* [`rich_text`](/reference/page-property-values#rich-text): response object includes a maximum of 25 populated inline page or person mentions.
* [`title`](/reference/page-property-values#title): response object includes a maximum of 25 inline page or person mentions.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the page doesn't exist, or if the connection doesn't have access to the page.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
