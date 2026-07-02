---
title: "Add a tarball dependency"
source: https://bun.com/docs/guides/install/add-tarball
path: docs/guides/install/add-tarball
---

Bun's package manager can install any publicly available tarball URL as a dependency of your project.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun add zod@https://registry.npmjs.org/zod/-/zod-3.21.4.tgz
```

***

This command downloads, extracts, and installs the tarball into your project's `node_modules` directory, and adds the following line to your `package.json`:

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "dependencies": {
    "zod": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz" // [!code ++]
  }
}
```

***

You can now import `zod` as usual.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
import { z } from "zod";
```

***

See [`bun install`](/docs/pm/cli/install).
