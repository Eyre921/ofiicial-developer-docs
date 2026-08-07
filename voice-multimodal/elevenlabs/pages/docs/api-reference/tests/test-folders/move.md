---
title: "Bulk move tests to folder"
source: https://elevenlabs.io/docs/api-reference/tests/test-folders/move.md
path: docs/api-reference/tests/test-folders/move
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bulk move tests to folder

POST https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move
Content-Type: application/json

Moves multiple tests or folders from one folder to another.

Reference: https://elevenlabs.io/docs/api-reference/tests/test-folders/move

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `entity_ids` (list of string, required) — The IDs of tests or folders to move.
- `move_to` (string, optional, nullable) — The folder to move the entities to. If not set, the entities will be moved to the root folder.

## Response

### 200

Tests or folders successfully moved to another folder

- `any`

## Examples

**Request**

```json
{
  "entity_ids": [
    "test_9f8b7c6d5e4a3b2c1d0e"
  ],
  "move_to": "folder_123abc456def789ghi"
}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.move({
        entityIds: [
            "test_9f8b7c6d5e4a3b2c1d0e",
        ],
        moveTo: "folder_123abc456def789ghi",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.move(
    entity_ids=[
        "test_9f8b7c6d5e4a3b2c1d0e"
    ],
    move_to="folder_123abc456def789ghi",
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move"

	payload := strings.NewReader("{\n  \"entity_ids\": [\n    \"test_9f8b7c6d5e4a3b2c1d0e\"\n  ],\n  \"move_to\": \"folder_123abc456def789ghi\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"entity_ids\": [\n    \"test_9f8b7c6d5e4a3b2c1d0e\"\n  ],\n  \"move_to\": \"folder_123abc456def789ghi\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move")
  .header("Content-Type", "application/json")
  .body("{\n  \"entity_ids\": [\n    \"test_9f8b7c6d5e4a3b2c1d0e\"\n  ],\n  \"move_to\": \"folder_123abc456def789ghi\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move', [
  'body' => '{
  "entity_ids": [
    "test_9f8b7c6d5e4a3b2c1d0e"
  ],
  "move_to": "folder_123abc456def789ghi"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"entity_ids\": [\n    \"test_9f8b7c6d5e4a3b2c1d0e\"\n  ],\n  \"move_to\": \"folder_123abc456def789ghi\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "entity_ids": ["test_9f8b7c6d5e4a3b2c1d0e"],
  "move_to": "folder_123abc456def789ghi"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/bulk-move")! as URL,
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
