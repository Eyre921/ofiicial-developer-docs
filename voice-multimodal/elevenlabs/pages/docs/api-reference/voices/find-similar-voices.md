---
title: "List similar voices"
source: https://elevenlabs.io/docs/api-reference/voices/find-similar-voices.md
path: docs/api-reference/voices/find-similar-voices
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List similar voices

POST https://api.elevenlabs.io/v1/similar-voices
Content-Type: multipart/form-data

Returns a list of shared voices similar to the provided audio sample. If neither similarity_threshold nor top_k is provided, we will apply default values.

Reference: https://elevenlabs.io/docs/api-reference/voices/find-similar-voices

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `audio_file` (file, optional)
- `similarity_threshold` (double, optional) — Threshold for voice similarity between provided sample and library voices. Values range from 0 to 2. The smaller the value the more similar voices will be returned.
- `top_k` (integer, optional) — Number of most similar voices to return. If similarity_threshold is provided, less than this number of voices may be returned. Values range from 1 to 100.

## Response

### 200

Successful Response

- `voices` (list of object, required) — The list of shared voices
  - `public_owner_id` (string, required) — The public owner id of the voice.
  - `voice_id` (string, required) — The id of the voice.
  - `date_unix` (integer, required) — The date the voice was added to the library in Unix time.
  - `name` (string, required) — The name of the voice.
  - `accent` (string, required) — The accent of the voice.
  - `gender` (string, required) — The gender of the voice.
  - `age` (string, required) — The age of the voice.
  - `descriptive` (string, required) — The descriptive of the voice.
  - `use_case` (string, required) — The use case of the voice.
  - `category` (enum, required) — The category of the voice.
    - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
  - `usage_character_count_1y` (integer, required) — The usage character count of the voice in the last year.
  - `usage_character_count_7d` (integer, required) — The usage character count of the voice in the last 7 days.
  - `play_api_usage_character_count_1y` (integer, required) — The play API usage character count of the voice in the last year.
  - `cloned_by_count` (integer, required) — The number of times the voice has been cloned.
  - `free_users_allowed` (boolean, required) — Whether free users are allowed to use the voice.
  - `live_moderation_enabled` (boolean, required) — Whether live moderation is enabled for the voice.
  - `featured` (boolean, required) — Whether the voice is featured.
  - `language` (string, optional, nullable) — The language of the voice.
  - `locale` (string, optional, nullable) — The locale of the voice.
  - `description` (string, optional, nullable) — The description of the voice.
  - `preview_url` (string, optional, nullable) — The preview URL of the voice.
  - `rate` (double, optional, nullable) — The rate multiplier of the voice.
  - `fiat_rate` (double, optional, nullable) — The rate of the voice in USD per 1000 credits. null if default
  - `verified_languages` (list of object, optional, nullable) — The verified languages of the voice.
    - `language` (string, required) — The language of the voice.
    - `model_id` (string, required) — The voice's model ID.
    - `accent` (string, optional, nullable) — The voice's accent, if applicable.
    - `locale` (string, optional, nullable) — The voice's locale, if applicable.
    - `preview_url` (string, optional, nullable) — The voice's preview URL, if applicable.
  - `notice_period` (integer, optional, nullable) — The notice period of the voice.
  - `instagram_username` (string, optional, nullable) — The Instagram username of the voice.
  - `twitter_username` (string, optional, nullable) — The Twitter username of the voice.
  - `youtube_username` (string, optional, nullable) — The YouTube username of the voice.
  - `tiktok_username` (string, optional, nullable) — The TikTok username of the voice.
  - `image_url` (string, optional, nullable) — The image URL of the voice.
  - `is_added_by_user` (boolean, optional, nullable) — Whether the voice was added by the user.
  - `is_bookmarked` (boolean, optional, nullable) — Whether the voice is bookmarked by the current user. Only relevant when is_added_by_user is True.
- `has_more` (boolean, required) — Whether there are more shared voices in subsequent pages.
- `total_count` (integer, optional, default: 0) — The total number of shared voices matching the query.
- `last_sort_id` (string, optional, nullable)

## Examples

**Request**

```json
{
  "audio_file": "<file: <file1>>"
}
```

**Response**

```json
{
  "voices": [
    {
      "public_owner_id": "63e84100a6bf7874ba37a1bab9a31828a379ec94b891b401653b655c5110880f",
      "voice_id": "sB1b5zUrxQVAFl2PhZFp",
      "date_unix": 1714423232,
      "name": "Alita",
      "accent": "american",
      "gender": "Female",
      "age": "young",
      "descriptive": "calm",
      "use_case": "characters_animation",
      "category": "professional",
      "usage_character_count_1y": 12852,
      "usage_character_count_7d": 12852,
      "play_api_usage_character_count_1y": 12852,
      "cloned_by_count": 11,
      "free_users_allowed": true,
      "live_moderation_enabled": false,
      "featured": false,
      "language": "en",
      "description": "Perfectly calm, neutral and strong voice. Great for a young female protagonist.",
      "preview_url": "https://storage.googleapis.com/eleven-public-prod/wqkMCd9huxXHX1dy5mLJn4QEQHj1/voices/sB1b5zUrxQVAFl2PhZFp/55e71aac-5cb7-4b3d-8241-429388160509.mp3",
      "rate": 1,
      "verified_languages": [
        {
          "language": "en",
          "model_id": "eleven_multilingual_v2",
          "accent": "american",
          "locale": "en-US",
          "preview_url": "https://storage.googleapis.com/eleven-public-prod/wqkMCd9huxXHX1dy5mLJn4QEQHj1/voices/sB1b5zUrxQVAFl2PhZFp/55e71aac-5cb7-4b3d-8241-429388160509.mp3"
        }
      ]
    }
  ],
  "has_more": false,
  "total_count": 0
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.findSimilarVoices({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.find_similar_voices(
    audio_file="example_audio_file",
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

	url := "https://api.elevenlabs.io/v1/similar-voices"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/similar-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/similar-voices")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/similar-voices', [
  'multipart' => [
    [
        'name' => 'audio_file',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/similar-voices");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"audio_file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"similarity_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"top_k\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "audio_file",
    "fileName": "<file1>"
  ],
  [
    "name": "similarity_threshold",
    "value": 
  ],
  [
    "name": "top_k",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/similar-voices")! as URL,
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
