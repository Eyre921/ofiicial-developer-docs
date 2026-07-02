---
title: "Convert a file URL to an absolute path"
source: https://bun.com/docs/guides/util/file-url-to-path
path: docs/guides/util/file-url-to-path
---

Use `Bun.fileURLToPath()` to convert a `file://` URL to an absolute path.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
Bun.fileURLToPath("file:///path/to/file.txt");
// => "/path/to/file.txt"
```

***

See [Utils](/docs/runtime/utils).
