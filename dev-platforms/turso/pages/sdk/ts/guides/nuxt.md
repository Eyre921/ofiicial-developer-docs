---
title: "Nuxt + Turso"
source: https://docs.turso.tech/sdk/ts/guides/nuxt
path: sdk/ts/guides/nuxt
---

Set up Turso in your Nuxt project in minutes

![Nuxt banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=9c0353730a9944cd5e99e71cb2666025)

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Nuxt app — [learn more](https://nuxt.com/docs/getting-started/installation#new-project)

**1. Install the libSQL SDK**

<Snippet />

**2. Configure database credentials**

Get the database URL:

```bash theme={null}
turso db show --url <database-name>
```

Get the database authentication token:

```bash theme={null}
turso db tokens create <database-name>
```

Assign credentials to the environment variables inside `.env`.

```bash theme={null}
NUXT_TURSO_DATABASE_URL=
NUXT_TURSO_AUTH_TOKEN=
```

**3. Configure variables inside Nuxt's runtime config.**

```ts nuxt.config.ts theme={null}
export default defineNuxtConfig({
  runtimeConfig: {
    turso: {
      databaseUrl: "",
      authToken: "",
    },
  },
});
```

> [!NOTE]
>
> Make sure that names of the keys in the `runtimeConfig` object match the names
> of your environment variables. Read more about this
> [here](https://nuxt.com/docs/guide/going-further/runtime-config).

**4. Configure libSQL Client.**

```ts server/utils/turso.ts theme={null}
import { createClient } from "@libsql/client";
// You can optionally pass in the event to useRuntimeConfig
// import { H3Event } from "h3";

export function useTurso(/* event: H3Event */) {
  const { turso } = useRuntimeConfig(/* event */);

  return createClient({
    url: turso.databaseUrl,
    authToken: turso.authToken,
  });
}
```

**5. Execute SQL**

```ts server/api/items.get.ts theme={null}
export default defineEventHandler(async (event) => {
  const client = useTurso(/* event */);
  const { rows } = await client.execute("select * from table_name");

  return {
    data: {
      items: rows,
    },
  };
});
```

## Examples

> **[Website + App](https://github.com/tursodatabase/examples/tree/master/app-top-web-frameworks)**
>
> See the full source code
