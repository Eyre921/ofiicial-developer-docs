---
title: "Enable compression for WebSocket messages"
source: https://bun.com/docs/guides/websocket/compression
path: docs/guides/websocket/compression
---

Set the `perMessageDeflate` parameter to enable the [permessage-deflate](https://tools.ietf.org/html/rfc7692) WebSocket extension. Bun then negotiates compression with clients that support it. Messages sent with `ws.send()` are still uncompressed unless you opt in per message (see below).

```ts server.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
Bun.serve({
  // ...
  websocket: {
    // enable compression
    perMessageDeflate: true,
  },
});
```

***

To enable compression for individual messages, pass `true` as the second parameter to `ws.send()`. This requires `perMessageDeflate` to be enabled; otherwise Bun sends the message uncompressed.

```ts server.ts icon="https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b" theme={"theme":{"light":"github-light","dark":"dracula"}}
Bun.serve({
  // ...
  websocket: {
    perMessageDeflate: true,
    async message(ws, message) {
      // send a compressed message
      ws.send(message, true);
    },
  },
});
```
