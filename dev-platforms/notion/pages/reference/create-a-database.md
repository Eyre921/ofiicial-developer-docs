---
title: "Create a database"
source: https://developers.notion.com/reference/create-a-database
path: reference/create-a-database
---

post /v1/databases

<Danger>
  **Deprecated as of version 2025-09-03**

  This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03).

  Refer to the new APIs instead:

  * [Create a database](/reference/create-database)
  * [Create a data source](/reference/create-a-data-source)
</Danger>

Creates a database as a subpage in the specified parent page, with the specified `properties` schema. Currently, the parent of a new database must be a Notion page or a [wiki database](https://www.notion.so/help/wikis-and-verified-pages).

<Info>
  **Connection capabilities**

  This endpoint requires a connection to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 404 if the specified parent page does not exist, or if the connection does not have access to the parent page.

Returns a 400 if the request is incorrectly formatted, or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
