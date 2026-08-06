---
title: "List projects"
source: https://elevenlabs.io/docs/api-reference/dubbing/list-projects.md
path: docs/api-reference/dubbing/list-projects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List projects

GET https://api.elevenlabs.io/v1/dubbing/project

List the workspace's dubbing projects (cursor-paginated).

Reference: https://elevenlabs.io/docs/api-reference/dubbing/list-projects

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project:
    get:
      operationId: list
      summary: List Dubbing Projects
      description: List the workspace's dubbing projects (cursor-paginated).
      tags:
        - project
      parameters:
        - name: cursor
          in: query
          description: Pagination cursor from a previous response's next_cursor.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: Number of projects per page (max 100).
          required: false
          schema:
            type: integer
            default: 20
        - name: status
          in: query
          description: Filter to projects in this status (preparing, ready, failed).
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: sort_direction
          in: query
          description: Sort by creation time (default 'DESCENDING').
          required: false
          schema:
            $ref: '#/components/schemas/V1DubbingProjectGetParametersSortDirection'
            default: DESCENDING
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
                $ref: '#/components/schemas/DubbingProjectListResponse'
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
    V1DubbingProjectGetParametersSortDirection:
      type: string
      enum:
        - ASCENDING
        - DESCENDING
      default: DESCENDING
      description: Sort by creation time (default 'DESCENDING').
      title: V1DubbingProjectGetParametersSortDirection
    DubbingProjectResponseStatus:
      type: string
      enum:
        - queued
        - preparing
        - processing
        - ready
        - failed
      description: >-
        Lifecycle status of the project: 'preparing'/'processing' while it
        transcribes, 'ready' once transcription is done, or 'failed'.
      title: DubbingProjectResponseStatus
    DubbingSourceMediaInfo:
      type: object
      properties:
        filename:
          type:
            - string
            - 'null'
          description: >-
            Original filename of the uploaded source media (null for URL
            sources).
        duration_s:
          type:
            - number
            - 'null'
          format: double
          description: Duration of the source media in seconds.
        has_video:
          type:
            - boolean
            - 'null'
          description: Whether the source media contains a video stream.
        mime_type:
          type:
            - string
            - 'null'
          description: MIME type of the uploaded source media.
      description: Metadata about the project's source media.
      title: DubbingSourceMediaInfo
    DubbingError:
      type: object
      properties:
        code:
          type: string
          description: >-
            Stable identifier for the failure, safe to branch on. New codes are
            added over time, so treat an unrecognized value as 'internal_error'.
        message:
          type: string
          description: >-
            Human-readable description of the failure, for display. The wording
            may change at any time; branch on `code` instead.
        retryable:
          type: boolean
          description: >-
            Whether resubmitting the same input could succeed. False means the
            failure describes the input or the account, so an identical retry
            will fail the same way.
      required:
        - code
        - message
        - retryable
      title: DubbingError
    VoicesNotPermittedWarning:
      type: object
      properties:
        type:
          type: string
          enum:
            - voices_not_permitted
          description: Identifies this warning; branch on it to read the fields below.
        speaker_ids:
          type: array
          items:
            type: string
          description: >-
            Speakers whose voices were not permitted for cloning. The dub used a
            replacement voice for each of them; the rest of the speakers are
            unaffected.
        message:
          type: string
          description: >-
            Human-readable description of the warning, for display. The wording
            may change at any time; branch on `type` instead.
      required:
        - type
        - speaker_ids
        - message
      title: VoicesNotPermittedWarning
    DubbingProjectResponse:
      type: object
      properties:
        project_id:
          type: string
          description: Unique identifier of the dubbing project.
        status:
          $ref: '#/components/schemas/DubbingProjectResponseStatus'
          description: >-
            Lifecycle status of the project: 'preparing'/'processing' while it
            transcribes, 'ready' once transcription is done, or 'failed'.
        reference:
          type:
            - string
            - 'null'
          description: >-
            Optional free-form string the customer can provide to identify the
            project on their end.
        source_language:
          type:
            - string
            - 'null'
          description: BCP-47 language tag of the source media (null if auto-detected).
        model_id:
          type:
            - string
            - 'null'
          description: Default dubbing model id applied to this project's language targets.
        media:
          oneOf:
            - $ref: '#/components/schemas/DubbingSourceMediaInfo'
            - type: 'null'
          description: Source media metadata; null until the project is ready.
        language_ids:
          type: array
          items:
            type: string
          default: []
          description: Identifiers of the language targets created under this project.
        webhook_ids:
          type: array
          items:
            type: string
          default: []
          description: >-
            Workspace webhooks notified when this project becomes ready or
            fails, and when any of its languages completes or fails.
        revision:
          type: integer
          description: >-
            Monotonic counter incremented whenever the source transcript is
            edited (segment add/edit/delete).
        error:
          oneOf:
            - $ref: '#/components/schemas/DubbingError'
            - type: 'null'
          description: >-
            Why the project failed; null unless `status` is 'failed'. Also null
            for the few projects that failed before failure reporting was
            introduced.
        warnings:
          type: array
          items:
            $ref: '#/components/schemas/VoicesNotPermittedWarning'
          description: >-
            Non-fatal conditions raised while preparing the source, empty when
            there are none. Reflects the latest preparation. Conditions raised
            while dubbing a particular language are reported on that language
            instead.
        created_at:
          type: string
          format: date-time
          description: When the project was created.
        updated_at:
          type: string
          format: date-time
          description: When the project was last updated.
      required:
        - project_id
        - status
        - revision
        - created_at
        - updated_at
      title: DubbingProjectResponse
    DubbingProjectListResponse:
      type: object
      properties:
        projects:
          type: array
          items:
            $ref: '#/components/schemas/DubbingProjectResponse'
          description: The page of dubbing projects the caller can access.
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for the next page, or null when there are no more results.
      required:
        - projects
      title: DubbingProjectListResponse
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
  "projects": [
    {
      "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
      "status": "ready",
      "revision": 3,
      "created_at": "2026-07-03T10:15:30Z",
      "updated_at": "2026-07-03T10:17:12Z",
      "reference": "Q3 marketing video",
      "source_language": "en",
      "model_id": "dubbing_v2",
      "media": {
        "filename": "promo.mp4",
        "duration_s": 42.5,
        "has_video": true,
        "mime_type": "video/mp4"
      },
      "language_ids": [
        "lang_1001kwkyxp0je6ktn4knsfrasx5s"
      ],
      "webhook_ids": [],
      "warnings": [
        {
          "type": "voices_not_permitted",
          "speaker_ids": [
            "speaker_1"
          ],
          "message": "Voice cloning was not permitted for speaker speaker_1, so a replacement voice was used."
        }
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.list({
        pageSize: 20,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.list(
    page_size=20,
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

	url := "https://api.elevenlabs.io/v1/dubbing/project?page_size=20"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project?page_size=20")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project?page_size=20")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project?page_size=20');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project?page_size=20");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project?page_size=20")! as URL,
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
