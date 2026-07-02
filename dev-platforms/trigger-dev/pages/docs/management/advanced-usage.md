---
title: "Advanced usage"
source: https://trigger.dev/docs/management/advanced-usage
path: docs/management/advanced-usage
---

Advanced usage of the Trigger.dev management API

### Accessing raw HTTP responses

All API methods return a `Promise` subclass `ApiPromise` that includes helpers for accessing the underlying HTTP response:

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

async function main() {
  const { data: run, response: raw } = await runs.retrieve("run_1234").withResponse();

  console.log(raw.status);
  console.log(raw.headers);

  const response = await runs.retrieve("run_1234").asResponse(); // Returns a Response object

  console.log(response.status);
  console.log(response.headers);
}
```
