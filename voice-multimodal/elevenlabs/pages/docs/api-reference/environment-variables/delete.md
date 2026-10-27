---
title: "Delete environment variable"
source: https://elevenlabs.io/docs/api-reference/environment-variables/delete.md
path: docs/api-reference/environment-variables/delete
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete environment variable

DELETE https://api.elevenlabs.io/v1/convai/environment-variables/{env_var_id}

Delete an environment variable and its values in all environments. WARNING: Agents are not checked. A variable that an agent still uses (custom LLM, webhooks or cloud storage export, on any branch or version) is deleted anyway, and that agent's conversations then fail. The delete is only rejected while tools, MCP servers or the workspace conversation initiation webhook use the variable.

Reference: https://elevenlabs.io/docs/api-reference/environment-variables/delete

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `env_var_id` (string, required)

## Response

### 204

Environment variable deleted

## Errors

### 404 Not Found Error

Environment variable not found

- `any`

### 409 Conflict Error

Environment variable is still in use

- `any`

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

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id"

response = requests.delete(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id';
const options = {method: 'DELETE'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

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
