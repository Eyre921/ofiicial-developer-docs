---
title: "Create comment"
source: https://developers.notion.com/reference/create-a-comment
path: reference/create-a-comment
---

post /v1/comments
Creates a comment on a page, block, or existing discussion thread.

Returns a [comment object](/reference/comment-object) for the created comment.

Choose exactly one target for the new comment:

| Target                     | Body parameter    | Use when                                                                                      |
| -------------------------- | ----------------- | --------------------------------------------------------------------------------------------- |
| Page                       | `parent.page_id`  | Creating a comment on a page.                                                                 |
| Block                      | `parent.block_id` | Creating a comment attached to a specific block, such as a paragraph, heading, or to-do item. |
| Existing discussion thread | `discussion_id`   | Replying to an existing page, block, or selected-text discussion.                             |

The request body will differ slightly depending on which target is being used.

To add a new comment to a page or block, provide a `parent` object with a `page_id` or `block_id` in the body params. For example, this request creates a comment attached to a block:

```json theme={null}
{
  "parent": {
    "block_id": "d40e767c-d7af-4b18-a86d-55c61f1e39a4"
  },
  "rich_text": [
    {
      "text": {
        "content": "This comment is attached to a block."
      }
    }
  ]
}
```

To add a new comment to an existing discussion thread, provide a `discussion_id` string in the body params.

<Note>
  The public API can create comments attached to whole blocks with `parent.block_id`. It does not support creating a new discussion anchored to a selected range of text inside a block. To reply to an existing selected-text discussion, use `discussion_id`.
</Note>

**Exactly one of `parent.page_id`, `parent.block_id`, or `discussion_id` must be provided.**

### Comment body format

The comment body can be provided in one of two formats:

* **`rich_text`**: An array of [rich text objects](/reference/rich-text) that represent the content of the comment.
* **`markdown`**: A Markdown string. Comment Markdown supports inline formatting only (bold, italic, strikethrough, inline code, links), inline equations, and mentions. Block-level Markdown such as fenced code blocks, headings, lists, tables, and blockquotes does not render as structured blocks in comments.

Exactly one of `rich_text` or `markdown` must be provided. Providing both or neither will return a validation error.

To see additional examples of creating a [page](/guides/data-apis/working-with-comments#adding-a-comment-to-a-page), [inline](/guides/data-apis/working-with-comments#adding-an-inline-comment), or [discussion](/guides/data-apis/working-with-comments#responding-to-a-discussion-thread) comment and to learn more about comments in Notion, see the [Working with comments](/guides/data-apis/working-with-comments) guide.

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Info>
  **Reminder: Turn on connection comment capabilities**

  Connection capabilities for reading and inserting comments are off by default.

  This endpoint requires a connection to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code.

  For more information on connection capabilities, see the [capabilities guide](/reference/capabilities). To update your connection settings, visit the <a href={developerConnectionsUrl}>Developer portal</a>.
</Info>
