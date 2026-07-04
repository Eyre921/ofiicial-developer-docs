---
title: "Upload Music"
source: https://elevenlabs.io/docs/api-reference/music/upload.md
path: docs/api-reference/music/upload
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Upload Music

POST https://api.elevenlabs.io/v1/music/upload
Content-Type: multipart/form-data

Upload a music file to be later used for inpainting. Price for uploading is the same as the one for song generation. All uploaded content gets inspected for copyright infringement. If copyrighted content is detected, half of the request cost is still charged.

Reference: https://elevenlabs.io/docs/api-reference/music/upload

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/upload:
    post:
      operationId: upload
      summary: Upload Music
      description: >-
        Upload a music file to be later used for inpainting. Price for uploading
        is the same as the one for song generation. All uploaded content gets
        inspected for copyright infringement. If copyrighted content is
        detected, half of the request cost is still charged.
      tags:
        - music
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successfully uploaded music file with optional composition plan
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MusicUploadResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: The audio file to upload.
                extract_composition_plan:
                  $ref: >-
                    #/components/schemas/V1MusicUploadPostRequestBodyContentMultipartFormDataSchemaExtractCompositionPlan
                  default: false
                  description: >-
                    Whether to generate and return the composition plan for the
                    uploaded song. Pass a model id (`music_v1` or `music_v2`) to
                    control which composition plan format is returned. Passing
                    `true`/`false` is deprecated; `true` defaults to the
                    `music_v1` plan format. Enabling this will increase the
                    latency.
                with_timestamps:
                  type: boolean
                  default: false
                  description: >-
                    Whether to transcribe the uploaded song and return
                    word-level timestamps. If True, the response will include
                    words_timestamps but will increase the latency.
              required:
                - file
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
    V1MusicUploadPostRequestBodyContentMultipartFormDataSchemaExtractCompositionPlan:
      type: string
      enum:
        - music_v1
        - music_v2
      description: >-
        Whether to generate and return the composition plan for the uploaded
        song. Pass a model id (`music_v1` or `music_v2`) to control which
        composition plan format is returned. Passing `true`/`false` is
        deprecated; `true` defaults to the `music_v1` plan format. Enabling this
        will increase the latency.
      title: >-
        V1MusicUploadPostRequestBodyContentMultipartFormDataSchemaExtractCompositionPlan
    TimeRange:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - start_ms
        - end_ms
      title: TimeRange
    SectionSource:
      type: object
      properties:
        song_id:
          type: string
          description: >-
            The ID of the song to source the section from. You can find the song
            ID in the response headers when you generate a song.
        range:
          $ref: '#/components/schemas/TimeRange'
          description: The range to extract from the source song.
        negative_ranges:
          type: array
          items:
            $ref: '#/components/schemas/TimeRange'
          description: The ranges to exclude from the 'range'.
      required:
        - song_id
        - range
      title: SectionSource
    SongSection:
      type: object
      properties:
        section_name:
          type: string
          description: The name of the section. Must be between 1 and 100 characters.
        positive_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in this
            section. Use English language for best result.
        negative_local_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in this
            section. Use English language for best result.
        duration_ms:
          type: integer
          description: >-
            The duration of the section in milliseconds. Must be between 3000ms
            and 120000ms.
        lines:
          type: array
          items:
            type: string
          description: >-
            The lyrics of the section. Max 30 lines per section and max 200
            characters per line.
        source_from:
          oneOf:
            - $ref: '#/components/schemas/SectionSource'
            - type: 'null'
          description: Optional source to extract the section from. Used for inpainting.
      required:
        - section_name
        - positive_local_styles
        - negative_local_styles
        - duration_ms
        - lines
      title: SongSection
    MusicPrompt:
      type: object
      properties:
        positive_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in the
            entire song. Use English language for best result.
        negative_global_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in the
            entire song. Use English language for best result.
        sections:
          type: array
          items:
            $ref: '#/components/schemas/SongSection'
          description: The sections of the song.
      required:
        - positive_global_styles
        - negative_global_styles
        - sections
      description: >-
        Composition plan for the `music_v1` model. Using this field with any
        other model will result in an error.
      title: MusicPrompt
    GenerationChunkInputContextAdherence:
      type: string
      enum:
        - low
        - medium
        - high
      default: high
      description: >-
        How much the model adheres to the context of its surrounding chunks. Low
        adherence means the model can deviate from the context and be more
        creative. High adherence means the model will be more consistent with
        the context.
      title: GenerationChunkInputContextAdherence
    AudioRefChunk:
      type: object
      properties:
        song_id:
          type: string
          description: >-
            The ID of the song to source the chunk from. You can find the song
            ID in the response headers when you generate a song.
        range:
          $ref: '#/components/schemas/TimeRange'
          description: The time range to extract from the song.
      required:
        - song_id
        - range
      title: AudioRefChunk
    GenerationChunkInputConditionStrength:
      type: string
      enum:
        - low
        - medium
        - high
        - xhigh
      description: >-
        How strongly the model adheres to the conditioning reference. Low
        strength means the model will be more creative and deviate from the
        reference. High strength means the model will be more consistent with
        the reference.
      title: GenerationChunkInputConditionStrength
    GenerationChunk-Input:
      type: object
      properties:
        text:
          type: string
          description: >-
            The text config to be generated for this chunk. Can contain section
            name in square brackets, e.g. [Verse 1], lyrics lines, and inline
            directions in curly braces, e.g. {scratching}.
        duration_ms:
          type: integer
          description: >-
            The duration of the chunk in milliseconds. Must be between 3000ms
            and 120000ms.
        positive_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should be present in this
            chunk. Use English language for best results. The styles for the
            first chunk are the most important as they set the overall tone and
            genre. Styles for subsequent chunks can be used to add nuance,
            progression, emphasis, or change the direction of the song. Aim to
            have at least 6-7 styles in early chunks until the direction is
            established. Generic styles like 'great production quality' are good
            default styles to append to the list.
        negative_styles:
          type: array
          items:
            type: string
          description: >-
            The styles and musical directions that should not be present in this
            chunk. Use English language for best results. Leaving empty is a
            good default, only use this field if you want to explicitly avoid a
            particular style or direction.
        context_adherence:
          $ref: '#/components/schemas/GenerationChunkInputContextAdherence'
          default: high
          description: >-
            How much the model adheres to the context of its surrounding chunks.
            Low adherence means the model can deviate from the context and be
            more creative. High adherence means the model will be more
            consistent with the context.
        conditioning_ref:
          oneOf:
            - $ref: '#/components/schemas/AudioRefChunk'
            - type: 'null'
          description: >-
            The audio reference to condition the generation on. The first chunk
            is the most important as it will influence the generation of all
            subsequent chunks. Thus, if you want to apply conditioning to the
            entire song, start conditioning from the first chunk.
        condition_strength:
          oneOf:
            - $ref: '#/components/schemas/GenerationChunkInputConditionStrength'
            - type: 'null'
          description: >-
            How strongly the model adheres to the conditioning reference. Low
            strength means the model will be more creative and deviate from the
            reference. High strength means the model will be more consistent
            with the reference.
      required:
        - text
        - duration_ms
        - positive_styles
      title: GenerationChunk-Input
    CompositionPlanChunksItems:
      oneOf:
        - $ref: '#/components/schemas/GenerationChunk-Input'
        - $ref: '#/components/schemas/AudioRefChunk'
      title: CompositionPlanChunksItems
    CompositionPlan:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/CompositionPlanChunksItems'
          description: The chunks that make up the generation.
      required:
        - chunks
      description: >-
        Composition plan for the `music_v2` model. Using this field with any
        other model will result in an error.
      title: CompositionPlan
    MusicUploadResponseCompositionPlan:
      oneOf:
        - $ref: '#/components/schemas/MusicPrompt'
        - $ref: '#/components/schemas/CompositionPlan'
      description: >-
        The composition plan extracted from the uploaded song. Only present if
        `extract_composition_plan` was provided in the request body.
      title: MusicUploadResponseCompositionPlan
    WordTimestamp:
      type: object
      properties:
        word:
          type: string
        start_ms:
          type: integer
        end_ms:
          type: integer
      required:
        - word
        - start_ms
        - end_ms
      title: WordTimestamp
    MusicUploadResponse:
      type: object
      properties:
        song_id:
          type: string
          description: Unique identifier for the uploaded song
        composition_plan:
          oneOf:
            - $ref: '#/components/schemas/MusicUploadResponseCompositionPlan'
            - type: 'null'
          description: >-
            The composition plan extracted from the uploaded song. Only present
            if `extract_composition_plan` was provided in the request body.
        words_timestamps:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WordTimestamp'
          description: >-
            Word-level timestamps transcribed from the uploaded song. Only
            present if `with_timestamps` was True in the request body
      required:
        - song_id
      description: Response model for music upload endpoint.
      title: MusicUploadResponse
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



**Request**

```json
{
  "file": "<file: string>"
}
```

**Response**

```json
{
  "song_id": "jR4Xz8kL2mNpQ9wVtY1b"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.upload({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.upload(
    file="example_file",
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

	url := "https://api.elevenlabs.io/v1/music/upload"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/music/upload")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/upload")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/upload', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/upload");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"with_timestamps\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "extract_composition_plan",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "string"
  ],
  [
    "name": "with_timestamps",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/upload")! as URL,
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
