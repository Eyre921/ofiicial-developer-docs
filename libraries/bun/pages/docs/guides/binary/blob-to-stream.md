---
title: "Convert a Blob to a ReadableStream"
source: https://bun.com/docs/guides/binary/blob-to-stream
path: docs/guides/binary/blob-to-stream
---

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides several methods for consuming its contents in different formats, including `.stream()`, which returns a `ReadableStream`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const blob = new Blob(["hello world"]);
const stream = blob.stream();
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
