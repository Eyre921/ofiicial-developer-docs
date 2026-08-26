---
title: "Get WhatsApp account"
source: https://elevenlabs.io/docs/api-reference/whats-app/accounts/get.md
path: docs/api-reference/whats-app/accounts/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get WhatsApp account

GET https://api.elevenlabs.io/v1/convai/whatsapp-accounts/{phone_number_id}

Get a WhatsApp account

Reference: https://elevenlabs.io/docs/api-reference/whats-app/accounts/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `phone_number_id` (string, required)

## Response

### 200

Successful Response

- `business_account_id` (string, required)
- `phone_number_id` (string, required)
- `business_account_name` (string, required)
- `phone_number_name` (string, required)
- `phone_number` (string, required)
- `assigned_agent_name` (string, required, nullable)
- `assigned_agent_id` (string, optional, nullable)
- `enable_messaging` (boolean, optional, default: true)
- `enable_audio_message_response` (boolean, optional, default: true)
- `enable_typing_indicator` (boolean, optional, default: true)
- `is_token_expired` (boolean, optional, default: false)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "business_account_id": "biz_9876543210",
  "phone_number_id": "phone_1234567890",
  "business_account_name": "Acme Corp",
  "phone_number_name": "Acme Support Line",
  "phone_number": "+14155552671",
  "assigned_agent_name": "Jane Doe",
  "assigned_agent_id": "agent_456789",
  "enable_messaging": true,
  "enable_audio_message_response": true,
  "enable_typing_indicator": true,
  "is_token_expired": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsappAccounts.get("phone_number_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp_accounts.get(
    phone_number_id="phone_number_id",
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

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
