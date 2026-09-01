---
title: "Create project"
source: https://elevenlabs.io/docs/api-reference/dubbing/create-project.md
path: docs/api-reference/dubbing/create-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create project

POST https://api.elevenlabs.io/v1/dubbing/project
Content-Type: multipart/form-data

Create a dubbing project from an uploaded file (`file`) or a source URL (`source_url`).

Returns as soon as the project record exists, before the source has been fetched: the project starts `queued` and reaches `ready` once its source has been transcribed. Creating a project does not dub anything — add a language target to it for each language you want, or pass `target_language` to queue the first one here.

Preparation can take minutes on a long source, so we recommend passing `webhook_ids` to be notified when the project turns `ready` or `failed`, rather than polling for it.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/create-project

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `file` (file, optional) — The source media file to dub: an audio or video file of at most 3 GiB. Provide this or `source_url`, not both.
- `source_url` (string, optional) — Public HTTP(S) URL the source media is fetched from server-side, subject to the same size and format limits as an upload. Provide this or `file`, not both.
- `reference` (string, optional) — Optional free-form string (at most 500 characters) to identify the project on your end. Stored and echoed back verbatim; it does not affect the dub.
- `source_language` (string, optional) — BCP-47 language tag of the source media; must be a language the transcription model supports. Any region or script subtag is ignored, since transcription is per-language. Omit to auto-detect.
- `model_id` (enum or string, optional) — Dubbing model (`dubbing_v1` or `dubbing_v2`) every language target of this project is dubbed with. Defaults to `dubbing_v2`. Fixed at create time — the source is prepared for this model, so neither the project nor an individual target can change it later.
- `keyterms` (list of string, optional) — Key terms to bias transcription and translation toward (for example, product or brand names). At most 1,000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\` are not allowed. Terms are trimmed and deduplicated.
- `webhook_ids` (list of string, optional) — IDs of workspace webhooks to notify as this project progresses — the alternative to polling, and what we recommend. Each receives a `dubbing_project_ready` or `dubbing_project_failed` event for the project, and a `dubbing_language_completed` or `dubbing_language_failed` event for every language under it; `dubbing_language_completed` carries the output download URLs. At most 3 IDs, each already configured in your workspace — see [Webhooks](https://elevenlabs.io/docs/eleven-api/resources/webhooks) for how to create one and verify its signature. Delivery is best-effort and can repeat, so we recommend handling events idempotently.
- `target_language` (string, optional) — Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready — equivalent to creating the project and then creating one language target. Must be one of the [languages the dubbing model supports](https://elevenlabs.io/docs/help-center/product/dubbing/which-languages-are-supported-in-dubbing), and a region-qualified tag must be one of the supported dialects. Its ID is returned in `language_ids`.
- `transcript` (file, optional) — Enterprise only. Optional JSON transcript to use instead of transcribing the source: a `{"segments": [...]}` document, at most 20,000 segments and 4 MiB. See [Bring your own transcript](https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/bring-your-own-transcript) for the segment fields and their constraints. `source_language` is required whenever a transcript is provided. If any segment carries a `translation`, `target_language` is required and every segment must carry one; those translations seed the target created via `target_language`, which then skips machine translation.

## Response

### 201

Successful Response

- `project_id` (string, required) — Unique identifier of the dubbing project.
- `status` (enum, required) — Lifecycle status of the project: `queued` before the source is picked up, `preparing` while it is transcribed, `ready` once transcription is done and language targets can start, or `failed`. A project is never reported as `processing` — that value belongs to language targets.
  - Allowed values: `queued`, `preparing`, `processing`, `ready`, `failed`
- `revision` (integer, required) — Monotonic counter incremented whenever the source transcript is edited (segment add/edit/delete).
- `created_at` (string, required) — When the project was created.
- `updated_at` (string, required) — When the project was last updated.
- `reference` (string, optional, nullable) — The free-form string you supplied as `reference` when creating the project, or null if you supplied none.
- `source_language` (string, optional, nullable) — BCP-47 language tag of the source media (null if auto-detected).
- `model_id` (string, optional, nullable) — Dubbing model every language target of this project is dubbed with. Fixed at create time and not selectable per language.
- `media` (object, optional, nullable) — Source media metadata, populated once the source has been fetched and decoded (shortly after create, before the project is `ready`); null until then.
  - `filename` (string, optional, nullable) — Original filename of the uploaded source media (null for URL sources).
  - `duration_s` (double, optional, nullable) — Duration of the source media, in seconds.
  - `has_video` (boolean, optional, nullable) — Whether the source media contains a video stream.
  - `mime_type` (string, optional, nullable) — MIME type of the uploaded source media (null for URL sources).
- `language_ids` (list of string, optional, default: []) — Identifiers of the language targets under this project. Populated when a single project is fetched, and on create when `target_language` creates one. Always empty in list responses — list the project's language targets instead.
- `webhook_ids` (list of string, optional, default: []) — IDs of the workspace webhooks notified as this project and its languages reach `ready`, `completed`, or `failed`.
- `error` (object, optional, nullable) — Why the project failed; null unless `status` is `failed`. Also null for the few projects that failed before failure reporting was introduced.
  - `message_type` ("error", required)
  - `error` (string, required)
- `warnings` (list of object, optional) — Non-fatal conditions raised while preparing the source, empty when there are none. Reflects the latest preparation. Conditions raised while dubbing a particular language are reported on that language instead.
  - `type` ("voices_not_permitted", required) — Identifies this warning; branch on it to read the other fields.
  - `speaker_ids` (list of string, required) — Speakers whose voices were not permitted for cloning. The dub used a replacement voice for each of them; all other speakers are unaffected.
  - `message` (string, required) — Human-readable description of the warning, for display. The wording may change at any time, so we recommend branching on `type` instead.

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
