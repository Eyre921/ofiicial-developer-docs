---
title: "Group By & Aggregation"
source: https://docs.trychroma.com/cloud/search-api/group-by
path: cloud/search-api/group-by
---

Learn how to group search results by metadata keys and select the top results from each group. GroupBy is useful for diversifying results, deduplication, and category-aware ranking.

<Callout>
  GroupBy currently requires a ranking expression to be specified. Support for grouping without ranking is planned for a future release.
</Callout>

## How Grouping Works

GroupBy organizes ranked results into groups based on metadata keys, then performs aggregation on each group. Currently, aggregation supports `MinK` and `MaxK`, which select the top k results from each group based on the specified sorting keys.

After grouping and aggregation, results from all groups are flattened and sorted by score. The `limit()` method operates on this flattened list.

<CodeGroup>
  ```python Python theme={null}
  from chromadb import Search, K, Knn, GroupBy, MinK

  # Get top 3 results per category, ordered by score
  search = (Search()
      .rank(Knn(query="machine learning research"))
      .group_by(GroupBy(
          keys=K("category"),
          aggregate=MinK(keys=K.SCORE, k=3)
      ))
      .limit(30)
      .select(K.DOCUMENT, K.SCORE, "category"))

  results = collection.search(search)
  ```

  ```typescript TypeScript theme={null}
  import { Search, K, Knn, GroupBy, MinK } from 'chromadb';

  // Get top 3 results per category, ordered by score
  const search = new Search()
    .rank(Knn({ query: "machine learning research" }))
    .groupBy(new GroupBy(
      [K("category")],
      new MinK([K.SCORE], 3)
    ))
    .limit(30)
    .select(K.DOCUMENT, K.SCORE, "category");

  const results = await collection.search(search);
  ```

  ```rust Rust theme={null}
  use chroma::types::{Aggregate, GroupBy, Key, QueryVector, RankExpr, SearchPayload};

  let search = SearchPayload::default()
      .rank(RankExpr::Knn {
          query: QueryVector::Dense(vec![0.1, 0.2, 0.3]),
          key: Key::Embedding,
          limit: 16,
          default: None,
          return_rank: false,
      })
      .group_by(GroupBy {
          keys: vec![Key::field("category")],
          aggregate: Some(Aggregate::MinK {
              keys: vec![Key::Score],
              k: 3,
          }),
      })
      .limit(Some(30), 0)
      .select([Key::Document, Key::Score, Key::field("category")]);

  let results = collection.search(vec![search]).await?;
  ```
</CodeGroup>

## The GroupBy Class

The `GroupBy` class specifies how to partition results and which records to keep from each partition.

<CodeGroup>
  ```python Python theme={null}
  from chromadb import GroupBy, MinK, K

  # Single grouping key
  GroupBy(
      keys=K("category"),
      aggregate=MinK(keys=K.SCORE, k=3)
  )

  # Multiple grouping keys
  GroupBy(
      keys=[K("category"), K("year")],
      aggregate=MinK(keys=K.SCORE, k=1)
  )
  ```

  ```typescript TypeScript theme={null}
  import { GroupBy, MinK, K } from 'chromadb';

  // Single grouping key
  new GroupBy(
    [K("category")],
    new MinK([K.SCORE], 3)
  );

  // Multiple grouping keys
  new GroupBy(
    [K("category"), K("year")],
    new MinK([K.SCORE], 1)
  );
  ```
</CodeGroup>

## GroupBy Parameters

| Parameter | Type | Description |
| - | - | - |
| `keys` | Key or List\[Key] | Metadata key(s) to group by |
| `aggregate` | MinK or MaxK | Aggregation function to select top k records within each group |

## Aggregation Functions

### MinK

Keeps the k records with the **smallest** values for the specified keys. Use `MinK` when lower values are better (e.g., distance scores, prices, priorities).

<CodeGroup>
  ```python Python theme={null}
  from chromadb import MinK, K

  # Keep 3 records with lowest scores per group
  MinK(keys=K.SCORE, k=3)

  # Keep 2 records with lowest priority, then lowest score as tiebreaker
  MinK(keys=[K("priority"), K.SCORE], k=2)
  ```

  ```typescript TypeScript theme={null}
  import { MinK, K } from 'chromadb';

  // Keep 3 records with lowest scores per group
  new MinK([K.SCORE], 3);

  // Keep 2 records with lowest priority, then lowest score as tiebreaker
  new MinK([K("priority"), K.SCORE], 2);
  ```
</CodeGroup>

| Parameter | Type | Description |
| - | - | - |
| `keys` | Key or List\[Key] | Key(s) to sort by in ascending order |
| `k` | int | Number of records to keep from each group |

### MaxK

Keeps the k records with the **largest** values for the specified keys. Use `MaxK` when higher values are better (e.g., ratings, relevance scores, dates).

<CodeGroup>
  ```python Python theme={null}
  from chromadb import MaxK, K

  # Keep 3 records with highest ratings per group
  MaxK(keys=K("rating"), k=3)

  # Keep 2 records with highest year, then highest rating as tiebreaker
  MaxK(keys=[K("year"), K("rating")], k=2)
  ```

  ```typescript TypeScript theme={null}
  import { MaxK, K } from 'chromadb';

  // Keep 3 records with highest ratings per group
  new MaxK([K("rating")], 3);

  // Keep 2 records with highest year, then highest rating as tiebreaker
  new MaxK([K("year"), K("rating")], 2);
  ```
</CodeGroup>

| Parameter | Type | Description |
| - | - | - |
| `keys` | Key or List\[Key] | Key(s) to sort by in descending order |
| `k` | int | Number of records to keep from each group |

## Key References

Use `K.SCORE` to reference the search score, or `K("field_name")` for metadata fields.

<CodeGroup>
  ```python Python theme={null}
  from chromadb import K

  # Built-in score key
  K.SCORE  # References "#score" - the search/ranking score

  # Metadata field keys
  K("category")   # References the "category" metadata field
  K("priority")   # References the "priority" metadata field
  K("year")       # References the "year" metadata field
  ```

  ```typescript TypeScript theme={null}
  import { K } from 'chromadb';

  // Built-in score key
  K.SCORE;  // References "#score" - the search/ranking score

  // Metadata field keys
  K("category");   // References the "category" metadata field
  K("priority");   // References the "priority" metadata field
  K("year");       // References the "year" metadata field
  ```
</CodeGroup>

## Common Patterns

### Single Key Grouping

Group by one metadata field and keep the top results from each group.

<CodeGroup>
  ```python Python theme={null}
  # Top 2 articles per category by relevance
  search = (Search()
      .rank(Knn(query="climate change impacts"))
      .group_by(GroupBy(
          keys=K("category"),
          aggregate=MinK(keys=K.SCORE, k=2)
      ))
      .limit(20))
  ```

  ```typescript TypeScript theme={null}
  // Top 2 articles per category by relevance
  const search = new Search()
    .rank(Knn({ query: "climate change impacts" }))
    .groupBy(new GroupBy(
      [K("category")],
      new MinK([K.SCORE], 2)
    ))
    .limit(20);
  ```
</CodeGroup>

### Multiple Key Grouping

Group by combinations of metadata fields for finer-grained control.

<CodeGroup>
  ```python # Fork collection
Source: https://docs.trychroma.com/api-reference/collection/fork-collection

https://api.trychroma.com/openapi.json post /api/v2/tenants/{tenant}/databases/{database}/collections/{collection_id}/fork
Creates a fork of an existing collection.
