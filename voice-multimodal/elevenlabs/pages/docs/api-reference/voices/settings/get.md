---
title: "Get voice settings"
source: https://elevenlabs.io/docs/api-reference/voices/settings/get.md
path: docs/api-reference/voices/settings/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get voice settings

GET https://api.elevenlabs.io/v1/voices/{voice_id}/settings

Returns the settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

Reference: https://elevenlabs.io/docs/api-reference/voices/settings/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

## Response

### 200

Successful Response

- `stability` (double, optional, nullable, default: 0.5) — Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
- `use_speaker_boost` (boolean, optional, nullable, default: true) — This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.
- `similarity_boost` (double, optional, nullable, default: 0.75) — Determines how closely the AI should adhere to the original voice when attempting to replicate it.
- `style` (double, optional, nullable, default: 0) — Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.
- `speed` (double, optional, nullable, default: 1) — Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up.

## Examples

**Response**

```json
{
  "stability": 1,
  "use_speaker_boost": true,
  "similarity_boost": 1,
  "style": 0,
  "speed": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.settings.get("voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.settings.get(
    voice_id="voice_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/voice_id/settings"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/voice_id/settings")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/voice_id/settings');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/settings");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/settings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
