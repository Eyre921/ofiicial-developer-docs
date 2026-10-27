---
title: "Delete Invite"
source: https://docs.turso.tech/api-reference/organizations/invites/delete-v2
path: api-reference/organizations/invites/delete-v2
---

DELETE /v2/organizations/{organizationSlug}/invites/{email}
Delete a pending invite for the organization by email.

> [!WARNING]
>
> Invites are limited to scaler plan and above.

```bash cURL theme={null}
curl -L -X DELETE https://api.turso.tech/v2/organizations/{organizationSlug}/invites/{email} \
  -H 'Authorization: Bearer TOKEN'
```

```ts Node.js theme={null}
import { createClient } from "@tursodatabase/api";

const turso = createClient({
  org: "mycompany",
  token: "",
});

await turso.organizations.deleteInvite("user@example.com");
```
