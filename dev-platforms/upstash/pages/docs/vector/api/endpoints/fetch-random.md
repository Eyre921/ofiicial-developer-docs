---
title: "Fetch Random Vector"
source: https://upstash.com/docs/vector/api/endpoints/fetch-random
path: docs/vector/api/endpoints/fetch-random
---

> Fetches a random vector.

`GET https://{endpoint}/random/{namespace}`

## Request

This endpoint doesn't require any additional data.

## Path

<ParamField path="namespace" type="string" default="">
  The namespace to use.
  When no namespace is specified, the default namespace will be used.
</ParamField>

## Response

The response will be `null` if the namespace is empty.

<ResponseField name="id" type="string" required>
  The id of the vector.
</ResponseField>
<ResponseField name="vector" type="number[]">
  The dense vector value for dense and hybrid indexes.
</ResponseField>
<ResponseField name="sparseVector" type="Object[]">
  The sparse vector value for sparse and hybrid indexes.
  <Expandable defaultOpen="true">
    <ResponseField name="indices" type="number[]">
      Indices of the non-zero valued dimensions.
    </ResponseField>
    <ResponseField name="values" type="number[]">
      Values of the non-zero valued dimensions.
    </ResponseField>
  </Expandable>
</ResponseField>
