---
title: "Seedance 2.5 quickstart"
source: https://docs.together.ai/docs/seedance2.5-quickstart
path: docs/seedance2.5-quickstart
---

Generate multi-shot videos with synchronized audio from text, image, video, and audio inputs.

Seedance 2.5 is a unified multimodal audio-video generation model from ByteDance. It accepts text, image, video, and audio inputs in any combination, and produces multi-shot videos up to 30 seconds with synchronized audio (dialogue, ambient sound, and effects). Compared to Seedance 2.0, it supports longer videos, longer prompts, and far more reference inputs per request.

| Feature                    | Limit                     |
| -------------------------- | ------------------------- |
| Reference images           | Up to 30                  |
| Reference videos           | Up to 10                  |
| Reference audios           | Up to 10                  |
| Frame images (first, last) | Up to two                 |
| Duration                   | 4 to 30 seconds (integer) |
| Resolutions                | 480p, 720p                |
| Audio output               | Always generated          |

The model API string is `ByteDance/Seedance-2.5`.

## Text-to-video

Generate a video from a text prompt. Video generation is asynchronous: you create a job, receive a job ID, and poll for the result.

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      model="ByteDance/Seedance-2.5",
      resolution="720p",
      seconds="5",
  )

  print(f"Job ID: {job.id}")

  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print(f"Error: {status.error}")
          break

      time.sleep(15)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      model: "ByteDance/Seedance-2.5",
      resolution: "720p",
      seconds: "5",
    });

    console.log(`Job ID: ${job.id}`);

    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log(`Error: ${JSON.stringify(status.error)}`);
        break;
      }

      await new Promise((resolve) => setTimeout(resolve, 15000));
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.xyz/v2/videos" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "ByteDance/Seedance-2.5",
      "prompt": "A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      "resolution": "720p",
      "seconds": "5"
    }'
  ```
</CodeGroup>

Seedance 2.5 always generates synchronized audio. The `settings.audio` toggle that Seedance 2.0 supports for producing silent videos is not honored by Seedance 2.5.

## Image-to-video

Animate a still image by passing it as the first frame through `media.frame_images`.

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A black cat curiously gazes up at the sky. The camera slowly rises from eye level to a bird's-eye view.",
      model="ByteDance/Seedance-2.5",
      resolution="720p",
      seconds="5",
      media={
          "frame_images": [
              {
                  "input_image": "https://example.com/cat.png",
                  "frame": "first",
              }
          ],
      },
  )

  print(f"Job ID: {job.id}")

  while True:
      status = client.videos.retrieve(job.id)
      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print(f"Error: {status.error}")
          break
      time.sleep(15)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A black cat curiously gazes up at the sky. The camera slowly rises from eye level to a bird's-eye view.",
      model: "ByteDance/Seedance-2.5",
      resolution: "720p",
      seconds: "5",
      media: {
        frame_images: [{
          input_image: "https://example.com/cat.png",
          frame: "first",
        }],
      },
    });

    console.log(`Job ID: ${job.id}`);

    while (true) {
      const status = await together.videos.retrieve(job.id);
      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log(`Error: ${JSON.stringify(status.error)}`);
        break;
      }
      await new Promise((resolve) => setTimeout(resolve, 15000));
    }
  }

  main();
  ```
</CodeGroup>

## First and last frame control

Pass two `frame_images` (one with `frame: "first"`, one with `frame: "last"`) to control both the starting and ending frames. The model generates smooth motion between the two keyframes.

<CodeGroup>
  ```python Python theme={null}
  job = client.videos.create(
      prompt="Smooth cinematic transition with natural motion.",
      model="ByteDance/Seedance-2.5",
      resolution="720p",
      seconds="5",
      media={
          "frame_images": [
              {"input_image": "https://example.com/start.png", "frame": "first"},
              {"input_image": "https://example.com/end.png", "frame": "last"},
          ],
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const job = await together.videos.create({
    prompt: "Smooth cinematic transition with natural motion.",
    model: "ByteDance/Seedance-2.5",
    resolution: "720p",
    seconds: "5",
    media: {
      frame_images: [
        { input_image: "https://example.com/start.png", frame: "first" },
        { input_image: "https://example.com/end.png", frame: "last" },
      ],
    },
  });
  ```
</CodeGroup>

<Note>
  If you pass one image without `frame`, it's used as the first frame. If you pass two without `frame`, they're used as first and last in order.
</Note>

## Reference-guided generation

Generate video featuring specific characters, objects, or scenes by passing reference images, reference videos, or both. Seedance 2.5 maintains identity, style, and composition from the references throughout the generated video. Multiple references combine for multi-character scenes.

<CodeGroup>
  ```python Python theme={null}
  job = client.videos.create(
      prompt="A person dances on a neon-lit stage with dynamic camera motion.",
      model="ByteDance/Seedance-2.5",
      resolution="720p",
      seconds="6",
      media={
          "reference_images": [
              "https://example.com/character.png",
              "https://example.com/outfit.png",
          ],
          "reference_videos": [
              {"video": "https://example.com/dance-style.mp4"},
          ],
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const job = await together.videos.create({
    prompt: "A person dances on a neon-lit stage with dynamic camera motion.",
    model: "ByteDance/Seedance-2.5",
    resolution: "720p",
    seconds: "6",
    media: {
      reference_images: [
        "https://example.com/character.png",
        "https://example.com/outfit.png",
      ],
      reference_videos: [
        { video: "https://example.com/dance-style.mp4" },
      ],
    },
  });
  ```
