---
title: "List Suppressions"
source: https://resend.com/docs/api-reference/suppressions/list-suppressions
path: docs/api-reference/suppressions/list-suppressions
---

GET /suppressions
Show all suppressions.

<QueryParams type="suppressions" />

<ParamField type="bounce | complaint | manual">
  Filter suppressions by origin.

  Possible values:
  `bounce`: emails suppressed automatically after a bounce
  `complaint`: emails suppressed due to a user complaint
  `manual`: emails suppressed by your team manually
</ParamField>

The `source_id` in the response references the email that triggered the
suppression. For suppressions with a `manual` origin, `source_id` is `null`.

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.suppressions.list();
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result, list_opts::ListOptions};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _data = resend.suppressions.list(ListOptions::default()).await?;

    Ok(())
  }
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->suppressions->list();
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/suppressions' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend suppressions list
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "object": "suppression",
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "email": "steve.wozniak@example.com",
        "origin": "manual",
        "source_id": null,
        "created_at": "2026-10-06T23:47:56.678Z"
      },
      {
        "object": "suppression",
        "id": "520784e2-887d-4c25-b53c-4ad46ad38100",
        "email": "susan.kare@example.com",
        "origin": "bounce",
        "source_id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
        "created_at": "2026-10-07T08:12:03.412Z"
      }
    ]
  }
  ```
</ResponseExample>
