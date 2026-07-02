---
title: "Embedding Functions"
source: https://docs.trychroma.com/reference/python/embedding-functions
path: reference/python/embedding-functions
---

## Embedding Function Base Classes

### EmbeddingFunction

Protocol for embedding functions.

To implement a new embedding function,
you need to implement the following methods:

* **init**
* **call**
* name
* build\_from\_config
* get\_config

Additionally, you should register the embedding function so it will automatically
be used by the Chroma client.

```python theme={null}
@register_embedding_function
class MyEmbeddingFunction(EmbeddingFunction[Documents]):
    ...
```

<span>Methods</span>

`__init__()`, `build_from_config()`, `default_space()`, `embed_query()`, `embed_with_retries()`, `get_config()`, `is_legacy()`, `name()`, `supported_spaces()`, `validate_config()`, `validate_config_update()`

### SparseEmbeddingFunction

Protocol for sparse embedding functions.

To implement a new sparse embedding function, you need to implement the following methods:

* **call**
* **init**
* name
* build\_from\_config
* get\_config

<span>Methods</span>

`__init__()`, `build_from_config()`, `embed_query()`, `embed_with_retries()`, `get_config()`, `name()`, `validate_config()`, `validate_config_update()`

***

## Registration

### register\_embedding\_function

Register a custom embedding function.

Can be used as a decorator:

```
@register_embedding_function
class MyEmbedding(EmbeddingFunction):
    @classmethod
    def name(cls): return "my_embedding"
```

Or directly:

```
register_embedding_function(MyEmbedding)
```

<ParamField type="Any">
  The embedding function class to register.
</ParamField>

### register\_sparse\_embedding\_function

Register a custom sparse embedding function.

Can be used as a decorator:

```
@register_sparse_embedding_function
class MySparseEmbeddingFunction(SparseEmbeddingFunction):
    @classmethod
    def name(cls): return "my_sparse_embedding"
```

<ParamField type="Any" />

***

## Types

### Embedding

`Embedding[Tuple[Any, Ellipsis], dtype[Union[int32, float32]]]`

### SparseVector

Sparse vector using parallel indices and values arrays.

<span>Properties</span>

<ParamField type="List[int]" />

<ParamField type="List[float]" />

<ParamField type="Optional[IDs]" />

<span>Methods</span>

`__init__()`, `from_dict()`, `to_dict()`
