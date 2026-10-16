---
title: "Create Music Finetune"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/create.md
path: docs/api-reference/music/finetunes/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Music Finetune

POST https://api.elevenlabs.io/v1/music/finetunes
Content-Type: multipart/form-data

Create a new music finetune

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

This endpoint expects a multipart form with multiple files.

- `name` (string, required) — Name for the finetune (5-200 characters).
- `primary_genre` (string, required) — Primary musical genre of the finetune.
- `files` (files, optional) — Audio files to train on.
- `tags` (list of string, optional) — Tags to associate with the finetune.
- `visibility` (enum, optional) — Finetune visibility. Only 'private' and 'workspace' can be set.
- `model_id` (enum, optional) — The model to create a finetune for.

## Response

### 201

Successful Response

- `id` (string, required) — Unique identifier of the finetune.
- `name` (string, required) — Name of the finetune.
- `tags` (list of string, required) — Tags associated with the finetune.
- `model_id` (string, required) — The base music model the finetune was trained on.
- `created_at` (string, required) — When the finetune was created (UTC).
- `visibility` (enum, required) — Who can access this finetune: `private` (only you), `workspace` (members of your workspace), `public` (ElevenLabs-curated, available to everyone).
  - Allowed values: `private`, `workspace`, `public`
- `created_by` (enum, required) — Who created the finetune: `self`, `workspace`, or `elevenlabs`.
  - Allowed values: `self`, `workspace`, `elevenlabs`
- `status` (enum, required) — Training lifecycle status: pending, in_progress, completed, failed, and blocked.
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `blocked`
- `training_progress` (double, required) — Training progress from 0.0 to 1.0.
- `primary_genre` (string, optional, nullable) — Primary musical genre of the finetune.
- `failure_reason` (enum, optional, nullable) — Reason the finetune failed or was blocked, if applicable.
  - Allowed values: `audio_processing_failed`, `copyright_violation`, `training_failed`

## Errors

### 403 Forbidden Error

Missing permissions to manage music finetunes.

- `any`

### 404 Not Found Error

Finetune not found.

- `any`

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{
  "files": [
    "<file: indie_rock_sample1.wav>",
    "<file: indie_rock_sample2.wav>"
  ],
  "model_id": "music_v2_5",
  "name": "Indie Rock Vibes Finetune",
  "primary_genre": "indie rock",
  "tags": [
    "indie",
    "rock",
    "guitar"
  ],
  "visibility": "workspace"
}
```

**Response**

```json
{
  "id": "a3f47b9e-8c2d-4f1a-9b7e-2d5f3c9a7e1b",
  "name": "Indie Rock Vibes Finetune",
  "tags": [
    "indie",
    "rock",
    "guitar"
  ],
  "model_id": "music_v2_5",
  "created_at": "2024-01-15T09:30:00Z",
  "visibility": "private",
  "created_by": "self",
  "status": "pending",
  "training_progress": 0,
  "primary_genre": "indie rock",
  "failure_reason": null
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/music/finetunes"

files = { "files": "open('indie_rock_sample2.wav', 'rb')" }
payload = {
    "model_id": "music_v2_5",
    "name": "Indie Rock Vibes Finetune",
    "primary_genre": "indie rock",
    "tags": "[
  \"indie\",
  \"rock\",
  \"guitar\"
]",
    "visibility": "workspace"
}

response = requests.post(url, data=payload, files=files)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/music/finetunes';
const form = new FormData();
form.append('files', 'indie_rock_sample1.wav');
form.append('files', 'indie_rock_sample2.wav');
form.append('model_id', 'music_v2_5');
form.append('name', 'Indie Rock Vibes Finetune');
form.append('primary_genre', 'indie rock');
form.append('tags', '[
  "indie",
  "rock",
  "guitar"
]');
form.append('visibility', 'workspace');

const options = {method: 'POST'};

options.body = form;

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/music/finetunes"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample1.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample2.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2_5\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Rock Vibes Finetune\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie rock\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"indie\",\n  \"rock\",\n  \"guitar\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample1.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample2.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2_5\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Rock Vibes Finetune\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie rock\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"indie\",\n  \"rock\",\n  \"guitar\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/finetunes")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample1.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample2.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2_5\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Rock Vibes Finetune\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie rock\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"indie\",\n  \"rock\",\n  \"guitar\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/finetunes', [
  'multipart' => [
    [
        'name' => 'files',
        'filename' => 'indie_rock_sample1.wav',
        'contents' => null
    ],
    [
        'name' => 'files',
        'filename' => 'indie_rock_sample2.wav',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'music_v2_5'
    ],
    [
        'name' => 'name',
        'contents' => 'Indie Rock Vibes Finetune'
    ],
    [
        'name' => 'primary_genre',
        'contents' => 'indie rock'
    ],
    [
        'name' => 'tags',
        'contents' => '[
  "indie",
  "rock",
  "guitar"
]'
    ],
    [
        'name' => 'visibility',
        'contents' => 'workspace'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/finetunes");
var request = new RestRequest(Method.POST);
request.AddParameter("undefined", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample1.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"indie_rock_sample2.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2_5\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Rock Vibes Finetune\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie rock\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"indie\",\n  \"rock\",\n  \"guitar\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation
let parameters = [
  [
    "name": "files",
    "fileName": "indie_rock_sample1.wav"
  ],
  [
    "name": "files",
    "fileName": "indie_rock_sample2.wav"
  ],
  [
    "name": "model_id",
    "value": "music_v2_5"
  ],
  [
    "name": "name",
    "value": "Indie Rock Vibes Finetune"
  ],
  [
    "name": "primary_genre",
    "value": "indie rock"
  ],
  [
    "name": "tags",
    "value": "[
  \"indie\",
  \"rock\",
  \"guitar\"
]"
  ],
  [
    "name": "visibility",
    "value": "workspace"
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/finetunes")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
