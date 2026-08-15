---
title: "Image & Video webhooks"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/image-and-video/webhooks.md
path: docs/eleven-api/guides/how-to/image-and-video/webhooks
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Image & Video webhooks

**How-to guide** · Assumes you have completed the [Image & Video
quickstart](/docs/eleven-api/guides/cookbooks/image-and-video).

## Overview

Video generations can take several minutes, which makes polling expensive to hold open. Opt a
generation into webhook delivery and ElevenLabs sends a `flows_generation` event to your endpoint
once the generation reaches `completed` or `failed`.

The event payload is the terminal response of the corresponding GET endpoint, so a handler that
already understands the polling response needs no separate parsing path.

## Before you begin

Webhook delivery uses the webhooks your workspace has subscribed to generation events. Setting one
up takes two steps: create the webhook, then subscribe it to the event.

#### Create a webhook

Go to [**Developers** > **Webhooks**](https://elevenlabs.io/app/developers/webhooks) and create a
webhook with a publicly reachable HTTPS callback URL. Keep the signing secret it returns; you
need it to verify incoming events.

#### Subscribe it to generation events

Under **Select events to listen to**, tick **Image & Video API generation completed**. A webhook
that exists but is not subscribed to this event is never called.

You can do the same through the API by passing the `flows` event to
[Update workspace webhook](/docs/api-reference/webhooks/update):

```json
{
  "events": ["flows"]
}
```

Creating and subscribing webhooks requires the Webhooks Manage permission, or workspace admin. A
single event accepts up to 10 webhooks; beyond that the request fails with `too_many_webhooks`.

A generation that requests webhook delivery when no webhook is subscribed to generation events is
rejected, so a result is never generated with nowhere to deliver it.

## Request webhook delivery

Add a `webhook` object to the create request. Use `{"type": "all"}` to deliver to every webhook
subscribed to generation events, which keeps the request stable as webhooks are added or replaced.

```python
from elevenlabs import VideoGenerationRequest_Veo31FastGenerate001, WebhookTarget_All

generation = elevenlabs.flows.video.create(
    request=VideoGenerationRequest_Veo31FastGenerate001(
        prompt="A corgi rides a tiny surfboard across a sunlit wave at golden hour, cinematic",
        duration_secs=8,
        webhook=WebhookTarget_All(),
    )
)
```

```typescript
const generation = await elevenlabs.flows.video.create({
  modelId: "veo-3.1-fast-generate-001",
  prompt: "A corgi rides a tiny surfboard across a sunlit wave at golden hour, cinematic",
  durationSecs: 8,
  webhook: { type: "all" },
});
```

To target specific webhooks instead, set the `webhook` field to a list of IDs. Each ID must be one
of the workspace's webhooks subscribed to generation events.

```json
{
  "webhook": {
    "type": "ids",
    "ids": ["Q8mVr2LpXcT4nB6yJdKw"]
  }
}
```

The create request validates the target before starting the generation and returns an error when
delivery would not be possible:

| Error status             | Cause                                                                         |
| ------------------------ | ----------------------------------------------------------------------------- |
| `no_webhooks_configured` | Delivery to all webhooks was requested, but the workspace has none.           |
| `invalid_webhook_id`     | A listed webhook is not subscribed to generation events, or no longer exists. |
| `webhook_disabled`       | A targeted webhook is disabled, manually or automatically after failures.     |

## Webhook payload

A completed generation delivers the output URL and MIME type:

```json
{
  "type": "flows_generation",
  "event_timestamp": 1739721600,
  "data": {
    "id": "JWr5N6X9ZTqf8jD2LmQb",
    "status": "completed",
    "content_url": "https://storage.googleapis.com/generations/JWr5N6X9ZTqf8jD2LmQb",
    "content_mime_type": "video/mp4"
  }
}
```

A failed generation delivers the failure category and message instead:

```json
{
  "type": "flows_generation",
  "event_timestamp": 1739721600,
  "data": {
    "id": "JWr5N6X9ZTqf8jD2LmQb",
    "status": "failed",
    "failure_reason": "timeout",
    "error_message": "Timed out while processing. You were not charged for this generation."
  }
}
```

Branch on `data.status` to decide which fields are present. The two terminal statuses are the only
ones a webhook can carry, since delivery happens only when a generation finishes.

`content_url` is a signed URL that expires roughly an hour after the event is sent. Download the
media promptly, or fetch the generation again for a fresh URL.

## Handle the event

A handler verifies the signature, checks the event type, then branches on `data.status`. This
example downloads the output of a completed generation and logs the reason for a failed one.

```python maxLines=0
# server.py
import os

import requests
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.errors import BadRequestError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

load_dotenv()

app = FastAPI()
elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")


@app.post("/webhook/flows")
async def receive_generation(request: Request):
    payload = await request.body()
    signature = request.headers.get("elevenlabs-signature")

    try:
        event = elevenlabs.webhooks.construct_event(
            rawBody=payload.decode("utf-8"),
            sig_header=signature,
            secret=WEBHOOK_SECRET,
        )
    except BadRequestError:
        return JSONResponse(content={"error": "Invalid signature"}, status_code=401)

    # construct_event returns a parsed dict, not an object with attributes.
    if event.get("type") != "flows_generation":
        return {"status": "ignored"}

    generation = event["data"]
    if generation["status"] == "completed":
        media = requests.get(generation["content_url"]).content
        with open(f"{generation['id']}.mp4", "wb") as f:
            f.write(media)
    else:
        print(f"Generation {generation['id']} failed: {generation['failure_reason']}")

    return {"status": "received"}
```

```typescript maxLines=0
// server.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import express from "express";
import { writeFile } from "fs/promises";

const elevenlabs = new ElevenLabsClient();
const app = express();

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;

// The raw body is required: verification runs over the exact bytes sent.
app.post("/webhook/flows", express.raw({ type: "application/json" }), async (req, res) => {
  const signature = req.headers["elevenlabs-signature"] as string;

  let event;
  try {
    event = await elevenlabs.webhooks.constructEvent(
      req.body.toString(),
      signature,
      WEBHOOK_SECRET
    );
  } catch {
    return res.status(401).json({ error: "Invalid signature" });
  }

  if (event.type !== "flows_generation") {
    return res.status(200).json({ received: true });
  }

  const generation = event.data;
  if (generation.status === "completed") {
    const response = await fetch(generation.content_url);
    await writeFile(`${generation.id}.mp4`, Buffer.from(await response.arrayBuffer()));
  } else {
    console.error(`Generation ${generation.id} failed: ${generation.failure_reason}`);
  }

  res.status(200).json({ received: true });
});

app.listen(3000);
```

Both examples download inside the request for brevity. A large video takes long enough that this can
outlast the delivery timeout, so in production hand the generation ID to a queue and return 2xx
immediately. The signed URL is valid for about an hour, which is ample for a background worker.

To receive events on a local server during development, expose it with a tunnel such as
[ngrok](https://ngrok.com/) and use the HTTPS URL it gives you as the webhook's callback URL.

## Verify the signature

The handler above calls `construct_event` / `constructEvent`, which verifies the
`ElevenLabs-Signature` header, validates the timestamp, and parses the payload in one step. Always
verify before trusting an event.

It is important for the listener to validate all incoming webhooks. Webhooks currently support authentication via HMAC signatures. Set up HMAC authentication by:

* Securely storing the shared secret generated upon creation of the webhook
* Verifying the ElevenLabs-Signature header in your endpoint using the SDK

The JavaScript SDK exposes `constructEvent`; the Python SDK exposes `construct_event` with **`rawBody`**, **`sig_header`**, and **`secret`** (these are not named `payload` / `signature` in Python). Both verify the signature, validate the timestamp, and parse the JSON payload.

#### Python

Example webhook handler using FastAPI:

```python
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from elevenlabs.client import ElevenLabs
from elevenlabs.errors import BadRequestError
import os

load_dotenv()

app = FastAPI()
elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

@app.post("/webhook")
async def receive_message(request: Request):
    payload = await request.body()
    signature = request.headers.get("elevenlabs-signature")

    try:
        event = elevenlabs.webhooks.construct_event(
            rawBody=payload.decode("utf-8"),
            sig_header=signature,
            secret=WEBHOOK_SECRET,
        )
    except BadRequestError as e:
        return JSONResponse(content={"error": "Invalid signature"}, status_code=401)

    # construct_event returns a dict (parsed JSON), not an object with attributes
    if event.get("type") == "post_call_transcription":
        print(f"Received transcription: {event.get('data')}")

    return {"status": "received"}
```

#### JavaScript

#### Express

Example webhook handler using Express:

```javascript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import express from 'express';

const app = express();

const elevenlabs = new ElevenLabsClient();
const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;

// Use express.text() to preserve raw body for signature verification
app.post('/webhook', express.text({ type: 'application/json' }), async (req, res) => {
  const signature = req.headers['elevenlabs-signature'];
  const payload = req.body; // Raw string body

  let event;
  try {
    event = await elevenlabs.webhooks.constructEvent(payload, signature, WEBHOOK_SECRET);
  } catch (error) {
    return res.status(401).json({ error: 'Invalid signature' });
  }

  // Process the webhook event
  if (event.type === 'post_call_transcription') {
    console.log('Received transcription:', event.data);
  }

  res.status(200).json({ received: true });
});
```

#### Next.js

Example webhook handler using Next.js API route:

```typescript app/api/webhook/route.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient();
const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;

export async function POST(req: NextRequest) {
  const body = await req.text();
  const signature = req.headers.get('elevenlabs-signature');

  let event;
  try {
    event = await elevenlabs.webhooks.constructEvent(body, signature, WEBHOOK_SECRET);
  } catch (error) {
    return NextResponse.json({ error: 'Invalid signature' }, { status: 401 });
  }

  // Process the webhook event
  if (event.type === 'post_call_transcription') {
    console.log('Received transcription:', event.data);
  }

  return NextResponse.json({ received: true }, { status: 200 });
}
```

## Delivery behavior

Each generation delivers exactly one terminal event per targeted webhook. Delivery is independent of
the generation itself: a webhook that fails or is unreachable does not affect the result, which
stays available from the GET endpoint and in the list response.

Return a 2xx status promptly from your handler. Repeated failures auto-disable a webhook, and a
disabled webhook causes subsequent generations that target it to be rejected at create time. Design
the handler to be idempotent and use the generation `id` to deduplicate.

For workflows where a missed result is not acceptable, treat webhooks as the fast path and reconcile
periodically with `flows.image.list` or `flows.video.list`, filtering on `status`.

## Next steps

#### [References and assets](/docs/eleven-api/guides/how-to/image-and-video/references)

Guide a generation with a previous generation, an uploaded asset, or inline media.

#### [Webhook configuration](/docs/eleven-api/resources/webhooks)

Create, secure, and manage webhooks for your workspace.

#### [API reference](/docs/api-reference/flows/image/create)

Explore the image, video and asset endpoints.
