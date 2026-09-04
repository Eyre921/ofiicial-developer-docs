---
title: "List data source templates"
source: https://developers.notion.com/reference/list-data-source-templates
path: reference/list-data-source-templates
---

get /v1/data_sources/{data_source_id}/templates
Use this API to retrieve details of all page templates available for a data source.

The response contains a `templates` array with up to 100 results per page. Each template has the following fields:

| Field        | Type              | Description                                        |
| :----------- | :---------------- | :------------------------------------------------- |
| `id`         | `string` (UUIDv4) | The template ID.                                   |
| `name`       | `string`          | The template's display name.                       |
| `is_default` | `boolean`         | Whether the template is the data source's default. |

### Pagination

If more templates are available, `has_more` is `true` and `next_cursor` contains the cursor for the next page. Pass that value as `start_cursor` in the next request.

### Permissions

This endpoint returns only templates under the specified data source that the connection can access. Sharing the parent database with the connection generally grants access to its child templates.

Templates are also Notion pages. Use [Retrieve a page](/reference/retrieve-a-page) to get a template's properties and content. You can also open a template in Notion and copy its URL to find its ID.

### Errors

Returns a 404 HTTP response if the data source doesn't exist or if the connection doesn't have access to it.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
