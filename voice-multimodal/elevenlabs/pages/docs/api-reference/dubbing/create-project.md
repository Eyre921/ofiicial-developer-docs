---
title: "Create project"
source: https://elevenlabs.io/docs/api-reference/dubbing/create-project.md
path: docs/api-reference/dubbing/create-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create project

POST https://api.elevenlabs.io/v1/dubbing/project
Content-Type: multipart/form-data

Create a dubbing project from an uploaded file or a source URL.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/create-project

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `file` (file, optional) — The source media file to dub. Provide this or source_url.
- `source_url` (string, optional) — Public URL to fetch the source media from. Provide this or file.
- `reference` (string, optional) — Optional free-form string (max 500 characters) to identify the project on your end.
- `source_language` (string, optional) — BCP-47 language tag of the source media; must be a language the transcription model supports. Any region or script subtag is ignored, since transcription is per-language. Omit to auto-detect.
- `model_id` (enum or string, optional) — Default dubbing model id ('dubbing_v1' or 'dubbing_v2') for the project's language targets; a target may override it. Omit to use the system default.
- `keyterms` (list of string, optional) — Key terms to bias transcription/translation toward (e.g. product or brand names). At most 1000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\` are not allowed.
- `webhook_ids` (list of string, optional) — Ids of workspace webhooks to notify when this project becomes ready or fails, and when any of its languages completes or fails. At most 3; each must be a webhook configured in your workspace.
- `target_language` (string, optional) — Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready. Must be a language the dubbing model supports, and a region-qualified tag must be one of the supported dialects.
- `transcript` (file, optional) — Enterprise only. Optional JSON transcript to use instead of automatic transcription. When provided, source_language is required. Segments may include an optional external_id and an optional translation; if any segment includes a translation, target_language is required and every segment must include one (used to seed the target created via target_language).

## Response

### 201

Successful Response

- `project_id` (string, required) — Unique identifier of the dubbing project.
- `status` (enum, required) — Lifecycle status of the project: 'preparing'/'processing' while it transcribes, 'ready' once transcription is done, or 'failed'.
  - Allowed values: `queued`, `preparing`, `processing`, `ready`, `failed`
- `revision` (integer, required) — Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete).
- `created_at` (string, required) — When the project was created.
- `updated_at` (string, required) — When the project was last updated.
- `reference` (string, optional, nullable) — Optional free-form string the customer can provide to identify the project on their end.
- `source_language` (string, optional, nullable) — BCP-47 language tag of the source media (null if auto-detected).
- `model_id` (string, optional, nullable) — Default dubbing model id applied to this project's language targets.
- `media` (object, optional, nullable) — Source media metadata; null until the project is ready.
  - `filename` (string, optional, nullable) — Original filename of the uploaded source media (null for URL sources).
  - `duration_s` (double, optional, nullable) — Duration of the source media in seconds.
  - `has_video` (boolean, optional, nullable) — Whether the source media contains a video stream.
  - `mime_type` (string, optional, nullable) — MIME type of the uploaded source media.
- `language_ids` (list of string, optional, default: []) — Identifiers of the language targets created under this project.
- `webhook_ids` (list of string, optional, default: []) — Workspace webhooks notified when this project becomes ready or fails, and when any of its languages completes or fails.
- `error` (object, optional, nullable) — Why the project failed; null unless `status` is 'failed'. Also null for the few projects that failed before failure reporting was introduced.
  - `message_type` ("error", required)
  - `error` (string, required)
- `warnings` (list of object, optional) — Non-fatal conditions raised while preparing the source, empty when there are none. Reflects the latest preparation. Conditions raised while dubbing a particular language are reported on that language instead.
  - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the fields below.
  - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; the rest of the speakers are unaffected.
  - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time; branch on `type` instead.

## Examples

**Request**

```json
{
  "file": "<file: <file1>>",
  "reference": "Q3 marketing video",
  "source_language": "en",
  "source_url": "https://example.com/promo.mp4",
  "transcript": "<file: <file1>>"
}
```

**Response**

```json
{
  "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
  "status": "queued",
  "revision": 0,
  "created_at": "2026-07-03T10:15:30Z",
  "updated_at": "2026-07-03T10:15:30Z",
  "reference": "Q3 marketing video",
  "source_language": "en",
  "model_id": "dubbing_v2",
  "language_ids": [],
  "webhook_ids": [],
  "warnings": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.create(
    file="example_file",
    transcript="example_transcript",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"reference\"\r\n\r\nQ3 marketing video\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_language\"\r\n\r\nen\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\nhttps://example.com/promo.mp4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"transcript\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_ids\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"reference\"\r\n\r\nQ3 marketing video\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_language\"\r\n\r\nen\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\nhttps://example.com/promo.mp4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"transcript\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_ids\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/project")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"reference\"\r\n\r\nQ3 marketing video\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_language\"\r\n\r\nen\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\nhttps://example.com/promo.mp4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"transcript\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_ids\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/project', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'reference',
        'contents' => 'Q3 marketing video'
    ],
    [
        'name' => 'source_language',
        'contents' => 'en'
    ],
    [
        'name' => 'source_url',
        'contents' => 'https://example.com/promo.mp4'
    ],
    [
        'name' => 'transcript',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"reference\"\r\n\r\nQ3 marketing video\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_language\"\r\n\r\nen\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\nhttps://example.com/promo.mp4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"transcript\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_ids\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "keyterms",
    "value": 
  ],
  [
    "name": "model_id",
    "value": 
  ],
  [
    "name": "reference",
    "value": "Q3 marketing video"
  ],
  [
    "name": "source_language",
    "value": "en"
  ],
  [
    "name": "source_url",
    "value": "https://example.com/promo.mp4"
  ],
  [
    "name": "target_language",
    "value": 
  ],
  [
    "name": "transcript",
    "fileName": "<file1>"
  ],
  [
    "name": "webhook_ids",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project")! as URL,
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
