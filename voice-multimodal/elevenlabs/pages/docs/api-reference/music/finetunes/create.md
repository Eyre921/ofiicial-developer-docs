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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/finetunes:
    post:
      operationId: create
      summary: Create Music Finetune
      description: Create a new music finetune
      tags:
        - finetunes
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MusicFinetuneResponseModel'
        '403':
          description: Missing permissions to manage music finetunes.
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Finetune not found.
          content:
            application/json:
              schema:
                description: Any type
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
                name:
                  type: string
                  description: Name for the finetune (5-200 characters).
                primary_genre:
                  type: string
                  description: Primary musical genre of the finetune.
                files:
                  type: array
                  items:
                    type: string
                    format: binary
                  description: Audio files to train on.
                tags:
                  type: array
                  items:
                    type: string
                  default: []
                  description: Tags to associate with the finetune.
                visibility:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaVisibility
                    - type: 'null'
                  description: >-
                    Finetune visibility. Only 'private' and 'workspace' can be
                    set.
                model_id:
                  $ref: >-
                    #/components/schemas/V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaModelId
                  default: music_v1
                  description: The model to create a finetune for.
              required:
                - name
                - primary_genre
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
    V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaVisibility:
      type: string
      enum:
        - private
        - workspace
      description: Finetune visibility. Only 'private' and 'workspace' can be set.
      title: V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaVisibility
    V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaModelId:
      type: string
      enum:
        - music_v1
        - music_v2
      default: music_v1
      description: The model to create a finetune for.
      title: V1MusicFinetunesPostRequestBodyContentMultipartFormDataSchemaModelId
    FinetuneVisibility:
      type: string
      enum:
        - private
        - workspace
        - public
      title: FinetuneVisibility
    FinetuneCreatedBy:
      type: string
      enum:
        - self
        - workspace
        - elevenlabs
      title: FinetuneCreatedBy
    MusicFinetuneStatus:
      type: string
      enum:
        - pending
        - in_progress
        - completed
        - failed
        - blocked
      title: MusicFinetuneStatus
    MusicFinetuneFailureReason:
      type: string
      enum:
        - audio_processing_failed
        - copyright_violation
        - training_failed
      title: MusicFinetuneFailureReason
    MusicFinetuneResponseModel:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the finetune.
        name:
          type: string
          description: Name of the finetune.
        tags:
          type: array
          items:
            type: string
          description: Tags associated with the finetune.
        primary_genre:
          type:
            - string
            - 'null'
          description: Primary musical genre of the finetune.
        model_id:
          type: string
          description: The base music model the finetune was trained on.
        created_at:
          type: string
          format: date-time
          description: When the finetune was created (UTC).
        visibility:
          $ref: '#/components/schemas/FinetuneVisibility'
          description: >-
            Who can access this finetune: `private` (only you), `workspace`
            (members of your workspace), `public` (ElevenLabs-curated, available
            to everyone).
        created_by:
          $ref: '#/components/schemas/FinetuneCreatedBy'
          description: 'Who created the finetune: `self`, `workspace`, or `elevenlabs`.'
        status:
          $ref: '#/components/schemas/MusicFinetuneStatus'
          description: >-
            Training lifecycle status: pending, in_progress, completed, failed,
            and blocked.
        training_progress:
          type: number
          format: double
          description: Training progress from 0.0 to 1.0.
        failure_reason:
          oneOf:
            - $ref: '#/components/schemas/MusicFinetuneFailureReason'
            - type: 'null'
          description: Reason the finetune failed or was blocked, if applicable.
      required:
        - id
        - name
        - tags
        - model_id
        - created_at
        - visibility
        - created_by
        - status
        - training_progress
      title: MusicFinetuneResponseModel
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
  "files": [
    "<file: acoustic_guitar_01.wav>",
    "<file: vocals_01.wav>"
  ],
  "model_id": "music_v2",
  "name": "Indie Acoustic Vibes",
  "primary_genre": "indie",
  "tags": [
    "acoustic",
    "indie",
    "relaxing"
  ],
  "visibility": "workspace"
}
```

**Response**

```json
{
  "id": "a3f47b9e-8c2d-4f1a-9b7e-2d3f5c6a7b8d",
  "name": "Indie Acoustic Vibes",
  "tags": [
    "acoustic",
    "indie",
    "relaxing"
  ],
  "model_id": "music_v2",
  "created_at": "2024-04-20T14:45:00Z",
  "visibility": "workspace",
  "created_by": "self",
  "status": "in_progress",
  "training_progress": 0.35,
  "primary_genre": "indie",
  "failure_reason": null
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.finetunes.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.finetunes.create(
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

	url := "https://api.elevenlabs.io/v1/music/finetunes"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"acoustic_guitar_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"vocals_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Acoustic Vibes\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"acoustic\",\n  \"indie\",\n  \"relaxing\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"acoustic_guitar_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"vocals_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Acoustic Vibes\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"acoustic\",\n  \"indie\",\n  \"relaxing\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/finetunes")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"acoustic_guitar_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"vocals_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Acoustic Vibes\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"acoustic\",\n  \"indie\",\n  \"relaxing\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n")
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
        'filename' => 'acoustic_guitar_01.wav',
        'contents' => null
    ],
    [
        'name' => 'files',
        'filename' => 'vocals_01.wav',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'music_v2'
    ],
    [
        'name' => 'name',
        'contents' => 'Indie Acoustic Vibes'
    ],
    [
        'name' => 'primary_genre',
        'contents' => 'indie'
    ],
    [
        'name' => 'tags',
        'contents' => '[
  "acoustic",
  "indie",
  "relaxing"
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
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"acoustic_guitar_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"vocals_01.wav\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nmusic_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nIndie Acoustic Vibes\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"primary_genre\"\r\n\r\nindie\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n[\n  \"acoustic\",\n  \"indie\",\n  \"relaxing\"\n]\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"visibility\"\r\n\r\nworkspace\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "files",
    "fileName": "acoustic_guitar_01.wav"
  ],
  [
    "name": "files",
    "fileName": "vocals_01.wav"
  ],
  [
    "name": "model_id",
    "value": "music_v2"
  ],
  [
    "name": "name",
    "value": "Indie Acoustic Vibes"
  ],
  [
    "name": "primary_genre",
    "value": "indie"
  ],
  [
    "name": "tags",
    "value": "[
  \"acoustic\",
  \"indie\",
  \"relaxing\"
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
