---
title: "Retrieve Metrics"
source: https://resend.com/docs/api-reference/emails/get-metrics
path: docs/api-reference/emails/get-metrics
---

GET /emails/metrics
Retrieve account-level email metrics.

<Note>
  Metrics are retained according to your plan's data retention window.
  Requesting a `start_date` older than your retention window returns data
  clamped to the oldest date your plan retains. This doesn't apply when
  `broadcast_id` is set.
</Note>

<Note>
  Responses are cached for up to 15 minutes, so a request for the same range may
  return slightly stale data within that window.
</Note>

## Query Parameters

<ListParamFormatNote />

<ParamField type="string">
  The start of the date range, as an ISO 8601 date (`2026-07-01`) or datetime
  (`2026-07-01T00:00:00Z`). Must be on or before `end_date`. Defaults to 6 days
  before `end_date`.
</ParamField>

<ParamField type="string">
  The end of the date range, as an ISO 8601 date or datetime. Values in the
  future are clamped to the current time. Defaults to now.
</ParamField>

<ParamField type="string">
  The IANA timezone (e.g. `America/New_York`) used to bucket periods when
  `period` is in `dimensions`.
</ParamField>

<ParamField type="hourly | daily | weekly | monthly">
  The bucket size used when `period` is in `dimensions`. Accepted but has no
  effect otherwise. The date range can't produce more than 10,000 periods at the
  chosen granularity. This limit only applies when `period` is in `dimensions`.
</ParamField>

<ParamField type="string[]">
  List of metrics to include in the response. Defaults to all of the
  following:

  `received`, `delivered`, `complained`, `suppressed`, `bounced`,
  `bounced_transient`, `bounced_permanent`, `bounced_undetermined`, `opened`,
  `clicked`, `unsubscribed`, `delivery_delayed`, `failed`, `sent`,
  `unique_opened`, `unique_clicked`, `delivery_rate`, `open_rate`, `click_rate`,
  `bounce_rate`, `complaint_rate`, `unsubscribe_rate`
</ParamField>

<ParamField type="string[]">
  List of dimensions to break the response down by. Combine
  any of `period`, `domain`, `email`, or `broadcast` to group the data by
  more than one at once, except `email` cannot be combined with `broadcast`.
  Defaults to `[]`, returning a single `totals` row for the whole range, with
  no `data`.

  Possible values:

  * `period`: groups the data by `granularity` period, in chronological order.
  * `domain`: groups the data by sending domain.
  * `email`: groups the data by email. Cannot be combined with `broadcast`.
  * `broadcast`: groups the data by broadcast. Cannot be combined with `email`.
</ParamField>

<ParamField type="string[]">
  List of sending domain IDs to restrict the response to, up to 100.
</ParamField>

<ParamField type="string[]">
  List of email IDs to restrict the response to, up to 100. Cannot be combined
  with the `broadcast` dimension or `broadcast_id`.
</ParamField>

<ParamField type="string[]">
  List of broadcast IDs to restrict the response to, up to 100. Cannot be
  combined with the `email` dimension or `email_id`.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  const { data } = await resend.emails.metrics({
    startDate: '2026-07-01',
    endDate: '2026-07-08',
    dimensions: ['period', 'broadcast'],
    broadcastId: ['5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a'],
  });
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  params: resend.Emails.MetricsParams = {
    "start_date": "2026-07-01",
    "end_date": "2026-07-08",
    "dimensions": ["period", "broadcast"],
    "broadcast_id": ["5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a"],
  }

  metrics = resend.Emails.metrics(params)
  print(metrics)
  ```

  ```rb Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  params = {
    start_date: "2026-07-01",
    end_date: "2026-07-08",
    dimensions: ["period", "broadcast"],
    broadcast_id: ["5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a"]
  }

  metrics = Resend::Emails.metrics(params)
  puts metrics
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import (
  	"context"
  	"fmt"

  	"github.com/resend/resend-go/v3"
  )

  func main() {
    ctx := context.TODO()
    client := resend.NewClient("re_xxxxxxxxx")

    startDate := "2026-07-01"
    endDate := "2026-07-08"

    metrics, err := client.Emails.MetricsWithOptions(ctx, &resend.MetricsOptions{
      StartDate: &startDate,
      EndDate:   &endDate,
      Dimensions: []resend.MetricsDimension{
        resend.MetricsDimensionPeriod,
        resend.MetricsDimensionBroadcast,
      },
      BroadcastId: []string{"5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a"},
    })

    if err != nil {
      panic(err)
    }
    fmt.Println(metrics.Totals)
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::types::GetEmailMetricsOptions;
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let options = GetEmailMetricsOptions::default()
      .with_start_date("2026-07-01")
      .with_end_date("2026-07-08")
      .with_period_dimension()
      .with_broadcast_dimension()
      .with_broadcast_id("5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a");

    let _metrics = resend.emails.metrics(options).await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;
  import com.resend.services.emails.model.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          GetEmailsMetricsOptions options = GetEmailsMetricsOptions.builder()
                  .startDate("2026-07-01")
                  .endDate("2026-07-08")
                  .dimensions(MetricsDimension.PERIOD, MetricsDimension.BROADCAST)
                  .broadcastIds("5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a")
                  .build();

          EmailsMetricsResponse metrics = resend.emails().metrics(options);
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" );

  var resp = await resend.EmailMetricsAsync( new EmailMetricsQuery()
  {
      StartDate = new DateTime( 2026, 7, 1 ),
      EndDate = new DateTime( 2026, 7, 8 ),
      Dimensions = new List<MetricDimension> { MetricDimension.Period, MetricDimension.Broadcast },
      BroadcastId = new List<Guid> { Guid.Parse( "5a5a3b1e-3b1a-4b1a-8b1a-3b1a4b1a8b1a" ) },
  } );
  Console.WriteLine( "Totals={0}", resp.Content?.Totals );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/emails/metrics?start_date=2026-07-01&end_date=2026-07-08&metrics=sent,delivered,open_rate&dimensions=period,domain' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "metrics",
    "start_date": "2026-07-01T00:00:00.000Z",
    "end_date": "2026-07-08T00:00:00.000Z",
    "metrics": ["sent", "delivered", "open_rate"],
    "dimensions": ["period", "domain"],
    "granularity": "daily",
    "totals": {
      "sent": 1204,
      "delivered": 1180,
      "open_rate": 50.0
    },
    "data": [
      {
        "period": "2026-07-01",
        "domain_id": "d91cd9bd-1176-4f47-2a4b-fce2d5399cbf",
        "domain_name": "example.com",
        "sent": 172,
        "delivered": 169,
        "open_rate": 49.7
      }
    ]
  }
  ```
</ResponseExample>
