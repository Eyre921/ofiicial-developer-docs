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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/read:
    post:
      operationId: analyze
      summary: Analyze text content
      description: Analyze text content using Deepgrams text analysis API
      tags:
        - text
      parameters:
        - name: callback
          in: query
          description: URL to which we'll make the callback request
          required: false
          schema:
            type: string
        - name: callback_method
          in: query
          description: HTTP method by which the callback request will be made
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersCallbackMethod'
            default: POST
        - name: sentiment
          in: query
          description: Recognizes the sentiment throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: summarize
          in: query
          description: >-
            Summarize content. For Listen API, supports string version option.
            For Read API, accepts boolean only.
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersSummarize'
        - name: tag
          in: query
          description: >-
            Label your requests for the purpose of identification during usage
            reporting
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersTag'
        - name: topics
          in: query
          description: Detect topics throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: custom_topic
          in: query
          description: >-
            Custom topics you want the model to detect within your input audio
            or text if present Submit up to `100`.
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersCustomTopic'
        - name: custom_topic_mode
          in: query
          description: >-
            Sets how the model will interpret strings submitted to the
            `custom_topic` param. When `strict`, the model will only return
            topics submitted using the `custom_topic` param. When `extended`,
            the model will return its own detected topics in addition to those
            submitted using the `custom_topic` param
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersCustomTopicMode'
            default: extended
        - name: intents
          in: query
          description: Recognizes speaker intent throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: custom_intent
          in: query
          description: >-
            Custom intents you want the model to detect within your input audio
            if present
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersCustomIntent'
        - name: custom_intent_mode
          in: query
          description: >-
            Sets how the model will interpret intents submitted to the
            `custom_intent` param. When `strict`, the model will only return
            intents submitted using the `custom_intent` param. When `extended`,
            the model will return its own detected intents in the
            `custom_intent` param.
          required: false
          schema:
            $ref: '#/components/schemas/V1ReadPostParametersCustomIntentMode'
            default: extended
        - name: language
          in: query
          description: >-
            The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that
            hints at the primary spoken language. Depending on the Model and API
            endpoint you choose only certain languages are available
          required: false
          schema:
            type: string
            default: en
        - name: Authorization
          in: header
          description: |
            Use `Authorization: Token <API_KEY>`
            Example: `Authorization: Token 12345abcdef`
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful text analysis
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReadV1Response'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: Analyze a text file
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ReadV1Request'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    V1ReadPostParametersCallbackMethod:
      type: string
      enum:
        - POST
        - PUT
      default: POST
      title: V1ReadPostParametersCallbackMethod
    V1ReadPostParametersSummarize0:
      type: string
      enum:
        - v2
      title: V1ReadPostParametersSummarize0
    V1ReadPostParametersSummarize:
      oneOf:
        - $ref: '#/components/schemas/V1ReadPostParametersSummarize0'
        - type: boolean
          default: false
      title: V1ReadPostParametersSummarize
    V1ReadPostParametersTag:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ReadPostParametersTag
    V1ReadPostParametersCustomTopic:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ReadPostParametersCustomTopic
    V1ReadPostParametersCustomTopicMode:
      type: string
      enum:
        - extended
        - strict
      default: extended
      title: V1ReadPostParametersCustomTopicMode
    V1ReadPostParametersCustomIntent:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ReadPostParametersCustomIntent
    V1ReadPostParametersCustomIntentMode:
      type: string
      enum:
        - extended
        - strict
      default: extended
      title: V1ReadPostParametersCustomIntentMode
    ReadV1RequestUrl:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: A URL pointing to the text source
      required:
        - url
      title: ReadV1RequestUrl
    ReadV1RequestText:
      type: object
      properties:
        text:
          type: string
          description: The plain text to analyze
      required:
        - text
      title: ReadV1RequestText
    ReadV1Request:
      oneOf:
        - $ref: '#/components/schemas/ReadV1RequestUrl'
        - $ref: '#/components/schemas/ReadV1RequestText'
      title: ReadV1Request
    ReadV1ResponseMetadataMetadataSummaryInfo:
      type: object
      properties:
        model_uuid:
          type: string
          format: uuid
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ReadV1ResponseMetadataMetadataSummaryInfo
    ReadV1ResponseMetadataMetadataSentimentInfo:
      type: object
      properties:
        model_uuid:
          type: string
          format: uuid
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ReadV1ResponseMetadataMetadataSentimentInfo
    ReadV1ResponseMetadataMetadataTopicsInfo:
      type: object
      properties:
        model_uuid:
          type: string
          format: uuid
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ReadV1ResponseMetadataMetadataTopicsInfo
    ReadV1ResponseMetadataMetadataIntentsInfo:
      type: object
      properties:
        model_uuid:
          type: string
          format: uuid
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ReadV1ResponseMetadataMetadataIntentsInfo
    ReadV1ResponseMetadataMetadata:
      type: object
      properties:
        request_id:
          type: string
          format: uuid
        created:
          type: string
          format: date-time
        language:
          type: string
        summary_info:
          $ref: '#/components/schemas/ReadV1ResponseMetadataMetadataSummaryInfo'
        sentiment_info:
          $ref: '#/components/schemas/ReadV1ResponseMetadataMetadataSentimentInfo'
        topics_info:
          $ref: '#/components/schemas/ReadV1ResponseMetadataMetadataTopicsInfo'
        intents_info:
          $ref: '#/components/schemas/ReadV1ResponseMetadataMetadataIntentsInfo'
      title: ReadV1ResponseMetadataMetadata
    ReadV1ResponseMetadata:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/ReadV1ResponseMetadataMetadata'
      title: ReadV1ResponseMetadata
    ReadV1ResponseResultsSummaryResultsSummary:
      type: object
      properties:
        text:
          type: string
      title: ReadV1ResponseResultsSummaryResultsSummary
    ReadV1ResponseResultsSummaryResults:
      type: object
      properties:
        summary:
          $ref: '#/components/schemas/ReadV1ResponseResultsSummaryResultsSummary'
      title: ReadV1ResponseResultsSummaryResults
    ReadV1ResponseResultsSummary:
      type: object
      properties:
        results:
          $ref: '#/components/schemas/ReadV1ResponseResultsSummaryResults'
      description: Output whenever `summary=true` is used
      title: ReadV1ResponseResultsSummary
    SharedTopicsResultsTopicsSegmentsItemsTopicsItems:
      type: object
      properties:
        topic:
          type: string
        confidence_score:
          type: string
          title: float
      title: SharedTopicsResultsTopicsSegmentsItemsTopicsItems
    SharedTopicsResultsTopicsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        topics:
          type: array
          items:
            $ref: >-
              #/components/schemas/SharedTopicsResultsTopicsSegmentsItemsTopicsItems
      title: SharedTopicsResultsTopicsSegmentsItems
    SharedTopicsResultsTopics:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedTopicsResultsTopicsSegmentsItems'
      title: SharedTopicsResultsTopics
    SharedTopicsResults:
      type: object
      properties:
        topics:
          $ref: '#/components/schemas/SharedTopicsResultsTopics'
      title: SharedTopicsResults
    SharedTopics:
      type: object
      properties:
        results:
          $ref: '#/components/schemas/SharedTopicsResults'
      description: Output whenever `topics=true` is used
      title: SharedTopics
    SharedIntentsResultsIntentsSegmentsItemsIntentsItems:
      type: object
      properties:
        intent:
          type: string
        confidence_score:
          type: string
          title: float
      title: SharedIntentsResultsIntentsSegmentsItemsIntentsItems
    SharedIntentsResultsIntentsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        intents:
          type: array
          items:
            $ref: >-
              #/components/schemas/SharedIntentsResultsIntentsSegmentsItemsIntentsItems
      title: SharedIntentsResultsIntentsSegmentsItems
    SharedIntentsResultsIntents:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedIntentsResultsIntentsSegmentsItems'
      title: SharedIntentsResultsIntents
    SharedIntentsResults:
      type: object
      properties:
        intents:
          $ref: '#/components/schemas/SharedIntentsResultsIntents'
      title: SharedIntentsResults
    SharedIntents:
      type: object
      properties:
        results:
          $ref: '#/components/schemas/SharedIntentsResults'
      description: Output whenever `intents=true` is used
      title: SharedIntents
    SharedSentimentsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        sentiment:
          type: string
        sentiment_score:
          type: number
          format: double
      title: SharedSentimentsSegmentsItems
    SharedSentimentsAverage:
      type: object
      properties:
        sentiment:
          type: string
        sentiment_score:
          type: number
          format: double
      title: SharedSentimentsAverage
    SharedSentiments:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedSentimentsSegmentsItems'
        average:
          $ref: '#/components/schemas/SharedSentimentsAverage'
      description: Output whenever `sentiment=true` is used
      title: SharedSentiments
    ReadV1ResponseResults:
      type: object
      properties:
        summary:
          $ref: '#/components/schemas/ReadV1ResponseResultsSummary'
        topics:
          $ref: '#/components/schemas/SharedTopics'
        intents:
          $ref: '#/components/schemas/SharedIntents'
        sentiments:
          $ref: '#/components/schemas/SharedSentiments'
      title: ReadV1ResponseResults
    ReadV1Response:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/ReadV1ResponseMetadata'
        results:
          $ref: '#/components/schemas/ReadV1ResponseResults'
      required:
        - metadata
        - results
      description: The standard text response
      title: ReadV1Response
    ErrorResponseTextError:
      type: string
      title: ErrorResponseTextError
    ErrorResponseLegacyError:
      type: object
      properties:
        err_code:
          type: string
          description: The error code
        err_msg:
          type: string
          description: The error message
        request_id:
          type: string
          description: The request ID
      title: ErrorResponseLegacyError
    ErrorResponseModernError:
      type: object
      properties:
        category:
          type: string
          description: The category of the error
        message:
          type: string
          description: A message about the error
        details:
          type: string
          description: A description of the error
        request_id:
          type: string
          description: The unique identifier of the request
      title: ErrorResponseModernError
    ErrorResponse:
      oneOf:
        - $ref: '#/components/schemas/ErrorResponseTextError'
        - $ref: '#/components/schemas/ErrorResponseLegacyError'
        - $ref: '#/components/schemas/ErrorResponseModernError'
      title: ErrorResponse
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: |
        Use `Authorization: Token <API_KEY>`
        Example: `Authorization: Token 12345abcdef`
    JwtAuth:
      type: http
      scheme: bearer
      description: |
        Use `Authorization: Bearer <JWT>`
        Example: `Authorization: Bearer eyJhbGciOiJ...`

```

## Examples



**Request**

```json
{
  "url": "string"
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
        "model_uuid": "string",
        "input_tokens": 1,
        "output_tokens": 1
      },
      "sentiment_info": {
        "model_uuid": "string",
        "input_tokens": 1,
        "output_tokens": 1
      },
      "topics_info": {
        "model_uuid": "string",
        "input_tokens": 1,
        "output_tokens": 1
      },
      "intents_info": {
        "model_uuid": "string",
        "input_tokens": 1,
        "output_tokens": 1
      }
    }
  },
  "results": {
    "summary": {
      "results": {
        "summary": {
          "text": "The summary of the text submitted."
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
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal. And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
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

payload = { "url": "string" }
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
  body: '{"url":"string"}'
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

	payload := strings.NewReader("{\n  \"url\": \"string\"\n}")

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
request.body = "{\n  \"url\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/read")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/read', [
  'body' => '{
  "url": "string"
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
request.AddParameter("application/json", "{\n  \"url\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["url": "string"] as [String : Any]

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
