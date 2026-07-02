---
title: "Get dubbing"
source: https://elevenlabs.io/docs/api-reference/dubbing/get.md
path: docs/api-reference/dubbing/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dubbing

GET https://api.elevenlabs.io/v1/dubbing/{dubbing_id}

Returns metadata about a dubbing project, including whether it's still in progress or not

Reference: https://elevenlabs.io/docs/api-reference/dubbing/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/{dubbing_id}:
    get:
      operationId: get
      summary: Get dubbing
      description: >-
        Returns metadata about a dubbing project, including whether it's still
        in progress or not
      tags:
        - subpackage_dubbing
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
                $ref: '#/components/schemas/DubbingMetadataResponse'
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
    DubbingMediaMetadata:
      type: object
      properties:
        content_type:
          type: string
          description: The content type of the media.
        duration:
          type: number
          format: double
          description: The duration of the media in seconds.
      required:
        - content_type
        - duration
      title: DubbingMediaMetadata
    DubbingMetadataResponse:
      type: object
      properties:
        dubbing_id:
          type: string
          description: The ID of the dubbing project.
        name:
          type: string
          description: The name of the dubbing project.
        status:
          type: string
          description: The state this dub is in.
        source_language:
          type:
            - string
            - 'null'
          description: >-
            Once dubbing has completed, the ISO-639-1 code of the original
            media's source language.
        target_languages:
          type: array
          items:
            type: string
          description: The ISO-639-1 code of the languages this media has been dubbed into.
        editable:
          type: boolean
          default: false
          description: Whether this dubbing project is editable in Dubbing Studio.
        created_at:
          type: string
          format: date-time
          description: Timestamp this dub was created.
        media_metadata:
          oneOf:
            - $ref: '#/components/schemas/DubbingMediaMetadata'
            - type: 'null'
          description: >-
            Metadata, such as the length in seconds and content type, of the
            dubbed content.
        error:
          type:
            - string
            - 'null'
          description: Error message indicate, if this dub has failed, what happened.
      required:
        - dubbing_id
        - name
        - status
        - source_language
        - target_languages
        - created_at
      title: DubbingMetadataResponse
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
  "dubbing_id": "21m00Tcm4TlvDq8ikWAM",
  "name": "My Dubbing Project",
  "status": "dubbed",
  "source_language": "en",
  "target_languages": [
    "es",
    "fr",
    "de"
  ],
  "created_at": "2025-07-15T14:49:41.149000",
  "editable": true,
  "media_metadata": {
    "content_type": "video/mp4",
    "duration": 127.5
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.get("dubbing_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.get(
    dubbing_id="dubbing_id",
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

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id")! as URL,
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
