---
title: "List Attempts"
source: https://resend.com/docs/api-reference/webhooks/list-event-attempts
path: docs/api-reference/webhooks/list-event-attempts
---

GET /webhooks/:webhook_id/events/:event_id/attempts
Retrieve the delivery attempts for a single webhook event.

## Path Parameters

<ResendParamField type="string">
  The Webhook ID.
</ResendParamField>

<ResendParamField type="string">
  The Webhook Event ID.
</ResendParamField>

## Query Parameters

<ParamField type="number">
  Number of attempts to return. Between `1` and `100`. Defaults to `20`.
</ParamField>

<ParamField type="string">
  The attempt ID to fetch the next page after.

  The `before` parameter is not supported for this endpoint.
</ParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more attempts exist beyond this page.
</ParamField>

<ParamField type="array">
  The delivery attempts for this event, most recent first.

  <Expandable title="properties">
    <ParamField type="string">
      The attempt ID.
    </ParamField>

    <ParamField type="number">
      The HTTP status code your endpoint returned for this attempt.
    </ParamField>

    <ParamField type="string">
      The response body your endpoint returned for this attempt.
    </ParamField>

    <ParamField type="string">
      When this attempt was sent.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.attempts.list({
    eventId: 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $attempts = $resend->webhooks->events->attempts->list(
      '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  );
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = 're_xxxxxxxxx'

  attempts = resend.Webhooks.list_event_attempts(
      webhook_id='4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      event_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
  )
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require 'resend'

  Resend.api_key = 're_xxxxxxxxx'

  attempts = Resend::Webhooks.list_event_attempts(
    '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
    'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  )
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v4"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Webhooks.ListEventAttempts(
  		"4dd369bc-aa82-4ff3-97de-514ae3000ee0",
  		"msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
  	)
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{list_opts::ListOptions, Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _attempts = resend
      .webhooks
      .list_event_attempts(
        "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
        "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        ListOptions::default(),
      )
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;
  import com.resend.core.exception.ResendException;
  import com.resend.services.webhooks.model.ListWebhookEventAttemptsResponseSuccess;

  public class Main {
      public static void main(String[] args) throws ResendException {
          Resend resend = new Resend("re_xxxxxxxxx");

          ListWebhookEventAttemptsResponseSuccess attempts = resend.webhooks().listEventAttempts(
              "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
              "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
          );
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.WebhookEventAttemptListAsync(
      new Guid( "4dd369bc-aa82-4ff3-97de-514ae3000ee0" ),
      "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events/msg_1srOrx2ZWZBpBUvZwXKQmoEYga2/attempts' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        "http_status_code": 200,
        "response": "{\"ok\":true}",
        "sent_at": "2026-08-22T15:33:12.000Z"
      },
      {
        "id": "atmpt_2ZbUCwvGmIT4mLIN6d3Yz0Ainbd",
        "http_status_code": 500,
        "response": "Internal Server Error",
        "sent_at": "2026-08-22T15:28:05.000Z"
      }
    ]
  }
  ```
</ResponseExample>
