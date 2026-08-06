---
title: "List Segment Contacts"
source: https://resend.com/docs/api-reference/segments/list-segment-contacts
path: docs/api-reference/segments/list-segment-contacts
---

GET /segments/:segment_id/contacts
Retrieve a list of contacts in a segment.

## Path Parameters

<ResendParamField type="string">
  The Segment ID.
</ResendParamField>

<QueryParams type="contacts" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.contacts.list({
    segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf',
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->contacts->list([
    'segment_id' => '78261eea-8f8b-4381-83c6-79fa7120f1cf',
  ]);
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = 're_xxxxxxxxx'

  contacts = resend.Contacts.list('78261eea-8f8b-4381-83c6-79fa7120f1cf')
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _contacts = resend
      .contacts
      .list("78261eea-8f8b-4381-83c6-79fa7120f1cf", ListOptions::default())
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          ListContactsResponseSuccess response = resend.contacts().list("78261eea-8f8b-4381-83c6-79fa7120f1cf");
      }
  }
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/segments/78261eea-8f8b-4381-83c6-79fa7120f1cf/contacts' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend segments contacts 78261eea-8f8b-4381-83c6-79fa7120f1cf
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "email": "steve.wozniak@gmail.com",
        "first_name": "Steve",
        "last_name": "Wozniak",
        "created_at": "2026-10-06 23:47:56.678+00",
        "unsubscribed": false
      }
    ]
  }
  ```
</ResponseExample>
