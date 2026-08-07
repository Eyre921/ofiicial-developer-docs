---
title: "Update environment variable"
source: https://elevenlabs.io/docs/api-reference/environment-variables/update.md
path: docs/api-reference/environment-variables/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update environment variable

PATCH https://api.elevenlabs.io/v1/convai/environment-variables/{env_var_id}
Content-Type: application/json

Replace an environment variable's values. Use null to remove an environment (except production).

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `env_var_id` (string, required)

### Body (application/json)

- `values` (map from string to string or object or object, required) — Values to replace. Set to null to remove an environment (except 'production').
  - EnvironmentVariableSecretValueRequest
    - `secret_id` (string, required)
  - EnvironmentVariableAuthConnectionValueRequest
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
{}
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
    await client.environmentVariables.update("env_var_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.environment_variables.update(
    env_var_id="env_var_id",
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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")

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

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")! as URL,
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
