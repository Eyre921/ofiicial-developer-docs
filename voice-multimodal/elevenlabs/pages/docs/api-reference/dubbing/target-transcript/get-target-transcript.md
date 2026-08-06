---
title: "Get target transcript"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/get-target-transcript.md
path: docs/api-reference/dubbing/target-transcript/get-target-transcript
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get target transcript

GET https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript

A language target's transcript: source segments with their translations.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/get-target-transcript

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/language/{language_id}/transcript:
    get:
      operationId: get
      summary: Get Dubbing Target Transcript
      description: 'A language target''s transcript: source segments with their translations.'
      tags:
        - transcript
      parameters:
        - name: project_id
          in: path
          description: Identifier of the dubbing project.
          required: true
          schema:
            type: string
        - name: language_id
          in: path
          description: Identifier of the language target.
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
                $ref: '#/components/schemas/DubbingTargetTranscriptResponse'
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
    DubbingTargetTranscriptSegment:
      type: object
      properties:
        id:
          type: string
          description: Stable identifier of the segment (from the source).
        speaker_id:
          type: string
          description: Identifier of the segment's speaker.
        start_s:
          type: number
          format: double
          description: Start time of the segment, in seconds.
        end_s:
          type: number
          format: double
          description: End time of the segment, in seconds.
        source_text:
          type: string
          description: The source-language text of the segment.
        translation:
          type:
            - string
            - 'null'
          description: >-
            The translated text, or null if not translated yet (needs
            translation).
      required:
        - id
        - speaker_id
        - start_s
        - end_s
        - source_text
      description: >-
        One segment of a target transcript: a source segment plus its
        translation.
      title: DubbingTargetTranscriptSegment
    DubbingTargetTranscriptResponse:
      type: object
      properties:
        source_language:
          type:
            - string
            - 'null'
          description: BCP-47 language tag of the source transcript.
        target_language:
          type: string
          description: BCP-47 language tag this target is translated into.
        segments:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTargetTranscriptSegment'
          description: The target segments, in playback order.
        revision:
          type: integer
          description: The target's revision at read time.
      required:
        - target_language
        - segments
        - revision
      title: DubbingTargetTranscriptResponse
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
  "target_language": "es",
  "segments": [
    {
      "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
      "speaker_id": "default_speaker",
      "start_s": 0,
      "end_s": 2.5,
      "source_text": "Welcome to our product demo.",
      "translation": "Bienvenido a la demostración de nuestro producto."
    }
  ],
  "revision": 3,
  "source_language": "en"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.get("lang_1001kwkyxp0je6ktn4knsfrasx5s", "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.transcript.get(
    language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript")! as URL,
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
