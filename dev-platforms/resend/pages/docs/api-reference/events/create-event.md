---
title: "Create Event"
source: https://resend.com/docs/api-reference/events/create-event
path: docs/api-reference/events/create-event
---

POST /events
Create a new event that can be used to trigger automations.

## Body Parameters

<ParamField type="string">
  The name of the event. Used to match events to automation triggers.

  <Note>
    The event name can be any string (e.g., `user.created`, `welcome`,
    `my-custom-event`). Dot notation is a recommended convention but is not
    required. If multiple enabled automations use the same event name, all of them
    will be triggered. Use unique event names if you want to target a specific
    automation.
  </Note>

  <Warning>
    Event names cannot start with the `resend:` prefix, which is reserved for system events.
  </Warning>
</ParamField>

<ParamField type="object">
  An optional schema definition for the event payload. Must be an object with
  flat key/type pairs. Supported types: `string`, `number`, `boolean`, `date`.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.events.create({
    name: 'user.created',
    schema: {
      plan: 'string',
    },
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->events->create([
    'name' => 'user.created',
    'schema' => ['plan' => 'string'],
  ]);
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  params: resend.Events.CreateParams = {
    "name": "user.created",
    "schema": {
      "plan": "string",
    },
  }

  resend.Events.create(params)
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  params = {
    name: "user.created",
    schema: {
      plan: "string",
    },
  }

  Resend::Events.create(params)
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	params := &resend.CreateEventRequest{
  		Name: "user.created",
  		Schema: map[string]string{
  			"plan": resend.EventSchemaTypeString,
  		},
  	}

  	client.Events.Create(params)
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{json, types::CreateEventOptions, Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let opts = CreateEventOptions {
      name: "user.created".to_owned(),
      schema: json!({
        "plan": "string",
      }),
    };

    let _event = resend.events.create(opts).await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          CreateEventOptions params = CreateEventOptions.builder()
                  .name("user.created")
                  .addSchema("plan", "string")
                  .build();

          CreateEventResponseSuccess data = resend.events().create(params);
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;
  using System.Text.Json;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" );

  var schema = JsonSerializer.SerializeToElement( new { plan = "string" } );

  var resp = await resend.EventCreateAsync( new EventCreateData()
  {
      Name = "user.created",
      Schema = schema,
  } );
  Console.WriteLine( "EventId={0}", resp.Content );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/events' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d '{
    "name": "user.created",
    "schema": {
      "plan": "string"
    }
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend events create --name user.created --schema '{"plan":"string"}'
  ```
</RequestExample>

<Note>
  Successful creation returns **201 Created** with the JSON body below.
</Note>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "event",
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  }
  ```
</ResponseExample>
