---
title: "Closest Region"
source: https://docs.turso.tech/api-reference/locations/closest-region
path: api-reference/locations/closest-region
---

GET https://region.turso.io
Returns the closest region to the user's location.

#### Response

**server** `string`

The location code for the server responding.

**client** `string`

The location code for the client request.

```bash cURL theme={null}
curl https://region.turso.io
```

```ts Node.js theme={null}
import { createClient } from "@tursodatabase/api";

const turso = createClient({
  org: "...",
  token: "",
});

const { server, client } = await turso.locations.closest();
```

```json 200 theme={null}
{
  "server": "lhr",
  "client": "lhr"
}
```
