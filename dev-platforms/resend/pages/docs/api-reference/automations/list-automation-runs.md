---
title: "List Automation Runs"
source: https://resend.com/docs/api-reference/automations/list-automation-runs
path: docs/api-reference/automations/list-automation-runs
---

GET /automations/:automation_id/runs
Retrieve a list of automation runs.

## Path Parameters

<ResendParamField type="string">
  The automation ID.
</ResendParamField>

<QueryParams type="automation-runs" />

<ResendParamField type="string">
  Filter runs by status. Comma-separated list: `running`, `completed`, `failed`,
  `cancelled`.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.automations.runs.list({
    automationId: 'c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd',
    status: 'completed',
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->automations->runs->list('c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd');
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  resend.Automations.Runs.list("c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd")
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  Resend::Automations::Runs.list("c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd")
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Automations.ListRuns("c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd")
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{list_opts::ListOptions, Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _automation = resend
      .automations
      .list_runs(
        "c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd",
        None,
        ListOptions::default(),
      )
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          ListAutomationRunsResponseSuccess data = resend.automations().listRuns("c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd");
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" );

  var resp = await resend.AutomationRunListAsync( new Guid( "c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd" ) );
  Console.WriteLine( "Count={0}", resp.Content.Data.Count );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/automations/c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd/runs?status=completed' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend automations runs list c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "status": "completed",
        "started_at": "2026-10-01 12:00:00.000000+00",
        "completed_at": "2026-10-01 12:05:00.000000+00",
        "created_at": "2026-10-01 12:00:00.000000+00"
      },
      {
        "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
        "status": "running",
        "started_at": "2026-10-02 08:30:00.000000+00",
        "completed_at": null,
        "created_at": "2026-10-02 08:30:00.000000+00"
      }
    ]
  }
  ```
</ResponseExample>
