---
title: "Create API Token"
source: https://docs.turso.tech/api-reference/tokens/create
path: api-reference/tokens/create
---

POST /v1/auth/api-tokens/{tokenName}
Returns a new API token belonging to a user.

The token can be minted at three levels of restriction, in increasing order of narrowness:

- **Organization-scoped** — pass `organization`. The token can only act on resources inside that organization.
- **Group-scoped** — pass `organization`, `group`, and `scopes`. The token is pinned to a single group inside the organization and only the operations listed in `scopes` are allowed. The caller must be an admin or owner of the organization.
- **Unrestricted** *(deprecated)* — no request body. The token can act on every organization the caller belongs to. **Unrestricted tokens are deprecated and will be removed in a future release.** Always pass `organization` for new tokens and rotate existing unrestricted tokens to scoped tokens.

Group-scoped tokens are designed for automations that should be able to provision and manage databases inside a single group without being able to touch the rest of the organization.

<Warning>
  The `token` in the response is never revealed again. Store this somewhere safe, and never share or commit it to source control.
</Warning>

<Warning>
  **Unrestricted (cross-org) tokens are deprecated and will be removed in a future release.** Always include at least `organization` in the request body.
</Warning>

<RequestExample>
  ```bash cURL (org-scoped) theme={null}
  curl -L -X POST https://api.turso.tech/v1/auth/api-tokens/{tokenName} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{"organization": "my-org"}'
  ```

  ```bash cURL (deprecated, unrestricted) theme={null}
  curl -L -X POST https://api.turso.tech/v1/auth/api-tokens/{tokenName} \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```bash cURL (group-scoped, presets) theme={null}
  curl -L -X POST https://api.turso.tech/v1/auth/api-tokens/{tokenName} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
      "organization": "my-org",
      "group": "default",
      "scopes": ["read-only"]
    }'
  ```

  ```bash cURL (group-scoped, fine-grained) theme={null}
  curl -L -X POST https://api.turso.tech/v1/auth/api-tokens/{tokenName} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
      "organization": "my-org",
      "group": "default",
      "scopes": ["db:create", "db:configure", "db:mint-token"]
    }'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const apiToken = await turso.apiTokens.create("my-token");
  ```
</RequestExample>
