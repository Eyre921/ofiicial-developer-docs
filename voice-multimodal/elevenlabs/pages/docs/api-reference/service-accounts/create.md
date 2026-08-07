---
title: "Create Service Account"
source: https://elevenlabs.io/docs/api-reference/service-accounts/create.md
path: docs/api-reference/service-accounts/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Service Account

POST https://api.elevenlabs.io/v1/service-accounts
Content-Type: application/json

Create a new service account in the workspace. By default, a workspace can have up to 20 service accounts. Enterprise customers may request an increase to this limit, up to 100.

Reference: https://elevenlabs.io/docs/api-reference/service-accounts/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `name` (string, required)
- `default_sharing_groups` (list of object, optional, nullable) — List of groups with their permission levels to share with by default. Each entry should specify a group_id and a permission_level (admin, editor, or viewer).
  - `group_id` (string, required) — The ID of the group to share with
  - `permission_level` (enum, required) — The permission level to grant to the group
    - Allowed values: `admin`, `editor`, `viewer`

## Response

### 200

Successful Response

- `service-account-user-id` (string, required)

## Examples

**Request**

```json
{
  "name": "analytics-service-account"
}
```

**Response**

```json
{
  "service-account-user-id": "svc-123e4567-e89b-12d3-a456-426614174000"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.create({
        name: "analytics-service-account",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.create(
    name="analytics-service-account",
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

	url := "https://api.elevenlabs.io/v1/service-accounts"

	payload := strings.NewReader("{\n  \"name\": \"analytics-service-account\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/service-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"analytics-service-account\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/service-accounts")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"analytics-service-account\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/service-accounts', [
  'body' => '{
  "name": "analytics-service-account"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"analytics-service-account\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "analytics-service-account"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts")! as URL,
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
