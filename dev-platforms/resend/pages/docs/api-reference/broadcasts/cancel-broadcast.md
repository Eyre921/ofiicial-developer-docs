---
title: "Cancel Broadcast"
source: https://resend.com/docs/api-reference/broadcasts/cancel-broadcast
path: docs/api-reference/broadcasts/cancel-broadcast
---

POST /broadcasts/:broadcast_id/cancel
Cancel a queued or scheduled broadcast.

You can only cancel Broadcasts that are `queued` or `scheduled`. Canceling a `queued` Broadcast stops it mid-send. Any emails already sent are not affected, but no further emails will go out.

## Path Parameters

<ResendParamField type="string">
  The broadcast ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.broadcasts.cancel(
    '559ac32e-9ef5-46fb-82a1-b76b840c0f7b',
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/broadcasts/559ac32e-9ef5-46fb-82a1-b76b840c0f7b/cancel' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "broadcast",
    "id": "559ac32e-9ef5-46fb-82a1-b76b840c0f7b"
  }
  ```
</ResponseExample>
