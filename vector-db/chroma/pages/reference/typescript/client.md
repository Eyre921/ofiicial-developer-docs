---
title: "Client"
source: https://docs.trychroma.com/reference/typescript/client
path: reference/typescript/client
---

## Clients

### ChromaClient

Main client class for interacting with ChromaDB.
Provides methods for managing collections and performing operations on them.

**host** `string | undefined`

The host address of the Chroma server. Defaults to 'localhost'

**port** `number | undefined`

The port number of the Chroma server. Defaults to 8000

**ssl** `boolean | undefined`

Whether to use SSL/HTTPS for connections. Defaults to false

**tenant** `string | undefined`

The tenant name in the Chroma server to connect to

**database** `string | undefined`

The database name to connect to

**headers** `Record\<string, string\> | undefined`

Additional HTTP headers to send with requests

**fetchOptions** `RequestInit | undefined`

Additional fetch options for HTTP requests

**path** `string | undefined`

**auth** `Record\<string, string\> | undefined`

### CloudClient

ChromaDB cloud client for connecting to hosted Chroma instances.
Extends ChromaClient with cloud-specific authentication and configuration.

**apiKey** `string`

**host** `string`

**port** `number`

**tenant** `string`

**database** `string`

**fetchOptions** `RequestInit`

### AdminClient

Administrative client for managing ChromaDB tenants and databases.
Provides methods for creating, deleting, and listing tenants and databases.

**host** `string` *required*

The host address of the Chroma server

**port** `number` *required*

The port number of the Chroma server

**ssl** `boolean` *required*

Whether to use SSL/HTTPS for connections

**headers** `Record\<string, string\> | undefined`

Additional HTTP headers to send with requests

**fetchOptions** `RequestInit | undefined`

Additional fetch options for HTTP requests

***

## Client Methods

### heartbeat

Sends a heartbeat request to check server connectivity.

**Returns:** Promise resolving to the server's nanosecond heartbeat timestamp

### listCollections

Lists all collections in the current database.

**limit** `number` *required*

**offset** `number` *required*

**Returns:** Promise resolving to an array of Collection instances

### countCollections

Gets the total number of collections in the current database.

**Returns:** Promise resolving to the collection count

### createCollection

Creates a new collection with the specified configuration.

**name** `string` *required*

**configuration** `CreateCollectionConfiguration`

**metadata** `CollectionMetadata`

**embeddingFunction** `EmbeddingFunction | null`

**schema** `Schema`

**Returns:** Promise resolving to the created Collection instance

### getCollection

Retrieves an existing collection by name.

**name** `string` *required*

**embeddingFunction** `EmbeddingFunction`

**Returns:** Promise resolving to the Collection instance

### getOrCreateCollection

Gets an existing collection or creates it if it doesn't exist.

**name** `string` *required*

**configuration** `CreateCollectionConfiguration`

**metadata** `CollectionMetadata`

**embeddingFunction** `EmbeddingFunction | null`

**schema** `Schema`

**Returns:** Promise resolving to the Collection instance

### deleteCollection

Deletes a collection and all its data.

**name** `string` *required*

### reset

Resets the entire database, deleting all collections and data.

**Returns:** Promise that resolves when the reset is complete

### version

Gets the version of the Chroma server.

**Returns:** Promise resolving to the server version string

***

## Admin Client Methods

### createTenant

Creates a new tenant.

**name** `string` *required*

### getTenant

Retrieves information about a specific tenant.

**name** `string` *required*

**Returns:** Promise resolving to the tenant name

### createDatabase

Creates a new database within a tenant.

**name** `string` *required*

**tenant** `string` *required*

### getDatabase

Retrieves information about a specific database.

**name** `string` *required*

**tenant** `string` *required*

**Returns:** Promise resolving to database information

### deleteDatabase

Deletes a database and all its data.

**name** `string` *required*

**tenant** `string` *required*

### listDatabases

Lists all databases within a tenant.

**args** `ListDatabasesArgs` *required*

Listing parameters including tenant and pagination

**Returns:** Promise resolving to an array of database information
