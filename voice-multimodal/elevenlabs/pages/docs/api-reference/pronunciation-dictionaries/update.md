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

- `archived` (boolean, optional) — Whether to archive the pronunciation dictionary.
- `name` (string, optional) — The name of the pronunciation dictionary, used for identification only.

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
- `archived_time_unix` (integer, optional, nullable) — The archive time of the pronunciation dictionary in Unix timestamp.
- `description` (string, optional, nullable) — The description of the pronunciation dictionary.

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
