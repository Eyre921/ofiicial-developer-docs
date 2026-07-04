---
title: "Get pronunciation dictionary"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/get.md
path: docs/api-reference/pronunciation-dictionaries/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get pronunciation dictionary

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}

Get metadata for a pronunciation dictionary

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}:
    get:
      operationId: get
      summary: Get pronunciation dictionary
      description: Get metadata for a pronunciation dictionary
      tags:
        - pronunciationDictionaries
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
                  #/components/schemas/GetPronunciationDictionaryWithRulesResponseModel
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
    GetPronunciationDictionaryWithRulesResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The permission on the resource of the pronunciation dictionary.
      title: GetPronunciationDictionaryWithRulesResponseModelPermissionOnResource
    PronunciationDictionaryAliasRuleResponseModel:
      type: object
      properties:
        string_to_replace:
          type: string
        case_sensitive:
          type: boolean
          default: true
          description: Whether the rule matches case-sensitively.
        word_boundaries:
          type: boolean
          default: true
          description: Whether the rule only matches at word boundaries.
        type:
          type: string
          enum:
            - alias
        alias:
          type: string
      required:
        - string_to_replace
        - type
        - alias
      title: PronunciationDictionaryAliasRuleResponseModel
    PronunciationDictionaryPhonemeRuleResponseModel:
      type: object
      properties:
        string_to_replace:
          type: string
        case_sensitive:
          type: boolean
          default: true
          description: Whether the rule matches case-sensitively.
        word_boundaries:
          type: boolean
          default: true
          description: Whether the rule only matches at word boundaries.
        type:
          type: string
          enum:
            - phoneme
        phoneme:
          type: string
        alphabet:
          type: string
      required:
        - string_to_replace
        - type
        - phoneme
        - alphabet
      title: PronunciationDictionaryPhonemeRuleResponseModel
    GetPronunciationDictionaryWithRulesResponseModelRulesItems:
      oneOf:
        - $ref: '#/components/schemas/PronunciationDictionaryAliasRuleResponseModel'
        - $ref: '#/components/schemas/PronunciationDictionaryPhonemeRuleResponseModel'
      title: GetPronunciationDictionaryWithRulesResponseModelRulesItems
    GetPronunciationDictionaryWithRulesResponseModel:
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
                #/components/schemas/GetPronunciationDictionaryWithRulesResponseModelPermissionOnResource
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
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/GetPronunciationDictionaryWithRulesResponseModelRulesItems
          description: The rules in the latest version of the pronunciation dictionary.
      required:
        - id
        - latest_version_id
        - latest_version_rules_num
        - name
        - permission_on_resource
        - created_by
        - creation_time_unix
        - rules
      title: GetPronunciationDictionaryWithRulesResponseModel
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
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "latest_version_id": "5xM3yVvZQKV0EfqQpLr2",
  "latest_version_rules_num": 2,
  "name": "My Dictionary",
  "permission_on_resource": "admin",
  "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
  "creation_time_unix": 1714156800,
  "rules": [
    {
      "alias": "tie-land",
      "string_to_replace": "Thailand",
      "type": "alias"
    },
    {
      "alphabet": "ipa",
      "phoneme": "/təˈmeɪtoʊ/",
      "string_to_replace": "Tomato",
      "type": "phoneme"
    }
  ],
  "description": "This is a test dictionary"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.get("pronunciation_dictionary_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.get(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")! as URL,
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
