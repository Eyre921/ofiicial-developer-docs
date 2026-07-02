---
title: "Delete Domain"
source: https://resend.com/docs/api-reference/domains/delete-domain
path: docs/api-reference/domains/delete-domain
---

DELETE /domains/:domain_id
Remove an existing domain.

<Warning>
  Removing a domain with a configured [custom tracking subdomain](/docs/dashboard/domains/tracking)
  will also remove the Resend provisioned proxy, breaking any existing email links that use that subdomain.

  To keep links working, set up your own proxy pointing to Resend’s tracking DNS records before removing the domain.
</Warning>

## Path Parameters

<ResendParamField type="string">
  The Domain ID.
</ResendParamField>

<RequestExample>
  ```js Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.domains.remove(
    'd91cd9bd-1176-453e-8fc1-35364d380206',
  );
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->domains->remove('d91cd9bd-1176-453e-8fc1-35364d380206');
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  resend.Domains.remove(domain_id="d91cd9bd-1176-453e-8fc1-35364d380206")
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  Resend.api_key = ENV["RESEND_API_KEY"]
  Resend::Domains.remove("d91cd9bd-1176-453e-8fc1-35364d380206")
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")

  	client.Domains.Remove("d91cd9bd-1176-453e-8fc1-35364d380206")
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _deleted = resend
      .domains
      .delete("d91cd9bd-1176-453e-8fc1-35364d380206")
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          RemoveDomainResponse removed = resend.domains().remove("d91cd9bd-1176-453e-8fc1-35364d380206");
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  await resend.DomainDeleteAsync( new Guid( "d91cd9bd-1176-453e-8fc1-35364d380206" ) );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X DELETE 'https://api.resend.com/domains/d91cd9bd-1176-453e-8fc1-35364d380206' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend domains delete d91cd9bd-1176-453e-8fc1-35364d380206
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "domain",
    "id": "d91cd9bd-1176-453e-8fc1-35364d380206",
    "deleted": true
  }
  ```
</ResponseExample>
