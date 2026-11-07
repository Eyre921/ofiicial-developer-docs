---
title: "Collection"
source: https://docs.trychroma.com/reference/typescript/collection
path: reference/typescript/collection
---

## Collection Methods

### count

Gets the total number of records in the collection

### add

Adds new records to the collection.

**ids** `string[]` *required*

**embeddings** `Embeddings`

**metadatas** `Metadata[]`

**documents** `string[]`

**uris** `string[]`

### get

Retrieves records from the collection based on filters.

**ids** `string[]`

**where** `Where`

**limit** `number`

**offset** `number`

**whereDocument** `WhereDocument`

**include** `Include[]`

**Returns:** Promise resolving to matching records

### peek

Retrieves a preview of records from the collection.

**limit** `number`

**Returns:** Promise resolving to a sample of records

### query

Performs similarity search on the collection.

**queryEmbeddings** `Embeddings`

**queryTexts** `string[]`

**queryURIs** `string[]`

**ids** `string[]`

**nResults** `number`

**where** `Where`

**whereDocument** `WhereDocument`

**include** `Include[]`

**Returns:** Promise resolving to similar records ranked by distance

### modify

Modifies collection properties like name, metadata, or configuration.

**name** `string`

**metadata** `CollectionMetadata`

**configuration** `UpdateCollectionConfiguration`

### update

Updates existing records in the collection.

**ids** `string[]` *required*

**embeddings** `Embeddings`

**metadatas** `Metadata[]`

**documents** `string[]`

**uris** `string[]`

### upsert

Inserts new records or updates existing ones (upsert operation).

**ids** `string[]` *required*

**embeddings** `Embeddings`

**metadatas** `Metadata[]`

**documents** `string[]`

**uris** `string[]`

### delete

Deletes records from the collection based on filters.

**ids** `string[]`

**where** `Where`

**whereDocument** `WhereDocument`

### search

Performs hybrid search on the collection using expression builders.

**searches** `SearchLike | SearchLike[]` *required*

Single search payload or array of payloads

**readLevel** `ReadLevel`

**Returns:** Promise resolving to column-major search results

***

## Types

### GetResult

Result class for get operations, containing retrieved records.

Properties

**documents** `(string | null)[]`

**embeddings** `Embeddings`

**ids** `string[]`

**include** `Include[]`

**metadatas** `(TMeta | null)[]`

**uris** `(string | null)[]`

### QueryResult

Result class for query operations, containing search results.

Properties

**distances** `(number | null)[][]`

**documents** `(string | null)[][]`

**embeddings** `(Embedding | null)[][]`

**ids** `string[][]`

**include** `Include[]`

**metadatas** `(TMeta | null)[][]`

**uris** `(string | null)[][]`
