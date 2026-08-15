---
title: "Detect when code is executed with Bun"
source: https://bun.com/docs/guides/util/detect-bun
path: docs/guides/util/detect-bun
---

Check `process.versions.bun` to detect whether code is running in Bun. This works in both JavaScript and TypeScript without extra type definitions.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
if (process.versions.bun) {
  // this code will only run when the file is run with Bun
}
```

***

Alternatively, check for the `Bun` global, the same way you'd check for `window` to detect a browser.

<Note>
  In TypeScript, this check is a type error unless `@types/bun` is installed. Install it with `bun add -d @types/bun`.
  If you're using TypeScript 6.0 or later, you also need `"types": ["bun"]` in your `compilerOptions`. See [TypeScript 6
  and 7](/docs/typescript-6) for details.
</Note>

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
if (typeof Bun !== "undefined") {
  // this code will only run when the file is run with Bun
}
```
