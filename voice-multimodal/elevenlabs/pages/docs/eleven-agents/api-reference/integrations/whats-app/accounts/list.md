---
title: "List WhatsApp accounts"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/integrations/whats-app/accounts/list.md
path: docs/eleven-agents/api-reference/integrations/whats-app/accounts/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List WhatsApp accounts

GET https://api.elevenlabs.io/v1/convai/whatsapp-accounts

List all WhatsApp accounts

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/integrations/whats-app/accounts/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional) — Filter by assigned agent ID

## Response

### 200

Successful Response

- `items` (list of GetWhatsAppAccountResponse, required)

## Errors

### 422 Whatsapp Accounts List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### GetWhatsAppAccountResponse

- `business_account_id` (string, required)
- `phone_number_id` (string, required)
- `business_account_name` (string, required)
- `phone_number_name` (string, required)
- `phone_number` (string, required)
- `account_type` (enum, optional, default: cloud_api) — Which Embedded Signup flow produced this account.
  - Allowed values: `cloud_api`, `coexistence`
- `assigned_agent_id` (string, optional)
- `enable_messaging` (boolean, optional, default: true)
- `enable_audio_message_response` (boolean, optional, default: true)
- `enable_typing_indicator` (boolean, optional, default: true)
- `assigned_agent_name` (string, optional)
- `is_token_expired` (boolean, optional, default: false)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "items": [
    {
      "business_account_id": "102938475610293",
      "phone_number_id": "114567890123456",
      "business_account_name": "Acme Corp Support",
      "phone_number_name": "Acme Customer Service",
      "phone_number": "+14155552671",
      "account_type": "cloud_api",
      "assigned_agent_id": "agent_8f3k2m9p1x7q",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "enable_typing_indicator": true,
      "assigned_agent_name": "Customer Support Agent",
      "is_token_expired": false
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/whatsapp-accounts"

querystring = {"agent_id":"agent_id"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")! as URL,
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
