---
title: "List test invocations"
source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/list.md
path: docs/api-reference/tests/test-invocations/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List test invocations

GET https://api.elevenlabs.io/v1/convai/test-invocations

Lists all test invocations with pagination support and optional search filtering.

Reference: https://elevenlabs.io/docs/api-reference/tests/test-invocations/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, optional, nullable) — Filter by agent ID
- `page_size` (integer, optional, default: 30) — How many Tests to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `results` (list of object, required)
  - `id` (string, required) — The ID of the test invocation
  - `created_at_unix_secs` (integer, required) — Creation time of the test invocation in unix seconds
  - `test_run_count` (integer, required) — Number of test runs in this invocation
  - `passed_count` (integer, required) — Number of test runs that passed
  - `failed_count` (integer, required) — Number of test runs that failed
  - `pending_count` (integer, required) — Number of test runs that are pending
  - `title` (string, required) — Title of the test invocation - either the single test name or count of tests
  - `agent_id` (string, optional, nullable) — The ID of the agent this test invocation belongs to
  - `branch_id` (string, optional, nullable) — The ID of the branch this test invocation was run on
  - `access_info` (object, optional, nullable) — The access information of the test invocation
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
  - `repeat_count` (integer, optional, default: 1) — Number of times each test was repeated in this invocation
- `has_more` (boolean, required) — Whether there are more results available
- `meta` (object, optional)
  - `total` (integer, optional, nullable)
  - `page` (integer, optional, nullable)
  - `page_size` (integer, optional, nullable)
- `next_cursor` (string, optional, nullable) — Cursor for the next page of results

## Examples

**Response**

```json
{
  "results": [
    {
      "id": "string",
      "created_at_unix_secs": 1,
      "test_run_count": 1,
      "passed_count": 1,
      "failed_count": 1,
      "pending_count": 1,
      "title": "string",
      "agent_id": "string",
      "branch_id": "string",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      },
      "repeat_count": 1
    }
  ],
  "has_more": true,
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 1
  },
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.invocations.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.invocations.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/test-invocations"

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

url = URI("https://api.elevenlabs.io/v1/convai/test-invocations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/test-invocations")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/test-invocations');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations")! as URL,
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
