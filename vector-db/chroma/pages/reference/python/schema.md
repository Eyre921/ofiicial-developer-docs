---
title: "Schema"
source: https://docs.trychroma.com/reference/python/schema
path: reference/python/schema
---

## Schema

Collection schema for indexing and encryption configuration.

Properties

**defaults** `ValueTypes`

**keys** `Dict[str, ValueTypes]`

**cmek** `Optional[Cmek]`

***

## Index configs

### FtsIndexConfig

Configuration for Full-Text Search index. No parameters required.

### HnswIndexConfig

Configuration for HNSW vector index.

Properties

**ef\_construction** `Optional[int]`

**max\_neighbors** `Optional[int]`

**ef\_search** `Optional[int]`

**num\_threads** `Optional[int]`

**batch\_size** `Optional[int]`

**sync\_threshold** `Optional[int]`

**resize\_factor** `Optional[float]`

### SpannIndexConfig

Configuration for SPANN vector index.

Properties

**search\_nprobe** `Optional[int]`

**write\_nprobe** `Optional[int]`

**ef\_construction** `Optional[int]`

**ef\_search** `Optional[int]`

**max\_neighbors** `Optional[int]`

**reassign\_neighbor\_count** `Optional[int]`

**split\_threshold** `Optional[int]`

**merge\_threshold** `Optional[int]`

### VectorIndexConfig

Configuration for vector index with space, embedding function, and algorithm config.

Properties

**space** `Optional[Literal[cosine, l2, ip]]`

**embedding\_function** `Optional[Any]`

**source\_key** `Optional[str]`

**hnsw** `Optional[HnswIndexConfig]`

**spann** `Optional[SpannIndexConfig]`

### SparseVectorIndexConfig

Configuration for sparse vector index.

Properties

**embedding\_function** `Optional[Any]`

**source\_key** `Optional[str]`

**bm25** `Optional[bool]`

### StringInvertedIndexConfig

Configuration for string inverted index.

### IntInvertedIndexConfig

Configuration for integer inverted index.

### FloatInvertedIndexConfig

Configuration for float inverted index.

### BoolInvertedIndexConfig

Configuration for boolean inverted index.
