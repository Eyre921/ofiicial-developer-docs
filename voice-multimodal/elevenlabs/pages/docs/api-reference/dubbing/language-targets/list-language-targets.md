---
title: "List language targets"
source: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/list-language-targets.md
path: docs/api-reference/dubbing/language-targets/list-language-targets
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List language targets

GET https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language

List a project's language targets (cursor-paginated).

Reference: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/list-language-targets

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/language:
    get:
      operationId: list
      summary: List Dubbing Language Targets
      description: List a project's language targets (cursor-paginated).
      tags:
        - language
      parameters:
        - name: project_id
          in: path
          description: Identifier of the parent dubbing project.
          required: true
          schema:
            type: string
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
          description: Number of language targets per page (max 100).
          required: false
          schema:
            type: integer
            default: 20
        - name: status
          in: query
          description: >-
            Filter to targets in this status (queued, processing, completed,
            stale, failed).
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/DubbingLanguageListResponse'
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
    DubbingLanguageResponseStatus:
      type: string
      enum:
        - queued
        - processing
        - completed
        - stale
        - failed
      description: >-
        Lifecycle status: 'queued' (waiting on the project), 'processing',
        'completed', 'stale' (source/transcript changed), or 'failed'.
      title: DubbingLanguageResponseStatus
    VoiceSettings:
      type: object
      properties:
        cloning_strength:
          type: integer
          default: 7
          description: How strongly the dubbed speakers clone the source voices, 0 to 10.
      title: VoiceSettings
    DubbingLanguageOutputs:
      type: object
      properties:
        lossless_audio:
          type:
            - string
            - 'null'
          description: Signed URL of the dubbed lossless audio track.
      description: Signed, time-limited download URLs for a language target's outputs.
      title: DubbingLanguageOutputs
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
    DubbingLanguageResponse:
      type: object
      properties:
        language_id:
          type: string
          description: Unique identifier of the language target.
        project_id:
          type: string
          description: Identifier of the parent dubbing project.
        target_language:
          type: string
          description: BCP-47 language tag this target is dubbed into.
        status:
          $ref: '#/components/schemas/DubbingLanguageResponseStatus'
          description: >-
            Lifecycle status: 'queued' (waiting on the project), 'processing',
            'completed', 'stale' (source/transcript changed), or 'failed'.
        model_id:
          type:
            - string
            - 'null'
          description: Effective dubbing model id (target override or project default).
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettings'
            - type: 'null'
          description: Voice settings applied to the whole language, or null if unset.
        outputs:
          oneOf:
            - $ref: '#/components/schemas/DubbingLanguageOutputs'
            - type: 'null'
          description: >-
            Signed output URLs; null until the target has produced an output
            (present once 'completed', and kept while 'stale' -- compare
            `output_revision` against `revision` to tell whether the output is
            up to date).
        revision:
          type: integer
          description: >-
            Monotonic counter incremented whenever this target's transcript
            changes (a source edit affecting it, or an edit to its translation).
        output_revision:
          type:
            - integer
            - 'null'
          description: >-
            The `revision` the current dubbed output was generated from; equal
            to `revision` when up to date, less than it when 'stale'. Null until
            a generation has completed.
        error:
          oneOf:
            - $ref: '#/components/schemas/DubbingError'
            - type: 'null'
          description: >-
            Why this language failed; null unless `status` is 'failed', and also
            null for the few languages that failed before failure reporting was
            introduced. A code of 'project_failed' means the parent project
            failed, so read the project for the underlying cause.
        warnings:
          type: array
          items:
            $ref: '#/components/schemas/VoicesNotPermittedWarning'
          description: >-
            Non-fatal conditions raised while dubbing this language, empty when
            there are none. Reflects the latest generation. Conditions raised
            while preparing the source are reported on the project instead.
        created_at:
          type: string
          format: date-time
          description: When the language target was created.
        updated_at:
          type: string
          format: date-time
          description: When the language target was last updated.
      required:
        - language_id
        - project_id
        - target_language
        - status
        - revision
        - created_at
        - updated_at
      title: DubbingLanguageResponse
    DubbingLanguageListResponse:
      type: object
      properties:
        languages:
          type: array
          items:
            $ref: '#/components/schemas/DubbingLanguageResponse'
          description: The page of language targets for the project.
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for the next page, or null when there are no more results.
      required:
        - languages
      title: DubbingLanguageListResponse
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
  "languages": [
    {
      "language_id": "lang_1001kwkyxp0je6ktn4knsfrasx5s",
      "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
      "target_language": "es",
      "status": "completed",
      "revision": 3,
      "created_at": "2026-07-03T10:16:00Z",
      "updated_at": "2026-07-03T10:20:45Z",
      "model_id": "dubbing_v2",
      "outputs": {
        "lossless_audio": "https://storage.googleapis.com/eleven-dubbing/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/lang_1001kwkyxp0je6ktn4knsfrasx5s/output.flac?X-Goog-Signature=..."
      },
      "output_revision": 3,
      "warnings": []
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.list("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        pageSize: 20,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.list(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language?page_size=20")! as URL,
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
