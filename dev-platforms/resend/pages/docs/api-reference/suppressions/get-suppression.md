---
title: "Retrieve Suppression"
source: https://resend.com/docs/api-reference/suppressions/get-suppression
path: docs/api-reference/suppressions/get-suppression
---

GET /suppressions/:suppression
Retrieve a single suppression by ID or email.

A suppression can be retrieved either by its ID or by the suppressed email
address.

## Path Parameters

<ParamField type="email | id">
  The Suppression ID or email address.
</ParamField>

The `source_id` in the response references the email that triggered the
suppression. For suppressions with a `manual` origin, `source_id` is `null`.

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  // Retrieve by suppression id
  const { data, error } = await resend.suppressions.get(
    'e169aa45-1ecf-4183-9955-b1499d5701d3',
  );

  // Retrieve by email
  const { data, error } = await resend.suppressions.get(
    'steve.wozniak@example.com',
  );
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _data = resend
      .suppressions
      .get("e169aa45-1ecf-4183-9955-b1499d5701d3")
      .await?;

    Ok(())
  }
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  // Retrieve by suppression id
  $resend->suppressions->get(
    'e169aa45-1ecf-4183-9955-b1499d5701d3'
  );

  // Retrieve by email
  $resend->suppressions->get(
    'steve.wozniak@example.com'
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Retrieve by suppression id
  curl -X GET 'https://api.resend.com/suppressions/e169aa45-1ecf-4183-9955-b1499d5701d3' \
       -H 'Authorization: Bearer re_xxxxxxxxx'

  # Retrieve by email
  curl -X GET 'https://api.resend.com/suppressions/steve.wozniak@example.com' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Retrieve by suppression id
  resend suppressions get e169aa45-1ecf-4183-9955-b1499d5701d3

  # Retrieve by email
  resend suppressions get steve.wozniak@example.com
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "suppression",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
    "email": "steve.wozniak@example.com",
    "origin": "bounce",
    "source_id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
    "created_at": "2026-10-06T23:47:56.678Z"
  }
  ```
</ResponseExample>
