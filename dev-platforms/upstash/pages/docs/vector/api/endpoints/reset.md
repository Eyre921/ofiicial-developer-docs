---
title: "Reset Namespace(s)"
source: https://upstash.com/docs/vector/api/endpoints/reset
path: docs/vector/api/endpoints/reset
---

> Resets one or all namespaces of an index to its initial state by deleting all the vectors.

`DELETE https://{endpoint}/reset/{namespace}`

The namespace will be completely empty after `/reset` is called, but will not be deleted.

<Tip>
  Reset operation will be performed against the default namespace by default.
  You can use a different namespace by specifying it in the request path.
</Tip>

## Request

This request doesn't require any additional data.

## Query

<ParamField query="all" type="string">
  When given, resets all namespaces of an index.
</ParamField>

## Path

<ParamField path="namespace" type="string" default="">
  The namespace to use.
  When no namespace is specified, the default namespace will be used.
</ParamField>

## Response

<ResponseField name="result" type="string">
  `"Success"` string.
</ResponseField>
