---
title: "References and assets"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/image-and-video/references.md
path: docs/eleven-api/guides/how-to/image-and-video/references
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# References and assets

**How-to guide** · Assumes you have completed the [Image & Video quickstart](/docs/eleven-api/guides/cookbooks/image-and-video).

## Overview

Most Image & Video models accept media alongside the prompt: a first frame for a video, images to
edit, audio to lip-sync against. Every media-valued field on the API takes a reference object rather
than raw bytes in a fixed shape, and each reference is tagged with a `type` that says where the
media comes from.

| `type`          | Points at                                                    | Fields                        |
| --------------- | ------------------------------------------------------------ | ----------------------------- |
| `generation`    | The output of another generation, finished or still running. | `generation_id`               |
| `asset`         | A file uploaded to the assets API.                           | `asset_id`                    |
| `inline_base64` | Media encoded directly into the request body.                | `content_base64`, `mime_type` |

The three kinds are interchangeable wherever a reference is accepted, so the same field can take a
generation on one request and an uploaded asset on the next.

## Chain one generation into the next

A `generation` reference does not have to point at a generation that has finished. Submit the image,
take the ID out of the response, and pass it straight into the video request without waiting: the
API queues the video behind the image and starts it the moment the image completes. Nothing is
uploaded between the two calls.

Set `webhook` on the last generation in the chain and there is nothing to wait on at all. Both calls
return as soon as their generation is queued, the whole graph runs server-side, and your endpoint is
called once the final generation reaches a terminal status.

```python maxLines=0
from elevenlabs import (
    ImageGenerationRequest_Gemini3ProImage,
    ImageReference_Generation,
    VideoGenerationRequest_Veo31FastGenerate001,
    WebhookTarget_All,
)

still = elevenlabs.flows.image.create(
    request=ImageGenerationRequest_Gemini3ProImage(
        prompt="A lighthouse on a cliff at dawn, heavy fog rolling in from the sea",
        aspect_ratio="16:9",
    )
)

# `still` is still pending here. Submitting now queues the video behind it.
clip = elevenlabs.flows.video.create(
    request=VideoGenerationRequest_Veo31FastGenerate001(
        prompt="The fog thickens and the beam sweeps across the water",
        start_frame=ImageReference_Generation(generation_id=still.id),
        duration_secs=8,
        webhook=WebhookTarget_All(),
    )
)

print(clip.id)
```

```typescript maxLines=0
const still = await elevenlabs.flows.image.create({
  modelId: "gemini-3-pro-image",
  prompt: "A lighthouse on a cliff at dawn, heavy fog rolling in from the sea",
  aspectRatio: "16:9",
});

// `still` is still pending here. Submitting now queues the video behind it.
const clip = await elevenlabs.flows.video.create({
  modelId: "veo-3.1-fast-generate-001",
  prompt: "The fog thickens and the beam sweeps across the water",
  startFrame: { type: "generation", generationId: still.id },
  durationSecs: 8,
  webhook: { type: "all" },
});

console.log(clip.id);
```

Only the last generation needs `webhook`. Setting it on the image as well delivers an event for the
intermediate result too, which is useful for reporting progress but is not needed to drive the
chain. As elsewhere, the field requires a webhook subscribed to generation events; see [Image & Video webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks) to set one up.

