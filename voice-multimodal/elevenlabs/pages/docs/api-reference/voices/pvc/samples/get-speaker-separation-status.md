---
title: "Get PVC speaker separation status"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-speaker-separation-status.md
path: docs/api-reference/voices/pvc/samples/get-speaker-separation-status
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get PVC speaker separation status

GET https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers

Retrieve the status of the speaker separation process and the list of detected speakers if complete.

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-speaker-separation-status

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

## Response

### 200

Successful Response

- `voice_id` (string, required) — The ID of the voice.
- `sample_id` (string, required) — The ID of the sample.
- `status` (enum, required) — The status of the speaker separation.
  - Allowed values: `not_started`, `pending`, `completed`, `failed`
- `speakers` (map from string to object, optional, nullable) — The speakers of the sample.
  - `speaker_id` (string, required) — The ID of the speaker.
  - `duration_secs` (double, required) — The duration of the speaker segment in seconds.
  - `utterances` (list of object, optional, nullable) — The utterances of the speaker.
    - `start` (double, required) — The start time of the utterance in seconds.
    - `end` (double, required) — The end time of the utterance in seconds.
- `selected_speaker_ids` (list of string, optional, nullable) — The IDs of the selected speakers.

## Examples

**Response**

```json
{
  "voice_id": "DCwhRBWXzGAHq8TQ4Fs18",
  "sample_id": "DCwhRBWXzGAHq8TQ4Fs18",
  "status": "not_started"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.speakers.get("sample_id", "voice_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.speakers.get(
    sample_id="sample_id",
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

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers"

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers")! as URL,
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
