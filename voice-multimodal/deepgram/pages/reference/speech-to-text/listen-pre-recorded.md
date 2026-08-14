---
title: "Pre-Recorded Audio"
source: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded.md
path: reference/speech-to-text/listen-pre-recorded
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Pre-Recorded Audio

POST https://api.deepgram.com/v1/listen
Content-Type: application/json

Transcribe audio and video using Deepgram's speech-to-text REST API

Reference: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`
- `Authorization` header (bearer token, required) — Use `Authorization: Bearer <JWT>` Example: `Authorization: Bearer eyJhbGciOiJ...`

## Request

### Query parameters

- `callback` (string, optional) — URL to which we'll make the callback request
- `callback_method` (enum, optional, default: POST) — HTTP method by which the callback request will be made
  - Allowed values: `POST`, `PUT`
- `extra` (string or list of string, optional) — Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
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
- `detect_entities` (boolean, optional, default: false) — Identifies and extracts key entities from content in submitted audio
- `detect_language` (boolean or list of string, optional) — Identifies the dominant language spoken in submitted audio
- `diarize` (boolean, optional, default: false, deprecated) — Deprecated: use `diarize_model` instead. Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0.
- `diarize_model` (enum, optional) — Select and enable a specific diarization model version. Specifying this parameter enables diarization and selects the model — you do not need to also set the deprecated `diarize=true` parameter. For batch, supported values are `latest` (currently v2), `v1`, and `v2`. For streaming, supported values are `latest` (currently v1) and `v1`; `v2` returns a validation error on streaming requests.
  - Allowed values: `latest`, `v1`, `v2`
- `dictation` (boolean, optional, default: false) — Dictation mode for controlling formatting with dictated speech
- `encoding` (enum, optional) — Specify the expected encoding of your submitted audio
  - Allowed values: `linear16`, `flac`, `mulaw`, `amr-nb`, `amr-wb`, `opus`, `speex`, `g729`
- `filler_words` (boolean, optional, default: false) — Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
- `keyterm` (list of string, optional) — Key term prompting improves recognition of specialized terminology and brands. Only compatible with Nova-3. `keyterm` accepts plain terms only. Unlike the legacy `keywords` feature, it does not support weights or intensifiers. Appending one (for example, `keyterm=term:0.15`) is not rejected—the weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple separate keyterms, repeat the `keyterm` parameter (for example, `keyterm=term1&keyterm=term2`). To boost one multi-word phrase as a single keyterm, join the words with `%20` or `+` (for example, `keyterm=customer%20service`). Do not separate keyterms with commas, semicolons, or line breaks.
- `keywords` (string or list of string, optional) — Keywords can boost or suppress specialized terminology and brands
- `language` (string, optional, default: en) — The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available
- `measurements` (boolean, optional, default: false) — Spoken measurements will be converted to their corresponding abbreviations
- `model` (enum or string, optional, default: base-general) — AI model used to process submitted audio
- `multichannel` (boolean, optional, default: false) — Transcribe each audio channel independently
- `numerals` (boolean, optional, default: false) — Numerals converts numbers from written format to numerical format
- `paragraphs` (boolean, optional, default: false) — Splits audio into paragraphs to improve transcript readability
- `profanity_filter` (boolean, optional, default: false) — Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely
- `punctuate` (boolean, optional, default: false) — Add punctuation and capitalization to the transcript
- `redact` (string or list of enum, optional, default: false) — Redaction removes sensitive information from your transcripts
- `replace` (string or list of string, optional) — Search for terms or phrases in submitted audio and replaces them
- `search` (string or list of string, optional) — Search for terms or phrases in submitted audio
- `smart_format` (boolean, optional, default: false) — Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability
- `utterances` (boolean, optional, default: false) — Segments speech into meaningful semantic units
- `utt_split` (double, optional, default: 0.8) — Seconds to wait before detecting a pause between words in submitted audio
- `version` (enum or string, optional, default: latest) — Version of an AI model to use
- `mip_opt_out` (boolean, optional, default: false) — Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip

### Body (application/json)

- `url` (string, required)

## Response

### 200

Returns either transcription results, or a request_id when using a callback.

- `object or object`
  - ListenV1Response
    - `metadata` (object, required)
      - `request_id` (string, required)
      - `sha256` (string, required)
      - `created` (string, required)
      - `duration` (double, required)
      - `channels` (integer, required)
      - `models` (list of string, required)
      - `model_info` (object, required)
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
      - `tags` (list of string, optional)
      - `transaction_key` (string, optional, default: deprecated, deprecated)
    - `results` (object, required)
      - `channels` (list of object, required)
        - `search` (list of object, optional)
          - `query` (string, optional)
          - `hits` (list of object, optional)
            - `confidence` (float, optional)
            - `start` (float, optional)
            - `end` (float, optional)
            - `snippet` (string, optional)
        - `alternatives` (list of object, optional)
          - `transcript` (string, optional)
          - `confidence` (float, optional)
          - `words` (list of object, optional)
            - `word` (string, optional)
            - `start` (float, optional)
            - `end` (float, optional)
            - `confidence` (float, optional)
            - `speaker` (integer, optional) — The speaker of the word, present when diarization is enabled
            - `speaker_confidence` (float, optional) — Confidence in the speaker assignment. Returned only for pre-recorded diarization; not available for streaming
          - `paragraphs` (object, optional)
            - `transcript` (string, optional)
            - `paragraphs` (list of object, optional)
          - `entities` (list of object, optional)
            - `label` (string, optional)
            - `value` (string, optional)
            - `raw_value` (string, optional)
            - `confidence` (float, optional)
            - `start_word` (float, optional)
            - `end_word` (float, optional)
          - `summaries` (list of object, optional)
            - `summary` (string, optional)
            - `start_word` (float, optional)
            - `end_word` (float, optional)
          - `topics` (list of object, optional)
            - `text` (string, optional)
            - `start_word` (float, optional)
            - `end_word` (float, optional)
            - `topics` (list of string, optional)
        - `detected_language` (string, optional)
      - `utterances` (list of object, optional)
        - `start` (float, optional)
        - `end` (float, optional)
        - `confidence` (float, optional)
        - `channel` (integer, optional)
        - `transcript` (string, optional)
        - `words` (list of object, optional)
          - `word` (string, optional)
          - `start` (float, optional)
          - `end` (float, optional)
          - `confidence` (float, optional)
          - `speaker` (integer, optional)
          - `speaker_confidence` (float, optional)
          - `punctuated_word` (string, optional)
        - `speaker` (integer, optional)
        - `id` (string, optional)
      - `summary` (object, optional)
        - `result` (string, optional)
        - `short` (string, optional)
      - `topics` (object, optional) — Output whenever `topics=true` is used
        - `results` (object, optional)
          - `topics` (object, optional)
            - `segments` (list of object, optional)
      - `intents` (object, optional) — Output whenever `intents=true` is used
        - `results` (object, optional)
          - `intents` (object, optional)
            - `segments` (list of object, optional)
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
  - ListenV1AcceptedResponse
    - `request_id` (string, required) — Unique identifier for tracking the asynchronous request

## Examples

**Request**

```json
{
  "url": "https://dpgr.am/spacewalk.wav"
}
```

**Response**

```json
{
  "metadata": {
    "channels": 1,
    "created": "2024-05-12T18:57:13.426Z",
    "duration": 25.933313,
    "intents_info": {
      "input_tokens": 105,
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "output_tokens": 4
    },
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "arch": "nova-2",
        "name": "2-general-nova",
        "version": "2024-01-09.29447"
      }
    },
    "models": [
      "30089e05-99d1-4376-b32e-c263170674af"
    ],
    "request_id": "a847f427-4ad5-4d67-9b95-db801e58251c",
    "sentiment_info": {
      "input_tokens": 105,
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "output_tokens": 105
    },
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33",
    "summary_info": {
      "input_tokens": 95,
      "model_uuid": "67875a7f-c9c4-48a0-aa55-5bdb8a91c34a",
      "output_tokens": 63
    },
    "tags": [
      "test"
    ],
    "topics_info": {
      "input_tokens": 105,
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "output_tokens": 7
    },
    "transaction_key": "deprecated"
  },
  "results": {
    "channels": [
      {
        "alternatives": [
          {
            "confidence": 0.95,
            "entities": [
              {
                "confidence": 0.95,
                "end_word": 3,
                "label": "Event",
                "raw_value": "spacewalk",
                "start_word": 2,
                "value": "spacewalk"
              }
            ],
            "paragraphs": {
              "paragraphs": [
                {
                  "end": 6,
                  "num_words": 12,
                  "sentences": [
                    {
                      "end": 6,
                      "start": 0,
                      "text": "This historic spacewalk marks a significant milestone for women in space exploration."
                    }
                  ],
                  "speaker": 1,
                  "start": 0
                }
              ],
              "transcript": "This historic spacewalk marks a significant milestone for women in space exploration."
            },
            "summaries": [
              {
                "end_word": 12,
                "start_word": 0,
                "summary": "The transcript highlights the importance of the first all-female spacewalk."
              }
            ],
            "topics": [
              {
                "end_word": 12,
                "start_word": 0,
                "text": "This historic spacewalk marks a significant milestone for women in space exploration.",
                "topics": [
                  "Space Exploration"
                ]
              }
            ],
            "transcript": "This historic spacewalk marks a significant milestone for women in space exploration.",
            "words": [
              {
                "confidence": 0.98,
                "end": 0.3,
                "start": 0,
                "word": "This"
              },
              {
                "confidence": 0.97,
                "end": 0.7,
                "start": 0.3,
                "word": "historic"
              },
              {
                "confidence": 0.99,
                "end": 5.8,
                "start": 5.2,
                "word": "spacewalk"
              }
            ]
          }
        ],
        "detected_language": "en",
        "search": [
          {
            "hits": [
              {
                "confidence": 0.98,
                "end": 5.8,
                "snippet": "the first all-female spacewalk",
                "start": 5.2
              }
            ],
            "query": "spacewalk"
          }
        ]
      }
    ],
    "intents": {
      "results": {
        "intents": {
          "segments": [
            {
              "end_word": 414,
              "intents": [
                {
                  "confidence_score": 0.0038975573,
                  "intent": "Encourage podcasting"
                }
              ],
              "start_word": 354,
              "text": "If you found this valuable, you can subscribe to the show on spotify or your favorite podcast app."
            }
          ]
        }
      }
    },
    "sentiments": {
      "average": {
        "sentiment": "positive",
        "sentiment_score": 0.5810185185185185
      },
      "segments": [
        {
          "end_word": 69,
          "sentiment": "positive",
          "sentiment_score": 0.5810546875,
          "start_word": 0,
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal. And, um, I think if it_signf"
        }
      ]
    },
    "summary": {
      "result": "success",
      "short": "Speaker 1 highlights the historic significance of the first all-female spacewalk as a milestone for women in space exploration."
    },
    "topics": {
      "results": {
        "topics": {
          "segments": [
            {
              "end_word": 69,
              "start_word": 32,
              "text": "And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
              "topics": [
                {
                  "confidence_score": 0.91581345,
                  "topic": "Spacewalk"
                }
              ]
            }
          ]
        }
      }
    },
    "utterances": [
      {
        "channel": 1,
        "confidence": 0.95,
        "end": 6,
        "id": "utt-001",
        "speaker": 1,
        "start": 0,
        "transcript": "This historic spacewalk marks a significant milestone for women in space exploration.",
        "words": [
          {
            "confidence": 0.98,
            "end": 0.3,
            "punctuated_word": "This",
            "speaker": 1,
            "speaker_confidence": 0.99,
            "start": 0,
            "word": "This"
          },
          {
            "confidence": 0.97,
            "end": 0.7,
            "punctuated_word": "historic",
            "speaker": 1,
            "speaker_confidence": 0.99,
            "start": 0.3,
            "word": "historic"
          },
          {
            "confidence": 0.99,
            "end": 5.8,
            "punctuated_word": "spacewalk.",
            "speaker": 1,
            "speaker_confidence": 0.99,
            "start": 5.2,
            "word": "spacewalk"
          }
        ]
      }
    ]
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/listen"

payload = { "url": "https://dpgr.am/spacewalk.wav" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/listen';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"url":"https://dpgr.am/spacewalk.wav"}'
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

	url := "https://api.deepgram.com/v1/listen"

	payload := strings.NewReader("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")

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

url = URI("https://api.deepgram.com/v1/listen")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/listen")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/listen', [
  'body' => '{
  "url": "https://dpgr.am/spacewalk.wav"
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

var client = new RestClient("https://api.deepgram.com/v1/listen");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["url": "https://dpgr.am/spacewalk.wav"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/listen")! as URL,
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
