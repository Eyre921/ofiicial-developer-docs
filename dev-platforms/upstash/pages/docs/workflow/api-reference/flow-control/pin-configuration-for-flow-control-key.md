---
title: "Pin Configuration for Flow Control Key"
source: https://upstash.com/docs/workflow/api-reference/flow-control/pin-configuration-for-flow-control-key
path: docs/workflow/api-reference/flow-control/pin-configuration-for-flow-control-key
---

> Pins a processing configuration for a specific flow-control key.

`POST /v2/flowControl/{flowControlKey}/pin`

Normally, each message sent to QStash includes a flow-control configuration for the corresponding flow-control key. 
The processing configuration is updated based on configurations provided by incoming messages.

This means that if you want to change the configuration, you typically need to update it in your code and wait until a new message with the updated configuration is sent.

By pinning a configuration, you can enforce a fixed configuration for a flow-control key. 
While pinned, the system ignores configurations provided by incoming messages and continues using the pinned configuration until it is explicitly unpinned.

This allows you to increase or decrease processing throughput without requiring code changes or waiting for new messages with updated configurations.
For example, you can temporarily increase the processing speed to clear a backlog of pending messages, or decrease it when a downstream dependency is experiencing issues.

<Warning>Pinning a configuration resets the current state (rate count and period) of the flow-control key.</Warning>
