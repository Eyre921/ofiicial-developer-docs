---
title: "Qwik + Turso"
source: https://docs.turso.tech/sdk/ts/guides/qwik
path: sdk/ts/guides/qwik
---

Set up Turso in your Qwik project in minutes

![Qwik banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/qwik-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=bd50c1555e2915546f901981ac6efba5)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Qwik app — [learn more](https://qwik.builder.io/docs/getting-started/#create-an-app-using-the-cli)

**1. Add Turso Integration**

```bash npm theme={null}
npm run qwik add turso
```

```bash pnpm theme={null}
pnpm qwik add turso
```

```bash yarn theme={null}
yarn qwik add turso
```

**2. Configure database credentials**

Get the database URL:

```bash theme={null}
turso db show --url <database-name>
```

Get the database authentication token:

```bash theme={null}
turso db tokens create <database-name>
```

Assign credentials to the environment variables inside `.env.local`.

```bash theme={null}
PRIVATE_TURSO_DATABASE_URL="..."
PRIVATE_TURSO_AUTH_TOKEN="..."
```

**3. Execute SQL**

```ts theme={null}
import { tursoClient } from "~/utils/turso";

export const useFrameworks = routeLoader$(
  async (requestEvent: RequestEventBase) => {
    const db = tursoClient(requestEvent["env"]);
    const { rows } = await db.execute("select * from table_name");

    return {
      items: rows,
    };
  },
);
```

## Examples

> **[Social Website](https://github.com/tursodatabase/examples/tree/master/app-find-me-on)**
>
> See the full source code

> **[Shopping Cart](https://github.com/tursodatabase/examples/tree/master/app-turqw-store)**
>
> See the full source code
