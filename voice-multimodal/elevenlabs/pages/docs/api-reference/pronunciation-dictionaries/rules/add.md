---
title: "Add pronunciation dictionary rules"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/add.md
path: docs/api-reference/pronunciation-dictionaries/rules/add
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules
Content-Type: application/json

Add rules to the pronunciation dictionary. If a rule with the same string_to_replace already exists, it will be replaced.

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/add

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules:
    post:
      operationId: add
      summary: Add pronunciation dictionary rules
      description: >-
        Add rules to the pronunciation dictionary. If a rule with the same
        string_to_replace already exists, it will be replaced.
      tags:
        - rules
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
                $ref: '#/components/schemas/PronunciationDictionaryRulesResponseModel'
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
                #/components/schemas/Body_Add_rules_to_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__add_rules_post
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
    BodyAddRulesToThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdAddRulesPostRulesItems:
      oneOf:
        - $ref: '#/components/schemas/PronunciationDictionaryAliasRuleRequestModel'
        - $ref: '#/components/schemas/PronunciationDictionaryPhonemeRuleRequestModel'
      title: >-
        BodyAddRulesToThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdAddRulesPostRulesItems
    Body_Add_rules_to_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__add_rules_post:
      type: object
      properties:
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/BodyAddRulesToThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdAddRulesPostRulesItems
          description: |-
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
      required:
        - rules
      title: >-
        Body_Add_rules_to_the_pronunciation_dictionary_v1_pronunciation_dictionaries__pronunciation_dictionary_id__add_rules_post
    PronunciationDictionaryRulesResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the pronunciation dictionary.
        version_id:
          type: string
          description: The version ID of the pronunciation dictionary.
        version_rules_num:
          type: integer
          description: The number of rules in the version of the pronunciation dictionary.
      required:
        - id
        - version_id
        - version_rules_num
      title: PronunciationDictionaryRulesResponseModel
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
  ]
}
```

**Response**

```json
{
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "version_id": "5xM3yVvZQKV0EfqQpLr2",
  "version_rules_num": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.rules.add("pronunciation_dictionary_id", {
        rules: [],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.rules.add(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
    rules=[],
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules', [
  'body' => '{
  "rules": [
    {
      "alias": "string",
      "string_to_replace": "string",
      "type": "string"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"string\",\n      \"type\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["rules": [
    [
      "alias": "string",
      "string_to_replace": "string",
      "type": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/add-rules")! as URL,
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
