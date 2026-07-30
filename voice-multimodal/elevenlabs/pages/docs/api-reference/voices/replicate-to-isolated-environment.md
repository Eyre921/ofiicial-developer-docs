---
title: "Replicate Voice To Isolated Environment"
source: https://elevenlabs.io/docs/api-reference/voices/replicate-to-isolated-environment.md
path: docs/api-reference/voices/replicate-to-isolated-environment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Replicate Voice To Isolated Environment

POST https://api.elevenlabs.io/v1/voices/{voice_id}/replicate-to-isolated-environment
Content-Type: application/json

Replicates an Instant Voice Clone or Voice Design voice to a workspace in a different data residency. The target workspace must belong to the same consolidated billing group. The user must have VOICES_WRITE in the source workspace, and be an admin on the source voice. Human users (i.e. not service accounts) must also have VOICES_WRITE in the target workspace. This endpoint is available on the central environment only.

Reference: https://elevenlabs.io/docs/api-reference/voices/replicate-to-isolated-environment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/voices/{voice_id}/replicate-to-isolated-environment:
    post:
      operationId: replicate_to_isolated_environment
      summary: Replicate Voice To Isolated Environment
      description: >-
        Replicates an Instant Voice Clone or Voice Design voice to a workspace
        in a different data residency. The target workspace must belong to the
        same consolidated billing group. The user must have VOICES_WRITE in the
        source workspace, and be an admin on the source voice. Human users (i.e.
        not service accounts) must also have VOICES_WRITE in the target
        workspace. This endpoint is available on the central environment only.
      tags:
        - voices
      parameters:
        - name: voice_id
          in: path
          description: >-
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices
            to list all the available voices.
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
                $ref: >-
                  #/components/schemas/ReplicateVoiceToIsolatedEnvironmentResponseModel
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
                #/components/schemas/ReplicateVoiceToIsolatedEnvironmentRequestModel
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
    ReplicateVoiceToIsolatedEnvironmentRequestModel:
      type: object
      properties:
        target_workspace_id:
          type: string
          description: >-
            ID of the workspace to replicate the voice into. It must belong to
            the same consolidated billing group as the calling workspace; the
            target's data residency is derived from that link.
        preserve_voice_id:
          type: boolean
          default: true
          description: >-
            When true (default) the replicated voice keeps the same voice ID in
            the target residency; set to false to assign a new voice ID.
      required:
        - target_workspace_id
      title: ReplicateVoiceToIsolatedEnvironmentRequestModel
    ReplicateVoiceToIsolatedEnvironmentResponseModel:
      type: object
      properties:
        voice_id:
          type: string
          description: Voice ID of the replicated voice in the target residency.
      required:
        - voice_id
      title: ReplicateVoiceToIsolatedEnvironmentResponseModel
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
  "target_workspace_id": "ws_8f3b2c9d7a1e4f6b"
}
```

**Response**

```json
{
  "voice_id": "21m00Tcm4TlvDq8ikWAM"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.replicateToIsolatedEnvironment("voice_id", {
        targetWorkspaceId: "ws_8f3b2c9d7a1e4f6b",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.replicate_to_isolated_environment(
    voice_id="voice_id",
    target_workspace_id="ws_8f3b2c9d7a1e4f6b",
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

	url := "https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment"

	payload := strings.NewReader("{\n  \"target_workspace_id\": \"ws_8f3b2c9d7a1e4f6b\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"target_workspace_id\": \"ws_8f3b2c9d7a1e4f6b\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment")
  .header("Content-Type", "application/json")
  .body("{\n  \"target_workspace_id\": \"ws_8f3b2c9d7a1e4f6b\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment', [
  'body' => '{
  "target_workspace_id": "ws_8f3b2c9d7a1e4f6b"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"target_workspace_id\": \"ws_8f3b2c9d7a1e4f6b\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["target_workspace_id": "ws_8f3b2c9d7a1e4f6b"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/voice_id/replicate-to-isolated-environment")! as URL,
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
