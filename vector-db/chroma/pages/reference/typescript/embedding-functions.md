---
title: "Embedding Functions"
source: https://docs.trychroma.com/reference/typescript/embedding-functions
path: reference/typescript/embedding-functions
---

## Embedding Functions

### EmbeddingFunction

Interface for embedding functions.
Embedding functions transform text documents into numerical representations
that can be used for similarity search and other vector operations.

<span>Properties</span>

<ParamField type="string | undefined">
  Optional name identifier for the embedding function
</ParamField>

<span>Methods</span>

`buildFromConfig()`, `defaultSpace()`, `generate()`, `generateForQueries()`, `getConfig()`, `supportedSpaces()`, `validateConfig()`, `validateConfigUpdate()`

### SparseEmbeddingFunction

Interface for sparse embedding functions.
Sparse embedding functions transform text documents into sparse numerical representations
where only non-zero values are stored, making them efficient for high-dimensional spaces.

<span>Properties</span>

<ParamField type="string | undefined">
  Optional name identifier for the embedding function
</ParamField>

<span>Methods</span>

`buildFromConfig()`, `generate()`, `generateForQueries()`, `getConfig()`, `validateConfig()`, `validateConfigUpdate()`
