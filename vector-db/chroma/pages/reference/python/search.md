---
title: "Search"
source: https://docs.trychroma.com/reference/python/search
path: reference/python/search
---

## Search

Payload for hybrid search operations.

Can be constructed by directly providing the parameters, or by using the builder pattern.

Methods

`__init__()`, `group_by()`, `limit()`, `rank()`, `select()`, `select_all()`, `to_dict()`, `where()`

***

## Select

Selection configuration for search results.

Fields can be:

* Key.DOCUMENT - Select document key (equivalent to Key("#document"))
* Key.EMBEDDING - Select embedding key (equivalent to Key("#embedding"))
* Key.SCORE - Select score key (equivalent to Key("#score"))
* Any other string - Select specific metadata property

Note: You can use K as an alias for Key for more concise code.

Properties

**keys** `Set[Union[Key, str]]`

Methods

`__init__()`, `from_dict()`, `to_dict()`

***

## Knn

KNN-based ranking expression.

Properties

**query** `Optional[Embeddings]`

**key** `Union[Key, str]`

**limit** `int`

**default** `Optional[float]`

**return\_rank** `bool`

Methods

`__init__()`, `abs()`, `exp()`, `from_dict()`, `log()`, `max()`, `min()`, `to_dict()`

***

## Rrf

Reciprocal Rank Fusion for combining ranking strategies.

RRF formula: score = -sum(weight\_i / (k + rank\_i)) for each ranking strategy
The negative is used because RRF produces higher scores for better results,
but Chroma uses ascending order (lower scores = better results).

Properties

**ranks** `List[Rank]`

**k** `int`

**weights** `Optional[List[float]]`

**normalize** `bool`

Methods

`__init__()`, `abs()`, `exp()`, `from_dict()`, `log()`, `max()`, `min()`, `to_dict()`

***

## Group By

### GroupBy

Group results by metadata keys and aggregate within each group.

Groups search results by one or more metadata fields, then applies an
aggregation (MinK or MaxK) to select records within each group.
The final output is flattened and sorted by score.

Properties

**keys** `Union[Key, str, List[Union[Key, str]]]`

**aggregate** `Optional[Aggregate]`

Methods

`__init__()`, `from_dict()`, `to_dict()`

### Limit

Limit(offset: int = 0, limit: Optional\[int] = None)

Properties

**offset** `int`

**limit** `Optional[int]`

Methods

`__init__()`, `from_dict()`, `to_dict()`

### MinK

Keep k records with minimum aggregate key values per group

Properties

**keys** `Union[Key, str, List[Union[Key, str]]]`

**k** `int`

Methods

`__init__()`, `from_dict()`, `to_dict()`

### MaxK

Keep k records with maximum aggregate key values per group

Properties

**keys** `Union[Key, str, List[Union[Key, str]]]`

**k** `int`

Methods

`__init__()`, `from_dict()`, `to_dict()`

***

## SearchResult

Column-major response from the search API.

Searches are performed in batches. Each batch is a list of records in columnar form.

```python theme={null}
results = collection.search([search_1, search_2, ...])
payloads = zip(results["ids"], results["documents"], results["metadatas"])
```

Each payload contains a field grouped per search payload, in column-major form.

```python theme={null}
for payload in payloads:
    ids, docs, metas = payload
    for id, doc, meta in zip(ids, docs, metas):
        print(id, doc, meta)
```

Properties

**ids** `List[IDs]`

**documents** `List[Optional[List[Optional[str]]]]`

**embeddings** `List[Optional[List[Optional[List[float]]]]]`

**metadatas** `List[Optional[List[Optional[Dict[str, Any]]]]]`

**scores** `List[Optional[List[Optional[float]]]]`

**select** `List[IDs]`

Methods

`rows()`
