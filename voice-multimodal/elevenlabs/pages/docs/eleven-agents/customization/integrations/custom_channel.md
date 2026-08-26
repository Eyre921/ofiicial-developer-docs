---
title: "Custom Channel"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/custom_channel.md
path: docs/eleven-agents/customization/integrations/custom_channel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Custom Channel

## Overview

Custom Channel connects an external messaging system to an ElevenLabs agent. Send user messages to an ElevenLabs webhook, then receive agent replies on your own HTTPS endpoint.

Custom Channel is in alpha.

Custom Channel is unavailable for agents or workspaces using zero-retention mode. Inbound requests
for such an agent or workspace are rejected with `403 Forbidden`.

## Setup

#### Open Custom Channel

Open your agent, select **Channels**, choose **Custom Channel**, and click **Add trigger**.

#### Configure the trigger

Select an existing connection or create one, then enter the **Reply Webhook URL**.

#### Copy the credentials

Click **Add**, then copy the **Inbound Webhook URL**, **Inbound Secret**, and **Outbound Signing Secret**.

#### Configure your service

Send user messages to the inbound webhook URL with the inbound secret in `X-Webhook-Secret`. Use the outbound signing secret to verify each reply.

## Send a message

Send a `POST` request to the generated webhook URL:

```text
POST /v1/convai/api-integrations/custom_channel/triggers/{trigger_connection_id}/async_message
X-Webhook-Secret: <inbound-secret>
Content-Type: application/json
```

```json
{
  "data": {
    "type": "user_message",
    "text": "Where is my order?",
    "user_identifier": "customer_8427"
  },
  "user_message_id": "msg_01k1e6z3f4t8n9c2",
  "dynamic_variables": {
    "order_id": "order_72491"
  }
}
```

| Field                  | Required | Description                                                                              |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `data.type`            | Yes      | Must be `user_message`.                                                                  |
| `data.text`            | Yes      | Non-empty user message.                                                                  |
| `data.user_identifier` | No       | Identifier for the external user.                                                        |
| `user_message_id`      | Yes      | Non-empty idempotency key supplied by your system.                                       |
| `conversation_id`      | No       | Include the returned ID to continue a conversation. Omit it to start a new conversation. |
| `dynamic_variables`    | No       | Dynamic variables supplied to the agent for this turn.                                   |

ElevenLabs returns `202 Accepted` before processing the turn:

```json
{
  "conversation_id": "conv_01k1e72d4x8p6v3m",
  "status": "queued"
}
```

To continue the conversation, send another request with that `conversation_id` and a new `user_message_id`.

Replaying the same scoped `user_message_id` within 24 hours does not start another turn. Initial
messages are scoped by trigger and `user_identifier`; continuation messages are additionally
scoped by `conversation_id`.

## Receive replies

ElevenLabs sends a `POST` request to the reply webhook URL after each turn:

```json
{
  "version": "1",
  "conversation_id": "conv_01k1e72d4x8p6v3m",
  "user_message_ids": ["msg_01k1e6z3f4t8n9c2"],
  "status": "completed",
  "data": [
    {
      "type": "agent_response",
      "event": {
        "agent_response": "Your order is scheduled to arrive tomorrow.",
        "response_id": "9f2c1a7e-4b3d-4e8a-9c1f-2d6b8e0a5f31",
        "event_id": 4
      }
    },
    {
      "type": "agent_tool_response",
      "event": {
        "tool_name": "end_call",
        "tool_call_id": "toolu_01k1e70r4b8y",
        "tool_type": "system",
        "event_id": 4,
        "is_called": true,
        "is_error": false,
        "is_blocked": false,
        "status": "success"
      }
    }
  ],
  "error": null
}
```

If processing fails, `status` is `failed`, `data` is `[]`, and `error` contains a description.

`data` lists events in turn order. Every item has a `type` and an `event`:

* `agent_response` contains one agent utterance. `response_id` uniquely identifies the utterance, while `event_id` associates it with a turn. Join the `agent_response` values if your channel renders one text bubble per turn.
* `agent_tool_response` reports a tool outcome and shares the turn's `event_id`. Its `status` is `success`, `error`, `blocked`, or `skipped`. A response with `tool_type: "system"`, `tool_name: "end_call"`, and `status: "success"` means the agent ended the conversation.

Multiple inbound messages can be coalesced into one turn. `user_message_ids` lists the user message IDs this reply is answering.

## Verify reply signatures

Each reply includes an `ElevenLabs-Signature` header:

```text
t=1753876800,v0=<hex-digest>
```

The digest is an HMAC-SHA256 signature over `{timestamp}.{raw_request_body}` using the outbound signing secret. Verify the raw body before parsing JSON and reject stale timestamps.

```python
import hashlib
import hmac
import time


def verify_signature(raw_body: bytes, header: str, secret: str) -> None:
    values = dict(part.split("=", 1) for part in header.split(","))
    timestamp = values["t"]
    if abs(time.time() - int(timestamp)) > 30 * 60:
        raise ValueError("Stale webhook signature")

    expected = hmac.new(
        secret.encode(),
        timestamp.encode() + b"." + raw_body,
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(expected, values["v0"]):
        raise ValueError("Invalid webhook signature")
```

```typescript
import { createHmac, timingSafeEqual } from "node:crypto";

export function verifySignature(rawBody: Buffer, header: string, secret: string): void {
  const values = Object.fromEntries(header.split(",").map((part) => part.split("=", 2)));
  const timestamp = values.t;
  if (!timestamp || Math.abs(Date.now() / 1000 - Number(timestamp)) > 30 * 60) {
    throw new Error("Stale webhook signature");
  }

  const expected = createHmac("sha256", secret).update(`${timestamp}.`).update(rawBody).digest();
  const received = Buffer.from(values.v0 ?? "", "hex");
  if (received.length !== expected.length || !timingSafeEqual(expected, received)) {
    throw new Error("Invalid webhook signature");
  }
}
```

## Delivery behavior

ElevenLabs makes three in-process delivery attempts at approximately 0, 0.5, and 2 seconds. A `2xx` response marks delivery successful.

The reply URL must use HTTPS. Local development also permits loopback HTTP URLs such as `http://127.0.0.1:8765/webhook`.

Request bodies are limited to 256 KiB.
