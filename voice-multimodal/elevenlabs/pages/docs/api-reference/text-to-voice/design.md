---
title: "Design a voice"
source: https://elevenlabs.io/docs/api-reference/text-to-voice/design.md
path: docs/api-reference/text-to-voice/design
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Design a voice

POST https://api.elevenlabs.io/v1/text-to-voice/design
Content-Type: application/json

Design a voice via a prompt. This method returns a list of voice previews. Each preview has a generated_voice_id and a sample of the voice as base64 encoded mp3 audio. To create a voice use the generated_voice_id of the preferred preview with the /v1/text-to-voice endpoint.

Reference: https://elevenlabs.io/docs/api-reference/text-to-voice/design

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

### Body (application/json)

- `voice_description` (string, required) — Description to use for the created voice.
- `model_id` (enum, optional, default: eleven_multilingual_ttv_v2) — Model to use for the voice generation. Possible values: eleven_multilingual_ttv_v2, eleven_ttv_v3.
  - Allowed values: `eleven_multilingual_ttv_v2`, `eleven_ttv_v3`
- `text` (string, optional, nullable) — Text to generate, text length has to be between 100 and 1000.
- `auto_generate_text` (boolean, optional, default: false) — Whether to automatically generate a text suitable for the voice description.
- `loudness` (double, optional, default: 0.5) — Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.
- `seed` (integer, optional, nullable) — Random number that controls the voice generation. Same seed with same inputs produces same voice.
- `guidance_scale` (double, optional, default: 5) — Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.
- `stream_previews` (boolean, optional, default: false) — Determines whether the Text to Voice previews should be included in the response. If true, only the generated IDs will be returned which can then be streamed via the /v1/text-to-voice/:generated_voice_id/stream endpoint.
- `should_enhance` (boolean, optional, default: false) — Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False
- `remixing_session_id` (string, optional, nullable) — The remixing session id.
- `remixing_session_iteration_id` (string, optional, nullable) — The id of the remixing session iteration where these generations should be attached to. If not provided, a new iteration will be created.
- `quality` (double, optional, nullable) — Higher quality results in better voice output but less variety.
- `reference_audio_base64` (string, optional, nullable) — Reference audio to use for the voice generation. The audio should be base64 encoded. Only supported when using the eleven_ttv_v3 model.
- `prompt_strength` (double, optional, nullable) — Controls the balance of prompt versus reference audio when generating voice samples. 0 means almost no prompt influence, 1 means almost no reference audio influence. Only supported when using the eleven_ttv_v3 model.

## Response

### 200

Successful Response

- `previews` (list of object, required) — The previews of the generated voices.
  - `audio_base_64` (string, required) — The base64 encoded audio of the preview.
  - `generated_voice_id` (string, required) — The ID of the generated voice. Use it to create a voice from the preview.
  - `media_type` (string, required) — The media type of the preview.
  - `duration_secs` (double, required) — The duration of the preview in seconds.
  - `language` (string, required, nullable) — The language of the preview.
- `text` (string, required) — The text used to preview the voices.

## Examples

**Request**

```json
{
  "voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling."
}
```

**Response**

```json
{
  "previews": [
    {
      "audio_base_64": "UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=",
      "generated_voice_id": "vcd_9f8a7b6c3d2e4f1a8b9c0d2e3f4a5b6c",
      "media_type": "audio/mpeg",
      "duration_secs": 5.2,
      "language": "en-US"
    }
  ],
  "text": "Every act of kindness, no matter how small, carries value and can make a difference, as no gesture of goodwill is ever wasted."
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.textToVoice.design({
        voiceDescription: "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.text_to_voice.design(
    voice_description="A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.",
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/design"

	payload := strings.NewReader("{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/design")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/design")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/design', [
  'body' => '{
  "voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/design");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters and lively storytelling."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/design")! as URL,
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
