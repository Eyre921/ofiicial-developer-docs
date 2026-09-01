---
title: "Quantization"
source: https://docs.fireworks.ai/models/quantization
path: models/quantization
---

Reduce model precision to improve performance and lower costs

Quantization reduces the number of bits used to serve a model, improving performance and reducing cost by 30-50%. However, this can change model numerics which may introduce small changes to the output.

<Tip>
  Read our [blog post](https://fireworks.ai/blog/fireworks-quantization) for a detailed treatment of how quantization affects model quality.
</Tip>

## Checking available precisions

Models may support different numerical precisions like FP16, FP8, BF16, or INT8, which affect memory usage and inference speed.

**Check default precision:**

```bash theme={null}
firectl model get accounts/fireworks/models/llama-v3p1-8b-instruct | grep "Default Precision"
```

**Check supported precisions:**

```bash theme={null}
firectl model get accounts/fireworks/models/llama-v3p1-8b-instruct | grep -E "(Supported Precisions|Supported Precisions With Calibration)"
```

The `Precisions` field indicates what precisions the model has been prepared for.

## Quantizing a model

A model can be quantized to 8-bit floating-point (FP8) precision.

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl prepare-model <MODEL_ID>
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to prepare

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:prepare",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "precision": "FP8"
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

<Note>This is an additive process that enables creating deployments with additional precisions. The original FP16 checkpoint is still available for use.</Note>

You can check on the status of preparation by running:

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl model get <MODEL_ID>
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    MODEL_ID = "<YOUR_MODEL_ID>" # The ID of the model you want to get

    response = requests.get(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/models/{MODEL_ID}",
      headers={
        "Authorization": f"Bearer {API_KEY}"
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

and checking if the state is still in `PREPARING`. A successfully prepared model will have the desired precision added
to the `Precisions` list.

## Creating an FP8 deployment

By default, creating a deployment uses the FP16 checkpoint. To use a quantized FP8 checkpoint, first ensure the model has been prepared for FP8 (see [Checking available precisions](#checking-available-precisions) above), then pass the `--precision` flag when creating your deployment:

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl deployment create <MODEL> --accelerator-type NVIDIA_H100_80GB --precision FP8
    ```
  </Tab>

  <Tab title="Python (REST API)">
    ```python theme={null}
    import os
    import requests

    ACCOUNT_ID = os.environ.get("FIREWORKS_ACCOUNT_ID")
    API_KEY = os.environ.get("FIREWORKS_API_KEY")
    # The ID of the model you want to deploy.
    # The model must be prepared for FP8 precision.
    MODEL_ID = "<YOUR_MODEL_ID>"
    DEPLOYMENT_NAME = "My FP8 Deployment"

    response = requests.post(
      f"https://api.fireworks.ai/v1/accounts/{ACCOUNT_ID}/deployments",
      headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
      },
      json={
        "displayName": DEPLOYMENT_NAME,
        "baseModel": MODEL_ID,
        "acceleratorType": "NVIDIA_H100_80GB",
        "precision": "FP8",
      }
    )

    print(response.json())
    ```
  </Tab>
</Tabs>

<Note>Quantized deployments can only be served using H100 GPUs.</Note>
