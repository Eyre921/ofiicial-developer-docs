---
title: "Get voice sample audio"
source: https://elevenlabs.io/docs/api-reference/voices/samples/get.md
path: docs/api-reference/voices/samples/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get voice sample audio

GET https://api.elevenlabs.io/v1/voices/{voice_id}/samples/{sample_id}/audio

Returns the audio corresponding to a sample attached to a voice.

Reference: https://elevenlabs.io/docs/api-reference/voices/samples/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.
- `sample_id` (string, required) — ID of the sample to be used. You can use the [Get voices](/docs/api-reference/voices/get) endpoint list all the available samples for a voice.

## Response

### 200

Successful Response

## Examples

**Request**

```json
{}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk-1234abcd5678efgh9012ijkl",
    });
    await client.voices.samples.audio.get("21m00Tcm4TlvDq8ikWAM", "VW7YKqPnjY4h39yTbx2L");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk-1234abcd5678efgh9012ijkl",
)

client.voices.samples.audio.get(
    voice_id="21m00Tcm4TlvDq8ikWAM",
    sample_id="VW7YKqPnjY4h39yTbx2L",
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

	url := "https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk-1234abcd5678efgh9012ijkl")
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

url = URI("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk-1234abcd5678efgh9012ijkl'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio")
  .header("xi-api-key", "sk-1234abcd5678efgh9012ijkl")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk-1234abcd5678efgh9012ijkl',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk-1234abcd5678efgh9012ijkl");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk-1234abcd5678efgh9012ijkl",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/21m00Tcm4TlvDq8ikWAM/samples/VW7YKqPnjY4h39yTbx2L/audio")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
