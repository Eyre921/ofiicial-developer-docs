---
title: "Search"
source: https://docs.trychroma.com/reference/search
path: reference/search
---

Reference guide for Search dictionary syntax used in Chroma.

Search dictionaries define filtering, ranking, grouping, pagination, and field
selection for Chroma queries. Each SDK provides a DSL, but they compile to the
same JSON format that you can construct directly.

For example, SDK code like this:

<CodeGroup>
  ```python Python theme={null}
  from chromadb import Search, K, Knn, GroupBy, MinK

  search = Search(
      where=K("status") == "active",
      rank=Knn(query="machine learning research", limit=100),
      group_by=GroupBy(keys=K("category"), aggregate=MinK(keys=K.SCORE, k=2)),
      limit=10,
      select=[K.DOCUMENT, K.SCORE, "category"]
  )
  ```

  ```typescript TypeScript theme={null}
  import { Search, K, Knn, GroupBy, MinK } from 'chromadb';

  const search = new Search({
    where: K("status").eq("active"),
    rank: Knn({ query: "machine learning research", limit: 100 }),
    groupBy: new GroupBy([K("category")], new MinK([K.SCORE], 2)),
    limit: 10,
    select: [K.DOCUMENT, K.SCORE, "category"]
  });
  ```

  ```rust Rust theme={null}
  use chroma::types::{Aggregate, GroupBy, Key, QueryVector, RankExpr, SearchPayload};

  let search = SearchPayload::default()
      .r#where(Key::field("status").eq("active"))
      .rank(RankExpr::Knn {
          query: QueryVector::Dense(vec![0.1, 0.2, 0.3]),
          key: Key::Embedding,
          limit: 100,
          default: None,
          return_rank: false,
      })
      .group_by(GroupBy {
          keys: vec![Key::field("category")],
          aggregate: Some(Aggregate::MinK {
              keys: vec![Key::Score],
              k: 2,
          }),
      })
      .limit(Some(10), 0)
      .select([Key::Document, Key::Score, Key::field("category")]);
  ```
</CodeGroup>

Gets compiled to this JSON:

```json theme={null}
{
  "where": {"status": {"$eq": "active"}},
  "rank": {"$knn": {"query": "machine learning research", "limit": 100}},
  "group_by": {
    "keys": ["category"],
    "aggregate": {"$min_k": {"keys": ["#score"], "k": 2}}
  },
  "limit": {"limit": 10, "offset": 0},
  "select": {"keys": ["#document", "#score", "category"]}
}
```

This reference describes the Search dictionary format and rules. For related
dictionary references, see [Where Filters](./where-filter).

## JSON Format

### Basic Structure

A Search dictionary is an object with optional keys:

```json theme={null}
{
  "where": { /* where filter dictionary */ },
  "rank": { /* rank expression dictionary */ },
  "group_by": { /* group by dictionary */ },
  "limit": {"limit": 10, "offset": 0},
  "select": {"keys": ["#document", "#score"]}
}
```

All keys are optional. Omitted keys use Search defaults.

## Component Schemas

### `where`

`where` uses the Where Filter dictionary schema.

```json theme={null}
{
  "where": ...
}
```

See [Where Filters](./where-filter) for full operator and rule definitions.

### `rank`

`rank` must be a dictionary with exactly one top-level operator.

```json theme={null}
{
  "rank": RankExpr
}
```

```json theme={null}
{
  "RankExpr": {"$val": "number"}
}
```

```json theme={null}
{
  "RankExpr": {
    "$knn": {
      "query": "string | number[] | SparseVector",
      "key": "string (optional)",
      "limit": "positive integer (optional)",
      "default": "number (optional)",
      "return_rank": "boolean (optional)"
    }
  }
}
```

```json theme={null}
{
  "RankExpr": {
    "$op": ...
  }
}
```

| Operator                   | Format                                        |
| -------------------------- | --------------------------------------------- |
| `$sum`                     | `["RankExpr", "RankExpr", "... (min 2)"]`     |
| `$mul`                     | `["RankExpr", "RankExpr", "... (min 2)"]`     |
| `$max`                     | `["RankExpr", "RankExpr", "... (min 2)"]`     |
| `$min`                     | `["RankExpr", "RankExpr", "... (min 2)"]`     |
| `$sub` (l-r)               | `{ "left": "RankExpr", "right": "RankExpr" }` |
| `$div` (l/r)               | `{ "left": "RankExpr", "right": "RankExpr" }` |
| `$abs`                     | `"RankExpr"`                                  |
| `$exp` (e<sup>x</sup>)     | `"RankExpr"`                                  |
| `$log` (Natural logarithm) | `"RankExpr"`                                  |

### `group_by`

`group_by` can be omitted or provided as a dictionary with both `keys` and
`aggregate`.

```json theme={null}
{
  "group_by": {
    "keys": ["metadata_field", "... (min 1)"],
    "aggregate": {
      "$min_k": { // Or $max_k
        "keys": ["metadata_field_or_#score", "... (min 1)"],
        "k": "positive integer"
      }
    }
  }
}
```

### `limit`

Controls pagination.

```json theme={null}
{
  "limit": {
    "limit": 10, (optional, default 0)
    "offset": 20 (optional)
  }
}
```

### `select`

Controls returned fields. Use built-ins (`#id`, `#document`, `#embedding`,
`#metadata`, `#score`) and/or metadata field names.

```json theme={null}
{
  "select": {
    "keys": ["#id", "#document", "#metadata", "#score", "author"]
  }
}
```
