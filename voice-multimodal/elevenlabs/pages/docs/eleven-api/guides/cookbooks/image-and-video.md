---
title: "Image & Video quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/image-and-video.md
path: docs/eleven-api/guides/cookbooks/image-and-video
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Image & Video quickstart

The Image & Video API is asynchronous. You submit a generation, and once it finishes you download the result from a signed URL. Images and videos have separate endpoints, but the request and response shapes are the same for both.

There are two ways to collect the result. [Webhook delivery](/docs/eleven-api/guides/how-to/image-and-video/webhooks) is the recommended one, and what the examples below use: ElevenLabs calls your endpoint the moment a generation reaches a terminal status, so nothing is spent waiting. Polling is the fallback for when you have no endpoint to receive a callback, and each example shows how to drop back to it.

The Image & Video API requires a Pro plan or above. Calls from a workspace below that tier are
rejected with a `402 paid_plan_required` error. Your API key must also carry the Image & Video or
Flows permission for the workspace.

## Generate an image

#### Create an API key

[Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

#### Install the SDK

#### SDK

We'll also use the `dotenv` library to load our API key from an environment variable.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

#### CLI

Install the ElevenLabs CLI. Homebrew (macOS) and Scoop (Windows) are recommended.

```bash title="Homebrew (macOS)"
brew install elevenlabs/tap/elevenlabs
```

```powershell title="Scoop (Windows)"
scoop bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop install elevenlabs
```

```bash title="npm"
npm install -g @elevenlabs/cli
```

```bash title="curl"
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh | sh
```

Working with an AI coding assistant? Run `elevenlabs generate-skills` in your project to write a
`SKILL.md` for every command group into `skills/`, so your assistant knows the CLI's full surface
without you pasting docs. Use `--output-dir` to put them elsewhere. This reads the CLI's own
embedded API definition, so it needs no API key and works offline — and it stays in step with
whichever CLI version you have installed.

Then authenticate — this opens your browser to authorize the CLI:

```bash
elevenlabs auth login
```

#### Submit the generation

Each model has its own request class, and the fields on it are the parameters that model
accepts, so switching models can change which fields are available. Unknown fields are rejected
rather than ignored.

`webhook` asks for the finished result to be delivered to your workspace's webhooks, so the call
returns as soon as the generation is queued. It requires a webhook subscribed to generation
events; see [Image & Video webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks) to set one up, or omit the
field and poll instead.

#### SDK

```python
# example.py
import os

from dotenv import load_dotenv
from elevenlabs import ImageGenerationRequest_Gemini3ProImage, WebhookTarget_All
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

generation = elevenlabs.flows.image.create(
    request=ImageGenerationRequest_Gemini3ProImage(
        prompt="A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic",
        aspect_ratio="16:9",
        resolution="2K",
        webhook=WebhookTarget_All(),
    )
)

print(generation.id, generation.status)
```

```typescript
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const generation = await elevenlabs.flows.image.create({
  modelId: "gemini-3-pro-image",
  prompt:
    "A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic",
  aspectRatio: "16:9",
  resolution: "2K",
  webhook: { type: "all" },
});

console.log(generation.id, generation.status);
```

#### CLI

The CLI submits the same request as JSON, then polls until the generation completes and downloads the result:

```bash
# 1. Submit the generation (note the returned id)
elevenlabs flows image create --json '{
  "model_id": "gemini-3-pro-image",
  "prompt": "A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic",
  "aspect_ratio": "16:9",
  "resolution": "2K"
}'

# 2. Poll until the status is "completed"
elevenlabs flows image get --generation-id <id> --query status

# 3. Read the signed content URL, then download the image
elevenlabs flows image get --generation-id <id> --query content_url
curl -o corgi.png "<content_url>"
```

The response contains the generation ID and nothing else. A newly created generation is always
`pending`:

```json
{
  "id": "JWr5N6X9ZTqf8jD2LmQb",
  "status": "pending"
}
```

#### Collect the result

Because the request opted into `webhook`, ElevenLabs posts a `flows_generation` event to your
endpoint once the generation reaches `completed` or `failed`. The event's `data` is identical to
what the GET endpoint returns, and
[Image & Video webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks) walks through
the handler that receives it.

Without an endpoint to receive callbacks, drop `webhook` from the request above and poll instead.
Fetch the generation until its status is `completed` or `failed`, leaving at least two seconds
between requests for an image — see [Polling guidelines](#polling-guidelines) for the intervals
to use per modality.

```python maxLines=0
import time

import requests

while True:
    result = elevenlabs.flows.image.get(generation.id)
    if result.status in ("completed", "failed"):
        break
    time.sleep(2)

if result.status == "failed":
    raise RuntimeError(f"{result.failure_reason}: {result.error_message}")

with open("corgi.png", "wb") as f:
    f.write(requests.get(result.content_url).content)
```

```typescript maxLines=0
import { writeFile } from "fs/promises";

let result = await elevenlabs.flows.image.get(generation.id);

while (result.status === "pending" || result.status === "generating") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  result = await elevenlabs.flows.image.get(generation.id);
}

if (result.status === "failed") {
  throw new Error(`${result.failureReason}: ${result.errorMessage}`);
}

const response = await fetch(result.contentUrl);
await writeFile("corgi.png", Buffer.from(await response.arrayBuffer()));
```

Either way, a completed generation carries the same fields:

```json
{
  "id": "JWr5N6X9ZTqf8jD2LmQb",
  "status": "completed",
  "content_url": "https://storage.googleapis.com/generations/JWr5N6X9ZTqf8jD2LmQb",
  "content_mime_type": "image/png"
}
```

#### Execute the code

```python
python example.py
```

```typescript
npx tsx example.mts
```

The generation is queued and its ID is printed. With webhook delivery the image arrives at your
endpoint; with the polling variant it is saved to `corgi.png`.

## Generate a video

Video generations use `flows.video` and follow the same submit-and-collect pattern. A video can take
several minutes, so this example opts into webhook delivery with `webhook` rather than waiting on
the result.

```python
from elevenlabs import VideoGenerationRequest_Veo31FastGenerate001, WebhookTarget_All

generation = elevenlabs.flows.video.create(
    request=VideoGenerationRequest_Veo31FastGenerate001(
        prompt="A corgi rides a tiny surfboard across a sunlit wave at golden hour, cinematic",
        duration_secs=8,
        aspect_ratio="16:9",
        resolution="1080p",
        generate_audio=True,
        webhook=WebhookTarget_All(),
    )
)

print(generation.id)
```

```typescript
const generation = await elevenlabs.flows.video.create({
  modelId: "veo-3.1-fast-generate-001",
  prompt: "A corgi rides a tiny surfboard across a sunlit wave at golden hour, cinematic",
  durationSecs: 8,
  aspectRatio: "16:9",
  resolution: "1080p",
  generateAudio: true,
  webhook: { type: "all" },
});

console.log(generation.id);
```

The call returns as soon as the generation is queued, and the finished result is delivered to every
webhook in your workspace subscribed to generation events. Video output is MP4, so the completed payload reports a
`content_mime_type` of `video/mp4`. See
[Image & Video webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks) for configuring a
webhook and writing the handler that receives this.

`webhook` requires at least one workspace webhook subscribed to generation events. Without one,
the create call is rejected rather than starting a generation whose result has nowhere to go. Drop
the field to fall back to polling with `flows.video.get`, and poll no more than once every 10
seconds.

## Collecting results

Webhooks and polling return the same payload, so the choice is about how you wait for it rather than
what you get.

|                 | Webhook delivery                                        | Polling                                          |
| --------------- | ------------------------------------------------------- | ------------------------------------------------ |
| Best for        | The default for both modalities, and any production use | Scripts and environments with no public endpoint |
| Requires        | An HTTPS endpoint subscribed to generation events       | Nothing                                          |
| Cost of waiting | None; you are called once the generation finishes       | One request per poll, per generation             |

Use webhooks wherever you can. Reach for polling when you have nowhere to receive a callback, and
follow the intervals below when you do.

### Choosing webhook targets

`webhook` accepts two forms. `WebhookTarget_All` reaches every webhook subscribed to generation
events, which is the right default because it survives webhooks being rotated or replaced.
`WebhookTarget_Ids` narrows delivery to specific webhooks, for when one workspace fans out to several
consumers and a given job should reach only one of them:

```python
from elevenlabs import WebhookTarget_Ids

webhook = WebhookTarget_Ids(ids=["Q8mVr2LpXcT4nB6yJdKw"])
```

```typescript
const webhook = { type: "ids", ids: ["Q8mVr2LpXcT4nB6yJdKw"] };
```

Every ID must already be subscribed to generation events; naming an unsubscribed webhook is
rejected rather than silently ignored. The delivered payload is identical to what the GET endpoint
returns, so a handler written against one works for the other. The
[webhooks guide](/docs/eleven-api/guides/how-to/image-and-video/webhooks) covers configuring a
webhook, verifying the signature, and handling the event.

### Polling guidelines

A generation's runtime depends on the model, the resolution, and, for video, the duration, so poll
on an interval matched to what you asked for rather than on a fixed loop:

* **Images**: poll no more than once every 2 seconds. Most finish within a few seconds.
* **Video**: poll no more than once every 10 seconds. Expect minutes, not seconds, and scale the
  interval with `duration_secs` and `resolution`.

Two rules apply to both. Back off when a generation runs long — doubling the interval up to about a
minute keeps a slow generation from turning into hundreds of requests. And give the loop a ceiling,
so a stuck generation ends as a timeout in your own code rather than an unbounded loop.

Polling faster than this earns you nothing: a generation's status does not change any sooner because
you asked twice. Sustained aggressive polling can return
[429 responses](/docs/eleven-api/resources/errors#rate-limiting-and-concurrency), which you should
handle with exponential backoff.

## Generation lifecycle

A generation moves through four statuses. The two terminal statuses carry different fields, so
branch on `status` before reading the rest of the response.

| Status       | Meaning                                                                             |
| ------------ | ----------------------------------------------------------------------------------- |
| `pending`    | The generation is queued. This is the status of every newly created generation.     |
| `generating` | The model is running.                                                               |
| `completed`  | The output is ready. The response carries `content_url` and `content_mime_type`.    |
| `failed`     | The generation did not produce an output. The response carries the failure details. |

`content_url` is a signed URL that expires roughly an hour after the response is returned. Fetch
the generation again for a fresh URL rather than storing the signed URL itself.

## Handling failures

A failed generation reports a `failure_reason` category alongside a human-readable `error_message`:

```json
{
  "id": "JWr5N6X9ZTqf8jD2LmQb",
  "status": "failed",
  "failure_reason": "moderated",
  "error_message": "The prompt was rejected by content moderation. You were not charged for this generation."
}
```

| `failure_reason`     | Cause                                                               |
| -------------------- | ------------------------------------------------------------------- |
| `timeout`            | The model did not return a result in time.                          |
| `model_error`        | The model provider returned an error or produced no output.         |
| `moderated`          | The prompt or an input was rejected by content moderation.          |
| `invalid_parameters` | The parameters were rejected once the generation reached the model. |
| `dependency_failed`  | A referenced generation this one depends on failed.                 |
| `charging_failed`    | The workspace could not be charged for the generation.              |
| `internal_error`     | An unexpected error occurred.                                       |

Failed generations are not charged. Parameter problems that can be detected up front — an
unsupported field, a value outside a model's allowed range, or an invalid combination of reference
inputs — are rejected by the create request instead, before any generation starts.

## Pricing

Generations are charged in credits. The cost depends on the model, the parameters you choose such as
resolution and duration, and the inputs you provide. A generation costs the same through the API as
it does in the ElevenLabs app, where the cost is shown before you submit. See
[Image & Video in the playground](/docs/eleven-creative/playground/image-video) for how the cost of
a given model and setting combination is presented.

## List your generations

Each endpoint lists the generations created through it, newest first. Results are scoped to your
workspace and to this API, so generations created in the ElevenLabs app do not appear.

```python
page = elevenlabs.flows.image.list(page_size=20, status="completed")

for item in page.generations:
    print(item.id, item.content_url)

while page.has_more:
    page = elevenlabs.flows.image.list(page_size=20, status="completed", cursor=page.next_cursor)
    for item in page.generations:
        print(item.id, item.content_url)
```

```typescript
let page = await elevenlabs.flows.image.list({ pageSize: 20, status: "completed" });

for (const item of page.generations) {
  console.log(item.id, item.contentUrl);
}

while (page.hasMore) {
  page = await elevenlabs.flows.image.list({
    pageSize: 20,
    status: "completed",
    cursor: page.nextCursor,
  });
  for (const item of page.generations) {
    console.log(item.id, item.contentUrl);
  }
}
```

`page_size` accepts 1 to 100 and defaults to 30. Pass `status` to return only generations in one
lifecycle state, and `model_id` to return only generations of a single model. Treat `next_cursor` as
opaque: pass the exact value back and stop when `has_more` is `false`.

## Available models

The API exposes a subset of the models available in the ElevenLabs app. Each model accepts only the
parameters listed for it — sending a field another model supports returns a validation error.

ByteDance models are disabled by default and require explicit approval before use. Until access is
granted, a request naming one of them is rejected with a `model_access_denied` error. Enterprise
customers can contact support to request access.

### Image models

| `model_id`                    | Reference images        | Output controls                                                         |
| ----------------------------- | ----------------------- | ----------------------------------------------------------------------- |
| `gpt-image-1`                 | Up to 5, plus a `mask`  | `aspect_ratio` (1:1, 3:2, 2:3), `quality`, `background`                 |
| `gpt-image-1.5`               | Up to 5, plus a `mask`  | `aspect_ratio` (1:1, 3:2, 2:3), `quality`, `background`                 |
| `gpt-image-2`                 | Up to 10, plus a `mask` | 15 aspect ratios, `resolution` (1K, 2K, 4K), `quality`                  |
| `gemini-2.5-flash-image`      | Up to 5                 | `aspect_ratio`                                                          |
| `gemini-3-pro-image`          | Up to 10                | `aspect_ratio`, `resolution` (1K, 2K, 4K)                               |
| `gemini-3.1-flash-image`      | Up to 14                | `aspect_ratio` (including 1:4, 4:1, 1:8, 8:1), `resolution` (512 to 4K) |
| `gemini-3.1-flash-lite-image` | Up to 14                | `aspect_ratio`, `resolution` (1K)                                       |
| `bytedance-seedream-5-lite`   | Up to 10                | `aspect_ratio`, `resolution` (2K, 3K), `seed`                           |
| `bytedance-seedream-5-pro`    | Up to 10                | `aspect_ratio`, `resolution` (1K, 2K), `seed`                           |

### Video models

| `model_id`                   | Media inputs                                                            | Output controls                                                                                          |
| ---------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `veo-3.1-generate-001`       | `start_frame`, `end_frame`, up to 3 `images` with a `role`              | `duration_secs` (4, 6, 8), `aspect_ratio` (16:9, 9:16), `resolution` (720p, 1080p, 4K), `generate_audio` |
| `veo-3.1-fast-generate-001`  | `start_frame`, `end_frame`, up to 3 `images` with a `role`              | `duration_secs` (4, 6, 8), `aspect_ratio` (16:9, 9:16), `resolution` (720p, 1080p, 4K), `generate_audio` |
| `bytedance-seedance-v2`      | `start_frame`, `end_frame`, up to 9 `images`, 3 `videos`, 3 `audios`    | `duration_secs` (4 to 15), 7 aspect ratios, `resolution` (480p to 4k), `generate_audio`                  |
| `bytedance-seedance-v2-fast` | `start_frame`, `end_frame`, up to 9 `images`, 3 `videos`, 3 `audios`    | `duration_secs` (4 to 15), 7 aspect ratios, `resolution` (480p, 720p), `generate_audio`                  |
| `bytedance-seedance-v2-mini` | `start_frame`, `end_frame`, up to 9 `images`, 3 `videos`, 3 `audios`    | `duration_secs` (4 to 15), 7 aspect ratios, `resolution` (480p, 720p), `generate_audio`                  |
| `bytedance-seedance-v2.5`    | `start_frame`, `end_frame`, up to 30 `images`, 10 `videos`, 10 `audios` | `duration_secs` (4 to 30), 7 aspect ratios, `resolution` (480p, 720p), `generate_audio`                  |
| `creatify-aurora`            | `image` and `audio`, both required                                      | `resolution` (480p, 720p), `guidance_scale`, `audio_guidance_scale`                                      |

For model capabilities, availability, and pricing, see the
[Image & Video overview](/docs/overview/capabilities/image-video).

## Next steps

#### [References and assets](/docs/eleven-api/guides/how-to/image-and-video/references)

Guide a generation with a previous generation, an uploaded asset, or inline media.

#### [Webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks)

Receive the result of a generation instead of polling for it.

#### [API reference](/docs/api-reference/flows/image/create)

Explore the image, video and asset endpoints.
