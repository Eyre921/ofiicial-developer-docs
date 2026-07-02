---
title: "Append block children"
source: https://developers.notion.com/reference/patch-block-children
path: reference/patch-block-children
---

patch /v1/blocks/{block_id}/children
Creates and appends new children blocks to the parent `block_id` specified. Blocks can be parented by other blocks, pages, or databases.

Returns a paginated list of newly created first level children [block objects](/reference/block).

Existing blocks cannot be moved using this endpoint. Once a block is appended as a child, it can't be moved elsewhere via the API.

For blocks that allow children, we allow up to **two** levels of nesting in a single request.

There is a limit of **100 block children** that can be appended by a single API request. Arrays of block children longer than 100 will result in an error.

### Controlling insert position

By default, blocks are appended to the end of the parent block's children. Use the `position` parameter to insert blocks at a specific location:

| Position type                                                      | Description                                                   |
| ------------------------------------------------------------------ | ------------------------------------------------------------- |
| `{ "type": "end" }`                                                | Insert at the end of the parent's children (default behavior) |
| `{ "type": "start" }`                                              | Insert at the beginning of the parent's children              |
| `{ "type": "after_block", "after_block": { "id": "<block_id>" } }` | Insert after the specified block                              |

<CodeGroup>
  ```json Insert at start theme={null}
  {
    "children": [/* blocks */],
    "position": { "type": "start" }
  }
  ```

  ```json Insert after specific block theme={null}
  {
    "children": [/* blocks */],
    "position": {
      "type": "after_block",
      "after_block": { "id": "12345678-1234-1234-1234-123456789abc" }
    }
  }
  ```
</CodeGroup>

<Warning>
  **Deprecated parameter**

  The `after` parameter is deprecated. Use the `position` parameter instead, which provides more flexibility including inserting at the start of the children list.

  If you're currently using `after`, migrate to `position` with type `after_block`:

  * **Before:** `{ "children": [...], "after": "<block_id>" }`
  * **After:** `{ "children": [...], "position": { "type": "after_block", "after_block": { "id": "<block_id>" } } }`

  You cannot specify both `after` and `position` in the same request.
</Warning>

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 HTTP response if the block specified by `id` doesn't exist, or if the connection doesn't have access to the block.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. To see a full description of each type of error code, see the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation.*
