---
title: "Retrieve a data source"
source: https://developers.notion.com/reference/retrieve-a-data-source
path: reference/retrieve-a-data-source
---

get /v1/data_sources/{data_source_id}

Retrieves a [data source](/reference/data-source) object — information that describes the structure and columns of a data source — for a provided data source ID. The response adheres to any limits to a connection’s capabilities and the permissions of the data source and its containing database.

To fetch data source *rows* (i.e. the child pages of a data source) rather than columns, use the [Query a data source](/reference/query-a-data-source) endpoint.

### Finding a data source ID

First, find the containing database's ID in its Notion URL. The database ID is the 32-character alphanumeric string between the slash following the workspace name (if applicable) and the question mark.

<Frame>
  <img />
</Frame>

Use [Retrieve a database](/reference/retrieve-database) with that database ID. Its `data_sources` array lists each data source's ID and name. Use the desired data source ID with this endpoint to retrieve its `properties`.

To get a data source ID from the Notion app directly, the settings menu for a database includes a "Copy data source ID" button under "Manage data sources":

<Frame>
  <img />
</Frame>

Refer to the [Working with databases](/guides/data-apis/working-with-databases) guide for more details.

### Errors

Returns a 404 HTTP response if the data source doesn't exist or if the connection doesn't have access to it.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

### Additional resources

* [How to share a database with your connection](/guides/get-started/quick-start#give-your-connection-page-permissions)
* [Working with databases guide](/guides/data-apis/working-with-databases)

<Info>
  **Data source relations must be shared with your connection**

  To retrieve data source properties from [database relations](https://www.notion.com/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your connection in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.
</Info>

<Warning>
  **The Notion API does not support retrieving linked data sources**

  To fetch the information in a [linked data source](https://www.notion.com/help/guides/using-linked-databases), share the original source database with your Notion connection.
</Warning>
