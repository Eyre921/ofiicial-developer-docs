---
title: "Create Video Generation"
source: https://elevenlabs.io/docs/api-reference/flows/video/create.md
path: docs/api-reference/flows/video/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Video Generation

POST https://api.elevenlabs.io/v1/flows/video
Content-Type: application/json

Start a video generation with the selected model.

Reference: https://elevenlabs.io/docs/api-reference/flows/video/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `object`
  - `model_id`: `bytedance-seedance-v2` (BytedanceSeedance2Request)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    - `audios` (list of object, optional) — Up to 3 reference audios, e.g. for lipsync. Requires at least one of `images` or `videos`, and cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineAudioReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded audio.
          - Allowed values: `audio/mpeg`, `audio/wav`
    - `duration_secs` (integer, optional, default: 5) — The duration of the output video in seconds.
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 9 reference images to draw subjects from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `480p`, `720p`, `1080p`, `4k`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `videos` (list of object, optional) — Up to 3 reference videos to draw subjects or motion from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineVideoReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded video.
          - Allowed values: `video/mp4`, `video/quicktime`, `video/webm`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `bytedance-seedance-v2-fast` (BytedanceSeedance2FastRequest)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    - `audios` (list of object, optional) — Up to 3 reference audios, e.g. for lipsync. Requires at least one of `images` or `videos`, and cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineAudioReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded audio.
          - Allowed values: `audio/mpeg`, `audio/wav`
    - `duration_secs` (integer, optional, default: 5) — The duration of the output video in seconds.
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 9 reference images to draw subjects from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `480p`, `720p`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `videos` (list of object, optional) — Up to 3 reference videos to draw subjects or motion from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineVideoReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded video.
          - Allowed values: `video/mp4`, `video/quicktime`, `video/webm`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `bytedance-seedance-v2-mini` (BytedanceSeedance2MiniRequest)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    - `audios` (list of object, optional) — Up to 3 reference audios, e.g. for lipsync. Requires at least one of `images` or `videos`, and cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineAudioReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded audio.
          - Allowed values: `audio/mpeg`, `audio/wav`
    - `duration_secs` (integer, optional, default: 5) — The duration of the output video in seconds.
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 9 reference images to draw subjects from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `480p`, `720p`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `videos` (list of object, optional) — Up to 3 reference videos to draw subjects or motion from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineVideoReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded video.
          - Allowed values: `video/mp4`, `video/quicktime`, `video/webm`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `bytedance-seedance-v2.5` (BytedanceSeedance25Request)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video. With `auto`, the model picks an aspect ratio based on the inputs. First-frame / first-and-last-frame tasks always use `auto`.
      - Allowed values: `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
    - `audios` (list of object, optional) — Up to 10 reference audios, e.g. for lipsync. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineAudioReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded audio.
          - Allowed values: `audio/mpeg`, `audio/wav`
    - `duration_secs` (integer, optional, default: 5) — The duration of the output video in seconds.
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 30 reference images to draw subjects from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `480p`, `720p`
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `videos` (list of object, optional) — Up to 10 reference videos to draw subjects or motion from. Cannot be combined with `start_frame`/`end_frame`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineVideoReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded video.
          - Allowed values: `video/mp4`, `video/quicktime`, `video/webm`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `creatify-aurora` (CreatifyAuroraRequest)
    - `audio` (object, required) — The speech audio to drive the character's lip movements.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineAudioReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded audio.
          - Allowed values: `audio/mpeg`, `audio/wav`
    - `image` (object, required) — The image of the character to animate.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `audio_guidance_scale` (double, optional, nullable) — How strongly the lip movements adhere to the audio. Omit to use the model's default.
    - `guidance_scale` (double, optional, nullable) — How strongly the generation adheres to the input image. Omit to use the model's default.
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `480p`, `720p`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `veo-3.1-fast-generate-001` (Veo3_1FastRequest)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video.
      - Allowed values: `16:9`, `9:16`
    - `duration_secs` (enum, optional, default: 8) — The duration of the output video in seconds.
      - Allowed values: `4`, `6`, `8`
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `enhance_prompt` (boolean, optional, default: true) — Whether the model may rewrite the prompt to improve results.
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 3 reference images to draw subjects or style from. Cannot be combined with `start_frame`/`end_frame`, and requires the 8-second duration.
      - `image` (object, required) — The reference image.
        - `type`: `asset` (StaticAssetReference)
          - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
        - `type`: `generation` (GenerationReference)
          - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
        - `type`: `inline_base64` (InlineImageReference)
          - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
          - `mime_type` (enum, required) — The MIME type of the encoded image.
            - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
      - `role` (enum, required) — How the model uses the image: `subject` places its subject or scene elements into the video; `style` transfers its visual style.
        - Allowed values: `subject`, `style`
    - `negative_prompt` (string, optional, nullable) — A text description of what the video should avoid.
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `720p`, `1080p`, `4K`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `veo-3.1-generate-001` (Veo3_1Request)
    - `prompt` (string, required) — A text description of the video to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output video.
      - Allowed values: `16:9`, `9:16`
    - `duration_secs` (enum, optional, default: 8) — The duration of the output video in seconds.
      - Allowed values: `4`, `6`, `8`
    - `end_frame` (object, optional, nullable) — The image to use as the video's last frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `enhance_prompt` (boolean, optional, default: true) — Whether the model may rewrite the prompt to improve results.
    - `generate_audio` (boolean, optional, default: true) — Whether to generate audio with the video.
    - `images` (list of object, optional) — Up to 3 reference images to draw subjects or style from. Cannot be combined with `start_frame`/`end_frame`, and requires the 8-second duration.
      - `image` (object, required) — The reference image.
        - `type`: `asset` (StaticAssetReference)
          - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
        - `type`: `generation` (GenerationReference)
          - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
        - `type`: `inline_base64` (InlineImageReference)
          - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
          - `mime_type` (enum, required) — The MIME type of the encoded image.
            - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
      - `role` (enum, required) — How the model uses the image: `subject` places its subject or scene elements into the video; `style` transfers its visual style.
        - Allowed values: `subject`, `style`
    - `negative_prompt` (string, optional, nullable) — A text description of what the video should avoid.
    - `resolution` (enum, optional, default: 720p) — The resolution of the output video.
      - Allowed values: `720p`, `1080p`, `4K`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `start_frame` (object, optional, nullable) — The image to use as the video's first frame.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.

## Response

### 200

Successful Response

- `id` (string, required) — The unique identifier of the generation. Pass it to the corresponding GET endpoint to retrieve the output.
- `status` ("pending", required) — A newly created generation is always `pending`.

## Examples

**Request**

```json
{
  "audio": {
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  },
  "image": {
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  },
  "model_id": "string"
}
```

**Response**

```json
{
  "id": "JWr5N6X9ZTqf8jD2LmQb",
  "status": "pending"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.video.create();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.video.create()

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/flows/video"

	payload := strings.NewReader("{\n  \"audio\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"image\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"model_id\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/flows/video")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"audio\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"image\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"model_id\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/flows/video")
  .header("Content-Type", "application/json")
  .body("{\n  \"audio\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"image\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"model_id\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/flows/video', [
  'body' => '{
  "audio": {
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  },
  "image": {
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  },
  "model_id": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/video");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"audio\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"image\": {\n    \"generation_id\": \"JWr5N6X9ZTqf8jD2LmQb\",\n    \"type\": \"string\"\n  },\n  \"model_id\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "audio": [
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  ],
  "image": [
    "generation_id": "JWr5N6X9ZTqf8jD2LmQb",
    "type": "string"
  ],
  "model_id": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/video")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
