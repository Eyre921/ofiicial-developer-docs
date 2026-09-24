---
title: "Replay Event"
source: https://resend.com/docs/api-reference/webhooks/replay-event
path: docs/api-reference/webhooks/replay-event
---

POST /webhooks/:webhook_id/events/:event_id/replay
Queue an additional delivery attempt for a webhook event.

<Note>
  Replaying an event queues one additional delivery immediately. It's the same
  action as the [dashboard's Replay
  button](/docs/webhooks/retries-and-replays#manual-replays) and does not affect the
  [automatic retry schedule](/docs/webhooks/retries-and-replays#automatic-retries)
  already running for that event.
</Note>

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

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.replay({
    eventId: 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $event = $resend->webhooks->events->replay(
      '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  );
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = 're_xxxxxxxxx'

  replayed = resend.Webhooks.replay_event(
      webhook_id='4dd369bc-aa82-4ff3-97de-514ae3000ee0',
      event_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
  )
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require 'resend'

  Resend.api_key = 're_xxxxxxxxx'

  replayed = Resend::Webhooks.replay_event(
    '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
    'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'
  )
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v4"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Webhooks.ReplayEvent(
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

    let _replayed = resend
      .webhooks
      .replay_event(
        "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
        "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
      )
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.Resend;
  import com.resend.core.exception.ResendException;
  import com.resend.services.webhooks.model.ReplayWebhookEventResponseSuccess;

  public class Main {
      public static void main(String[] args) throws ResendException {
          Resend resend = new Resend("re_xxxxxxxxx");

          ReplayWebhookEventResponseSuccess replayed = resend.webhooks().replayEvent(
              "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
              "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
          );
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.WebhookEventReplayAsync(
      new Guid( "4dd369bc-aa82-4ff3-97de-514ae3000ee0" ),
      "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events/msg_1srOrx2ZWZBpBUvZwXKQmoEYga2/replay' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "webhook_event",
    "id": "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"
  }
  ```
</ResponseExample>
