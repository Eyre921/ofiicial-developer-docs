---
title: "Set workspace third-party disabling policy"
source: https://elevenlabs.io/docs/api-reference/api-keys/set-third-party-disabling-policy.md
path: docs/api-reference/api-keys/set-third-party-disabling-policy
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Set workspace third-party disabling policy

POST https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling
Content-Type: application/json

Set the workspace-wide Third-Party Disabling policy. When set, it forces, for every API key in the workspace, whether the holder of a key (potentially a third party who found it) may disable it via the self-disable endpoint or when it leaks publicly — overriding each key's own setting. Pass `true` to allow it for all keys, `false` to forbid it for all keys, or `null` to clear the override so per-key values and the plan default apply again. Workspace admins only.

Reference: https://elevenlabs.io/docs/api-reference/api-keys/set-third-party-disabling-policy

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `third_party_disable_allowed` (boolean, optional, nullable) — `true` forces every key in the workspace to be disable-able by its holder; `false` forbids it for every key; `null` clears the override (per-key values and the plan default apply).

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{
  "third_party_disable_allowed": true
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
    await client.workspace.setThirdPartyDisablingPolicy({
        thirdPartyDisableAllowed: true,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.set_third_party_disabling_policy(
    third_party_disable_allowed=True,
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

	url := "https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling"

	payload := strings.NewReader("{\n  \"third_party_disable_allowed\": true\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"third_party_disable_allowed\": true\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling")
  .header("Content-Type", "application/json")
  .body("{\n  \"third_party_disable_allowed\": true\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling', [
  'body' => '{
  "third_party_disable_allowed": true
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"third_party_disable_allowed\": true\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["third_party_disable_allowed": true] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspaces/api-keys/third-party-disabling")! as URL,
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
