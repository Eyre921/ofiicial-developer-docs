---
title: "Video generation with Wan 2.1"
source: https://docs.together.ai/docs/dedicated_containers_video
path: docs/dedicated_containers_video
---

Deploy a multi-GPU video generation model on Together's managed GPU infrastructure using dedicated containers.

This example demonstrates deploying a multi-GPU video generation model using Dedicated Containers. You'll build a Sprocket worker that uses `torchrun` for distributed inference across multiple GPUs and deploy it to Together's managed infrastructure.

## What you'll learn

* Deploying multi-GPU models with Sprocket and Jig
* Using `use_torchrun=True` for distributed inference
* Automatic file upload with `FileOutput`
* Submitting jobs via the Queue API and polling for results

## Requirements

* **Together API key**: Get one from [together.ai](https://together.ai)
* **Dedicated Containers access**: Contact [support@together.ai](mailto:support@together.ai) to enable for your organization
* **Docker**: For building container images. [Install Docker](https://docs.docker.com/engine/install)
* **Together CLI**: Install with `pip install "together[cli]" --upgrade` or `uv tool install "together[cli]"`

Set your API key:

```shell theme={null}
export TOGETHER_API_KEY=your_key_here
```

Install Together library:

<CodeGroup>
  ```shell pip theme={null}
  pip install together
  ```

  ```shell uv theme={null}
  uv add together
  ```
</CodeGroup>

## Overview

This example deploys a Wan 2.1 text-to-video model as a Dedicated Container with multi-GPU support. The Sprocket worker handles distributed inference across 2 GPUs, and Together manages provisioning, autoscaling, and observability.

**Output specs:**

* Resolution: 480×832
* Frames: 81 (5.4 seconds at 15fps)
* Format: MP4

**Why multi-GPU?**

* Video generation requires significant VRAM for temporal attention
* Context parallelism splits the sequence dimension across GPUs
* 2x H100 allows comfortable generation without memory pressure

## How it works

1. **Build** – Jig builds a Docker image from your `pyproject.toml` configuration
2. **Push** – The image is pushed to Together's private container registry
3. **Deploy** – Together provisions 2x H100 GPUs and starts your container
4. **Torchrun** – Sprocket's `use_torchrun=True` launches child processes (one per GPU)
5. **Queue** – Jobs are submitted to the managed queue, broadcast to all GPU ranks, and processed in parallel

## Project structure

```
sprocket_wan2.1/
├── pyproject.toml    # Configuration and dependencies
└── run_wan.py        # Distributed Sprocket worker
```

## Implementation

### Sprocket worker code

<CodeGroup>
  ```python run_wan.py theme={null}
  from typing import Optional

  import torch
  import torch.distributed as dist
  from diffusers import WanPipeline
  from diffusers.utils import export_to_video
  from para_attn.context_parallel import init_context_parallel_mesh
  from para_attn.context_parallel.diffusers_adapters import parallelize_pipe

  import sprocket


  class WanSprocket(sprocket.Sprocket):
      def setup(self) -> None:
          dist.init_process_group()
          torch.cuda.set_device(dist.get_rank())

          pipe = WanPipeline.from_pretrained("Wan-AI/Wan2.1-T2V-1.3B-Diffusers")
          self.pipe = pipe.to("cuda")

          para_mesh = init_context_parallel_mesh(self.pipe.device.type)
          parallelize_pipe(self.pipe, mesh=para_mesh)

      def predict(self, args: dict) -> Optional[dict]:
          video = self.pipe(
              prompt=args["prompt"],
              negative_prompt="",
              height=480,
              width=832,
              num_frames=81,
              num_inference_steps=int(args.get("num_inference_steps", 30)),
              output_type="pil" if dist.get_rank() == 0 else "pt",
          ).frames[0]

          if dist.get_rank() == 0:
              print("Saving video to output.mp4")
              export_to_video(video, "output.mp4", fps=15)
              return {"url": sprocket.FileOutput("output.mp4")}


  if __name__ == "__main__":
      sprocket.run(WanSprocket(), use_torchrun=True)
  ```
</CodeGroup>

### Configuration

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [project]
  name = "sprocket-wan"
  version = "0.1.0"
  dependencies = [
      "diffusers==0.33.0",
      "transformers==4.48.3",
      "para_attn==0.3.38",
      "ftfy==6.3.1",
      "accelerate==1.13.0",
      "einops==0.8.2",
      "omegaconf==2.3.0",
      "pillow==12.2.0",
      "ffmpeg-python==0.2.0",
      "opencv-python==4.13.0.92",
      "torch==2.6.0",
      "sprocket==0.1.4",
  ]

  [[tool.uv.index]]
  name = "together-pypi"
  url = "https://pypi.together.ai/"

  [tool.uv.sources]
  sprocket = { index = "together-pypi" }

  [tool.jig.image]
  python_version = "3.11"
  system_packages = ["libgl1", "libglx-mesa0", "ffmpeg"]
  cmd = "python3 run_wan.py --queue"
  auto_include_git = false
  copy = ["run_wan.py"]

  [tool.jig.deploy]
  description = "Wan2.1 Video Generation with Sprocket"
  gpu_type = "h100-80gb"
  gpu_count = 2
  cpu = 4
  memory = 32
  port = 8000
  min_replicas = 1
  max_replicas = 1
  termination_grace_period_seconds = 600
  ```
</CodeGroup>

## Key concepts

### How `use_torchrun=True` works

When you call `sprocket.run(..., use_torchrun=True)`, Sprocket handles multi-GPU orchestration automatically.

**Flow:**

1. Parent process receives a job from Together's queue
2. Job payload is broadcast to all child processes via Unix socket
3. Each rank executes `setup()` once at startup, then `predict()` for each job
4. Ranks synchronize via NCCL during forward pass
5. Only rank 0 saves output and returns result
6. Parent uploads `FileOutput` and reports job completion

### Distributed process initialization

Each worker process must initialize its distributed context before loading the model:

```python theme={null}
def setup(self) -> None:
    # Required: Initialize the process group for NCCL communication
    dist.init_process_group()

    # Required: Set the correct GPU for this rank
    torch.cuda.set_device(dist.get_rank())

    # Now load and parallelize the model...
```

When `use_torchrun=True` is passed to `sprocket.run()`, Sprocket launches torchrun internally, which sets `RANK`, `LOCAL_RANK`, `WORLD_SIZE`, and other environment variables.

### Rank 0 output pattern

In distributed inference, only rank 0 should handle I/O and return results:

```python theme={null}
def predict(self, args: dict) -> Optional[dict]:
    # Generate on all ranks (synchronized via NCCL)
    video = self.pipe(
        prompt=args["prompt"],
        # Rank 0 needs PIL for saving; others use tensors (less memory)
        output_type="pil" if dist.get_rank() == 0 else "pt",
    ).frames[0]

    # Only rank 0 saves and returns
    if dist.get_rank() == 0:
        export_to_video(video, "output.mp4", fps=15)
        return {"url": sprocket.FileOutput("output.mp4")}

    # Other ranks implicitly return None
```

**Why this pattern?**

* Avoids duplicate file writes
* Reduces memory on non-rank-0 GPUs (tensor output vs PIL)
* Sprocket collects output from rank 0 only

### Automatic file upload with `FileOutput`

Wrapping a path in `FileOutput` triggers automatic upload:

```python theme={null}
return {"url": sprocket.FileOutput("output.mp4")}
```

**What happens:**

1. Sprocket detects the `FileOutput` in the response
2. Uploads the file to Together's storage
3. Replaces `FileOutput` with the access URL in the final response

The client receives (when polling job status):

```json theme={null}
{
  "request_id": "req_abc123",
  "status": "done",
  "outputs": {
    "url": "https://..."
  }
}
```

### Multi-GPU configuration

For multi-GPU deployments, configure `gpu_count` in your deployment settings and pass `use_torchrun=True` to `sprocket.run()`:

```toml theme={null}
[tool.jig.deploy]
gpu_count = 2  # Sprocket launches one process per GPU automatically
```

Sprocket handles launching `torchrun` internally. You don't need to include it in your `cmd`. It coordinates the parent process and GPU workers automatically.

## Deployment

### Deploy

<CodeGroup>
  ```shell Shell theme={null}
  # Deploy (builds, pushes, and creates deployment)
  tg beta jig deploy

  # Or deploy with cache warmup to reduce cold start latency
  tg beta jig deploy --warmup

  # Monitor startup
  tg beta jig logs --follow
  ```
</CodeGroup>

### Check deployment status

<CodeGroup>
  ```shell Shell theme={null}
  # View deployment status and replica health
  tg beta jig status
  ```
</CodeGroup>

Wait until the deployment shows `running` and replicas are ready before submitting jobs.

### Submit jobs

Jobs are submitted to the managed queue and processed asynchronously. Video generation typically takes 30-75 seconds depending on settings.

<CodeGroup>
  ```python Python SDK theme={null}
  from together import Together
  import time

  client = Together()
  deployment = "sprocket-wan2.1"

  # Submit job to queue
  job = client.beta.jig.queue.submit(
      model=deployment,
      payload={
          "prompt": "A serene lake at sunset with mountains in the background",
          "num_inference_steps": 30,
      },
  )
  print(f"Job submitted: {job.request_id}")

  # Poll for completion
  while True:
      status = client.beta.jig.queue.retrieve(
          request_id=job.request_id,
          model=deployment,
      )

      print(f"Status: {status.status}")

      if status.status == "done":
          print(f"Video URL: {status.outputs['url']}")
          break
      elif status.status == "failed":
          print(f"Job failed: {status.error}")
          break

      time.sleep(5)
  ```

  ```python requests theme={null}
  import requests
  import time

  api_key = "your_key_here"
  deployment = "sprocket-wan2.1"

  # Submit job to queue
  response = requests.post(
      "https://api.together.ai/v1/queue/submit",
      headers={"Authorization": f"Bearer {api_key}"},
      json={
          "model": deployment,
          "payload": {
              "prompt": "A cat playing with a ball of yarn",
              "num_inference_steps": 30,
          },
      },
  )
  job = response.json()
  print(f"Job submitted: {job['request_id']}")

  # Poll for completion
  while True:
      status_response = requests.get(
          f"https://api.together.ai/v1/queue/status?request_id={job['request_id']}&model={deployment}",
          headers={"Authorization": f"Bearer {api_key}"},
      )
      status = status_response.json()

      print(f"Status: {status['status']}")

      if status["status"] == "done":
          print(f"Video URL: {status['outputs']['url']}")
          break
      elif status["status"] == "failed":
          print(f"Job failed: {status.get('error')}")
          break

      time.sleep(5)
  ```

  ```shell cURL theme={null}
  # Submit job
  curl -X POST https://api.together.ai/v1/queue/submit \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sprocket-wan2.1",
      "payload": {
        "prompt": "A serene lake at sunset with mountains in the background",
        "num_inference_steps": 30
      }
    }'

  # Response: {"request_id": "req_abc123", "status": "pending"}

  # Poll for result (replace REQUEST_ID with actual value)
  curl "https://api.together.ai/v1/queue/status?request_id=REQUEST_ID&model=sprocket-wan2.1" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"

  # When status is "done", the video URL is in outputs.url
  ```
</CodeGroup>

## Input parameters

| Parameter             | Type   | Default  | Description                                                 |
| --------------------- | ------ | -------- | ----------------------------------------------------------- |
| `prompt`              | string | Required | Text description of the video to generate                   |
| `num_inference_steps` | int    | `30`     | Number of denoising steps (higher = better quality, slower) |

## Output

When the job completes, the status response contains:

```json theme={null}
{
  "request_id": "req_abc123",
  "status": "done",
  "outputs": {
    "url": "https://..."
  }
}
```

* `url`: URL to the generated MP4 video file (480×832, 81 frames, 15fps). Authenticated with your API key.

### Scaling to more GPUs

To scale for higher throughput, increase `max_replicas` to add more workers:

```toml theme={null}
[tool.jig.deploy]
min_replicas = 1
max_replicas = 10

[tool.jig.deploy.autoscaling]
metric = "QueueBacklogPerWorker"
target = 1.05
```

To scale to zero when idle, specify `min_replicas = 0` (saves costs but adds cold start latency).

## Cleanup

When you're done, delete the deployment:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig destroy
  ```
</CodeGroup>

## Next steps

* [Image Generation Example](/docs/dedicated_containers_image) – Single-GPU inference with Flux2
* [Quickstart](/docs/containers-quickstart) – Deploy your first container in 20 minutes
* [Sprocket SDK](/reference/dci-reference-sprocket) – Full SDK reference for workers
* [Jig CLI Reference](/reference/cli/jig) – CLI commands and configuration options
* [Deployments API Reference](/reference/deployments-list) – REST API for deployments, secrets, storage, and queues
