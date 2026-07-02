---
title: "Re-run tests multiple times with the Bun test runner"
source: https://bun.com/docs/guides/test/rerun-each
path: docs/guides/test/rerun-each
---

The `--rerun-each` flag runs every test multiple times. Use it to find flaky or non-deterministic tests.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
# re-run each test 10 times
bun test --rerun-each 10
```

***

See [`bun test`](/docs/test).
