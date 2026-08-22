---
title: "Update API key"
source: https://resend.com/docs/api-reference/api-keys/update-api-key
path: docs/api-reference/api-keys/update-api-key
---

PATCH /api-keys/:api_key_id
Update an existing API key.

## Path Parameters

<ResendParamField type="string">
  The API key ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  The API key name. Maximum 50 characters.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/api-keys/b6d24b8e-af0b-4c3c-be0c-359bbd97381e' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Production"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "api_key",
    "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e"
  }
  ```
</ResponseExample>
