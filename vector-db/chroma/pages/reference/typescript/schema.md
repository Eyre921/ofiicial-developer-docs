---
title: "Schema"
source: https://docs.trychroma.com/reference/typescript/schema
path: reference/typescript/schema
---

## Schema

Collection schema for configuring indexes and encryption.

The schema controls how data is indexed and can optionally specify
customer-managed encryption keys (CMEK) for data at rest.

<span>Properties</span>

<ParamField type="ValueTypes" />

<ParamField type="Record<string, ValueTypes>" />

<ParamField type="Cmek | null" />

***

## Index configs

### FtsIndexConfig

<span>Properties</span>

<ParamField type="FtsIndexConfig" />

### StringInvertedIndexConfig

<span>Properties</span>

<ParamField type="StringInvertedIndexConfig" />

### IntInvertedIndexConfig

<span>Properties</span>

<ParamField type="IntInvertedIndexConfig" />

### FloatInvertedIndexConfig

<span>Properties</span>

<ParamField type="FloatInvertedIndexConfig" />

### BoolInvertedIndexConfig

<span>Properties</span>

<ParamField type="BoolInvertedIndexConfig" />

### VectorIndexConfig

<span>Properties</span>

<ParamField type="VectorIndexConfig" />

<ParamField type="Space | null" />

<ParamField type="EmbeddingFunction | null | undefined" />

<ParamField type="string | null" />

<ParamField type="HnswIndexConfig | null" />

<ParamField type="SpannIndexConfig | null" />

### SparseVectorIndexConfig

<span>Properties</span>

<ParamField type="SparseVectorIndexConfig" />

<ParamField type="SparseEmbeddingFunction | null | undefined" />

<ParamField type="string | null" />

<ParamField type="boolean | null" />
