---
title: "Next.js + Turso"
source: https://docs.turso.tech/sdk/ts/guides/nextjs
path: sdk/ts/guides/nextjs
---

Set up Turso in your Next.js project in minutes.

![Next.js banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=70fd7aa0941f6871ae5e4a2eb3292cce)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Next.js app — [learn more](https://nextjs.org/docs/getting-started/installation)

**1. Install the libSQL SDK**

<Snippet />

**2. Configure database credentials**

<Snippet />

**3. Configure libSQL client**

<Snippet />

**4. Execute SQL**

```tsx App Router theme={null}
import { turso } from "@/lib/turso";

export default async function Page() {
  const { rows } = await turso.execute("SELECT * FROM table_name");

  return (
    <ul>
      {rows.map((row) => (
        <li key={row.id}>{row.id}</li>
      ))}
    </ul>
  );
}
```

```ts Pages Directory theme={null}
import type { InferGetServerSidePropsType, GetServerSideProps } from "next";

import { turso } from "@/lib/turso";

export const getServerSideProps = (async () => {
  const { rows } = await turso.execute("SELECT * FROM table_name");

  return {
    props: {
      rows,
    },
  };
}) satisfies GetServerSideProps<{ rows: any[] }>;

export default function Page({
  rows,
}: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return (
    <ul>
      {rows.map((row) => (
        <li key={row.id}>{row.id}</li>
      ))}
    </ul>
  );
}
```

## Examples

> **[Full Stack App](https://github.com/tursodatabase/nextjs-turso-starter)**
>
> Build with Next.js, Turso, and Drizzle ORM.
