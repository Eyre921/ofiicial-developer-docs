---
title: "Convert a Blob to a string"
source: https://bun.com/docs/guides/binary/blob-to-string
path: docs/guides/binary/blob-to-string
---

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides several methods for consuming its contents in different formats, including `.text()`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const blob = new Blob(["hello world"]);
const str = await blob.text();
// => "hello world"
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
