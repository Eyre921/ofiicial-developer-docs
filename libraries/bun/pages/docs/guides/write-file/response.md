---
title: "Write a Response to a file"
source: https://bun.com/docs/guides/write-file/response
path: docs/guides/write-file/response
---

Use [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write) to write a `Response` to disk. Bun writes the body of the `Response` to the destination.

The first argument is a *destination*, like an absolute path or `BunFile` instance. The second argument is the *data* to write.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const result = await fetch("https://bun.com");
const path = "./file.txt";
await Bun.write(path, result);
```

***

See [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).
