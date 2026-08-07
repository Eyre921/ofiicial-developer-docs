---
title: "Think Models"
source: https://developers.deepgram.com/reference/voice-agent/think-models.md
path: reference/voice-agent/think-models
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Think Models

GET https://agent.deepgram.com/v1/agent/settings/think/models

Retrieves the available think models that can be used for AI agent processing

Reference: https://developers.deepgram.com/reference/voice-agent/think-models

## Response

### 200

List of available think models

- `models` (list of object or object or object or object or object, required)
  - object
    - `id` (enum, required) — The unique identifier of the OpenAI model
      - Allowed values: `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-4o`, `gpt-4o-mini`
    - `name` (string, required) — The display name of the model
    - `provider` (any, required) — The provider of the model
  - object
    - `id` (enum, required) — The unique identifier of the Anthropic model
      - Allowed values: `claude-3-5-haiku-latest`, `claude-sonnet-4-20250514`
    - `name` (string, required) — The display name of the model
    - `provider` (any, required) — The provider of the model
  - object
    - `id` (enum, required) — The unique identifier of the Google model
      - Allowed values: `gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`
    - `name` (string, required) — The display name of the model
    - `provider` (any, required) — The provider of the model
  - object
    - `id` (enum, required) — The unique identifier of the Groq model
      - Allowed values: `openai/gpt-oss-20b`
    - `name` (string, required) — The display name of the model
    - `provider` (any, required) — The provider of the model
  - object
    - `id` (string, required) — The unique identifier of the AWS Bedrock model (any model string accepted for BYO LLMs)
    - `name` (string, required) — The display name of the model
    - `provider` (any, required) — The provider of the model

## Examples

**Response**

```json
{
  "models": [
    {
      "id": "gpt-5",
      "name": "GPT-5",
      "provider": "open_ai"
    }
  ]
}
```

**SDK Code**

```python List supported models
import requests

url = "https://agent.deepgram.com/v1/agent/settings/think/models"
response = requests.get(url)

print(response.json())

```

```typescript List supported models
const res = await fetch(
  "https://agent.deepgram.com/v1/agent/settings/think/models",
);
const data = await res.json();
console.log(data);

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://agent.deepgram.com/v1/agent/settings/think/models"

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

url = URI("https://agent.deepgram.com/v1/agent/settings/think/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://agent.deepgram.com/v1/agent/settings/think/models")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://agent.deepgram.com/v1/agent/settings/think/models');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://agent.deepgram.com/v1/agent/settings/think/models");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://agent.deepgram.com/v1/agent/settings/think/models")! as URL,
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
