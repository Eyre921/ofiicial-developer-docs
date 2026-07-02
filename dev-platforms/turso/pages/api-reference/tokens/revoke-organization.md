---
title: "Revoke Organization API Token"
source: https://docs.turso.tech/api-reference/tokens/revoke-organization
path: api-reference/tokens/revoke-organization
---

DELETE /v1/organizations/{organizationSlug}/api-tokens/{tokenId}
Revokes a token scoped to this organization.

The path takes a token **ID**, not a name, because names are unique per user but not across users — an admin revoking a member's token can't disambiguate by name alone.

Authorization is symmetric with the list endpoint:

- **Admins and owners** can revoke any token scoped to the organization (org-scoped or group-scoped, regardless of who minted it).
- **Members and viewers** can revoke only tokens they minted themselves.

A token scoped to a different organization returns `404`, not `403`, so the endpoint does not leak the existence of cross-org token IDs. Unrestricted tokens are also unreachable here and must be revoked via [`DELETE /v1/auth/api-tokens/{tokenName}`](/api-reference/tokens/revoke).

<Info>
  This endpoint takes a token **ID** (not a name) because token names are not unique across users in an organization. Admins and owners may revoke any token scoped to the organization; members and viewers may only revoke tokens they minted themselves. Use [`DELETE /v1/auth/api-tokens/{tokenName}`](/api-reference/tokens/revoke) to revoke unrestricted tokens.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/organizations/{organizationSlug}/api-tokens/{tokenId}' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
