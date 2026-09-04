---
title: "Create a database"
source: https://developers.notion.com/reference/create-database
path: reference/create-database
---

post /v1/databases
Create a database and its initial data source.

Creates a database as a subpage in the specified parent page, or as a private page at the workspace level, with the specified `properties` schema set on its `initial_data_source`. Currently, the `parent` of a new database must be a Notion page (`page_id` type) or a [wiki database](https://www.notion.com/help/wikis-and-verified-pages).

Use this endpoint to create a database, its first [data source](/reference/data-source), and its first table view, all in one API call. Then, if you want to add a second data source, use the [Create a data source](/reference/create-a-data-source) API with a version of at least `2025-09-03`, and provide the `database_id` as the `id` returned by the database create response.

For a complete reference on what properties are available, see [Data source properties](/reference/property-object). After creating the database, to update one of its child data sources' properties, use the [Update a data source](/reference/update-a-data-source) API.

### Typed databases

Pass `database_type` to build the database from one of Notion's canonical schemas instead of your own. Notion sets the properties and the metadata that marks the database as that type, so the result matches a database of that type created in the Notion app. Supported values are `tasks`, `projects`, and `skills`.

Each type creates a fixed set of properties:

| `database_type` | Properties                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| `tasks`         | Task name (`title`), Assignee (`people`), Status (`status`), Due (`date`)                                          |
| `projects`      | Project name (`title`), Owner (`people`), Dates (`date`), Status (`status`)                                        |
| `skills`        | Skill name (`title`), Description (`rich_text`), Files (`files`), Tags (`multi_select`), Created by (`created_by`) |

Property names follow the language preference of the user who owns the integration token. Internal integrations have no owner, so they get English names. Call [Retrieve a data source](/reference/retrieve-a-data-source) on the data source returned in the create response to read the exact names, along with the `status` option names and IDs, before writing pages. To add properties of your own on top of a typed schema, use [Update a data source](/reference/update-a-data-source).

`database_type` can't be combined with `initial_data_source`, because a typed database always uses Notion's schema. Sending both returns a 400 HTTP response. If you omit `title`, the database is named after its type. The created database and its data source both report the type back as `database_type`.

<Info>
  **Connection capabilities**

  > This endpoint requires a connection to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

> Returns a 404 if the specified parent page does not exist, or if the connection does not have access to the parent page.

> Returns a 400 if the request is incorrectly formatted, or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
