---
title: "Video generation parameters"
source: https://docs.together.ai/docs/inference/videos/parameters
path: docs/inference/videos/parameters
---

Reference for video generation parameters, including guidance scale and quality control.

A high-level overview of video generation parameters and when to use them. For parameters tied to reference images, keyframes, audio input, or video editing, see [Capability-specific parameters](#capability-specific-parameters) at the bottom.

For the complete schema, including every supported field along with its types and ranges, see the [video generation API reference](/reference/create-videos).

<Note>
  **Available parameters vary by model.** Wan 2.7 models use `resolution` and `ratio` instead of `width` and `height`. Kling requires keyframe images via `media.frame_images` instead of a `prompt`. See the [supported models table](/docs/inference/videos/overview#supported-models) for per-model coverage.
</Note>

## Quick reference

Match the problem you're solving to the parameter most likely to help.

* **Video doesn't match the prompt:** Make the prompt more specific, add a `negative_prompt` for what to exclude, or raise `guidance_scale` toward `9`-`10`.
* **Output looks oversaturated or has weird motion:** Lower `guidance_scale` to `6`-`7`. Avoid values above `12`.
* **Poor visual quality:** Raise `steps` to `30`-`40` for production runs. Diminishing returns past `50`.
* **Generation is too slow or expensive while iterating:** Lower `steps` to `10` for quick previews, and shorten `seconds`.
* **Need the same video every run (evals, regression tests):** Set `seed` to a fixed integer.
* **Wrong dimensions or aspect ratio:** Set `width` and `height` explicitly. On Wan 2.7, set `resolution` and `ratio` instead.
* **Output file is too large:** Raise `output_quality` (higher number means more compression). Lower it for higher fidelity.
* **Need consistent characters or style across the video:** Pass `media.reference_images`. See [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes).
* **Need to pin starting or ending frames:** Pass `media.frame_images`. See [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes).
* **Need lip sync or beat-matched motion:** Pass `media.audio_inputs`. See [Video audio input](/docs/inference/videos/audio-input).

## Prompting

### prompt

A description of the video to generate. Required for every model except Kling. Maximum length is 32,000 characters.

Be specific about subject, action, setting, camera movement, and pacing. Vague prompts produce generic motion. Include verbs and temporal cues ("slowly pans", "the camera tracks left") since video models are sensitive to motion language.

Typical default: required.

### negative\_prompt

A description of what to avoid in the generated video. Useful for excluding common artifacts.

Set it when the model produces unwanted elements (extra limbs, flickering, watermarks). A reasonable starting point: `"blurry, low quality, distorted, flickering"`.

Typical default: unset.

## Output dimensions

### width and height

The size of the generated video in pixels. Available combinations differ by model.

Typical default: `1366` x `768`.

### resolution

A resolution tier used by Wan 2.7 models in place of `width` and `height`. Accepts `"720P"` or `"1080P"`.

Typical default: `"1080P"`.

### ratio

The aspect ratio used by Wan 2.7 models. Accepts `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, or `"3:4"`.

Typical default: `"16:9"`.

## Length and frame rate

### seconds

Clip duration in seconds. Accepted range is `"1"` through `"10"`. Passed as a string.

Longer clips cost more and take longer to generate. Use shorter clips while iterating on prompts and parameters.

Typical default: `"6"`.

### fps

Frames per second. Higher values produce smoother motion at the cost of generation time and file size.

Typical default: `24` (some models accept up to `60`).

## Quality and speed

### steps

The number of denoising steps. More steps generally improve visual quality and temporal consistency at a near-linear cost in latency. Past a model-specific point, additional steps stop helping.

Lower it (`10`) for quick previews. Use `20` for a balanced default. Raise it (`30`-`40`) for production runs. Avoid values above `50`. Range: `10`-`50`.

Typical default: model-specific.

<CodeGroup>
  ```python Python theme={null}
  # Quick preview
  job_quick = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=10,
  )

  # Production quality
  job_production = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=40,
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  // Quick preview
  const jobQuick = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 10
  });

  // Production quality
  const jobProduction = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 40
  });
  ```
</CodeGroup>

### guidance\_scale

Controls how closely the video follows the prompt. Higher values make the model adhere more strictly to the text description. Lower values give the model more creative freedom. Affects both visual content and temporal consistency.

Recommended range is `6.0`-`10.0`. Values above `12` may cause over-guidance artifacts or unnatural motion.

* `6.0`-`7.0`: More creative, less literal.
* `7.0`-`9.0`: Sweet spot for most use cases.
* `9.0`-`10.0`: Strict adherence to the prompt.

Typical default: model-specific.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # Low guidance: more creative interpretation
  job_creative = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=6.0,
      seed=100,
  )

  # High guidance: closer to literal prompt
  job_literal = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=10.0,
      seed=100,
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  // Low guidance: more creative interpretation
  const jobCreative = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 6.0,
    seed: 100
  });

  // High guidance: closer to literal prompt
  const jobLiteral = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 10.0,
    seed: 100
  });
  ```
</CodeGroup>

## Reproducibility

