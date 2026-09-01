---
title: "Retrieve Event"
source: https://resend.com/docs/api-reference/webhooks/get-event
path: docs/api-reference/webhooks/get-event
---

GET /webhooks/:webhook_id/events/:event_id
Retrieve the details of a single event delivered to a webhook.

## Path Parameters

<ResendParamField type="string">
  The Webhook ID.
</ResendParamField>

<ResendParamField type="string">
  The Webhook Event ID.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `webhook_event`.
</ParamField>

<ParamField type="string">
  The event ID.
</ParamField>

<ParamField type="string">
  The event type, for example `email.sent`.
</ParamField>

<ParamField type="string">
  When the event was created.
</ParamField>

<ParamField type="string">
  Delivery status of the event to this webhook: `success`, `failed`,
  `attempting`, or `pending`.
</ParamField>

<ParamField type="string | null">
  When the next delivery attempt is scheduled. `null` once the event reaches
  `success` or `failed`.
</ParamField>

<ParamField type="object">
  The event payload that was sent to your endpoint.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.get({
    eventId: 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $event = $resend->webhooks->events->get(
      '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  );
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = 're_xxxxxxxxx'

  event = resend.Webhooks.get_event(
      webhook_id='4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      event_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
  )
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require 'resend'

  Resend.api_key = 're_xxxxxxxxx'

  event = Resend::Webhooks.get_event(
    '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
    'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  )
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v4"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Webhooks.GetEvent(
  		"4dd369bc-aa82-4ff3-97de-514ae3000ee0",
  		"msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
  	)
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _event = resend
      .webhooks
      .get_event(
        "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
        "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
      )
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;
  import com.resend.core.exception.ResendException;
  import com.resend.services.webhooks.model.GetWebhookEventResponseSuccess;

  public class Main {
      public static void main(String[] args) throws ResendException {
          Resend resend = new Resend("re_xxxxxxxxx");

          GetWebhookEventResponseSuccess event = resend.webhooks().getEvent(
              "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
              "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
          );
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.WebhookEventRetrieveAsync(
      new Guid( "4dd369bc-aa82-4ff3-97de-514ae3000ee0" ),
      "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events/msg_1srOrx2ZWZBpBUvZwXKQmoEYga2' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "webhook_event",
    "id": "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    "type": "email.sent",
    "created_at": "2026-08-22T15:28:00.000Z",
    "status": "attempting",
    "next_attempt_at": "2026-08-22T15:33:00.000Z",
    "payload": {
      "type": "email.sent",
      "created_at": "2026-08-22T15:28:00.000Z",
      "data": {
        "email_id": "571f1f42-1c2d-4b1f-8f8e-8b3b5b3b5b3b",
        "from": "onboarding@resend.dev",
        "to": ["delivered@resend.dev"],
        "subject": "Welcome",
        "created_at": "2026-08-22T15:27:59.000Z"
      }
    }
  }
  ```
</ResponseExample>
