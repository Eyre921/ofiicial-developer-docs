---
title: "Add source segment"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/add-source-segment.md
path: docs/api-reference/dubbing/source-transcript/add-source-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add source segment

POST https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segment
Content-Type: application/json

Enterprise only. Add a new source segment to the transcript. Its span must lie within the source media, last between 0.1 and 25 seconds, and not overlap another segment by the same speaker. Bumps the project's `revision`, discards the affected translations in every language target, and marks any target that had already completed `stale`. No audio changes until you regenerate a target.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/add-source-segment

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the dubbing project.

### Body (application/json)

- `text` (string, required) — The text of the new segment.
- `speaker_id` (string, required) — Identifier of the segment's speaker.
- `start_s` (double, required) — Start time of the segment, in seconds.
- `end_s` (double, required) — End time of the segment, in seconds.

## Response

### 201

Successful Response

- `segment` (object, required) — The segment in its updated state.
  - `id` (string, required) — Stable identifier of the segment, used to address it in edit requests.
  - `text` (string, required) — The transcribed text of the segment.
  - `speaker_id` (string, required) — Identifier of the segment's speaker.
  - `start_s` (double, required) — Start time of the segment, in seconds.
  - `end_s` (double, required) — End time of the segment, in seconds.
  - `external_id` (string, optional, nullable) — The caller-supplied external ID for this segment, if one was provided.
- `revision` (integer, required) — The project's source-transcript revision after this edit.

## Examples

**Request**

```json
{
  "text": "Thanks for watching.",
  "speaker_id": "default_speaker",
  "start_s": 42,
  "end_s": 44
}
```

**Response**

```json
{
  "segment": {
    "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
    "text": "Thanks for watching.",
    "speaker_id": "default_speaker",
    "start_s": 42,
    "end_s": 44
  },
  "revision": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.transcript.createSegment("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        text: "Thanks for watching.",
        speakerId: "default_speaker",
        startS: 42,
        endS: 44,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.transcript.create_segment(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    text="Thanks for watching.",
    speaker_id="default_speaker",
    start_s=42,
    end_s=44,
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment"

	payload := strings.NewReader("{\n  \"text\": \"Thanks for watching.\",\n  \"speaker_id\": \"default_speaker\",\n  \"start_s\": 42,\n  \"end_s\": 44\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Thanks for watching.\",\n  \"speaker_id\": \"default_speaker\",\n  \"start_s\": 42,\n  \"end_s\": 44\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Thanks for watching.\",\n  \"speaker_id\": \"default_speaker\",\n  \"start_s\": 42,\n  \"end_s\": 44\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment', [
  'body' => '{
  "text": "Thanks for watching.",
  "speaker_id": "default_speaker",
  "start_s": 42,
  "end_s": 44
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Thanks for watching.\",\n  \"speaker_id\": \"default_speaker\",\n  \"start_s\": 42,\n  \"end_s\": 44\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "text": "Thanks for watching.",
  "speaker_id": "default_speaker",
  "start_s": 42,
  "end_s": 44
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment")! as URL,
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
