---
title: "Search by title"
source: https://developers.notion.com/reference/post-search
path: reference/post-search
---

post /v1/search
Searches all parent or child pages and data_sources that have been shared with a connection.

Returns all [pages](/reference/page) or [data\_sources](/reference/data-source) , excluding duplicated linked databases, that have titles that include the `query` param. If no `query` param is provided, then the response contains all pages or data\_sources that have been shared with the connection. The results adhere to any limitations related to an [connection’s capabilities](/reference/capabilities).

To limit the request to search only pages or to search only data\_source, use the `filter` param.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  The Search endpoint supports pagination. To learn more about working with [paginated](/reference/intro#pagination) responses, see the pagination section of the Notion API Introduction.
</Info>

<Warning>
  To search a specific data\_source — not all sources shared with the connection — use the [Query a data\_source](/reference/query-a-data-source) endpoint instead.
</Warning>
