---
title: "Regenerate target"
source: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/regenerate-target.md
path: docs/api-reference/dubbing/target-transcript/regenerate-target
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Regenerate target

POST https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language/{language_id}/transcript/regenerate

Enterprise only. Re-dub a target from its edited transcript, re-synthesizing only the edited regions (charged like a generation). Conflicts when the target has no edits to apply -- nothing is dispatched and nothing is charged.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/target-transcript/regenerate-target

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/language/{language_id}/transcript/regenerate:
    post:
      operationId: regenerate
      summary: Regenerate Dubbing Target
      description: >-
        Enterprise only. Re-dub a target from its edited transcript,
        re-synthesizing only the edited regions (charged like a generation).
        Conflicts when the target has no edits to apply -- nothing is dispatched
        and nothing is charged.
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
        '202':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DubbingRegenerateResponse'
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
    DubbingRegenerateResponse:
      type: object
      properties:
        regenerated_segment_ids:
          type: array
          items:
            type: string
          description: 'The segments this re-dub re-synthesizes: those with edits to apply.'
        regenerated_seconds:
          type: number
          format: double
          description: >-
            Seconds of audio this re-dub covers -- the edited regions only,
            never the whole target. `charged_seconds` is the part of it that was
            billed.
        charged_seconds:
          type: number
          format: double
          description: >-
            Seconds actually billed, after the free-regeneration allowance. Zero
            when the re-dub cost nothing -- the allowance covered all of it, or
            the project's included generation did.
        free_regeneration_seconds_remaining:
          type: number
          format: double
          description: >-
            Free-regeneration seconds left for this language target after this
            re-dub. The allowance is the source's own duration.
      required:
        - regenerated_segment_ids
        - regenerated_seconds
        - charged_seconds
        - free_regeneration_seconds_remaining
      description: 'The accepted re-dub: what it covers and what it cost.'
      title: DubbingRegenerateResponse
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
  "regenerated_segment_ids": [
    "0199a3f0-1c2d-7abc-8def-0123456789ab",
    "0199a3f0-3e4f-7abc-8def-0123456789cd"
  ],
  "regenerated_seconds": 4,
  "charged_seconds": 0,
  "free_regeneration_seconds_remaining": 38
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.transcript.regenerate("lang_1001kwkyxp0je6ktn4knsfrasx5s", "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.transcript.regenerate(
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language/lang_1001kwkyxp0je6ktn4knsfrasx5s/transcript/regenerate")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
