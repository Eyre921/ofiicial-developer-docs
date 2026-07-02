---
title: "Wan 2.7 quickstart"
source: https://docs.together.ai/docs/wan2.7-quickstart
path: docs/wan2.7-quickstart
---

Generate videos from text, images, and reference materials with the Wan 2.7 model family.

## Wan 2.7

Wan 2.7 is a family of video generation models supporting text-to-video, image-to-video with keyframe control, reference-based character/object consistency, and video editing. All models output 720P or 1080P video at 30fps in MP4 format.

| Model                  | API String                | Best For                                                     | Duration  |
| ---------------------- | ------------------------- | ------------------------------------------------------------ | --------- |
| **Wan 2.7 T2V**        | `Wan-AI/wan2.7-t2v`       | Text-to-video with audio                                     | Up to 15s |
| **Wan 2.7 I2V**        | `Wan-AI/wan2.7-i2v`       | Image-to-video, keyframe control, video continuation         | Up to 15s |
| **Wan 2.7 R2V**        | `Wan-AI/wan2.7-r2v`       | Character/object consistency from reference images or videos | Up to 10s |
| **Wan 2.7 Video Edit** | `Wan-AI/wan2.7-videoedit` | Instruction-based editing, style transfer                    | Up to 10s |

## Text-to-Video

Generate a video from a text prompt. Video generation is asynchronous — you create a job, receive a job ID, and poll for the result.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      model="Wan-AI/wan2.7-t2v",
      resolution="720P",
      ratio="16:9",
      seconds="10",
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      model: "Wan-AI/wan2.7-t2v",
      resolution: "720P",
      ratio: "16:9",
      seconds: "10",
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v2/videos" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Wan-AI/wan2.7-t2v",
      "prompt": "A small cute cartoon kitten general in golden armor stands on a cliff, commanding an army of mice charging below. Epic ancient war atmosphere, dramatic clouds over snowy mountains.",
      "resolution": "720P",
      "ratio": "16:9",
      "seconds": "10"
    }'
  ```
</CodeGroup>

## Text-to-Video with Audio

Drive video generation with an audio file using `media.audio_inputs`. The model synchronizes the generated video to the audio — useful for lip sync, beat-matched motion, or narration-driven scenes. If no audio is provided, the model automatically generates matching background music or sound effects.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A graffiti character comes to life off a concrete wall, rapping energetically under an urban railway bridge at night, lit by a lone streetlamp.",
      model="Wan-AI/wan2.7-t2v",
      resolution="720P",
      ratio="16:9",
      seconds="10",
      media={
          "audio_inputs": [
              "https://example.com/rap-audio.mp3",
          ],
      },
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A graffiti character comes to life off a concrete wall, rapping energetically under an urban railway bridge at night, lit by a lone streetlamp.",
      model: "Wan-AI/wan2.7-t2v",
      resolution: "720P",
      ratio: "16:9",
      seconds: "10",
      media: {
        audio_inputs: [
          "https://example.com/rap-audio.mp3",
        ],
      },
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```
</CodeGroup>

<Note>
  Audio constraints: WAV or MP3 format, 3-30 seconds, up to 15 MB. If the audio is longer than the video duration, it will be truncated. If shorter, the remaining portion of the video will be silent.
</Note>

## Image-to-Video

