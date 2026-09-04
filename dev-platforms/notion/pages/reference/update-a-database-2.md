---
title: "Update a database"
source: https://developers.notion.com/reference/update-a-database
path: reference/update-a-database
---

patch /v1/databases/{database_id}

<Danger>
  **Deprecated as of version 2025-09-03**

  >

  This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03).

  Refer to the new APIs instead:

  * [Update a database](/reference/update-database)
  * [Update a data source](/reference/update-a-data-source)
</Danger>

Updates the database object — the title, description, or properties — of a specified database.

Returns the updated [database object](/reference/database).

Database properties represent the columns (or schema) of a database. To update the properties of a database, use the `properties` [body param](/reference/update-property-schema-object) with this endpoint. Learn more about database properties in the [database properties](/reference/property-object) and [Update database properties](/reference/update-property-schema-object) docs.

To update a `relation` database property, share the related database with the connection. Learn more about relations in the [database properties](/reference/property-object#relation) page.

For an overview of how to use the REST API with databases, refer to the [Working with databases](/guides/data-apis/working-with-databases) guide.

### How database property type changes work

All properties in pages are stored as rich text. Notion will convert that rich text based on the types defined in a database's schema. When a type is changed using the API, the data will continue to be available, it is just presented differently.

For example, a multi select property value is represented as a comma-separated list of strings (eg. "1, 2, 3") and a people property value is represented as a comma-separated list of IDs. These are compatible and the type can be converted.

Note: Not all type changes work. In some cases data will no longer be returned, such as people type → file type.

### Interacting with database rows

This endpoint cannot be used to update database rows.

To update the properties of a database row — rather than a column — use the [Update page](/reference/patch-page) endpoint. To add a new row to a database, use the [Create a page](/reference/post-page) endpoint.

### Recommended database schema size limit

Developers are encouraged to keep their database schema size to a maximum of **50KB**. To stay within this schema size limit, the number of properties (or columns) added to a database should be managed.

Database schema updates that are too large will be blocked by the REST API to help developers keep their database queries performant. When a schema update is blocked, the error response includes a `validation_error` code with a message identifying the largest property by name, ID, and byte size to help you reduce your schema size.

### Errors

Returns a 404 HTTP response if the database doesn't exist or if the connection doesn't have access to it.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

<Warning>
  **The following database properties cannot be updated via the API:**

  * `formula`
  * `select`
  * [Synced content](https://www.notion.com/help/guides/synced-databases-bridge-different-tools)
  * A `multi_select` database property’s options values. An option can be removed, but not updated.
</Warning>

<Info>
  **Database relations must be shared with your connection**

  To update a database [relation](https://www.notion.com/help/relations-and-rollups#what-is-a-database-relation) property, the related database must also be shared with your connection.
</Info>
