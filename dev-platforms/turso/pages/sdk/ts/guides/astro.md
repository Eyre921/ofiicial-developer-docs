---
title: "Astro + Turso"
source: https://docs.turso.tech/sdk/ts/guides/astro
path: sdk/ts/guides/astro
---

Set up Turso in your Astro project in minutes.

![Astro banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=5b0999657788a4cdccf007d44d34ca89)

## Prerequisites

To get the most out of this guide, you'll need to:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Astro project — [learn more](https://docs.astro.build/en/install/auto/#1-run-the-setup-wizard)

**1. Install the libSQL SDK**

<Snippet />

**2. Configure database credentials**

<Snippet />

**3. Configure libSQL client**

```ts src/turso.ts theme={null}
import { createClient } from "@libsql/client/web";

export const turso = createClient({
  url: import.meta.env.TURSO_DATABASE_URL!,
  authToken: import.meta.env.TURSO_AUTH_TOKEN,
});
```

> [!NOTE]
>
> Astro will soon introduce a new ENV API. [Take a
> look](https://docs.astro.build/en/reference/configuration-reference/#experimentalenv).

**4. Execute SQL**

```ts theme={null}
---
import { turso } from './turso'

const { rows } = await turso.execute('SELECT * FROM table_name')
---
```

## Examples

> **[Blog](https://github.com/tursodatabase/examples/tree/master/app-tustro-blog)**
>
> See the full source code
