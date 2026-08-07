---
title: "Update secret"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/update.md
path: docs/api-reference/workspace/secrets/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update secret

PATCH https://api.elevenlabs.io/v1/convai/secrets/{secret_id}
Content-Type: application/json

Update an existing secret for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `secret_id` (string, required)

### Body (application/json)

- `type` ("update", required)
- `name` (string, required)
- `value` (string, required)

## Response

### 200

Successful Response

- `type` ("stored", required)
- `secret_id` (string, required)
- `name` (string, required)

## Examples

**Request**

```json
{
  "type": "string",
  "name": "string",
  "value": "string"
}
```

**Response**

```json
{
  "type": "string",
  "secret_id": "string",
  "name": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.update("secret_id", {
        type: "string",
        name: "string",
        value: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.update(
    secret_id="secret_id",
    name="string",
    value="string",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

	payload := strings.NewReader("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id', [
  'body' => '{
  "type": "string",
  "name": "string",
  "value": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"string\",\n  \"name\": \"string\",\n  \"value\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "string",
  "name": "string",
  "value": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
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
