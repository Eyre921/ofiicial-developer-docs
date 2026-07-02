---
title: "Get Project Snapshot"
source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot.md
path: docs/api-reference/studio/get-project-snapshot
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Project Snapshot

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}

Returns the project snapshot.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}:
    get:
      operationId: get
      summary: Get Project Snapshot
      description: Returns the project snapshot.
      tags:
        - subpackage_studio/projects/snapshots
      parameters:
        - name: project_id
          in: path
          description: The ID of the Studio project.
          required: true
          schema:
            type: string
        - name: project_snapshot_id
          in: path
          description: The ID of the Studio project snapshot.
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
                $ref: '#/components/schemas/ProjectSnapshotExtendedResponseModel'
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
    CharacterAlignmentModel:
      type: object
      properties:
        characters:
          type: array
          items:
            type: string
        character_start_times_seconds:
          type: array
          items:
            type: number
            format: double
        character_end_times_seconds:
          type: array
          items:
            type: number
            format: double
      required:
        - characters
        - character_start_times_seconds
        - character_end_times_seconds
      title: CharacterAlignmentModel
    ProjectSnapshotExtendedResponseModel:
      type: object
      properties:
        project_snapshot_id:
          type: string
          description: The ID of the project snapshot.
        project_id:
          type: string
          description: The ID of the project.
        created_at_unix:
          type: integer
          description: The creation date of the project snapshot.
        name:
          type: string
          description: The name of the project snapshot.
        audio_upload:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: (Deprecated)
        zip_upload:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: (Deprecated)
        character_alignments:
          type: array
          items:
            $ref: '#/components/schemas/CharacterAlignmentModel'
        audio_duration_secs:
          type: number
          format: double
          description: The total duration of the audio in seconds.
      required:
        - project_snapshot_id
        - project_id
        - created_at_unix
        - name
        - character_alignments
        - audio_duration_secs
      title: ProjectSnapshotExtendedResponseModel
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
  "project_snapshot_id": "aw1NgEzBg83R7vgmiJt6",
  "project_id": "aw1NgEzBg83R7vgmiJt6",
  "created_at_unix": 1714204800,
  "name": "My Project Snapshot",
  "character_alignments": [],
  "audio_duration_secs": 123.45
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.snapshots.get("project_id", "project_snapshot_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.snapshots.get(
    project_id="project_id",
    project_snapshot_id="project_snapshot_id",
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")! as URL,
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