Animate a still image by using it as the first frame. Pass images via `media.frame_images` with `frame` set to `"first"` or `"last"`.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A black cat curiously gazes up at the sky. The camera slowly rises from eye level to a bird's-eye view, capturing the cat's curious eyes.",
      model="Wan-AI/wan2.7-i2v",
      resolution="720P",
      ratio="16:9",
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
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print(f"Error: {status.error}")
          break

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A black cat curiously gazes up at the sky. The camera slowly rises from eye level to a bird's-eye view, capturing the cat's curious eyes.",
      model: "Wan-AI/wan2.7-i2v",
      resolution: "720P",
      ratio: "16:9",
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
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log(`Error: ${JSON.stringify(status.error)}`);
        break;
      }

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v2/videos" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Wan-AI/wan2.7-i2v",
      "prompt": "A black cat curiously gazes up at the sky. The camera slowly rises from eye level to an overhead view.",
      "media": {
        "frame_images": [
          {
            "input_image": "https://example.com/cat.png",
            "frame": "first"
          }
        ]
      }
    }'
  ```
</CodeGroup>

## First and Last Frame Control

Provide both a starting and ending frame to control the video's transition. The model generates smooth motion between the two keyframes.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="Smooth cinematic transition with natural motion",
      model="Wan-AI/wan2.7-i2v",
      resolution="720P",
      ratio="16:9",
      seconds="5",
      media={
          "frame_images": [
              {"input_image": "https://example.com/start.png", "frame": "first"},
              {"input_image": "https://example.com/end.png", "frame": "last"},
          ],
      },
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "Smooth cinematic transition with natural motion",
      model: "Wan-AI/wan2.7-i2v",
      resolution: "720P",
      ratio: "16:9",
      seconds: "5",
      media: {
        frame_images: [
          { input_image: "https://example.com/start.png", frame: "first" },
          { input_image: "https://example.com/end.png", frame: "last" },
        ],
      },
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```
</CodeGroup>

## Video Continuation

Continue from an existing video clip using `media.frame_videos`. The model generates new content that seamlessly extends the input video.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A dog wearing sunglasses skateboarding down a street, 3D cartoon style.",
      model="Wan-AI/wan2.7-i2v",
      resolution="720P",
      ratio="16:9",
      seconds="15",
      media={
          "frame_videos": [
              {"video": "https://example.com/skateboarding-clip.mp4"},
          ],
      },
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A dog wearing sunglasses skateboarding down a street, 3D cartoon style.",
      model: "Wan-AI/wan2.7-i2v",
      resolution: "720P",
      ratio: "16:9",
      seconds: "15",
      media: {
        frame_videos: [
          { video: "https://example.com/skateboarding-clip.mp4" },
        ],
      },
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```
</CodeGroup>

## Reference-to-Video

Generate video featuring a specific person or object by providing reference images or videos via `media.reference_images` or `media.reference_videos`. The model maintains the character's appearance throughout the generated video. Multiple references can be passed for multi-character scenes.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A person dancing on stage",
      model="Wan-AI/wan2.7-r2v",
      resolution="1080P",
      ratio="16:9",
      seconds="5",
      media={
          "reference_videos": [
              {"video": "https://example.com/character-reference.mp4"},
          ],
      },
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A person dancing on stage",
      model: "Wan-AI/wan2.7-r2v",
      resolution: "1080P",
      ratio: "16:9",
      seconds: "5",
      media: {
        reference_videos: [
          { video: "https://example.com/character-reference.mp4" },
        ],
      },
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v2/videos" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Wan-AI/wan2.7-r2v",
      "prompt": "A person dancing on stage",
      "resolution": "1080P",
      "seconds": 10,
      "media": {
        "reference_videos": [
          {"video": "https://example.com/character-reference.mp4"}
        ]
      }
    }'
  ```
</CodeGroup>

## Video Editing

