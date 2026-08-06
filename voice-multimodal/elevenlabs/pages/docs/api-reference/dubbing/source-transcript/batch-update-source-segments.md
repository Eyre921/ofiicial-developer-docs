---
title: "Batch update source segments"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/batch-update-source-segments.md
path: docs/api-reference/dubbing/source-transcript/batch-update-source-segments
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Batch update source segments

PATCH https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segments
Content-Type: application/json

Enterprise only. Edit several source segments' text, speaker, or timing in one atomic request.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/batch-update-source-segments

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/transcript/segments:
    patch:
      operationId: update_segments
      summary: Update Dubbing Transcript Segments
      description: >-
        Enterprise only. Edit several source segments' text, speaker, or timing
        in one atomic request.
      tags:
        - transcript
      parameters:
        - name: project_id
          in: path
          description: Identifier of the dubbing project.
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
                $ref: '#/components/schemas/DubbingBulkSourceSegmentUpdateResponse'
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
              $ref: '#/components/schemas/DubbingBulkSegmentUpdateRequest'
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
    DubbingSegmentUpdateRequest:
      type: object
      properties:
        text:
          type:
            - string
            - 'null'
          description: New text for the segment.
        speaker_id:
          type:
            - string
            - 'null'
          description: New speaker id for the segment.
        start_s:
          type:
            - number
            - 'null'
          format: double
          description: New start time, in seconds.
        end_s:
          type:
            - number
            - 'null'
          format: double
          description: New end time, in seconds.
      description: A partial update to a source segment; omitted fields are left unchanged.
      title: DubbingSegmentUpdateRequest
    DubbingBulkSegmentUpdateRequest:
      type: object
      properties:
        segments:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DubbingSegmentUpdateRequest'
          description: Map of segment id to the partial update to apply to that segment.
      required:
        - segments
      description: >-
        Edit several source segments at once, applied atomically (all succeed or
        none do).
      title: DubbingBulkSegmentUpdateRequest
    DubbingTranscriptSegment:
      type: object
      properties:
        id:
          type: string
          description: Stable identifier of the segment.
        text:
          type: string
          description: The transcribed text of the segment.
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
        external_id:
          type:
            - string
            - 'null'
          description: >-
            The caller-supplied external id for this segment, if one was
            provided.
      required:
        - id
        - text
        - speaker_id
        - start_s
        - end_s
      description: One segment of a source transcript.
      title: DubbingTranscriptSegment
    DubbingBulkSourceSegmentUpdateResponse:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/DubbingTranscriptSegment'
          description: The edited segments in their updated state.
        revision:
          type: integer
          description: The project's source-transcript revision after the edits.
      required:
        - segments
        - revision
      description: >-
        The result of a bulk source edit: the updated segments and the new
        revision.
      title: DubbingBulkSourceSegmentUpdateResponse
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
      "text": "Welcome to our latest product demo."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "speaker_id": "narrator"
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
      "text": "Welcome to our latest product demo.",
      "speaker_id": "default_speaker",
      "start_s": 0,
      "end_s": 2.5
    },
    {
      "id": "0199a3f0-3e4f-7abc-8def-0123456789cd",
      "text": "Let's get started.",
      "speaker_id": "narrator",
      "start_s": 2.5,
      "end_s": 4
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
    await client.dubbing.project.transcript.updateSegments("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        segments: {
            "0199a3f0-1c2d-7abc-8def-0123456789ab": {
                text: "Welcome to our latest product demo.",
            },
            "0199a3f0-3e4f-7abc-8def-0123456789cd": {
                speakerId: "narrator",
            },
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DubbingSegmentUpdateRequest

client = ElevenLabs()

client.dubbing.project.transcript.update_segments(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segments={
        "0199a3f0-1c2d-7abc-8def-0123456789ab": DubbingSegmentUpdateRequest(
            text="Welcome to our latest product demo.",
        ),
        "0199a3f0-3e4f-7abc-8def-0123456789cd": DubbingSegmentUpdateRequest(
            speaker_id="narrator",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments"

	payload := strings.NewReader("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"text\": \"Welcome to our latest product demo.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"speaker_id\": \"narrator\"\n    }\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"text\": \"Welcome to our latest product demo.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"speaker_id\": \"narrator\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"text\": \"Welcome to our latest product demo.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"speaker_id\": \"narrator\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments', [
  'body' => '{
  "segments": {
    "0199a3f0-1c2d-7abc-8def-0123456789ab": {
      "text": "Welcome to our latest product demo."
    },
    "0199a3f0-3e4f-7abc-8def-0123456789cd": {
      "speaker_id": "narrator"
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

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": {\n    \"0199a3f0-1c2d-7abc-8def-0123456789ab\": {\n      \"text\": \"Welcome to our latest product demo.\"\n    },\n    \"0199a3f0-3e4f-7abc-8def-0123456789cd\": {\n      \"speaker_id\": \"narrator\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["segments": [
    "0199a3f0-1c2d-7abc-8def-0123456789ab": ["text": "Welcome to our latest product demo."],
    "0199a3f0-3e4f-7abc-8def-0123456789cd": ["speaker_id": "narrator"]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segments")! as URL,
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
