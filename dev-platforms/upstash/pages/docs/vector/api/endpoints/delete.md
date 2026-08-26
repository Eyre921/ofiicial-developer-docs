---
title: "Delete Vectors"
source: https://upstash.com/docs/vector/api/endpoints/delete
path: docs/vector/api/endpoints/delete
---

> Deletes the vectors with the given ids.

`DELETE https://{endpoint}/delete/{namespace}`

You can delete one or more vectors by providing their vector ids,
vector id prefix, or metadata filter.

<Tip>
  Vectors will be deleted from the default namespace by default.
  You can use a different namespace by specifying it in the request path.
</Tip>

## Request

<ParamField body="ids" type="string[]">
  Array of vector ids to delete.
</ParamField>

<ParamField body="prefix" type="string">
  Prefix of vector ids to delete.
</ParamField>

<ParamField body="filter" type="string">
  [Metadata filter](/vector/features/filtering) for the vectors to delete.
  <Warning>Deleting vectors with metadata filter is a O(N) operation that performs a full scan.
  Therefore, it might be slow for large indexes.</Warning>
</ParamField>

## Path

<ParamField path="namespace" type="string" default="">
  The namespace to use.
  When no namespace is specified, the default namespace will be used.
</ParamField>

## Response

<ResponseField name="deleted" type="number">
  The number of the successfully deleted vectors.
</ResponseField>
