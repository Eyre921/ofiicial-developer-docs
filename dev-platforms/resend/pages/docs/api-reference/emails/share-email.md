---
title: "Share Email"
source: https://resend.com/docs/api-reference/emails/share-email
path: docs/api-reference/emails/share-email
---

POST /emails/:email_id/share
Create a shareable link to view a sent or received email.

## Path Parameters

<ResendParamField type="string">
  The Email ID.
</ResendParamField>

## Body Parameters

<ResendParamField type="string">
  How long the link stays valid for, as a duration like `10m`, `2 hours`, or `1
      day`. Defaults to `48h` and cannot exceed 48 hours.
</ResendParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/emails/49a3999c-0ce1-4ea6-ab68-afcd6dc2e794/share' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "expires_in": "2 hours"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "email",
    "id": "49a3999c-0ce1-4ea6-ab68-afcd6dc2e794",
    "url": "https://resend.com/shared?token=eyJhbGciOiJIUzI1NiJ9..."
  }
  ```
</ResponseExample>
