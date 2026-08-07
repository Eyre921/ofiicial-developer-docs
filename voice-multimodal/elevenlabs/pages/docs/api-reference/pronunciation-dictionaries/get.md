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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `pronunciation_dictionary_id` (string, required) — The id of the pronunciation dictionary

## Response

### 200

Successful Response

- `id` (string, required) — The ID of the pronunciation dictionary.
- `latest_version_id` (string, required) — The ID of the latest version of the pronunciation dictionary.
- `latest_version_rules_num` (integer, required) — The number of rules in the latest version of the pronunciation dictionary.
- `name` (string, required) — The name of the pronunciation dictionary.
- `permission_on_resource` (enum, required, nullable) — The permission on the resource of the pronunciation dictionary.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `created_by` (string, required) — The user ID of the creator of the pronunciation dictionary.
- `creation_time_unix` (integer, required) — The creation time of the pronunciation dictionary in Unix timestamp.
- `rules` (list of object or object, required) — The rules in the latest version of the pronunciation dictionary.
  - PronunciationDictionaryAliasRuleResponseModel
    - `string_to_replace` (string, required)
    - `type` ("alias", required)
    - `alias` (string, required)
    - `case_sensitive` (boolean, optional, default: true) — Whether the rule matches case-sensitively.
    - `word_boundaries` (boolean, optional, default: true) — Whether the rule only matches at word boundaries.
  - PronunciationDictionaryPhonemeRuleResponseModel
    - `string_to_replace` (string, required)
    - `type` ("phoneme", required)
    - `phoneme` (string, required)
    - `alphabet` (string, required)
    - `case_sensitive` (boolean, optional, default: true) — Whether the rule matches case-sensitively.
    - `word_boundaries` (boolean, optional, default: true) — Whether the rule only matches at word boundaries.
- `archived_time_unix` (integer, optional, nullable) — The archive time of the pronunciation dictionary in Unix timestamp.
- `description` (string, optional, nullable) — The description of the pronunciation dictionary.

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
