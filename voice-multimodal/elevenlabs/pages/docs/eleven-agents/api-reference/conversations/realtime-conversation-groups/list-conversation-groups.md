---
title: "List realtime conversation groups"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/list-conversation-groups.md
path: docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/list-conversation-groups
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List realtime conversation groups

GET https://api.elevenlabs.io/v1/convai/realtime/conversation-groups

List the realtime conversation groups the current user can view.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/realtime-conversation-groups/list-conversation-groups

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — How many conversation groups to return. Can not exceed 100.
- `search` (string, optional) — If specified, only conversation groups whose title or description contains this string (case-insensitive) are returned.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `conversation_groups` (list of RealtimeConversationGroupResponseModel, required)
- `next_cursor` (string, optional) — Cursor to pass to the next request to fetch the following page.
- `has_more` (boolean, optional, default: false) — Whether more conversation groups are available beyond this page.

## Errors

### 422 Realtime List Conversation Groups Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### RealtimeConversationGroupResponseModel

- `id` (string, required)
- `title` (string, required)
- `access_info` (ResourceAccessInfo, required)
- `sharing` (RealtimeConversationGroupSharingSummary, required) — How widely a group is shared, besides its owner and workspace admins (who always have access).
- `created_at_unix_secs` (integer, required)
- `description` (string, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

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

### ValidationErrorLocItem

- string
- integer

## Examples

**Response**

```json
{
  "conversation_groups": [
    {
      "id": "id",
      "title": "title",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      },
      "sharing": {
        "people_count": 1
      },
      "created_at_unix_secs": 1,
      "description": "description"
    }
  ],
  "next_cursor": "next_cursor",
  "has_more": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups"

querystring = {"cursor":"cursor","page_size":"1","search":"search"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search';
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

	url := "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search"

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

url = URI("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/realtime/conversation-groups?cursor=cursor&page_size=1&search=search")! as URL,
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
