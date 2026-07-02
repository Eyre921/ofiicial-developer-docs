---
title: "List data source templates"
source: https://developers.notion.com/reference/list-data-source-templates
path: reference/list-data-source-templates
---

get /v1/data_sources/{data_source_id}/templates
Use this API to retrieve details of all page templates available for a data source.

The response object contains an array `page_size` results (up to 100) under the `templates` key. Each element of the array is a JSON object with the following attributes:

| Key          | Data Type                | Meaning                                             |
| :----------- | :----------------------- | :-------------------------------------------------- |
| `id`         | `String` (UUIDv4 format) | The ID of the template.                             |
| `name`       | `String`                 | The display name of the template.                   |
| `is_default` | `Boolean`                | Whether that template is the data source's default. |

**Pagination**: When there are more templates than the current API response contains, the `has_more` boolean field is set to `true`, and the `next_cursor` is set to the ID of the next template to use as the `start_cursor` of your next API request.

Only templates under the data source identified by the `data_source_id` in the URL are returned. Also, the bot must have access to the template for it to appear in this API. However, in most cases, as long as the bot is connected to the data source's parent database (check the "Connections" list under the 3-dot menu), this access also extends to all of the child templates.

Templates are also valid Notion pages, so you can retrieve a template's full properties and content using the [Retrieve a page](/reference/retrieve-a-page) API. This also means that opening a template in the Notion app and copying its URL is an alternative way to get its ID.
