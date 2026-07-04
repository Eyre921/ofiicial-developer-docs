---
title: "Get dubbing resource"
source: https://elevenlabs.io/docs/api-reference/dubbing/resources/get-resource.md
path: docs/api-reference/dubbing/resources/get-resource
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dubbing resource

GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}

Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio enabled, returns the dubbing resource.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/get-resource

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/resource/{dubbing_id}:
    get:
      operationId: get
      summary: Get dubbing resource
      description: >-
        Given a dubbing ID generated from the '/v1/dubbing' endpoint with studio
        enabled, returns the dubbing resource.
      tags:
        - resource
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
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
                $ref: '#/components/schemas/DubbingResource'
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
    DubbingMediaReference:
      type: object
      properties:
        src:
          type: string
        content_type:
          type: string
        bucket_name:
          type: string
        random_path_slug:
          type: string
        duration_secs:
          type: number
          format: double
        is_audio:
          type: boolean
        url:
          type: string
      required:
        - src
        - content_type
        - bucket_name
        - random_path_slug
        - duration_secs
        - is_audio
        - url
      title: DubbingMediaReference
    SpeakerTrack:
      type: object
      properties:
        id:
          type: string
        media_ref:
          $ref: '#/components/schemas/DubbingMediaReference'
        speaker_name:
          type: string
        voices:
          type: object
          additionalProperties:
            type: string
        segments:
          type: array
          items:
            type: string
      required:
        - id
        - media_ref
        - speaker_name
        - voices
        - segments
      title: SpeakerTrack
    SegmentSubtitleFrame:
      type: object
      properties:
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        lines:
          type: array
          items:
            type: string
      required:
        - start_time
        - end_time
        - lines
      title: SegmentSubtitleFrame
    DubbedSegment:
      type: object
      properties:
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        text:
          type:
            - string
            - 'null'
        subtitles:
          type: array
          items:
            $ref: '#/components/schemas/SegmentSubtitleFrame'
        audio_stale:
          type: boolean
        media_ref:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
      required:
        - start_time
        - end_time
        - text
        - subtitles
        - audio_stale
        - media_ref
      title: DubbedSegment
    SpeakerSegment:
      type: object
      properties:
        id:
          type: string
        start_time:
          type: number
          format: double
        end_time:
          type: number
          format: double
        text:
          type: string
        subtitles:
          type: array
          items:
            $ref: '#/components/schemas/SegmentSubtitleFrame'
        dubs:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DubbedSegment'
      required:
        - id
        - start_time
        - end_time
        - text
        - subtitles
        - dubs
      title: SpeakerSegment
    RenderType:
      type: string
      enum:
        - mp4
        - aac
        - mp3
        - wav
        - aaf
        - tracks_zip
        - clips_zip
        - zip
      title: RenderType
    RenderStatus:
      type: string
      enum:
        - complete
        - processing
        - failed
      title: RenderStatus
    Render:
      type: object
      properties:
        id:
          type: string
        version:
          type: integer
        language:
          type:
            - string
            - 'null'
        type:
          oneOf:
            - $ref: '#/components/schemas/RenderType'
            - type: 'null'
        media_ref:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
        status:
          $ref: '#/components/schemas/RenderStatus'
      required:
        - id
        - version
        - language
        - type
        - media_ref
        - status
      title: Render
    DubbingResource:
      type: object
      properties:
        id:
          type: string
        version:
          type: integer
        source_language:
          type: string
        target_languages:
          type: array
          items:
            type: string
        input:
          $ref: '#/components/schemas/DubbingMediaReference'
        background:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
        foreground:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaReference'
            - type: 'null'
        speaker_tracks:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SpeakerTrack'
        speaker_segments:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SpeakerSegment'
        renders:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/Render'
      required:
        - id
        - version
        - source_language
        - target_languages
        - input
        - background
        - foreground
        - speaker_tracks
        - speaker_segments
        - renders
      title: DubbingResource
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
  "id": "string",
  "version": 1,
  "source_language": "string",
  "target_languages": [
    "string"
  ],
  "input": {
    "src": "string",
    "content_type": "string",
    "bucket_name": "string",
    "random_path_slug": "string",
    "duration_secs": 1.1,
    "is_audio": true,
    "url": "string"
  },
  "background": {
    "src": "string",
    "content_type": "string",
    "bucket_name": "string",
    "random_path_slug": "string",
    "duration_secs": 1.1,
    "is_audio": true,
    "url": "string"
  },
  "foreground": {
    "src": "string",
    "content_type": "string",
    "bucket_name": "string",
    "random_path_slug": "string",
    "duration_secs": 1.1,
    "is_audio": true,
    "url": "string"
  },
  "speaker_tracks": {},
  "speaker_segments": {},
  "renders": {}
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.get("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.get(
    dubbing_id="dubbing_id",
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id")! as URL,
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
