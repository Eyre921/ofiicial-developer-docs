---
title: "Working with markdown content"
source: https://developers.notion.com/guides/data-apis/working-with-markdown-content
path: guides/data-apis/working-with-markdown-content
---

Learn how to create, read, and update Notion page content using enhanced markdown instead of the block API.

## Overview

The Notion API supports reading, writing, and updating page content using **enhanced markdown** (also called "Notion-flavored Markdown") as an alternative to the [block-based API](/guides/data-apis/working-with-page-content). This is especially useful for agentic systems and developer tools that work natively with markdown.

Three API surfaces are available:

| Operation | Endpoint                            | Description                                                     |
| --------- | ----------------------------------- | --------------------------------------------------------------- |
| Create    | `POST /v1/pages`                    | Create a page with markdown content (via `markdown` body param) |
| Read      | `GET /v1/pages/:page_id/markdown`   | Retrieve a page's full content as markdown                      |
| Update    | `PATCH /v1/pages/:page_id/markdown` | Insert or replace content using markdown                        |

<Tip>
  All three endpoints use the same **enhanced markdown** format. See the [Enhanced markdown format reference](/guides/data-apis/enhanced-markdown) for the full specification.
</Tip>

## Block type support

The markdown API supports most Notion block types. The table below shows how each block type maps to its markdown representation.

### Supported block types

