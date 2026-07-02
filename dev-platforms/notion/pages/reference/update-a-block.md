---
title: "Update a block"
source: https://developers.notion.com/reference/update-a-block
path: reference/update-a-block
---

patch /v1/blocks/{block_id}

Updates the content for the specified `block_id` based on the block type. Supported fields based on the block object type (see [Block object](/reference/block#block-type-objects) for available fields and the expected input for each field).

**Note**: The update replaces the *entire* value for a given field. If a field is omitted (ex: omitting `checked` when updating a `to_do` block), the value will not be changed.

<Info>
  **Updating `child_page` blocks**

  To update `child_page` type blocks, use the [Update page](/reference/patch-page) endpoint. Updating the page's `title` updates the text displayed in the associated `child_page` block.
</Info>

<Info>
  **Updating `child_database` blocks**

  To update `child_database` type blocks, use the [Update database](/reference/update-a-database) endpoint. Updating the page's `title` updates the text displayed in the associated `child_database` block.
</Info>

<Info>
  **Updating `children`**

  A block's children *CANNOT* be directly updated with this endpoint. Instead use [Append block children](/reference/patch-block-children) to add children.
</Info>

### Success

Returns a 200 HTTP response containing the updated [block object](/reference/block) on success.

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have update content capabilities. Attempting to call this API without update content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the block doesn't exist, is in the trash, or if the connection doesn't have access to the page.

Returns a 400 if the `type` for the block is incorrect or the input is incorrect for a given field.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
