---
title: "List Automations"
source: https://resend.com/docs/api-reference/automations/list-automations
path: docs/api-reference/automations/list-automations
---

GET /automations
Retrieve a list of automations.

<QueryParams type="automations" />

<ResendParamField type="string">
  Filter automations by status. Possible values: `enabled`, `disabled`.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.automations.list();
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->automations->list();
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  resend.Automations.list()
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  Resend::Automations.list
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Automations.List()
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{list_opts::ListOptions, Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _automations = resend.automations.list(ListOptions::default()).await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          ListAutomationsResponseSuccess data = resend.automations().list();
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" );

  var resp = await resend.AutomationListAsync();
  Console.WriteLine( "Count={0}", resp.Content.Data.Count );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/automations' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend automations list
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd",
        "name": "Welcome series",
        "status": "enabled",
        "created_at": "2026-10-01 12:00:00.000000+00",
        "updated_at": "2026-10-01 12:00:00.000000+00"
      },
      {
        "id": "662892b2-4270-4130-a186-33a19752319d",
        "name": "Re-engagement",
        "status": "disabled",
        "created_at": "2026-09-15 08:30:00.000000+00",
        "updated_at": "2026-09-20 14:00:00.000000+00"
      }
    ]
  }
  ```
</ResponseExample>
