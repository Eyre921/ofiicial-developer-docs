---
title: "Create sound effect"
source: https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert.md
path: docs/api-reference/text-to-sound-effects/convert
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create sound effect

POST https://api.elevenlabs.io/v1/sound-generation
Content-Type: application/json

Turn text into sound effects for your videos, voice-overs or video games using the most advanced sound effects models in the world.

Reference: https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert

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

- `text` (string, required) — The text that will get converted into a sound effect.
- `loop` (boolean, optional, default: false) — Whether to create a sound effect that loops smoothly. Only available for the 'eleven_text_to_sound_v2 model'.
- `duration_seconds` (double, optional, nullable) — The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. If set to None we will guess the optimal duration using the prompt. Defaults to None.
- `prompt_influence` (double, optional, nullable, default: 0.3) — A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3.
- `model_id` (enum, optional, default: eleven_text_to_sound_v2) — The model ID to use for the sound generation.
  - Allowed values: `eleven_text_to_sound_v2`

## Response

### 200

The generated sound effect as an MP3 file

- File download.

## Examples

**Request**

```json
{
  "text": "Spacious braam suitable for high-impact movie trailer moments"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "xi-api-key",
    });
    await client.textToSoundEffects.convert({
        text: "Spacious braam suitable for high-impact movie trailer moments",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="xi-api-key",
)

client.text_to_sound_effects.convert(
    text="Spacious braam suitable for high-impact movie trailer moments",
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

	url := "https://api.elevenlabs.io/v1/sound-generation"

	payload := strings.NewReader("{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("xi-api-key", "xi-api-key")
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

url = URI("https://api.elevenlabs.io/v1/sound-generation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["xi-api-key"] = 'xi-api-key'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/sound-generation")
  .header("xi-api-key", "xi-api-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/sound-generation', [
  'body' => '{
  "text": "Spacious braam suitable for high-impact movie trailer moments"
}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/sound-generation");
var request = new RestRequest(Method.POST);
request.AddHeader("xi-api-key", "xi-api-key");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Spacious braam suitable for high-impact movie trailer moments\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "xi-api-key",
  "Content-Type": "application/json"
]
let parameters = ["text": "Spacious braam suitable for high-impact movie trailer moments"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/sound-generation")! as URL,
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
