---
title: "Revoke Grant"
source: https://resend.com/docs/api-reference/oauth/revoke-grant
path: docs/api-reference/oauth/revoke-grant
---

DELETE /oauth/grants/:oauth_grant_id
Revoke an OAuth grant for the authenticated team.

Revoking a grant invalidates every access and refresh token issued under it. Any
team API key can revoke any of the team's grants. Returns `404` if the grant
does not exist or was already revoked.

## Path Parameters

<ResendParamField type="string">
  The OAuth grant ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.oauthGrants.revoke(
    '650e8400-e29b-41d4-a716-446655440001',
  );
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  use resend_rs::{Resend, Result};

  #[tokio::main]
  async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    let _data = resend
      .oauth
      .revoke("650e8400-e29b-41d4-a716-446655440001")
      .await?;

    Ok(())
  }
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X DELETE 'https://api.resend.com/oauth/grants/650e8400-e29b-41d4-a716-446655440001' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "oauth_grant",
    "id": "650e8400-e29b-41d4-a716-446655440001",
    "revoked_at": "2026-04-08T00:11:13.110Z",
    "revoked_reason": "revoked_from_api"
  }
  ```
</ResponseExample>