Without an endpoint to receive callbacks, drop `webhook` and poll the end of the chain instead. The
intermediate image still needs no polling of its own — wait once, on the last generation, at the
interval for its modality, which for video is no more than once every 10 seconds. See [Polling guidelines](/docs/eleven-api/guides/cookbooks/image-and-video#polling-guidelines).

```python
import time

while True:
    result = elevenlabs.flows.video.get(clip.id)
    if result.status in ("completed", "failed"):
        break
    time.sleep(10)
```

```typescript
let result = await elevenlabs.flows.video.get(clip.id);
while (result.status === "pending" || result.status === "generating") {
  await new Promise((resolve) => setTimeout(resolve, 10000));
  result = await elevenlabs.flows.video.get(clip.id);
}
```

A generation that references unfinished work is created immediately and sits in `pending` until
everything it references has finished, with no further action needed from you to start it. Chains
can be any depth and any width — a generation may wait on several references, each itself still
waiting — so an entire graph can be submitted in one pass and collected only at its leaves. Time
spent queued does not count against the generation's timeout.

If a referenced generation fails, the dependent never runs: it fails with a `dependency_failed`
reason and takes anything queued behind it with it. Nothing in the collapsed chain is charged — a
generation that was already paid for is refunded, and one whose price depends on a referenced
output that does not exist yet, such as a lip-sync priced by the duration of a pending audio
generation, is only charged once it starts. A `generation_id` that does not exist in your workspace
is rejected on the create call itself, so a typo surfaces immediately rather than as a failed
generation.

## Upload media as an asset

Upload a file to the assets API when the media comes from outside ElevenLabs and you want to reuse
it across generations. Assets belong to the workspace and persist until you delete them.

```python
from elevenlabs import ImageReference_Asset, VideoGenerationRequest_Veo31FastGenerate001

with open("lighthouse.png", "rb") as f:
    asset = elevenlabs.assets.create(asset=f, name="lighthouse.png")

print(asset.asset_id)

clip = elevenlabs.flows.video.create(
    request=VideoGenerationRequest_Veo31FastGenerate001(
        prompt="The beam sweeps across the water as the fog thickens",
        start_frame=ImageReference_Asset(asset_id=asset.asset_id),
    )
)
```

```typescript
import { createReadStream } from "fs";

const asset = await elevenlabs.assets.create({
  asset: createReadStream("lighthouse.png"),
  name: "lighthouse.png",
});

console.log(asset.assetId);

const clip = await elevenlabs.flows.video.create({
  modelId: "veo-3.1-fast-generate-001",
  prompt: "The beam sweeps across the water as the fog thickens",
  startFrame: { type: "asset", assetId: asset.assetId },
});
```

The upload response describes the stored asset:

```json
{
  "asset_id": "5xM2KqOnZyce22SPZ9d4",
  "name": "lighthouse.png",
  "mime_type": "image/png",
  "created_at_unix": 1721520000,
  "content_url": "https://storage.googleapis.com/assets/5xM2KqOnZyce22SPZ9d4"
}
```

`content_url` is a signed URL valid for about an hour, and is `null` while the upload is still being
processed. Fetch the asset again for a fresh URL.

Reaching the assets API with an API key requires a Pro plan or above, the same tier as the
generation endpoints.

### Storage limits

Uploaded assets count against a total storage limit for the workspace, which depends on your plan:

| Plan       | Asset storage |
| ---------- | ------------- |
| Pro        | 11 GB         |
| Scale      | 33 GB         |
| Business   | 111 GB        |
| Enterprise | 333 GB        |

Only the files you upload count toward the limit; generated outputs do not. An upload that would
take the workspace over its limit is rejected with an `asset_storage_limit_exceeded` error before
the file is read. Delete assets you no longer need to free space, or contact support to have the
limit raised.

### Manage assets

List assets newest first, optionally filtering by name, and page through results with the cursor
from the previous response. `page_size` accepts 1 to 100 and defaults to 30.

```python
page = elevenlabs.assets.list(page_size=20, search="lighthouse")

for asset in page.assets:
    print(asset.asset_id, asset.name, asset.mime_type)

if page.has_more:
    page = elevenlabs.assets.list(page_size=20, search="lighthouse", cursor=page.next_cursor)
```

```typescript
let page = await elevenlabs.assets.list({ pageSize: 20, search: "lighthouse" });

for (const asset of page.assets) {
  console.log(asset.assetId, asset.name, asset.mimeType);
}

if (page.hasMore) {
  page = await elevenlabs.assets.list({
    pageSize: 20,
    search: "lighthouse",
    cursor: page.nextCursor,
  });
}
```

Retrieve or delete a single asset by ID. Deleting an asset does not affect generations that already
used it.

```python
asset = elevenlabs.assets.get("5xM2KqOnZyce22SPZ9d4")
elevenlabs.assets.delete("5xM2KqOnZyce22SPZ9d4")
```

```typescript
const asset = await elevenlabs.assets.get("5xM2KqOnZyce22SPZ9d4");
await elevenlabs.assets.delete("5xM2KqOnZyce22SPZ9d4");
```

## Pass media inline

An `inline_base64` reference carries the media in the request body, which avoids a separate upload
for one-off inputs. Encode the file with the standard base64 alphabet and declare its MIME type.

```python
import base64

from elevenlabs import ImageGenerationRequest_GptImage2, ImageReference_InlineBase64

with open("headshot.jpg", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

generation = elevenlabs.flows.image.create(
    request=ImageGenerationRequest_GptImage2(
        prompt="Replace the background with a softly lit studio backdrop",
        images=[
            ImageReference_InlineBase64(
                content_base64=encoded,
                mime_type="image/jpeg",
            )
        ],
    )
)
```

```typescript
import { readFile } from "fs/promises";

const encoded = (await readFile("headshot.jpg")).toString("base64");

const generation = await elevenlabs.flows.image.create({
  modelId: "gpt-image-2",
  prompt: "Replace the background with a softly lit studio backdrop",
  images: [
    {
      type: "inline_base64",
      contentBase64: encoded,
      mimeType: "image/jpeg",
    },
  ],
});
```

Inline media is stored as an ephemeral asset with no retention guarantee and may be deleted once
the generation completes. Upload the file to the assets API instead when you need to reference the
same input more than once.

Inline content is capped at 25MB per reference after decoding. Larger files belong on the assets
API, which accepts much bigger uploads and does not pay the base64 size penalty. Each modality
accepts a fixed set of MIME types:

| Reference | Accepted `mime_type`                                                |
| --------- | ------------------------------------------------------------------- |
| Image     | `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif` |
| Audio     | `audio/mpeg`, `audio/wav`                                           |
| Video     | `video/mp4`, `video/quicktime`, `video/webm`                        |

## Reference fields by model

Reference fields are named for the role the media plays. `start_frame` and `end_frame` are single
images that bound a video, `image` and `audio` are the required inputs of a lip-sync model, and the
bare plurals `images`, `videos`, and `audios` are free-form reference material the model draws from.

Which fields a model accepts, and which combinations are valid, differ per model. An `end_frame`
always requires a `start_frame`. Violating a constraint returns a validation error naming the
offending field, so the generation never starts and is never charged.

### Veo 3.1

Both Veo models accept `start_frame`, `end_frame`, and up to three entries in `images`. Unlike other
models, each entry in `images` wraps the reference together with the role it plays:

```json
{
  "images": [
    {
      "image": { "type": "asset", "asset_id": "5xM2KqOnZyce22SPZ9d4" },
      "role": "subject"
    },
    {
      "image": { "type": "asset", "asset_id": "7pQ4LnBvXkR2mT9wYcHd" },
      "role": "style"
    }
  ]
}
```

A `subject` reference places the image's subject or scene elements into the video; a `style`
reference transfers its visual style. Reference images cannot be combined with `start_frame` or
`end_frame`, and require the eight-second duration.

### Seedance

ByteDance models are disabled by default and require explicit approval before use. Enterprise
customers can contact support to request access.

The three Seedance 2.0 tiers accept `start_frame`, `end_frame`, up to 9 `images`, up to 3 `videos`,
and up to 3 `audios`, subject to these constraints:

* References cannot be combined with `start_frame` or `end_frame`.
* Reference audio requires at least one reference image or video, for example to drive lip-sync.
* The combined number of reference files must not exceed 12.

Seedance 2.5 raises the caps to 30 `images`, 10 `videos`, and 10 `audios` with no combined total,
and drops the rule that reference audio needs an accompanying image or video, so audio-only input is
accepted. References still cannot be combined with `start_frame` or `end_frame`.

### GPT Image

The GPT Image models accept a `mask` alongside `images`. Fully transparent areas of the mask mark
where the first reference image may be edited. A mask without reference images is rejected.

## Next steps

#### [Webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks)

Receive the result of a generation instead of polling for it.

#### [Image & Video overview](/docs/overview/capabilities/image-video)

Compare model capabilities, supported formats, and availability.

#### [API reference](/docs/api-reference/flows/image/create)

Explore the image, video and asset endpoints.
