---
title: "Voice design"
source: https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews.md
path: docs/api-reference/legacy/voices/create-previews
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice design

POST https://api.elevenlabs.io/v1/text-to-voice/create-previews
Content-Type: application/json

Create a voice from a text prompt.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `output_format` (enum, optional) — The output format of the generated audio.
  - Allowed values: `mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_32000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`, `alaw_8000`, `opus_48000_32`, `opus_48000_64`, `opus_48000_96`, `opus_48000_128`, `opus_48000_192`

### Body (application/json)

- `voice_description` (string, required) — Description to use for the created voice.
- `text` (string, optional, nullable) — Text to generate, text length has to be between 100 and 1000.
- `auto_generate_text` (boolean, optional, default: false) — Whether to automatically generate a text suitable for the voice description.
- `loudness` (double, optional, default: 0.5) — Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.
- `quality` (double, optional, default: 0.9) — Higher quality results in better voice output but less variety.
- `seed` (integer, optional, nullable) — Random number that controls the voice generation. Same seed with same inputs produces same voice.
- `guidance_scale` (double, optional, default: 5) — Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.
- `should_enhance` (boolean, optional, default: false) — Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False

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
  "voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters."
}
```

**Response**

```json
{
  "previews": [
    {
      "audio_base_64": "UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=",
      "generated_voice_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
      "media_type": "audio/mp3",
      "duration_secs": 12.5,
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
    await client.textToVoice.createPreviews({
        voiceDescription: "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.text_to_voice.create_previews(
    voice_description="A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.",
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

	url := "https://api.elevenlabs.io/v1/text-to-voice/create-previews"

	payload := strings.NewReader("{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/text-to-voice/create-previews")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/text-to-voice/create-previews")
  .header("Content-Type", "application/json")
  .body("{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/text-to-voice/create-previews', [
  'body' => '{
  "voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/create-previews");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"voice_description\": \"A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["voice_description": "A sassy squeaky mouse with a playful and energetic tone, perfect for animated characters."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/create-previews")! as URL,
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
