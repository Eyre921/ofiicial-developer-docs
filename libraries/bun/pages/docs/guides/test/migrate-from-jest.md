---
title: "Migrate from Jest to Bun's test runner"
source: https://bun.com/docs/guides/test/migrate-from-jest
path: docs/guides/test/migrate-from-jest
---

In many cases, Bun's test runner can run Jest test suites with no code changes. Run `bun test` instead of `npx jest` or `yarn test`.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
npx jest # [!code --]
yarn test # [!code --]
bun test # [!code ++]
```

***

Your test files usually work as-is.

* Bun internally rewrites imports from `@jest/globals` to their `bun:test` equivalents.
* If you rely on Jest to inject globals like `test` and `expect`, Bun does that too.

If you'd rather import from `bun:test` directly, update the imports.

```ts title="test.ts" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
import { test, expect } from "@jest/globals"; // [!code --]
import { test, expect } from "bun:test"; // [!code ++]
```

***

Since Bun v1.2.19, a triple-slash directive enables **TypeScript support** for global test functions. Add it to *one file* in your project, such as:

* A `global.d.ts` file in your project root
* Your test `preload.ts` setup file (if using `preload` in bunfig.toml)
* Any single `.ts` file that TypeScript includes in your compilation

```ts title="global.d.ts" icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
/// <reference types="bun-types/test-globals" />
```

***

Once added, every test file in your project gets TypeScript support for the Jest globals:

```ts math.test.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
describe("my test suite", () => {
  test("should work", () => {
    expect(1 + 1).toBe(2);
  });

  beforeAll(() => {
    // setup code
  });

  afterEach(() => {
    // cleanup code
  });
});
```

***

Bun implements most of Jest's matchers, but compatibility isn't 100%. See the compatibility table in [Writing tests](/docs/test/writing-tests#matchers).

***

If you use `testEnvironment: "jsdom"` to run your tests in a browser-like environment, follow the [DOM testing with Bun and happy-dom](/docs/guides/test/happy-dom) guide to inject browser APIs into the global scope. That guide uses [`happy-dom`](https://github.com/capricorn86/happy-dom), a leaner and faster alternative to [`jsdom`](https://github.com/jsdom/jsdom).

```toml bunfig.toml icon="settings" theme={"theme":{"light":"github-light","dark":"dracula"}}
[test]
preload = ["./happydom.ts"]
```

***

Replace `bail` in your Jest config with the `--bail` CLI flag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun test --bail=3
```

***

Replace `collectCoverage` with the `--coverage` CLI flag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun test --coverage
```

***

Replace `testTimeout` with the `--timeout` CLI flag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun test --timeout 10000
```

***

Many other Jest settings are irrelevant in `bun test`.

* `transform` — Bun supports TypeScript & JSX. Configure other file types with [plugins](/docs/runtime/plugins).
* `extensionsToTreatAsEsm`
* `haste` — Bun uses its own [module resolver](/docs/runtime/module-resolution)
* `watchman`, `watchPlugins`, `watchPathIgnorePatterns` — use `--watch` to run tests in watch mode
* `verbose` — `bun test` reports each test by default. Use `--only-failures` or `--dots` for less output (see [Test reporters](/docs/test/reporters)).

***

Many other settings have an equivalent in the `[test]` section of `bunfig.toml`. For example:

* `setupFiles`/`setupFilesAfterEnv` → `preload`
* `testPathIgnorePatterns` → `pathIgnorePatterns`
* `rootDir` → `root`
* `coverageDirectory` → `coverageDir`
* `coverageReporters` → `coverageReporter`
* `coverageThreshold` → `coverageThreshold` (as a fraction like `0.9`, not a percentage)

See [Test configuration](/docs/test/configuration). Settings without an equivalent are not supported. [File a feature request](https://github.com/oven-sh/bun) if something you need is missing.

***

See also:

* [Mark a test as a todo](/docs/guides/test/todo-tests)
* [Writing tests](/docs/test/writing-tests)
