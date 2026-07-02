---
title: "Schema"
source: https://docs.trychroma.com/reference/python/schema
path: reference/python/schema
---

## Schema

Collection schema for indexing and encryption configuration.

<span>Properties</span>

<ParamField type="ValueTypes" />

<ParamField type="Dict[str, ValueTypes]" />

<ParamField type="Optional[Cmek]" />

***

## Index configs

### FtsIndexConfig

Configuration for Full-Text Search index. No parameters required.

### HnswIndexConfig

Configuration for HNSW vector index.

<span>Properties</span>

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[float]" />

### SpannIndexConfig

Configuration for SPANN vector index.

<span>Properties</span>

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

### VectorIndexConfig

Configuration for vector index with space, embedding function, and algorithm config.

<span>Properties</span>

<ParamField type="Optional[Literal[cosine, l2, ip]]" />

<ParamField type="Optional[Any]" />

<ParamField type="Optional[str]" />

<ParamField type="Optional[HnswIndexConfig]" />

<ParamField type="Optional[SpannIndexConfig]" />

### SparseVectorIndexConfig

Configuration for sparse vector index.

<span>Properties</span>

<ParamField type="Optional[Any]" />

<ParamField type="Optional[str]" />

<ParamField type="Optional[bool]" />

### StringInvertedIndexConfig

Configuration for string inverted index.

### IntInvertedIndexConfig

Configuration for integer inverted index.

### FloatInvertedIndexConfig

Configuration for float inverted index.

### BoolInvertedIndexConfig

Configuration for boolean inverted index.
