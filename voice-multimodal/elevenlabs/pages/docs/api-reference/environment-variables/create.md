---
title: "Create environment variable"
source: https://elevenlabs.io/docs/api-reference/environment-variables/create.md
path: docs/api-reference/environment-variables/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create environment variable

POST https://api.elevenlabs.io/v1/convai/environment-variables
Content-Type: application/json

Create a new environment variable for the workspace

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `object`
  - `type`: `string` (CreateStringEnvironmentVariableRequest)
    - `label` (string, required) — Unique label for the environment variable.
    - `values` (map from string to string, required) — Environment-specific values. Must include 'production' key.
  - `type`: `secret` (CreateSecretEnvironmentVariableRequest)
    - `label` (string, required) — Unique label for the environment variable.
    - `values` (map from string to object, required) — Environment-specific secret references. Must include 'production' key.
      - `secret_id` (string, required)
  - `type`: `auth_connection` (CreateAuthConnectionEnvironmentVariableRequest)
    - `label` (string, required) — Unique label for the environment variable.
    - `values` (map from string to object, required) — Environment-specific auth connection references. Must include 'production' key.
      - `auth_connection_id` (string, required)

## Response

### 200

Successful Response

- `label` (string, required)
- `created_at_unix_secs` (integer, required)
- `updated_at_unix_secs` (integer, required)
- `type` (enum, required)
  - Allowed values: `string`, `secret`, `auth_connection`
- `id` (string, required)
- `workspace_id` (string, required)
- `values` (map from string to string or map from string to object or map from string to object, required)
- `created_by_user_id` (string, optional, nullable)

## Examples

**Request**

```json
{
  "type": "string",
  "label": "string"
}
```

**Response**

```json
{
  "label": "string",
  "created_at_unix_secs": 1,
  "updated_at_unix_secs": 1,
  "type": "string",
  "id": "string",
  "workspace_id": "string",
  "values": {},
  "created_by_user_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.environmentVariables.create({
        type: "string",
        label: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs
from elevenlabs.environment_variables import EnvironmentVariablesCreateRequestBody_String

client = ElevenLabs()

client.environment_variables.create(
    request=EnvironmentVariablesCreateRequestBody_String(
        label="string",
        values={},
    ),
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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables"

	payload := strings.NewReader("{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/environment-variables")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/environment-variables', [
  'body' => '{
  "type": "string",
  "label": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"string\",\n  \"label\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "string",
  "label": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables")! as URL,
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
