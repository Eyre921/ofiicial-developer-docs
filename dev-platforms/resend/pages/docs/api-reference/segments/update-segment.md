---
title: "Update Segment"
source: https://resend.com/docs/api-reference/segments/update-segment
path: docs/api-reference/segments/update-segment
---

PATCH /segments/:segment_id
Update an existing segment.

## Path Parameters

<ResendParamField type="string">
  The Segment ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  The name of the segment.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/segments/78261eea-8f8b-4381-83c6-79fa7120f1cf' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Active Users"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "segment",
    "id": "78261eea-8f8b-4381-83c6-79fa7120f1cf"
  }
  ```
</ResponseExample>
