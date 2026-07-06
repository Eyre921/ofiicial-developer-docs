---
title: "Translate segment"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/translate-segment.md
path: docs/api-reference/legacy/dubbing/resources/translate-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Translate segment

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/translate
Content-Type: application/json

Regenerate the translations for either the entire resource or the specified segments/languages. Will automatically transcribe missing transcriptions. Will not automatically regenerate the dubs.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/translate-segment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/resource/{dubbing_id}/translate:
    post:
      operationId: translate
      summary: Translate segments
      description: >-
        Regenerate the translations for either the entire resource or the
        specified segments/languages. Will automatically transcribe missing
        transcriptions. Will not automatically regenerate the dubs.
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
                $ref: '#/components/schemas/SegmentTranslationResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Translates_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__translate_post
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
    Body_Translates_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__translate_post:
      type: object
      properties:
        segments:
          type: array
          items:
            type: string
          description: Translate only this list of segments.
        languages:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Translate only these languages for each segment.
      required:
        - segments
        - languages
      title: >-
        Body_Translates_all_or_some_segments_and_languages_v1_dubbing_resource__dubbing_id__translate_post
    SegmentTranslationResponse:
      type: object
      properties:
        version:
          type: integer
      required:
        - version
      title: SegmentTranslationResponse
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
  "segments": [
    "string"
  ],
  "languages": [
    "string"
  ]
}
```

**Response**

```json
{
  "version": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.translate("dubbing_id", {
        segments: [
            "string",
        ],
        languages: [
            "string",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.translate(
    dubbing_id="dubbing_id",
    segments=[
        "string"
    ],
    languages=[
        "string"
    ],
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate"

	payload := strings.NewReader("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate', [
  'body' => '{
  "segments": [
    "string"
  ],
  "languages": [
    "string"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "segments": ["string"],
  "languages": ["string"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")! as URL,
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
