---
title: "Delete Music Finetune"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/delete.md
path: docs/api-reference/music/finetunes/delete
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete Music Finetune

DELETE https://api.elevenlabs.io/v1/music/finetunes/{finetune_id}

Delete a music finetune

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/finetunes/{finetune_id}:
    delete:
      operationId: delete
      summary: Delete Music Finetune
      description: Delete a music finetune
      tags:
        - finetunes
      parameters:
        - name: finetune_id
          in: path
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
                $ref: '#/components/schemas/MusicFinetuneResponseModel'
        '403':
          description: Missing permissions to manage music finetunes.
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Finetune not found.
          content:
            application/json:
              schema:
                description: Any type
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
    FinetuneVisibility:
      type: string
      enum:
        - private
        - workspace
        - public
      title: FinetuneVisibility
    FinetuneCreatedBy:
      type: string
      enum:
        - self
        - workspace
        - elevenlabs
      title: FinetuneCreatedBy
    MusicFinetuneStatus:
      type: string
      enum:
        - pending
        - in_progress
        - completed
        - failed
        - blocked
      title: MusicFinetuneStatus
    MusicFinetuneFailureReason:
      type: string
      enum:
        - audio_processing_failed
        - copyright_violation
        - training_failed
      title: MusicFinetuneFailureReason
    MusicFinetuneResponseModel:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the finetune.
        name:
          type: string
          description: Name of the finetune.
        tags:
          type: array
          items:
            type: string
          description: Tags associated with the finetune.
        primary_genre:
          type:
            - string
            - 'null'
          description: Primary musical genre of the finetune.
        model_id:
          type: string
          description: The base music model the finetune was trained on.
        created_at:
          type: string
          format: date-time
          description: When the finetune was created (UTC).
        visibility:
          $ref: '#/components/schemas/FinetuneVisibility'
          description: >-
            Who can access this finetune: `private` (only you), `workspace`
            (members of your workspace), `public` (ElevenLabs-curated, available
            to everyone).
        created_by:
          $ref: '#/components/schemas/FinetuneCreatedBy'
          description: 'Who created the finetune: `self`, `workspace`, or `elevenlabs`.'
        status:
          $ref: '#/components/schemas/MusicFinetuneStatus'
          description: >-
            Training lifecycle status: pending, in_progress, completed, failed,
            and blocked.
        training_progress:
          type: number
          format: double
          description: Training progress from 0.0 to 1.0.
        failure_reason:
          oneOf:
            - $ref: '#/components/schemas/MusicFinetuneFailureReason'
            - type: 'null'
          description: Reason the finetune failed or was blocked, if applicable.
      required:
        - id
        - name
        - tags
        - model_id
        - created_at
        - visibility
        - created_by
        - status
        - training_progress
      title: MusicFinetuneResponseModel
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
{}
```

**Response**

```json
{
  "id": "ftn_9a8b7c6d5e4f3g2h1i0j",
  "name": "Chillwave Sunset",
  "tags": [
    "chillwave",
    "synth",
    "ambient"
  ],
  "model_id": "mdl_12345abcde67890fghij",
  "created_at": "2024-01-15T09:30:00Z",
  "visibility": "private",
  "created_by": "self",
  "status": "completed",
  "training_progress": 1,
  "primary_genre": "electronic",
  "failure_reason": null
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.finetunes.delete("finetune_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.finetunes.delete(
    finetune_id="finetune_id",
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

	url := "https://api.elevenlabs.io/v1/music/finetunes/finetune_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes/finetune_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/music/finetunes/finetune_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/music/finetunes/finetune_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/finetunes/finetune_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/finetunes/finetune_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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
