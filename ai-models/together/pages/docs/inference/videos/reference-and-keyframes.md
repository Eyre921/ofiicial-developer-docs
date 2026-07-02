---
title: "Reference images and keyframes"
source: https://docs.together.ai/docs/inference/videos/reference-and-keyframes
path: docs/inference/videos/reference-and-keyframes
---

Guide visual style with reference images and control specific frames in your video.

Use reference images to steer a video's visual style, and use keyframes to pin specific frames to a known image.

## Reference images

Guide your video's visual style with reference images:

<CodeGroup>
  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A cat dancing energetically",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds="6",
      reference_images=[
          "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ],
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
    const job = await together.videos.create({
      prompt: "A cat dancing energetically",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: "6",
      reference_images: [
        "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ]
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

## Keyframe control

Control specific frames in your video for precise transitions.

Set a single frame (the first frame, in the example below) to a specific image. Depending on the model, you can also set multiple keyframes.

<CodeGroup>
  ```python Python theme={null}
  import base64
  import requests
  import time
  from together import Together

  client = Together()

  # Download image and encode to base64
  image_url = (
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
  )
  response = requests.get(image_url)
  base64_image = base64.b64encode(response.content).decode("utf-8")

  # Single keyframe at start
  job = client.videos.create(
      prompt="Smooth transition from day to night",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      fps=24,
      frame_images=[{"input_image": base64_image, "frame": 0}],  # Starting frame
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
  import * as fs from 'fs';
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Load and encode your image
    const imageBuffer = fs.readFileSync('keyframe.jpg');
    const base64Image = imageBuffer.toString('base64');

    // Single keyframe at start
    const job = await together.videos.create({
      prompt: "Smooth transition from day to night",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      fps: 24,
      frame_images: [
        {
          input_image: base64Image,
          frame: 0  // Starting frame
        }
      ]
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

<Tip>Frame number = seconds × fps.</Tip>
