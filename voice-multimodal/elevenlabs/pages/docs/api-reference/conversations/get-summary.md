---
title: "Get conversation summary"
source: https://elevenlabs.io/docs/api-reference/conversations/get-summary.md
path: docs/api-reference/conversations/get-summary
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get conversation summary

GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/summary

Get a lightweight summary of a conversation: its title, the generated transcript summary, whether the call was successful, and — only when the conversation is short — the plain chat messages. Tool calls, tool results, and contextual updates are omitted so the response stays small. Use this instead of the full conversation endpoint when you only need the gist (e.g. an agent reading many conversations); use GET /v1/convai/conversations/\{conversation\_id} when you need the full transcript with tool calls and contextual updates.

Reference: https://elevenlabs.io/docs/api-reference/conversations/get-summary

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — The id of the conversation you're taking the action on.

### Query parameters

- `max_messages` (integer, optional, default: 40) — Maximum number of chat message turns to include inline. When the conversation has more than this, the messages are omitted and messages_omitted is set.

## Response

### 200

Successful Response

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `message_count` (integer, required) — Number of plain chat message turns in the conversation.
- `note` (string, required) — Guidance telling the agent how to get the full transcript.
- `call_summary_title` (string, optional, nullable) — Short generated title for the conversation.
- `transcript_summary` (string, optional, nullable) — Generated natural-language summary of the call.
- `call_successful` (enum, optional, nullable)
  - Allowed values: `success`, `failure`, `unknown`
- `messages` (list of ConversationSummaryMessageModel, optional, nullable) — The plain chat messages (role and text only). Included only when message_count does not exceed the requested max_messages; otherwise null and messages_omitted is true.
- `messages_omitted` (boolean, optional, default: false) — True when the chat messages were omitted because the conversation was too long. Fetch the full transcript for the messages.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConversationSummaryMessageModel

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `message` (string, required)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "conversation_id": "21m00Tcm4TlvDq8ikWAM",
  "agent_id": "9BWtsMINqrJLrRacOk9x",
  "status": "done",
  "message_count": 6,
  "note": "This summary omits tool calls and contextual updates. To retrieve the full transcript including tool calls and contextual updates, use GET /v1/convai/conversations/21m00Tcm4TlvDq8ikWAM.",
  "call_summary_title": "Customer Inquiry About Subscription Upgrade",
  "transcript_summary": "The user contacted support to inquire about upgrading their current plan from the Starter tier to the Professional tier. The agent explained the pricing differences, additional features included in the Professional plan, and walked the user through the upgrade process. The user confirmed they wanted to proceed and the upgrade was successfully initiated.",
  "call_successful": "success",
  "messages": [
    {
      "role": "user",
      "message": "Hi, I'd like to know more about upgrading my current subscription plan."
    },
    {
      "role": "agent",
      "message": "Hello! I'd be happy to help you with that. Could you tell me which plan you're currently on and what you're looking to upgrade to?"
    },
    {
      "role": "user",
      "message": "I'm on the Starter plan and I'm interested in moving to the Professional plan."
    },
    {
      "role": "agent",
      "message": "Great choice! The Professional plan includes advanced analytics, priority support, and up to 10 team members. It's priced at $49 per month. Would you like to proceed with the upgrade?"
    },
    {
      "role": "user",
      "message": "Yes, that sounds good. Please go ahead and upgrade my account."
    },
    {
      "role": "agent",
      "message": "Your account has been successfully upgraded to the Professional plan. You'll have immediate access to all the new features. Is there anything else I can help you with?"
    }
  ],
  "messages_omitted": false
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary';
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/21m00Tcm4TlvDq8ikWAM/summary")! as URL,
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
