---
title: "Create API key"
source: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create.md
path: docs/api-reference/service-accounts/api-keys/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create API key

POST https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys
Content-Type: application/json

Create a new API key for a service account

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `service_account_user_id` (string, required)

### Body (application/json)

- `name` (string, required)
- `permissions` (list of enum or "all", required) — The permissions of the XI API.
- `character_limit` (integer, optional, nullable) — The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.
- `allowed_ips` (list of string, optional, nullable) — List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.
- `third_party_disable_allowed` (boolean, optional, nullable) — Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

## Response

### 200

Successful Response

- `xi-api-key` (string, required)
- `key_id` (string, required)

## Examples

**Request**

```json
{
  "name": "ServiceAccountKey2024",
  "permissions": [
    "text_to_speech",
    "models_read",
    "voices_read"
  ]
}
```

**Response**

```json
{
  "xi-api-key": "sk_live_4f8b9c7d2e1a4b6f9c3d7e8a1b2c3d4e",
  "key_id": "key_123e4567-e89b-12d3-a456-426614174000"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.apiKeys.create("service_account_user_id", {
        name: "ServiceAccountKey2024",
        permissions: [
            "text_to_speech",
            "models_read",
            "voices_read",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.api_keys.create(
    service_account_user_id="service_account_user_id",
    name="ServiceAccountKey2024",
    permissions=[
        "text_to_speech",
        "models_read",
        "voices_read"
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

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys"

	payload := strings.NewReader("{\n  \"name\": \"ServiceAccountKey2024\",\n  \"permissions\": [\n    \"text_to_speech\",\n    \"models_read\",\n    \"voices_read\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"ServiceAccountKey2024\",\n  \"permissions\": [\n    \"text_to_speech\",\n    \"models_read\",\n    \"voices_read\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"ServiceAccountKey2024\",\n  \"permissions\": [\n    \"text_to_speech\",\n    \"models_read\",\n    \"voices_read\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys', [
  'body' => '{
  "name": "ServiceAccountKey2024",
  "permissions": [
    "text_to_speech",
    "models_read",
    "voices_read"
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

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"ServiceAccountKey2024\",\n  \"permissions\": [\n    \"text_to_speech\",\n    \"models_read\",\n    \"voices_read\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "name": "ServiceAccountKey2024",
  "permissions": ["text_to_speech", "models_read", "voices_read"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")! as URL,
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
