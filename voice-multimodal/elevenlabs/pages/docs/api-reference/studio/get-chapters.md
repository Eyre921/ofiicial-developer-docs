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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/chapters:
    get:
      operationId: list
      summary: List Chapters
      description: Returns a list of a Studio project's chapters.
      tags:
        - subpackage_studio/projects/chapters
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetChaptersResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    ChapterState:
      type: string
      enum:
        - default
        - converting
      description: The state of the chapter.
      title: ChapterState
    VoiceStatisticsResponseModel:
      type: object
      properties:
        project_voice_ref_id:
          type: string
          description: The project voice reference ID.
        characters_unconverted:
          type: integer
          description: The number of unconverted characters for this voice.
        characters_converted:
          type: integer
          description: The number of converted characters for this voice.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: >-
            The number of credits needed to convert the remaining audio for this
            voice.
        voice_id:
          type: string
          description: The voice ID.
      required:
        - project_voice_ref_id
        - characters_unconverted
        - characters_converted
        - voice_id
      title: VoiceStatisticsResponseModel
    ChapterStatisticsResponseModel:
      type: object
      properties:
        characters_unconverted:
          type: integer
          description: The number of unconverted characters.
        characters_converted:
          type: integer
          description: The number of converted characters.
        paragraphs_converted:
          type: integer
          description: The number of converted paragraphs.
        paragraphs_unconverted:
          type: integer
          description: The number of unconverted paragraphs.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: The number of credits needed to convert the remaining paragraphs.
        voice_statistics:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VoiceStatisticsResponseModel'
          description: Per-voice breakdown of character counts.
      required:
        - characters_unconverted
        - characters_converted
        - paragraphs_converted
        - paragraphs_unconverted
      title: ChapterStatisticsResponseModel
    ChapterResponseModel:
      type: object
      properties:
        chapter_id:
          type: string
          description: The ID of the chapter.
        name:
          type: string
          description: The name of the chapter.
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
          description: The last conversion date of the chapter.
        conversion_progress:
          type:
            - number
            - 'null'
          format: double
          description: The conversion progress of the chapter.
        can_be_downloaded:
          type: boolean
          description: Whether the chapter can be downloaded.
        state:
          $ref: '#/components/schemas/ChapterState'
          description: The state of the chapter.
        has_video:
          type:
            - boolean
            - 'null'
          description: Whether the chapter has a video.
        has_visual_content:
          type:
            - boolean
            - 'null'
          description: >-
            Whether the chapter has any visual content (video, image, or text
            clips).
        voice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of voice ids used by the chapter
        statistics:
          oneOf:
            - $ref: '#/components/schemas/ChapterStatisticsResponseModel'
            - type: 'null'
          description: The statistics of the chapter.
        last_conversion_error:
          type:
            - string
            - 'null'
          description: The last conversion error of the chapter.
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
      title: ChapterResponseModel
    GetChaptersResponseModel:
      type: object
      properties:
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/ChapterResponseModel'
      required:
        - chapters
      title: GetChaptersResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
