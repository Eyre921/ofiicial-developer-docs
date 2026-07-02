---
title: "Search"
source: https://docs.trychroma.com/reference/typescript/search
path: reference/typescript/search
---

## Search

<ParamField type="WhereInput" />

<ParamField type="RankInput" />

<ParamField type="GroupByInput | undefined" />

<ParamField type="LimitInput" />

<ParamField type="SelectInput" />

***

## Select

<ParamField type="Iterable<SelectKeyInput>" />

***

## Knn

<span>Properties</span>

<ParamField type="string | SparseVector | IterableInput<number>" />

<ParamField type="string | Key | undefined" />

<ParamField type="number | undefined" />

<ParamField type="number | null | undefined" />

<ParamField type="boolean | undefined" />

***

## Rrf

<span>Properties</span>

<ParamField type="RankInput[]" />

<ParamField type="number | undefined" />

<ParamField type="Embedding | undefined" />

<ParamField type="boolean | undefined" />

***

## Group By

### GroupBy

<ParamField type="Key[]" />

<ParamField type="Aggregate" />

### MinK

<ParamField type="Key[]" />

<ParamField type="number" />

### MaxK

<ParamField type="Key[]" />

<ParamField type="number" />

***

## Group By

### Limit

<span>Properties</span>

<ParamField type="number" />

<ParamField type="number | undefined" />

<span>Methods</span>

`from()`, `toJSON()`

***

## SearchResult

<span>Properties</span>

<ParamField type="string[][]" />

<ParamField type="((string | null)[] | null)[]" />

<ParamField type="((Embedding | null)[] | null)[]" />

<ParamField type="((Metadata | null)[] | null)[]" />

<ParamField type="((number | null)[] | null)[]" />

<ParamField type="Key[][]" />
