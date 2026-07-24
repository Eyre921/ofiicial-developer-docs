---
title: "Remove Suppressions"
source: https://resend.com/docs/api-reference/suppressions/remove-suppressions
path: docs/api-reference/suppressions/remove-suppressions
---

POST /suppressions/batch/remove
Remove up to 100 suppressions from the suppression list at once.

## Body Parameters

Provide either `emails` or `ids`, but not both.

<ParamField type="array">
  The email addresses to remove from the suppression list. Must contain between
  1 and 100 email addresses.
</ParamField>

<ParamField type="array">
  The suppression IDs to remove from the suppression list. Must contain between
  1 and 100 IDs.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  // Remove by suppression ids
  const { data, error } = await resend.suppressions.batch.remove({
    ids: ['e169aa45-1ecf-4183-9955-b1499d5701d3'],
  });

  // Remove by emails
  const { data, error } = await resend.suppressions.batch.remove({
    emails: ['steve.wozniak@example.com', 'susan.kare@example.com'],
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  // Remove by suppression ids
  $resend->suppressions->batch->remove([
    'ids' => ['e169aa45-1ecf-4183-9955-b1499d5701d3'],
  ]);

  // Remove by emails
  $resend->suppressions->batch->remove([
    'emails' => ['steve.wozniak@example.com', 'susan.kare@example.com'],
  ]);
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result, types::BatchRemoveSuppressionOptions};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    // Remove by email
    let opt_emails = BatchRemoveSuppressionOptions::new()
      .add_emails(vec!["steve.wozniak@example.com", "susan.kare@example.com"]);
    let _data = resend.suppressions.batch_remove(opt_emails).await?;

    // Remove by id
    let opt_ids =
      BatchRemoveSuppressionOptions::new().add_ids(vec!["e169aa45-1ecf-4183-9955-b1499d5701d3"]);

    let _data = resend.suppressions.batch_remove(opt_ids).await?;

    Ok(())
  }
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by suppression ids
  curl -X POST 'https://api.resend.com/suppressions/batch/remove' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "ids": ["e169aa45-1ecf-4183-9955-b1499d5701d3"]
  }'

  # Remove by emails
  curl -X POST 'https://api.resend.com/suppressions/batch/remove' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "emails": ["steve.wozniak@example.com", "susan.kare@example.com"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by email
  resend suppressions batch remove --file suppressions.json

  # Remove by id
  resend suppressions batch remove --file suppression-ids.json --ids
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "data": [
      {
        "object": "suppression",
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "deleted": true
      }
    ]
  }
  ```
</ResponseExample>
