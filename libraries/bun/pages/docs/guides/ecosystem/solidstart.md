---
title: "Build an app with SolidStart and Bun"
source: https://bun.com/docs/guides/ecosystem/solidstart
path: docs/guides/ecosystem/solidstart
---

Initialize a SolidStart app with `create-solid`. Pass the `--solidstart` flag to create a SolidStart project and `--ts` for TypeScript support. When prompted for a SolidStart version, select `2 (Stable)`. When prompted for a template, select `basic` for a minimal starter app.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun create solid my-app --solidstart --ts
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
┌
 Create-Solid v0.9.0
│
◇  Which version of SolidStart?
│  2 (Stable)
│
◇  Which template would you like to use?
│  basic
│
◇  Project created 🎉
│
◇  To get started, run: ─╮
│                        │
│  cd my-app             │
│  bun install           │
│  bun dev               │
│                        │
├────────────────────────╯
```

***

Install the dependencies.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
cd my-app
bun install
```

Then run the development server with `bun dev`.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun dev
```

```txt theme={"theme":{"light":"github-light","dark":"dracula"}}
$ vite dev

  VITE v8.1.4  ready in 818 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

Open [localhost:3000](http://localhost:3000). The development server automatically hot-reloads changes you make to `src/routes/index.tsx`.

***

See the [SolidStart docs](https://docs.solidjs.com/solid-start) to learn more.
