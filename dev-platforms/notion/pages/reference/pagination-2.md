---
title: "Pagination"
source: https://developers.notion.com/reference/pagination
path: reference/pagination
---

Read lists of results with cursor-based pagination in the Notion API.

A paginated endpoint returns part of a list at a time. Read `has_more` to tell whether another page is available. A page can contain fewer items than you requested even when more remain.

## Requests

| Parameter | Meaning |
| :- | :- |
| `start_cursor` | Omit it on the first request. For the next page, pass the previous response's `next_cursor` unchanged. |
| `page_size` | The maximum number of items to return in one response. Most list endpoints default to 100 and accept values from 1 to 100. |

For GET requests, pass these parameters in the query string. For [search](/reference/post-search) and [data source queries](/reference/query-a-data-source), pass them in the POST body. Keep the same filters and sort order between requests.

## Responses

| Field | Meaning |
| :- | :- |
| `results` | The items on this page of a standard list response. |
| `has_more` | `true` if another page of results is available. |
| `next_cursor` | The cursor for the next page, or `null` at the end of a standard list. |

A standard list has `object: "list"`. Its `type` identifies the kind of result. For [paginated page properties](/reference/property-item-object#paginated-values), the response also includes information about the property.

[List data source templates](/reference/list-data-source-templates) returns items in `templates`. When you [create a view query](/reference/create-view-query), use its `query_id` with [Get view query results](/reference/get-view-query-results) to read subsequent pages.

## Paginated endpoints

The endpoint reference gives the shape of each result. Common examples include [block children](/reference/get-block-children), [users](/reference/get-users), [comments](/reference/list-comments), [file uploads](/reference/list-file-uploads), [custom emojis](/reference/list-custom-emojis), and [views](/reference/list-views).

## Example

Set `NOTION_API_KEY` to your token and `NOTION_BLOCK_ID` to a page or block your token can read. The curl request requests up to two children. The JavaScript SDK example follows each cursor and prints one child ID at a time.

```bash curl theme={null}
curl --get "https://api.notion.com/v1/blocks/$NOTION_BLOCK_ID/children" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  --data-urlencode "page_size=2"
```

```javascript JavaScript SDK theme={null}
import { Client, iteratePaginatedAPI } from "@notionhq/client";

const notion = new Client({ auth: process.env.NOTION_API_KEY });
for await (const block of iteratePaginatedAPI(notion.blocks.children.list, {
  block_id: process.env.NOTION_BLOCK_ID,
  page_size: 2,
})) {
  console.log(block.id);
}
```

For a large data source, a single query can reach its result limit even when `has_more` is false. See [Query large data sources](/guides/data-apis/query-large-data-sources) to detect the limit and read the remaining rows.
