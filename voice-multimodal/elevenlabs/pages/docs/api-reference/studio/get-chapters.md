---
title: "List Chapters"
source: https://elevenlabs.io/docs/api-reference/studio/get-chapters.md
path: docs/api-reference/studio/get-chapters
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Chapters

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters

Returns a list of a Studio project's chapters.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-chapters

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — The ID of the Studio project.

## Response

### 200

Successful Response

- `chapters` (list of object, required)
  - `chapter_id` (string, required) — The ID of the chapter.
  - `name` (string, required) — The name of the chapter.
  - `can_be_downloaded` (boolean, required) — Whether the chapter can be downloaded.
  - `state` (enum, required) — The state of the chapter.
    - Allowed values: `default`, `converting`
  - `last_conversion_date_unix` (integer, optional, nullable) — The last conversion date of the chapter.
  - `conversion_progress` (double, optional, nullable) — The conversion progress of the chapter.
  - `has_video` (boolean, optional, nullable) — Whether the chapter has a video.
  - `has_visual_content` (boolean, optional, nullable) — Whether the chapter has any visual content (video, image, or text clips).
  - `voice_ids` (list of string, optional, nullable) — List of voice ids used by the chapter
  - `statistics` (object, optional, nullable) — The statistics of the chapter.
    - `characters_unconverted` (integer, required) — The number of unconverted characters.
    - `characters_converted` (integer, required) — The number of converted characters.
    - `paragraphs_converted` (integer, required) — The number of converted paragraphs.
    - `paragraphs_unconverted` (integer, required) — The number of unconverted paragraphs.
    - `credits_needed_to_convert` (integer, optional, nullable) — The number of credits needed to convert the remaining paragraphs.
    - `voice_statistics` (list of object, optional, nullable) — Per-voice breakdown of character counts.
      - `project_voice_ref_id` (string, required) — The project voice reference ID.
      - `characters_unconverted` (integer, required) — The number of unconverted characters for this voice.
      - `characters_converted` (integer, required) — The number of converted characters for this voice.
      - `voice_id` (string, required, deprecated) — The voice ID.
      - `credits_needed_to_convert` (integer, optional, nullable) — The number of credits needed to convert the remaining audio for this voice.
  - `last_conversion_error` (string, optional, nullable) — The last conversion error of the chapter.

## Examples

**Response**

```json
{
  "chapters": [
    {
      "chapter_id": "string",
      "name": "string",
      "can_be_downloaded": true,
      "state": "default",
      "last_conversion_date_unix": 1,
      "conversion_progress": 1.1,
      "has_video": true,
      "has_visual_content": true,
      "voice_ids": [
        "string"
      ],
      "statistics": {
        "characters_unconverted": 1000,
        "characters_converted": 500,
        "paragraphs_converted": 20,
        "paragraphs_unconverted": 10,
        "credits_needed_to_convert": 1000,
        "voice_statistics": [
          {
            "project_voice_ref_id": "voice123",
            "characters_unconverted": 600,
            "characters_converted": 300,
            "voice_id": "voice123"
          },
          {
            "project_voice_ref_id": "voice456",
            "characters_unconverted": 400,
            "characters_converted": 200,
            "voice_id": "voice456"
          }
        ]
      },
      "last_conversion_error": "string"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.list("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.list(
    project_id="project_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
