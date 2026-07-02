---
title: "Get the MIME type of a file"
source: https://bun.com/docs/guides/read-file/mime
path: docs/guides/read-file/mime
---

The `Bun.file()` function accepts a path and returns a `BunFile` instance. The `BunFile` class extends `Blob`, so use the `.type` property to read the MIME type.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const file = Bun.file("./package.json");
file.type; // application/json

const file = Bun.file("./index.html");
file.type; // text/html

const file = Bun.file("./image.png");
file.type; // image/png
```

***

See [File I/O](/docs/runtime/file-io) for more on working with `BunFile`.
