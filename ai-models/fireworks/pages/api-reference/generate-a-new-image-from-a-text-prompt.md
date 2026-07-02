---
title: "Generate an image with FLUX.1 [schnell] FP8"
source: https://docs.fireworks.ai/api-reference/generate-a-new-image-from-a-text-prompt
path: api-reference/generate-a-new-image-from-a-text-prompt
---

POST https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image

[FLUX.1
\[schnell\]](https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina) is a
12 billion parameter rectified flow transformer capable of generating images
from text descriptions. The FP8 version uses reduced precision numerics for 2x
faster inference.

See our
[Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-1-schnell-fp8)
to quickly try it out in your browser.

## Headers

<ParamField type="string" placeholder="image/png">
  Specifies which format to return the response in. With `image/png` and
  `image/jpeg`, the server will populate the response body with a binary image
  of the specified format.
</ParamField>

<ParamField type="string" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField type="string">
  The Bearer with Fireworks API Key.
</ParamField>

## Request Body

<ParamField type="string" placeholder="A photo of a cat">
  Prompt to use for the image generation process.
</ParamField>

<ParamField type="string" placeholder="16:9">
  Aspect ratio of the generated image.

  **Options:** `1:1`, `21:9`, `16:9`, `3:2`, `5:4`, `4:5`, `2:3`, `9:16`, `9:21`, `4:3`, `3:4`
</ParamField>

<ParamField type="float" placeholder="3.5">
  Classifier-free guidance scale for the image diffusion process. Default value is 3.5.
</ParamField>

<ParamField type="integer" placeholder="4">
  Number of denoising steps for the image generation process. Default value is 4.
</ParamField>

<ParamField type="integer" placeholder="0">
  Random seed to use for the image generation process. If 0, we will use a totally random seed.
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image"
  headers = {
      "Content-Type": "application/json",
      "Accept": "image/jpeg",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean"
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
      with open("a.jpg", "wb") as f:
          f.write(response.content)
      print("Image saved as a.jpg")
  else:
      print("Error:", response.status_code, response.text)

  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "image/jpeg",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });

      // To process the response and get the image:
      const buffer = await response.arrayBuffer();

      fs.writeFile('a.jpg', Buffer.from(buffer), () => console.log('Finished downloading!'));
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image \
  -H 'Content-Type: application/json' \
  -H 'Accept: image/jpeg' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }' -o a.jpg
  ```
</RequestExample>

<ResponseExample>
  ```json Accept: application/json theme={null}
  {
    "id": "1234567890",
    "base64": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."],
    "finishReason": "SUCCESS",
    "seed": 1234567890
  }
  ```

  ```txt Accept: image/jpeg theme={null}
  /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k=
  ```

  ```txt Accept: image/png theme={null}
  iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==
  ```
</ResponseExample>

## Response

<Tabs>
  <Tab title="application/json">
    <ResponseField name="id" type="string">
      The unique identifier for the image generation request.
    </ResponseField>

    <ResponseField name="base64" type="string">
      Includes a base64-encoded string containing an image in PNG format.
      To retrieve the image, base64-decode the string into binary data,
      then load that binary data as a PNG file.
    </ResponseField>

    <ResponseField name="finishReason" type="string">
      Can be `SUCCESS` or `CONTENT_FILTERED`.

      Specifies the outcome of the image generation process. It could be
      `SUCCESS` indicating that the image was successfully generated, or
      `CONTENT_FILTERED` if the image was filtered due to the safety\_check=true
      parameter being set.
    </ResponseField>

    <ResponseField name="seed" type="integer">
      The seed used for the image generation process.
    </ResponseField>
  </Tab>

  <Tab title="image/jpeg">
    When the Accept type is `image/jpeg`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>

  <Tab title="image/png">
    When the Accept type is `image/png`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>
</Tabs>
