---
title: "Build an app with Next.js and Bun"
source: https://bun.com/docs/guides/ecosystem/nextjs
path: docs/guides/ecosystem/nextjs
---

[Next.js](https://nextjs.org/) is a React framework for building full-stack web applications. It supports server-side rendering, static site generation, and API routes. Bun installs packages fast and can run Next.js development and production servers.

***

<Steps>
  <Step title="Create a new Next.js app">
    Use the interactive CLI to scaffold a new Next.js project and install its dependencies.

    ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
    bun create next-app@latest my-bun-app
    ```
  </Step>

  <Step title="Start the dev server">
    Change to the project directory and run the dev server with Bun.

    ```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
    cd my-bun-app
    bun --bun run dev
    ```

    This starts the Next.js dev server with Bun's runtime.

    Open [`http://localhost:3000`](http://localhost:3000) in your browser to see the result. Changes you make to `app/page.tsx` are hot-reloaded in the browser.
  </Step>

  <Step title="Update scripts in package.json">
    Prefix the Next.js CLI commands in your `package.json` scripts with `bun --bun` so that Bun executes the Next.js CLI for `dev`, `build`, and `start`.

    ```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
    {
      "scripts": {
        "dev": "bun --bun next dev", // [!code ++]
        "build": "bun --bun next build", // [!code ++]
        "start": "bun --bun next start" // [!code ++]
      }
    }
    ```
  </Step>
</Steps>

***

## Hosting

<Columns>
  <Card title="Vercel" href="/guides/deployment/vercel" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/ecosystem/vercel.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=165bc9841eef2a62f3951be494dbc89a">
    Deploy on Vercel
  </Card>

  <Card title="Railway" href="/guides/deployment/railway" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/ecosystem/railway.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=029a2b4b7c3a9f8dfab8d1bebbbfa054">
    Deploy on Railway
  </Card>

  <Card title="DigitalOcean" href="/guides/deployment/digital-ocean" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/ecosystem/digitalocean.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=aead95e8fef32d0ec83e63292f21f80c">
    Deploy on DigitalOcean
  </Card>

  <Card title="AWS Lambda" href="/guides/deployment/aws-lambda" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/ecosystem/aws.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=f747e7b59435e87b2e379be04eabda8f">
    Deploy on AWS Lambda
  </Card>

  <Card title="Google Cloud Run" href="/guides/deployment/google-cloud-run" icon="https://mintcdn.com/bun-1dd33a4e/cfVIaCNGtFU88Wgc/icons/ecosystem/gcp.svg?fit=max&auto=format&n=cfVIaCNGtFU88Wgc&q=85&s=a99e6cb0cfadfeb9ea3b6451de38cfd6">
    Deploy on Google Cloud Run
  </Card>

  <Card title="Render" href="/guides/deployment/render" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/ecosystem/render.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=b632a0b982a579fa5a2d0b96f33bace8">
    Deploy on Render
  </Card>
</Columns>

***

## Templates

<Columns>
  <Card title="Bun + Next.js Basic Starter" href="https://github.com/bun-templates/bun-nextjs-basic">
    A basic App Router starter with Bun, Next.js, and Tailwind CSS.
  </Card>

  <Card title="Todo App with Next.js + Bun" href="https://github.com/bun-templates/bun-nextjs-todo">
    A full-stack todo application built with Bun, Next.js, and PostgreSQL.
  </Card>
</Columns>

***

Refer to the [Next.js documentation](https://nextjs.org/docs) for more on building and deploying Next.js applications.
