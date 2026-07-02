---
title: "Convert an absolute path to a file URL"
source: https://bun.com/docs/guides/util/path-to-file-url
path: docs/guides/util/path-to-file-url
---

Use `Bun.pathToFileURL()` to convert an absolute path to a `file://` URL.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
Bun.pathToFileURL("/path/to/file.txt");
// => "file:///path/to/file.txt"
```

***

See [Utils](/docs/runtime/utils).
