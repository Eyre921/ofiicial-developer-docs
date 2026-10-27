---
title: "Remix + Turso"
source: https://docs.turso.tech/sdk/ts/guides/remix
path: sdk/ts/guides/remix
---

Set up Turso in your Remix project in minutes

![Remix banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=84822de5a6eb5531447a66d6afe6662a)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Remix app — [learn more](https://remix.run/docs/en/main/start/quickstart#quick-start)

**1. Install the libSQL SDK**

<Snippet />

**2. Configure database credentials**

<Snippet />

**3. Configure libSQL Client.**

<Snippet />

**4. Execute SQL**

```ts app/routes/_index.ts theme={null}
import type { LoaderFunction } from "@remix-run/node";

import { turso } from "~/lib/turso";

export const loader: LoaderFunction = async () => {
  const { rows } = await turso.execute("SELECT * from TABLE_NAME");

  return {
    items: rows,
  };
};
```

## Examples

> **[E-commerce Store](https://github.com/tursodatabase/examples/tree/master/app-the-mug-store)**
>
> See the full source code

> **[CRM App](https://github.com/tursodatabase/examples/tree/master/app-turso-crm)**
>
> See the full source code
