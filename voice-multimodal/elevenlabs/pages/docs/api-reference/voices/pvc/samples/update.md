---
title: "Update PVC voice sample"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/update.md
path: docs/api-reference/voices/pvc/samples/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update PVC voice sample

POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}
Content-Type: application/json

Update a PVC voice sample - apply noise removal, select speaker, change trim times or file name.

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/update

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

### Body (application/json)

- `remove_background_noise` (boolean, optional, default: false) — If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.
- `selected_speaker_ids` (list of string, optional, nullable) — Speaker IDs to be used for PVC training. Make sure you send all the speaker IDs you want to use for PVC training in one request because the last request will override the previous ones.
- `trim_start_time` (integer, optional, nullable) — The start time of the audio to be used for PVC training. Time should be in milliseconds
- `trim_end_time` (integer, optional, nullable) — The end time of the audio to be used for PVC training. Time should be in milliseconds
- `file_name` (string, optional, nullable) — The name of the audio file to be used for PVC training.

## Response

### 200

Successful Response

- `voice_id` (string, required) — The ID of the voice.

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "voice_id": "b38kUX8pkfYO2kHyqfFy"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.update("voice_id", "sample_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.update(
    voice_id="voice_id",
    sample_id="sample_id",
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

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")! as URL,
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
