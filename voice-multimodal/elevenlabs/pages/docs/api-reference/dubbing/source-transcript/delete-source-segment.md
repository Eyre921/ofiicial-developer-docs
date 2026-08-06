---
title: "Delete source segment"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/delete-source-segment.md
path: docs/api-reference/dubbing/source-transcript/delete-source-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete source segment

DELETE https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segment/{segment_id}

Enterprise only. Remove a source segment from the transcript.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/delete-source-segment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/transcript/segment/{segment_id}:
    delete:
      operationId: delete_segment
      summary: Delete Dubbing Transcript Segment
      description: Enterprise only. Remove a source segment from the transcript.
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
          description: Identifier of the segment to remove.
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
                $ref: '#/components/schemas/DubbingTranscriptRevisionResponse'
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
    DubbingTranscriptRevisionResponse:
      type: object
      properties:
        revision:
          type: integer
          description: The project's source-transcript revision after this edit.
      required:
        - revision
      description: >-
        The new revision after a source edit that returns no segment (e.g. a
        delete).
      title: DubbingTranscriptRevisionResponse
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
  "revision": 6
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.transcript.deleteSegment("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "0199a3f0-1c2d-7abc-8def-0123456789ab");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.transcript.delete_segment(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab"

	req, _ := http.NewRequest("DELETE", url, nil)

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

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

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