Edit an existing video with text instructions using `media.source_video`. Optionally pass `media.reference_images` to guide the edit with a visual reference.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="Replace the background with the ocean",
      model="Wan-AI/wan2.7-videoedit",
      resolution="720P",
      ratio="16:9",
      media={
          "source_video": "https://example.com/input-video.mp4",
      },
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

      time.sleep(60)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "Replace the background with the ocean",
      model: "Wan-AI/wan2.7-videoedit",
      resolution: "720P",
      ratio: "16:9",
      media: {
        source_video: "https://example.com/input-video.mp4",
      },
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

      await new Promise((resolve) => setTimeout(resolve, 60000));
    }
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v2/videos" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Wan-AI/wan2.7-videoedit",
      "prompt": "Replace the background with the ocean",
      "resolution": "720P",
      "media": {
        "source_video": "https://example.com/input-video.mp4"
      }
    }'
  ```
</CodeGroup>

## Parameters

| Parameter         | Type    | Description                                                             | Default      |
| ----------------- | ------- | ----------------------------------------------------------------------- | ------------ |
| `prompt`          | string  | Text description of the video to generate (up to 5,000 characters)      | **Required** |
| `model`           | string  | Model identifier (see model table above)                                | **Required** |
| `resolution`      | string  | Video resolution tier (`720P`, `1080P`)                                 | `"1080P"`    |
| `ratio`           | string  | Aspect ratio (`16:9`, `9:16`, `1:1`, `4:3`, `3:4`)                      | `"16:9"`     |
| `seconds`         | string  | Video duration in seconds. T2V and I2V: 2-15. R2V and Video Edit: 2-10. | `"5"`        |
| `seed`            | integer | Random seed for reproducibility (0-2,147,483,647)                       | Random       |
| `negative_prompt` | string  | Elements to exclude from generation (up to 500 characters)              | -            |
| `media`           | object  | Media inputs for the request (see schema and compatibility below)       | -            |

### Media Object

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

| Field              | Type   | Description                                                                                                                               |
| ------------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `frame_images`     | array  | Keyframe images for I2V. Each item: `{input_image, frame}` where `frame` is `"first"` or `"last"`.                                        |
| `frame_videos`     | array  | Input video clips for video continuation (I2V). Each item: `{video: "url"}`.                                                              |
| `reference_images` | array  | Reference images for character/object consistency (R2V) or visual guidance (Video Edit).                                                  |
| `reference_videos` | array  | Reference videos for character/object consistency (R2V). Each item: `{video: "url"}`.                                                     |
| `source_video`     | string | Source video URL to edit (Video Edit).                                                                                                    |
| `audio_inputs`     | array  | Audio file URLs to drive generation — lip sync, beat-matched motion, etc. (T2V, I2V). Each item: `"url"`. WAV or MP3, 3-30s, up to 15 MB. |

### Media Compatibility by Model

Not all `media` fields are supported on every model. Unsupported fields are rejected.

| `media` field      | T2V    | I2V                     | R2V      | Video Edit        |
| ------------------ | ------ | ----------------------- | -------- | ----------------- |
| `frame_images`     | -      | First and/or last frame | -        | -                 |
| `frame_videos`     | -      | Single video clip       | -        | -                 |
| `reference_images` | -      | -                       | Multiple | Single            |
| `reference_videos` | -      | -                       | Multiple | -                 |
| `source_video`     | -      | -                       | -        | Single (required) |
| `audio_inputs`     | Single | Single                  | -        | -                 |

## Prompting Tips

<Tip>
  Wan 2.7 supports both Chinese and English prompts. Detailed, descriptive prompts produce the best results — include subject, action, style, camera movement, and atmosphere.
</Tip>

**Write descriptive prompts:** Instead of "a cat walking," try "A small black cat walks gracefully through a sunlit garden, soft bokeh background, gentle breeze rustling the flowers, cinematic slow motion."

**Use negative prompts** to avoid common artifacts:

```
low resolution, errors, worst quality, low quality, incomplete, extra fingers, bad proportions, blurry, distorted
```

**Control aspect ratio and resolution:** Use `resolution` and `ratio` to set output dimensions:

| Aspect Ratio | 720P Dimensions | 1080P Dimensions |
| ------------ | --------------- | ---------------- |
| 16:9         | 1280x720        | 1920x1080        |
| 9:16         | 720x1280        | 1080x1920        |
| 1:1          | 960x960         | 1440x1440        |
| 4:3          | 1104x832        | 1648x1248        |
| 3:4          | 832x1104        | 1248x1648        |

## Next Steps

* [Video Generation Overview](/docs/inference/videos/overview) — Full parameter reference and supported models
* [API Reference: Create Video](/reference/create-videos) — REST API details
* [API Reference: Get Video Status](/reference/get-videos-id) — Polling and status codes
