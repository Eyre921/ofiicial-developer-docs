---
title: "Update a database"
source: https://developers.notion.com/reference/update-database
path: reference/update-database
---

patch /v1/databases/{database_id}
Updates the attributes — the title, description, icon, or cover, etc. — of a specified database.

Returns the updated [database object](/reference/database).

To update the `properties` of the [data sources](/reference/data-source) under a database, use the [Update a data source](/reference/update-a-data-source) API starting from API version `2025-09-03`.

For an overview of how to use the REST API with databases, refer to the [Working with databases](/guides/data-apis/working-with-databases) guide.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
