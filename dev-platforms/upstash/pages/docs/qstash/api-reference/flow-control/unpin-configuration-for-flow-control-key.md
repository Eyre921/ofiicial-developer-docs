---
title: "Unpin Configuration for Flow Control Key"
source: https://upstash.com/docs/qstash/api-reference/flow-control/unpin-configuration-for-flow-control-key
path: docs/qstash/api-reference/flow-control/unpin-configuration-for-flow-control-key
---

> Removes the pinned configuration for a specific flow-control key.

`POST /v2/flowControl/{flowControlKey}/unpin`

Normally, each message sent to QStash includes a flow-control configuration for the corresponding flow-control key, and the processing configuration is updated according to incoming messages.

When a configuration is pinned, the system ignores configurations provided by incoming messages and continues using the pinned configuration.

Calling this endpoint removes the pinned configuration. After unpinning, the system resumes the default behavior and updates the configuration based on configurations provided by incoming messages.

Message delivery will initially continue using the last pinned configuration. Once a new message with a different configuration is received, the system updates the configuration accordingly.

Use this API when you want to return to the default flow-control behavior after temporarily pinning a configuration.
