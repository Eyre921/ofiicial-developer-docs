---
title: "Templates quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/templates.md
path: docs/eleven-api/guides/cookbooks/templates
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Templates quickstart

In this tutorial you run a public template from a Python or TypeScript script. The template turns a casual phone photo of a piece of clothing into a clean product shot, and the script saves the result next to it. The tutorial takes about five minutes, of which the run itself is under a minute.

![Phone photo and packshot](/docs/_fern-img/6afed41d4d791df68c87f183bd8db1d4aca8b4be3e946cc518534bda902f9528.webp)

A **template** is a published [ElevenCreative Flow](/docs/eleven-creative/products/flows): a chain of models that takes a fixed set of **inputs** and produces a fixed set of **outputs**. The one you will run, [Phone Photo to Packshot](https://elevenlabs.io/app/templates/Yz4DETxRv4uXyIo5PnEy), takes one image and returns one image. Its author already chose the models and prompts, so your code only passes the photo.

> **Warning**
>
> Running a template requires a Pro plan or above.

## Set up

#### Create an API key

[Create an API key in the dashboard here](https://elevenlabs.io/app/api/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as an environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

**`.env`**

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

Give the key the **Image & Video** permission.

#### Install the SDK

#### SDK

We'll also use the `dotenv` library to load our API key from an environment variable.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

#### CLI

Install the ElevenLabs CLI. Homebrew (macOS) and Scoop (Windows) are recommended.

**`Homebrew (macOS)`**

```bash title="Homebrew (macOS)"
brew install elevenlabs/tap/elevenlabs
```

**`Scoop (Windows)`**

```powershell title="Scoop (Windows)"
scoop bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop install elevenlabs
```

**`npm`**

```bash title="npm"
npm install -g @elevenlabs/cli
```

**`curl`**

```bash title="curl"
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh | sh
```

> **Tip**
>
> Working with an AI coding assistant? Run `elevenlabs generate-skills` in your project to write a
> `SKILL.md` for every command group into `skills/`, so your assistant knows the CLI's full surface
> without you pasting docs. Use `--output-dir` to put them elsewhere. This reads the CLI's own
> embedded API definition, so it needs no API key and works offline — and it stays in step with
> whichever CLI version you have installed.

Then authenticate — this opens your browser to authorize the CLI:

```bash
elevenlabs auth login
```

#### Get a photo

Download the sample photo into the folder where you will create your script:

```bash
curl -o garment.jpg https://storage.googleapis.com/eleven-public-cdn/documentation_assets/templates/garment.jpg
```

## Find the template's code

Open [Phone Photo to Packshot](https://elevenlabs.io/app/templates/Yz4DETxRv4uXyIo5PnEy) in the ElevenLabs app and select the **API** tab. Every template has one, with the code that runs it in cURL, Python and TypeScript.

![Template API tab](/docs/_fern-img/801c9d2e2736964b35f5bad954092c973b21eedc03801128f1ed8bf31ea095b1.webp)

The tab walks through three steps: get an API key, choose how to get the result, and run the template. Under **Choose how to get the result**, **Wait for the result** is selected by default. The code in the third step opens on cURL; select **Python** or **TypeScript**, and the step becomes **Run and wait for the result**. Its snippet starts a run, waits for it to finish and prints each output. It passes one value under `inputs` for each of the template's inputs, keyed by the input's id, and reads each result from `outputs` by the output's id. This template has one input, `garment_photo`, and one output, `packshot`. These two ids are the only names your code needs.

## Run the template

Create `packshot.py` or `packshot.mts`. It is the API tab's snippet with these changes:

* The API key is loaded from your `.env` file.
* The photo is passed as base64 in place of `YOUR_ASSET_ID`, the ID of a file already uploaded to ElevenLabs.
* The script prints a line while the run is in progress, and saves the packshot to `packshot.jpg` instead of printing its URL.

**`packshot.py`**

```python title="packshot.py" maxLines=0
import base64
import os
import urllib.request

from dotenv import load_dotenv
from elevenlabs import ElevenLabs, TemplateInputReference_InlineBase64

load_dotenv()

client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])

with open("garment.jpg", "rb") as f:
    photo = base64.b64encode(f.read()).decode()

print("Running the template, this takes up to a minute...")

# Starts a run and waits for it to finish, checking back as often as the API
# asks. In production, receive the result by webhook instead.
run = client.flows.templates.runs.create_and_wait(
    template_id="Yz4DETxRv4uXyIo5PnEy",
    # Pins the version this tutorial was written against.
    version_id="Kqs4nRrpndEjQ54BhbwE",
    inputs={
        "garment_photo": TemplateInputReference_InlineBase64(
            content_base_64=photo,
            mime_type="image/jpeg",
        ),
    },
)

packshot = run.outputs["packshot"]
# Checking `type` tells your editor this output is an image, which has a content_url.
if packshot.type == "image" and packshot.status == "completed" and packshot.content_url:
    urllib.request.urlretrieve(packshot.content_url, "packshot.jpg")
    print("Saved packshot.jpg")
else:
    print("The run failed:", packshot.failure_reason)

```

**`packshot.mts`**

```typescript title="packshot.mts" maxLines=0
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import { readFile, writeFile } from "fs/promises";

const client = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

const photo = await readFile("garment.jpg");

console.log("Running the template, this takes up to a minute...");

// Starts a run and waits for it to finish, checking back as often as the API
// asks. In production, receive the result by webhook instead.
const run = await client.flows.templates.runs.createAndWait("Yz4DETxRv4uXyIo5PnEy", {
  // Pins the version this tutorial was written against.
  versionId: "Kqs4nRrpndEjQ54BhbwE",
  inputs: {
    garment_photo: {
      type: "inline_base64",
      contentBase64: photo.toString("base64"),
      mimeType: "image/jpeg",
    },
  },
});

const packshot = run.outputs["packshot"];
// Checking `type` tells TypeScript this output is an image, which has a contentUrl.
if (packshot.type === "image" && packshot.status === "completed" && packshot.contentUrl) {
  const response = await fetch(packshot.contentUrl);
  await writeFile("packshot.jpg", Buffer.from(await response.arrayBuffer()));
  console.log("Saved packshot.jpg");
} else {
  console.error("The run failed:", packshot.failureReason);
}

```

`create_and_wait` (`createAndWait` in TypeScript) starts the run, then checks on it at the interval the API suggests until every output has finished. A run that fails is returned, not raised, so the script checks the output's `status` before reading it. `version_id` pins the version of the template this tutorial was written against, so a later edit to the template can't break the script.

Run the script. A run of this template uses about 1,020 credits, the same as running it in the app.

```python
python packshot.py
```

```typescript
npx tsx packshot.mts
```

After 30 seconds to a minute, the script prints:

```text
Running the template, this takes up to a minute...
Saved packshot.jpg
```

Open `packshot.jpg`. The garment from the photo is now on a mannequin against a plain studio background, with the bed and the lighting gone.

> **Note**
>
> `create_and_wait` is for scripts and trying templates out. In production, receive finished runs
> with a [webhook](/docs/eleven-api/guides/how-to/image-and-video/webhooks) instead, so your
> application does not hold a request open while a run is in progress. [Run your team's template](/docs/eleven-api/guides/how-to/templates/run-a-template) shows how.

## Run it with your own photo

Take a photo of any piece of clothing with your phone. It does not need to be a good photo: a t-shirt on your bed or a jacket over a chair works. Save it as a JPEG over `garment.jpg` and run the script again.

You get a packshot of your garment with the same studio look, because every run of a template goes through the same models and settings. The details can still vary from run to run, even with the same photo.

## What you learned

* A template takes named **inputs** and produces named **outputs**, and its **API** tab shows the code that runs it.
* `flows.templates.runs.create_and_wait` starts a **run** with one value per input id and returns once it finishes. You read each output by its id and check its `status`.
* In production, a **webhook** delivers each finished run, so nothing waits on it.

## Next steps

#### [Run your team's template](/docs/eleven-api/guides/how-to/templates/run-a-template)

Copy a template's code from its API tab, fill in each kind of input, receive the result by
webhook and pin a version.

#### [Webhooks](/docs/eleven-api/guides/how-to/image-and-video/webhooks)

Set up a production webhook, verify signatures by hand, and handle retries and duplicate events.

#### [Create a template](/docs/eleven-creative/products/flows#creating-a-template)

How your team turns a Flow into a template: choosing its inputs and outputs, and sharing it.

#### [API reference](/docs/api-reference/flows/templates/runs/create)

Every parameter of a template run.
