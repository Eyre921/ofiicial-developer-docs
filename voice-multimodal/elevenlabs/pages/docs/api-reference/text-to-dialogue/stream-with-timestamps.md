---
title: "Stream dialogue with timestamps"
source: https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps.md
path: docs/api-reference/text-to-dialogue/stream-with-timestamps
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stream dialogue with timestamps

POST https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps
Content-Type: application/json

Converts a list of text and voice ID pairs into speech (dialogue) and returns a stream of JSON blobs containing audio as a base64 encoded string and timestamps

Reference: https://elevenlabs.io/docs/api-reference/text-to-dialogue/stream-with-timestamps

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `output_format` (enum, optional) — Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.
  - Allowed values: `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_32000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`, `alaw_8000`, `opus_48000_32`, `opus_48000_64`, `opus_48000_96`, `opus_48000_128`, `opus_48000_192`
- `enable_logging` (boolean, optional, default: true) — When enable_logging is set to false zero retention mode will be used for the request. This will mean history features are unavailable for this request, including request stitching. Zero retention mode may only be used by enterprise customers.

### Body (application/json)

- `inputs` (list of object, required) — A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10. For reliable generation, keep the total character count across all `inputs[].text` values at or below 2,000 characters per request. Longer requests can terminate early in streaming responses or return a validation error.
  - `text` (string, required) — The text to be converted into speech.
  - `voice_id` (string, required) — The ID of the voice to be used for the generation.
- `model_id` (string, optional, default: eleven_v3) — Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.
- `language_code` (string, optional, nullable) — Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support the provided language code, it will be ignored. This parameter is not supported for multilingual_v2 models.
- `settings` (object, optional, nullable) — Settings controlling the dialogue generation.
  - `stability` (double, optional, nullable, default: 0.5) — Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
- `pronunciation_dictionary_locators` (list of object, optional, nullable) — A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request
  - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary.
  - `version_id` (string, optional, nullable) — The ID of the version of the pronunciation dictionary. If not provided, the latest version will be used.
- `seed` (integer, optional, nullable) — If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.
- `apply_text_normalization` (enum, optional, default: auto) — This parameter controls text normalization with three modes: 'auto', 'on', and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped.
  - Allowed values: `auto`, `on`, `off`

## Response

### 200

Stream of transcription chunks

- Streaming response of `object`.

## Examples

**Request**

```json
{
  "inputs": [
    {
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    },
    {
      "text": "I'm doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    }
  ]
}
```

**Response**

```json
[
  {
    "alignment": {
      "character_end_times_seconds": [
        0.1,
        0.2
      ],
      "character_start_times_seconds": [
        0,
        0.1
      ],
      "characters": [
        "H",
        "e"
      ]
    },
    "audio_base64": "base64_encoded_audio_chunk",
    "normalized_alignment": {
      "character_end_times_seconds": [
        0.1,
        0.2
      ],
      "character_start_times_seconds": [
        0,
        0.1
      ],
      "characters": [
        "H",
        "e"
      ]
    },
    "voice_segments": [
      {
        "character_end_index": 2,
        "character_start_index": 0,
        "dialogue_input_index": 0,
        "end_time_seconds": 0.2,
        "start_time_seconds": 0,
        "voice_id": "VEDscrYI8uIMttlO2Ztu"
      }
    ]
  }
]
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.textToDialogue.streamWithTimestamps({
        inputs: [
            {
                text: "Hello, how are you?",
                voiceId: "bYTqZQo3Jz7LQtmGTgwi",
            },
            {
                text: "I'm doing well, thank you!",
                voiceId: "6lCwbsX1yVjD49QmpkTR",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DialogueInput

client = ElevenLabs()

client.text_to_dialogue.stream_with_timestamps(
    inputs=[
        DialogueInput(
            text="Hello, how are you?",
            voice_id="bYTqZQo3Jz7LQtmGTgwi",
        ),
        DialogueInput(
            text="I\'m doing well, thank you!",
            voice_id="6lCwbsX1yVjD49QmpkTR",
        )
    ],
)

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

	url := "https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps"

	payload := strings.NewReader("{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")
  .header("Content-Type", "application/json")
  .body("{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps', [
  'body' => '{
  "inputs": [
    {
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    },
    {
      "text": "I\'m doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    {\n      \"text\": \"Hello, how are you?\",\n      \"voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    },\n    {\n      \"text\": \"I'm doing well, thank you!\",\n      \"voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["inputs": [
    [
      "text": "Hello, how are you?",
      "voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    ],
    [
      "text": "I'm doing well, thank you!",
      "voice_id": "6lCwbsX1yVjD49QmpkTR"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-dialogue/stream/with-timestamps")! as URL,
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
