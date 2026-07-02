---
title: "Delete a file"
source: https://bun.com/docs/guides/write-file/unlink
path: docs/guides/write-file/unlink
---

The `Bun.file()` function accepts a path and returns a `BunFile` instance. Use the `.delete()` method to delete the file.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const path = "/path/to/file.txt";
const file = Bun.file(path);

await file.delete();
```

***

See [`Bun.file()`](/docs/runtime/file-io#reading-files-bun-file).
