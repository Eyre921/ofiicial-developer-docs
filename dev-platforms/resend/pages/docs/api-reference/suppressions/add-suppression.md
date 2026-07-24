---
title: "Add Suppression"
source: https://resend.com/docs/api-reference/suppressions/add-suppression
path: docs/api-reference/suppressions/add-suppression
---

POST /suppressions
Add an email address to the suppression list.

## Body Parameters

<ParamField type="string">
  The email address to suppress.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.suppressions.add({
    email: 'steve.wozniak@example.com',
  });
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::types::AddSuppressionOptions;
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let opts = AddSuppressionOptions::new().with_email("steve.wozniak@example.com");
    let _data = resend.suppressions.add(opts).await?;

    Ok(())
  }
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->suppressions->add([
    'email' => 'steve.wozniak@example.com',
  ]);
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/suppressions' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "email": "steve.wozniak@example.com"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend suppressions add steve.wozniak@example.com
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "suppression",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3"
  }
  ```
</ResponseExample>
