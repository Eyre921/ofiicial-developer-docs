---
title: "Post agent hold audio"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/hold-audio/create.md
path: docs/eleven-agents/api-reference/agents/hold-audio/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Post agent hold audio

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/hold-audio
Content-Type: multipart/form-data

Sets the custom hold audio played on loop to callers waiting in the agent's concurrency wait queue. Replaces any previously uploaded clip.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/hold-audio/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Body (multipart/form-data)

This endpoint expects a multipart form containing a file.

- `hold_audio_file` (file, required) — An MP3 or WAV file played on loop to callers waiting in the agent's concurrency wait queue. Maximum size 40 MB, maximum duration 180 seconds.

## Response

### 200

Successful Response

- `agent_id` (string, required)
- `hold_audio` (object, required) — Custom hold audio played on loop to callers waiting in the agent's queue. Set by uploading a file through the agent hold-audio endpoint. Values sent in agent create or update requests are ignored.
  - `audio_path` (string, required) — Storage path of the uploaded clip
  - `audio_url` (string, required) — Public CDN URL of the uploaded clip
  - `original_filename` (string, required) — Filename of the uploaded clip as provided by the user
  - `duration_secs` (double, required) — Duration of the uploaded clip in seconds
  - `size_bytes` (integer, required) — Size of the uploaded clip in bytes

## Errors

### 422 Hold Audio Create Request Unprocessable Entity Error

Validation Error

- `detail` (list of object, optional)
  - `loc` (list of string or integer, required)
  - `msg` (string, required)
  - `type` (string, required)

## Examples

**Request**

```json
{
  "hold_audio_file": "<file: <file1>>"
}
```

**Response**

```json
{
  "agent_id": "agent_id",
  "hold_audio": {
    "audio_path": "audio_path",
    "audio_url": "audio_url",
    "original_filename": "original_filename",
    "duration_secs": 1.1,
    "size_bytes": 1
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.holdAudio.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.hold_audio.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    hold_audio_file="example_hold_audio_file",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"hold_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"hold_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"hold_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio', [
  'multipart' => [
    [
        'name' => 'hold_audio_file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"hold_audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "hold_audio_file",
    "fileName": "<file1>"
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/hold-audio")! as URL,
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
