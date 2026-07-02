---
title: "Client"
source: https://docs.trychroma.com/reference/python/client
path: reference/python/client
---

## Clients

### EphemeralClient

Create an in-memory client for local use.

This client stores all data in memory and does not persist to disk.
It is intended for testing and development.

<ParamField type="Optional[Settings]">
  Optional settings to override defaults.
</ParamField>

<ParamField type="str">
  Tenant name to use for requests. Defaults to the default tenant.
</ParamField>

<ParamField type="str">
  Database name to use for requests. Defaults to the default database.
</ParamField>

### PersistentClient

Create a persistent client that stores data on disk.

This client is intended for local development and testing. For production,
prefer a server-backed Chroma instance.

<ParamField type="Union[str, Path]">
  Directory to store persisted data.
</ParamField>

<ParamField type="Optional[Settings]">
  Optional settings to override defaults.
</ParamField>

<ParamField type="str">
  Tenant name to use for requests.
</ParamField>

<ParamField type="str">
  Database name to use for requests.
</ParamField>

### HttpClient

Create a client that connects to a Chroma server.

<ParamField type="str">
  Hostname of the Chroma server.
</ParamField>

<ParamField type="int">
  HTTP port of the Chroma server.
</ParamField>

<ParamField type="bool">
  Whether to enable SSL for the connection.
</ParamField>

<ParamField type="Optional[Dict[str, str]]">
  Optional headers to send with each request.
</ParamField>

<ParamField type="Optional[Settings]">
  Optional settings to override defaults.
</ParamField>

<ParamField type="str">
  Tenant name to use for requests.
</ParamField>

<ParamField type="str">
  Database name to use for requests.
</ParamField>

### AsyncHttpClient

Create an async client that connects to a Chroma HTTP server.

This supports multiple clients connecting to the same server and is the
recommended production configuration.

<ParamField type="str">
  Hostname of the Chroma server.
</ParamField>

<ParamField type="int">
  HTTP port of the Chroma server.
</ParamField>

<ParamField type="bool">
  Whether to enable SSL for the connection.
</ParamField>

<ParamField type="Optional[Dict[str, str]]">
  Optional headers to send with each request.
</ParamField>

<ParamField type="Optional[Settings]">
  Optional settings to override defaults.
</ParamField>

<ParamField type="str">
  Tenant name to use for requests.
</ParamField>

<ParamField type="str">
  Database name to use for requests.
</ParamField>

### CloudClient

Create a client for Chroma Cloud.

If not provided, `tenant`, `database`, and `api_key` will be inferred from the environment variables `CHROMA_TENANT`, `CHROMA_DATABASE`, and `CHROMA_API_KEY`.

<ParamField type="Optional[str]">
  Tenant name to use, or None to infer from credentials.
</ParamField>

<ParamField type="Optional[str]">
  Database name to use, or None to infer from credentials.
</ParamField>

<ParamField type="Optional[str]">
  API key for Chroma Cloud.
</ParamField>

<ParamField type="Optional[Settings]">
  Optional settings to override defaults.
</ParamField>

<ParamField type="str" />

<ParamField type="int" />

<ParamField type="bool" />

### AdminClient

Create an admin client for tenant and database management.

<ParamField type="Settings" />

***

## Client Methods

### heartbeat

Get the current time in nanoseconds since epoch.

Used to check if the server is alive.

**Returns:** The current time in nanoseconds since epoch

### list\_collections

List all collections.

<ParamField type="Optional[int]">
  The maximum number of entries to return. Defaults to None.
</ParamField>

<ParamField type="Optional[int]">
  The number of entries to skip before returning. Defaults to None.
</ParamField>

**Returns:** A list of collections

### count\_collections

Count the number of collections.

**Returns:** The number of collections.

### create\_collection

Create a new collection with the given name and metadata.

<ParamField type="str">
  The name of the collection to create.
</ParamField>

<ParamField type="Optional[Schema]" />

<ParamField type="Optional[CreateCollectionConfiguration]" />

<ParamField type="Optional[Dict[str, Any]]">
  Optional metadata to associate with the collection.
</ParamField>

<ParamField type="Optional[EmbeddingFunction[Optional[Embeddings]]]">
  Optional function to use to embed documents.
  Uses the default embedding function if not provided.
</ParamField>

<ParamField type="Optional[DataLoader[Optional[Embeddings]]]">
  Optional function to use to load records (documents, images, etc.)
</ParamField>

<ParamField type="bool">
  If True, return the existing collection if it exists.
</ParamField>

**Returns:** The newly created collection.

**Raises:**

* ValueError: If the collection already exists and get\_or\_create is False.
* ValueError: If the collection name is invalid.

### get\_collection

Get a collection with the given name.

<ParamField type="str">
  The name of the collection to get
</ParamField>

<ParamField type="Optional[EmbeddingFunction[Optional[Embeddings]]]">
  Optional function to use to embed documents.
  Uses the default embedding function if not provided.
</ParamField>

<ParamField type="Optional[DataLoader[Optional[Embeddings]]]">
  Optional function to use to load records (documents, images, etc.)
</ParamField>

**Returns:** The collection

**Raises:**

* ValueError: If the collection does not exist

### get\_or\_create\_collection

Get or create a collection with the given name and metadata.

Args:
name: The name of the collection to get or create
metadata: Optional metadata to associate with the collection. If
the collection already exists, the metadata provided is ignored.
If the collection does not exist, the new collection will be created
with the provided metadata.
embedding\_function: Optional function to use to embed documents
data\_loader: Optional function to use to load records (documents, images, etc.)

Returns:
The collection

Examples:

```python theme={null}
client.get_or_create_collection("my_collection")
# collection(name="my_collection", metadata={})
```

<ParamField type="str" />

<ParamField type="Optional[Schema]" />

<ParamField type="Optional[CreateCollectionConfiguration]" />

<ParamField type="Optional[Dict[str, Any]]" />

<ParamField type="Optional[EmbeddingFunction[Optional[Embeddings]]]" />

<ParamField type="Optional[DataLoader[Optional[Embeddings]]]" />

### delete\_collection

Delete a collection with the given name.

<ParamField type="str">
  The name of the collection to delete.
</ParamField>

**Raises:**

* ValueError: If the collection does not exist.

### reset

Resets the database. This will delete all collections and entries.

**Returns:** True if the database was reset successfully.

### get\_version

Get the version of Chroma.

**Returns:** The version of Chroma

### get\_settings

Get the settings used to initialize.

**Returns:** The settings used to initialize.

### get\_max\_batch\_size

Return the maximum number of records that can be created or mutated in a single call.

***

## Admin Client Methods

### create\_tenant

Create a new tenant. Raises an error if the tenant already exists.

<ParamField type="str" />

### get\_tenant

Get a tenant. Raises an error if the tenant does not exist.

<ParamField type="str" />

### create\_database

Create a new database. Raises an error if the database already exists.

<ParamField type="str" />

<ParamField type="str" />

### get\_database

Get a database. Raises an error if the database does not exist.

<ParamField type="str" />

<ParamField type="str">
  The tenant of the database to get.
</ParamField>

### delete\_database

Delete a database. Raises an error if the database does not exist.

<ParamField type="str" />

<ParamField type="str">
  The tenant of the database to delete.
</ParamField>

### list\_databases

List all databases for a tenant. Raises an error if the tenant does not exist.

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="str">
  The tenant to list databases for.
</ParamField>
