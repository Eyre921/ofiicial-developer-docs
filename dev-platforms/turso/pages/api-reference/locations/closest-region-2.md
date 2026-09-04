---
title: "Closest Region"
source: https://docs.turso.tech/api-reference/locations/closest-region
path: api-reference/locations/closest-region
---

GET https://region.turso.io
Returns the closest region to the user's location.

#### Response

<ResponseField name="server" type="string">
  The location code for the server responding.
</ResponseField>

<ResponseField name="client" type="string">
  The location code for the client request.
</ResponseField>

<RequestExample>
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
</RequestExample>

<ResponseExample>
  ```json 200 theme={null}
  {
    "server": "lhr",
    "client": "lhr"
  }
  ```
</ResponseExample>
