---
title: "List tests"
source: https://elevenlabs.io/docs/api-reference/tests/list.md
path: docs/api-reference/tests/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tests

GET https://api.elevenlabs.io/v1/convai/agent-testing

Lists all agent response tests with pagination support and optional search filtering.

Reference: https://elevenlabs.io/docs/api-reference/tests/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 30) — How many Tests to return at maximum. Can not exceed 100, defaults to 30.
- `search` (string, optional, nullable) — Search query to filter tests by name.
- `parent_folder_id` (string, optional, nullable) — Filter by parent folder ID. Use 'root' to get items in the root folder.
- `types` (list of enum, optional, nullable) — If present, the endpoint will return only tests/folders of the given types.
  - Allowed values: `llm`, `tool`, `simulation`, `folder`
- `include_folders` (boolean, optional, nullable, deprecated) — Deprecated. Use the `types` query param and include `folder` instead.
- `sort_mode` (enum, optional, default: default) — Sort mode for listing tests. Use 'folders_first' to place folders before tests.
  - Allowed values: `default`, `folders_first`
- `sharing_mode` (enum, optional) — Filter test visibility. Use `shared_with_me` to return only tests/folders shared with the current user that they did not create.
  - Allowed values: `all`, `shared_with_me`

## Response

### 200

Successful Response

- `tests` (list of object, required)
  - `id` (string, required) — The ID of the test
  - `name` (string, required) — Name of the test
  - `created_at_unix_secs` (integer, required) — Creation time of the test in unix seconds
  - `last_updated_at_unix_secs` (integer, required) — Last update time of the test in unix seconds
  - `type` (enum, required) — Type of the test or entity
    - Allowed values: `llm`, `tool`, `simulation`, `folder`
  - `access_info` (object, optional, nullable) — The access information of the test
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
  - `entity_type` (enum, optional, default: test) — The type of entity (test or folder)
    - Allowed values: `test`, `folder`
  - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder
  - `folder_path` (list of object, optional) — The folder path segments from root to this entity
    - `id` (string, required)
    - `name` (string, optional, default: )
  - `children_count` (integer, optional, nullable) — Number of direct children (tests and subfolders) for folders only
  - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Channel the test simulates the conversation as. Null for folders or default behavior.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "tests": [
    {
      "id": "string",
      "name": "string",
      "created_at_unix_secs": 1,
      "last_updated_at_unix_secs": 1,
      "type": "llm",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      },
      "entity_type": "test",
      "folder_parent_id": "string",
      "folder_path": [
        {
          "id": "string",
          "name": ""
        }
      ],
      "children_count": 1,
      "conversation_initiation_source": "unknown"
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing")! as URL,
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
