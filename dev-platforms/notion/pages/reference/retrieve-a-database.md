---
title: "Retrieve a database"
source: https://developers.notion.com/reference/retrieve-a-database
path: reference/retrieve-a-database
---

get /v1/databases/{database_id}

<Warning>
  **Deprecated as of version 2025-09-03**

  This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03).

  Refer to the new APIs instead:

  * [Retrieve a database](/reference/retrieve-database)
  * [Retrieve a data source](/reference/retrieve-a-data-source)
</Warning>

Retrieves a [database object](/reference/database) — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to a connection’s capabilities.

To fetch database rows rather than columns, use the [Query a database](/reference/post-database-query) endpoint.

To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.

<Frame>
  <img alt="1340" />
</Frame>

Refer to the [Working with databases](/guides/data-apis/working-with-databases) guide for more details.

### Errors

ErrorsEach Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

### Additional resources

* [How to share a database with your connection](/guides/get-started/quick-start#give-your-connection-page-permissions)
* [Working with databases guide](/guides/data-apis/working-with-databases)

<Info>
  **Database relations must be shared with your connection**

  To retrieve database properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your connection in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.
</Info>

<Warning>
  **The Notion API does not support retrieving linked databases.**

  To fetch the information in a [linked database](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion connection.
</Warning>
