---
title: "List Logs"
source: https://resend.com/docs/api-reference/logs/list-logs
path: docs/api-reference/logs/list-logs
---

GET /logs
Retrieve a list of API request logs.

<QueryParams type="logs" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.logs.list();
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->logs->list();
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  resend.Logs.list()
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  Resend.api_key = "re_xxxxxxxxx"

  logs = Resend::Logs.list
  puts logs
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import (
  	"context"

  	"github.com/resend/resend-go/v3"
  )

  func main() {
  	ctx := context.TODO()
  	client := resend.NewClient("re_xxxxxxxxx")

  	logs, err := client.Logs.ListWithOptions(ctx, nil)
  	if err != nil {
  		panic(err)
  	}

  	if logs.HasMore {
  		opts := &resend.ListOptions{
  			After: &logs.Data[len(logs.Data)-1].Id,
  		}
  		client.Logs.ListWithOptions(ctx, opts)
  	}
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result, list_opts::ListOptions};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _logs = resend
      .logs
      .list(ListOptions::default())
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          resend.logs().list();
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;
  using System.Linq;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.LogListAsync();
  Console.WriteLine( "Count={0}", resp.Content.Data.Count );

  if ( resp.Content.HasMore )
  {
      var lastId = resp.Content.Data.Last().Id;
      await resend.LogListAsync( new PaginatedQuery()
      {
          After = lastId.ToString(),
      } );
  }
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/logs' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend logs list
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "37e4414c-5e25-4dbc-a071-43552a4bd53b",
        "created_at": "2026-03-30 13:43:54.622865+00",
        "endpoint": "/emails",
        "method": "POST",
        "response_status": 200,
        "user_agent": "resend-node:6.0.3"
      },
      {
        "id": "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "created_at": "2026-03-30 12:15:00.123456+00",
        "endpoint": "/emails/4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
        "method": "GET",
        "response_status": 200,
        "user_agent": "curl/8.7.1"
      }
    ]
  }
  ```
</ResponseExample>