| Block type                                                      | Markdown format                                                        |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Paragraph](/reference/block#paragraph)                         | Plain text                                                             |
| [Heading 1 / 2 / 3 / 4](/reference/block#headings)              | `#` / `##` / `###` / `####`                                            |
| [Bulleted list item](/reference/block#bulleted-list-item)       | `- item`                                                               |
| [Numbered list item](/reference/block#numbered-list-item)       | `1. item`                                                              |
| [To do](/reference/block#to-do)                                 | `- [ ]` / `- [x]`                                                      |
| [Toggle](/reference/block#toggle-blocks)                        | `<details>` / `<summary>`                                              |
| [Quote](/reference/block#quote)                                 | `> quote`                                                              |
| [Callout](/reference/block#callout)                             | `<callout>`                                                            |
| [Divider](/reference/block#divider)                             | `---`                                                                  |
| [Code](/reference/block#code)                                   | Fenced code block with language                                        |
| [Equation](/reference/block#equation)                           | `$$ equation $$`                                                       |
| [Table](/reference/block#table)                                 | `<table>` with `<tr>` and `<td>`                                       |
| [Image](/reference/block#image)                                 | `![caption](url)`                                                      |
| [File](/reference/block#file)                                   | `<file src="url">caption</file>`                                       |
| [Video](/reference/block#video)                                 | `<video src="url">caption</video>`                                     |
| [Audio](/reference/block#audio)                                 | `<audio src="url">caption</audio>`                                     |
| [PDF](/reference/block#pdf)                                     | `<pdf src="url">caption</pdf>`                                         |
| [Child page](/reference/block#child-page)                       | `<page url="...">title</page>`                                         |
| [Child database](/reference/block#child-database)               | `<database url="...">title</database>`                                 |
| [Synced block](/reference/block#synced-block)                   | `<synced_block>` with content                                          |
| [Column list / Column](/reference/block#column-list-and-column) | `<columns>` / `<column>`                                               |
| [Table of contents](/reference/block#table-of-contents)         | `<table_of_contents/>`                                                 |
| [Transcription](/reference/block#transcription)                 | `<meeting-notes>` (transcript included when `include_transcript=true`) |

For file-based blocks (image, file, video, audio, PDF), the URLs in the markdown output are pre-signed and ready to download. They expire after a short period, consistent with the [block-based API](/reference/block#file).

### Unsupported block types

The following block types are not yet rendered in the markdown output. When encountered, they appear as `<unknown url="..." alt="block_type"/>` tags. The `url` links to the block in Notion, and `alt` indicates the original block type.

| Block type                                    | Notes                           |
| --------------------------------------------- | ------------------------------- |
| [Bookmark](/reference/block#bookmark)         | Web bookmarks with URL previews |
| [Embed](/reference/block#embed)               | Embedded third-party content    |
| [Link preview](/reference/block#link-preview) | Unfurled URL previews           |
| [Breadcrumb](/reference/block#breadcrumb)     | Navigation breadcrumbs          |
| [Template](/reference/block#template)         | Template buttons (deprecated)   |

Block types that are not recognized by the block API (returned as `"unsupported"`) will also appear as `<unknown>` in the markdown output.

<Tip>
  You can use the [block-based API](/reference/block) to retrieve structured data for any unsupported block types you encounter in the markdown output.
</Tip>

## Creating a page with markdown

Use `POST /v1/pages` with the `markdown` parameter instead of `children` to create a page from a markdown string.

<Tip>
  The `markdown` field expects actual newline characters. In JSON, use `\n` to encode them — for example, `"# Heading\nParagraph"`. To create a line break inside a single paragraph block, use `<br>`. When using cURL, wrap the `--data` body in **single quotes** so that `\n` is preserved for the JSON parser.
</Tip>

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.notion.com/v1/pages \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "parent": { "page_id": "YOUR_PAGE_ID" },
      "markdown": "# Meeting Notes\nDiscussed roadmap priorities.\n## Action items\n- [ ] Draft proposal\n- [ ] Schedule follow-up"
    }'
  ```

  ```javascript JavaScript theme={null}
  const { Client } = require("@notionhq/client");
  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  const response = await notion.pages.create({
    parent: { page_id: "YOUR_PAGE_ID" },
    markdown: "# Meeting Notes\nDiscussed roadmap priorities.\n## Action items\n- [ ] Draft proposal\n- [ ] Schedule follow-up",
  });
  ```
</CodeGroup>

**Key behaviors:**

* The `markdown` parameter is mutually exclusive with `children` and `content`. You cannot use both.
* If `properties.title` is omitted, the first `# h1` heading is extracted as the page title.
* Available to all connection types (public, internal, and personal access tokens).
* Requires `insert_content` and `insert_property` capabilities.

The response is a standard [page object](/reference/page).

## Retrieving a page as markdown

Use `GET /v1/pages/:page_id/markdown` to retrieve a page's content rendered as enhanced markdown.

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.pages.retrieveMarkdown({
    page_id: "YOUR_PAGE_ID",
  });

  console.log(response.markdown);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "object": "page_markdown",
  "id": "page-uuid",
  "markdown": "# Meeting Notes\nDiscussed roadmap priorities.\n## Action items\n- [ ] Draft proposal\n- [ ] Schedule follow-up",
  "truncated": false,
  "unknown_block_ids": []
}
```

Retrieved markdown uses a single newline (`\n`) between adjacent top-level blocks. Line breaks inside a single block are represented as `<br>`.

### Query parameters

| Parameter            | Type    | Description                                          |
| -------------------- | ------- | ---------------------------------------------------- |
| `include_transcript` | boolean | Include meeting note transcripts (default: `false`). |

<CodeGroup>
  ```bash cURL (with transcript) theme={null}
  curl 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown?include_transcript=true' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.pages.retrieveMarkdown({
    page_id: "YOUR_PAGE_ID",
    include_transcript: true,
  });
  ```
</CodeGroup>

**Key behaviors:**

* Available to all connection types (public, internal, and personal access tokens).
* Requires `read_content` capability.
* File URIs in the content are automatically converted to pre-signed URLs.

### Unknown blocks, truncation, and permissions

Some blocks in a page may appear as `<unknown>` tags in the markdown output. This can happen for two reasons:

1. **Truncation** — the page exceeds the record limit (approximately 20,000 blocks) and some blocks were not loaded.
2. **Permissions** — the page contains child pages or other content that is not shared with the connection. The connection can access the parent page, but not those specific child blocks.

In both cases:

* The `truncated` field is set to `true`.
* The affected blocks appear as `<unknown url="..." alt="..."/>` tags in the markdown.
* The `unknown_block_ids` array contains the IDs of these blocks.

```json theme={null}
{
  "object": "page_markdown",
  "id": "page-uuid",
  "markdown": "# Large Document\nFirst section content...\n<unknown url=\"https://notion.com/abc123#def456\"/>",
  "truncated": true,
  "unknown_block_ids": ["def456-with-dashes-uuid"]
}
```

You can attempt to fetch the content of unknown blocks by passing their IDs back to the same endpoint:

<CodeGroup>
  ```bash cURL (fetching an unknown block) theme={null}
  curl 'https://api.notion.com/v1/pages/UNKNOWN_BLOCK_ID/markdown' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const blockResp = await notion.pages.retrieveMarkdown({
    page_id: "UNKNOWN_BLOCK_ID",
  });
  ```
</CodeGroup>

For blocks that were unknown due to truncation, this returns the subtree rooted at that block. For blocks that are unknown due to permissions, the request returns an `object_not_found` error — the connection does not have access to that content.

<Note>
  The `unknown_block_ids` array does not distinguish between truncated and inaccessible blocks. When re-fetching unknown block IDs, handle `object_not_found` errors gracefully as they indicate blocks the connection cannot access.
</Note>

<Tip>
  For the best experience, keep pages under a few thousand blocks. Very large pages may require multiple requests to fully retrieve.
</Tip>

**Example: iteratively fetching a large page**

<CodeGroup>
  ```python Python theme={null}
  import requests

  headers = {
      "Authorization": f"Bearer {NOTION_API_KEY}",
      "Notion-Version": "2026-03-11",
  }

  resp = requests.get(
      f"https://api.notion.com/v1/pages/{page_id}/markdown",
      headers=headers,
  ).json()

  all_markdown = resp["markdown"]

  for block_id in resp.get("unknown_block_ids", []):
      block_resp = requests.get(
          f"https://api.notion.com/v1/pages/{block_id}/markdown",
          headers=headers,
      ).json()
      all_markdown += "\n" + block_resp["markdown"]
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.pages.retrieveMarkdown({
    page_id: "YOUR_PAGE_ID",
  });

  let allMarkdown = response.markdown;

  for (const blockId of response.unknown_block_ids) {
    const blockResp = await notion.pages.retrieveMarkdown({
      page_id: blockId,
    });
    allMarkdown += "\n" + blockResp.markdown;
  }
  ```
</CodeGroup>

## Updating a page with markdown

Use `PATCH /v1/pages/:page_id/markdown` to insert or replace content in an existing page using markdown.

The request body uses a **discriminated union** with four command variants. We recommend `update_content` and `replace_content` for new connections — they offer more precise control and better performance than the older `insert_content` and `replace_content_range` commands.

<Tip>
  The `content` field expects enhanced markdown with actual newline characters. In your JSON request body, use `\n` to encode newlines — for example, `"## Heading\nParagraph text"` creates a heading followed by a paragraph block. To create a line break inside a single paragraph block, use `<br>`. Literal backslash-n sequences (like typing `\n` into a form field) will not be interpreted as newlines.

  When using cURL, wrap the `--data` body in **single quotes** so that `\n` is preserved for the JSON parser. Avoid `$'...'` quoting, which converts `\n` into a literal newline and produces invalid JSON.
</Tip>

### Updating content with search-and-replace

Use `update_content` to make targeted edits with an array of search-and-replace operations. Each operation specifies `old_str` (content to find) and `new_str` (replacement content).

<CodeGroup>
  ```bash cURL theme={null}
  curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "type": "update_content",
      "update_content": {
        "content_updates": [
          {
            "old_str": "Draft proposal",
            "new_str": "Draft proposal (due Friday)"
          },
          {
            "old_str": "Schedule follow-up",
            "new_str": "Schedule follow-up with design team"
          }
        ]
      }
    }'
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.pages.updateMarkdown({
    page_id: "YOUR_PAGE_ID",
    type: "update_content",
    update_content: {
      content_updates: [
        { old_str: "Draft proposal", new_str: "Draft proposal (due Friday)" },
        { old_str: "Schedule follow-up", new_str: "Schedule follow-up with design team" },
      ],
    },
  });
  ```
</CodeGroup>

Each `old_str` must match exactly one location in the page. If it matches multiple locations, a `validation_error` is returned — set `replace_all_matches: true` on that operation to replace all occurrences.

### Replacing all page content

Use `replace_content` to replace the entire page content with new markdown.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "type": "replace_content",
      "replace_content": {
        "new_str": "# Fresh Start\nThis replaces all previous content."
      }
    }'
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.pages.updateMarkdown({
    page_id: "YOUR_PAGE_ID",
    type: "replace_content",
    replace_content: {
      new_str: "# Fresh Start\nThis replaces all previous content.",
    },
  });
  ```
</CodeGroup>

### Legacy commands

<Info>
  The `insert_content` and `replace_content_range` commands are still supported but are no longer recommended. They use an ellipsis-based selection format that is less precise than the search-and-replace approach of `update_content`. New connections should use `update_content` or `replace_content` instead.
</Info>

<Accordion title="insert_content (legacy)">
  Insert new markdown content at the start of a page, after a specific point in the page, or at the end.

  <CodeGroup>
    ```bash cURL (prepend to start) theme={null}
    curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
      -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
      -H "Content-Type: application/json" \
      -H "Notion-Version: 2026-03-11" \
      --data '{
        "type": "insert_content",
        "insert_content": {
          "content": "## Latest update\nAdded at the top of the page.",
          "position": { "type": "start" }
        }
      }'
    ```

    ```javascript JavaScript theme={null}
    const response = await notion.pages.updateMarkdown({
      page_id: "YOUR_PAGE_ID",
      type: "insert_content",
      insert_content: {
        content: "## Latest update\nAdded at the top of the page.",
        position: { type: "start" },
      },
    });
    ```
  </CodeGroup>

  <CodeGroup>
    ```bash cURL (insert after selection) theme={null}
    curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
      -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
      -H "Content-Type: application/json" \
      -H "Notion-Version: 2026-03-11" \
      --data '{
        "type": "insert_content",
        "insert_content": {
          "content": "## New Section\nInserted content here.",
          "after": "# Meeting Notes...Action items"
        }
      }'
    ```

    ```javascript JavaScript theme={null}
    const response = await notion.pages.updateMarkdown({
      page_id: "YOUR_PAGE_ID",
      type: "insert_content",
      insert_content: {
        content: "## New Section\nInserted content here.",
        after: "# Meeting Notes...Action items",
      },
    });
    ```
  </CodeGroup>

  <CodeGroup>
    ```bash cURL (append to end) theme={null}
    curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
      -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
      -H "Content-Type: application/json" \
      -H "Notion-Version: 2026-03-11" \
      --data '{
        "type": "insert_content",
        "insert_content": {
          "content": "## Appendix\nAdded at the end of the page.",
          "position": { "type": "end" }
        }
      }'
    ```

    ```javascript JavaScript theme={null}
    const response = await notion.pages.updateMarkdown({
      page_id: "YOUR_PAGE_ID",
      type: "insert_content",
      insert_content: {
        content: "## Appendix\nAdded at the end of the page.",
        position: { type: "end" },
      },
    });
    ```
  </CodeGroup>

  The `position` parameter supports `{ "type": "start" }` and `{ "type": "end" }`. When both `position` and `after` are omitted, content is appended to the end of the page, preserving the existing behavior.

  The `after` parameter uses an **ellipsis-based selection** format: `"start text...end text"`. This matches a range from the first occurrence of the start text to the end text. Do not provide `after` and `position` in the same request.
</Accordion>

<Accordion title="replace_content_range (legacy)">
  Replace a matched range of existing content with new markdown.

  <CodeGroup>
    ```bash cURL theme={null}
    curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
      -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
      -H "Content-Type: application/json" \
      -H "Notion-Version: 2026-03-11" \
      --data '{
        "type": "replace_content_range",
        "replace_content_range": {
          "content": "## Updated Section\nNew content replaces the old.",
          "content_range": "## Old Section...end of old content"
        }
      }'
    ```

    ```javascript JavaScript theme={null}
    const response = await notion.pages.updateMarkdown({
      page_id: "YOUR_PAGE_ID",
      type: "replace_content_range",
      replace_content_range: {
        content: "## Updated Section\nNew content replaces the old.",
        content_range: "## Old Section...end of old content",
      },
    });
    ```
  </CodeGroup>

  The `content_range` parameter uses the same ellipsis-based selection as `after`.
</Accordion>

### Safety: protecting child pages and databases

By default, the update endpoint refuses to delete child pages or databases. If an operation would delete them, a `validation_error` is returned listing the affected items.

To allow deletion, set `allow_deleting_content: true` in the command body. This option is supported by `replace_content_range`, `update_content`, and `replace_content`:

```json theme={null}
{
  "type": "replace_content",
  "replace_content": {
    "new_str": "Replacement content.",
    "allow_deleting_content": true
  }
}
```

### Update response

All variants return the full page content as markdown after the update:

```json theme={null}
{
  "object": "page_markdown",
  "id": "page-uuid",
  "markdown": "...full page content after update...",
  "truncated": false,
  "unknown_block_ids": []
}
```

**Key behaviors:**

* Available to all connection types (public, internal, and personal access tokens).
* Requires `update_content` capability.
* The `content_range` / `after` / `old_str` matching is case-sensitive.

### Error responses

| Error code            | Condition                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `validation_error`    | The `content_range` or `after` selection does not match any content in the page, or an `old_str` in `update_content` is not found.          |
| `validation_error`    | Both `insert_content.after` and `insert_content.position` are provided. Use only one insertion target.                                      |
| `validation_error`    | An `old_str` in `update_content` matches multiple locations and `replace_all_matches` is not `true`.                                        |
| `validation_error`    | The operation would delete child pages or databases and `allow_deleting_content` is not `true`. The error message lists the affected items. |
| `validation_error`    | The provided ID is a database or non-page block (use the appropriate API for those record types).                                           |
| `validation_error`    | The target page is a synced page (`external_object_instance_page`). Synced pages cannot be updated.                                         |
| `object_not_found`    | The page does not exist or the connection does not have access to it.                                                                       |
| `restricted_resource` | The connection lacks `update_content` capability.                                                                                           |

### Meeting note transcripts

The update endpoint always skips meeting note transcript content, matching the default behavior of the GET endpoint. If you retrieve a page with `include_transcript=true`, the transcript text will appear in the response but cannot be used in `content_range` or `after` selections — the update endpoint does not see transcript content during matching and will return a `validation_error` for selections that span transcript text.

## Running large markdown writes asynchronously

Create and update requests with large markdown bodies can take longer than typical HTTP client, browser, or edge timeout budgets. For those writes, set `allow_async: true` to receive an `async_task` handle and poll for completion.

Async support is available for:

| Surface | Operation                                                                |
| ------- | ------------------------------------------------------------------------ |
| REST    | `POST /v1/pages` when the request includes the `markdown` body parameter |
| REST    | `PATCH /v1/pages/:page_id/markdown`                                      |
| MCP     | `create_pages`                                                           |
| MCP     | `update_page`                                                            |

Requests that omit `allow_async`, or set it to `false`, keep the existing synchronous response behavior. `allow_async` changes response behavior only; it does not change validation, permissions, or the operation being performed. Notion does not automatically convert a synchronous request into an async response.

<Note>
  Async task completion is polling-first in this version. Use `poll_after_seconds` from the task response as the minimum delay before polling again. Webhook notifications and ETA estimates are not part of the async task contract.
</Note>

### REST: Create a page asynchronously

Set `allow_async: true` on `POST /v1/pages` when creating a page from markdown:

```bash theme={null}
curl -X POST https://api.notion.com/v1/pages \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2026-03-11" \
  --data '{
    "parent": { "page_id": "YOUR_PAGE_ID" },
    "markdown": "# Migration plan\n\nLarge markdown content...",
    "allow_async": true
  }'
```

The initial response is HTTP `202`:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "queued",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "rest",
    "name": "POST /v1/pages"
  }
}
```

### REST: Update markdown asynchronously

Set `allow_async: true` at the top level of the `PATCH /v1/pages/:page_id/markdown` request body:

```bash theme={null}
curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2026-03-11" \
  --data '{
    "allow_async": true,
    "type": "replace_content",
    "replace_content": {
      "new_str": "# Updated plan\n\nLarge replacement markdown..."
    }
  }'
```

The initial response is an `async_task` object with a `status_url` to poll. A `202` response means Notion accepted the request for background execution after initial request and access checks. Markdown parsing, content matching, and other update validation can still fail while the task runs, so always poll until the task reaches `succeeded` or `failed`.

### Poll for completion

Poll the task's `status_url`, or call [Retrieve an async task](/reference/retrieve-async-task) with the returned `id`:

```bash theme={null}
curl 'https://api.notion.com/v1/async_tasks/task_abc123' \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Notion-Version: 2026-03-11"
```

In the [SDK for JavaScript and TypeScript](https://github.com/makenotion/notion-sdk-js) (v5.23.0 and later), `pages.create()` and `pages.updateMarkdown()` accept `allow_async: true`, and `asyncTasks.retrieve()` polls the returned task:

```javascript theme={null}
const task = await notion.asyncTasks.retrieve({ task_id: "task_abc123" })
```

An active task returns a non-terminal status and another polling hint:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "running",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  }
}
```

A successful update task includes the same result shape as the synchronous update:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "succeeded",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  },
  "result": {
    "object": "page_markdown",
    "id": "page-uuid",
    "markdown": "# Updated plan\n\nLarge replacement markdown...",
    "truncated": false,
    "unknown_block_ids": []
  }
}
```

A failed task includes the standard Public API error shape:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "failed",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  },
  "error": {
    "object": "error",
    "status": 400,
    "code": "validation_error",
    "message": "The request body was invalid."
  }
}
```

If a task is `retrying`, Notion is retrying a retryable infrastructure or downstream-service failure. Continue polling with the returned `poll_after_seconds` guidance. If a task reaches `failed`, inspect the error before retrying; validation and permission failures usually require a corrected request.

Completed and failed task metadata is retained for a bounded period. After expiry, polling the task returns the standard not-found response, so store any final result data your application needs.

For the full status resource, see [Retrieve an async task](/reference/retrieve-async-task).

### MCP async examples

For Notion MCP, pass `allow_async: true` to `create_pages` or `update_page`. The tools keep their normal synchronous behavior when `allow_async` is omitted.

```json theme={null}
{
  "tool": "notion-create-pages",
  "arguments": {
    "allow_async": true,
    "parent": { "page_id": "YOUR_PAGE_ID" },
    "pages": [
      {
        "properties": { "title": "Migration plan" },
        "content": "# Migration plan\n\nLarge markdown content..."
      }
    ]
  }
}
```

```json theme={null}
{
  "tool": "notion-update-page",
  "arguments": {
    "allow_async": true,
    "page_id": "YOUR_PAGE_ID",
    "command": "replace_content",
    "new_str": "# Updated plan\n\nLarge replacement markdown..."
  }
}
```

Poll the task with `notion-get-async-task`:

```json theme={null}
{
  "tool": "notion-get-async-task",
  "arguments": {
    "task_id": "task_abc123"
  }
}
```

The MCP status values are the same as REST: `queued`, `running`, `retrying`, `succeeded`, and `failed`. When the task succeeds, the response includes the create or update result. When it fails, the response includes an error object.

## Access control summary

| Endpoint                      | Public connections | Internal connections | Personal access tokens | Required capability |
| ----------------------------- | ------------------ | -------------------- | ---------------------- | ------------------- |
| Create (`POST /v1/pages`)     | Yes                | Yes                  | Yes                    | `insert_content`    |
| Read (`GET .../markdown`)     | Yes                | Yes                  | Yes                    | `read_content`      |
| Update (`PATCH .../markdown`) | Yes                | Yes                  | Yes                    | `update_content`    |
