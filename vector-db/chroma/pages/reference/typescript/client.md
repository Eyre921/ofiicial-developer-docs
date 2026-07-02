---
title: "Client"
source: https://docs.trychroma.com/reference/typescript/client
path: reference/typescript/client
---

## Clients

### ChromaClient

Main client class for interacting with ChromaDB.
Provides methods for managing collections and performing operations on them.

<ParamField type="string | undefined">
  The host address of the Chroma server. Defaults to 'localhost'
</ParamField>

<ParamField type="number | undefined">
  The port number of the Chroma server. Defaults to 8000
</ParamField>

<ParamField type="boolean | undefined">
  Whether to use SSL/HTTPS for connections. Defaults to false
</ParamField>

<ParamField type="string | undefined">
  The tenant name in the Chroma server to connect to
</ParamField>

<ParamField type="string | undefined">
  The database name to connect to
</ParamField>

<ParamField type="Record<string, string> | undefined">
  Additional HTTP headers to send with requests
</ParamField>

<ParamField type="RequestInit | undefined">
  Additional fetch options for HTTP requests
</ParamField>

<ParamField type="string | undefined" />

<ParamField type="Record<string, string> | undefined" />

### CloudClient

ChromaDB cloud client for connecting to hosted Chroma instances.
Extends ChromaClient with cloud-specific authentication and configuration.

<ParamField type="string" />

<ParamField type="string" />

<ParamField type="number" />

<ParamField type="string" />

<ParamField type="string" />

<ParamField type="RequestInit" />

### AdminClient

Administrative client for managing ChromaDB tenants and databases.
Provides methods for creating, deleting, and listing tenants and databases.

<ParamField type="string">
  The host address of the Chroma server
</ParamField>

<ParamField type="number">
  The port number of the Chroma server
</ParamField>

<ParamField type="boolean">
  Whether to use SSL/HTTPS for connections
</ParamField>

<ParamField type="Record<string, string> | undefined">
  Additional HTTP headers to send with requests
</ParamField>

<ParamField type="RequestInit | undefined">
  Additional fetch options for HTTP requests
</ParamField>

***

## Client Methods

### heartbeat

Sends a heartbeat request to check server connectivity.

**Returns:** Promise resolving to the server's nanosecond heartbeat timestamp

### listCollections

Lists all collections in the current database.

<ParamField type="number" />

<ParamField type="number" />

**Returns:** Promise resolving to an array of Collection instances

### countCollections

Gets the total number of collections in the current database.

**Returns:** Promise resolving to the collection count

### createCollection

Creates a new collection with the specified configuration.

<ParamField type="string" />

<ParamField type="CreateCollectionConfiguration" />

<ParamField type="CollectionMetadata" />

<ParamField type="EmbeddingFunction | null" />

<ParamField type="Schema" />

**Returns:** Promise resolving to the created Collection instance

### getCollection

Retrieves an existing collection by name.

<ParamField type="string" />

<ParamField type="EmbeddingFunction" />

**Returns:** Promise resolving to the Collection instance

### getOrCreateCollection

Gets an existing collection or creates it if it doesn't exist.

<ParamField type="string" />

<ParamField type="CreateCollectionConfiguration" />

<ParamField type="CollectionMetadata" />

<ParamField type="EmbeddingFunction | null" />

<ParamField type="Schema" />

**Returns:** Promise resolving to the Collection instance

### deleteCollection

Deletes a collection and all its data.

<ParamField type="string" />

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

<ParamField type="string" />

### getTenant

Retrieves information about a specific tenant.

<ParamField type="string" />

**Returns:** Promise resolving to the tenant name

### createDatabase

Creates a new database within a tenant.

<ParamField type="string" />

<ParamField type="string" />

### getDatabase

Retrieves information about a specific database.

<ParamField type="string" />

<ParamField type="string" />

**Returns:** Promise resolving to database information

### deleteDatabase

Deletes a database and all its data.

<ParamField type="string" />

<ParamField type="string" />

### listDatabases

Lists all databases within a tenant.

<ParamField type="ListDatabasesArgs">
  Listing parameters including tenant and pagination
</ParamField>

**Returns:** Promise resolving to an array of database information
