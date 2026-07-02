---
title: "Generate or edit an image with FLUX.1 Kontext"
source: https://docs.fireworks.ai/api-reference/generate-or-edit-image-using-flux-kontext
path: api-reference/generate-or-edit-image-using-flux-kontext
---

POST https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}

💡 Note that this API is async and will return the **request\_id** instead of the image. Call the [get\_result](/api-reference/get-generated-image-from-flux-kontex) API to obtain the generated image.

<Tabs>
  <Tab title="FLUX.1 Kontext Pro">
    FLUX Kontext Pro is a specialized model for generating contextually-aware images from text descriptions. Designed for professional use cases requiring high-quality, consistent image generation.

    Use our [Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-pro) to quickly try it out in your browser.
  </Tab>

  <Tab title="FLUX.1 Kontext Max">
    FLUX Kontext Max is the most advanced model in the Kontext series, offering maximum quality and context understanding. Ideal for enterprise applications requiring the highest level of image generation performance.

    Use our [Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-max) to quickly try it out in your browser.
  </Tab>
</Tabs>

## Path

<ParamField type="string" placeholder="flux-kontext-pro">
  The model to use for image generation. Use **flux-kontext-pro** or  **flux-kontext-max** as the model name in the API.
</ParamField>

## Headers

<ParamField type="string" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField type="string">
  Your Fireworks API key.
</ParamField>

## Request Body

<ParamField type="string" placeholder="A photo of a cat">
  Prompt to use for the image generation process.
</ParamField>

<ParamField type="string | null">
  Base64 encoded image or URL to use with Kontext.
</ParamField>

<ParamField type="integer | null" placeholder="42">
  Optional seed for reproducibility.
</ParamField>

<ParamField type="string | null">
  Aspect ratio of the image between 21:9 and 9:21.
</ParamField>

<ParamField type="string" placeholder="png">
  Output format for the generated image. Can be 'jpeg' or 'png'.

  **Options:** `jpeg`, `png`
</ParamField>

<ParamField type="string | null">
  URL to receive webhook notifications.

  **Length:** 1-2083 characters
</ParamField>

<ParamField type="string | null">
  Optional secret for webhook signature verification.
</ParamField>

<ParamField type="boolean" placeholder="false">
  Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation.
</ParamField>

<ParamField type="integer" placeholder="2">
  Tolerance level for input and output moderation. Between 0 and 6, 0 being most strict, 6 being least strict. Limit of 2 for Image to Image.

  **Range:** 0-6
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean",
      "input_image": "<string>",
      "seed": 42,
      "aspect_ratio": "<string>",
      "output_format": "jpeg",
      "webhook_url": "<string>",
      "webhook_secret": "<string>",
      "prompt_upsampling": False,
      "safety_tolerance": 2
  }

  response = requests.post(url, headers=headers, json=data)
  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model} \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }'
  ```
</RequestExample>

## Response

<Tabs>
  <Tab title="200">
    Successful Response

    <ParamField type="string">
      request id
    </ParamField>
  </Tab>

  <Tab title="400">
    Unsuccessful Response

    <ParamField type="string">
      error message
    </ParamField>
  </Tab>
</Tabs>
