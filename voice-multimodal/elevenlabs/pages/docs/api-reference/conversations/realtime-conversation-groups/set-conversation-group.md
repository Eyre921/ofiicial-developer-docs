---
title: "Set realtime conversation group"
source: https://elevenlabs.io/docs/api-reference/conversations/realtime-conversation-groups/set-conversation-group.md
path: docs/api-reference/conversations/realtime-conversation-groups/set-conversation-group
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Set realtime conversation group

PUT https://api.elevenlabs.io/v1/convai/realtime/conversations/{conversation_id}/conversation-group
Content-Type: application/json

Place a realtime conversation in a conversation group, moving it out of its current group if it has one.

Reference: https://elevenlabs.io/docs/api-reference/conversations/realtime-conversation-groups/set-conversation-group

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — The id of a realtime conversation.

### Body (application/json)

This endpoint expects a SetConversationGroupRequestModel.

- `conversation_group_id` (string, required) — The conversation group to place the conversation in. A conversation belongs to at most one group, so this moves it out of any current group.

## Response

### 200

Successful Response

- `any`

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Request**

```json
{
  "conversation_group_id": "string"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group"

payload = { "conversation_group_id": "string" }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"conversation_group_id":"string"}'
};

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

	url := "https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group"

	payload := strings.NewReader("{\n  \"conversation_group_id\": \"string\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"conversation_group_id\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group")
  .header("Content-Type", "application/json")
  .body("{\n  \"conversation_group_id\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group', [
  'body' => '{
  "conversation_group_id": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"conversation_group_id\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["conversation_group_id": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/realtime/conversations/conversation_id/conversation-group")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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
