---
title: "Analyze Text"
source: https://developers.deepgram.com/reference/text-intelligence/analyze-text.md
path: reference/text-intelligence/analyze-text
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Analyze Text

POST https://api.deepgram.com/v1/read
Content-Type: application/json

Analyze text content using Deepgrams text analysis API

Reference: https://developers.deepgram.com/reference/text-intelligence/analyze-text

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`
- `Authorization` header (bearer token, required) — Use `Authorization: Bearer <JWT>` Example: `Authorization: Bearer eyJhbGciOiJ...`

## Request

### Query parameters

- `callback` (string, optional) — URL to which we'll make the callback request
- `callback_method` (enum, optional, default: POST) — HTTP method by which the callback request will be made
  - Allowed values: `POST`, `PUT`
- `sentiment` (boolean, optional, default: false) — Recognizes the sentiment throughout a transcript or text
- `summarize` (enum or boolean, optional) — Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only.
- `tag` (string or list of string, optional) — Label your requests for the purpose of identification during usage reporting
- `topics` (boolean, optional, default: false) — Detect topics throughout a transcript or text
- `custom_topic` (string or list of string, optional) — Custom topics you want the model to detect within your input audio or text if present Submit up to `100`.
- `custom_topic_mode` (enum, optional, default: extended) — Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param
  - Allowed values: `extended`, `strict`
- `intents` (boolean, optional, default: false) — Recognizes speaker intent throughout a transcript or text
- `custom_intent` (string or list of string, optional) — Custom intents you want the model to detect within your input audio if present
- `custom_intent_mode` (enum, optional, default: extended) — Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.
  - Allowed values: `extended`, `strict`
- `language` (string, optional, default: en) — The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available

### Body (application/json)

- `object or object`
  - ReadV1RequestUrl
    - `url` (string, required) — A URL pointing to the text source
  - ReadV1RequestText
    - `text` (string, required) — The plain text to analyze

## Response

### 200

Successful text analysis

- `metadata` (object, required)
  - `metadata` (object, optional)
    - `request_id` (string, optional)
    - `created` (string, optional)
    - `language` (string, optional)
    - `summary_info` (object, optional)
      - `model_uuid` (string, optional)
      - `input_tokens` (integer, optional)
      - `output_tokens` (integer, optional)
    - `sentiment_info` (object, optional)
      - `model_uuid` (string, optional)
      - `input_tokens` (integer, optional)
      - `output_tokens` (integer, optional)
    - `topics_info` (object, optional)
      - `model_uuid` (string, optional)
      - `input_tokens` (integer, optional)
      - `output_tokens` (integer, optional)
    - `intents_info` (object, optional)
      - `model_uuid` (string, optional)
      - `input_tokens` (integer, optional)
      - `output_tokens` (integer, optional)
- `results` (object, required)
  - `summary` (object, optional) — Output whenever `summary=true` is used
    - `results` (object, optional)
      - `summary` (object, optional)
        - `text` (string, optional)
  - `topics` (object, optional) — Output whenever `topics=true` is used
    - `results` (object, optional)
      - `topics` (object, optional)
        - `segments` (list of object, optional)
          - `text` (string, optional)
          - `start_word` (double, optional)
          - `end_word` (double, optional)
          - `topics` (list of object, optional)
            - `topic` (string, optional)
            - `confidence_score` (float, optional)
  - `intents` (object, optional) — Output whenever `intents=true` is used
    - `results` (object, optional)
      - `intents` (object, optional)
        - `segments` (list of object, optional)
          - `text` (string, optional)
          - `start_word` (double, optional)
          - `end_word` (double, optional)
          - `intents` (list of object, optional)
            - `intent` (string, optional)
            - `confidence_score` (float, optional)
  - `sentiments` (object, optional) — Output whenever `sentiment=true` is used
    - `segments` (list of object, optional)
      - `text` (string, optional)
      - `start_word` (double, optional)
      - `end_word` (double, optional)
      - `sentiment` (string, optional)
      - `sentiment_score` (double, optional)
    - `average` (object, optional)
      - `sentiment` (string, optional)
      - `sentiment_score` (double, optional)

## Examples

**Request**

```json
{
  "url": "https://example.com/audio/interview-episode1.mp3"
}
```

**Response**

```json
{
  "metadata": {
    "metadata": {
      "request_id": "d04af392-db11-4c1d-83e1-20e34f0b8999",
      "created": "2024-11-18T23:47:44.674Z",
      "language": "en",
      "summary_info": {
        "model_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "input_tokens": 350,
        "output_tokens": 75
      },
      "sentiment_info": {
        "model_uuid": "f1e2d3c4-b5a6-7890-cdef-1234567890ab",
        "input_tokens": 350,
        "output_tokens": 10
      },
      "topics_info": {
        "model_uuid": "123e4567-e89b-12d3-a456-426614174000",
        "input_tokens": 350,
        "output_tokens": 20
      },
      "intents_info": {
        "model_uuid": "0a1b2c3d-4e5f-6789-abcd-ef0123456789",
        "input_tokens": 350,
        "output_tokens": 15
      }
    }
  },
  "results": {
    "summary": {
      "results": {
        "summary": {
          "text": "This transcript highlights the significance of the first all-female spacewalk and honors the women pioneers who paved the way."
        }
      }
    },
    "topics": {
      "results": {
        "topics": {
          "segments": [
            {
              "text": "And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
              "start_word": 32,
              "end_word": 69,
              "topics": [
                {
                  "topic": "Spacewalk",
                  "confidence_score": 0.91581345
                }
              ]
            }
          ]
        }
      }
    },
    "intents": {
      "results": {
        "intents": {
          "segments": [
            {
              "text": "If you found this valuable, you can subscribe to the show on spotify or your favorite podcast app.",
              "start_word": 354,
              "end_word": 414,
              "intents": [
                {
                  "intent": "Encourage podcasting",
                  "confidence_score": 0.0038975573
                }
              ]
            }
          ]
        }
      }
    },
    "sentiments": {
      "segments": [
        {
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal. And, um, I think if it_signf",
          "start_word": 0,
          "end_word": 69,
          "sentiment": "positive",
          "sentiment_score": 0.5810546875
        }
      ],
      "average": {
        "sentiment": "positive",
        "sentiment_score": 0.5810185185185185
      }
    }
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/read"

payload = { "url": "https://example.com/audio/interview-episode1.mp3" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/read';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"url":"https://example.com/audio/interview-episode1.mp3"}'
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

	url := "https://api.deepgram.com/v1/read"

	payload := strings.NewReader("{\n  \"url\": \"https://example.com/audio/interview-episode1.mp3\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v1/read")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://example.com/audio/interview-episode1.mp3\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/read")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://example.com/audio/interview-episode1.mp3\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/read', [
  'body' => '{
  "url": "https://example.com/audio/interview-episode1.mp3"
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/read");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://example.com/audio/interview-episode1.mp3\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["url": "https://example.com/audio/interview-episode1.mp3"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/read")! as URL,
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
