---
title: "Retrieve a transcript"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/transcripts/get.md
path: docs/api-reference/legacy/dubbing/transcripts/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retrieve a transcript

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/transcripts/{language_code}/format/{format_type}

Fetch the transcript for one of the languages in a dub.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/transcripts/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `dubbing_id` (string, required) — ID of the dubbing project.
- `language_code` (string, required) — ISO-693 language code to retrieve the transcript for. Use 'source' to fetch the transcript of the original media.
- `format_type` (enum, required) — Format to return transcript in. For subtitles use either 'srt' or 'webvtt', and for a full transcript use 'json'. The 'json' format is not yet supported for Dubbing Studio.
  - Allowed values: `srt`, `webvtt`, `json`

## Response

### 200

Successful Response

- `transcript_format` (enum, required)
  - Allowed values: `srt`, `webvtt`, `json`
- `srt` (string, optional, nullable)
- `webvtt` (string, optional, nullable)
- `json` (DubbingTranscript, optional, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### DubbingTranscript

- `language` (string, required)
- `utterances` (list of DubbingTranscriptUtterance, required)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### DubbingTranscriptUtterance

- `text` (string, optional, default: )
- `speaker_id` (string, optional, default: unknown)
- `start_s` (double, optional, default: 0)
- `end_s` (double, optional, default: 0)
- `words` (list of DubbingTranscriptWord, optional)

### ValidationErrorLocItems

### DubbingTranscriptWord

- `text` (string, optional, default: )
- `word_type` (string, optional, default: unknown)
- `start_s` (double, optional, default: 0)
- `end_s` (double, optional, default: 0)
- `characters` (list of DubbingTranscriptCharacter, optional)

### DubbingTranscriptCharacter

- `text` (string, optional, default: )
- `start_s` (double, optional, default: 0)
- `end_s` (double, optional, default: 0)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "transcript_format": "srt",
  "srt": "1\n00:00:01,000 --> 00:00:04,500\nWelcome to our presentation on climate change.\n\n2\n00:00:05,000 --> 00:00:09,200\nToday we will explore the key factors driving global warming.",
  "webvtt": null,
  "json": {
    "language": "en",
    "utterances": [
      {
        "text": "Welcome to our presentation on climate change.",
        "speaker_id": "speaker_01",
        "start_s": 1,
        "end_s": 4.5,
        "words": [
          {
            "text": "Welcome",
            "word_type": "word",
            "start_s": 1,
            "end_s": 1.45,
            "characters": [
              {
                "text": "W",
                "start_s": 1,
                "end_s": 1.08
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/source/format/srt")! as URL,
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
