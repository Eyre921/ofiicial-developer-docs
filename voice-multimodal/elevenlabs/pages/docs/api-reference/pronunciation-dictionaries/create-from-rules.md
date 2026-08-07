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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

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
- `name` (string, required) — The name of the pronunciation dictionary, used for identification only.
- `description` (string, optional, nullable) — A description of the pronunciation dictionary, used for identification only.
- `workspace_access` (enum, optional, nullable) — Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`

## Response

### 200

Successful Response

- `id` (string, required) — The ID of the created pronunciation dictionary.
- `name` (string, required) — The name of the created pronunciation dictionary.
- `created_by` (string, required) — The user ID of the creator of the pronunciation dictionary.
- `creation_time_unix` (integer, required) — The creation time of the pronunciation dictionary in Unix timestamp.
- `version_id` (string, required) — The ID of the created pronunciation dictionary version.
- `version_rules_num` (integer, required) — The number of rules in the version of the pronunciation dictionary.
- `permission_on_resource` (enum, required, nullable) — The permission on the resource of the pronunciation dictionary.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `description` (string, optional, nullable) — The description of the pronunciation dictionary.

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
