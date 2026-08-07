---
title: "Create tag"
source: https://elevenlabs.io/docs/api-reference/conversations/tags/create.md
path: docs/api-reference/conversations/tags/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create tag

POST https://api.elevenlabs.io/v1/convai/tags
Content-Type: application/json

Create a new conversation tag for the workspace.

Reference: https://elevenlabs.io/docs/api-reference/conversations/tags/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `title` (string, required) — Display title of the tag.
- `description` (string, optional, nullable) — Optional free-text description.

## Response

### 200

Successful Response

- `tag_id` (string, required)
- `workspace_id` (string, required)
- `owner_user_id` (string, required)
- `title` (string, required)
- `description` (string, required, nullable)
- `created_at_unix_secs` (integer, required)

## Examples

**Request**

```json
{
  "title": "Urgent Support"
}
```

**Response**

```json
{
  "tag_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef56gh78",
  "workspace_id": "workspace_987654321",
  "owner_user_id": "user_123456789",
  "title": "Urgent Support",
  "description": "Tag for conversations requiring immediate attention",
  "created_at_unix_secs": 1712000000
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.tags.create({
        title: "Urgent Support",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.tags.create(
    title="Urgent Support",
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

	url := "https://api.elevenlabs.io/v1/convai/tags"

	payload := strings.NewReader("{\n  \"title\": \"Urgent Support\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/tags")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"title\": \"Urgent Support\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/tags")
  .header("Content-Type", "application/json")
  .body("{\n  \"title\": \"Urgent Support\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/tags', [
  'body' => '{
  "title": "Urgent Support"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tags");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"title\": \"Urgent Support\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["title": "Urgent Support"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tags")! as URL,
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
