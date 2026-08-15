---
title: "Set pronunciation dictionary rules"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/set.md
path: docs/api-reference/pronunciation-dictionaries/rules/set
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Set pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/set-rules
Content-Type: application/json

Replaces all existing rules on the pronunciation dictionary with the provided ones.

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/set

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `pronunciation_dictionary_id` (string, required) — The id of the pronunciation dictionary

### Body (application/json)

- `rules` (list of object or object, required) — List of pronunciation rules. Rule can be either: an alias rule: \{'string\_to\_replace': 'a', 'type': 'alias', 'alias': 'b', } or a phoneme rule: \{'string\_to\_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
  - PronunciationDictionaryAliasRuleRequestModel
    - `string_to_replace` (string, required) — The string to replace. Must be a non-empty string.
    - `type` ("alias", required) — The type of the rule.
    - `alias` (string, required) — The alias for the string to be replaced.
    - `case_sensitive` (boolean, optional, default: true) — Whether the rule should match case-sensitively.
    - `word_boundaries` (boolean, optional, default: true) — Whether the rule should only match at word boundaries.
  - PronunciationDictionaryPhonemeRuleRequestModel
    - `string_to_replace` (string, required) — The string to replace. Must be a non-empty string.
    - `type` ("phoneme", required) — The type of the rule.
    - `phoneme` (string, required) — The phoneme rule.
    - `alphabet` (string, required) — The alphabet to use with the phoneme rule.
    - `case_sensitive` (boolean, optional, default: true) — Whether the rule should match case-sensitively.
    - `word_boundaries` (boolean, optional, default: true) — Whether the rule should only match at word boundaries.

## Response

### 200

Successfully set rules on the pronunciation dictionary

- `id` (string, required) — The ID of the pronunciation dictionary.
- `version_id` (string, required) — The version ID of the pronunciation dictionary.
- `version_rules_num` (integer, required) — The number of rules in the version of the pronunciation dictionary.

## Examples

**Request**

```json
{
  "rules": [
    {
      "alias": "color",
      "string_to_replace": "colour",
      "type": "alias"
    },
    {
      "alias": "string",
      "string_to_replace": "route",
      "type": "phoneme"
    }
  ]
}
```

**Response**

```json
{
  "id": "5xM3yVvZQKV0EfqQpLrJ",
  "version_id": "5xM3yVvZQKV0EfqQpLr2",
  "version_rules_num": 2
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.rules.set("pronunciation_dictionary_id", {
        rules: [
            {
                type: "alias",
                stringToReplace: "colour",
                alias: "color",
            },
            {
                type: "phoneme",
                stringToReplace: "route",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs
from elevenlabs.pronunciation_dictionaries.rules import BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem_Alias, BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem_Phoneme

client = ElevenLabs()

client.pronunciation_dictionaries.rules.set(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
    rules=[
        BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem_Alias(
            string_to_replace="colour",
            alias="color",
        ),
        BodySetRulesOnThePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdSetRulesPostRulesItem_Phoneme(
            string_to_replace="route",
            phoneme="string",
            alphabet="string",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"alias\": \"color\",\n      \"string_to_replace\": \"colour\",\n      \"type\": \"alias\"\n    },\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"route\",\n      \"type\": \"phoneme\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"alias\": \"color\",\n      \"string_to_replace\": \"colour\",\n      \"type\": \"alias\"\n    },\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"route\",\n      \"type\": \"phoneme\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"alias\": \"color\",\n      \"string_to_replace\": \"colour\",\n      \"type\": \"alias\"\n    },\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"route\",\n      \"type\": \"phoneme\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules', [
  'body' => '{
  "rules": [
    {
      "alias": "color",
      "string_to_replace": "colour",
      "type": "alias"
    },
    {
      "alias": "string",
      "string_to_replace": "route",
      "type": "phoneme"
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

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"alias\": \"color\",\n      \"string_to_replace\": \"colour\",\n      \"type\": \"alias\"\n    },\n    {\n      \"alias\": \"string\",\n      \"string_to_replace\": \"route\",\n      \"type\": \"phoneme\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["rules": [
    [
      "alias": "color",
      "string_to_replace": "colour",
      "type": "alias"
    ],
    [
      "alias": "string",
      "string_to_replace": "route",
      "type": "phoneme"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/set-rules")! as URL,
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
