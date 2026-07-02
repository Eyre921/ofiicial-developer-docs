---
title: "Listen for CTRL+C"
source: https://bun.com/docs/guides/process/ctrl-c
path: docs/guides/process/ctrl-c
---

The `ctrl+c` shortcut sends an *interrupt signal* to the running process. Intercept it by listening for the `SIGINT` event. To close the process, you must explicitly call `process.exit()`.

```ts process.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
process.on("SIGINT", () => {
  console.log("Ctrl-C was pressed");
  process.exit();
});
```

***

See [Utils](/docs/runtime/utils) for more utilities.
