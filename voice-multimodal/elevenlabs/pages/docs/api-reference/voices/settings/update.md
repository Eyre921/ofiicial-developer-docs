---
title: "Edit voice settings"
source: https://elevenlabs.io/docs/api-reference/voices/settings/update.md
path: docs/api-reference/voices/settings/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Edit voice settings

POST https://api.elevenlabs.io/v1/voices/{voice_id}/settings/edit
Content-Type: application/json

Edit your settings for a specific voice. "similarity_boost" corresponds to "Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

Reference: https://elevenlabs.io/docs/api-reference/voices/settings/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

### Body (application/json)

- `stability` (double, optional, nullable, default: 0.5) — Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
- `use_speaker_boost` (boolean, optional, nullable, default: true) — This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.
- `similarity_boost` (double, optional, nullable, default: 0.75) — Determines how closely the AI should adhere to the original voice when attempting to replicate it.
- `style` (double, optional, nullable, default: 0) — Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.
- `speed` (double, optional, nullable, default: 1) — Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up.

## Response

### 200

Successful Response

- `status` (string, required) — The status of the voice settings edit request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

## Examples

**Request**

```json
{
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
}
```

**Response**

```json
{
  "status": "ok"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.settings.update("voice_id", {
        stability: 1,
        useSpeakerBoost: true,
        similarityBoost: 1,
        style: 0,
        speed: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, VoiceSettings

client = ElevenLabs()

client.voices.settings.update(
    voice_id="voice_id",
    request=VoiceSettings(
        stability=1,
        use_speaker_boost=True,
        similarity_boost=1,
        style=0,
        speed=1,
    ),
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/settings/edit"

	payload := strings.NewReader("{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}")

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")
  .header("Content-Type", "application/json")
  .body("{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/voice_id/settings/edit', [
  'body' => '{
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/settings/edit");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stability\": 1,\n  \"use_speaker_boost\": true,\n  \"similarity_boost\": 1,\n  \"style\": 0,\n  \"speed\": 1\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/settings/edit")! as URL,
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
