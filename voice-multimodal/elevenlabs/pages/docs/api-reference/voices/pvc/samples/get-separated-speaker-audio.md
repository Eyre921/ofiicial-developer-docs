---
title: "Get separated speaker audio"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-separated-speaker-audio.md
path: docs/api-reference/voices/pvc/samples/get-separated-speaker-audio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get separated speaker audio

GET https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio

Retrieve the separated audio for a specific speaker.

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-separated-speaker-audio

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
- `sample_id` (string, required) — Sample ID to be used
- `speaker_id` (string, required) — Speaker ID to be used, you can use GET [https://api.elevenlabs.io/v1/voices/\{voice\_id}/samples/\{sample\_id}/speakers](https://api.elevenlabs.io/v1/voices/\{voice_id}/samples/\{sample_id}/speakers) to list all the available speakers for a sample.

## Response

### 200

Successful Response

- `audio_base_64` (string, required) — The base64 encoded audio.
- `media_type` (string, required) — The media type of the audio.
- `duration_secs` (double, required) — The duration of the audio in seconds.

## Examples

**Response**

```json
{
  "audio_base_64": "audio_base_64",
  "media_type": "audio/mpeg",
  "duration_secs": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.speakers.audio.get("sample_id", "speaker_id", "voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.speakers.audio.get(
    sample_id="sample_id",
    speaker_id="speaker_id",
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

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio"

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio")! as URL,
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
