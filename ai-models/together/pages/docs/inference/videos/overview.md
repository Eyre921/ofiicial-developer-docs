---
title: "Generate videos"
source: https://docs.together.ai/docs/inference/videos/overview
path: docs/inference/videos/overview
---

Generate videos from text and image prompts.

<Tip>Using a coding agent? Install the [together-video](https://github.com/togethercomputer/skills/tree/main/skills/together-video) skill to let your agent write correct video generation code automatically. See [agent skills](/docs/agent-skills) for details.</Tip>

## Generate a video

Video generation is asynchronous: you create a job, receive a job ID, and poll for completion.

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  # Create a video generation job
  job = client.videos.create(
      prompt="A serene sunset over the ocean with gentle waves",
      model="minimax/video-01-director",
      width=1366,
      height=768,
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(60)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Create a video generation job
    const job = await together.videos.create({
      prompt: "A serene sunset over the ocean with gentle waves",
      model: "minimax/video-01-director",
      width: 1366,
      height: 768,
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 60000));
    }
  }

  main();
  ```
</CodeGroup>

Example output when the job is complete:

```json theme={null}
{
  "id": "019a0068-794a-7213-90f6-cc4eb62e3da7",
  "model": "minimax/video-01-director",
  "status": "completed",
  "size": "1366x768",
  "seconds": "6",
  "outputs": {
    "cost": 0.28,
    "video_url": "https://api.together.ai/shrt/DwlaBdSakNRFlBxN"
  },
  "created_at": "2025-10-20T06:57:18.154804Z",
  "completed_at": "2025-10-20T07:00:12.234472Z"
}
```

When a job fails, the response includes an `error` object instead of `outputs`:

```json theme={null}
{
  "id": "019a0068-794a-7213-90f6-cc4eb62e3da7",
  "model": "minimax/hailuo-02",
  "status": "failed",
  "error": {
    "message": "Unsupported use of 'negativePrompt' parameter. ...",
    "code": "unsupportedParameter"
  },
  "outputs": null
}
```

**Job status reference:**

| Status        | Description                               |
| ------------- | ----------------------------------------- |
| `queued`      | Job is waiting in queue.                  |
| `in_progress` | Video is being generated.                 |
| `completed`   | Generation successful, video available.   |
| `failed`      | Generation failed, check `error.message`. |
| `cancelled`   | Job was cancelled.                        |

## Supported models

For the current list of video models, including duration, resolution, FPS, and keyframe support per model, see the [serverless catalog](/docs/serverless/models) or the [dedicated model inference catalog](/docs/dedicated-endpoints/models).

## Troubleshooting

### Video doesn't match prompt well

* Increase `guidance_scale` to 8-10.
* Make prompt more descriptive and specific.
* Add `negative_prompt` to exclude unwanted elements.

### Video has artifacts

* Reduce `guidance_scale` (keep below 12).
* Increase `steps` to 30-40.
* Adjust `fps` if motion looks unnatural.

### Generation is too slow

* Reduce `steps` (try 10-20 for testing).
* Use shorter `seconds` during development.
* Lower `fps` for slower-paced scenes.

### URLs expire

* Download videos immediately after completion.
* Don't rely on URLs for long-term storage.

## Next steps

* [Video generation parameters](/docs/inference/videos/parameters): full parameter reference, plus guidance scale and quality control.
* [Reference images and keyframes](/docs/inference/videos/reference-and-keyframes): guide visual style and control specific frames.
* [Video audio input](/docs/inference/videos/audio-input): drive generation with an audio file for lip sync and beat-matched motion.
