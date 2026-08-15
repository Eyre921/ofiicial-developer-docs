---
title: "Sleep for a fixed number of milliseconds"
source: https://bun.com/docs/guides/util/sleep
path: docs/guides/util/sleep
---

`Bun.sleep()` returns a void `Promise` that resolves after a given number of milliseconds.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
// sleep for 1 second
await Bun.sleep(1000);
```

***

Internally, `Bun.sleep()` is equivalent to the following [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout) snippet.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
await new Promise(resolve => setTimeout(resolve, ms));
```

***

See [Utils](/docs/runtime/utils).
