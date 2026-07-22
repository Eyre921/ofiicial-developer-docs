---
title: "Get Music Finetunes"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/list.md
path: docs/api-reference/music/finetunes/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Music Finetunes

GET https://api.elevenlabs.io/v1/music/finetunes

List music finetunes accessible to you (your own, workspace-shared, and ElevenLabs-curated), with optional filtering, sorting, and cursor pagination.

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/music/finetunes:
    get:
      operationId: list
      summary: Get Music Finetunes
      description: >-
        List music finetunes accessible to you (your own, workspace-shared, and
        ElevenLabs-curated), with optional filtering, sorting, and cursor
        pagination.
      tags:
        - finetunes
      parameters:
        - name: cursor
          in: query
          description: Used for fetching the next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: How many finetunes to return. Max 100, default 50.
          required: false
          schema:
            type: integer
            default: 50
        - name: visibility
          in: query
          description: >-
            Filter by visibility. 'private' returns private finetunes;
            'workspace' returns workspace-shared finetunes; 'public' returns
            public finetunes, which are currently ElevenLabs curated finetunes.
            Omit to return all accessible finetunes.
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/FinetuneVisibility'
              - type: 'null'
        - name: created_by
          in: query
          description: >-
            Filter by creator. 'self' returns finetunes you created; 'workspace'
            returns finetunes created by workspace teammates; 'elevenlabs'
            returns ElevenLabs curated finetunes. Omit to return finetunes from
            all creators.
          required: false
          schema:
            oneOf:
              - $ref: '#/components/schemas/FinetuneCreatedBy'
              - type: 'null'
        - name: sort
          in: query
          description: Sort by field (created_at or name)
          required: false
          schema:
            $ref: '#/components/schemas/V1MusicFinetunesGetParametersSort'
            default: created_at
        - name: sort_direction
          in: query
          description: Sort direction (asc or desc)
          required: false
          schema:
            $ref: '#/components/schemas/V1MusicFinetunesGetParametersSortDirection'
            default: desc
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
                $ref: '#/components/schemas/MusicFinetunePageResponseModel'
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
    V1MusicFinetunesGetParametersSort:
      type: string
      enum:
        - created_at
        - name
      default: created_at
      description: Sort by field (created_at or name)
      title: V1MusicFinetunesGetParametersSort
    V1MusicFinetunesGetParametersSortDirection:
      type: string
      enum:
        - asc
        - desc
      default: desc
      description: Sort direction (asc or desc)
      title: V1MusicFinetunesGetParametersSortDirection
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
    MusicFinetunePageResponseModel:
      type: object
      properties:
        finetunes:
          type: array
          items:
            $ref: '#/components/schemas/MusicFinetuneResponseModel'
          description: The finetunes in this page.
        next_cursor:
          type:
            - string
            - 'null'
          description: >-
            Cursor to pass as `cursor` to fetch the next page; `null` when there
            are no more results.
        has_more:
          type: boolean
          description: Whether more finetunes are available beyond this page.
      required:
        - finetunes
        - next_cursor
        - has_more
      title: MusicFinetunePageResponseModel
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
  "finetunes": [
    {
      "id": "ftn_9a8b7c6d5e4f3a2b1c0d",
      "name": "Chillwave Sunset",
      "tags": [
        "chillwave",
        "electronic",
        "summer vibes"
      ],
      "model_id": "model_12345abcde",
      "created_at": "2024-01-15T09:30:00Z",
      "visibility": "private",
      "created_by": "self",
      "status": "completed",
      "training_progress": 1,
      "primary_genre": "Electronic",
      "failure_reason": null
    }
  ],
  "next_cursor": "cursor_eyJpZCI6IjEyMzQ1NiJ9",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.finetunes.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.finetunes.list()

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

	url := "https://api.elevenlabs.io/v1/music/finetunes"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/music/finetunes")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/music/finetunes")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/music/finetunes', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/finetunes");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/finetunes")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
