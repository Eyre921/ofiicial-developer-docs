---
title: "Create Speech Generation"
source: https://elevenlabs.io/docs/api-reference/flows/text-to-speech/create.md
path: docs/api-reference/flows/text-to-speech/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Speech Generation

POST https://api.elevenlabs.io/v1/flows/text-to-speech
Content-Type: application/json

Start a speech generation with the selected model. Charged per character via text-to-speech billing. Use this over `/v1/text-to-speech` for the asynchronous generation lifecycle or for models not offered there; for direct, synchronous speech synthesis, prefer `/v1/text-to-speech`.

Reference: https://elevenlabs.io/docs/api-reference/flows/text-to-speech/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `object`
  - `model_id`: `eleven_flash_v2_5` (ElevenFlashV2_5Request)
    - `text` (string, required) — The text to synthesize into speech.
    - `voice` (string, required) — The ID of the voice to speak with.
    - `language_code` (string, optional, nullable) — ISO 639-1 language code to enforce on the output. Omit to detect the language from the text.
    - `output_format` (enum, optional, default: mp3_44100_128) — The audio encoding of the output, as `codec_sampleRateHz_bitrateKbps`. `mp3_44100_192` requires the Creator tier or above.
      - Allowed values: `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`
    - `pronunciation_dictionary_locators` (list of object, optional) — Pronunciation dictionaries to apply to the text, in order of precedence. Up to 3.
      - `pronunciation_dictionary_id` (string, required) — The ID of a pronunciation dictionary created via `POST /v1/pronunciation-dictionaries/add-from-file` or `POST /v1/pronunciation-dictionaries/add-from-rules`.
      - `version_id` (string, optional, nullable) — The version of the dictionary to use. Omit to use the latest version.
    - `voice_settings` (object, optional, nullable) — Overrides for the voice's saved settings, applied to this generation only.
      - `stability` (double, optional, nullable) — How consistent the voice stays across generations. Lower values give more expressive, varied speech.
      - `similarity_boost` (double, optional, nullable) — How closely the output adheres to the original voice.
      - `speed` (double, optional, nullable) — The speed of the generated speech, where 1.0 is the voice's natural pace.
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `eleven_multilingual_v2` (ElevenMultilingualV2Request)
    - `text` (string, required) — The text to synthesize into speech.
    - `voice` (string, required) — The ID of the voice to speak with.
    - `output_format` (enum, optional, default: mp3_44100_128) — The audio encoding of the output, as `codec_sampleRateHz_bitrateKbps`. `mp3_44100_192` requires the Creator tier or above.
      - Allowed values: `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`
    - `pronunciation_dictionary_locators` (list of object, optional) — Pronunciation dictionaries to apply to the text, in order of precedence. Up to 3.
      - `pronunciation_dictionary_id` (string, required) — The ID of a pronunciation dictionary created via `POST /v1/pronunciation-dictionaries/add-from-file` or `POST /v1/pronunciation-dictionaries/add-from-rules`.
      - `version_id` (string, optional, nullable) — The version of the dictionary to use. Omit to use the latest version.
    - `voice_settings` (object, optional, nullable) — Overrides for the voice's saved settings, applied to this generation only.
      - `stability` (double, optional, nullable) — How consistent the voice stays across generations. Lower values give more expressive, varied speech.
      - `similarity_boost` (double, optional, nullable) — How closely the output adheres to the original voice.
      - `style` (double, optional, nullable) — How strongly the speaking style is exaggerated.
      - `use_speaker_boost` (boolean, optional, nullable) — Whether to boost similarity to the original speaker, at some latency cost.
      - `speed` (double, optional, nullable) — The speed of the generated speech, where 1.0 is the voice's natural pace.
    - `webhook` (object, optional, nullable) — Include to send the generation's result to the workspace's configured flows webhooks once it completes or fails. The webhook payload matches the terminal response of the corresponding GET endpoint.
      - `type`: `all` (WebhookTargetAll)
      - `type`: `ids` (WebhookTargetIds)
        - `ids` (list of string, required) — The IDs of the workspace flows webhooks to deliver the result to. Each must be one of the workspace's configured flows webhooks.
  - `model_id`: `eleven_v3` (ElevenV3Request)
    - `text` (string, required) — The text to synthesize into speech.
    - `voice` (string, required) — The ID of the voice to speak with.
    - `language_code` (string, optional, nullable) — ISO 639-1 language code to enforce on the output. Omit to detect the language from the text.
    - `output_format` (enum, optional, default: mp3_44100_128) — The audio encoding of the output, as `codec_sampleRateHz_bitrateKbps`. `mp3_44100_192` requires the Creator tier or above.
      - Allowed values: `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`
    - `pronunciation_dictionary_locators` (list of object, optional) — Pronunciation dictionaries to apply to the text, in order of precedence. Up to 3.
      - `pronunciation_dictionary_id` (string, required) — The ID of a pronunciation dictionary created via `POST /v1/pronunciation-dictionaries/add-from-file` or `POST /v1/pronunciation-dictionaries/add-from-rules`.
      - `version_id` (string, optional, nullable) — The version of the dictionary to use. Omit to use the latest version.
    - `voice_settings` (object, optional, nullable) — Overrides for the voice's saved settings, applied to this generation only.
      - `stability` (double, optional, nullable) — How consistent the voice stays across generations. Lower values give more expressive, varied speech.
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
  "text": "The first move is what sets everything in motion.",
  "voice": "JBFqnCBsd6RMkjVDRZzb"
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
    await client.flows.textToSpeech.create();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.flows.text_to_speech.create()

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

	url := "https://api.elevenlabs.io/v1/flows/text-to-speech"

	payload := strings.NewReader("{\n  \"model_id\": \"string\",\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"voice\": \"JBFqnCBsd6RMkjVDRZzb\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/flows/text-to-speech")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model_id\": \"string\",\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"voice\": \"JBFqnCBsd6RMkjVDRZzb\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/flows/text-to-speech")
  .header("Content-Type", "application/json")
  .body("{\n  \"model_id\": \"string\",\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"voice\": \"JBFqnCBsd6RMkjVDRZzb\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/flows/text-to-speech', [
  'body' => '{
  "model_id": "string",
  "text": "The first move is what sets everything in motion.",
  "voice": "JBFqnCBsd6RMkjVDRZzb"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/flows/text-to-speech");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model_id\": \"string\",\n  \"text\": \"The first move is what sets everything in motion.\",\n  \"voice\": \"JBFqnCBsd6RMkjVDRZzb\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "model_id": "string",
  "text": "The first move is what sets everything in motion.",
  "voice": "JBFqnCBsd6RMkjVDRZzb"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/flows/text-to-speech")! as URL,
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
