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

<ParamField type="string[]" />

<ParamField type="Embeddings" />

<ParamField type="Metadata[]" />

<ParamField type="string[]" />

<ParamField type="string[]" />

### get

Retrieves records from the collection based on filters.

<ParamField type="string[]" />

<ParamField type="Where" />

<ParamField type="number" />

<ParamField type="number" />

<ParamField type="WhereDocument" />

<ParamField type="Include[]" />

**Returns:** Promise resolving to matching records

### peek

Retrieves a preview of records from the collection.

<ParamField type="number" />

**Returns:** Promise resolving to a sample of records

### query

Performs similarity search on the collection.

<ParamField type="Embeddings" />

<ParamField type="string[]" />

<ParamField type="string[]" />

<ParamField type="string[]" />

<ParamField type="number" />

<ParamField type="Where" />

<ParamField type="WhereDocument" />

<ParamField type="Include[]" />

**Returns:** Promise resolving to similar records ranked by distance

### modify

Modifies collection properties like name, metadata, or configuration.

<ParamField type="string" />

<ParamField type="CollectionMetadata" />

<ParamField type="UpdateCollectionConfiguration" />

### update

Updates existing records in the collection.

<ParamField type="string[]" />

<ParamField type="Embeddings" />

<ParamField type="Metadata[]" />

<ParamField type="string[]" />

<ParamField type="string[]" />

### upsert

Inserts new records or updates existing ones (upsert operation).

<ParamField type="string[]" />

<ParamField type="Embeddings" />

<ParamField type="Metadata[]" />

<ParamField type="string[]" />

<ParamField type="string[]" />

### delete

Deletes records from the collection based on filters.

<ParamField type="string[]" />

<ParamField type="Where" />

<ParamField type="WhereDocument" />

### search

Performs hybrid search on the collection using expression builders.

<ParamField type="SearchLike | SearchLike[]">
  Single search payload or array of payloads
</ParamField>

<ParamField type="ReadLevel" />

**Returns:** Promise resolving to column-major search results

***

## Types

### GetResult

Result class for get operations, containing retrieved records.

<span>Properties</span>

<ParamField type="(string | null)[]" />

<ParamField type="Embeddings" />

<ParamField type="string[]" />

<ParamField type="Include[]" />

<ParamField type="(TMeta | null)[]" />

<ParamField type="(string | null)[]" />

### QueryResult

Result class for query operations, containing search results.

<span>Properties</span>

<ParamField type="(number | null)[][]" />

<ParamField type="(string | null)[][]" />

<ParamField type="(Embedding | null)[][]" />

<ParamField type="string[][]" />

<ParamField type="Include[]" />

<ParamField type="(TMeta | null)[][]" />

<ParamField type="(string | null)[][]" />
