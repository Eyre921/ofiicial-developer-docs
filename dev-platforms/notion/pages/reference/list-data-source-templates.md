---
title: "List data source templates"
source: https://developers.notion.com/reference/list-data-source-templates
path: reference/list-data-source-templates
---

get /v1/data_sources/{data_source_id}/templates
List the page templates your connection can read in a data source.

The response contains a `templates` array with up to 100 results per page. To filter by name, pass all or part of a template name in the `name` query parameter. Matching ignores case.

| Field | Type | Description |
| :- | :- | :- |
| `id` | `string` (UUIDv4) | The template ID. |
| `name` | `string` | The template's display name. |
| `is_default` | `boolean` | Whether the template is the data source's default. |

### Pagination

If more templates are available, `has_more` is `true` and `next_cursor` contains the cursor for the next page. Pass that value as `start_cursor` in the next request.

In the [JavaScript SDK](https://github.com/makenotion/notion-sdk-js) v5.3.0 or later, use `iterateDataSourceTemplates` to follow the cursors. The example reads your token from `NOTION_API_KEY` and the data source ID from `NOTION_DATA_SOURCE_ID`.

```javascript theme={null}
import { Client, iterateDataSourceTemplates } from "@notionhq/client";

const notion = new Client({ auth: process.env.NOTION_API_KEY });
for await (const template of iterateDataSourceTemplates(notion, {
  data_source_id: process.env.NOTION_DATA_SOURCE_ID,
})) {
  console.log(template.name, template.id);
}
```

### Permissions

This endpoint returns only templates under the specified data source that the connection can access. Sharing the parent database with the connection generally grants access to its child templates.

Templates are also Notion pages. Use [Retrieve a page](/reference/retrieve-a-page) for its properties or [Retrieve a page as markdown](/reference/retrieve-page-markdown) for its content. You can also open a template in Notion and copy its URL to find its ID.

### Errors

Returns a 404 HTTP response if the data source doesn't exist or if the connection doesn't have access to it.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
