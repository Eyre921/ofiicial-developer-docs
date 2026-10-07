---
title: "List environment variables"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list.md
path: docs/eleven-agents/api-reference/environment-variables/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List environment variables

GET https://api.elevenlabs.io/v1/convai/environment-variables

List all environment variables for the workspace with optional filtering

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional) — Pagination cursor from previous response
- `page_size` (integer, optional, default: 100) — Number of items to return (1-100)
- `label` (string, optional) — Filter by exact label match
- `environment` (string, optional) — Filter to only return variables that have this environment. When specified, the values dict in the response will only contain this environment.
- `type` (enum, optional) — Filter by variable type
  - Allowed values: `string`, `secret`, `auth_connection`

## Response

### 200

Successful Response

- `environment_variables` (list of EnvironmentVariableResponse, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Errors

### 400 Environment Variables List Request Bad Request Error

Invalid environment filter

- `any`

### 422 Environment Variables List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### EnvironmentVariableResponse

- `label` (string, required)
- `created_at_unix_secs` (integer, required)
- `updated_at_unix_secs` (integer, required)
- `type` (enum, required)
  - Allowed values: `string`, `secret`, `auth_connection`
- `id` (string, required)
- `workspace_id` (string, required)
- `values` (EnvironmentVariableResponseValues, required)
- `created_by_user_id` (string, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### EnvironmentVariableResponseValues

### ValidationErrorLocItem

## Examples

**Response**

```json
{
  "environment_variables": [
    {
      "label": "label",
      "created_at_unix_secs": 1,
      "updated_at_unix_secs": 1,
      "type": "string",
      "id": "id",
      "workspace_id": "workspace_id",
      "values": {
        "key": "value"
      },
      "created_by_user_id": "created_by_user_id"
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/environment-variables"

querystring = {"cursor":"cursor","environment":"environment","label":"label","page_size":"1","type":"string"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string';
const options = {method: 'GET'};

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

	url := "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string"

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

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/environment-variables?cursor=cursor&environment=environment&label=label&page_size=1&type=string")! as URL,
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
