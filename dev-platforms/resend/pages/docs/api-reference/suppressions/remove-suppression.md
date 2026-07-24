---
title: "Remove Suppression"
source: https://resend.com/docs/api-reference/suppressions/remove-suppression
path: docs/api-reference/suppressions/remove-suppression
---

DELETE /suppressions/:suppression
Remove a single suppression by ID or email.

## Path Parameters

<ParamField type="email | id">
  The Suppression ID or email address.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  // Remove by suppression id
  const { data, error } = await resend.suppressions.remove(
    'e169aa45-1ecf-4183-9955-b1499d5701d3',
  );

  // Remove by email
  const { data, error } = await resend.suppressions.remove(
    'steve.wozniak@example.com',
  );
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    // Remove by suppression id
    let _data = resend
      .suppressions
      .remove("e169aa45-1ecf-4183-9955-b1499d5701d3")
      .await?;

    // Remove by email
    let _data = resend
      .suppressions
      .remove("steve.wozniak@example.com")
      .await?;

    Ok(())
  }
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  // Remove by suppression id
  $resend->suppressions->remove(
    'e169aa45-1ecf-4183-9955-b1499d5701d3'
  );

  // Remove by email
  $resend->suppressions->remove(
    'steve.wozniak@example.com'
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by suppression id
  curl -X DELETE 'https://api.resend.com/suppressions/e169aa45-1ecf-4183-9955-b1499d5701d3' \
       -H 'Authorization: Bearer re_xxxxxxxxx'

  # Remove by email
  curl -X DELETE 'https://api.resend.com/suppressions/steve.wozniak@example.com' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by suppression id
  resend suppressions delete e169aa45-1ecf-4183-9955-b1499d5701d3

  # Remove by email
  resend suppressions delete steve.wozniak@example.com
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "suppression",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
    "deleted": true
  }
  ```
</ResponseExample>
