---
title: "Render project"
source: https://elevenlabs.io/docs/api-reference/dubbing/resources/render-project.md
path: docs/api-reference/dubbing/resources/render-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Render project

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/render/{language}
Content-Type: application/json

Regenerate the output media for a language using the latest Studio state. Please ensure all segments have been dubbed before rendering, otherwise they will be omitted. Renders are generated asynchronously, and to check the status of all renders please use the 'Get Dubbing Resource' endpoint.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/resources/render-project

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/resource/{dubbing_id}/render/{language}:
    post:
      operationId: render
      summary: Render Audio Or Video For The Given Language
      description: >-
        Regenerate the output media for a language using the latest Studio
        state. Please ensure all segments have been dubbed before rendering,
        otherwise they will be omitted. Renders are generated asynchronously,
        and to check the status of all renders please use the 'Get Dubbing
        Resource' endpoint.
      tags:
        - subpackage_dubbing/resource
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: language
          in: path
          description: >-
            The target language code to render, eg. 'es'. To render the source
            track use 'original'.
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
                $ref: '#/components/schemas/DubbingRenderResponseModel'
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
                #/components/schemas/Body_Render_audio_or_video_for_the_given_language_v1_dubbing_resource__dubbing_id__render__language__post
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
    Body_Render_audio_or_video_for_the_given_language_v1_dubbing_resource__dubbing_id__render__language__post:
      type: object
      properties:
        render_type:
          $ref: '#/components/schemas/RenderType'
          description: >-
            The type of the render. One of ['mp4', 'aac', 'mp3', 'wav', 'aaf',
            'tracks_zip', 'clips_zip']
        normalize_volume:
          type:
            - boolean
            - 'null'
          default: false
          description: Whether to normalize the volume of the rendered audio.
      required:
        - render_type
      title: >-
        Body_Render_audio_or_video_for_the_given_language_v1_dubbing_resource__dubbing_id__render__language__post
    DubbingRenderResponseModel:
      type: object
      properties:
        version:
          type: integer
        render_id:
          type: string
      required:
        - version
        - render_id
      title: DubbingRenderResponseModel
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
  "render_type": "mp4"
}
```

**Response**

```json
{
  "version": 1,
  "render_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.render("dubbing_id", "language", {
        renderType: "mp4",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.render(
    dubbing_id="dubbing_id",
    language="language",
    render_type="mp4",
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language"

	payload := strings.NewReader("{\n  \"render_type\": \"mp4\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"render_type\": \"mp4\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")
  .header("Content-Type", "application/json")
  .body("{\n  \"render_type\": \"mp4\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language', [
  'body' => '{
  "render_type": "mp4"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"render_type\": \"mp4\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["render_type": "mp4"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/render/language")! as URL,
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
