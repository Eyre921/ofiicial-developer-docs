---
title: "Get realtime conversation group"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/get-conversation-group.md
path: docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/get-conversation-group
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get realtime conversation group

GET https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/{conversation_group_id}

Get a realtime conversation group by id.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/get-conversation-group

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_group_id` (string, required) — The id of a realtime conversation group.

## Response

### 200

Successful Response

- `id` (string, required)
- `title` (string, required)
- `access_info` (ResourceAccessInfo, required)
- `sharing` (RealtimeConversationGroupSharingSummary, required) — How widely a group is shared, besides its owner and workspace admins (who always have access).
- `created_at_unix_secs` (integer, required)
- `description` (string, optional)

## Errors

### 422 Realtime Get Conversation Group Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ResourceAccessInfo

- `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
- `creator_name` (string, required) — Name of the agent's creator
- `creator_email` (string, required) — Email of the agent's creator
- `role` (enum, required) — The role of the user making the request
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
  - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

### RealtimeConversationGroupSharingSummary

How widely a group is shared, besides its owner and workspace admins (who always have access).

- `people_count` (integer, required) — Distinct people besides the owner with access, whether shared directly or through a workspace group they belong to.
- `shared_with_everyone` (boolean, optional, default: false) — Whether every workspace member has access to the group.
- `everyone_role` (enum, optional) — The preset role every workspace member has, when shared with everyone. None for a workspace custom role.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

- string
- integer

## Examples

**Response**

```json
{
  "id": "id",
  "title": "title",
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "sharing": {
    "people_count": 1,
    "shared_with_everyone": true,
    "everyone_role": "admin"
  },
  "created_at_unix_secs": 1,
  "description": "description"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id';
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

	url := "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups/conversation_group_id")! as URL,
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