</CodeGroup>

## Audio-guided generation

Drive video generation with an audio file by passing it through `media.reference_audios`. The model synchronizes the generated video to the audio, which is useful for lip sync, beat-matched motion, and narration-driven scenes. Pair the audio with a reference image or reference video to anchor the visual subject.

<CodeGroup>
  ```python Python theme={null}
  job = client.videos.create(
      prompt="The character raps energetically into a microphone, bobbing with the beat.",
      model="ByteDance/Seedance-2.5",
      resolution="720p",
      seconds="10",
      media={
          "reference_images": [
              "https://example.com/rapper.png",
          ],
          "reference_audios": [
              "https://example.com/rap-audio.mp3",
          ],
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const job = await together.videos.create({
    prompt: "The character raps energetically into a microphone, bobbing with the beat.",
    model: "ByteDance/Seedance-2.5",
    resolution: "720p",
    seconds: "10",
    media: {
      reference_images: [
        "https://example.com/rapper.png",
      ],
      reference_audios: [
        "https://example.com/rap-audio.mp3",
      ],
    },
  });
  ```
</CodeGroup>

<Note>
  If no reference audio is provided, Seedance 2.5 still generates synchronized audio (dialogue, ambient sound, and effects) based on the prompt and visual content.
</Note>

## Parameters

| Parameter    | Type   | Description                                                         | Default      |
| ------------ | ------ | ------------------------------------------------------------------- | ------------ |
| `prompt`     | string | Text description of the video to generate (2 to 10,000 characters). | **Required** |
| `model`      | string | `ByteDance/Seedance-2.5`.                                           | **Required** |
| `resolution` | string | Output resolution tier: `480p` or `720p`.                           | `"720p"`     |
| `seconds`    | string | Video duration in seconds, integer between 4 and 30.                | `"5"`        |
| `media`      | object | Media inputs for the request (see below).                           | -            |

<Note>
  Unlike Seedance 2.0, Seedance 2.5 does not support the `ratio`, `width`, and `height` parameters, the `1080p` and `4k` resolution tiers, or disabling audio output. Output is capped at 720p.
</Note>

### Media object

The `media` object is the unified way to pass images, videos, and audio into a Seedance 2.5 request.

```json theme={null}
{
  "prompt": "...",
  "model": "ByteDance/Seedance-2.5",
  "media": {
    "frame_images": [],
    "reference_images": [],
    "reference_videos": [],
    "reference_audios": []
  }
}
```

| Field              | Type  | Description                                                                                                                                                                                                                              |
| ------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `frame_images`     | array | Up to two keyframe images. Each item: `{input_image, frame}` where `frame` is `"first"` or `"last"`. With one item and no `frame`, it's used as the first frame. With two items and no `frame`, they're used as first and last in order. |
| `reference_images` | array | Up to 30 reference images for character, object, or scene consistency. Each item is a URL or base64-encoded image.                                                                                                                       |
| `reference_videos` | array | Up to 10 reference videos for motion or composition guidance. Each item: `{video: "url"}`.                                                                                                                                               |
| `reference_audios` | array | Up to 10 reference audio files to drive video generation. Each item is a URL.                                                                                                                                                            |

<Note>
  Reference videos outside the supported duration range are rejected with `invalidDuration`, and the error message states the allowed range. Trim your clip before submitting the job. For example, `ffmpeg -i input.mp4 -t 5 -c copy reference.mp4` produces a 5-second reference clip.
</Note>

### Input compatibility

`frame_images` cannot be combined with any reference input. Use one of the following modes per request:

| Mode             | `frame_images` | `reference_images` | `reference_videos` | `reference_audios` |
| ---------------- | :------------: | :----------------: | :----------------: | :----------------: |
| Text-to-video    |        -       |          -         |          -         |          -         |
| Image-to-video   |    Up to two   |          -         |          -         |          -         |
| Reference-guided |        -       |      Up to 30      |      Up to 10      |          -         |
| Audio-guided     |        -       |      Up to 30      |      Up to 10      |      Up to 10      |

## Pricing

| Resolution | Price                 |
| ---------- | --------------------- |
| 480p       | \$0.115 / second      |
| 720p       | from \$0.249 / second |

## Prompting tips

<Tip>
  Seedance 2.5 supports both Chinese and English prompts. Detailed prompts with subject, action, style, camera movement, and atmosphere produce the best results.
</Tip>

Write descriptive prompts. Instead of "a cat walking", try "A small black cat walks gracefully through a sunlit garden, soft bokeh background, gentle breeze rustling the flowers, cinematic slow motion."

For multi-shot scenes, describe the transitions explicitly. Seedance 2.5 follows shot-by-shot instructions like "Shot 1: wide aerial of the city. Shot 2: cut to a close-up of the protagonist's face." Camera moves such as pans, dollies, and orbits can be requested directly in the prompt.

## Next steps

* [Video generation overview](/docs/inference/videos/overview) for the full parameter reference and supported models.
* [API reference: create video](/reference/create-videos) for REST API details.
* [API reference: get video status](/reference/get-videos-id) for polling and status codes.
