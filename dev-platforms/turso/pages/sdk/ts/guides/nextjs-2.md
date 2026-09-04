---
title: "Next.js + Turso"
source: https://docs.turso.tech/sdk/ts/guides/nextjs
path: sdk/ts/guides/nextjs
---

Set up Turso in your Next.js project in minutes.

<img alt="Next.js banner" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Next.js app — [learn more](https://nextjs.org/docs/getting-started/installation)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet />
  </Step>

  <Step title="Configure database credentials">
    <Snippet />
  </Step>

  <Step title="Configure libSQL client">
    <Snippet />
  </Step>

  <Step title="Execute SQL">
    <CodeGroup>
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
    </CodeGroup>
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Full Stack App" icon="github" href="https://github.com/tursodatabase/nextjs-turso-starter">
    Build with Next.js, Turso, and Drizzle ORM.
  </Card>
</CardGroup>
