---
title: "Update source segment"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/update-source-segment.md
path: docs/api-reference/dubbing/source-transcript/update-source-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update source segment

PATCH https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segment/{segment_id}
Content-Type: application/json

Enterprise only. Edit a source segment's text, speaker, or timing.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/update-source-segment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/transcript/segment/{segment_id}:
    patch:
      operationId: update_segment
      summary: Update Dubbing Transcript Segment
      description: Enterprise only. Edit a source segment's text, speaker, or timing.
      tags:
        - transcript
      parameters:
        - name: project_id
          in: path
          description: Identifier of the dubbing project.
          required: true
          schema:
            type: string
        - name: segment_id
          in: path
          description: Identifier of the segment to edit.
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
                $ref: '#/components/schemas/DubbingSourceSegmentUpdateResponse'
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
              $ref: '#/components/schemas/DubbingSegmentUpdateRequest'
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
    DubbingSourceSegmentUpdateResponse:
      type: object
      properties:
        segment:
          $ref: '#/components/schemas/DubbingTranscriptSegment'
          description: The segment in its updated state.
        revision:
          type: integer
          description: The project's source-transcript revision after this edit.
      required:
        - segment
        - revision
      description: >-
        The result of a source-segment add or edit: the segment and the new
        revision.
      title: DubbingSourceSegmentUpdateResponse
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
  "text": "Welcome to our latest product demo."
}
```

**Response**

```json
{
  "segment": {
    "id": "0199a3f0-1c2d-7abc-8def-0123456789ab",
    "text": "Welcome to our latest product demo.",
    "speaker_id": "default_speaker",
    "start_s": 0,
    "end_s": 2.5
  },
  "revision": 4
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.transcript.updateSegment("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "0199a3f0-1c2d-7abc-8def-0123456789ab", {
        text: "Welcome to our latest product demo.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, DubbingSegmentUpdateRequest

client = ElevenLabs()

client.dubbing.project.transcript.update_segment(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
    request=DubbingSegmentUpdateRequest(
        text="Welcome to our latest product demo.",
    ),
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab"

	payload := strings.NewReader("{\n  \"text\": \"Welcome to our latest product demo.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Welcome to our latest product demo.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Welcome to our latest product demo.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab', [
  'body' => '{
  "text": "Welcome to our latest product demo."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Welcome to our latest product demo.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["text": "Welcome to our latest product demo."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")! as URL,
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
