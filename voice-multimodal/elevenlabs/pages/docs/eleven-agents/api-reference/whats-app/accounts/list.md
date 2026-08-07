---
title: "List WhatsApp accounts"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/accounts/list.md
path: docs/eleven-agents/api-reference/whats-app/accounts/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List WhatsApp accounts

GET https://api.elevenlabs.io/v1/convai/whatsapp-accounts

List all WhatsApp accounts

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/accounts/list

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

- `items` (list of object, required)
  - `business_account_id` (string, required)
  - `phone_number_id` (string, required)
  - `business_account_name` (string, required)
  - `phone_number_name` (string, required)
  - `phone_number` (string, required)
  - `assigned_agent_id` (string, optional)
  - `enable_messaging` (boolean, optional, default: true)
  - `enable_audio_message_response` (boolean, optional, default: true)
  - `enable_typing_indicator` (boolean, optional, default: true)
  - `assigned_agent_name` (string, optional)
  - `is_token_expired` (boolean, optional, default: false)

## Examples

**Response**

```json
{
  "items": [
    {
      "business_account_id": "business_account_id",
      "phone_number_id": "phone_number_id",
      "business_account_name": "business_account_name",
      "phone_number_name": "phone_number_name",
      "phone_number": "phone_number",
      "assigned_agent_id": "assigned_agent_id",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "enable_typing_indicator": true,
      "assigned_agent_name": "assigned_agent_name",
      "is_token_expired": true
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsappAccounts.list({
        agentId: "agent_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp_accounts.list(
    agent_id="agent_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id"

	req, _ := http.NewRequest("GET", url, nil)

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

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts?agent_id=agent_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
