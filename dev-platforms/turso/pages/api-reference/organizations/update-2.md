---
title: "Update Organization"
source: https://docs.turso.tech/api-reference/organizations/update
path: api-reference/organizations/update
---

PATCH /v1/organizations/{organizationSlug}
Update an organization you own or are a member of.

<RequestExample>
  ```bash cURL (overages) theme={null}
  curl -L -X PATCH https://api.turso.tech/v1/organizations/{organizationSlug} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "overages": true
    }'
  ```

  ```bash cURL (require MFA) theme={null}
  curl -L -X PATCH https://api.turso.tech/v1/organizations/{organizationSlug} \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "require_mfa": true
    }'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const organization = await turso.organizations.update("mycompany", {
    overages: true,
  });
  ```
</RequestExample>
