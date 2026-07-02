---
title: "Read stderr from a child process"
source: https://bun.com/docs/guides/process/spawn-stderr
path: docs/guides/process/spawn-stderr
---

When you spawn a child process with [`Bun.spawn()`](/docs/runtime/child-process), it inherits the `stderr` of the spawning process. To read and handle `stderr` instead, set the `stderr` option to `"pipe"`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const proc = Bun.spawn(["echo", "hello"], {
  stderr: "pipe",
});

proc.stderr; // => ReadableStream
```

***

To read `stderr` until the child process exits, use `.text()`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const proc = Bun.spawn(["echo", "hello"], {
  stderr: "pipe",
});

const errors: string = await proc.stderr.text();
if (errors) {
  // handle errors
}
```

***

See [Child processes](/docs/runtime/child-process).
