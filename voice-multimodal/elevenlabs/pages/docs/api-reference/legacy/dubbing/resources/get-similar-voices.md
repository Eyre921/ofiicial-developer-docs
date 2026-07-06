---
title: "Get similar voices"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/get-similar-voices.md
path: docs/api-reference/legacy/dubbing/resources/get-similar-voices
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get similar voices

GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices

Fetch the top 10 similar voices to a speaker, including the voice IDs, names, descriptions, and, where possible, a sample audio recording.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/get-similar-voices

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices:
    get:
      operationId: find_similar_voices
      summary: Search The Elevenlabs Library For Voices Similar To A Speaker.
      description: >-
        Fetch the top 10 similar voices to a speaker, including the voice IDs,
        names, descriptions, and, where possible, a sample audio recording.
      tags:
        - speaker
      parameters:
        - name: dubbing_id
          in: path
          description: ID of the dubbing project.
          required: true
          schema:
            type: string
        - name: speaker_id
          in: path
          description: ID of the speaker.
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
                $ref: '#/components/schemas/SimilarVoicesForSpeakerResponse'
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
    VOICE_CATEGORY:
      type: string
      enum:
        - premade
        - cloned
        - generated
        - professional
        - famous
      title: VOICE_CATEGORY
    SimilarVoice:
      type: object
      properties:
        voice_id:
          type: string
        name:
          type: string
        category:
          $ref: '#/components/schemas/VOICE_CATEGORY'
        description:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
      required:
        - voice_id
        - name
        - category
      title: SimilarVoice
    SimilarVoicesForSpeakerResponse:
      type: object
      properties:
        voices:
          type: array
          items:
            $ref: '#/components/schemas/SimilarVoice'
      required:
        - voices
      title: SimilarVoicesForSpeakerResponse
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
  "voices": [
    {
      "voice_id": "string",
      "name": "string",
      "category": "premade",
      "description": "string",
      "preview_url": "string"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.speaker.findSimilarVoices("dubbing_id", "speaker_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.speaker.find_similar_voices(
    dubbing_id="dubbing_id",
    speaker_id="speaker_id",
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker/speaker_id/similar-voices")! as URL,
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
