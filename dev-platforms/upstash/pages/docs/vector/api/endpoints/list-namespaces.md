---
title: "List Namespaces"
source: https://upstash.com/docs/vector/api/endpoints/list-namespaces
path: docs/vector/api/endpoints/list-namespaces
---

## Request

This endpoint doesn't require any additional data.

## Response

<ResponseField name="namespaces" type="string[]" required>
  Array of namespace names.

  <Note>Every index has at least one namespace called default namespace, whose name is the empty string `""`.</Note>
</ResponseField>

<RequestExample>

```sh curl
curl $UPSTASH_VECTOR_REST_URL/list-namespaces \
  -H "Authorization: Bearer $UPSTASH_VECTOR_REST_TOKEN"
```

</RequestExample>

<ResponseExample>

```json 200 OK
{
    "result": ["", "ns0", "ns1"]
}
```

</ResponseExample>
