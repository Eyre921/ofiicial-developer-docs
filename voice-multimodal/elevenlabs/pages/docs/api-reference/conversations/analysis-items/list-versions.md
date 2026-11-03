---
title: "List analysis item versions"
source: https://elevenlabs.io/docs/api-reference/conversations/analysis-items/list-versions.md
path: docs/api-reference/conversations/analysis-items/list-versions
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List analysis item versions

GET https://api.elevenlabs.io/v1/convai/analysis-items/{analysis_item_id}/versions

List the published versions of an analysis item, newest first.

Reference: https://elevenlabs.io/docs/api-reference/conversations/analysis-items/list-versions

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `analysis_item_id` (string, required) — ID of the requested analysis item.

### Query parameters

- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `versions` (list of AnalysisItemVersionResponseModel, required)
- `current_version_id` (string, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AnalysisItemVersionResponseModel

- `id` (string, required)
- `version_number` (integer, required)
- `created_at_unix_secs` (integer, required)
- `definition` (AnalysisItemVersionResponseModelDefinition, required)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### AnalysisItemVersionResponseModelDefinition

- `kind`: `data_collection` (UserDataCollectionAnalysisItem)
  - `name` (string, required)
  - `value_schema` (DataCollectionValueSchema, required) — Type/description/enum describing the value to extract.
  - `llm` (enum, optional, nullable) — LLM to use for this item. If unset, the attaching agent's analysis_llm default is used.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `gemini-4-argon`, `claude-sonnet-4-5`, `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-5-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-haiku-5-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `deepseek-v41-flash`, `nemotron-35-super-vl-nvfp4`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `source` ("user", optional, default: user)
- `kind`: `evaluation` (UserEvaluationAnalysisItem)
  - `conversation_goal_prompt` (string, required) — The prompt used to evaluate the conversation.
  - `name` (string, required)
  - `llm` (enum, optional, nullable) — LLM to use for this item. If unset, the attaching agent's analysis_llm default is used.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `gemini-4-argon`, `claude-sonnet-4-5`, `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-5-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-haiku-5-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `deepseek-v41-flash`, `nemotron-35-super-vl-nvfp4`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `scoring` (UserEvaluationAnalysisItemScoring, optional) — How this criterion is scored (binary or numeric_uniform).
  - `source` ("user", optional, default: user)
  - `use_knowledge_base` (boolean, optional, default: false) — Whether the attaching agent's knowledge base is used when evaluating this criterion.

### ValidationErrorLocItems

- string
- integer

### DataCollectionValueSchema

Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.

- `type` (DataCollectionValueSchemaType, required)
- `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
- `enum` (list of string, optional, nullable) — List of allowed string values for string type parameters
- `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
- `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
- `allowed_values` (AllowedValues, optional, nullable) — Server-side rejection guard for an LLM-provided value: the runtime rejects any value outside the permitted set this object names, and the set is not advertised to the LLM as an enum. Only supported when the value source is `description`; combining it with dynamic_variable, is_system_provided, constant_value, or is_omitted is rejected.
- `constant_value` (DataCollectionValueSchemaConstantValue, optional, nullable, default: ) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
- `allowed_values_dynamic_variable` (string, optional, default: , deprecated) — DEPRECATED: use `allowed_values` instead. When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable (must be a JSON array such as ["ws_alpha", "ws_beta"]). Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.

### UserEvaluationAnalysisItemScoring

How this criterion is scored (binary or numeric_uniform).

- `mode`: `binary` (BinaryScoring)
- `mode`: `numeric_uniform` (NumericUniformScoring)
  - `max_score` (integer, required)
  - `instructions` (string, optional, nullable)

### DataCollectionValueSchemaType

- enum
  - Allowed values: `boolean`, `string`, `integer`, `number`
- list of string

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### DataCollectionValueSchemaConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

- string
- integer
- double
- boolean

## Examples

**Response**

```json
{
  "versions": [
    {
      "id": "string",
      "version_number": 1,
      "created_at_unix_secs": 1,
      "definition": {
        "kind": "evaluation",
        "conversation_goal_prompt": "string",
        "name": "string",
        "llm": "gpt-4o-mini",
        "scoring": {
          "mode": "binary"
        },
        "source": "user",
        "use_knowledge_base": false
      }
    }
  ],
  "current_version_id": "string",
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions';
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

	url := "https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions"

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

url = URI("https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/analysis-items/analysis_item_id/versions")! as URL,
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
