---
title: "Audio input for videos"
source: https://docs.together.ai/docs/inference/videos/audio-input
path: docs/inference/videos/audio-input
---

Drive video generation with an audio file for lip sync, beat-matched motion, or narration.

For models that support audio-driven generation (such as Wan 2.7 T2V), pass an audio file via the `media.audio_inputs` field. The model synchronizes the generated video to the audio, which is useful for lip sync, beat-matched motion, or narration-driven scenes.

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A cartoon kitten general in golden armor stands on a cliff, commanding an army",
      model="Wan-AI/wan2.7-t2v",
      resolution="720P",
      ratio="16:9",
      seconds="10",
      media={
          "audio_inputs": ["https://download.samplelib.com/mp3/sample-3s.mp3"]
      },
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

      time.sleep(60)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A cartoon kitten general in golden armor stands on a cliff, commanding an army",
      model: "Wan-AI/wan2.7-t2v",
      resolution: "720P",
      ratio: "16:9",
      seconds: "10",
      media: {
        audio_inputs: ["https://download.samplelib.com/mp3/sample-3s.mp3"]
      },
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

      await new Promise(resolve => setTimeout(resolve, 60000));
    }
  }

  main();
  ```
</CodeGroup>

If no audio is provided, the model automatically generates matching background music or sound effects based on the video content.

<Note>
  **Audio constraints:** WAV or MP3 format, 3 to 30 seconds, up to 15 MB. Audio longer than the video is truncated; audio shorter than the video leaves the remaining portion silent.
</Note>
