---
title: "List Namespaces"
source: https://upstash.com/docs/vector/api/endpoints/list-namespaces
path: docs/vector/api/endpoints/list-namespaces
---

> Lists the names of the namespaces of an index.

`GET https://{endpoint}/list-namespaces`

## Request

This endpoint doesn't require any additional data.

## Response

<ResponseField name="namespaces" type="string[]" required>
  Array of namespace names.

  <Note>Every index has at least one namespace called default namespace, whose name is the empty string `""`.</Note>
</ResponseField>
