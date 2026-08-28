---
title: "Add samples to PVC voice"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create.md
path: docs/api-reference/voices/pvc/samples/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add samples to PVC voice

POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples
Content-Type: multipart/form-data

Add audio samples to a PVC voice

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

### Body (multipart/form-data)

- `files` (files, required) — Audio files used to create the voice.
- `remove_background_noise` (boolean, optional) — If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

## Response

### 200

Successful Response

- `list of object`
  - `sample_id` (string, optional) — The ID of the sample.
  - `file_name` (string, optional) — The name of the sample file.
  - `mime_type` (string, optional) — The MIME type of the sample file.
  - `size_bytes` (integer, optional) — The size of the sample file in bytes.
  - `hash` (string, optional) — The hash of the sample file.
  - `duration_secs` (double, optional, nullable)
  - `remove_background_noise` (boolean, optional, nullable)
  - `has_isolated_audio` (boolean, optional, nullable)
  - `has_isolated_audio_preview` (boolean, optional, nullable)
  - `speaker_separation` (object, optional, nullable)
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
  - `trim_start` (integer, optional, nullable)
  - `trim_end` (integer, optional, nullable)

## Examples

**Request**

```json
{
  "files": [
    "<file: string>"
  ]
}
```

**Response**

```json
[
  {
    "sample_id": "string",
    "file_name": "string",
    "mime_type": "string",
    "size_bytes": 1,
    "hash": "string",
    "duration_secs": 1.1,
    "remove_background_noise": true,
    "has_isolated_audio": true,
    "has_isolated_audio_preview": true,
    "speaker_separation": {
      "voice_id": "DCwhRBWXzGAHq8TQ4Fs18",
      "sample_id": "DCwhRBWXzGAHq8TQ4Fs18",
      "status": "not_started"
    },
    "trim_start": 1,
    "trim_end": 1
  }
]
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.create("voice_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.create(
    voice_id="voice_id",
    files=["example_files"],
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

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples', [
  'multipart' => [
    [
        'name' => 'files',
        'filename' => 'string',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "files",
    "fileName": "string"
  ],
  [
    "name": "remove_background_noise",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples")! as URL,
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
