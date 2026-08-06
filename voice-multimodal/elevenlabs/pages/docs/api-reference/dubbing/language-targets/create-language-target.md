---
title: "Create language target"
source: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/create-language-target.md
path: docs/api-reference/dubbing/language-targets/create-language-target
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create language target

POST https://api.elevenlabs.io/v1/dubbing/project/{project_id}/language
Content-Type: application/json

Queue a language target for a project (starts once the project is ready).

Reference: https://elevenlabs.io/docs/api-reference/dubbing/language-targets/create-language-target

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/project/{project_id}/language:
    post:
      operationId: create
      summary: Create Dubbing Language Target
      description: >-
        Queue a language target for a project (starts once the project is
        ready).
      tags:
        - language
      parameters:
        - name: project_id
          in: path
          description: Identifier of the parent dubbing project.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DubbingLanguageResponse'
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
              $ref: >-
                #/components/schemas/Body_Create_Dubbing_Language_Target_v1_dubbing_project__project_id__language_post
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
    VoiceSettings:
      type: object
      properties:
        cloning_strength:
          type: integer
          default: 7
          description: How strongly the dubbed speakers clone the source voices, 0 to 10.
      title: VoiceSettings
    Body_Create_Dubbing_Language_Target_v1_dubbing_project__project_id__language_post:
      type: object
      properties:
        target_language:
          type: string
          description: >-
            BCP-47 language tag to dub the project into (e.g. 'fr', 'es-MX');
            must be a language the dubbing model supports. A region-qualified
            tag must be one of the supported dialects.
        voice_settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettings'
            - type: 'null'
          description: >-
            Voice settings applied to the whole language (e.g. cloning
            strength).
        translations:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
          description: >-
            Optional translations to use instead of machine translation. A map
            from each source segment's external_id (or its id, if you supplied
            none) to the translated text; every source segment must be covered
            exactly once. At most 20000 entries, totalling at most 4 MiB of
            text.
      required:
        - target_language
      title: >-
        Body_Create_Dubbing_Language_Target_v1_dubbing_project__project_id__language_post
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
  "target_language": "es"
}
```

**Response**

```json
{
  "language_id": "lang_1001kwkyxp0je6ktn4knsfrasx5s",
  "project_id": "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
  "target_language": "es",
  "status": "queued",
  "revision": 0,
  "created_at": "2026-07-03T10:16:00Z",
  "updated_at": "2026-07-03T10:16:00Z",
  "model_id": "dubbing_v2",
  "warnings": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.language.create("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", {
        targetLanguage: "es",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.language.create(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    target_language="es",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language"

	payload := strings.NewReader("{\n  \"target_language\": \"es\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"target_language\": \"es\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language")
  .header("Content-Type", "application/json")
  .body("{\n  \"target_language\": \"es\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language', [
  'body' => '{
  "target_language": "es"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"target_language\": \"es\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["target_language": "es"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/language")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
