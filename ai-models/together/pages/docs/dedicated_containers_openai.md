---
title: "Serve an OpenAI-compatible endpoint"
source: https://docs.together.ai/docs/dedicated_containers_openai
path: docs/dedicated_containers_openai
---

Deploy a custom model behind an OpenAI-compatible endpoint using dedicated containers.

This guide deploys FLUX.2 behind an OpenAI-compatible `/v1/images/generations` endpoint using Sprocket and Jig. Clients call it with the OpenAI SDK or plain HTTP, with no Together-specific request or response shapes.

Two things make a container OpenAI-compatible:

* **HTTP server mode:** Run the worker without the `--queue` flag. Requests go straight to your container and return synchronously, instead of through the managed queue.
* **`predict_path`:** Pass the OpenAI route to `sprocket.run()`. In HTTP server mode the raw JSON request body is passed straight to `predict()`, so `predict()` owns both parsing the OpenAI request and returning the OpenAI response shape.

## Prerequisites

* **Together API key**: Get one from [together.ai](https://together.ai).
* **Dedicated containers access**: Contact [support@together.ai](mailto:support@together.ai) to enable it for your organization.
* **Docker**: For building container images. [Install Docker](https://docs.docker.com/engine/install).
* **Together CLI**: Install with `pip install "together[cli]" --upgrade` or `uv tool install "together[cli]"`.
* **Hugging Face token**: The FLUX.2 weights are gated. Request access to [black-forest-labs/FLUX.2-klein-9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B).

## HTTP server mode vs queue mode

The [image generation example](/docs/dedicated_containers_image) serves the same model family through the managed queue. The difference is entirely in how requests are served:

|                 | Queue mode                                                   | HTTP server mode (this guide)                      |
| --------------- | ------------------------------------------------------------ | -------------------------------------------------- |
| Startup command | `python3 run.py --queue`                                     | `python3 run.py`                                   |
| Request shape   | Your own payload dict                                        | Whatever your route expects (here, OpenAI)         |
| How you call it | `tg beta jig submit`, then poll                              | OpenAI client or `curl` against the endpoint URL   |
| Best for        | Long-running jobs that need durability and progress tracking | Synchronous requests and OpenAI-compatible clients |

## Write the worker

The worker validates the OpenAI Images request with Pydantic, generates the image(s), and returns the OpenAI response shape. The last line sets the endpoint path:

```python run.py theme={null}
import base64
import time
from io import BytesIO
from typing import Literal

import sprocket
import torch
from diffusers import Flux2KleinPipeline
from pydantic import BaseModel, Field, ValidationError

# FLUX.2-klein is distilled for few-step inference.
NUM_INFERENCE_STEPS = 4
GUIDANCE_SCALE = 1.0


class ImageGenerationRequest(BaseModel):
    """The subset of the OpenAI Images API this worker accepts."""

    prompt: str = Field(min_length=1)
    model: str | None = None
    n: int = Field(default=1, ge=1, le=10)
    size: str = Field(default="1024x1024", pattern=r"^\d+x\d+$")
    response_format: Literal["b64_json"] = "b64_json"


class Flux2OpenAISprocket(sprocket.Sprocket):
    def setup(self) -> None:
        self.pipe = Flux2KleinPipeline.from_pretrained(
            "black-forest-labs/FLUX.2-klein-9B",
            torch_dtype=torch.bfloat16,
        ).to("cuda")

    def _generate_one(self, req: ImageGenerationRequest) -> str:
        width, height = (int(d) for d in req.size.split("x"))
        image = self.pipe(
            prompt=req.prompt,
            width=width,
            height=height,
            num_inference_steps=NUM_INFERENCE_STEPS,
            guidance_scale=GUIDANCE_SCALE,
        ).images[0]
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()

    def predict(self, args: dict) -> dict:
        try:
            req = ImageGenerationRequest.model_validate(args)
        except ValidationError as e:
            raise ValueError(f"invalid request: {e}") from e

        return {
            "created": int(time.time()),
            "data": [
                {"b64_json": self._generate_one(req)} for _ in range(req.n)
            ],
        }


if __name__ == "__main__":
    sprocket.run(Flux2OpenAISprocket(), predict_path="/v1/images/generations")
```

Three details to note:

* **`predict_path` sets the route:** Without it, the worker serves `POST /generate`. Setting it to `/v1/images/generations` is what lets OpenAI clients call the deployment unmodified. The path can't collide with the reserved `/health` and `/metrics` routes.
* **`predict()` owns the contract:** Pydantic rejects bad types, out-of-range `n`, or an unsupported `response_format` before generation runs. The returned dict is sent back as the JSON response body, so it must match the OpenAI response shape exactly.
* **`b64_json` only:** Returning base64 keeps the image in the response with no external storage dependency, and it is what `gpt-image-1` itself returns. Serving the `url` response format would require publicly fetchable storage, which this guide doesn't cover.

To support more of the OpenAI Images API (`quality`, `output_format`, `output_compression`), add the fields to `ImageGenerationRequest` and map them to pipeline arguments. Pydantic ignores fields you don't declare, so clients sending extra OpenAI parameters won't get errors.

## Configure the deployment

```toml pyproject.toml theme={null}
[project]
name = "flux2-openai"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "diffusers==0.38.0",
    "transformers==4.57.1",
    "torch==2.6.0",
    "torchvision==0.21.0",
    "pillow==12.2.0",
    "accelerate==1.13.0",
    "safetensors==0.7.0",
    "sprocket>=0.1.6",
    "pydantic==2.12.3",
]

[[tool.uv.index]]
name = "together-pypi"
url = "https://pypi.together.ai/"

[tool.uv.sources]
sprocket = { index = "together-pypi" }

[tool.jig.image]
python_version = "3.11"
cmd = "python3 run.py"
auto_include_git = false
copy = ["run.py"]

[tool.jig.deploy]
description = "FLUX.2 with an OpenAI-compatible endpoint"
gpu_type = "h100-80gb"
gpu_count = 1
cpu = 4
memory = 32
storage = 50
port = 8000
min_replicas = 1
max_replicas = 1
```

Unlike the queue examples, `cmd` has no `--queue` flag. That single difference switches the worker into HTTP server mode. The example also pins one always-on replica so requests never wait for a cold start.

## Set the Hugging Face token

The model weights are gated, so the container needs your Hugging Face token at runtime. Store it as a [secret](/reference/cli/jig#jig-secrets-set):

```shell theme={null}
tg beta jig secrets set --name HF_TOKEN --value <YOUR_HF_TOKEN>
```

## Deploy

```shell theme={null}
# Build, push, and create the deployment
tg beta jig deploy

# Watch startup (the model download takes a few minutes on first deploy)
tg beta jig logs --follow

# Confirm the deployment is running
tg beta jig status
```

Then get the endpoint URL:

```shell theme={null}
tg beta jig endpoint
```

The URL has the form `https://api.together.ai/v1/deployment-request/<DEPLOYMENT_NAME>`. Requests to any path under it are forwarded to your container, authenticated with your Together API key. Your worker never handles auth.

## Call the endpoint

Point any OpenAI client at the endpoint URL plus `/v1`, using your Together API key:

<CodeGroup>
  ```python OpenAI Python SDK theme={null}
  import base64
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.together.ai/v1/deployment-request/flux2-openai/v1",
      api_key=os.environ["TOGETHER_API_KEY"],
  )

  result = client.images.generate(
      model="black-forest-labs/FLUX.2-klein-9B",
      prompt="a cat sitting on a red chair",
      n=1,
      size="1024x1024",
      response_format="b64_json",
  )

  with open("out.png", "wb") as f:
      f.write(base64.b64decode(result.data[0].b64_json))
  ```

  ```bash cURL theme={null}
  curl "$(tg beta jig endpoint)/v1/images/generations" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "black-forest-labs/FLUX.2-klein-9B",
      "prompt": "a cat sitting on a red chair",
      "n": 1,
      "size": "1024x1024",
      "response_format": "b64_json"
    }'
  ```
</CodeGroup>

The response is the standard OpenAI Images shape:

```json theme={null}
{
  "created": 1700000000,
  "data": [{ "b64_json": "iVBORw0KGgoAAAANSUhEUgAA..." }]
}
```

### Supported parameters

| Parameter         | Notes                                                        |
| ----------------- | ------------------------------------------------------------ |
| `prompt`          | Required.                                                    |
| `model`           | Accepted for compatibility. The deployment serves one model. |
| `n`               | 1 to 10, default 1.                                          |
| `size`            | `WIDTHxHEIGHT`, default `1024x1024`.                         |
| `response_format` | Only `b64_json` is supported.                                |

Any other OpenAI parameter is accepted and ignored, so standard clients work without modification.

## Clean up

Delete the deployment when you're done:

```shell theme={null}
tg beta jig destroy
```

## Next steps

<CardGroup>
  <Card title="Image generation with queues" icon="photo" href="/docs/dedicated_containers_image">
    Serve the same model through the managed queue for async jobs.
  </Card>

  <Card title="Sprocket overview" icon="settings" href="/docs/deployments-sprocket">
    Understand queue mode, HTTP server mode, and the worker lifecycle.
  </Card>

  <Card title="Sprocket SDK reference" icon="code" href="/reference/dci-reference-sprocket">
    Full reference for `sprocket.run()`, including `predict_path`.
  </Card>

  <Card title="Jig CLI reference" icon="terminal-2" href="/reference/cli/jig">
    All deploy, secrets, and endpoint commands.
  </Card>
</CardGroup>
