---
title: "Update Pronunciation Dictionary"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/update.md
path: docs/api-reference/pronunciation-dictionaries/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Pronunciation Dictionary

PATCH https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}
Content-Type: application/json

Partially update the pronunciation dictionary without changing the version

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}:
    patch:
      operationId: update
      summary: Update Pronunciation Dictionary
      description: >-
        Partially update the pronunciation dictionary without changing the
        version
      tags:
        - subpackage_pronunciationDictionaries
      parameters:
        - name: pronunciation_dictionary_id
          in: path
          description: The id of the pronunciation dictionary
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
                  #/components/schemas/GetPronunciationDictionaryMetadataResponseModel
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
                #/components/schemas/Body_Update_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__patch
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
    Body_Update_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__patch:
      type: object
      properties:
        archived:
          type: boolean
          description: Whether to archive the pronunciation dictionary.
        name:
          type: string
          description: >-
            The name of the pronunciation dictionary, used for identification
            only.
      title: >-
        Body_Update_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__patch
    GetPronunciationDictionaryMetadataResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The permission on the resource of the pronunciation dictionary.
      title: GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
    GetPronunciationDictionaryMetadataResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the pronunciation dictionary.
        latest_version_id:
          type: string
          description: The ID of the latest version of the pronunciation dictionary.
        latest_version_rules_num:
          type: integer
          description: >-
            The number of rules in the latest version of the pronunciation
            dictionary.
        name:
          type: string
          description: The name of the pronunciation dictionary.
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/GetPronunciationDictionaryMetadataResponseModelPermissionOnResource
            - type: 'null'
          description: The permission on the resource of the pronunciation dictionary.
        created_by:
          type: string
          description: The user ID of the creator of the pronunciation dictionary.
        creation_time_unix:
          type: integer
          description: The creation time of the pronunciation dictionary in Unix timestamp.
        archived_time_unix:
          type:
            - integer
            - 'null'
          description: The archive time of the pronunciation dictionary in Unix timestamp.
        description:
          type:
            - string
            - 'null'
          description: The description of the pronunciation dictionary.
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix
      title: GetPronunciationDictionaryMetadataResponseModel
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
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "latest_version_id": "5xM3yVvZQKV0EfqQpLr2",
  "latest_version_rules_num": 2,
  "name": "My Dictionary",
  "permission_on_resource": "admin",
  "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
  "creation_time_unix": 1714156800,
  "description": "This is a test dictionary"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.update("pronunciation_dictionary_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.update(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
