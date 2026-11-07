---
title: "Search"
source: https://docs.trychroma.com/reference/typescript/search
path: reference/typescript/search
---

## Search

**where** `WhereInput`

**rank** `RankInput`

**groupBy** `GroupByInput | undefined`

**limit** `LimitInput`

**select** `SelectInput`

***

## Select

**keys** `Iterable\<SelectKeyInput\>`

***

## Knn

Properties

**query** `string | SparseVector | IterableInput\<number\>`

**key** `string | Key | undefined`

**limit** `number | undefined`

**default** `number | null | undefined`

**returnRank** `boolean | undefined`

***

## Rrf

Properties

**ranks** `RankInput[]`

**k** `number | undefined`

**weights** `Embedding | undefined`

**normalize** `boolean | undefined`

***

## Group By

### GroupBy

**keys** `Key[]` *required*

**aggregate** `Aggregate` *required*

### MinK

**keys** `Key[]` *required*

**k** `number` *required*

### MaxK

**keys** `Key[]` *required*

**k** `number` *required*

***

## Group By

### Limit

Properties

**offset** `number`

**limit** `number | undefined`

Methods

`from()`, `toJSON()`

***

## SearchResult

Properties

**ids** `string[][]`

**documents** `((string | null)[] | null)[]`

**embeddings** `((Embedding | null)[] | null)[]`

**metadatas** `((Metadata | null)[] | null)[]`

**scores** `((number | null)[] | null)[]`

**select** `Key[][]`
