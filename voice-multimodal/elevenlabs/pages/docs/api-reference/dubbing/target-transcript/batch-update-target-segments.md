---
title: "Batch update target segments"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/batch-update-target-segments.md
path: docs/api-reference/dubbing/target-transcript/batch-update-target-segments
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Batch update target segments

PATCH https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript/segments
Content-Type: application/json

Enterprise only. Edit several segments' translations for a language target in one atomic request.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/batch-update-target-segments

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the dubbing project.
- `language_id` (string, required) — Identifier of the language target.

### Body (application/json)

- `segments` (map from string to object, required) — Map of segment id to the translation edit to apply to that segment.
  - `translation` (string, optional, nullable) — New translated text, or null to mark the segment for re-translation.

## Response

### 200

Successful Response

- `segments` (list of object, required) — The edited target segments in their updated state.
  - `id` (string, required) — Stable identifier of the segment (from the source).
  - `speaker_id` (string, required) — Identifier of the segment's speaker.
  - `start_s` (double, required) — Start time of the segment, in seconds.
  - `end_s` (double, required) — End time of the segment, in seconds.
  - `source_text` (string, required) — The source-language text of the segment.
  - `translation` (string, optional, nullable) — The translated text, or null if not translated yet (needs translation).
- `revision` (integer, required) — The target's revision after the edits.

## Examples

**Request**

```json
{
  "segments": {
    "0199a3f0-1c2d-7abc-8def-0123456789ab": {
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "translation": "Empecemos."
    }
  }
}
```

**Response**

```json
{
  "segments": [
    {
      "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
      "speaker_id": "default_speaker",
      "start_s": 0,
      "end_s": 2.5,
      "source_text": "Welcome to our product demo.",
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    {
      "id": "0199a3f0-3e4f-7abc-8def-0123456789cd",
      "speaker_id": "narrator",
      "start_s": 2.5,
      "end_s": 4,
      "source_text": "Let's get started.",
      "translation": "Empecemos."
    }
  ],
  "revision": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.updateSegments("lang_1001kwkyxp0je6ktn4knsfrasx5s", "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        segments: {
            "0199a3f0-1c2d-7abc-8def-0123456789ab": {
                translation: "Bienvenido a nuestra última demostración de producto.",
            },
            "0199a3f0-3e4f-7abc-8def-0123456789cd": {
                translation: "Empecemos.",
            },
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DubbingTargetSegmentUpdateRequest

client = ElevenLabs()

client.dubbing.project.language.transcript.update_segments(
    language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segments={
        "0199a3f0-1c2d-7abc-8def-0123456789ab": DubbingTargetSegmentUpdateRequest(
            translation="Bienvenido a nuestra última demostración de producto.",
        ),
        "0199a3f0-3e4f-7abc-8def-0123456789cd": DubbingTargetSegmentUpdateRequest(
            translation="Empecemos.",
        )
    },
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments"

	payload := strings.NewReader("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments', [
  'body' => '{
  "segments": {
    "0199a3f0-1c2d-7abc-8def-0123456789ab": {
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "translation": "Empecemos."
    }
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["segments": [
    "0199a3f0-1c2d-7abc-8def-0123456789ab": ["translation": "Bienvenido a nuestra última demostración de producto."],
    "0199a3f0-3e4f-7abc-8def-0123456789cd": ["translation": "Empecemos."]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")! as URL,
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
