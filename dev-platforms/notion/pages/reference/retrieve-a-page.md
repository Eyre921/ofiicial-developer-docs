---
title: "Retrieve a page"
source: https://developers.notion.com/reference/retrieve-a-page
path: reference/retrieve-a-page
---

get /v1/pages/{page_id}

Retrieves a [page object](/reference/page) by ID. The response includes [page property values](/reference/page-property-values). To read the page’s content, use [Retrieve block children](/reference/get-block-children).

<span />

## Parent and properties

For a page in a data source, the property values follow that [data source’s schema](/reference/property-object). For a page whose parent is another page, the only property is `title`.

## Limits

A page response can omit values when a property refers to many pages or people:

| Property             | Page response limit                                                                                  |
| :------------------- | :--------------------------------------------------------------------------------------------------- |
| `relation`           | Up to 25 page references. `has_more: true` means more references exist.                              |
| `people`             | More than 25 people may be omitted.                                                                  |
| `title`, `rich_text` | Up to 25 populated inline page or person mentions. This is a mention limit, not a text-length limit. |
| `formula`, `rollup`  | Results can depend on references that the page response does not fully load.                         |

Use [Retrieve a page property item](/reference/retrieve-a-page-property) when you need the full value. Read every [page of property items](/reference/property-item-object#paginated-values). Formula and rollup [calculation limits](/reference/page-property-values#unsupported-formula) still apply.

## Errors

The connection needs [read content capabilities](/reference/capabilities). Missing capabilities return `403`. A missing page or missing access returns `404`.

Requests can also fail with a [validation or rate-limit error](/reference/status-codes#error-codes). See [Request limits](/reference/request-limits).
