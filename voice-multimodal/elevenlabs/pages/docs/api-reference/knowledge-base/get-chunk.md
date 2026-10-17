---
title: "Get document chunk"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-chunk.md
path: docs/api-reference/knowledge-base/get-chunk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get document chunk

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/chunk/{chunk_id}

Get details about a specific documentation part used by RAG.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/get-chunk

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.
- `chunk_id` (string, required) — The id of a document RAG chunk from the knowledge base.

### Query parameters

- `embedding_model` (enum, optional, nullable, default: e5_mistral_7b_instruct) — The embedding model used to retrieve the chunk.
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`

## Response

### 200

Successful Response

- `id` (string, required)
- `name` (string, required)
- `content` (string, required)

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

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "21m00Tcm4TlvDq8ikWAM_chunk_1",
  "name": "Introduction to ElevenLabs Conversational AI",
  "content": "ElevenLabs Conversational AI enables developers to build intelligent voice agents that can engage in natural, real-time conversations. The platform supports a wide range of use cases including customer support, virtual assistants, and interactive storytelling. Agents can be configured with custom knowledge bases, tools, and personas to suit specific application needs."
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1"

querystring = {"embedding_model":"e5_mistral_7b_instruct"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct';
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/1?embedding_model=e5_mistral_7b_instruct")! as URL,
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
