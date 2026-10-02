---
title: "Move a page"
source: https://developers.notion.com/reference/move-page
path: reference/move-page
---

post /v1/pages/{page_id}/move
Use this API to move an existing Notion page to a new parent.

## Authentication

Requires [bearer token authentication](/reference/authentication) with appropriate [page edit permissions](/reference/capabilities#content-capabilities).

## Path parameters

**`page_id`** (required)

* **Type**: `string` (UUIDv4)
* **Description**: The ID of the page to move
  * This must be a regular Notion page, and not a database. Moving databases or other block types in the API is not currently supported.
* **Format**: UUIDs can be provided with or without dashes
* **Example**: `195de9221179449fab8075a27c979105` or `195de922-1179-449f-ab80-75a27c979105`

## Body parameters

**`parent`** (required)

* **Type**: `object`
* **Description**: The new parent location for the page.
  * The bot must have edit access to the new parent.

The `parent` object can be one of two types:

### Page parent

Move the page under another page:

```json JSON theme={null}
{
  "parent": {
    "type": "page_id",
    "page_id": "<parent-page-id>"
  }
}
```

* **`type`**: Always `"page_id"`
* **`page_id`**: UUID of the parent page (with or without dashes)

<Warning>
  **Page parent must be a regular Notion page**

  The `parent[page_id]` parameter must be a page and cannot be any other type of [block](/reference/block).

  One limited exception: for databases that only have a single [data source](/reference/data-source) , the `database_id` *can* be provided under `page_id`, but this is not recommended, since your connection will start encountering HTTP 400 errors if a second data source is added to the database.
</Warning>

### Database parent

Move the page into a database:

```json JSON theme={null}
{
  "parent": {
    "type": "data_source_id",
    "data_source_id": "<database-data-source-id>"
  }
}
```

* **`type`**: Always `"data_source_id"`
* **`data_source_id`**: UUID of the database's data source (with or without dashes)

**Note**: You must use `data_source_id` rather than `database_id`. Use the [Retrieve a database](/reference/retrieve-a-database) endpoint to get the child data source ID(s) from the database.

## Example requests

### Move page under another page

```bash cURL theme={null}
curl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \
  -H "Authorization: Bearer secret_xxx" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "type": "page_id",
      "page_id": "f336d0bc-b841-465b-8045-024475c079dd"
    }
  }'
```

### Move page into a database

```bash cURL theme={null}
curl -X POST https://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move \
  -H "Authorization: Bearer secret_xxx" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "type": "data_source_id",
      "data_source_id": "1c7b35e6-e67f-8096-bf3f-000ba938459e"
    }
  }'
```
