---
title: "Bulk delete knowledge base documents"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-delete.md
path: docs/api-reference/knowledge-base/bulk-delete
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bulk delete knowledge base documents

POST https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete
Content-Type: application/json

Delete multiple documents or folders from the knowledge base. Each id succeeds or fails independently.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-delete

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `document_ids` (list of string, required) — The ids of documents or folders from the knowledge base.
- `force` (boolean, optional, default: false) — If set to true, documents or folders will be deleted regardless of whether they are used by any agents and will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.

## Response

### 200

Successful Response

- `map from string to object`
  - `status`: `success` (KnowledgeBaseBulkDeleteSuccessfulResponseModel)
    - `data` (object, required)
      - `id` (string, required)
  - `status`: `failure` (BatchFailureResponseModel)
    - `error_code` (integer, required)
    - `error_message` (string, required)
    - `error_status` (string, required)

## Examples

**Request**

```json
{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
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
    await client.conversationalAi.knowledgeBase.documents.bulkDelete({
        documentIds: [
            "21m00Tcm4TlvDq8ikWAM",
            "31m00Tcm4TlvDq8ikWBM",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.bulk_delete(
    document_ids=[
        "21m00Tcm4TlvDq8ikWAM",
        "31m00Tcm4TlvDq8ikWBM"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete"

	payload := strings.NewReader("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete")
  .header("Content-Type", "application/json")
  .body("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete', [
  'body' => '{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["document_ids": ["21m00Tcm4TlvDq8ikWAM", "31m00Tcm4TlvDq8ikWBM"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-delete")! as URL,
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
