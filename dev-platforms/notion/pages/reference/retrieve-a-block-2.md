---
title: "Retrieve a block"
source: https://developers.notion.com/reference/retrieve-a-block
path: reference/retrieve-a-block
---

get /v1/blocks/{block_id}
Retrieves a [Block object](/reference/block) using the ID specified.

If the block returned contains the key `has_children: true`, use the [Retrieve block children](/reference/get-block-children) endpoint to get the list of children.

To retrieve page content for a specific page, use [Retrieve block children](/reference/get-block-children) and set the page ID as the `block_id`.

For more information, read the [Working with page content guide](/guides/data-apis/working-with-page-content#modeling-content-as-blocks).

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the block doesn't exist, or if the connection doesn't have access to the block.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
