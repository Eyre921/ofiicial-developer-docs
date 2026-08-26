---
title: "Delete Namespace"
source: https://upstash.com/docs/vector/api/endpoints/delete-namespace
path: docs/vector/api/endpoints/delete-namespace
---

> Deletes a namespace of an index.

`DELETE https://{endpoint}/delete-namespace/{namespace}`

<Note>
  The default namespace, which is the empty string `""`, cannot be deleted.
</Note>

## Request

This endpoint doesn't require any additional data.

## Path

<ParamField path="namespace" type="string" required>
  The namespace to delete.
</ParamField>

## Response

<ResponseField name="result" type="string">
  `"Success"` string.
</ResponseField>
