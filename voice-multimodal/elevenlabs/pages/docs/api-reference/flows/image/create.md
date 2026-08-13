---
title: "Create Image Generation"
source: https://elevenlabs.io/docs/api-reference/flows/image/create.md
path: docs/api-reference/flows/image/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Image Generation

POST https://api.elevenlabs.io/v1/flows/image
Content-Type: application/json

Start an image generation with the selected model.

Reference: https://elevenlabs.io/docs/api-reference/flows/image/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `object`
  - `model_id`: `bytedance-seedream-5-lite` (BytedanceSeedream5LiteRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `3:4`, `16:9`, `4:3`, `9:16`
    - `images` (list of object, optional) — Up to 10 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 2K) — The resolution of the output image.
      - Allowed values: `2K`, `3K`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `bytedance-seedream-5-pro` (BytedanceSeedream5ProRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `3:4`, `16:9`, `4:3`, `9:16`
    - `images` (list of object, optional) — Up to 10 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 2K) — The resolution of the output image.
      - Allowed values: `1K`, `2K`
    - `seed` (integer, optional, nullable) — A seed for reproducible generation: the same seed and inputs give similar output across generations. Omit for random.
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gemini-2.5-flash-image` (Gemini25FlashImageRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
    - `images` (list of object, optional) — Up to 5 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gemini-3-pro-image` (Gemini3ProImageRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
    - `images` (list of object, optional) — Up to 10 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 1K) — The resolution of the output image.
      - Allowed values: `1K`, `2K`, `4K`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gemini-3.1-flash-image` (Gemini31FlashImageRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1`
    - `images` (list of object, optional) — Up to 14 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` (enum, optional, default: 1K) — The resolution of the output image.
      - Allowed values: `512`, `1K`, `2K`, `4K`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gemini-3.1-flash-lite-image` (Gemini31FlashLiteImageRequest)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
    - `images` (list of object, optional) — Up to 14 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `resolution` ("1K", optional, default: 1K) — The resolution of the output image.
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gpt-image-1` (GPTImage1Request)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 1:1) — The aspect ratio of the output image.
      - Allowed values: `1:1`, `3:2`, `2:3`
    - `background` (enum, optional, default: auto) — The background of the output image. With `auto`, the model picks the background that suits the image.
      - Allowed values: `transparent`, `opaque`, `auto`
    - `images` (list of object, optional) — Up to 5 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `mask` (object, optional, nullable) — An image whose fully transparent areas mark where the first reference image may be edited; requires `images`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `quality` (enum, optional, default: medium) — The quality of the output image.
      - Allowed values: `low`, `medium`, `high`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gpt-image-1.5` (GPTImage1_5Request)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 1:1) — The aspect ratio of the output image.
      - Allowed values: `1:1`, `3:2`, `2:3`
    - `background` (enum, optional, default: auto) — The background of the output image. With `auto`, the model picks the background that suits the image.
      - Allowed values: `transparent`, `opaque`, `auto`
    - `images` (list of object, optional) — Up to 5 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `mask` (object, optional, nullable) — An image whose fully transparent areas mark where the first reference image may be edited; requires `images`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `quality` (enum, optional, default: medium) — The quality of the output image.
      - Allowed values: `low`, `medium`, `high`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `gpt-image-2` (GPTImage2Request)
    - `prompt` (string, required) — A text description of the image to generate.
    - `aspect_ratio` (enum, optional, default: 16:9) — The aspect ratio of the output image. With `auto`, the model picks an aspect ratio based on the inputs.
      - Allowed values: `auto`, `1:1`, `4:5`, `5:4`, `3:4`, `4:3`, `2:3`, `3:2`, `1:2`, `2:1`, `9:16`, `16:9`, `21:9`, `1:3`, `3:1`
    - `images` (list of object, optional) — Up to 10 reference images to edit or draw from.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `mask` (object, optional, nullable) — An image whose fully transparent areas mark where the first reference image may be edited; requires `images`.
      - `type`: `asset` (StaticAssetReference)
        - `asset_id` (string, required) — The ID of an asset uploaded via the assets API (`POST /v1/assets`), as returned in that response's `asset_id`.
      - `type`: `generation` (GenerationReference)
        - `generation_id` (string, required) — The ID of the generation whose output to use, as returned when the generation was created.
      - `type`: `inline_base64` (InlineImageReference)
        - `content_base64` (string, required) — The media file's bytes, base64-encoded (standard alphabet). Up to 25MB decoded.
        - `mime_type` (enum, required) — The MIME type of the encoded image.
          - Allowed values: `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/heif`
    - `quality` (enum, optional, default: medium) — The quality of the output image.
      - Allowed values: `low`, `medium`, `high`
    - `resolution` (enum, optional, default: 1K) — The resolution of the output image.
      - Allowed values: `1K`, `2K`, `4K`
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.

## Response

### 200

Successful Response

- `id` (string, required) — The unique identifier of the generation. Pass it to the corresponding GET endpoint to retrieve the output.
- `status` ("pending", required) — A newly created generation is always `pending`.

## Examples

**Request**

```json
{
  "model_id": "string",
  "prompt": "A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic"
}
```

**Response**

```json
{
  "id": "JWr5N6X9ZTqf8jD2LmQb",
  "status": "pending"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.flows.image.create();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.image.create()

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/flows/image"

	payload := strings.NewReader("{\n  \"model_id\": \"string\",\n  \"prompt\": \"A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/flows/image")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model_id\": \"string\",\n  \"prompt\": \"A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/flows/image")
  .header("Content-Type", "application/json")
  .body("{\n  \"model_id\": \"string\",\n  \"prompt\": \"A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/flows/image', [
  'body' => '{
  "model_id": "string",
  "prompt": "A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/image");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model_id\": \"string\",\n  \"prompt\": \"A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "model_id": "string",
  "prompt": "A corgi in a tiny lifeguard chair on a sunlit beach at golden hour, photorealistic"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/image")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