### seed

An integer that fixes the random initialization. With the same `seed`, prompt, model, and parameters, the model returns the same video. Useful for reproducibility and for fair comparisons when tuning other parameters.

Typical default: unset (each call returns a new video).

## Output format

### output\_format

The encoded video format. Accepts `"MP4"` or `"WEBM"`. MP4 is the broadest-compatible default. WEBM produces smaller files but isn't supported by every player.

Typical default: `"MP4"`.

### output\_quality

Compression quality. Lower values produce higher fidelity and larger files. Higher values produce smaller files with more compression artifacts.

Typical default: `20`.

## Audio

### generate\_audio

Whether the model should generate audio for the video. Only applies to models that support audio generation.

Typical default: `false`.

## Capability-specific parameters

| Parameter         | Type    | Description                                                                                                                                                 | Default      |
| ----------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `prompt`          | string  | Text description of the video to generate.                                                                                                                  | **Required** |
| `model`           | string  | Model identifier.                                                                                                                                           | **Required** |
| `width`           | integer | Video width in pixels.                                                                                                                                      | 1366         |
| `height`          | integer | Video height in pixels.                                                                                                                                     | 768          |
| `seconds`         | string  | Length of video (1-10).                                                                                                                                     | `"6"`        |
| `fps`             | integer | Frames per second.                                                                                                                                          | 15-60        |
| `steps`           | integer | Diffusion steps (higher = better quality, slower).                                                                                                          | 10-50        |
| `guidance_scale`  | float   | How closely to follow prompt.                                                                                                                               | 6.0-10.0     |
| `seed`            | integer | Random seed for reproducibility.                                                                                                                            | any          |
| `output_format`   | string  | Video format (MP4, WEBM).                                                                                                                                   | MP4          |
| `output_quality`  | integer | Bitrate/quality (lower = higher quality).                                                                                                                   | 20           |
| `negative_prompt` | string  | What to avoid in generation.                                                                                                                                | -            |
| `frame_images`    | array   | Keyframe images for video generation. If size 1, starting frame; if size 2, starting and ending frame; if more than 2, `frame` must be specified per image. |              |
| `resolution`      | string  | Video resolution tier (`720P`, `1080P`). Used by Wan 2.7 models instead of `width`/`height`.                                                                | `"1080P"`    |
| `ratio`           | string  | Aspect ratio (`16:9`, `9:16`, `1:1`, `4:3`, `3:4`). Used by Wan 2.7 models.                                                                                 | `"16:9"`     |
| `media`           | object  | Media inputs for the request (see schema and compatibility below).                                                                                          | -            |

These parameters belong to features with their own dedicated pages. Each link below covers supported models and end-to-end examples. The full `media` object schema is documented in the next subsection.

* **`media.frame_images`:** Pin specific frames to known images (keyframes). See [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes).
* **`media.reference_images` and `media.reference_videos`:** Steer visual style with references that should appear consistently across the video. See [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes).
* **`media.audio_inputs`:** Drive generation with an audio file for lip sync, beat-matched motion, or narration. See [Video audio input](/docs/inference/videos/audio-input).
* **`media.source_video` and `media.frame_videos`:** Edit or extend an existing clip. Wan 2.7 specific. See the [Wan 2.7 quickstart](/docs/wan2.7-quickstart).

<Note>
  The top-level `frame_images` and `reference_images` parameters are deprecated. Use `media.frame_images` and `media.reference_images` instead.
</Note>

### media object schema

The `media` object is the unified way to pass images, videos, and audio into video generation requests.

```json theme={null}
{
  "prompt": "...",
  "model": "...",
  "media": {
    "frame_images": [],
    "frame_videos": [],
    "reference_images": [],
    "reference_videos": [],
    "source_video": "",
    "audio_inputs": []
  }
}
```

| Field              | Type   | Description                                                                                                                                    |
| ------------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `frame_images`     | array  | Keyframe images for I2V. Each item: `{input_image, frame}` where `frame` is `"first"` or `"last"`.                                             |
| `frame_videos`     | array  | Input video clips for video continuation (I2V). Each item: `{video: "url"}`.                                                                   |
| `reference_images` | array  | Reference images for character or object consistency (R2V) or visual guidance (Video Edit).                                                    |
| `reference_videos` | array  | Reference videos for character or object consistency (R2V). Each item: `{video: "url"}`.                                                       |
| `source_video`     | string | Source video URL to edit (Video Edit).                                                                                                         |
| `audio_inputs`     | array  | Audio file URLs to drive generation (lip sync, beat-matched motion, etc.) for T2V and I2V. Each item: `"url"`. WAV or MP3, 3-30s, up to 15 MB. |

Not all `media` fields are supported on every model. See the [Wan 2.7 quickstart](/docs/wan2.7-quickstart) for field compatibility across Wan 2.7 models.

## See also

* [Video generation overview](/docs/inference/videos/overview): generate a video and poll for completion.
* [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes): guide visual style and pin specific frames.
* [Video audio input](/docs/inference/videos/audio-input): drive generation with an audio file.
