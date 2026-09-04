---
title: "List Organization API Tokens"
source: https://docs.turso.tech/api-reference/tokens/list-organization
path: api-reference/tokens/list-organization
---

GET /v1/organizations/{organizationSlug}/api-tokens
Returns the API tokens scoped to this organization (both organization-scoped and group-scoped). Unrestricted tokens are not returned here — manage those via [`GET /v1/auth/api-tokens`](/api-reference/tokens/list).

Authorization is symmetric with the revoke endpoint:

- **Admins and owners** see every token scoped to the organization, with the minting user attached in the `owner` field.
- **Members and viewers** see only tokens they minted themselves.

This mirrors the personal-access-token model used in GitHub organization settings: admins get the full attribution list; everyone else sees their own access.

<Info>
  Use this endpoint to enumerate the tokens that act on a single organization (both org-scoped and group-scoped). Admins and owners see every token in the organization with the minting user attached; members and viewers see only their own. To list tokens across every organization the caller belongs to, use [`GET /v1/auth/api-tokens`](/api-reference/tokens/list) instead.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/organizations/{organizationSlug}/api-tokens' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>
