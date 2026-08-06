---
title: "Batch update target segments"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/batch-update-target-segments.md
path: docs/api-reference/dubbing/target-transcript/batch-update-target-segments
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Batch update target segments

PATCH https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript/segments
Content-Type: application/json

Enterprise only. Edit several segments' translations for a language target in one atomic request.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/batch-update-target-segments

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/language/{language_id}/transcript/segments:
    patch:
      operationId: update_segments
      summary: Update Dubbing Target Transcript Segments
      description: >-
        Enterprise only. Edit several segments' translations for a language
        target in one atomic request.
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
                $ref: '#/components/schemas/DubbingBulkTargetSegmentUpdateResponse'
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
              $ref: '#/components/schemas/DubbingBulkTargetSegmentUpdateRequest'
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
    DubbingTargetSegmentUpdateRequest:
      type: object
      properties:
        translation:
          type:
            - string
            - 'null'
          description: New translated text, or null to mark the segment for re-translation.
      description: >-
        A partial edit to a target segment. An omitted field is left unchanged;
        a provided ``null``

        clears it (see each field for what clearing means).
      title: DubbingTargetSegmentUpdateRequest
    DubbingBulkTargetSegmentUpdateRequest:
      type: object
      properties:
        segments:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DubbingTargetSegmentUpdateRequest'
          description: Map of segment id to the translation edit to apply to that segment.
      required:
        - segments
      description: >-
        Edit several target translations at once, applied atomically (all
        succeed or none do).
      title: DubbingBulkTargetSegmentUpdateRequest
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
    DubbingBulkTargetSegmentUpdateResponse:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTargetTranscriptSegment'
          description: The edited target segments in their updated state.
        revision:
          type: integer
          description: The target's revision after the edits.
      required:
        - segments
        - revision
      description: >-
        The result of a bulk target edit: the updated segments and the new
        revision.
      title: DubbingBulkTargetSegmentUpdateResponse
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
  "segments": {
    "0199a3f0-1c2d-7abc-8def-0123456789ab": {
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "translation": "Empecemos."
    }
  }
}
```

**Response**

```json
{
  "segments": [
    {
      "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
      "speaker_id": "default_speaker",
      "start_s": 0,
      "end_s": 2.5,
      "source_text": "Welcome to our product demo.",
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    {
      "id": "0199a3f0-3e4f-7abc-8def-0123456789cd",
      "speaker_id": "narrator",
      "start_s": 2.5,
      "end_s": 4,
      "source_text": "Let's get started.",
      "translation": "Empecemos."
    }
  ],
  "revision": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.updateSegments("lang_1001kwkyxp0je6ktn4knsfrasx5s", "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        segments: {
            "0199a3f0-1c2d-7abc-8def-0123456789ab": {
                translation: "Bienvenido a nuestra última demostración de producto.",
            },
            "0199a3f0-3e4f-7abc-8def-0123456789cd": {
                translation: "Empecemos.",
            },
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DubbingTargetSegmentUpdateRequest

client = ElevenLabs()

client.dubbing.project.language.transcript.update_segments(
    language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segments={
        "0199a3f0-1c2d-7abc-8def-0123456789ab": DubbingTargetSegmentUpdateRequest(
            translation="Bienvenido a nuestra última demostración de producto.",
        ),
        "0199a3f0-3e4f-7abc-8def-0123456789cd": DubbingTargetSegmentUpdateRequest(
            translation="Empecemos.",
        )
    },
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments"

	payload := strings.NewReader("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments', [
  'body' => '{
  "segments": {
    "0199a3f0-1c2d-7abc-8def-0123456789ab": {
      "translation": "Bienvenido a nuestra última demostración de producto."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "translation": "Empecemos."
    }
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"translation\": \"Bienvenido a nuestra última demostración de producto.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"translation\": \"Empecemos.\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["segments": [
    "0199a3f0-1c2d-7abc-8def-0123456789ab": ["translation": "Bienvenido a nuestra última demostración de producto."],
    "0199a3f0-3e4f-7abc-8def-0123456789cd": ["translation": "Empecemos."]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/segments")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
