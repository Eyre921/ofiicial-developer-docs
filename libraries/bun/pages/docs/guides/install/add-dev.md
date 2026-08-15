---
title: "Add a development dependency"
source: https://bun.com/docs/guides/install/add-dev
path: docs/guides/install/add-dev
---

To add an npm package as a development dependency, use `bun add --development`.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun add zod --dev
bun add zod -d # shorthand
```

***

This adds the package to `devDependencies` in `package.json`.

```json theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "devDependencies": {
    "zod": "^4.0.0" // [!code ++]
  }
}
```

***

See [`bun install`](/docs/pm/cli/install).
