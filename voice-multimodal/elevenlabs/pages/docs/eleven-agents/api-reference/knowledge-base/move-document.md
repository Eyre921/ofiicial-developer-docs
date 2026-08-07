---
title: "Move document"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/move-document.md
path: docs/eleven-agents/api-reference/knowledge-base/move-document
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Move document

POST https://api.elevenlabs.io/v1/convai/knowledge-base/{document_id}/move
Content-Type: application/json

Moves the entity from one folder to another.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/move-document

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `document_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

### Body (application/json)

- `move_to` (string, optional) — The folder to move the entities to. If not set, the entities will be moved to the root folder.

## Examples

**Request**

```json
{
  "move_to": "project_documents/marketing_campaigns"
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
    await client.conversationalAi.knowledgeBase.documents.move("21m00Tcm4TlvDq8ikWAM", {
        moveTo: "project_documents/marketing_campaigns",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.move(
    document_id="21m00Tcm4TlvDq8ikWAM",
    move_to="project_documents/marketing_campaigns",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move"

	payload := strings.NewReader("{\n  \"move_to\": \"project_documents/marketing_campaigns\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"move_to\": \"project_documents/marketing_campaigns\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move")
  .header("Content-Type", "application/json")
  .body("{\n  \"move_to\": \"project_documents/marketing_campaigns\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move', [
  'body' => '{
  "move_to": "project_documents/marketing_campaigns"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"move_to\": \"project_documents/marketing_campaigns\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["move_to": "project_documents/marketing_campaigns"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/move")! as URL,
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
