---
title: "Copy a file to another location"
source: https://bun.com/docs/guides/write-file/file-cp
path: docs/guides/write-file/file-cp
---

Use [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write) to copy a file to another location on disk. The first argument is a *destination*, like an absolute path or `BunFile` instance. The second argument is the *data* to write.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const file = Bun.file("/path/to/original.txt");
await Bun.write("/path/to/copy.txt", file);
```

***

See [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).
