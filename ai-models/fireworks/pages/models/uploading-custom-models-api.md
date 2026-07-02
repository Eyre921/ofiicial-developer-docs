---
title: "Upload via REST API"
source: https://docs.fireworks.ai/models/uploading-custom-models-api
path: models/uploading-custom-models-api
---

Programmatically upload custom models using the Fireworks REST API

Use the Fireworks REST API to upload custom models programmatically — ideal for automation, CI/CD pipelines, and notebooks. If you just want the quickest path from a terminal, use [`firectl`](/models/uploading-custom-models#uploading-your-model) instead.

## The upload pipeline

Uploading a model via the REST API is a four-step pipeline:

1. **Create the model** – Register a model object that references the files you're about to upload.
2. **Get upload URLs** – Request a signed URL for each file.
3. **Upload the files** – Upload each file directly to its signed URL.
4. **Validate the upload** – Finalize the upload and move the model to `READY`.

<Warning>
  Step 4 is required. Until you call `validateUpload`, your model stays in the `UPLOADING` state and **cannot be deployed** — even after every file has finished uploading.
</Warning>

## Why validation is a separate step

Transfer and validation are decoupled because uploads can arrive several ways (signed-URL upload, S3 import, Azure import) and the transfer runs asynchronously on Fireworks infrastructure. The `validateUpload` call is what:

* Confirms every expected file has landed and is intact.
* Parses your model config to detect architecture, precision, and context length.
* Transitions the model from `UPLOADING` to `READY` so it can be deployed.

Because the transfer is asynchronous, `validateUpload` returns `FAILED_PRECONDITION` while files are still landing. Poll it until it returns `200` — at that point the model is `READY`.

## Full example

This script runs the entire pipeline end to end. Set your API key, account ID, model ID, and the local folder containing your Hugging Face model files.

```python theme={null}
import os
import time
import requests

# --- Configuration ---
API_KEY = os.environ["FIREWORKS_API_KEY"]
ACCOUNT_ID = "your-account-id"
MODEL_ID = "my-custom-model"
MODEL_PATH = "/path/to/model/files/"  # folder of Hugging Face files: config.json, *.safetensors, tokenizer, ...

BASE_URL = "https://api.fireworks.ai/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

files = [f for f in os.listdir(MODEL_PATH) if os.path.isfile(os.path.join(MODEL_PATH, f))]
file_sizes = {f: os.path.getsize(os.path.join(MODEL_PATH, f)) for f in files}

# --- Step 1: Create the model ---
requests.post(
    f"{BASE_URL}/accounts/{ACCOUNT_ID}/models",
    headers=HEADERS,
    json={
        "modelId": MODEL_ID,
        "model": {
            "kind": "HF_BASE_MODEL",
            "baseModelDetails": {
                "checkpointFormat": "HUGGINGFACE",
                "worldSize": 1,
                "huggingfaceFiles": files,
            },
        },
    },
).raise_for_status()
print(f"Created model {MODEL_ID}")

# --- Step 2: Get a signed upload URL for each file ---
resp = requests.post(
    f"{BASE_URL}/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:getUploadEndpoint",
    headers=HEADERS,
    json={"filenameToSize": file_sizes, "enableResumableUpload": False},
)
resp.raise_for_status()
upload_urls = resp.json()["filenameToSignedUrls"]

# --- Step 3: Upload each file to its signed URL ---
for filename, url in upload_urls.items():
    size = file_sizes[filename]
    with open(os.path.join(MODEL_PATH, filename), "rb") as f:
        requests.put(
            url,
            data=f,
            headers={
                "Content-Type": "application/octet-stream",
                "x-goog-content-length-range": f"{size},{size}",
            },
        ).raise_for_status()
    print(f"Uploaded {filename}")

# --- Step 4: Validate — poll until the model is READY ---
validate_url = f"{BASE_URL}/accounts/{ACCOUNT_ID}/models/{MODEL_ID}:validateUpload"
while True:
    resp = requests.get(validate_url, headers=HEADERS)
    if resp.status_code == 200:
        print("Model validated and ready to deploy!")
        break
    if "FAILED_PRECONDITION" in resp.text:  # files still landing
        print("Files still finalizing, retrying in 30s...")
        time.sleep(30)
        continue
    resp.raise_for_status()  # any other error is fatal
```

<Tip>
  Every step is safe to retry. `create` and `getUploadEndpoint` no-op if the model already exists (returning `ALREADY_EXISTS`), so an automated uploader that gets interrupted can simply re-run from the top and keep polling `validateUpload` until it succeeds.
</Tip>

## Troubleshooting: model stuck in `UPLOADING`

The most common cause is that `validateUpload` was never called — files transferring successfully does not move the model to `READY` on its own. Call the endpoint (and poll it):

```bash theme={null}
curl -X GET "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/models/<MODEL_ID>:validateUpload" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

If it returns `FAILED_PRECONDITION`, files are still landing — wait and retry. If it keeps failing after the transfer should be complete, confirm that every [required file](/models/uploading-custom-models#required-files) was included.

## Next steps

1. **Verify**: `firectl model get accounts/<ACCOUNT_ID>/models/<MODEL_ID>` — look for `State: READY`.
2. **Deploy**: see the [Custom Models guide](/models/uploading-custom-models#deploying-your-model) for deployment instructions.
