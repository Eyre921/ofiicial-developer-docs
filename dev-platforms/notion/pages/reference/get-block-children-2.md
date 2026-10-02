---
title: "Retrieve block children"
source: https://developers.notion.com/reference/get-block-children
path: reference/get-block-children
---

get /v1/blocks/{block_id}/children
Returns a paginated array of child [block objects](/reference/block) contained in the block using the ID specified. In order to receive a complete representation of a block, you may need to recursively retrieve the block children of child blocks.

<Check>
  Page content is represented by block children. See the [Working with page content guide](/guides/data-apis/working-with-page-content#modeling-content-as-blocks) for more information.
</Check>

Returns only the first level of children for the specified block. See [block objects](/reference/block) for more detail on determining if that block has nested children.

The response may contain fewer than `page_size` of results.

See [Pagination](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the block specified by `id` doesn't exist, or if the connection doesn't have access to the block.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
