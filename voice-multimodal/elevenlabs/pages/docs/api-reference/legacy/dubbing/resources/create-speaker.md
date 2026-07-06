---
title: "Create speaker"
source: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/create-speaker.md
path: docs/api-reference/legacy/dubbing/resources/create-speaker
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create speaker

POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker
Content-Type: application/json

Creates a new speaker in a dubbing resource. The speaker is added to every available language and can optionally be associated with an ElevenLabs voice and voice settings.

Reference: https://elevenlabs.io/docs/api-reference/legacy/dubbing/resources/create-speaker

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/dubbing/resource/{dubbing_id}/speaker:
    post:
      operationId: create
      summary: Create A New Speaker
      description: >-
        Creates a new speaker in a dubbing resource. The speaker is added to
        every available language and can optionally be associated with an
        ElevenLabs voice and voice settings.
      tags:
        - speaker
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
                $ref: '#/components/schemas/SpeakerCreatedResponse'
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
                #/components/schemas/Body_Create_a_new_speaker_v1_dubbing_resource__dubbing_id__speaker_post
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
    Body_Create_a_new_speaker_v1_dubbing_resource__dubbing_id__speaker_post:
      type: object
      properties:
        speaker_name:
          type:
            - string
            - 'null'
          description: Name to attribute to this speaker.
        voice_id:
          type:
            - string
            - 'null'
          description: >-
            Either the identifier of a voice from the ElevenLabs voice library,
            or one of ['track-clone', 'clip-clone'].
        voice_stability:
          type:
            - number
            - 'null'
          format: double
          description: >-
            For models that support it, the voice similarity value to use. This
            will default to 0.65, with a valid range of [0.0, 1.0].
        voice_similarity:
          type:
            - number
            - 'null'
          format: double
          description: >-
            For models that support it, the voice similarity value to use. This
            will default to 1.0, with a valid range of [0.0, 1.0].
        voice_style:
          type:
            - number
            - 'null'
          format: double
          description: >-
            For models that support it, the voice style value to use. This will
            default to 1.0, with a valid range of [0.0, 1.0].
      title: Body_Create_a_new_speaker_v1_dubbing_resource__dubbing_id__speaker_post
    SpeakerCreatedResponse:
      type: object
      properties:
        version:
          type: integer
        speaker_id:
          type: string
      required:
        - version
        - speaker_id
      title: SpeakerCreatedResponse
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
  "version": 1,
  "speaker_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.speaker.create("dubbing_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.speaker.create(
    dubbing_id="dubbing_id",
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

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/speaker")! as URL,
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
