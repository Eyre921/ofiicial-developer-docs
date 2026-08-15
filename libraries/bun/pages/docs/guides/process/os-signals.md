---
title: "Listen to OS signals"
source: https://bun.com/docs/guides/process/os-signals
path: docs/guides/process/os-signals
---

Bun supports the Node.js `process` global, including the `process.on()` method for listening to OS signals.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
process.on("SIGINT", () => {
  console.log("Received SIGINT");
});
```

***

To run code when the process exits, listen for these events:

* [`"beforeExit"`](https://nodejs.org/api/process.html#event-beforeexit): Bun emits this event when the event loop empties.
* [`"exit"`](https://nodejs.org/api/process.html#event-exit): Bun emits this event when the event loop empties or when `process.exit()` is called.

Neither event is emitted when the process is killed by a signal it has no listener for. To run cleanup on a signal, listen for that signal and call `process.exit()` from the listener.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
process.on("beforeExit", code => {
  console.log(`Event loop is empty!`);
});

process.on("exit", code => {
  console.log(`Process is exiting with code ${code}`);
});
```

***

See [Utils](/docs/runtime/utils) for more utilities.
