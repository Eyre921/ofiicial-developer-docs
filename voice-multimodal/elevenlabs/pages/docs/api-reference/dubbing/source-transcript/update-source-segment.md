---
title: "Update source segment"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/update-source-segment.md
path: docs/api-reference/dubbing/source-transcript/update-source-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update source segment

PATCH https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segment/{segment_id}
Content-Type: application/json

Enterprise only. Edit a source segment's text, speaker, or timing. Omitted fields are left unchanged. Bumps the project's `revision`, discards the affected translations in every language target, and marks any target that had already completed `stale`. No audio changes until you regenerate a target.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/update-source-segment

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the dubbing project.
- `segment_id` (string, required) — Identifier of the segment to edit.

### Body (application/json)

- `text` (string, optional, nullable) — New text for the segment.
- `speaker_id` (string, optional, nullable) — New speaker ID for the segment.
- `start_s` (double, optional, nullable) — New start time, in seconds.
- `end_s` (double, optional, nullable) — New end time, in seconds.

## Response

### 200

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
  "text": "Welcome to our latest product demo."
}
```

**Response**

```json
{
  "segment": {
    "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
    "text": "Welcome to our latest product demo.",
    "speaker_id": "default_speaker",
    "start_s": 0,
    "end_s": 2.5
  },
  "revision": 4
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.transcript.updateSegment("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "0199a3f0-1c2d-7abc-8def-0123456789ab", {
        text: "Welcome to our latest product demo.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DubbingSegmentUpdateRequest

client = ElevenLabs()

client.dubbing.project.transcript.update_segment(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
    request=DubbingSegmentUpdateRequest(
        text="Welcome to our latest product demo.",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab"

	payload := strings.NewReader("{\n  \"text\": \"Welcome to our latest product demo.\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Welcome to our latest product demo.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Welcome to our latest product demo.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab', [
  'body' => '{
  "text": "Welcome to our latest product demo."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Welcome to our latest product demo.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["text": "Welcome to our latest product demo."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
