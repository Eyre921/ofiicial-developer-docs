---
title: "Schema"
source: https://docs.trychroma.com/reference/typescript/schema
path: reference/typescript/schema
---

## Schema

Collection schema for configuring indexes and encryption.

The schema controls how data is indexed and can optionally specify
customer-managed encryption keys (CMEK) for data at rest.

Properties

**defaults** `ValueTypes`

**keys** `Record\<string, ValueTypes\>`

**cmek** `Cmek | null`

***

## Index configs

### FtsIndexConfig

Properties

**type** `FtsIndexConfig`

### StringInvertedIndexConfig

Properties

**type** `StringInvertedIndexConfig`

### IntInvertedIndexConfig

Properties

**type** `IntInvertedIndexConfig`

### FloatInvertedIndexConfig

Properties

**type** `FloatInvertedIndexConfig`

### BoolInvertedIndexConfig

Properties

**type** `BoolInvertedIndexConfig`

### VectorIndexConfig

Properties

**type** `VectorIndexConfig`

**space** `Space | null`

**embeddingFunction** `EmbeddingFunction | null | undefined`

**sourceKey** `string | null`

**hnsw** `HnswIndexConfig | null`

**spann** `SpannIndexConfig | null`

### SparseVectorIndexConfig

Properties

**type** `SparseVectorIndexConfig`

**embeddingFunction** `SparseEmbeddingFunction | null | undefined`

**sourceKey** `string | null`

**bm25** `boolean | null`
