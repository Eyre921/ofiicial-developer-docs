---
title: "Convert an ArrayBuffer to a string"
source: https://bun.com/docs/guides/binary/arraybuffer-to-string
path: docs/guides/binary/arraybuffer-to-string
---

Bun implements the Web-standard [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder) class for converting between binary data types and strings.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = new ArrayBuffer(64);
const decoder = new TextDecoder();
const str = decoder.decode(buf);
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
