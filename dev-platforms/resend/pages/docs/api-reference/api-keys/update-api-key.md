---
title: "Update API key"
source: https://resend.com/docs/api-reference/api-keys/update-api-key
path: docs/api-reference/api-keys/update-api-key
---

PATCH /api-keys/:api_key_id
Update an existing API key.

## Path Parameters

<ResendParamField type="string">
  The API key ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  The API key name. Maximum 50 characters.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.apiKeys.update(
    'b6d24b8e-af0b-4c3c-be0c-359bbd97381e',
    { name: 'Production' },
  );
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  $resend = Resend::client('re_xxxxxxxxx');

  $resend->apiKeys->update('b6d24b8e-af0b-4c3c-be0c-359bbd97381e', [
    'name' => 'Production'
  ]);
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = "re_xxxxxxxxx"

  params: resend.ApiKeys.UpdateParams = {
    "api_key_id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
    "name": "Production",
  }

  resend.ApiKeys.update(params)
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  params = {
    id: "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
    name: "Production"
  }
  Resend::ApiKeys.update(params)
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import "github.com/resend/resend-go/v3"

  func main() {
  	client := resend.NewClient("re_xxxxxxxxx")
  	params := &resend.UpdateApiKeyRequest{
  		Name: "Production",
  	}
  	client.ApiKeys.Update("b6d24b8e-af0b-4c3c-be0c-359bbd97381e", params)
  }
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{types::UpdateApiKeyOptions, Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _api_key = resend
      .api_keys
      .update(
        "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
        UpdateApiKeyOptions::new("Production"),
      )
      .await?;

    Ok(())
  }
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  import com.resend.*;

  public class Main {
      public static void main(String[] args) {
          Resend resend = new Resend("re_xxxxxxxxx");

          UpdateApiKeyOptions params = UpdateApiKeyOptions
                  .builder()
                  .name("Production").build();

          UpdateApiKeyResponseSuccess apiKey = resend.apiKeys().update("b6d24b8e-af0b-4c3c-be0c-359bbd97381e", params);
      }
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.ApiKeyUpdateAsync( new Guid( "b6d24b8e-af0b-4c3c-be0c-359bbd97381e" ), "Production" );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/api-keys/b6d24b8e-af0b-4c3c-be0c-359bbd97381e' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Production"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend api-keys update b6d24b8e-af0b-4c3c-be0c-359bbd97381e --name Production
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "api_key",
    "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e"
  }
  ```
</ResponseExample>
