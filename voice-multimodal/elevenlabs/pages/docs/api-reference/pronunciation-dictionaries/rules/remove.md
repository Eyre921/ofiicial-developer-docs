---
title: "Remove pronunciation dictionary rules"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/remove.md
path: docs/api-reference/pronunciation-dictionaries/rules/remove
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Remove pronunciation dictionary rules

POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/remove-rules
Content-Type: application/json

Remove rules from the pronunciation dictionary

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/rules/remove

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

- `rule_strings` (list of string, required) — List of strings to remove from the pronunciation dictionary.

## Response

### 200

Successful Response

- `id` (string, required) — The ID of the pronunciation dictionary.
- `version_id` (string, required) — The version ID of the pronunciation dictionary.
- `version_rules_num` (integer, required) — The number of rules in the version of the pronunciation dictionary.

## Examples

**Request**

```json
{
  "rule_strings": [
    "['a', 'b']"
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
    await client.pronunciationDictionaries.rules.remove("pronunciation_dictionary_id", {
        ruleStrings: [
            "['a', 'b']",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.rules.remove(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
    rule_strings=[
        "[\'a\', \'b\']"
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

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules"

	payload := strings.NewReader("{\n  \"rule_strings\": [\n    \"['a', 'b']\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rule_strings\": [\n    \"['a', 'b']\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")
  .header("Content-Type", "application/json")
  .body("{\n  \"rule_strings\": [\n    \"['a', 'b']\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules', [
  'body' => '{
  "rule_strings": [
    "[\'a\', \'b\']"
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

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rule_strings\": [\n    \"['a', 'b']\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["rule_strings": ["['a', 'b']"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id/remove-rules")! as URL,
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
