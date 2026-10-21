---
title: "Review A Merge Proposal"
source: https://elevenlabs.io/docs/api-reference/agents/merge-proposals/submit-review.md
path: docs/api-reference/agents/merge-proposals/submit-review
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Review A Merge Proposal

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}/reviews
Content-Type: application/json

Approve a merge_proposal or request changes on it. A user's latest review replaces their previous one. Non-admins need an approval from another user before the merge is allowed.

Reference: https://elevenlabs.io/docs/api-reference/agents/merge-proposals/submit-review

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `merge_proposal_id` (string, required) — Unique identifier for the merge_proposal.

### Body (application/json)

This endpoint expects a Body_Review_a_merge_proposal_v1_convai_agents__agent_id__merge_proposals__merge_proposal_id__reviews_post.

- `state` (enum, required) — The review verdict.
  - Allowed values: `approved`, `changes_requested`
- `comment` (string, optional, default: ) — Optional comment to leave with the review.

## Response

### 200

Successful Response

- `id` (string, required)
- `agent_id` (string, required)
- `source_branch_id` (string, required)
- `target_branch_id` (string, required)
- `source_tip_version_id_at_creation` (string, required)
- `title` (string, required)
- `created_at` (integer, required)
- `updated_at` (integer, required)
- `description` (string, optional, default: )
- `requested_reviewer_user_ids` (list of string, optional)
- `reviews` (list of MergeProposalReview, optional)
- `comments` (list of MergeProposalComment, optional)
- `outcome` (AgentMergeProposalResponseOutcome, optional)
- `author_user_id` (string, optional, nullable) — User ID of the merge_proposal's author.
- `access_info` (ResourceAccessInfo, optional, nullable) — Access information for the merge_proposal, including creator.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### MergeProposalReview

- `user_id` (string, required)
- `state` (enum, required)
  - Allowed values: `approved`, `changes_requested`
- `submitted_at` (integer, required)
- `comment` (string, optional, default: )
- `reviewer_role` (enum, optional, nullable)
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`

### MergeProposalComment

- `id` (string, required)
- `user_id` (string, required)
- `body` (string, required)
- `created_at` (integer, required)

### AgentMergeProposalResponseOutcome

- `status`: `closed` (ClosedOutcome)
  - `at` (integer, required)
  - `by_user_id` (string, required, nullable)
  - `reason` (enum, required)
    - Allowed values: `withdrawn`, `rejected`, `branch_archived`
- `status`: `merged` (MergedOutcome)
  - `at` (integer, required)
  - `by_user_id` (string, required, nullable)
  - `version_id` (string, required)
- `status`: `open` (OpenOutcome)

### ResourceAccessInfo

- `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
- `creator_name` (string, required) — Name of the agent's creator
- `creator_email` (string, required) — Email of the agent's creator
- `role` (enum, required) — The role of the user making the request
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
  - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Request**

```json
{
  "state": "approved"
}
```

**Response**

```json
{
  "id": "string",
  "agent_id": "string",
  "source_branch_id": "string",
  "target_branch_id": "string",
  "source_tip_version_id_at_creation": "string",
  "title": "string",
  "created_at": 1,
  "updated_at": 1,
  "description": "",
  "requested_reviewer_user_ids": [
    "string"
  ],
  "reviews": [
    {
      "user_id": "string",
      "state": "approved",
      "submitted_at": 1,
      "comment": "",
      "reviewer_role": "admin"
    }
  ],
  "comments": [
    {
      "id": "string",
      "user_id": "string",
      "body": "string",
      "created_at": 1
    }
  ],
  "outcome": {
    "status": "open"
  },
  "author_user_id": "string",
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews"

payload = { "state": "approved" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"state":"approved"}'
};

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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews"

	payload := strings.NewReader("{\n  \"state\": \"approved\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"state\": \"approved\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews")
  .header("Content-Type", "application/json")
  .body("{\n  \"state\": \"approved\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews', [
  'body' => '{
  "state": "approved"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"state\": \"approved\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["state": "approved"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj/reviews")! as URL,
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
