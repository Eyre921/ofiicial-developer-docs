---
title: "Create knowledge base document from text"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-text.md
path: docs/api-reference/knowledge-base/create-from-text
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create knowledge base document from text

POST https://api.elevenlabs.io/v1/convai/knowledge-base/text
Content-Type: application/json

Create a knowledge base document containing the provided text.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-text

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `text` (string, required) — Text content to be added to the knowledge base.
- `name` (string, optional, nullable) — A custom, human-readable name for the document.
- `parent_folder_id` (string, optional, nullable) — If set, the created document or folder will be placed inside the given folder.

## Response

### 200

Successful Response

- `id` (string, required)
- `name` (string, required)
- `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
  - `id` (string, required)

## Examples

**Request**

```json
{
  "text": "ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications."
}
```

**Response**

```json
{
  "id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
  "name": "ElevenLabs AI Voice Tech Overview",
  "folder_path": [
    {
      "id": "folder1234abcd5678ef"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.createFromText({
        text: "ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.create_from_text(
    text="ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/text"

	payload := strings.NewReader("{\n  \"text\": \"ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/text")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/text', [
  'body' => '{
  "text": "ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/text");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["text": "ElevenLabs provides advanced AI-driven text-to-speech and voice synthesis services to enhance conversational applications."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/text")! as URL,
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
