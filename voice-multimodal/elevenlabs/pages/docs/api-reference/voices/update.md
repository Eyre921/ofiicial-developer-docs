---
title: "Edit voice"
source: https://elevenlabs.io/docs/api-reference/voices/update.md
path: docs/api-reference/voices/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Edit voice

POST https://api.elevenlabs.io/v1/voices/{voice_id}/edit
Content-Type: multipart/form-data

Edit a voice created by you.

Reference: https://elevenlabs.io/docs/api-reference/voices/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

### Body (multipart/form-data)

- `name` (string, required) — The name that identifies this voice. This will be displayed in the dropdown of the website.
- `files` (files, optional) — Audio files to add to the voice
- `remove_background_noise` (boolean, optional) — If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.
- `description` (string, optional) — A description of the voice.
- `labels` (map from string to string or string, optional) — Labels for the voice. Keys can be language, accent, gender, or age.
- `moderate_metadata` (boolean, optional) — Run synchronous LLM moderation over the voice name and description when they change. Has no effect unless the voice_library_metadata_moderation feature flag is enabled for the user.

## Response

### 200

Successful Response

- `status` (string, required) — The status of the voice edit request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

## Examples

**Request**

```json
{
  "files": [],
  "name": "John Smith"
}
```

**Response**

```json
{
  "status": "ok"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.update("voice_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.update(
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/edit"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"moderate_metadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/edit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"moderate_metadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/voice_id/edit")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"moderate_metadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/voice_id/edit', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'John Smith'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/edit");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"labels\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"moderate_metadata\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nJohn Smith\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "labels",
    "value": 
  ],
  [
    "name": "moderate_metadata",
    "value": 
  ],
  [
    "name": "name",
    "value": "John Smith"
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/edit")! as URL,
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
