---
title: "Create secret"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/create.md
path: docs/api-reference/workspace/secrets/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create secret

POST https://api.elevenlabs.io/v1/convai/secrets
Content-Type: application/json

Create a new secret for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `type` ("new", required)
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
  "type": "new",
  "name": "database_password",
  "value": "S3cureP@ssw0rd!2024"
}
```

**Response**

```json
{
  "type": "stored",
  "secret_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
  "name": "database_password"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.create({
        type: "new",
        name: "database_password",
        value: "S3cureP@ssw0rd!2024",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.create(
    name="database_password",
    value="S3cureP@ssw0rd!2024",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets"

	payload := strings.NewReader("{\n  \"type\": \"new\",\n  \"name\": \"database_password\",\n  \"value\": \"S3cureP@ssw0rd!2024\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"new\",\n  \"name\": \"database_password\",\n  \"value\": \"S3cureP@ssw0rd!2024\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/secrets")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"new\",\n  \"name\": \"database_password\",\n  \"value\": \"S3cureP@ssw0rd!2024\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/secrets', [
  'body' => '{
  "type": "new",
  "name": "database_password",
  "value": "S3cureP@ssw0rd!2024"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"new\",\n  \"name\": \"database_password\",\n  \"value\": \"S3cureP@ssw0rd!2024\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "new",
  "name": "database_password",
  "value": "S3cureP@ssw0rd!2024"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets")! as URL,
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
