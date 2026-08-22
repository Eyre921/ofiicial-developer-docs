---
title: "Delete Event"
source: https://resend.com/docs/api-reference/events/delete-event
path: docs/api-reference/events/delete-event
---

DELETE /events/:id
Remove an existing event.

## Path Parameters

<ResendParamField type="string">
  The event ID or name.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.events.remove('user.created');
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->events->remove('user.created');
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  resend.Events.remove("user.created")
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  Resend::Events.remove("user.created")
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Events.Remove("user.created")
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _event = resend.events.delete("user.created").await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          RemoveEventResponseSuccess data = resend.events().remove("user.created");
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" );

  var resp = await resend.EventDeleteAsync( "user.created" );
  Console.WriteLine( "Deleted={0}", resp.Content.Deleted );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X DELETE 'https://api.resend.com/events/user.created' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend events delete user.created
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "event",
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "deleted": true
  }
  ```
</ResponseExample>
