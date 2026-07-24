---
title: "Add Suppressions"
source: https://resend.com/docs/api-reference/suppressions/add-suppressions
path: docs/api-reference/suppressions/add-suppressions
---

POST /suppressions/batch/add
Add up to 100 email addresses to the suppression list at once.

## Body Parameters

<ParamField type="array">
  The email addresses to suppress. Must contain between 1 and 100 email
  addresses.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.suppressions.batch.add({
    emails: ['steve.wozniak@example.com', 'susan.kare@example.com'],
  });
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::types::BatchAddSuppressionOptions;
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let opts =
      BatchAddSuppressionOptions::from(vec!["steve.wozniak@example.com", "susan.kare@example.com"]);
    let _data = resend.suppressions.batch_add(opts).await?;

    Ok(())
  }
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->suppressions->batch->add([
    'emails' => ['steve.wozniak@example.com', 'susan.kare@example.com'],
  ]);
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/suppressions/batch/add' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "emails": ["steve.wozniak@example.com", "susan.kare@example.com"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend suppressions batch add --file suppressions.json
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "data": [
      {
        "object": "suppression",
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3"
      },
      {
        "object": "suppression",
        "id": "520784e2-887d-4c25-b53c-4ad46ad38100"
      }
    ]
  }
  ```
</ResponseExample>
