---
title: "Introduction"
source: https://developers.notion.com/reference/intro
path: reference/intro
---

Find the base URL, headers, and data formats for Notion API requests.

Send requests over HTTPS to `https://api.notion.com`. To make your first request, follow the [API quickstart](/guides/get-started/quick-start).

## Conventions

For requests to pages, databases, and other workspace resources, send an `Authorization: Bearer` header with your token and a [`Notion-Version` header](/reference/versioning). The [authentication reference](/reference/authentication) lists the supported token types.

Most endpoints use JSON. Set `Content-Type: application/json` when you send a JSON body. [Sending a file](/reference/upload-file) uses multipart form data instead.

### JSON conventions

* The `object` field identifies a resource, such as a `page` or `user`.
* You can send page and database IDs with or without dashes.
* Property names use `snake_case`.
* Dates and timestamps use ISO 8601, such as `2026-03-11` or `2026-03-11T09:30:00.000Z`.
* To clear a [URL page property](/reference/page-property-values#url), send `null`.

## Code samples & SDKs

Use the [JavaScript SDK](https://github.com/makenotion/notion-sdk-js), curl, or any client that can send HTTPS requests. Each endpoint reference lists its parameters and response fields. See [status codes](/reference/status-codes) to interpret an error response.

## Pagination

For lists with more than one page, pass the response’s `next_cursor` as `start_cursor` in the next request. See the [pagination reference](/reference/pagination).

* [Request parameters](/reference/pagination#requests) and [response fields](/reference/pagination#responses)
* [Paginated endpoints](/reference/pagination#paginated-endpoints)
* [Examples in curl and JavaScript](/reference/pagination#example)
