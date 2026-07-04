---
title: "Create a pronunciation dictionary from rules"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-rules.md
path: docs/api-reference/pronunciation-dictionaries/create-from-rules
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create a pronunciation dictionary from rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules
Content-Type: application/json

Creates a new pronunciation dictionary from provided rules.

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-rules

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries/add-from-rules:
    post:
      operationId: create_from_rules
      summary: Create a pronunciation dictionary from rules
      description: Creates a new pronunciation dictionary from provided rules.
      tags:
        - pronunciationDictionaries
      parameters:
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
                $ref: '#/components/schemas/AddPronunciationDictionaryResponseModel'
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
                #/components/schemas/Body_Add_a_pronunciation_dictionary_v1_pronunciation_dictionaries_add_from_rules_post
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
    PronunciationDictionaryAliasRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
          description: The string to replace. Must be a non-empty string.
        case_sensitive:
          type: boolean
          default: true
          description: Whether the rule should match case-sensitively.
        word_boundaries:
          type: boolean
          default: true
          description: Whether the rule should only match at word boundaries.
        type:
          type: string
          enum:
            - alias
          description: The type of the rule.
        alias:
          type: string
          description: The alias for the string to be replaced.
      required:
        - string_to_replace
        - type
        - alias
      title: PronunciationDictionaryAliasRuleRequestModel
    PronunciationDictionaryPhonemeRuleRequestModel:
      type: object
      properties:
        string_to_replace:
          type: string
          description: The string to replace. Must be a non-empty string.
        case_sensitive:
          type: boolean
          default: true
          description: Whether the rule should match case-sensitively.
        word_boundaries:
          type: boolean
          default: true
          description: Whether the rule should only match at word boundaries.
        type:
          type: string
          enum:
            - phoneme
          description: The type of the rule.
        phoneme:
          type: string
          description: The phoneme rule.
        alphabet:
          type: string
          description: The alphabet to use with the phoneme rule.
      required:
        - string_to_replace
        - type
        - phoneme
        - alphabet
      title: PronunciationDictionaryPhonemeRuleRequestModel
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItems:
      oneOf:
        - $ref: '#/components/schemas/PronunciationDictionaryAliasRuleRequestModel'
        - $ref: '#/components/schemas/PronunciationDictionaryPhonemeRuleRequestModel'
      title: >-
        BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItems
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: >-
        Should be one of 'admin', 'editor' or 'viewer'. If not provided,
        defaults to no access.
      title: >-
        BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess
    Body_Add_a_pronunciation_dictionary_v1_pronunciation_dictionaries_add_from_rules_post:
      type: object
      properties:
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItems
          description: |-
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
        name:
          type: string
          description: >-
            The name of the pronunciation dictionary, used for identification
            only.
        description:
          type:
            - string
            - 'null'
          description: >-
            A description of the pronunciation dictionary, used for
            identification only.
        workspace_access:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess
            - type: 'null'
          description: >-
            Should be one of 'admin', 'editor' or 'viewer'. If not provided,
            defaults to no access.
      required:
        - rules
        - name
      title: >-
        Body_Add_a_pronunciation_dictionary_v1_pronunciation_dictionaries_add_from_rules_post
    AddPronunciationDictionaryResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The permission on the resource of the pronunciation dictionary.
      title: AddPronunciationDictionaryResponseModelPermissionOnResource
    AddPronunciationDictionaryResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the created pronunciation dictionary.
        name:
          type: string
          description: The name of the created pronunciation dictionary.
        created_by:
          type: string
          description: The user ID of the creator of the pronunciation dictionary.
        creation_time_unix:
          type: integer
          description: The creation time of the pronunciation dictionary in Unix timestamp.
        version_id:
          type: string
          description: The ID of the created pronunciation dictionary version.
        version_rules_num:
          type: integer
          description: The number of rules in the version of the pronunciation dictionary.
        description:
          type:
            - string
            - 'null'
          description: The description of the pronunciation dictionary.
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/AddPronunciationDictionaryResponseModelPermissionOnResource
            - type: 'null'
          description: The permission on the resource of the pronunciation dictionary.
      required:
        - id
        - name
        - created_by
        - creation_time_unix
        - version_id
        - version_rules_num
        - permission_on_resource
      title: AddPronunciationDictionaryResponseModel
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
  "rules": [
    {
      "alias": "string",
      "string_to_replace": "string",
      "type": "string"
    }
  ],
  "name": "My Dictionary"
}
```

**Response**

```json
{
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "name": "My Dictionary",
  "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
  "creation_time_unix": 1714156800,
  "version_id": "5xM3yVvZQKV0EfqQpLrJ",
  "version_rules_num": 5,
  "permission_on_resource": "admin",
  "description": "This is a test dictionary"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.createFromRules({
        rules: [],
        name: "My Dictionary",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.create_from_rules(
    rules=[],
    name="My Dictionary",
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules', [
  'body' => '{
  "rules": [
    {
      "alias": "string",
      "string_to_replace": "string",
      "type": "string"
    }
  ],
  "name": "My Dictionary"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ],\n  \"name\": \"My Dictionary\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "rules": [
    [
      "alias": "string",
      "string_to_replace": "string",
      "type": "string"
    ]
  ],
  "name": "My Dictionary"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules")! as URL,
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
